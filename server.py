from flask import (Flask,render_template)

app = Flask(__name__, static_folder='./assets', template_folder='./templates')

# app.run(debug=True, use_debugger=False, use_reloader=False)

@app.route('/')
def render_index():
    return render_template("index.jinja",name="home")

