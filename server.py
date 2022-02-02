from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
  print('getting post info')
  session['name'] = request.form['username']
  session['location'] = request.form['location']
  session['language'] = request.form['language']
  session['comment'] = request.form['comment']
  return redirect('/show')

@app.route('/show')
def show_info():
  return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)