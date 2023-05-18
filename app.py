print("Helllo World")
# flask is web framework of python
# from module flask import Flask -->jo ki ek class hai
from flask import Flask
# creating an object of the class humne sari functinality of class Flask import kra krr app me dal di hai 
# jab bhi url access ho  show hello world
app=Flask(__name__)
@app.route("/")
def hello_world():
  return "hello World_____Helloo agian"
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)