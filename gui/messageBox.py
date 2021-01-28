from PyQt5.QtWidgets import QMessageBox
from gui import darkTheme


def show_message(message='', err = True):
    if message != '':

        msg = QMessageBox()
        msg.setPalette(darkTheme.dark_palette)

        if err:
            msg.setIcon(QMessageBox.Critical)
            msg.setText('Query Failed')
            msg.setWindowTitle('Error')

        else:
            msge = ''
            for m in message:
                msge += str(m) + '\n'
            message = msge
            msg.setIcon(QMessageBox.Information)
            msg.setText('Result: ')
            msg.setWindowTitle('Succeed')

        msg.setInformativeText(message)
        msg.setEscapeButton(QMessageBox.Ok)
        msg.show()
        msg.exec_()



