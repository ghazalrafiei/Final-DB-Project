import gui
import sys


class Customer:
    def __init__(
            self,
            firstname,
            surname,
            username,
            nationality_number,
            phone_number,
            password):
        self.firstname = firstname
        self.surname = surname
        self.nationality_number = nationality_number
        self.phone_number = phone_number
        self.password = password


if __name__ == '__main__':

    gui.window.show()
    sys.exit(gui.app.exec_())

    print('end')
