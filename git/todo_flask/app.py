from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

with app.app_context():
    db.create_all()
    # new_todo = ToDo(title="todo1", complete=False)
    # db.session.add(new_todo)
    # db.session.commit()

#CONCEPT 1: Routing
@app.route('/')
def home():
    todo_list = ToDo.query.all()
    print(todo_list)
    #CONCEPT 2: Templates
    return render_template('base.html', todo_list=todo_list)

@app.route('/add', methods = ["POST"])
def add():
    title = request.form.get("title")
    new_todo = ToDo(title= title, complete=False)
    #CONCEPT 3: Sessions
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)