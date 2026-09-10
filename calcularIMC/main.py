from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])

    imc = round(peso / (altura * altura),2)

    if imc < 18.5:
        diagnostico = 'Abaixo do peso'

    elif 18.5 <= imc < 25:
        diagnostico = 'Peso normal'

    elif 25 <= imc < 30:
        diagnostico = 'Sobrepeso'

    else:
        diagnostico = 'Obesidade'

    return render_template('index.html', imc=imc, diagnostico=diagnostico)

if __name__ == '__main__':
    app.run(debug=True)
