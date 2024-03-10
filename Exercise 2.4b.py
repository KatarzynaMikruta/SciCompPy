n = ["1","2","3","4","5","6","7","8","9","10"]
name = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon"]
symbol = ["H","He","Li","Be","B","C","N","O","F","Ne"]
weight = ["1","4","7","9","11","12","14","16","19","20"]
line = '+---+--------------------+------+----------+'

pt = [[n[x], name[x], symbol[x], weight[x]] for x in range(1,10)]
print(pt)

print(line)
print("|No.|Name (en)           |Symbol|Weight (u)|")
print(line)
for (n, name, symbol, weight) in pt:
    print("|" + "|".join([n.rjust(3), name.ljust(20), symbol.center(6), weight.rjust(10)]) + "|")
print(line)