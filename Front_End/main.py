from flask import Flask, render_template, request
from Search_DB_3 import *

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/results', methods = ['POST','GET'])
def results():
	if request.method == 'POST':
		results = request.form
		results=dict(results)
		results=query((results['searchtext']))
		return render_template("results.html", results = results)


    
if __name__ == "__main__":
    app.run(debug=True)
