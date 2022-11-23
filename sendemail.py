import smtplib
from email.message import EmailMessage
from load_creds import load_creds

creds = load_creds()

def send_email(text):
	user = creds[0]
	password = creds[1]
	recipient = creds[2]

	email_server = smtplib.SMTP("smtp.gmail.com", 587)
	email_server.starttls()

	msg = EmailMessage()
	msg['subject'] = "Chat Room Notification"
	msg.set_content(text)

	msg['from'] = user
	msg['to'] = recipient

	email_server.login(user,password)
	email_server.send_message(msg)

	del msg['from']
	email_server.quit()

if __name__ == '__main__':
	sent = False
	while not sent:
		try:
			send_email("Hello World")
			sent = True
		except:
			pass
