from todo import app
from flask import render_template, redirect, url_for, request

todos = []

@app.route('/', methods=['GET', 'POST'])
def show_todos():

    return render_template('todo.html', todos=todos)


@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    todo = request.form.get('new-todo')
    if todo != '':
        todos.append(todo)
        
    return redirect(url_for('show_todos'))


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_todo(id):
    del todos[id]
    
    return redirect(url_for('show_todos'))
