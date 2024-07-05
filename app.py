from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

 # Importamos el módulo database.py
import database as db

project_dir = os.path.dirname(os.path.abspath(__file__))  # Project directory (where app.py is located)
template_dir = os.path.join(project_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'cac'

#rutas de la aplicación

@app.route('/')
def index():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM recetas")
    recetas = cursor.fetchall()
    logged_in = session.get('logged_in', [False])
    print(recetas[3])
    return render_template('index.html', logged_in=logged_in, recetas=recetas)




#ruta para mostrar el formulario de registro
@app.route('/register')
def register():
    logged_in = session.get('logged_in', [False])
    return render_template('users.html', logged_in=logged_in)

#ruta para guardar un usuario
@app.route('/usuarionuevo', methods=['POST'])
def save_user():
    usuario = request.form['username']	
    contraseña = request.form['password']	

    if usuario and contraseña:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (nombre, contraseña) VALUES (%s, %s)"
        data = (usuario, contraseña)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('index'))

#ruta para mostrar el formulario de login
@app.route('/login')
def login():
    logged_in = session.get('logged_in', [False])
    return render_template('login.html', logged_in=logged_in)

#inicio de sesión
@app.route('/login', methods=['POST'])
def login_user():
    usuario = request.form['username']
    contraseña = request.form['password']

    cursor = db.database.cursor()
    sql = "SELECT * FROM users WHERE nombre = %s AND contraseña = %s"
    data = (usuario, contraseña)
    cursor.execute(sql, data)
    user = cursor.fetchone()

    if user:
        session['logged_in'] = [True, user[0], user[1]]        
        print(login)
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

#cerrar sesión
@app.route('/logout')
def logout():
    session['logged_in'] = [False]
    return redirect(url_for('index'))

#ruta para editar la contraseña del usuario
@app.route('/changepassword')
def change_password():
    logged_in = session.get('logged_in', [False])
    return render_template('editUser.html', logged_in=logged_in)

#ruta para guardar la nueva contraseña
@app.route('/changepassword', methods=['POST'])
def save_password():
    usuario = session['logged_in'][1]
    contraseñaInp = request.form['password']
    nueva_contraseña = request.form['newpass']
    
    try:
        cursor = db.database.cursor()
        # Obtener la contraseña actual del usuario
        cursor.execute("SELECT contraseña FROM users WHERE id = %s", (usuario,))
        contraseñaDb = cursor.fetchone()[0]
        
        # Comparar la contraseña actual ingresada con la almacenada en la base de datos
        if contraseñaInp == contraseñaDb:
            # Si coinciden, actualizar la contraseña
            sql = "UPDATE users SET contraseña = %s WHERE id = %s"
            data = (nueva_contraseña, usuario)
            cursor.execute(sql, data)
            db.database.commit()
            return redirect(url_for('index'))
        else:
            flash('La contraseña actual es incorrecta.')  
            return redirect(url_for('change_password')) 
    except Exception as e:
        print(e)
        flash('Error al actualizar la contraseña.')
        return redirect(url_for('change_password')) 

#ruta para borrar usuario
@app.route('/deleteuser/<int:id>')
def delete_user(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    data = (id, )
    cursor.execute(sql, data)
    db.database.commit()
    session.pop('logged_in', None)
    return redirect(url_for('index'))

#ruta para mostrar recetas detalle
@app.route('/detalle/<int:id>')
def detalle(id):
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM recetas WHERE id = %s", (id,))
    receta = cursor.fetchone()
    return render_template('Receta-detalle.html', receta=receta)


# #crear recetas
# @app.route('/crearreceta')
# def crearreceta():
#     return render_template('crearreceta.html')

# #guardar recetas
# @app.route('/recetanueva', methods=['POST'])
# def save_receta():
#     titulo = request.form['titulo']
#     descripcion = request.form['descripcion']
#     ingredientes = request.form['ingredientes']
#     preparacion = request.form['pasos']
#     imagen = request.form['foto']

#     if titulo and descripcion and ingredientes and preparacion and imagen:
#         cursor = db.database.cursor()
#         sql = "INSERT INTO recetas (nombre, preparacion, imagen) VALUES (%s, %s, %s)"
#         data = (nombre, preparacion, imagen)
#         cursor.execute(sql, data)
#         db.database.commit()
#         return redirect(url_for('index'))
if __name__ == '__main__':
     app.run(debug=True, port=8000)