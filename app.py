from flask import Flask, render_template, request, redirect,url_for,flash
# redirect,url_for se hace un redireccionamineto 
from flask_mysqldb import MySQL

#inicialisacion del servidor flask
app= Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="papeleria"

app.secret_key = 'mysecretkey'
mysql = MySQL (app)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/utiles')
def utiles():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from utiles')
    #creamos la variable consulta para crear la lista que se va a desplegar en vista
    consulta=curSelect.fetchall() #fetchall para jalar la lista completa de registros
    #print(consulta)
    return render_template('utiles.html', utiles=consulta)

@app.route('/empleados')
def empleados():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from empleados')
    #creamos la variable consulta para crear la lista que se va a desplegar en vista
    consulta=curSelect.fetchall() #fetchall para jalar la lista completa de registros
    #print(consulta)
    return render_template('empleados.html', empleados=consulta)

#Guardar en empleados

@app.route('/guardar',methods=['POST']) ##Una segunda ruta o más ya pueden tener otros nombres.
def guardar(): 
    if request.method == 'POST':
        Vn=request.form['nombre']
        Vpp=request.form['app']
        Vpm=request.form['apm']
        Vc=request.form['cargo']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into empleados(nombre,app,apm,puesto) values (%s,%s,%s,%s)',(Vn,Vpp,Vpm,Vc))
        mysql.connection.commit()
        
    flash('Articulo agregado correctamente')
    return redirect(url_for('index'))

@app.route('/guardaru',methods=['POST']) ##Una segunda ruta o más ya pueden tener otros nombres.
def guardaru(): 
    if request.method == 'POST':
        Vn=request.form['nombre']
        Vpp=request.form['clas']
        Vpm=request.form['canti']
        Vc=request.form['pres']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into utiles(nombre,clasificacion,cantidad,precio) values (%s,%s,%s,%s)',(Vn,Vpp,Vpm,Vc))
        mysql.connection.commit()
        
    flash('Articulo agregado correctamente')
    return redirect(url_for('index'))


@app.route('/actualizarr', methods=['POST'])
def actualizarr():
    if request.method == 'POST':
        Vfruta = request.form['nombre']
        Vtemp = request.form['clasificacion']
        Vprecio = request.form['cantidad']
        Vstoc = request.form['precio']

        curAct=mysql.connection.cursor()
        curAct.execute('update utiles set clasificacion=%s, cantidad=%s, precio=%s where nombre = %s', (Vfruta, Vtemp, Vprecio,Vstoc))
        mysql.connection.commit()

    return redirect(url_for('utiles'))

@app.route('/actulaizar')
def actulaizar():
    return render_template('editar.html')




if __name__=='__main__':
    app.run(port= 5001, debug=True) #debug=true activaactualizacion 