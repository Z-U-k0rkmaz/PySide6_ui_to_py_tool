import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from form import Ui_MainWindow

import subprocess
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("UI to PY Converter")
        self.setFixedSize(543, 203)
        
        self.file_path = ''
        self.file_name = ''
        self.file_directory = ''
        
        
        self.ui.BtnConvert.clicked.connect(self.convert)
        self.ui.BtnSelectFile.clicked.connect(self.select_file)
        self.ui.BtnSelectDestinationFolder.clicked.connect(self.select_folder)
        self.ui.BtnExit.clicked.connect(self.exit)
    
      
    def convert(self):
        self.ui.LblStatus.setText('Starting conversion process...')
        time.sleep(1.5)
        commend = f'pyside6-uic {self.file_path} -o {self.file_directory}{self.file_name.replace(".ui", ".py")}'
        if self.file_path == '':
            self.ui.LblStatus.setText('Please select a file first')
            return
        subprocess.run(commend, shell=True)
        self.ui.LblStatus.setText('Conversion completed')
     
    
    def select_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'ui files (*.ui)')
        self.file_name = self.file_path.split('/')[-1]
        self.file_directory = self.file_path.replace(self.file_name, '')
        self.ui.LblFileName.setText(self.file_name)
        self.ui.LblStatus.setText('Selected file')
        self.ui.LblDestinationName.setText(self.file_directory)
        self.ui.LblFinalPath.setText(f"{self.file_directory}{self.file_name.replace('.ui', '.py')}")
    
    def select_folder(self):
        self.file_directory = QFileDialog.getExistingDirectory(self, 'Select folder') + '/'
        
        self.ui.LblDestinationName.setText(self.file_directory)
        
        self.ui.LblStatus.setText('Selected folder')
        self.ui.LblFinalPath.setText(f"{self.file_directory}{self.file_name.replace('.ui', '.py')}")
        
    
    def exit(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    