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

@app.route('/predictuni', methods=['GET', 'POST'])
def predictuni():
    if request.method == 'POST':
        major = request.form.get("Major")
        cgpa = float(request.form.get("CGPA"))
        greV= float(request.form.get("GRE_V"))
        greQ= float(request.form.get("GRE_Q"))
        greAWA= float(request.form.get("GRE_AWA"))
        toefl= round(float(request.form.get("toeflScore")) * 2) / 2 #Handling for IELTS
        industryExp= float(request.form.get("industryExp"))
        researchExp= float(request.form.get("researchExp"))
        # major = "Computer Science"
        # # major = "MIS"
        # cgpa = processData.handleCGPA(3.71)
        # greV = 158
        # greQ = 164
        # greAWA = 4
        # toefl = 119
        # industryExp = 36
        # researchExp = 0
        univs = pred.getUniversities(prepData, major, cgpa, greV, greQ, greAWA, toefl, industryExp, researchExp)
        # ranks = pred.getRank(univs)
        # print(ranks)
        major = [major]*len(univs)
    return render_template("page2.html", universities=univs)
                
@app.route('/',methods=['GET', 'POST'])
def ssd():
    return render_template("index.html")

@app.route('/university')
def university():
    
    with open('data/Universities.txt', 'r') as f:
        universities = [line.strip() for line in f]
    search_query = request.args.get('search')

    if search_query:
        universities = [u for u in universities if search_query.lower() in u.lower()]

    # Remove the first and last square brackets
    universities = " ".join(universities).split("[")[1].split("]")[0]

    # Split the universities string at the comma and create a list of strings
    universities_list = universities.split(",")

    return render_template("university.html", universities=universities_list)


port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)