x = 5 # jeżeli wartość wyrażenia po lewej od operatora „and” jest fałszywa to zwracana jest wartość logiczna „False”, w przeciwnym wypadku zwracana jest wartość wyrażenia po prawej
x == 5 and 3 + 8   # 11 – wyrażenie po lewej jest prawdziwe, więc zwracany jest wynik działania po prawej
x == 4 and 3 + 8   # False – wyrażenie po lewej jest fałszywe, więc zwracana jest wartość „False” bez sprawdzania wyrażenia po prawej
3 + 8 and x == 5   # True - wyrażenie po lewej nie zwraca wartości fałszywej, więc zwracana jest wartość logiczna prawdziwego wyrażenia po prawej
3 + 8 and x == 4   # False - wyrażenie po lewej nie zwraca wartości fałszywej, więc zwracana jest wartość logiczna fałszywego wyrażenia po prawej

isinstance(True, int)    # True – funkcja sprawdza, czy dany obiekt należy do danego typu danych
isinstance(True, bool)   # True – wartość logiczna „True” należy do typu danych „bool”, który jest podtypem typu „int”, więc obie te funkcje zwracają prawdę