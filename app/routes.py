from flask import render_template, jsonify, request
from app import app
from .forms import QuestionForm
from app import run

@app.route('/')
def home():
    form = QuestionForm()
    context = {
        "form": form,
        "title": "Contactez Grandpy!"
    }
    return render_template('grandpy.html', **context)

@app.route('/api')
def api():
    question = request.args.get('question', default='', type=str)
    answer = run.get_infos_on_place(question)
    return jsonify(answer)