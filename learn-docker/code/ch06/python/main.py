from flask import Flask, jsonify
app = Flask(__name__)
 
@app.route("/")
def hello():
  return "Hello World!"
 
@app.route("/colors")
def colors():
   return jsonify(["red", "green", "blue", "orange"])
 
if __name__ == "__main__":
  app.run()