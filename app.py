from flask import Flask , render_template , redirect
import requests
from json import loads

app = Flask(__name__)


@app.route('/')
def portal():
    return  render_template('portal.html') 

@app.route('/dashboard/')
def naya():
    return  render_template('dashboard.html') 
    

@app.route('/login')
def nayaa():
    return  render_template('login.html')

@app.route('/query')
def nayaaa():
    return  render_template('query.html')

@app.route('/madashboard')
def new():
    return  render_template('madashboard.html')


@app.route('/admission')
def hello_world():
    return  render_template('admission.html') 
@app.route('/Link')
def link(): 
 return redirect("https://drive.google.com/drive/folders/1Z4KU-sOnIztqSCEro8Or7AwtMC_Mw2eB")

@app.route('/semster12')
def smeseter(): 
 return redirect("https://drive.google.com/drive/folders/1CTxA4nhRC3Wjbvlw7aEafrNGTeaByBmX")

@app.route('/semster34')
def sem34(): 
 return redirect("https://drive.google.com/drive/folders/1yakEhlolq1RH2f5eVxib0bzPKsQnA0AX")

@app.route('/semster56')
def sem56(): 
 return redirect("https://drive.google.com/drive/folders/1ykrm9R84bDQpJxMPNFt8euj1miSY05Sy")

@app.route('/semster78')
def sem78(): 
 return redirect("https://drive.google.com/drive/folders/1z36HYqXF1361tmU_Q3NnyMh5PlnViCbY")








if __name__ == '__main__':
    app.run(debug=True)