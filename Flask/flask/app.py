from flask import Flask, request,render_template, redirect, url_for
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def welcome():
    return "Hello, welcome to Flask!"

@app.route("/index")
def index():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        logging.debug(f"Received values: a={a}, b={b}")
        sum_result = a + b
        return f"The sum of {a} and {b} is {sum_result}."
    except ValueError as e:
        logging.error(f"Error: {e}")
        return "Please provide valid numbers for 'a' and 'b'."
@app.route("/main")
def html_page():
    return render_template("index.html")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"hello mr.{name} your email id is {email} and your message is {message}. welcome to the club"
    return render_template("form.html")
@app.route("/success/<int:score>")
def sucess(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)

@app.route("/sucessdata/<int:score>")
def sucessres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp ={'score': score, "res": res}

    return render_template("result1.html",results=exp)

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/submit",methods=["POST","GET"])
def submit():
    total_score = 0
    if request.method == "POST":
         science = float(request.form.get("science"))
         maths = float(request.form.get("maths"))
         c = float(request.form.get("c"))
         data_science = float(request.form.get("data_science"))

         total_score = (science + maths + c + data_science )/ 4
    return redirect(url_for('sucessres', score=total_score))


            

if __name__ == "__main__":
    app.run(debug=True)
