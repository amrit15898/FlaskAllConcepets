from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'd4e504dfaf96fa'
app.config['MAIL_PASSWORD'] = 'aee908e8f0d3c8'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/home')
def index():
    recipient = "apalsingh1581998@gmail.com"
    subject = "Test Mail"
    message_body = "This mail sent to only for testing don't take it serious"

    msg = Message(subject = subject,sender = "amrit@gmail.com" ,recipients = [recipient])
    msg.body = message_body

    try:
        mail.send(msg)
        print("this functoin is called")
        return "Email sent successfully"

    except Exception as e:
        print(e)

    return "Hello "


if __name__ == "__main__":
    app.run(debug=True)


