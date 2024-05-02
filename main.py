from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado="")

@app.route('/resultado', methods=['POST'])
def resultado():
    media = 0
    x = 1
    qtd = int(input("Informe a quantidade de pessoas: "))
    while x <= qtd:
        temp = float(input("Informe a temperatura: "))
        media += temp

    if (temp <= 37.2):
        resultado = "temp normal"

    elif ((temp > 37.3) and (temp <= 38)):
        resultado = "Estado febril"

    elif ((temp > 38) and (temp <= 39)):
        resultado = "Com febre"

    else:
        resultado = "Febre alta"
    x = x + 1
    print('quantidade ', qtd)
    print('media ', media / qtd)

    return render_template('index.html', resultado=f'0 número {numero} é {resultado}')
if __name__ == '__main__':
    app.run(debug=True)
