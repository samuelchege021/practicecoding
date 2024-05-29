from flask import Flask

from flask import render template ,url_for

from flask import url_for
from flask   import flask,request
app= flask (_name_)
@pp.route("/")
def helloworld():
    return ("<p>" "hello,world!</>")
g

@app.route ('/login',methods=['get,post'])
def login():
    error=None
    if request.method=="post":
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
    
    else:

       error='invalid username/password'
    #the code below is executed if the request method
    #was get or thee credentials were invalid
    return render_template ('login.html',error=error)