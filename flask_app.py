from flask import Flask, request, jsonify
from sendmail import send_mail
import os
import threading

app = Flask(__name__)


@app.route('/mail', methods=['POST'])
def mail():
    fullpath = os.path.realpath(__file__)
    folder = os.path.dirname(fullpath)

    with open((folder + '/info.txt'), 'r') as file:
        lines = file.readlines()

        login = lines[0]
        password = lines[1]
        my_mail   = lines[2]

    req_email = request.form['email']
    req_name  = request.form['name']

    if(req_email and req_name):
        try:

            trhd = threading.Thread(target=send_mail, args=(login,password,my_mail,req_name,req_email))
            #send_mail(login,password,my_mail,req_name,req_email)
            trhd.start()
            trhd.join()

            return jsonify({'end':'success'})
        except Exception as ex:
            return jsonify({'error':'an error ocurred during email processing'})
    else:
        return jsonify({'error':'data is not valid'})

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

