import constants
from app import app
from flask import render_template, request


@app.route('/subject/<sub>')
def subject(sub):
    return render_template(
        'subject.html',
        sub=sub,
        discription=constants.subject_dict[sub]
    )
