from flask import Flask,render_template, request, redirect, url_for
from create_db import create_user_entries,get_users,insert_user_entries
app=Flask(__name__)

@app.route('/')
def welcome_page():
    return "Please visit /users endpoint"


@app.route('/users', methods=['GET','POST'] )
def show_users():

     if request.method=='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            insert_user_entries(name,email)
            return redirect(url_for('show_users'))

     users=get_users()
     return render_template('users.html',users=users)



if __name__=='__main__':
     create_user_entries()
     app.run(debug=True)
