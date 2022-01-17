# 1.1 Ejercicios resueltos de variables
# 1 :
def ejer1_1():
    a = 46
    a = 15
    a = 30


# Respuesta: Las variables que presenta el pgrama es X= 15 ya que es el ultimo valor guardado y x=30
# ya que hay una diferencia entre mayuscula y minuscula.append()

# 2:
def ejer2_1():
    a = 10 * 2
    a -= 5


# Respuesta: Lo que la variable esta conteniendo es el numero 15, en la primera asiganacion
# de 10*2 daria 20 pero en la declaracion de abajo dice que al valor antes contenido se
# le reste 5 unidades (20 -5) dando asi el numero 15


# 3:
def ejer3_1():
    a = 10 - 2
    10 + 2


# Respuesta: X al final contiene el numero 8 ya que la suma que estaba abajo de la variable no afecta
# debido a que no se especifica en donde se va a contener

# 4:
def ejer4_1():
    y = 3 * (4 + 2)
    x = y + 2
    z = 5
    x = y - z


# Respuesta: X al final contiene el numero 13 debido a que al final X contiene el resultado de la
# resta entre Y y Z el cual Y = 18 y Z = 5 haciendo resta de variables dentro de otra variable.


# 5:
def ejer5_1():
    x = 25
    x + 10


# Respuesta: X al final contiene el numero 25 esto debido a que en la declaracion de X+10
# no se suma el 10 a los 25 contenido con aterioridad esto debido a que està mal digitada debio ser (X+=10)


# 6:
def ejer5_1():
    x = 3
    y = x + 6
    x = y + 1


# Respuesta: AL final X contiene el numero 10 debido a que X =Y+1 y en eso Y = 9, dando asi el resultado.


# 2.1 Ejercicios resueltos de tipos de datos
# 1:
100 / 5
# Respuesta:EL tipo de variable que se contiene es: float

# 2:
7 / 2
# Respuesta:EL tipo de variable que se contiene es:float

# 3:
7 // 2
# Respuesta:EL tipo de variable que se contiene es: int

# 4:
7 % 2
# Respuesta:EL tipo de variable que se contiene es: int

# 5:
"tiza" + "."
# Respuesta:EL tipo de variable que se contiene es: str

# 6:
"hola"[1 + 1]
# Respuesta:EL tipo de variable que se contiene es: str

# 7:
len("hola")
# Respuesta:EL tipo de variable que se contiene es: int

# 8:
int("145")
# Respuesta:EL tipo de variable que se contiene es: int

# 9:
float("145")
# Respuesta:EL tipo de variable que se contiene es: float

# 10:
float(145)
# Respuesta:EL tipo de variable que se contiene es: float

# 11:
str(32)
# Respuesta:EL tipo de variable que se contiene es: str

# 12:
1 + 2 != 3
# Respuesta:EL tipo de variable que se contiene es: False

# 13:
177 % 2 == 0
# Respuesta:EL tipo de variable que se contiene es: False

# 14:
len("nube") <= 20
# Respuesta:EL tipo de variable que se contiene es: True

# 15:
n = 167 / 10
# Respuesta:La variable: 16.7

# 16:
n = 167 // 10
# Respuesta:La variable: 16

# 17:
n = 167 % 10
# Respuesta:La variable: 7

# 18:
letra = "a"
# Respuesta:La variable: a

# 19:
saludo = "hola" + letra
# Respuesta:La variable: holaa

# 20:
C = saludo[0]
# Respuesta:La variable: h

# 21:
C = saludo[1 + 3]
# Respuesta:La variable: a

# 22:
L = len(saludo)
# Respuesta:La variable: 5

# 23:
C = saludo[len(saludo) - 1]
# Respuesta:La variable: a

# 24:
menor = "a" < "b"
# Respuesta:La variable: True

# 25:
D = 1 != 1
# Respuesta:La variable: False

# 25:
D = "cinta" >= "canto"
# Respuesta:La variable: True

# 27
c = "z" + "a" + "paz"[0]
# Respuesta:La variable: "zap"

# 28:
x = c[0] == "z"
# Respuesta:La variable: True

# 29:
11 - (4 % 2 + 10)
# Respuesta: No arroja error

# 30:
"30" + 2
# Respuesta: Arroja error (No se peuden sumar una variable in con una str)

# 31
"30" + "2"
# Respuesta: No arroja error

# 32:
"hola"[len("hola")]
# Respuesta: Arroja error

# 33:
len(124)
# Respuesta: Arroja error porque el metodo len es un metodo para ina variable str

# 34:
"hola"[len("fin")]
# Respuesta: No arroja error

# 35:
"hola"[11 - (4 % 2 + 10)]
# Respuesta: No arroja error

# 36:
int("4")
# Respuesta: No arroja error

# 37:
int(4)
# Respuesta: No arroja error

# 38:
int("z")
# Respuesta: Arroja error

# 39:
int("4.")
# Respuesta: Arroja error

# 40:
4 < "f"
# Respuesta: Error de comparar un int con un str

# 41:
"palabra" = "rama"
# Respuesta: Arroja error (Asignacion)

# 42:
"palabra" == "rama"
# Respuesta: No arroja error (False)

# 3.1 Ejercicios resueltos con tablas de verdad

# 1:
not (True)
# Respuesta: Muestra False

# 2:
not (1 + 2 != 3)
# Respuesta: Muestra True

# 3:
x = (len("jugar") > 5) and (len("jugar") < 10)
# Respuesta: Muestra False

# 4:
"alto"[2] == "t" and x
# Respuesta: Muestra False

# 5:
842913 % 10 != 3 and len("cafe") == 3
# Respuesta: Muestra False

# 6
0 != 0 or "a" < "y"
# Respuesta: Muestra True

# 7:
True or int("50") >= 50
# Respuesta: Muestra True

# 8:
edad = 20
not (x) or edad % 2 == 0
# Respuesta: Muestra True

# 9:
es_cliente = False
not (es_cliente and not (edad < 18))
# Respuesta: Muestra True


# 10:
# EL numero no puede ser menor que 0 ni mayor que 100:
numero < 0 and numero > 100
# Correccion: numero >=0 and numero<=100

# 11:
# La edad debe estar entre 10 y 20
edad > 10 and < 20
# Correccion: edad >10 and edad<20


# 12:
# La longitud de la cadena no debe ser superior a 10 caracteres
cad = 0
len(cad) < 10
# !Respuesta: len(cadena)<=10

# 13:
# EL numero es multiplo de 4 y tambien es negativo
# Resouesta: numero %4 == 0 and numero < 0

# 14:
# Decidiste comprar un auto usado, pero debe cumplir ciertas condiciones:
# EL kilometraje debe ser menor a 30000 y el modelo debe estar entre 2015 y 2017
# Respuesta: km<30000 and (modelo>=2015 and modelo<=2017)

# 15:
# Una agrupacion academica tiene ciertos requisitos para cualquier estudiante que
# desea ingresar:
# Debe tener màs de 30% de sus estudios completos y no debe ser miembro de otra
# agrupacion academica en la misma universidad.
# Respuesta: porcentaje_completo > 30 and not (miembro_agrupacion)

# 16:
# Una persona pasa frio si es invierno y ademas no tiene calefacciòn ni esta abrigada
# respuesta: es_invierno and not tiene_calefacciòn and not esta_abrigada
# es_invierno and not(tiene_calefaccion or esta_abrigada)

# 4.1 Ejercicios resueltos de strings

cade = "si, profe, es cierto... yo me comi la tarea"

cadena[10]  # Respuesta: " "
cadena[-1]  # Respuesta: a
cadena[0:9]  # Respuesta: si, prof
cadena[::3]  # Respuesta: s o,sit.ymciaaa

s = "   hola, ¿como estas?"
# 1:
s[::-1]
# Respuesta: ?satse omoc¿ ,aloh

# 2:
s[len(s)]
# Respuesta: error

# 3:
s.count("o")
# Respuesta: 2

# 4:
s.count("Hola")
# Respuesta: 0

# 5:
s[-4]
# Respuesta: tas

# 6:
s[15:]
# Respuesta: estas?

# 7:
s.find("o")
# Respuesta: 4

# 8:
s.strip()
# Respuesta: hola, ¿como estas?

# 9:
x = s.upper()  # Respuesta: False
x == s
# Respuesta: False

# 10:
s[14:].upper
# Respuesta: " ESTAS?"

# 11:
len(s) % 2 != 0
# Respuesta:

# 12:
s.replace(" ", "*")
# Respuesta:"***hola,*¿como*estas?"

# 13:
s.replace("z", "Z")
# Respuesta: "   hola, ¿como estas?"


X = "programar en python"
# Dada la variable X de tipo string ¿como se puede hallar el indice del ultimo caracter?
# Respuesta: X[-1]

# Dada la variable cadena="hola" ¿que retorna cadena.find("2")
# Respuesta: -1

# ¿Que retorna? "a" in "dàtiles"
# Respuesta: False

# ¿Que operaciones retorna la cantidad de espacios de la cadena "Me gusta programar"
# Respuesta: 2

# ¿Por que da error? cadena[0]="H"
# Respuesta: Es porque los string son inmutables cuando estan dentro de una variable

# ¿Que almacena la siguiente variable? nueva="C"+cadena[1:]
# Respuesta: "Cola"

# ¿Como reemplazar las vocales acentuadas por vocales no acentuadas en la cadena X?
# Respuesta: con el metodo .replace en las variables string cambiando las vocales por vocales con tilde

# ¿Que comparacion podria hacerse para averiguar si la longitud de la cadena es par?
# Respuesta:

# ¿De que forma se puede obtener la cantidad de vocales de la cadena X?
# Respuesta: poner un contador asi: X.cont(vocal que se desea contar)

# 5.1 Ejercicios resueltos de input y print
# 1:
nombre = []
A = input(nombre, "¿cual es tu cancion favorita?")
# Solucion: print(nombre, "¿Cual es tu edad?")
# A=input

# 2:
precio = input("Precio")
total = precio + (precio * 0.10)
# Solucion: precio=float(input("Precio:"))
# total=precio+(precio*0.10)

# 3:
edad = int(input("Edad:"))
print("tu edad es, edad")
# Solucion edad=int(input("Edad:"))
# print("tu edad es ", edad)

# 4:
edad = int(input("Edad:"))
print("Veamos si tu edad es 18...", edad=18)
# Solucion: edad=int(input("Edad:"))
# print("Veamos si tu edad es 18...", edad==18)

# Solicitar al usuario que ingrese su nombre. EL nombre se debe almacenar en una variable llamda N.
# A continuacion se debe mostrar en pantalla el texto "Ahora estàs en la matrix, [usuario]", donde
# se reemplazara el nombre que el usuario haya ingresado.

# Solucion:
N = str(input("Ingrese su nombre: "))
print("Ahora estàs en la matrix, ", N)

# Hacer un programa que solicite al usuario cuanto costo una cena en un restaurante. A ese valor, sumarle un 6.2%.
# A ese valor, sumarle un 6.2% en conceptos de servicio. Imprimir en pantalla el monto final a pagar

Costo_cena = float(input("Ingrese el valor de la cena: "))
Total = Costo_cena + (Costo_cena * 0.162)
print("EL valor total a pagar incluido el servicio y la propina es: ", Total)

# !Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una variable
# !numerica (en total, tres variables diferentes). finalmente, mostrar la fecha en formato dd/mm/aaaa

# !Hacer otra version del programa, pero esta vez almacenando todo an una unica variable numerico, en la forma DDMMAAAA.
# !¿Y si la variable fuera de tipo string?.

dia = int(input("Dia de tu nacimiento: "))
mes = int(input("Mes de tu nacimiento: "))
año = int(input("Año de tu nacimiento: "))
print(dia, "/", mes, "/", año)

fecha = input("Fecha en formato DDMMAAAA: ")
dia = fecha[:2]
mes = fecha[2:4]
año = fecha[4:]
print(dia, "/", mes, "/", año)

# !Una pareja de motociclistas necesita hacer ciertos calculos antes de emprender un viaje en moto, para saber cuantos
# !tanques de emprender un viaje en moto, para saber cuantos tanques de combustibles consumira el viaje entero.
# !Para eso deben ingresar: cuantos kilometros puede recorrer su moto con 1 litro de combustible, que capacidad (en litro)
# !tiene el tanque y cuantos kilometros en total recorreran.
# !Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustibles necesarios.

capacidad = float(input("Capacidad del tanque: "))
kmxl = float(input("Rendimiento (km por litro): "))
recorrido = float(input("Km totales a recorrer: "))
kmxtanque = capacidad * kmxl
print("seran necesarios", recorrido / kmxtanque, "tanques.")

# 5.2 Ejercicio resuelto de input y print
# 1:
# !Un empresario que se dedica al espectaculo necesita un programa que le ayude a hacer ciertos calculos cada
# !vez que organiza un concierto en un estadio deportivo.
# !Lo primero que necesita saber es que capacidad de publico tendra cada concierto, para saber cuantas entradas o boletos tienen que imprimirse.
# !Para eso cuando contrata un estadio deportivo, pregunta cuantos metros cuadrados tiene. El sabe que, por metro cuadrado,
# !caben 4 personas. Tambien sabe que siempre hay un espacio con gradas y que normalmente estas ocupan un 20% de los metros
# !cuadrados totales. En cada estadio las gradas pueden ser diferentes, asi que el empresario consulta cuantas gente cabe en ellas.
# !Cuando contra a la banda que dara el concierto, esta le indica que porcentaje del espacio disponible necesitan ellos
# !para mostrar su escenario.
# !Con estos datos, debe calcularse cuanta gente va a caber en el estadio para un concierto determinado. El empresario, cada vez que
# !use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrato, la cantidad de gente que
# !cabe en las gradas y el porcentaje de espacio ocupado por el escenario.
# !Luego, el quiere saber cuanto dinero ingresaria si vende todas las entradas disponibles, sabiendo que el 30% de las entradas
# !vendidas seran "a precio especial" y el resto son "a precio comun." EL empresario ingresa el precio de cada tipo de entrada
# !cuando usa el programa.

CAPACIDADM2 = 4
PORCENTAJEGRADAS = 0.2
PORCENTAJEESPECIALES = 0.3
PORCENTAJESCOMUNES = 0.7

dimensiones = float(input("Dimensiones del estadio (en m2): "))
personasengradas = int(input("capacidad de personas que caben en las gradas: "))
porcentajeescenario = int(input("Porcentaje que ocupa el escenario: "))
m2gradas = dimensiones * PORCENTAJEGRADAS
m2escenario = dimensiones * (porcentajeescenario / 100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasengradas
print("Caben", personastotales, "personas")
percioentradasespecial = float(input("Precio entrada especial: "))
precioentradacomun = float(input("Precio entrada comun: "))
print("Ingreso total de ventas: $",
      (personastotales * PORCENTAJEESPECIALES) * percioentradasespecial +
      (personastotales * PORCENTAJESCOMUNES * precioentradacomun))

>> > edad = 16
>> > edad > 10 and edad < 20
True
>> > edad > 20 and edad < 30
False
>> > edad > 20 or edad < 20
True
>> > es_cliente = True
>> > type(es_cliente)
<

class 'bool'>

>> > es_cliente and edad > 18
False
>> > es_cliente
True
>> > not es_cliente
False
>> >

>> > not True
False
>> > not (1 + 2 != 3)
True
>> > x = (len("jugar") > 5) and (len("jugar") < 10)
>> > x
False
>> > "alto"[2] == "t" and x
False
>> > 842913 % 10 != 3 and len("café") == 3
False
>> > 0 != 0 or "a" < "y"
True
>> > True or int("50") >= 50
True
>> > edad = 20
>> > not (x) or edad % 2 == 0
True
>> > es_cliente = False
>> > not (es_cliente and not (edad < 18))
True
>> >

>> > cadena = "programación en python"
>> > cadena[6]
'm'
>> > len(cadena)
22
>> > cadena[21]
'n'
>> > i = len(cadena) - 1
>> > cadena[i]
'n'
>> > i
21
>> > cadena[len(cadena) - 1]
'n'
>> > cadena[0:10]
'programaci'
>> > cadena[10:]
'ón en python'
>> > cadena[:10]
'programaci'
>> > cadena[:13]
'programación '
>> > cadena[:13:2]
'pormcó '
>> > cadena[::2]
'pormcó npto'
>> > cadena[::-1]
'nohtyp ne nóicamargorp'
>> > cadena[-1:]
'n'
>> > cadena.find("python")
16
>> > cadena.find("p")
0
>> > cadena.find("z")
-1
>> > cadena.find("z") == -1
True
>> > "python" in cadena
True
>> > precio = "40"
>> > int(precio)
40
>> > type(int(precio))
<

class 'int'>

>> > cadena.upper()
'PROGRAMACIÓN EN PYTHON'
>> > cadena.lower()
'programación en python'
>> > cadena
'programación en python'
>> > "6709".upper()
'6709'
>> > cadena.title()
'Programación En Python'
>> > cadena.capitalize()
'Programación en python'
>> > a = "      hola"
>> > a.strip()
'hola'
>> > a = "     hola    chau     "
>> > a.strip()
'hola    chau'
>> > cadena
'programación en python'
>> > cadena.count("p")
2
>> > cadena.count("o")
2
>> > cadena.replace("python", "***")
'programación en ***'
>> > cadena
'programación en python'
>> > cadena.replace("a", "-")
'progr-m-ción en python'
>> > cadena.replace("z", "i")
'programación en python'
>> > cadena.replace("ó", "o")
'programacion en python'
>> >

>> > cadena = "sí, profe, es cierto... yo me comí la tarea"
>> > cadena[10]
' '
>> > cadena[-1]
'a'
>> > cadena[0:9]
'sí, profe'
>> > cadena[::3]
's o,sit.ymcíaaa'
>> > cadena[::-1]
'aerat al ímoc em oy ...otreic se ,eforp ,ís'
>> > cadena[4:9]
'profe'
>> >

>> > s = "   hola, ¿cómo estás?"
>> > s[::-1]
'?sátse omóc¿ ,aloh   '
>> > s[len(s)]
Traceback(most
recent
call
last):
File
"<pyshell#149>", line
1, in < module >
s[len(s)]
IndexError: string
index
out
of
range
>> > s[len(s) - 1]
'?'
>> > s.count("o")
2
>> > s.count("Hola")
0
>> > s[-4:]
'tás?'
>> > s.find("o")
4
>> > s.strip()
'hola, ¿cómo estás?'
>> > x = s.upper()
>> > x == s
False
>> > x
'   HOLA, ¿CÓMO ESTÁS?'
>> > s
'   hola, ¿cómo estás?'
>> > s[14:].upper()
' ESTÁS?'
>> > s
'   hola, ¿cómo estás?'
>> > len(s) % 2 != 0
True
>> > len(s)
21
>> > s.replace(" ", "*")
'***hola,*¿cómo*estás?'
>> > s.replace("z", "Z")
'   hola, ¿cómo estás?'
>> >

>> > X = "programar en python"
>> > X[-1]
'n'
>> > X[len(X) - 1]
'n'
>> > cadena = "hola"
>> > cadena.find("2")
-1
>> > "a" in "dátiles"
False
>> > "me gusta programar".count(" ")
2
>> > "me gusta programar".find(" ")
2
>> > cadena[0] = "H"
Traceback(most
recent
call
last):
File
"<pyshell#175>", line
1, in < module >
cadena[0] = "H"
TypeError: 'str'
object
does
not support
item
assignment
>> > nueva = "C" + cadena[1:]
>> > nueva
'Cola'
>> > X
'programar en python'
>> > X = "hoy es día miércoles"
>> > X.replace("í", "i")
'hoy es dia miércoles'
>> > X
'hoy es día miércoles'
>> > X.replace("í", "i").replace("é", "e")
'hoy es dia miercoles'
>> > X
'hoy es día miércoles'
>> > X.count("a") + X.count("e") + X.count("i") + X.count("o") + X.count("u")
6
>> >

N = input("tu nombre: ")
print("Ahora estás en la matrix, ", N)

costo = float(input("costo de la cena: $"))
servicio = costo * 0.062
propina = costo * 0.1
print("costo total de la comida: $", costo + servicio + propina)

fecha = input("Fecha en formato DDMMAAAA: ")
dia = fecha[:2]
mes = fecha[2:4]
anio = fecha[4:]
print(dia + "/" + mes + "/" + anio)

capacidad = float(input("Capacidad del tanque: "))
kmxl = float(input("Rendimiento (km por litro): "))
recorrido = float(input("Km totales a recorrer: "))
kmxtanque = capacidad * kmxl
print("Serán necesarios", recorrido / kmxtanque, "tanques.")

CAPACIDADM2 = 4
PORCENTAJEGRADAS = 0.2
PORCENTAJEESPECIALES = 0.3
PORCENTAJECOMUNES = 0.7

dimensiones = float(input("Dimensiones del estadio (en m2) : "))
personasengradas = int(input("Cantidad de personas que caben en las gradas: "))
porcentajeescenario = int(input("Porcentaje que ocupa el escenario: "))
m2gradas = dimensiones * PORCENTAJEGRADAS
m2escenario = dimensiones * (porcentajeescenario / 100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasengradas
print("Caben", personastotales, "personas")
precioentradaespecial = float(input("Precio entrada especial: $"))
precioentradacomun = float(input("Precio entrada común: $"))
print("Ingreso total de ventas: ",
      (personastotales * PORCENTAJEESPECIALES) * precioentradaespecial +
      (personastotales * PORCENTAJECOMUNES) * precioentradacomun)

############### Ejercicio 15 ###############
numero = int(input("Numero: "))
if numero < 0:
    numero = numero * -1
print("El valor absoluto es", numero)

############### Ejercicio 15 ###############
nombre1 = input("Un nombre: ")
numero2 = input("Otro nombre: ")
indice_final_nombre1 = len(nombre1) - 1
indice_final_nombre2 = len(nombre2) - 1
if nombre1[0] == nombre2[0] or nombre1[indice_final_nombre1] == nombre2[indice_final_nombre2]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

############### Ejercicio 15 ###############
Candidato = input("Candidato elegido: ")
if candidato.upper() == "A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido azul")
elif candidato.upper() == "C":
    print("Usted ha votado por el partido verde")
else:
    print("Opcion erronea")

############### Ejercicio 15 ###############
letra = input("Letra: ")
if len(letra) != 1:
    print("Debe ser solo una letra")
else:
    if letra in "aeiou":
        print("Es vocal")

############### Ejercicio 15 ###############
anio = int(input("Anio: "))
if anio % 4 != 0:
    print("No es bisiesto.")
else:
    if anio % 100 != 0 or anio % 400 == 0:
        print("Es bisiesto")
else:
print("No es bisiesto")

############### Ejercicio 16 ###############
fecha = input("Fecha(formato 'dia, DD/MM'): ")
fecha = fecha.lower()
diasemana = fecha[0:fecha.find(',')]
dianro = int(fecha[fecha.find(' ') + 1:fecha.find('/')])
mesnro = int(fecha[fecha.find('/') + 1:])
if dianro > 31 or mesnro > 12:
    print("Fecha incorrecta")
else:
    if diasemana in "lunes,martes,miercoles":
        respuesta = input("Se tomaron examenes? S/N: ")
        if respuesta.lower() == "s":
            aprobados = int(input("Cantidad de aprobados"))
            reprobados = int(input("Cantidad de reprobados"))
            print("Porcentaje de aprobados: ", (aprobados * 100) / (aprobados + reprobados), "%")
    elif diasemana == "jueves":
        asistencia = int(input("Porcentaje de asistencia: "))
        if asistencia > 50:
            print("Asistio la mayoria")
            else:
            print("No asistio la mayoria")
elif diasemana == "viernes":
if dianro == 1 and (mesnro == 1 or mesnro == 7):
    print("Comienzo de nuevo ciclo")
    alumnos = int(input("Cantidad de alumnos: "))
    arancel = float(input("Arancel: $"))
    print("Ingreso total: $", alumnos * arancel)
else:
    print("Fecha incorrecta")
print("Fin del programa")

############### Ejercicio 17 ###############
# for x in range(10):
#    print(x)
# for x in range(100,200):
#   print(x)


for x in range(5, 20, 3):
    print(x)
############### Ejercicio 17 ###############
n = int(input("Numero: "))
for x in range(n, n * 2):
    print(x)

############### Ejercicio 17 ###############
C = int(input("Cantidad de numeros: "))
total = 0
for variable in range(c):
    numero = int(input("Numero a sumar: "))
    total = total + numero
print("Total de la suma: ", total)

############### Ejercicio 17 ###############
frase = input("Frase: ")
print("Vocales en la frase: ")
for x in "aeiou":
    if x in frase:
        print(x)
print("hola")
if 4 != 5:
    print("adios")

############### Ejercicio 17 ###############
frase = input("Frase: ")
cantidad = 0
for x in frase:
    if x in "aeiou":
        cantidad += 1
print("Cantidad de vocales:", cantidad)

############### Ejercicio 18 ###############
total = 0
for i in range(101):
    if i % 3 == 0:
        total += i
print("Sumatoria", total)

############### Ejercicio 18 ###############
numero = int(input("Numero: "))
f = 1
if numero != 0:
    for i in range(1, numero + 1):
        f = f * i
print("Factorial:", f)

############### Ejercicio 17 ###############
C = int(input("Cantidad de numeros: "))
total = 0
for variable in range(c):
    numero = int(input("Numero a sumar: "))
    total = total + numero
print("Total de la suma: ", total)

############### Ejercicio 18 ###############
sumaNegativos = 0
sumaPositivos = 0
cantidadPositivos = 0
for i in range(6):
    nro = int(input("Numero: "))
    if nro >= 0:
        cantidadPositivos += 1
        sumaPositivos += nro
    else:
        sumaNegativos += nro
print("Sumatoria de negativos", sumaNegativos)
if cantidadPositivos != 0:
    print("Promedio de positivos:", sumaPositivos / cantidadPositivos)
else:
    print("No se ingresaron numeros positivos")


#Ejercicio 27
def primo (numero):
    for i in range(2,numero):
        if numero%i==0:
            return False
    return True

from ejercicio27_from import *

numero=int(input("Numero: "))
if primo(numero):
    print("Es primo")
else:
    print("No es primo")

#ejercicio 27.1
def frecuencia(numero,digito):
    cantidad=0
    while numero!=0:
        ultDigito=numero%10
        if ultDigito==digito:
            cantidad+=1
        numero=numero//10
    return cantidad

from ejercicio27_1 import *
num=int(input("Numero: "))
digito=int(input("Digitos: "))
print("Frecuencia: ",frecuencia(num,digito))

#Ejercicio 27.2
def factorial(n):
    f=1
    if n!=0:
        for i in range (1,n+1):
            f=f*i
    return f

from ejercicio27_2 import *
cantidad=0
num=int(input("Numero (-1 para cortar): "))
while num!=-1:
    print("Factorial: ", factorial(num))
    cantidad+=1
    num=int(input("Numero (-1 para cortar): "))
print("Se leyeron", cantidad, "numeros")

#Ejercicio 27.3
def sumaDigitos (numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

from ejercicio27_3 import *
cantidad=0
mayor=1
numero=int(input("Numero positivo:"))
while numero>=0:
    suma=sumaDigitos(numero)
    if suma>mayor:
        mayor=suma
        n_mayorsuma=numero
    if suma < 10:
        cantidad+=1
    numero=int(input("Numero Positivo: "))
print("Sumatoria de digitos de", n_mayorsuma, ":", mayor)
print("Cantidad con sumatoria menor a 10:", cantidad)

#Ejercicio 28

def maximo (a,b):
    if a>b:
        return a
    else:
        return b

def minimo(a,b):
    if a<b:
        return a
    else:
        return

#Ejercicio 29

def lenUltimaPalabra(cadena):
    longitud=len(cadena)
    if logitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i] !=" ":
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena [i+1] !=" ":
    return

#Ejercici0 30
def titulo(cadena):
    nueva=""
    inicioPalabra=True
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva + caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False
            else:
                nueva=nueva+caracter.lower()
    return nueva

#Ejercicio 31
letras=list("ABC")
letras
[A,B,C]
print(list("ZXU"))
[Z,X,U]

for i in range(len(letras)):
    print(letras[i])

i=0
while i<len(letras):
    print(letras[i])
    i+=1
for elemento in letras:
    print(elemento
dir(list)
numero+list(range(4,10))

#Ejercicio 32
#1
numeros=[]
nro=int(input("Numero: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Numero: "))
#2
eliminar=int(input("Numero a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese numero no esta entre los ingresados")
#3
print("Sumatoria de los numeros:", sumatoria(numeros))
#4
limite=int(input("Filtrar numeros menores a: "))
for n in numerosMenores(numeros, limite):
#5
print("Frecuencias: ")
for tupla in frecuencias(numeros):
    print(tupla[0], "aparece", tupla[1], "veces")

def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=0
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return
def frecuencias(lista):
    nueva=[]
    for n inlista:
        if (n, lista.count(n)) not in nueva:

#Ejercicio #33
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar pais destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un pais")
    print("7. Salir del programa")
    opcion=int(input("Accion a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades = agregarCiudades(ciudades)
    elif opcion == 3:
        dni=int(input("DNI: ")
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion == 4:
        ciudad = int("Ciudad: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion == 5:
        dni=int(input("DNI: ")
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion == 6:
        pais==6:
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion == 7:
        break
    else:
        print("Opcion invalida")

#Ejercicio 34
A=set()
type(A)
A={1,2,3}

B={1,2,3,2,1,3,2,1,3,2,1,2,3}
C=set(numeros)
for n in A:
    print(n)


#Ejercicio 35
def cargarNombres(alumnos):
    nombre=input("NOmbre: ")
    while nombre!="x":
        alumnos.add(nombre)
        nombre=input("Nombre: ")
    return alumnos

from funciones import *
primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS: ")
for nombre in primaria|secundaria
    print(nombre)

print("NOMBRES COMUNES: ")
for nombre in primaria&secundaria:
    print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria
    print(nombre)

#Ejercicio 36
#Diccionarios
A=dict()

B={}
traducciones=("hola":"hello", "adios:bye","dia:day", "noche:night")

calendario=[("enero",1),("febrero",2), ("marzo",3)]
type(meses)

#Ejercicio 37
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for i in range(50):
    cadena=input("Cadena de caracteres: ")
    for caracter in cadena:
    if caracter not in contadores.keys():
        contadores[caracter]=1
    else:
        contadores[caracter]+=1

for caracter,cantidad in contadores.items():
    print(caracter,":",cantidad)

#Ejercicio 38
socios_activos={1:["Amanda Nunez","123545147", True], 2:["Jairo Calle","09658745", True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")
print("***Registrar pago de cuotas")
numero=int(input("Numero de socios: "))
socios_activos[numero] [2]=True

print("***Eliminar socio: ")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
del socios_activos[numero]

imprimirListado(socios_activos)

#Ejercicio 39
#1
lista=[1,2,3,4]
for elemento in lista:
    print(elemento)

#2
articulos={154:["javon en polvo", "limpieza", True],
            248:["talco", "cosmetica", False],
           199:["cera para pisos", "limpieza", True]}
for clave, valor in articulos.items():
    print("Codigo:", calve)
    print("Descripcion:", valor[0])
    print("Rubro:", valor[1])
    if valor[2]:
        print("Hay stock")
    else:
        print("Agotado")
    print("----------")













