
from flask import Flask
app = Flask(__name__)

@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
	return str(a + b)

if __name__ == "__main__":
	app.run()
