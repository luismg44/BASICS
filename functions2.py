### Ejercicios de functions ###


# Ejercicio 1 se definen los valores de a y b con 20 y 10 y se solicita la multiplicacion de estos, da de resultado 200
def numbers(a, b):
    return a * b


result = numbers(20, 10)
print(result)


# Ejercicio 2 nos da resultado solamente impreso el mensaje 4 veces pero sin el numero 4
def message(message, count):
    for index in range(4):
        print(message)


message("Steelers the best team in nfl", 4)


# Ejercicio 3 nos da de resultado "Hello Luis Morales"
def full_name(name1, name2):
    print(f"Hello {name1} {name2}")


name1 = "Luis"
name2 = "Morales"

full_name(name1, name2)

### Ejercicios con Default Parameters ###


# Ejercicio 1 nos da de resultado "Hello Luis Morales"
def names(name1, name2):
    print(f"Hello {name1} {name2}")


name1 = "Luis"
name2 = "Morales"
full_name = names(name1, name2)


# Ejercicio 2 nos da de resultado 44
def sumados(num1, num2):
    return num1 + num2


total = sumados(22, 22)
print(total)


# Ejercicio 3 nos da de resultado "Hello Luis, Your age is 27 and you are from Mexico"
def personal_info(name, age, nation):
    print(f"Hello, {name}")
    print(f"Your age is {age}")
    print(f"And you are from {nation}")


personal_info("Luis", 27, "Mexico")

### Ejercicios de keyword arguments ###


# Ejercicio 1 nos da de resultado "Hello Luis, Your age is 27 and you are from Mexico"
def personal_info(name, age=27, nation="Mexico"):
    print(f"Hello, {name}")
    print(f"Your age is {age}")
    print(f"And you are from {nation}")


personal_info("Luis")


# Ejercicio 2 nos da de resultado 80
def sumados(num1, num2=42, num3=30):
    return num1 + num2 + num3


total = sumados(8)
print(total)


# Ejercicio 3
def la_suma(x=3, y=0, z=0):
    return x - y + z


print(la_suma(y=7))
