from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_moeda', methods=['POST'])
def converter_moeda():
    reais = float(request.form['reais'])

    dolar = reais / 5.40

    return render_template('index.html', dolar=dolar)

if __name__ == '__main__':
    app.run(debug=True)
