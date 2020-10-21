import flask 
from flask import render_template, url_for, session, Flask, request
import mysql.connector as mys
import webbrowser
from threading import Timer 

app = Flask(__name__, static_folder = 'templates/static/')

app.secret_key = 'senha'

@app.route('/')

def login():
    session.pop('L', None)
    session.pop('P', None)
    return render_template('login.html')


@app.route('/logar', methods =  ['POST'])

def inicial():

    session.pop('L', None)
    session.pop('P', None)
    log, sen = request.form.getlist('login')
    
    db = mys.connect(host='localhost', user='root', password='###', database='database')
    curso = db.cursor()
    curso.execute('SELECT * FROM ident WHERE Login = "%s" AND Password = "%s";' % (str(log), str(sen)))
    result = curso.fetchall()
    print(result)
    if result == []:
        return render_template('login.html', msg = 0)   
    else:
        session["L"] = log
        session["P"] = sen
        nome_user = result[0][1]

        return render_template('resultado.html', us_na = nome_user)
    db.commit()
    db.close()
    curso.close()

@app.route('/new_user', methods = ['POST'])

def logado():

    return render_template('inicial.html')

@app.route('/novo_user', methods =  ['POST'])

def banco_dados():

    nome, sobrenome, idade, peso, altura, Login, Password = request.form.getlist('valores')
    db = mys.connect(host='localhost', user='root', password='###', database='database')
    curso = db.cursor()
    try:
        curso.execute('INSERT INTO ident(nome, sobrenome, idade, peso, altura, Login, Password) VALUES("%s", "%s", %d, %d, %d, "%s", "%s");' % (str(nome), str(sobrenome), int(idade), int(peso), int(altura), str(Login), str(Password)))
        curso.execute('INSERT INTO pass_logi(Login, Password) VALUES("%s", "%s");' % (str(nome), str(sobrenome)))    
    except:
        return render_template('login.html')
    finally:
        curso.close()
        db.commit()
        db.close()
        return render_template('login.html')

@app.route('/alterar')

def troca():
    return render_template('conf.html')

@app.route('/mudar', methods = ['POST'])

def mudar_():

    new_login, new_pass = request.form.getlist('mudar_l_s')
    db = mys.connect(host='localhost', user='root', password='###', database='database')
    curso = db.cursor()
    curso.execute('UPDATE ident SET Login = "%s", Password = "%s" WHERE Login = "%s";' % (str(new_login), str(new_pass), str(session['L'])))
    curso.close()
    db.commit()
    db.close()
    return render_template('login.html')

@app.route('/deletar', methods = ['POST'])

def deletar_():

    db = mys.connect(host='localhost', user='root', password='###', database='database')
    curso = db.cursor()
    curso.execute('DELETE FROM pass_logi WHERE Login = "%s";' % (str(session['L'])))
    curso.execute('DELETE FROM ident WHERE Login = "%s";' % (str(session['L'])))
    curso.close()
    db.commit()
    db.close()
    return render_template('login.html')

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(host = '127.0.0.1')