from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/send_message", methods=["POST"])
def send_message():
    # Handle the form data here
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Process the data (e.g., save to database, send email, etc.)
    return redirect("/contact")


if __name__ == "__main__":
    app.run(debug = True)