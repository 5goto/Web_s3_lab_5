from flask import Flask, render_template, url_for


app = Flask(__name__)

import controllers.index
import controllers.hello
import controllers.subject

if __name__ == '__main__':
    app.run(debug=True)
