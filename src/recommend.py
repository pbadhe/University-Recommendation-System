import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
from flask import jsonify
import pandas as pd
import pred, processData

app = Flask(__name__)
CORS(app)
prepData = pd.read_csv("data/Prepared MS University Data.csv")

programs = ['Computer Science', 'Speech Language Pathology', 'Electrical Engineering', 'MIS', 'Civil Engineering', 'Mechanical Engineering', 'Electronics and Communication', 'Industrial Engineering', 'Information Systems', 'Statistics', 'Urban Planning', 'Public Policy', 'Business Analytics', 'Architecture', 'Engineering Management', 'Electrical and Computer Engineering', 'Economics', 'Aerospace Engineering', 'Biomedical Engineering', 'Public Health', 'English', 'Chemical Engineering', 'Philosophy']

@app.route('/')
def home():
    return render_template("home.html", programs=programs)

@app.route('/page1')
def page1():
    return render_template("page1.html", programs=programs)

@app.route('/page2')
def page2():
    return render_template("page2.html", programs=programs)

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html", programs=programs)

@app.route('/university')
def university():
    return render_template("university.html")

@app.route('/predictuni', methods=['GET', 'POST'])
def predictuni():
    if request.method == 'POST':
        # major = request.form.get("Major")  
        # cgpa = request.form.get("CGPA")  
        # greV= request.form.get("GRE_V")  
        # greQ= request.form.get("GRE_Q")  
        # greAWA= request.form.get("GRE_AWA")  
        # toefl= request.form.get("toeflScore")  
        # industryExp= request.form.get("industryExp")  
        # researchExp= request.form.get("researchExp")
        # major = "Computer Science"
        major = "MIS"
        cgpa = 3.71
        greV = 158
        greQ = 164
        greAWA = 4
        toefl = 106
        industryExp = 20
        researchExp = 0
        # print(major,cgpa,greV,greQ,greAWA,toefl,industryExp,researchExp)
        unis = pred.getUniversities(prepData, major, cgpa, greV, greQ, greAWA, toefl, industryExp, researchExp)
        print(unis)
    return render_template("page2.html", universities=unis)
                
@app.route('/',methods=['GET', 'POST'])
def ssd():
    return render_template("index.html")

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)