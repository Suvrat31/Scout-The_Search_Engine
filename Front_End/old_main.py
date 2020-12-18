from flask import Flask, render_template, request
import socket
import ast

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/results', methods = ['POST','GET'])
def results():
	if request.method == 'POST':
		results1 = request.form
		results=str(results1)
		#results=' '.join(results)  
		port=12397
		soc_obj=socket.socket()
		soc_obj.connect(('localhost', port))
		soc_obj.send((results).encode())
		results1 = soc_obj.recv(1000).decode()
		results=ast.literal_eval(results1)   
		return render_template("results.html", results = results)


    
if __name__ == "__main__":
    app.run(debug=True)
