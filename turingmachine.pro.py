# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Signal as pyqtSignal, QObject,Qt, QMetaObject
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox, QTableWidgetItem, QComboBox, QPushButton, QLabel, QVBoxLayout
from ui_license_import import Ui_EnterLicense
from ui_form import Ui_Widget
import requests
import webbrowser
import uuid
import os, json, threading
import time


def create_uid():
    uid = uuid.uuid4()


session = requests
baseurl = "https://turingmachine.pro/api"
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



class UpdateChecker(QObject):
    update_check_finished = pyqtSignal(bool, str, str)

    def __init__(self, update_url):
        super().__init__()
        self.update_url = update_url

    def check_for_update(self):
        try:
            response = requests.get(self.update_url)
            if response.status_code == 200:
                update_info = response.json()
                current_version = update_info.get('current_version')
                latest_version = update_info.get('latest_version')
                update_available = update_info.get('update_available')
                download_url = update_info.get('download_url')

                if update_available:
                    message = f"Update available!\nCurrent Version: {current_version}\nLatest Version: {latest_version}"
                    self.update_check_finished.emit(True, message, download_url)
                else:
                    self.update_check_finished.emit(False, "No updates available.", "")
            else:
                self.update_check_finished.emit(False, "Failed to check for updates.", "")
        except Exception as e:
            self.update_check_finished.emit(False, f"Error: {str(e)}")

def show_update_message(update_available, message, download_url):
    print(message)
    print(download_url)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle("Update Available")

    if update_available:
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Ok)

        result = msg_box.exec_()

        if result == QMessageBox.Ok:
            webbrowser.open(download_url, new=2)


class MyMessageBox(QMessageBox):
    def __init__(self, communicator, app, result, license_input):
        super().__init__()
        self.license_input = license_input
        self.setWindowTitle("Message Box with Link")
        self.setText(result["message"])

        self.communicator = communicator

        if "license" in result and "heartbeat" in result["message"]:
            self.renew_link = f'https://turingmachine.pro/api/renewLicense?license={result["license"]}'
            self.setText(result["message"] + " Please renew it")
            self.buttonClicked.connect(self.renew_license)
        else:
            self.buttonClicked.connect(self.reenter_license)
            # pass

    def renew_license(self):
        webbrowser.open(self.renew_link, new=2)

    def reenter_license(self):
        self.hide()
        self.license_input.exec()


class LicenseInput(QDialog):
    def __init__(self, communicator, parent):
        super().__init__()
        self.ui = Ui_EnterLicense()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.thread_on_ok_button_clicked)
        self.ui.buttonBox.rejected.connect(sys.exit)
        self.ui.buy.clicked.connect(self.buy_now)
        self.communicator = communicator
        self.parent = parent
        self.data = read_or_create_config_file()
        self.internet_connector = Communicator()
        self.internet_connector.signal.connect(self.show_message)
        self.stop_progress = False
    
    def closeEvent(self, event):
        print("exiting")
        sys.exit()

    def show_message(self, response):
        result = response["result"]
        if result:
            self.accept()
        else:
            error_message = MyMessageBox(self.communicator, self.app, response, self)
            error_message.setStandardButtons(QMessageBox.StandardButton.Ok)
            error_message.setIcon(QMessageBox.Icon.Critical)
            error_message.setWindowTitle('Error')
            error_message.exec()
            self.reject()

    def thread_on_ok_button_clicked(self):
        thread = threading.Thread(target=self.on_ok_button_clicked)
        thread.start()
        self.progress_bar.show()
    

    def on_ok_button_clicked(self):
        l = self.ui.license_input.text()
        if " " in l:
            self.communicator.signal.emit({"result": False})
            self.internet_connector.signal.emit({"result": False, "message": "Wrong License format"})
            return
        machine_id = self.data["uid"]
        response = json.loads(session.get(baseurl + f"/days?license={l}&machineId={machine_id}").text)
        if "days" in response and response["days"] is not None and response["days"] >= 0:
            self.data["license"] = l
            self.data["days"] = response["days"]
            self.data["machineId"] = machine_id
            self.communicator.signal.emit({"result": True, "data": self.data})
            with open(filename, 'w') as file:
                json.dump(self.data, file)
            self.internet_connector.signal.emit({"result": True})
        else:
            self.communicator.signal.emit({"result": False})
            response["license"] = l
            if "days" in response and response["days"] is not None and response["days"] < 0:
                response["message"] = "The license has expired."
            self.internet_connector.signal.emit(
                {"result": False, "message": response["message"], "license": response["license"]})
        self.stop_progress = True

    def buy_now(self):
        webbrowser.open("https://turingmachine.pro/buy", new=2)


class Widget(QWidget):
    def __init__(self, app, communicator, parent=None):
        super().__init__(parent)
        version='v1.0.0'
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Example usage
        update_url = "https://turingmachine.pro/api/update?version="+version
        update_checker = UpdateChecker(update_url)
        update_checker.update_check_finished.connect(show_update_message)

        # Trigger the update check
        update_thread = threading.Thread(target=update_checker.check_for_update)
        update_thread.start()

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
        self.ping_thread = threading.Thread(target=self.periodic_ping)
        self.ping_thread.daemon = True
        self.should_ping = True
        self.uid = None
        data = read_or_create_config_file()
        self.license_input = LicenseInput(communicator, self)
        if "license" not in data:
            self.license_input.exec()
        else:
            thread = threading.Thread(target=read_saved_license, args=(data,))
            thread.start()
    
    
    def periodic_ping(self):
        while self.should_ping:
            self.ping_keygen()
            time.sleep(3600)
    
    def ping_keygen(self):
        account_id = "ea0d5c4f-12a0-4870-aa52-bcf7508003e9"
        url = f'https://api.keygen.sh/v1/accounts/{account_id}/machines/{self.uid}/actions/ping'
        print("Ping successfull")

        headers = {
            "Accept": "application/vnd.api+json",
            "Authorization": f"License {self.license}"
        }

        requests.post(url, headers=headers)
        


    def convert_to_format(self):
        transition_rules = {}
        for row in range(self.ui.transition_rules.rowCount()):
            state = self.ui.transition_rules.cellWidget(row, 1).currentText()
            symbol = self.ui.transition_rules.item(row, 2).text() if self.ui.transition_rules.item(row, 2) else ""
            if symbol == "":
                transition_rules["error"]="Error in line {}. the symbol I read cannot be empty.".format((row+1))
            new_state = self.ui.transition_rules.cellWidget(row, 3).currentText()
            write_symbol = self.ui.transition_rules.item(row, 4).text() if self.ui.transition_rules.item(row, 4) else ""
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
        self.ui.newState.setText("")
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
            self.ui.result_box.setStyleSheet("")
            self.ui.result_box.setText("Loading...")
            thread = threading.Thread(target=self.run_background)
            thread.start()


    def run_background(self):
        states=[self.ui.states.item(i).text() for i in range(self.ui.states.count())]
        if not states:
            self.result_connector.signal.emit({"error": "You need to enter at least on state for the machine to process"})
            return
        tape = self.ui.tape.text()
        if not tape:
            self.result_connector.signal.emit({"error": "You need to enter a tape"})
            return
        transition_rules = self.convert_to_format()
        if "error" in transition_rules:
            self.result_connector.signal.emit({"error": transition_rules["error"]})
            return
        headers = {
            'machineId': self.uid,
            'license': self.license,
            'Content-Type': 'application/json'
        }
        data = {
            'States': states,
            'tape': tape,
            'transitionRules': transition_rules
        }
        try:
            response = requests.post(f"{baseurl}/turing", headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            self.result_connector.signal.emit(response.json())  # Assuming the response is in JSON format
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            self.result_connector.signal.emit({"error": e})


    def show_result(self, response):
        if "error" in response:
            self.ui.result_box.setStyleSheet("color: red")
            self.ui.result_box.setText("Error: "+str(response["error"]))

            return
        final_state = response['final_state']
        final_symbol = response['final_symbol']
        result_code = response['result']
        final_tape = response['tape']
        if result_code == "1":
            self.ui.result_box.setText("The Turing machine accepted your tape.\nThe tape, after being processed is: {}".format("".join(final_tape)))  # Set your desired text
            self.ui.result_box.setStyleSheet("color: green")
        elif result_code == "-1":
            self.ui.result_box.setText("The Turing machine discarded your tape.\nThe tape, after being processed is: {}".format("".join(final_tape)))  # Set your desired text
            self.ui.result_box.setStyleSheet("color: purple")
        else:
            self.ui.result_box.setText("Undefined transition for state: {}, symbol: {}. The tape that has been returned is: {}".format(final_state, final_symbol, "".join(final_tape)))
            self.ui.result_box.setStyleSheet("color: yellow")

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
        link=f"/renewLicense?license={self.license}&quantity={self.ui.monthsQuantity.value()}"
        webbrowser.open(baseurl+link, new=2)


    def set_credentials(self, result):
        if result["result"]:
            self.license = result["data"]["license"]
            self.uid = result["data"]["uid"]
            # self.ping_thread.start()
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
    
    
    def check_app_updates(self):
        pass


class Communicator(QObject):
    signal = pyqtSignal(dict)


def read_saved_license(data):
    license = data["license"]
    machine_id = data["uid"]
    server_response=session.get(baseurl+f"/days?license={license}&machineId={machine_id}").text
    print(server_response)
    response = json.loads(server_response)
    data["days"] = response["days"]
    with open(filename, 'w') as file:
        json.dump(data, file)
    communicator.signal.emit({"result":True, "data":data})

if __name__ == "__main__":


    app = QApplication(sys.argv)
    communicator = Communicator()
    main_window = Widget(app, communicator)
    main_window.show()
    system_status = app.exec()
    if main_window.uid is not None:
        account_id = "ea0d5c4f-12a0-4870-aa52-bcf7508003e9"
        res = requests.delete(
        f"https://api.keygen.sh/v1/accounts/{account_id}/machines/{main_window.uid}",
            headers={
                "Accept": "application/vnd.api+json",
                "Authorization": f"License {main_window.license}"
            }
        )
    sys.exit()

