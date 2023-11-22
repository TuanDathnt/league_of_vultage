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
  if data:
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
def get_max_id_order():
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()    
  max_id=0
  sqlcommand= "SELECT Max(Order_ID) from Order"
  cursor.execute(sqlcommand)
  max_id = cursor.fetchone()[0]
  conn.close()
  return max_id+1
def get_max_id():
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()    
  max_id=0
  sqlcommand= "SELECT Max(Account_ID) from Account"
  cursor.execute(sqlcommand)
  max_id = cursor.fetchone()[0]
  conn.close()
  return max_id+1
def execute_command(object):
  conn = sqlite3.connect('db/lovdb.db')
  cursor = conn.cursor() 
  print(object)
  # Câu lệnh SQL để chèn dữ liệu
  insert_sql = '''
  INSERT INTO Account
  (Account_ID,Username,Password,Gmail) 
  VALUES 
  (?, ?, ?, ?)
  '''

  # Chèn dữ liệu vào bảng

  cursor.execute(insert_sql, object)

  conn.commit()
  conn.close()
    
@app.route("/")
def index():
  if "username" in session:
    username = session['username']
  else:
    username = ""
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()   
  sqlcommand= "SELECT * from Book"
  cursor.execute(sqlcommand)
  books =  cursor.fetchall()
  conn.close()
  return render_template("index.html", username = username,books=books)

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
      if "username" in session:
          return redirect(url_for("/"))

      return render_template("login.html")


@app.route("/logout")
def logout():
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route("/signup", methods = ['GET','POST'])
def signup():
  result=''
  username=''
  if request.method=="GET":
    return render_template("signup.html",account_message='',password_message='',password_confirm_message='aa',result=result)
  else:
    username = request.form['username']
    password = request.form['password']
    gmail= request.form['email']
    password_confirm= request.form['re-enter-password']
    
    username_message = valid_username(username)[1]
    password_message= valid_username(password)[1]
    if password != password_confirm:
      password_confirm=''
    if check_account(username):
        username_message = "Tai Khoan da ton tai"
    if password_confirm =='' or username_message!='' or password_message!='':
     pass
    else:
     
      object = (get_max_id(),username,password,gmail)
      execute_command(object)
      result="Dang Ky Thanh Cong"
    
    return render_template("signup.html",account_message=username_message,password_message=password_message,password_confirm_message=password_confirm,result=result,username=username,email=gmail)
# DONEEEEEEEEEEEEEEEEEEEE


@app.route("/store", methods = ['GET'])
def store():
  search=request.args.get('search',default="",type=str)
  page=request.args.get('page',default=1,type=int)
  filter = request.args.get('filter',default='all',type=str)
  books=[]
  if 'username' in session:
    username = session['username']
  else:
    username=""
  focus=""
  # if category==None:
  #   return render_template("store.html")
  # sqlcommand = f"select * from Book where Category = '{category}'"
  # if subcategory != None:
  #   sqlcommand += f" and Subcategory = '{subcategory}'"
  # if genre !=  None:
  #   sqlcommand += f" and Genre = '{genre}'"
  # if age_range !=  None:
  #   sqlcommand += f" and Age_Range = '{age_range}'"
  # if sort_type !=  None:
  #   sorter = sort_type.split('_')
  #   sqlcommand += f" order by {sorter[0]} {sorter[1]}"
  #   conn = sqlite3.connect(lovdb)
  #   cursor = conn.cursor()
  #   cursor.execute(sqlcommand)
  #   book_list = cursor.fetchall()
  #   conn.close()
  if search != "":
    conn=sqlite3.connect(lovdb)
    cursor = conn.cursor()
    cursor.execute(F"select * from Book where Book_Name Like '%{search}%'")
    books = cursor.fetchall()
    conn.close()
    return render_template("store.html",username=username,books=books)
  
  if filter!='all':
    conn=sqlite3.connect(lovdb)
    cursor = conn.cursor()
    cursor.execute(F"select * from Book where Book_Category Like '%{filter}%'")
    books = cursor.fetchall()
    conn.close()
  else:
    conn=sqlite3.connect(lovdb)
    cursor = conn.cursor()
    cursor.execute(F"select * from Book")
    books = cursor.fetchall()
    conn.close()
    print(books[0])
  
  # print(filter)
  return render_template("store.html",username=username,books=books,focus=filter)
@app.route("/book/<id>")
def book(id):
  if "username" in session:
    username=session.get("username")
  else:
    username=''
  conn=sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(F"select * from Book where Book_ID={id}")
  book = cursor.fetchone()
  conn.close()
  print(book)
  return render_template('book.html',username=username,book=book)

@app.route("/cart/add/<id>", methods = ['GET','POST'])
def add_cart(id):
  cart = session.get('cart',[])
  print(id)
  cart.append(id)


  session["cart"]=cart  

  referer_url = request.headers.get('Referer')

    
  if referer_url:
      return redirect(referer_url)
  else:
      return redirect('/')
@app.route("/cart/delete/<id>", methods = ['GET','POST'])
def delete_cart(id):
  cart = session.get('cart',[])
  if id in cart:
    cart.remove(id)
  referer_url = request.headers.get('Referer')

    
  if referer_url:
      return redirect(referer_url)
  else:
      return redirect('/') 
@app.route("/cart")
def cart():
  username=""
  carts=[]
  money=0
  if "username" in session:
    username=session.get("username")
  current_cart=[]
  if 'cart' in session:
    current_cart=session.get('cart',[1,2,3])
  
  conn=sqlite3.connect(lovdb)
  cursor = conn.cursor()
  for id in current_cart:
    cursor.execute(f"select * from Book where Book_ID={id}")
    print()
    product = cursor.fetchone()
    money = money +product[10]
    carts.append(product)
  conn.close()
  print(money)
  return render_template(
  "cart.html",carts=carts,money=money
  )
@app.route("/pay")
def pay():
  username=""
  if "username" in session:
    username=session.get("username")
  carts= session.get("cart",[])
  referer_url = request.headers.get('Referer')
  if request.method=="POST":
    print(session['cart'])  
    
    order=[]
    
    conn=sqlite3.connect(lovdb)
    cursor = conn.cursor()
    for id in carts:
      cursor.execute(f"select * from Book where Book_ID={id}")
      obj = cursor.fetchone()
      product = {"name":obj[0],"quantity":request.form[f"{obj[0]}"]}
      order.append(product)
    print(order)
    conn.close()
 

  return render_template("/pay.html",username=username)

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
#CHECKOUT FUNCTION
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    # Check if the user is logged in
  username=""
  if "username" in session:
    username=session.get("username")
  if request.method=="POST":
    first_name = request.form('first_name')
    last_name = request.form('last_name')
    address = request.form('address')
    city = request.form('city')
    country = request.form('country')
    last_name = request.form('last_name')
    insert_sql = '''
    INSERT INTO Order
    (Order_ID,Account_ID,Book_ID,Number,Form,Total_Price,Address) 
    VALUES 
    (?, ?, ?, ?,?,?,?)
    '''
    conn = sqlite3.connect(lovdb)
    cursor = conn.cursor()
    cursor.execute(insert_sql,(get_max_id_order(),"","","","","",""))
    conn.commit()
    conn.close()
  referer_url = request.headers.get('Referer')
  # print(session['cart'])  
  # carts = session["cart"]
  # referer_url = request.headers.get('Referer')
  # order=[]

  # conn=sqlite3.connect(lovdb)
  # cursor = conn.cursor()
  # for id in carts:
  #   cursor.execute(f"select * from Book where Book_ID={id}")
  #   obj = cursor.fetchone()
  #   product = {"name":obj[0],"quantity":request.form[f"{obj[0]}"]}
  #   order.append(product)
  # print(order)
  # conn.close()
    
  if referer_url:
      return redirect(referer_url)
  else:
      return redirect('/')
    # Retrieve the user's cart from the session

  # total_price = sum(item['new_price'] for item in cart)
  # # Generate a unique order_id (you can use uuid or any other method)
  # order_uuid = generate_order_id()
  # return render_template('checkout.html', cart=cart, total_price=total_price, order_uuid=order_uuid)

#PROCEED TO CHECKOUT FUNCTION
# @app.route('/proceed-checkout-<order_uuid>', methods=['GET', 'POST'])
# def proceed_checkout(order_uuid):
#     # Retrieve the user's cart from the session
#     if order_uuid != session['instant_order_id']:
#       cart = session.get('cart', [])
#     else:
#       cart = session.get('instant_cart', [])
#     # Calculate total price
#     total_price = sum(item['new_price'] for item in cart)
#     if request.method == 'POST':
#         # Get user id
#         username = session['username']
#         conn = sqlite3.connect(sqldbuser)
#         cursor = conn.cursor()
#         sqlcommand="Select id from users where username = '"+username+"' or email = '"+username+"'"
#         cursor.execute(sqlcommand)
#         user_id = int(''.join(map(str, cursor.fetchone())))
#         # Save the order
#         order = save_order(user_id, order_uuid, total_price, cart)
#         # Clear the cart after successful payment
#         session['cart'] = []
#         flash('Payment successful. Thank you for your purchase!', 'success')
#         return redirect(url_for('index'))
#     return render_template('checkout.html', cart=cart, total_price=total_price)

@app.route("/admin",methods=['GET',"POST"])
def admin():
  search=request.args.get('search',default="",type=str)
  if search!="":
    conn = sqlite3.connect(lovdb)
    cursor = conn.cursor()

    cursor.execute(f"select * from Account WHERE Username Like '%{search}%'")
    users = cursor.fetchall()
    conn.close()
    return render_template("admin.html",users=users,len=len(users),focus='users',order=[],books=[])
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Account")
  users = cursor.fetchall()
  conn.close()
  return render_template("admin.html",users=users,len=len(users),focus='users',order=[],books=[])
@app.route("/delete/<id>")
def delete(id):
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"DELETE FROM Account WHERE Account_ID = {id}")
  conn.commit()
  conn.close()
  return redirect(url_for('admin'))

@app.route("/admin/orders")
def orders():
  
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Account")
  users = cursor.fetchall()
  conn.close()
  return render_template("admin.html",users=[],len=len(users),focus='orders',order=users,books=[])
@app.route("/admin/books")
def books():
  conn = sqlite3.connect(lovdb)
  cursor = conn.cursor()
  cursor.execute(f"select * from Book ")
  users = cursor.fetchall()
  conn.close()
  return render_template("admin.html",users=[],len=len(users),focus='books',order=[],books=users)

if __name__=="__main__":
  app.run(debug=True)