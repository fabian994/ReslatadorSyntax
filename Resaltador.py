
#import re

#------------------------Abre archivo con claves------------------------------
f = open("lexico_python.txt", "r")
reserv=f.readline()
reserv=reserv.strip()
reserv=reserv.split()
coment=f.readline()
opera=f.readline()

reservadas=[]
reservadas.append(reserv)
f.close()
#--------------------------------------------------------------

#------------------------Crea HTML------------------------------
f = open("salida.html", "w")
f.write("<!DOCTYPE html>\n")
f.write("<meta charset='UTF-8'>\n")
f.write("<title>Salida</title>\n")
f.write("<link href='estilos.css' rel='stylesheet' type='text/css'>\n")
f.writelines(["</head>\n", "<body>\n"])
f.close()
#--------------------------------------------------------------

#data = input("Escribe el nombre de un archivo de texto Ejemplo: ('archivo.txt'): ")
data="prueba.py"
with open(data) as f:
    contents = f.read()
    print(contents)
    s = contents
    s = s.split("\n")
    print(s)
    print("---------------------------------------------------------------------")

Lexema = ""
token = ""
p = 0




f = open("salida.html", "w")
f.write("<p>hola </p>\n")
f.write("<p class='comentario'> //Prueba con comentario </p>\n")

#---------------Cierra HTML-----------------------------
f.writelines(["</body>\n</html>"])
f.close()
#-------------------------------------------------------
