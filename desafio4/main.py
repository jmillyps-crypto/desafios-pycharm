from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idade_pet', methods=['POST'])
def idade_pet():
    ano = float(request.form['ano'])

    idade = 24 + (ano - 200) * 5

    return render_template('index.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)