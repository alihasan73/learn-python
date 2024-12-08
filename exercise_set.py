import math
film_kesukaan = input("Masukkan film kesukaan anda :")
arr_film_kesukaan = film_kesukaan.split(',')
set_film_kesukaan = set(arr_film_kesukaan)

film_kesukaan_teman = input("Masukan film kesukaan teman :")
arr_film_kesukaan_teman = film_kesukaan_teman.split(',')
set_film_kesukaan_teman = set(arr_film_kesukaan_teman)

irisan_film = set_film_kesukaan.intersection(set_film_kesukaan_teman)
panjang_irisan_film = len(irisan_film)

gabungan_film = set_film_kesukaan.union(set_film_kesukaan_teman)
panjang_gabungan_film = len(gabungan_film)

persen = (panjang_irisan_film / panjang_gabungan_film)

print(round(persen, 1))
