from flask import Flask, render_template, request
from twilio.rest import *

app = Flask(__name__)
data = ['Account sid','twilio number','Auth-Token']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST','GET'])
def send_credentials():
    if request.method == 'POST':
         data[0] = request.form['sid']
         data[1] = request.form['t_number']
         data[2] = request.form['auth_token']
         return render_template('main.html')

@app.route('/main.html', methods  = ['POST','GET'])
def send_msg():
    if request.method == 'POST':
        
        client = Client(data[0], data[2])       
        receiver_number  = request.form['Receiver_number']
        my_msg = request.form['msg']       
        message = client.messages.create(to = receiver_number, from_= data[1], body = my_msg)  
        return ("Your Msg has been sent\n" + message.sid)



if __name__ == '__main__':
    app.run(debug=True)
