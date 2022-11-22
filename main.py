import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QCheckBox
from PySide6.QtCore import QThread, Signal
from design import Ui_MainWindow
from telethon.sync import TelegramClient
from telethon.errors import rpcerrorlist
from multiprocessing import Manager
import socks
import schedule
from time import sleep
from typing import Union
from PySide6 import QtGui
import csv
import json


class Session(QThread):
    answer = Signal(str, bool, str, str)
    getting = Signal(str, dict)

    def __init__(self, name, session):
        super(Session, self).__init__()
        self.name = name
        self.session = session
        self.connected = False
        self.client = None

    def run(self) -> None:
        self.getting.connect(self.get_target)

    def __del__(self):
        self.wait()

    def get_target(self, name, values):
        print('get')
        if name == 'connect':
            connected, text = self.connecting()
            self.answer.emit(self.name, connected, name, text)

    def connecting(self):
        try:
            session = self.session
            data = self.session.get('data', {})
            self.client = TelegramClient(session['session_path'], api_id=data.get('app_id'),
                                         api_hash=data.get('app_hash'),
                                         proxy=(socks.SOCKS5, session.get('addr'), int(session.get('port')), True,
                                                session.get('login'), session.get('pass')))

            sleep(10)
            self.client.connect()
            print('start connecting...')
            if self.client.is_user_authorized():
                print(f'{self.name} is authorized')
                self.connected = True
                return True, 'success'
            else:
                return False, f'{self.name}  is not authorized or banned'
        except rpcerrorlist.AuthKeyDuplicatedError:
            return False, f'session {self.name} file timeout'
        except BaseException as e:
            return False, f'other error {e}'


class Telegrammer(QMainWindow):
    def __init__(self):
        self.setting = {
            "sessions": {}
        }

        self.processes = {}

        super(Telegrammer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if 'setting.json' in os.listdir():
            self.read()
        else:
            self.write()

        self.ui.drop_proxy.setAcceptDrops(True)
        self.ui.drop_sessions.setAcceptDrops(True)
        self.ui.drop_proxy.dragEnterEvent = self.dragEnterEvent
        self.ui.drop_sessions.dragEnterEvent = self.dragEnterEvent

        self.ui.drop_proxy.dropEvent = lambda event: self.dropEvent(event, 'proxy')
        self.ui.drop_sessions.dropEvent = lambda event: self.dropEvent(event, 'session')

        self.ui.table_sessions.setColumnCount(9)
        self.ui.table_sessions.setHorizontalHeaderLabels(
            ['Name', 'session', 'json', 'admin', 'addr', 'port', 'login', 'pass', 'delete'])
        self.ui.table_sessions.append = lambda x: self.append(x)
        self.count_dot = 0
        self.waiting = False

        self.ui.btn_connect.clicked.connect(self.sessions_connect)

        if self.setting.get('sessions') is None:
            self.setting['sessions'] = {}

        self.write()

    def answer(self, session: str, result: bool, name: str, text: str):
        print(session, result, name, text)
        if result:
            self.colored_table_sessions(list(self.setting.get('sessions', {}).keys()).index(session), (0, 255, 0))
        else:
            self.colored_table_sessions(list(self.setting.get('sessions', {}).keys()).index(session), (255, 0, 0))

    def admined(self) -> None:
        btn = self.sender()
        name = btn.name
        session = self.setting['sessions'].get(name)
        if not session:
            return
        self.setting['sessions'][name]['admin'] = self.sender().isChecked()
        self.write()

    def delete(self) -> None:
        btn = self.sender()
        name = btn.name
        session = self.setting['sessions'].get(name)
        if session is None:
            return
        del self.setting['sessions'][name]
        self.write()

    def append(self, row: list) -> None:
        rowPosition = self.ui.table_sessions.rowCount()
        self.ui.table_sessions.insertRow(rowPosition)

        for n, i in enumerate(row):
            self.ui.table_sessions.setItem(rowPosition, n, QTableWidgetItem(str(i)))

        del_button: QPushButton = QPushButton(self, 'delete')
        del_button.name = row[0]
        del_button.clicked.connect(self.delete)

        admin_btn: QCheckBox = QCheckBox(self)
        admin_btn.setChecked(bool(row[3]))
        admin_btn.name = row[0]
        admin_btn.clicked.connect(self.admined)

        self.ui.table_sessions.setItem(rowPosition, 3, QTableWidgetItem(''))
        self.ui.table_sessions.setCellWidget(rowPosition, 3, admin_btn)
        self.ui.table_sessions.setCellWidget(rowPosition, 8, del_button)

    def sessions_connect(self):
        ses: dict = self.setting.get('sessions', {})
        sessions: list = list(filter(
            lambda x: False not in [ses[x].get('data', False), ses[x].get('addr', False), ses[x].get('port', False),
                                    ses[x].get('login', False),
                                    ses[x].get('pass', False), ], self.setting.get('sessions', {})))
        self.ui.out_concole.setText('>>> Connecting...')
        self.ui.out_concole.setStyleSheet('background-color:  rgb(0, 0, 0);color: rgb(255, 255, 255)')
        for i in sessions:
            if i not in self.processes:
                self.processes[i] = Session(i, self.setting.get('sessions', {}).get(i, {}))
                self.processes[i].answer.connect(self.answer)
                self.processes[i].start()
            self.processes[i].getting.emit('connect', None)
            self.colored_table_sessions(list(ses.keys()).index(i), (255, 255, 0))

    def colored_table_sessions(self, x: int, color: tuple):
        self.ui.table_sessions.item(x, 1).setBackground(QtGui.QColor(*color))

    def write(self):
        self.tab_update()
        with open('setting.json', 'w') as f:
            json.dump(self.setting, f, indent=4)

    def read(self):
        with open('setting.json', 'r') as f:
            self.setting = json.load(f)

    def tab_update(self):
        self.ui.table_sessions.clear()
        self.ui.table_sessions.setRowCount(0)
        self.ui.table_sessions.setHorizontalHeaderLabels(
            ['Name', 'session', 'json', 'admin', 'addr', 'port', 'login', 'pass', 'delete'])
        sessions = self.setting.get('sessions', {})
        for i in sessions:
            obj: dict = sessions.get(i, {})
            self.ui.table_sessions.append(
                [i, not not obj.get('session_path'), not not obj.get('data'), not not obj.get('admin'), obj.get('addr'),
                 obj.get('port'), obj.get('login'), obj.get('pass')])
        self.waiting = True

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event, type: str) -> None:
        if type == 'session':
            files = [u for u in event.mimeData().urls()]
            for f in files:
                name, file_t = f.fileName().split('.')
                if name not in self.setting.get('sessions', {}):
                    self.setting['sessions'][name] = {}
                if file_t == 'json':
                    self.setting['sessions'][name]['data'] = json.load(open(f.toLocalFile(), 'r', encoding='utf8'))
                elif file_t == 'session':
                    self.setting['sessions'][name]['session_path'] = f.toLocalFile()
                    # print(f.path())
                # print(f'{type} ::: {f.toLocalFile()}')
        elif type == 'proxy':
            proxys = []
            files = [u for u in event.mimeData().urls()]
            for f in files:
                with open(f.toLocalFile(), 'r') as f:
                    reader = csv.reader(f, delimiter=':')
                    for i in reader:
                        if list(i) not in proxys:
                            proxys.append(list(i))
            sessions: dict = self.setting.get('sessions', {})
            ln_proxy = len(proxys)
            n_proxy = 0
            for i in sessions:
                if ln_proxy == n_proxy:
                    break
                obj = sessions[i]
                if not obj.get('addr'):
                    addr, port, login, pas = proxys[n_proxy]
                    obj['addr'] = addr
                    obj['port'] = port
                    obj['login'] = login
                    obj['pass'] = pas
                    n_proxy += 1
        self.write()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Telegrammer()
    window.show()
    sys.exit(app.exec())
