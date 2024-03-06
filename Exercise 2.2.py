Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> x == 5 and 3 + 8   # 11 – wyrażenie po lewej jest prawdziwe, więc zwracany jest wynik działania po prawej
11
>>> x == 4 and 3 + 8   # False – wyrażenie po lewej jest fałszywe, więc zwracana jest wartość „False” bez sprawdzania wyrażenia po prawej
False
>>> 3 + 8 and x == 5   # True - wyrażenie po lewej nie zwraca wartości fałszywej, więc zwracana jest wartość logiczna prawdziwego wyrażenia po prawej
True
>>> 3 + 8 and x == 4   # False - wyrażenie po lewej nie zwraca wartości fałszywej, więc zwracana jest wartość logiczna fałszywego wyrażenia po prawej
False
>>> isinstance(True, int)    # True – funkcja sprawdza, czy dany obiekt należy do danego typu danych
True
>>> isinstance(True, bool)   # True – wartość logiczna „True” należy do typu danych „bool”, który jest podtypem typu „int”, więc obie te funkcje zwracają prawdę
True
