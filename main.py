import sys
import logics
import re
import ast
from PySide6.QtWidgets import QApplication, QWidget,QFileDialog,QInputDialog
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.load_cap_csv.clicked.connect(self.cap_csv_fun)
        self.ui.load_rma_csv.clicked.connect(self.rma_csv_fun)
        self.ui.assign_cap_csv.clicked.connect(self.assign_cap_logins)
        self.ui.assign_rma_csv.clicked.connect(self.assign_rma_logins)
        self.ui.gen_logins.clicked.connect(self.find_eligible_logins)

    prepd_file = "Prepared CSV file is saved in prepd Folder"

    def cap_csv_fun(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # Allow selecting existing files only
        file_dialog.setNameFilter("Text files (*.csv);;All files (*)")  # Filter by file extension
        file_dialog.setViewMode(QFileDialog.List)
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            print(f"Selected file: {selected_file}")
            cap_file_ret= logics.cap_prep(selected_file)
            cap_file_data = cap_file_ret.split(":")
            self.ui.cap_csv_data.setText(f"Original count : {cap_file_data[0]}\nCount post dup. remove : {cap_file_data[1]}\nPrepared cap count : {cap_file_data[2]}\nHours of Work (23 IPH) : {round(int(cap_file_data[2])/23,2)} hours\n{self.prepd_file}")            
        else:
            print("No file selected.")    

    def rma_csv_fun(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile) 
        file_dialog.setNameFilter("Text files (*.txt);;All files (*)")
        file_dialog.setViewMode(QFileDialog.List)
        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            print(f"Selected file: {selected_file}")
            rma_file_ret= logics.rma_prep(selected_file)
            rma_file_data = rma_file_ret.split(":")
            self.ui.rma_csv_data.setText(f"Original count : {rma_file_data[0]}\nCount post dup. remove : {rma_file_data[1]}\nPrepared rma count : {rma_file_data[2]}\nHours of Work (23 IPH) : {round(int(rma_file_data[2])/23,2)} hours\n{self.prepd_file}") 
        else:
            print("No file selected.")

    def assign_cap_logins(self):
        cap_logins, ok = QInputDialog.getText(self, "Input Dialog", "Enter the logins:")
        if ok and cap_logins:
            print(f"User entered: {cap_logins}")
            investc= [x for x in cap_logins.split(",")]
            text= logics.cap_assign(investc)
            formattedtext = text.split("|")
            parsed_list = ast.literal_eval(formattedtext[1])
            formatted_second_part = "\n".join(parsed_list)
            print(text)
            self.ui.cap_assign_csv.setText(f"Total Login = {formattedtext[0]} \n Login  :  Case Count  : Hours assigned \n {formatted_second_part} ")
            # self.ui.cap_assign_csv.setText(text)
        else:
            print("User cancelled or didn't enter text.")

    def assign_rma_logins(self):
        rma_logins, ok = QInputDialog.getText(self, "Input Dialog", "Enter the logins:")
        investr = [x for x in rma_logins.split(",")]
        if ok and rma_logins:
            print(f"User entered: {rma_logins}")
            text= logics.rma_assign(investr)
            formattedtext = text.split("|")
            parsed_list = ast.literal_eval(formattedtext[1])
            formatted_second_part = "\n".join(parsed_list)
            print(text)
            self.ui.rma_assign_csv.setText(f"Total Login = {formattedtext[0]} \n Login  :  Case Count  : Hours assigned \n {formatted_second_part} ")
            #self.ui.rma_assign_csv.setText(text)
        else:
            print("User cancelled or didn't enter text.")

    def find_eligible_logins(self):
        l=[]
        t_1l=re.split(r'[,\s/]+',self.ui.t_1_logins.toPlainText())
        t_2l=re.split(r'[,\s/]+',self.ui.t_2_logins.toPlainText())
        present_logins= re.split(r'[,\s/]+',self.ui.present_logins.toPlainText())
    
        for x in present_logins :
            if x not in t_1l  and x not in t_2l:
                l.append(x)

        self.ui.eligible_logins.setText((",").join(l))
            
        



def main():
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())


if __name__=="__main__":
    main()