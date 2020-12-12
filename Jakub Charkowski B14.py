# Przedmiot: Informatyka
# Kierunek studiów: Mechanika i Budowa Maszyn
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 20.11.2020
# Imię: Jakub
# Nazwisko: Charkowski
# Numer albumu ZUT: 49940
from random import choice

FILENAME1 = 'Bogurodzica.txt'
FILENAME2 = 'Bogurodzica2.txt'

file1 = open(FILENAME1, encoding='utf-8')
file2 = open(FILENAME2, encoding='utf-8')


while True:
    try:
        line1 = next(file1)
        line2 = next(file2)
        while line1 != line2:
            print(line1)
            line1 = next(file1)
            
            except StopIteration:
                break 
             
while True:
    try:
        line1 = next(file1)
        print(line1)
    except StopIteration:
        break
    
FILENAME = 'Bogurodzica'

words set

with open(FILENAME, encoding='utf-8'):
    for line in file:
        for word in line.split():
            if len(word) >= 5:
                words.add(word)

words = sorted(words)

w1 = choice(words)
choosen = [w1]

while True:
    w2 = choice(word)
    if w2 not in choosen:
        choosen.append(w2)
        break

print('.' * 8)
print(w1)
print('.' * 8)
print(w2)
print('.' * 8)

print()

for w3 in words:
    if len(w4) > 5 and w[1] == w[1] and w3[3] == w2[1]:
        break
    
print()

for w4 in words:
    if len(w4) > 5 and w4[1] == w1[3] and w4[3] == w2[3]:
        break
    
print(f'{w3[0]} {w4[0]}')
print(w1)
print(f'{w3[2]} {w4[2]}')
print(w2)
print(f'{w3[4]} {w4[4]}')

print()
print(w1, w2 ,w3 ,w4)