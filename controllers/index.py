import constants
from app import app
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        name = "none"
        return render_template(
            'index.html',
            name=name,
            program_list=constants.programs,
            subject_list=constants.subjects,
            len=len
        )
    else:
        print('!!!!!!!post')
        name = ""
        gender = ""
        program_id = 0
        subject_id = []
        subjects_select = []

        name = request.values.get('username')
        gender = request.values.get('gender')
        program_id = request.values.get('program')

        subject_id = request.values.getlist('subject[]')
        subjects_select = [constants.subjects[int(i)] for i in subject_id]

        return render_template(
            'index.html',
            name=name,
            gender=gender,
            program=constants.programs[int(program_id)],
            program_list=constants.programs,
            len=len,
            enumerate=enumerate,
            subjects_select=subjects_select,
            subject_list=constants.subjects
        )
