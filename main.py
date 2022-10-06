from flask import Flask, render_template, request, redirect, flash
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = "itismytopsecretkeyforthisportfoliowebsite"

MY_EMAIL = "iamsiddharth238@gmail.com"
PASSWORD = "sevzkruakvzcccjv"


def send_message(name, email, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Message from Portfolio\n\nName: {name}\nEmail: {email}\nMessage: {message}"
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact_me():
    data = request.form
    name = data["Name"]
    email = data["Email"]
    message = data["Message"]
    send_message(name, email, message)
    flash("Thanks for contacting me. Your message was received!")
    return redirect("/#contact")


if __name__ == "__main__":
    app.run(debug=True)
