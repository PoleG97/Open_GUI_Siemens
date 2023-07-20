import snap7

# Pedimos informacion de la conexion
rack = input("Introduce el rack: ")
slot = input("Introduce el slot: ")
ip = input("Introduce la IP: ")

# Creamos y realizamos la conexion con el PLC
plc = snap7.client.Client()
plc.connect(ip, rack, slot)

# Conectamos con las bases de datos que queramos leer