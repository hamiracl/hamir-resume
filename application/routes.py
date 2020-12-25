from application import app
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from application.forms import ContactForm
from flask_mail import Message, Mail
import smtplib 

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'shrekandonkey69@gmail.com'
app.config["MAIL_PASSWORD"] = 'Shrekmeples89'

mail.init_app(app)

@app.route("/", methods = ['GET', 'POST'])
@app.route("/index", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email       = form.email.data
            name    = form.name.data
            phone  = form.phone.data
            message   = form.message.data
            msg = Message(form.name.data, sender = 'shrekandonkey69@gmail.com', recipients = ['hamir99@gmail.com'])
            msg.body = """
            From: %s <%s> <%s>
                %s
            """ % (form.name.data, form.email.data, form.phone.data, form.message.data)
            mail.send(msg)
            flash("Message sent!","success")
            return render_template("index.html", index=True, title = "Contact", form = form, contaced = True)
        return render_template("index.html", index=True, title = "Contact", form = form, contacted = False)
    else:
        return render_template("index.html", index=True, title = "Contact", form = form, contacted = False)
        

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")