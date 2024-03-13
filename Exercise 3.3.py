Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> n = 2022
>>> x = round(math.pi, 5)
>>> word = "Python"
>>> polish = "książka"
>>> outfile = open('vars.txt', 'w', encoding='utf-8')
>>> outfile.write("{}\n{}\n{}\n{}".format(n, x, word, polish))
27
>>> outfile.close()
>>> infile = open('vars.txt', 'r', encoding='utf-8')
>>> S = infile.read()
>>> print(S)
2022
3.14159
Python
książka
>>> infile.close()
