import pyodbc

# import webbrowser
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ARUN\SQLEXPRESS;'
                      'Database=testdb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

from flask import Flask, render_template, request, flash

# webbrowser.open_new_tab('http://127.0.0.1:5000')
app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
@app.route('/index.html')
# @app.route('/home')
def home():
    return render_template("index.html")


@app.route('/confim', methods=["POST", "GET"])
def Confirm():
    if request.method == "POST":
        a = request.form.get("uname")
        b = request.form.get("upswd")

        # c="open.mail"
        print(a)

        cursor.execute("select * from Register1")
        error = None

        for i in cursor:
            if i[0]==a:
                flag=0
                return render_template("Register_form.html")
                conn.commit()
                conn.close()
                break
            else:
                flag=1
        if flag==1:
            error = 'User Does Not Exit!'
            return render_template("index.html", error=error)
        conn.commit()
        conn.close()




@app.route('/register.html')
def Register():
    return render_template('register.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    global f, a, b, c, d
    f = 0
    if request.method == "POST":
        a = request.form.get("uname1")
        b = request.form.get("email1")
        c = request.form.get("upswd1")
        d = request.form.get("Pnum")
        cursor.execute("select*from Register1")

        for i in cursor:
            if (a == i[0]):
                f = 1
                break
            else:
                f = 0
                print("pass")
        return check2()


def check2():
    if (f == 0):
        cursor.execute("insert into Register1 values(?,?,?,?)", (a, b, c, d))

        flash = 'sucessfully Registered!'
        return render_template("index.html")
    else:
        error = "User already exist"
        return render_template("register.html", error=error)


@app.route('/index.html')
def BackToMenu():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
