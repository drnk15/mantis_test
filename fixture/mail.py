import poplib
import email
import time
import quopri


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]
                    msgtext = '\n'.join(map(lambda x: x.decode('utf-8'), msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        text = quopri.decodestring(msg.get_payload()).decode('utf-8')
                        pop.dele(n+1)
                        pop.quit()
                        return text
            pop.close()
            time.sleep(3)
        return None
