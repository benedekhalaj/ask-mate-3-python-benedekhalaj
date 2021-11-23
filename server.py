from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route('/')
@app.route("/list")
def list_questions():
    questions = data_manager.get_questions()
    return render_template('list.html', questions=questions)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        
        return redirect('/')
    return render_template('add_question.html')






if __name__ == "__main__":
    app.run(host='0.0.0.0',
            debug=True,
            port=8000)
