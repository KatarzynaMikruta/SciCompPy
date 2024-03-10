Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t = (2, 4)
>>> print(t[2]) #zakres liczony jest od 0, a więc indeks 2 jest poza zakresem dla tej krotki
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(t[2]) #zakres liczony jest od 0, a więc indeks 2 jest poza zakresem dla tej krotki
IndexError: tuple index out of range
>>> t.append(6) #krotki są niemodyfikowalne, a więc nie można dokładać do nich elementów
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.append(6) #krotki są niemodyfikowalne, a więc nie można dokładać do nich elementów
AttributeError: 'tuple' object has no attribute 'append'
>>> a, b = t ; print(a, b)  #przypisuje kolejne wartości z krotki do kolejnych zmiennych
2 4
