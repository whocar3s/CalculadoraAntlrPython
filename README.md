
# **Calculadora Antlr y Python**

## **Pasos para ejecutar**
**Requisitos:** Para ejecutar este proyecto se debe tener instalado Antlr v4.13 y Python3.

1. Clonar el repositorio con `git clone https://github.com/whocar3s/CalculadoraAntlrPython.git`

2. Desde la consola acceder a la ruta donde se clono el proyecto y entrar a la carpeta `Calculadora-Antlr-Python3`
3. Compilar el proyecto con el comando `antlr4 -visitor -Dlanguage=Python3 nombredelarchivo.g4`

4. Ejecutar el `Test.py` con el comando `python3 Test.py` o `python3 Test.py archivo.txt` si se quiere leer un archivo de texto externo

5. En caso de ejecutar la primera opción, escribir la operación a realizar

<br>

--------

## **Pruebas**

### **Asociatividad**: 
La asociatividad indica como se agrupan los operandos de un operador cuando aparecen más de dos operandos, teniendo en cuenta esto, la calculadora posee la asociatividad por la izquierda.

Para visualizar esta prueba ejecute:

```
python3 Test.py TestAsociatividad.txt
```

El cual ejecutara las siguientes operaciones
```
7 + 3 - 4
(7 + 8) + 2
7 + (8 + 2)
(3 * 5) * 2
3 * (5 * 2)
2 * (3 + 4)
2 + 3 * 4
2 * 3 + 4
(2 + 3) * 4
```

Y como resultado se obtendrá:

```
6.00
17.00
17.00
30.00
30.00
14.00
14.00
10.00
20.00
```

-------


### **Precedencia**: 
La precedencia se define como la prioridad que tiene un operador en una operación o expresión, en este caso, cumple con la precedencia de operadores estandar poniendole mas prioridad al paréntesis.

Para visualizar esta prueba ejecute:

```
python3 Test.py TestPrecedencia.txt
```

El cual ejecutara las siguientes operaciones
```
2 + 3 * 4
2 * 3 + 4
(2 + 3) * 4
5 * (7 + 3) / 2 + 4
3 * 4 + 2 * (8 - 5) - 14 / 7
```

Y como resultado se obtendrá:

```
14.00
10.00
20.00
29.00
16.00
```

-------

### **Operadores Unarios**: 

Es un tipo de operador que actúa un único operando, es decir, sobre una sola variable, valor o expresión. Nuestra calculadora trabaja los siguientes operadores unarios: `+` `-` (Cambian el signo a un número), `++` `--` (Incremento/Decremento), `!` (Negación lógica).


Para visualizar esta prueba ejecute:

```
python3 Test.py TestOprUniarios.txt
```

El cual ejecutara las siguientes operaciones
```
-5 
+5
8--
6++
!true
!false
!!!true
```

Y como resultado se obtendrá:

```
-5.00
5.00
7.00
7.00
False
True
False
```

-------
<br><br>

# **Calculadora Flex y Bison**
**Requisitos:** Para ejecutar este proyecto se debe tener instalado Flex, Bison y C.

1. Clonar el repositorio con `git clone https://github.com/whocar3s/CalculadoraAntlrPython.git`

2. Desde la consola acceder a la ruta donde se clono el proyecto y entrar a la carpeta `Calculadora-Flex-Bison`
3. Compilar el proyecto con el comando `make`

4. Ejecutar el `a.out` con el comando `./a.out`

5. Escribir las operaciones a realizar

<br>

--------

## **Pruebas**
Para este caso se ejecutaron las mismas pruebas que para la cálculadora de Antlr4 y se obtuvieron los mismos resultados, como conclusión, ambas pruebas fueron exitosas en ambas cálculadoras.
<br>

--------

## Miembros del grupo

- Laura González
- Camilo Madero
- Paula Páez
- Felipe Rodriguez
