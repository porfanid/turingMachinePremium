# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Signal as pyqtSignal, QObject,Qt
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QTableWidgetItem, QComboBox, QPushButton
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_license_import import Ui_EnterLicense
from ui_form import Ui_Widget
import requests
import webbrowser
import uuid
import os, json, threading


def create_uid():
    uid = uuid.uuid4()


session = requests
baseurl = "https://app.turingmachine.pro"
# baseurl="http://127.0.0.1:5000"
filename="./config.json"


def read_or_create_config_file(data={"uid":str(uuid.uuid4())}):

    # Check if the config file exists
    if os.path.exists(filename):
        # If the file exists, read data from it
        with open(filename, 'r') as file:
            try:
                config_data = json.load(file)
                return config_data
            except json.JSONDecodeError:
                with open(filename, 'w') as file:
                    json.dump(data, file, indent=2)
    else:
        # If the file does not exist, create it and add data
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
            return data


class LicenseInput(QDialog):
    def __init__(self, communicator, parent=None):
        super().__init__()
        self.ui = Ui_EnterLicense()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.thread_on_ok_button_clicked)
        self.ui.buy.clicked.connect(self.buy_now)
        self.communicator = communicator
        self.data = read_or_create_config_file()
        self.internet_connector = Communicator()
        self.internet_connector.signal.connect(self.show_message)

    def show_message(self, response):
        
        result = response["result"]
        if result:
            self.accept()
        else:
            error_message = QMessageBox(self)
            error_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText('An error occurred!\n'+response["message"])
            # Show the error message
            error_message.exec()
            self.reject()


    def thread_on_ok_button_clicked(self):
        thread = threading.Thread(target=self.on_ok_button_clicked)
        thread.start()

    def on_ok_button_clicked(self):
        l = self.ui.license_input.text()
        machine_id = self.data["uid"]
        response = json.loads(session.get(baseurl+f"/days?license={l}&machineId={machine_id}").text)
        if "days" in response and response["days"] is not None and response["days"]>0:
            self.data["license"] = l
            self.data["days"]  = response["days"]
            self.communicator.signal.emit({"result":True, "data":self.data})
            with open(filename, 'w') as file:
                json.dump(self.data, file)
            self.internet_connector.signal.emit({"result":True})
        else:
            self.communicator.signal.emit({"result":False})
            self.internet_connector.signal.emit({"result":False, "message": response["message"]})


    def buy_now(self):
        webbrowser.open(baseurl+"/", new=2)


class Widget(QWidget):
    def __init__(self, communicator, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.communicator = communicator
        self.communicator.signal.connect(self.set_credentials)
        self.hasLoaded = False
        self.state_options = []  # Variable to store state options
        
        self.ui.run.clicked.connect(self.run)

        self.ui.addState.clicked.connect(self.addNewState)
        self.ui.add_transition_rule_button.clicked.connect(self.add_row)
        self.ui.states.itemEntered.connect(self.update_rows)
        self.ui.renewLicense.clicked.connect(self.renew_license)
        self.result_connector = Communicator()
        self.result_connector.signal.connect(self.show_result)


    def convert_to_format(self):
        transition_rules = {}
        for row in range(self.ui.transition_rules.rowCount()):
            state = self.ui.transition_rules.cellWidget(row, 1).currentText()
            symbol = self.ui.transition_rules.item(row, 2).text()
            new_state = self.ui.transition_rules.cellWidget(row, 3).currentText()
            write_symbol = self.ui.transition_rules.item(row, 4).text()
            move_direction = "L" if self.ui.transition_rules.cellWidget(row, 5).currentText() == "LEFT" else "R"

            key = f"({state}, {symbol})"
            value = (new_state, write_symbol, move_direction)

            transition_rules[key] = value
        return transition_rules


    def add_row(self):
        row_position = self.ui.transition_rules.rowCount()
        self.ui.transition_rules.insertRow(row_position)

        delete_button = QPushButton("Delete", self)
        delete_button.clicked.connect(lambda: self.ui.transition_rules.removeRow(self.ui.transition_rules.indexAt(delete_button.pos()).row()))
        self.ui.transition_rules.setCellWidget(row_position, 0, delete_button)

        for col in range(1, 4):
            item = QTableWidgetItem()
            self.ui.transition_rules.setItem(row_position, col, item)

        move_direction_combo = QComboBox()
        move_direction_combo.addItems(["LEFT", "RIGHT"])
        self.ui.transition_rules.setCellWidget(row_position, 5, move_direction_combo)

        # Automatically populate the next state column (column 4) with items from state_options
        next_state_combo = QComboBox()
        next_state_combo.addItems(self.state_options)
        self.ui.transition_rules.setCellWidget(row_position, 3, next_state_combo)

        current_state_combo = QComboBox()
        current_state_combo.addItems(self.state_options)
        self.ui.transition_rules.setCellWidget(row_position, 1, current_state_combo)


    def update_rows(self):
        # Update state_options with the current items in the QListWidget
        self.state_options = [self.ui.states.item(index).text() for index in range(self.ui.states.count())]

        # Update all rows in the QTableWidget with the updated state_options
        for row in range(self.ui.transition_rules.rowCount()):
            next_state_combo = QComboBox()
            next_state_combo.addItems(self.state_options)
            self.ui.transition_rules.setCellWidget(row, 3, next_state_combo)

            current_state_combo = QComboBox()
            current_state_combo.addItems(self.state_options)
            self.ui.transition_rules.setCellWidget(row, 1, current_state_combo)


    def addNewState(self):
        newState = self.ui.newState.text()
        self.ui.states.addItem(newState)
        self.update_rows()  # Call update_rows after adding a new state


    def run(self):
        if not self.hasLoaded:
            error_message = QMessageBox(self)
            error_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText("Please wait until the application has fully loaded.\n\nYou will see your info on the bottom left corner of the screen when the app is ready")
            # Show the error message
            error_message.exec()
            return None
        else:
            thread = threading.Thread(target=self.run_background)
            thread.start()


    def run_background(self):
        headers = {
            'machineId': self.uid,
            'license': self.license,
            'Content-Type': 'application/json'
        }
        data = {
            'States': [self.ui.states.item(i).text() for i in range(self.ui.states.count())],
            'tape': self.ui.tape.text(),
            'transitionRules': self.convert_to_format()
        }
        try:
            response = requests.post(f"{baseurl}/turing", headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            self.result_connector.signal.emit(response.json())  # Assuming the response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            self.result_connector.signal.emit(None)


    def show_result(self, response):
        print(response)


    def renew_license(self):
        if not self.hasLoaded:
            error_message = QMessageBox(self)
            error_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.setWindowTitle('Error')
            error_message.setText("Please wait until the application has fully loaded.\n\nYou will see your info on the bottom left corner of the screen when the app is ready")
            # Show the error message
            error_message.exec()
            return None
        link="/renewLicense?license="+self.license
        webbrowser.open(baseurl+link, new=2)


    def set_credentials(self, result):
        if result["result"]:
            self.license = result["data"]["license"]
            self.uid = result["data"]["uid"]
            self.ui.license.setText(result["data"]["license"])
            self.ui.days.setText(str(result["data"]["days"]) + " days")

            error_message = QMessageBox(self)
            error_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_message.setIcon(QMessageBox.Icon.Information)
            error_message.setWindowTitle('Loaded')
            error_message.setText("The application has fully loaded. You can now use it")
            # Show the error message
            error_message.exec()
            self.hasLoaded = True
        else:
            print(result)


class Communicator(QObject):
    signal = pyqtSignal(dict)


def read_saved_license(data):
    license = data["license"]
    machine_id = data["uid"]
    server_response=session.get(baseurl+f"/days?license={license}&machineId={machine_id}").text
    response = json.loads(server_response)
    data["days"] = response["days"]
    with open(filename, 'w') as file:
        json.dump(data, file)
    communicator.signal.emit({"result":True, "data":data})

if __name__ == "__main__":
    app = QApplication(sys.argv)
    communicator = Communicator()
    main_window = Widget(communicator)
    main_window.show()
    thread=None
    data = read_or_create_config_file()
    if "license" not in data:
        license_input = LicenseInput(communicator, main_window)
        license_input.show()
    else:
        thread = threading.Thread(target=read_saved_license, args=(data,))
        thread.start()
    sys.exit(app.exec())

