print("Helllo World")
# flask is web framework of python
# from module flask import Flask -->jo ki ek class hai
from flask import Flask, render_template
# creating an object of the class humne sari functinality of class Flask import kra krr app me dal di hai
# jab bhi url access ho  show hello world
app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'Role': 'Data Analyst',
    'Location': 'Bengluru,India',
    'Salary': '10,00,000'
  },
  {
    'id': 2,
    'Role': 'Data Scientist',
    'Location': 'Delhi,India',
    'Salary': '12,00,000'
  },
  {
    'id': 3,
    'Role': 'Front-End Developer',
    'Location': 'Bengluru,India',
    'Salary': '15,00,000'
  },
  {
    'id': 1,
    'Role': 'Back-End Developer',
    'Location': 'Pune,India',
    'Salary': '17,00,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

 




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
