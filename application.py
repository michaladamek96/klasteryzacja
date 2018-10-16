from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
@app.route("/ku")	
def kuku():
	return "kuku!"
	
if __name__ == "__main__":
	app.run()