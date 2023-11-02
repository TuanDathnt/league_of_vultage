from flask import Flask,render_template,request,redirect,session,url_for

app = Flask(__name__)
app.secret_key = "tc,;sv.f;bmgnlmvlrmvlmwdmwsq".encode('utf8')
app.template_folder = "templates"
app.static_folder = "static"

@app.route("/")
def index():
  return render_template("index.html",username="")

@app.route("/login", methods = ['GET', 'POST'])
def login():
  if request.method=="GET":
    return render_template("login.html")

@app.route("/logout")
def logout():
  pass

@app.route("/signup", methods = ['GET','POST'])
def register():
  if request.method=="GET":
    return render_template("signup.html")

@app.route("/browse", methods = ['GET','POST'])
def show_products():
  pass

@app.route("/cart", methods = ['GET','POST'])
def show_cart(account_id):
  pass

@app.route("/cart/finalize_purchase", methods = ['GET','POST'])
def finalize_purchase(account_id):
  pass

@app.route("/profile/<account_id>", methods = ['GET','POST'])
def profile(account_id):
  pass

@app.route("/profile/achievement/<account_id>", methods = ['GET','POST'])
def show_achievement(account_id):
  pass

@app.route("/profile/history/<account_id>", methods = ['GET','POST'])
def show_history(account_id):
  pass

@app.route("/library/<account_id>", methods = ['GET', 'POST'])
def show_library(account_id):
  pass

@app.route("/read/<book_name>", methods = ['GET', 'POST'])
def read(book_name):
  pass


if __name__=="__main__":
  app.run(debug=True)