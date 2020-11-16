from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from PyQt5.uic import loadUi
import urllib.request


class Downloader(QDialog):
    def __init__(self):
        super(Downloader, self).__init__()
        loadUi(r'DownLoad APP\forms\download.ui', self)
        self.downloadbtn.clicked.connect(self.download_fun)
        self.browse.clicked.connect(self.browse_file)


    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption='Save File As', directory='.',
                                                filter='All Files (*.*)')
        self.save_location.setText(QDir.toNativeSeparators(save_file))


    def download_fun(self):
        url = self.url.text()
        save_location = self.save_location.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, 'Warning', 'The download failed')

        QMessageBox.information(self, 'Information', 'The dowmload is complete')
        #reset our app after download to start point
        self.progress.setValue(0)
        self.url.setText('')
        self.save_location.setText('')


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progressBar.setValue(int(percent))


app = QApplication([])
dialog = Downloader()
dialog.show()
app.exec_()

        
        

        