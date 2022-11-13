from flask import Flask,render_template,request,session, url_for,redirect
from flask_session import Session
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.environ.get('Secret_Key')
SESSION_TYPE = os.environ.get('Session_Type')
app.config.from_object(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)  # Session will expire after 5 minutes
Session(app)
usrname = os.environ.get('Usrnme')
psd = os.environ.get('pswd')

@app.route('/',methods=['GET','POST'])
def index():
    message = None
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']
        session.permanent = True
        session['username'] = username
        if username == usrname and password == psd:
            return redirect (url_for('basket_gate1'))
        else:
            message = "Invalid username or password"

    return render_template("index.html",message = message)

@app.route('/basket_gate1',methods=['GET','POST'])
def basket_gate1():
    if 'username' in session:
        username = session['username']
        return render_template('basketball_court.html')
    else:
        return redirect(url_for('notloggedin'))
    

@app.route('/canteen',methods=['GET','POST'])
def canteen():
    if 'username' in session:
        username = session['username']
        return render_template('canteen.html')
    else:
        return redirect(url_for('notloggedin'))


@app.route('/civil_dept',methods=['GET','POST'])
def civil_dept():
    if 'username' in session:
        username = session['username']
        return render_template('civil.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/ct_dept',methods=['GET','POST'])
def ct_dept():
    if 'username' in session:
        username = session['username']
        return render_template('ct.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/ece_dept',methods=['GET','POST'])
def ece_dept():
    if 'username' in session:
        username = session['username']
        return render_template('ece.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/mech_dept',methods=['GET','POST'])
def mech_dept():
    if 'username' in session:
        username = session['username']
        return render_template('mech.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/PET_dept',methods=['GET','POST'])
def PET_dept():
    if 'username' in session:
        username = session['username']
        return render_template('PET_GYM.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/Playground',methods=['GET','POST'])
def Playground():
    if 'username' in session:
        username = session['username']   
        return render_template('Playground.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/RO_Plants',methods=['GET','POST'])
def RO_Plants():
    if 'username' in session:
        username = session['username'] 
        return render_template('RO_Plants.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/Robotics',methods=['GET','POST'])
def Robotics():
    if 'username' in session:
        username = session['username']
        return render_template('Robotics.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route('/Tennikoit',methods=['GET','POST'])
def Tennikoit():
    if 'username' in session:
        username = session['username']
        return render_template('Tennikoit.html')
    else:
        return redirect(url_for('notloggedin'))

@app.route("/logout", methods=['GET','POST'])
def logout():
    #global message
    #message = "You are logged out"
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/notloggedin", methods=['GET','POST'])
def notloggedin():
    errormessage = "You are not currently logged in please login to continue"
    return render_template("notloggedin.html", errormessage=errormessage)
    
app.run(host="0.0.0.0",port=5000)

