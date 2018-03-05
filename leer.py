
#!/usr/bin/python

# Importamos la libreira de PySerial
import serial
import mysql.connector


# Abrimos el puerto del arduino a 9600
PuertoSerie = serial.Serial('/dev/ttyACM0', 57600, timeout=3.0)
# Creamos un buble sin fin
while True:
  # leemos hasta que encontarmos el final de linea
  xdk = PuertoSerie.readline()
  #Convertimos la lectura a variable flotante y convertimos a grados
  T= float(xdk.rstrip('\n'))/1000
  # Mostramos el valor leido y eliminamos el salto de linea del final
  # print  xdk.rstrip('\n')
  print T
  cnx=mysql.connector.connect(user='boschdb', password='robertbosch2018',host='boschdb.cyqvrdghzceg.us-east-1.rds.amazonaws.com', database='sensores')
  cursor=cnx.cursor()
  add_temp=("INSERT INTO temperatura (temperatura) VALUES (%(data_temp)s)")
  data={'data_temp':T}
  cursor.execute(add_temp,data)
  cnx.commit()
 # cursor.close()
 # cnx.close()
 #xdk.close()	
 #cnx.close()
