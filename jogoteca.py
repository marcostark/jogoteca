from flask import Flask, render_template

app = Flask(__name__)

# Rota, caminho definido
@app.route('/inicio')
def ola():
    return render_template('lista.html')


app.run()

