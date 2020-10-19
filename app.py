from flask import Flask, render_template, request

app = Flask(__name__)

student_list = [{                           
    'name':'ebulfez',
    'surname':'beydullayev',
    'gender':'male',
    'status':'active',
    'image':"/static/images/index.jpeg",
    'bio':'Oxumuram el cekin'  
},
    {'name':'Isfendiyar',
    'surname':'Ebejdadli',
    'gender':'male',
    'status':'active',
    'image': "/static/images/isfendiyar.jpeg",
    'bio': 'Kitab oxumaq saglamliginiza ziyandir'
},
    {'name':'Gulpike',
    'surname':'Imishlili',
    'gender':'female',
    'status':'negative',
    'image':"/static/images/gulpike.jpeg",
    'bio': 'Ag atli shehzademi gozleyirem'

}
] 
@app.route('/students/')
def students():
    return render_template('students.html', student_list = student_list)




#detail#
@app.route('/student/<int:student_index>')
def student(student_index):
   
    student = student_list[student_index]

    
    return render_template('student.html', student_detail = student)    