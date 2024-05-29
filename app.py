from flask import Flask, render_template, request, redirect
from model import fake_news_det as fnd

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/reload_redirect')
def reload_redirect():
    return redirect('/home')

@app.route('/read_form', methods=['POST'])
def read_form():
    data = request.form
    df = data['msg']
    op = fnd(df)  
    response = "True" if op else "False"
    return render_template('home.html', response=response)






if __name__ == '__main__':
    app.run(debug=True, port=5000)

