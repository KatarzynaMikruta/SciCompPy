word = "Katarzyna"
line = "+" + "---+" * len(word)
L = [line]

for x in word:
    a = "| " + (" | ".join(word)) + " |"

L.append(a)
L.append(line)
print("\n".join(L))
