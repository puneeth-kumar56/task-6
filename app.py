from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Contact form route
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # For now, just print it (later you can save to DB or send email)
        print(f"Message from {name} ({email}): {message}")
        return "Thank you for contacting me!"
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
