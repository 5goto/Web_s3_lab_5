import constants
from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template(
        'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        len=len
    )
