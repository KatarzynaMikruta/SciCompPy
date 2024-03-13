# metoda z pętlą "for"
for x in range(1,41):
    if x == 13:
        continue
    elif (x % 5 == 0 and x % 7 == 0):
        print(x, "is divided by 5 and 7")
    elif x % 5 == 0:
        print(x, "is divided by 5")
    elif x % 7 == 0:
        print(x, "is divided by 7")
    elif not (x % 5 == 0 or x % 7 == 0):
        print(x, "is not important")

# metoda z pętlą "while"
x = 1
while x < 41:
    if x == 13:
        pass
        x = x + 1
    elif (x % 5 == 0 and x % 7 == 0):
        print(x, "is divided by 5 and 7")
        x = x + 1
    elif x % 5 == 0:
        print(x, "is divided by 5")
        x = x + 1
    elif x % 7 == 0:
        print(x, "is divided by 7")
        x = x + 1
    elif not (x % 5 == 0 or x % 7 == 0):
        print(x, "is not important")
        x = x + 1