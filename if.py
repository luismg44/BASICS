### Ejercicios de if, elif, else

# Ejemplo 1 da como resultado "puede ver la pelicula"
age = 61

if age > 18:
    print("Puede ver la pelicula")

# Ejemplo 2 da como resultado "puede ver la pelicula con descuento"
if age > 60:
    print("Puede ver la pelicula con descuento")
elif age > 18:
    print("Puedes ver la pelicula")

# Ejemplo 3 si la edad fuera 17 daria resultado "no puedes entrar, ve a otro lado"
if age > 60:
    print("Puede ver la pelicula con descuento")
elif age > 18:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar")
    print("Ve a otro lado")

### Ejercicios de Ternary operator

# Ejemplo 1 da como resultado True
name = "Luis"
result = "True" if name == "Luis" else "False"
print(result)

# Ejemplo 2 da como resultado Negative
number = 44
result = "Positive" if number > 45 else "Negative"
print(result)

# Ejemplo 3 da como resultado "Luis, bienvenido!"
user_name = "Luis"
age = 27

if age > 18:
    print(f"{user_name}, bienvenido!")

### Ejercicios de for loop with range

# Ejemplo 1 el resultado nos da un listado de las frutas
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(fruit)

# Ejemplo 2 nos da de resultado el listado de los 3 items determinados
items = ["apple", 4, "chair"]
for item in items:
    print(item)

# Ejemplo 3 nos da de resultado el listado de equipos
football_teams = ["steelers", "bengals", "ravens"]
for better_team in football_teams:
    print(better_team)

### Ejercicios de while statement

# Ejercicio 1 nos da de reultado 3 veces "Hello, world!"
message = "Hello, world!"
count = 0
while count < 3:
    print(message)
    count += 1

# Ejercicio 2 nos da de resultado 1, 20 y 400 porque el siguiente numero multiplicado rebasa el 1000
numero = 1
while numero < 1000:
    print(numero)
    numero *= 20

# Ejercicio 3 no se ejecuta debido a que el valor asignado supera el 1000
numero = 1001
while numero < 1000:
    print(numero)
    numero *= 20
