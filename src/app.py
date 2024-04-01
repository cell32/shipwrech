from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("login.html")

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_name = request.form.get("user_input", "")
    input_password = request.form.get("user_password", "")
    # return "You entered: " + input_name + input_password
    return redirect(url_for("show_choices", input_name=input_name))

@app.route("/show_choices/<input_name>", methods=["GET", "POST"])
def show_choices(input_name):
    continent = request.form.get("continent", "")
    return render_template("choices.html", input_name=input_name, continent=continent)

@app.route("/exit")
def exit():
    return redirect(url_for("main"))

# @app.route("/retrieve_shipwrech_data", methods="POST")
# def retrieve_data():
#     selected_option = request.form.get("shipwreck-type")
#     result = retrieve_shipwrech_data(selected_option)
    

if __name__ == '_main__':
    app.run(debug=True, use_reloader=True )