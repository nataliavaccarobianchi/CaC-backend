import mysql.connector

#database = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="",
    #database="cacrecetas"
    
 #   host="viaduct.proxy.rlwy.net",
   # user="root",
   # port=48486,
   # password="iqXIMyVbjTMFQbbbkbHYbAhxEEZDjmLr",
   # database="railway"
#)
try:
    database = mysql.connector.connect(
        host="viaduct.proxy.rlwy.net",
        user="root",
        port=48486,
        password="iqXIMyVbjTMFQbbbkbHYbAhxEEZDjmLr",
        database="cacrecetas"
    )
    print("Conexión establecida correctamente.")
    
    # Aquí puedes continuar con el resto de tu lógica para interactuar con la base de datos
    
except mysql.connector.Error as err:
    print(f"Error al conectarse a la base de datos: {err}")
    # Aquí puedes manejar el error de conexión de acuerdo a tus necesidades

finally:
    if 'database' in locals() and database.is_connected():
        database.close()
        print("Conexión cerrada.")
# Rest of your code goes here