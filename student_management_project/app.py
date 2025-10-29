from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list of students (no database)
students = [
    {'id': 1, 'name': 'Meghana', 'age': 19, 'address': 'Bangalore'},
    {'id': 2, 'name': 'Sanjana', 'age': 18, 'address': 'Bangalore'},
    {'id': 3, 'name': 'Keerthana', 'age': 20, 'address': 'Bangalore'},
    {'id': 4, 'name': 'Anu', 'age': 19, 'address': 'Bangalore'}
]

# -----------------------
# ROUTES
# -----------------------

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':
        new_id = max([s['id'] for s in students]) + 1 if students else 1
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']

        students.append({'id': new_id, 'name': name, 'age': int(age), 'address': address})
        return redirect(url_for('index'))
    return render_template('add_student.html')



@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['age'] = int(request.form['age'])
        student['address'] = request.form['address']
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    global students
    students = [s for s in students if s['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
