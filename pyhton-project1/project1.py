from copy import deepcopy

# wprowadzanie, zmienne
'''stan_konta = input("Podaj stan konta:")
stan_konta = int(stan_konta)
stan_konta = stan_konta + 500'''

# wypiswanie
# print(stan_konta)

# zmienne
x = 9
y = x//2

print(y)

z = x**2

print(z)

temperature = -5
temperature2 = 20
czy_szczesliwy = True

# warunki
if temperature > 10 and czy_szczesliwy:
    print("Wychodzimy")
elif temperature > -10:
    print("ubierz się ciepło")
else:
    print("nie wychodzimy")

# pętle

for i in range(4,10,2):
    if i ==5:
        continue
    print(i)

while temperature2 > 10:
    print('temperatura jest ok', temperature2)
    temperature2 -= 1

# listy

oceny = [4, 5 , 3, 2, 1, 6, 4]
print(oceny[0])
print(oceny[2])

for i in range(len(oceny)): # dlugosc len
    print(oceny[i], end=" ")

for ocena in oceny:
    print(ocena, end=" ")

for i, ocena in enumerate(oceny):
    if i%2 == 0 and ocena > 3:
      print(i, ocena)

oceny.append(2) # dodać 1 element
oceny.extend([2,3,4]) # dodać wiele
oceny.insert(1,4) # dodać przed index
oceny.remove(4) # usunąć
oceny.pop() # usuwa ostatni element
oceny.sort() # sortowanie

print(oceny.index(6)) # konkretny index

if 4 in oceny:
    print("Jest taka ocena")

oceny_all = [[1,2,3], [6,6,6], [3,3,4]]
print(oceny_all[0][0])

for student in oceny_all:
    for ocena in student:
        print(ocena, end=' ')
    print()

oceny_2 = deepcopy(oceny_all)
oceny_2[0][0]=43
print(oceny_all)

# sety
oceny = [4, 5, 5, 4, 8, 9, 34, 32, 1, 35, 2, 2, 4, 5]
oceny = set(oceny)
print(oceny)

oceny_marka = [1, 2, 3, 2, 1, 1, 3]
oceny_kozaka = [6, 5, 4, 3, 6]

marek_set = set(oceny_marka)
kozak_set = set(oceny_kozaka)
print(marek_set.difference(kozak_set)) # róznica między zbiorami


# słowniki

oceny_slownik = {}
oceny_slownik['marek'] = [1, 2, 3, 3, 2]
oceny_slownik['kozak'] = [6, 5, 6]
print(oceny_slownik['marek'])

for k,v in oceny_slownik.items():
    print(k,v)

# stringi

imie = 'Wojtek'
print(imie[5])

for letter in imie:
    print(letter)

if 'W' in imie:
    print('Jest taka litera')

string1 = "Wojtek"
new_string = f"Pan {string1} jest kozak" # zmienne i wypisywanie
print(new_string)

# pliki
with open('plik1.txt', 'r', encoding='UTF-8') as file:
    print(file.readlines())

lines = []

# funkcje
def silnia(n):
    # 5! = 1 * 2 * 3 * 4 * 5
    res = 1
    for x in range(1,n+1):
        res = res * x
    return res

with open("liczby.txt") as f:
    for line in f:
        lines.append(int(line.strip()))
    print(lines)

for number in lines:
    print(silnia(number))