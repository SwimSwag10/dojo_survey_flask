from flask import render_template,request, redirect, session
from flask_app import app
from flask_app.models import survey

@app.route('/create/survey', methods=['POST'])
def create():
  if not survey.Survey.validate_survey(request.form):
    return redirect('/')
  data = {
    "name" : request.form['name'],
    "location" : request.form['location'],
    "language" : request.form['language'],
    "comments" : request.form['comments'],
  }
  survey.Survey.save(data)
  return redirect('/show')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/show')
def show_info():
  return render_template('results.html', results=survey.Survey.get_one())