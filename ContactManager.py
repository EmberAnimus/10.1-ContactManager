import PySide6
from ui_main import Ui_Widget
import sys, pandas as pd, os
import pycountry
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog
from PySide6.QtCore import QAbstractTableModel, Qt

currentDir = os.curdir
contacts = []

class TableModel(QAbstractTableModel): 
    #Sets a TableModel Class. This is neccessary to work with a TableView in QT. 
    #The reason it is neccessary is because QAbstractTableModel and its subclasses don't do anything inherently in the QT library. 
    #You have to manually sub-class it and define what it does. 
    #In this case it combines QT and Pandas to allow me to easily and dynamically define tables for the TableViews in my UI files. 
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        #This identifies the data table from the Coloumn and Index headers in the DataFrame.
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        #Gets the number of rows
        return self._data.shape[0]

    def columnCount(self, index):
        #Gets the number of columns
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        #This checks the headerData to get the defined Headers. This identified in the DataFrame.
        #Column is the Column Headers of course, while Index is the Row Headers. By using DataFrames it provides readability and simplicity.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

class ui_main(QMainWindow):
    #Initalizes the UI from the ui_main file, and sets any connections.
    def __init__(self):
        super(ui_main, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.file_prompt()
        self.set_countries()

        self.ui.pushButtonChange.clicked.connect(self.file_prompt)
        self.ui.pushButtonClear.clicked.connect(self.clear_fields)
        self.ui.pushButtonQuit.clicked.connect(self.exit)
        self.ui.pushButtonDelete.clicked.connect(self.delete)
        self.ui.pushButtonSubmit.clicked.connect(self.add_Contact)
        self.ui.comboBoxCountry.currentTextChanged.connect(self.get_regions)


    def set_countries(self):
        names = []
        for country in pycountry.countries:
            names.append(country.name)
        names.sort()
        self.ui.comboBoxCountry.insertItems(0,names)
        return 
    
    def get_regions(self):
        country = self.ui.comboBoxCountry.currentText()
        country = pycountry.countries.get(name=country).alpha_2
        regions = []
        for region in pycountry.subdivisions.get(country_code=country):
            regions.append(region.name)
        regions.sort()
        
        self.ui.comboBoxState.clear()
        self.ui.comboBoxState.insertItems(0,regions)
        return

    def add_Contact(self):
        name = self.ui.lineEditName.text()
        phNumber = self.ui.lineEditNum.text()
        street = self.ui.lineEdit.text()
        city = self.ui.lineEditCity.text()
        region = self.ui.comboBoxState.currentText()
        country = self.ui.comboBoxCountry.currentText()

        contacts.append([name,phNumber,street,city,region,country])
        self.update_model()
        pass

    def write_to_file(self):
        dir = self.ui.labelFileDir.text()
        dataFrame = pd.DataFrame(contacts, columns=["Name", "Phone Number", "Street", "City", "State", "Country"])
        dataFrame.to_csv(dir)
        return

    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.lineEditName.clear()
        self.ui.lineEditNum.clear()
        self.ui.lineEditCity.clear()
        self.ui.comboBoxState.clear()
        pass


    def update_model(self):
        contactsView = self.ui.tableViewContacts
        contactsModel = pd.DataFrame(contacts, columns=["Name", "Phone Number", "Street", "City", "State", "Country"])
        contactsView.model = TableModel(contactsModel)
        contactsView.setModel(contactsView.model)

    def read_file(self, dir):
        try:
            file = open(dir, "r")
        except FileNotFoundError:
            file = open(dir,"w")
            file.close()
            file = open(dir, "r")
        try:
            dataFrame = pd.read_csv(file)
            for i in dataFrame.values.tolist():
                contacts.append(i[1:])
        except:
            pass
        file.close()
        return
    
    def file_prompt(self):
        choice = QMessageBox(self)
        choice.setWindowTitle("Open Contacts")
        choice.setText("Do you want to open an existing file or create new")
        existingBtn = choice.addButton("Existing",QMessageBox.RejectRole)
        newBtn = choice.addButton("New",QMessageBox.AcceptRole)
        choice.exec()

        if choice.clickedButton() == existingBtn:
            dir = QFileDialog.getOpenFileName(self, "Open Contacts", currentDir, "CSV (*.csv)")[0]
            
            
        elif choice.clickedButton() == newBtn:
            name = QInputDialog(self)
            name.setWindowTitle("File Name")
            name.setLabelText("What is the name of the file?")
            name.exec()
            name_input = name.textValue().strip()
        
            dir = f'{QFileDialog.getExistingDirectory(self, "File Directory", currentDir)}/{name_input}.csv'
            
        
        else:
            pass

        self.read_file(dir)
        self.update_model()

        self.ui.labelFileDir.setText(dir)
        
        return

    def delete(self):
        try: #Attempts to remove a vehicle from the model. We fetch selected rows, get the row index, then remove it from the garage. We refresh the view.
            contactsView = self.ui.tableViewContacts
            selRow = contactsView.selectionModel().selectedRows()
            index = selRow[0].row()
            contacts.pop(index)
            self.update_model()
        except: #Abort function on fail. This is usually because the model is empty, or because a row isn't selected.
            return        
        return

    def exit(self):
        self.write_to_file()
        app.exit()

if __name__ == "__main__": #Load the app if this is the main module.
    app = QApplication(sys.argv)
    window = ui_main()
    window.show()    

    sys.exit(app.exec())