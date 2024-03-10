>>> t = (2, 4)
>>> print(t[2]) #zakres liczony jest od 0, a więc indeks 2 jest poza zakresem dla tej krotki
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(t[2])
IndexError: tuple index out of range
>>> t.append(6) #krotki są niemodyfikowalne, a więc nie można dokładać do nich elementów
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.append(6)
AttributeError: 'tuple' object has no attribute 'append'
>>> a, b = t ; print(a, b)  #przypisuje kolejne wartości z krotki do kolejnych zmiennych
2 4
