from MySQLdb import MySQLError
import MySQLdb
from flask import Flask, Response, jsonify,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required
from flask_mysqldb import MySQL,MySQLdb
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb
from sqlalchemy import func
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
        
app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'students'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

mysql = MySQL(app)

# MY db connection



# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/students'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class Student(db.Model):
    usn=db.Column(db.String(100),primary_key=True)
    Name=db.Column(db.String(50))
    fname=db.Column(db.String(50))
    mname=db.Column(db.String(50))
    date=db.Column(db.Date())
    Email=db.Column(db.String(100))
    Mobile=db.Column(db.Integer())
    nationality=db.Column(db.String(50))
    paddress=db.Column(db.String(100))
    sem=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    religion=db.Column(db.String(50))
    voter=db.Column(db.String(50))
    cat=db.Column(db.String(5))
    caste=db.Column(db.String(50))
    subcaste=db.Column(db.String(50))
    income=db.Column(db.Integer())
    incomecertif=db.Column(db.String(50))
    address=db.Column(db.String(100))
    aadhar=db.Column(db.Integer())
    blood=db.Column(db.String(50))
    parentsmobile=db.Column(db.Integer())
    programme=db.Column(db.String(100))
    Branch=db.Column(db.String(100))
    Course=db.Column(db.String(100))
    Batch=db.Column(db.Integer())
    type=db.Column(db.String(100))
    rank=db.Column(db.Integer)
    regno=db.Column(db.String(100))
    category=db.Column(db.String(100))
    categorya=db.Column(db.String(100))
    admission=db.Column(db.Date())
    fees=db.Column(db.Integer())
    marks=db.Column(db.Integer())
    num=db.Column(db.Integer())
    school=db.Column(db.String(100))
    scheme=db.Column(db.String(100))
    
    

@app.route('/')
def main(): 
    return render_template('main.html')

@app.route('/searching')
def searching(): 
    return render_template('searching.html')

@app.route('/index')
def index(): 
    return render_template('index.html')


@app.route('/download')
def download(): 
    return render_template('download.html')

@app.route('/addstudent',methods=['POST','GET'])
def addstudent():
    # dept=db.engine.execute("SELECT * FROM `department`")
    stu=Student.query.all()
    if request.method=="POST":
        Name=request.form.get('Name')
        fname=request.form.get('fname')
        mname=request.form.get('mname')
        date=request.form.get('date')
        Email=request.form.get('Email')
        Mobile=request.form.get('Mobile')
        nationality=request.form.get('nationality')
        paddress=request.form.get('paddress')
        address=request.form.get('address')
        gender=request.form.get('gender')
        religion=request.form.get('religion')
        voter=request.form.get('voter')
        cat=request.form.get('cat')
        caste=request.form.get('caste')
        subcaste=request.form.get('subcaste')
        income=request.form.get('income')
        incomecertif=request.form.get('incomecertif')
        sem=request.form.get('sem')
        aadhar=request.form.get('aadhar')
        blood=request.form.get('blood')
        parentsmobile=request.form.get('parentsmobile')
        usn=request.form.get('usn')
        Batch=request.form.get('Batch')
        Branch=request.form.get('Branch')
        scheme=request.form.get('scheme')
        Course=request.form.get('Course')
        type=request.form.get('type')
        rank=request.form.get('rank')
        regno=request.form.get('regno')
        category=request.form.get('category')
        categorya=request.form.get('categorya')
        admission=request.form.get('admission')
        fees=request.form.get('fees')
        marks=request.form.get('marks')
        num=request.form.get('num')
        programme=request.form.get('programme')
        school=request.form.get('school')
      
        # query=db.engine.execute(f"INSERT INTO `student` (`rollno`,`sname`,`sem`,`gender`,`branch`,`email`,`number`,`address`) VALUES ('{rollno}','{sname}','{sem}','{gender}','{branch}','{email}','{num}','{address}')")
        query=Student(Name=Name,fname=fname,mname=mname,date=date,Email=Email,Mobile=Mobile,nationality=nationality,paddress=paddress,address=address,gender=gender,religion=religion,voter=voter,cat=cat,caste=caste,subcaste=subcaste,income=income,incomecertif=incomecertif,sem=sem,aadhar=aadhar,blood=blood,parentsmobile=parentsmobile,usn=usn,Batch=Batch,Branch=Branch,scheme=scheme,Course=Course,type=type,rank=rank,regno=regno,category=category,categorya=categorya,admission=admission,fees=fees,marks=marks,num=num,programme=programme,school=school)
        db.session.add(query)
        db.session.commit()

    flash("Confirmed","Thanks for Registering!!")
    return render_template('docupdt.html',stu=stu)


@app.route('/deptlgn', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if (username=='gecr' and password=='123456'):
            session['logged_in']=True
            return render_template('dept.html')
        else:
            error = 'Invalid username or password'
            return render_template('deptlgn.html', error=error)
    return render_template('deptlgn.html')

@app.route('/adminlgn', methods=['GET', 'POST'])
def alogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        if (username=='gecr' and password =='654321'):
            session['logged_in'] = True
            return render_template('admin.html')
        else:
            error = 'Invalid username or password'
            return render_template('adminlgn.html', error=error)
    return render_template('adminlgn.html')




@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=="POST":
        usn=request.form.get('usn')
        bio=Student.query.filter_by(usn=usn).first()
        if(usn=='1gg21cs014'):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'durba.jpg')
        elif(usn=='1gg21cs017'):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'gouri.jpg')
        elif(usn=='1gg21cs030'):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'nandish.jpg')
        elif(usn=='1gg21cs004'):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'bharat.jpg')
        elif(usn=='1gg21cs011'):
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'deepak.jpg')
        else:
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'people.jpg')
        return render_template('search.html',bio=bio,user_image = full_filename)
        
    return render_template('search.html')

@app.route('/searchx',methods=['POST','GET'])
def searchx():
    if request.method=="POST":
        scheme=request.form.get('scheme')
        sear = Student.query.filter_by(scheme=scheme).all()
        return render_template('searchx.html',sear=sear)
    
    return render_template('searchx.html')

@app.route('/searchy',methods=['POST','GET'])
def searchy():
    if request.method=="POST":
        sem=request.form.get('sem')
        searc = Student.query.filter_by(sem=sem).all()
        return render_template('searchy.html',searc=searc)
    
    return render_template('searchy.html')

@app.route('/studentdetail')
def studentdetail():
    # query=db.engine.execute(f"SELECT * FROM `student`")
    query=Student.query.all() 
    return render_template('studentdetail.html',query=query)

@app.route('/stats')
def statistics():
    total_students = Student.query.count()
    gender_distribution = db.session.query(Student.gender, func.count(Student.usn)).group_by(Student.gender).all()
    Branch_distribution = db.session.query(Student.Branch, func.count(Student.usn)).group_by(Student.Branch).all()
    return render_template('stats.html', total_students=total_students, gender_distribution=gender_distribution,Branch_distribution=Branch_distribution)


@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'


app.run(debug=True)    