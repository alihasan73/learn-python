arr1 = [1,3,4,5]
arr2 = [11,22,23, 25,67]

def check(angka):
    if(angka % 2):
        return 'ganjil'
    else:
        return 'genap'
    
hasil = map(check,arr2)

# print(list(hasil))


arr3 = [9100000,9800000,9500000,10300000,9300000]
def check_value(angka):
    hasil_pertama = 5 * angka / 100
    hasil_kedua = angka - hasil_pertama
    if(hasil_kedua > 9000000):
        return hasil_kedua

check_2 = filter(check_value, arr3)
print(list(check_2))