# Importing necessary modules.
import random
import sys
import sqlite3
import webbrowser
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap


# First Screen -Welcome Screen- class. Inheriting from QDialog class.
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()

        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/welcomescreen.ui", self)  # Loading ui.

        # Click functions when pressing buttons.
        self.login.clicked.connect(lambda: self.openLoginScreen())
        self.create.clicked.connect(lambda: self.openCreateAccScreen())

    """This method opens login screen.
     Creates login screen class and changing the widget frame index for show login screen."""

    def openLoginScreen(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    """This method opens creating account screen.
         Creates creating account screen class and changing the widget frame index for show login screen."""

    def openCreateAccScreen(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# Login Screen class. Inheriting from QDialog class.
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()

        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/login.ui", self)  # Loading ui.

        # Click functions when pressing buttons.
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(lambda: self.loginButtonClicked())

    def loginButtonClicked(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        # This statement connects database and queries whether the user exists.
        else:
            conn = sqlite3.connect("login_app.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\'' + user + "\'"
            email = 'SELECT email FROM login_info WHERE username =\'' + user + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()
            result_pass_password = result_pass[0]
            if result_pass_password == password:
                cur.execute(email)
                result_email = cur.fetchone()
                result_email_main = result_email[0]
                self.openEmailCode(result_email_main)
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

    # This method opens email code screen
    def openEmailCode(self, email):
        emailScreen = EmailScreen(email)
        widget.addWidget(emailScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# Create Account Screen class. Inheriting from QDialog class.
class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()

        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/createacc.ui", self)  # Loading ui.

        # Click functions when pressing buttons.
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(lambda: self.signUpButtonClicked())

    """This method creates user with given inputs and adds to user to database."""

    def signUpButtonClicked(self):
        user = self.userfield.text()
        password = self.passwordfield.text()
        email = self.emailfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0 or len(email) == 0:
            self.error.setText("Please fill in all inputs.")

        elif password != confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("login_app.db")
            cur = conn.cursor()

            cur.execute("Insert into login_info values (?,?,?)", (user, password, email))

            conn.commit()
            conn.close()

            fillprofile = FillProfileScreen(user, email)
            widget.addWidget(fillprofile)
            widget.setCurrentIndex(widget.currentIndex() + 1)


# Email Code Screen class. Inheriting from QDialog class.
class EmailScreen(QDialog):
    def __init__(self, email):
        self.email = email
        super(EmailScreen, self).__init__()
        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/emailCode.ui", self)
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Sending random email registration code.
        message = MIMEMultipart()
        message["From"] = "loginappbaver@gmail.com"
        message["To"] = email
        message["Subject"] = "Baver Kaçar Login App Entrance"
        randomCode = random.randint(1000, 9999)
        text = "You need to enter the code down below for login to app:\n{}".format(randomCode)
        message_body = MIMEText(text, "plain")
        message.attach(message_body)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            print(123123)
            mail.login("loginappbaver", "loginapp11-")
            print(12)
            mail.sendmail(message["From"], message["To"], message.as_string())
            print("mail sent successfully")
            mail.close()

        except:
            sys.stderr.write("Problem occurred")
            sys.stderr.flush()

        self.login.clicked.connect(lambda: self.emailLoginButton(randomCode))

    def emailLoginButton(self, randomCode):
        text = self.emailfield.text()
        if text == str(randomCode):
            self.error.setText("Logged in Successfully")
            baverkacar = BaverKacar()
            widget.addWidget(baverkacar)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.error.setText("Code is wrong")


# Final information screen class. Inheriting from QDialog class.
class BaverKacar(QDialog):
    def __init__(self):
        super(BaverKacar, self).__init__()
        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/baverkacar.ui", self)
        self.github.clicked.connect(lambda: webbrowser.open("https://github.com/baverkacar"))
        self.linkedin.clicked.connect(
            lambda: webbrowser.open("https://www.linkedin.com/in/baver-ka%C3%A7ar-b14460187/"))


# Filling Profile screen class. Inheriting from QDialog class.
class FillProfileScreen(QDialog):
    def __init__(self, userText, emailText):
        super(FillProfileScreen, self).__init__()
        loadUi("/Users/bryan/Code/pycharm/myunet/ui/login/fillprofile.ui", self)
        self.userText = userText
        self.emailText = emailText
        self.username.setText(userText)
        self.email.setText(emailText)
        self.image.setPixmap(QPixmap('empty-profile.png'))
        self.cont.clicked.connect(lambda: self.openLoginScreen())
        self.upload.clicked.connect(lambda: self.on_click())

    def openLoginScreen(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # This method adds to profile photo to app.
    def on_click(self):
        print('PyQt5 button click')
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)
        print(imagePath)


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())
