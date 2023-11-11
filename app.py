from flask import Flask,render_template,request,redirect,session,url_for
import sqlite3
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "tc,;sv.f;bmgnlmvlrmvlmwdmwsq".encode('utf8')
app.template_folder = "templates"
app.static_folder = "static"
lovdb = 'db/lovdb.db'
def check_exists(username,password):
    result = False
    conn = sqlite3.connect(lovdb)
    cursor = conn.cursor()
    cursor.execute(f"select * from Account where Username ='{username}' and Password = '{password}'")
    data = cursor.fetchone()
    if len(data) > 0:
        result = True
    conn.close()
    return result
def check_account(username):
  result = False
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Account where Username ='{username}'")
  data = cursor.fetchone()
  if len(data) > 0:
      result = True
  conn.close()
  return result
def valid_username(username):
  numupper =0
  for c in username:
    if c.isupper():
        numupper = numupper + 1

  if numupper <= 0:
    reason=('username must contain at least one uppercase character')
    return '',reason

  numlower =0
  for c in username:
    if c.islower():
        numlower = numlower + 1

  if numlower <= 0:
    reason=('username must contain at least one lowercase character')
    return '', reason

  if len(username)<8:
      reason = ('username must be greater than 8 characters')
      return '',reason

  numdigit=0
  for c in username:  
    if c.isdigit():
        numdigit = numdigit + 1

  if numdigit <= 0:
    reason= ('username must contain at least one number')
    return '',reason

  else:
    return username, ''

@app.route("/")
def index():
  if "username" in session:
    username = session['username']
  else:
    username = ""
  return render_template("index.html", username = username)

@app.route("/login", methods = ['GET', 'POST'])
def login():
  if request.method == "POST":
      session.permanent = True
      username = request.form['username']
      password = request.form['password']
      if check_exists(username,password):
        session['username'] = username
        return redirect(url_for("index"))
      else :
        return  redirect(url_for("login"))
  else:
      if "user" in session:
          return redirect(url_for("/"))

      return render_template("login.html")


@app.route("/logout")
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route("/signup", methods = ['GET','POST'])
def signup():
  if request.method=="GET":
    return render_template("signup.html")
  else:
    username = request.form['username']
    password = request.form['password']
    username = valid_username(username)[1]
    password = valid_username(password)[1]
    return render_template("signup.html",account_message=username,password_message=password,)

      


@app.route("/browse/<category>/<subcategory>/<genre>/<age_range>/<sort_type>", methods = ['GET','POST'])
def show_products(category, subcategory, genre, age_range, sort_type):
  sqlcommand = f"select * from Book where Category = '{category}'"
  if subcategory != "null":
    sqlcommand += f" and Subcategory = '{subcategory}'"
  if genre != "null":
    sqlcommand += f" and Genre = '{genre}'"
  if age_range != "null":
    sqlcommand += f" and Age_Range = '{age_range}'"
  if sort_type != "null":
    sorter = sort_type.split('_')
    sqlcommand += f" order by {sorter[0]} {sorter[1]}"
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(sqlcommand)
  book_list = cursor.fetchall()
  conn.close()
  return render_template("store.html", book_list = book_list)

@app.route("/cart", methods = ['GET','POST'])
def show_cart(account_id):
  pass

@app.route("/cart/finalize_purchase", methods = ['GET','POST'])
def finalize_purchase(account_id):
  pass

@app.route("/profile/<account_id>", methods = ['GET','POST'])
def profile(account_id):
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Profile where Account_ID ='{account_id}'")
  profile = cursor.fetchone()
  conn.close()
  return render_template("profile.html", profile = profile)

@app.route("/profile/achievement/<account_id>", methods = ['GET','POST'])
def show_achievement(account_id):
  pass

@app.route("/profile/history/<account_id>", methods = ['GET','POST'])
def show_history(account_id):
  pass

@app.route("/library/<account_id>", methods = ['GET', 'POST'])
def show_library(account_id):
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Library where Account_ID ='{account_id}' inner join Book on Book.Book_ID = Library.Book_ID")
  library = cursor.fetchall()
  conn.close()
  return render_template("profile.html", library = library)

@app.route("/read/<book_id>", methods = ['GET', 'POST'])
def read(book_id):
  pass


if __name__=="__main__":
  app.run(debug=True)