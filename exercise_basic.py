import math

# aritmatika
angka1 = int(input("Masukan angka pertama : "))
angka2 = int(input("Masukan angka kedua : "))
tanda = input("Proses yang akan dilakukan : ")

def arithmetic(val, val2, symb):
    if(symb == '*'):
        hasil = val * val2
        return hasil
    elif(symb == '/'):
        hasil = val / val2
        return hasil
    elif(symb == '-'):
        hasil = val - val2
        return hasil
    elif(symb == '+'):
        hasil = val + val2
        return hasil
    else:
        hasil = "Proses gagal"
        return hasil
    

res = arithmetic(angka1, angka2, tanda)
print(res)


angka3 = int(input("Masukkan Angka :"))

# check_number
def check_number(val):
    if(val % 2):
        hasil = "Angka ganjil"
        return hasil
    else:
        hasil = "Angka genap"
        return hasil
    
res2 = check_number(angka3)
print(res2)


# sum_number
def sum_number():
    init = 0
    while init <= 100:
        init += 1

    return init

res3 = sum_number()
print(res3)

# multiple_table
def multiple_table(angka):
    table = f'Perkalian {angka} \n'
    for i in range(10):
        table += f'{i + 1} X {angka} = {(i + 1) * angka} \n'

    return table

res4 = multiple_table(8)
print(res4)

# factorial
def factorial(angka):
    total = 1
    for i in range(angka):
        nmbr = i + 1
        total *= nmbr
    
    return total

res5 = factorial(4)
print(res5)


# prime
def is_prime(val):
    hasil = True
    for i in range(2, val):
        if val % i == 0:
            hasil = False
    
    return hasil

arr = []

for i in range(50):
    if i < 2:
        continue

    if is_prime(i):  
        arr.append(i)

print(arr)

# FizzBuzz
def game_fizz(val):
    text = ''
    for i in range(1, val):
        if i % 3 == 0 and i % 5 == 0:
            text += f"{i} => FizzBuzz \n"
        elif i % 5 == 0:
            text += f"{i} => Buzz \n"
        elif i % 3 == 0:
            text += f"{i} => Fizz \n"
        else:
            text += f"{i} => Normal number \n"

    return text

res6 = game_fizz(50)
print(res6)

cel = int(input("Masukkan suhu celcius yang akan di proses : "))
suhu = input("Suhu apa yang akan digunakan Fahrenheit / Kelvin :")

def determine(s, cel):
    if s == 'Fahrenheit':
        F = (9/5) * cel + 32
        return int(F)
    elif s == 'Kelvin':
        K = cel + 273,15
        return int(K)
    else:
        H = "Suhu tidak ditemukan"
        return H

res7 = determine(suhu, cel)
print(res7)