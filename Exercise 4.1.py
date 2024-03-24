#przykładowe współrzędne punktu p
x = [9, 0.5, -4, -0.2, 0, 8.3]
y = [-3, 0.2, -16, 0.3, 0, 5]
point_list = list(zip(x, y))

print(list(filter((lambda p: p[0] ** 2 + p[1] ** 2 <= 1), point_list))) #zwraca punkty, których współrzędne należą do koła jednostkowego

print(list(filter((lambda p: p[0] > 0 and p[1] > 0), point_list)))      #zwraca punkty, których współrzędne są dodatnie

point_list.sort(key = lambda p: (-p[1], p[0]))                          #sortuje punkty wg malejącego y i rosnącego x
print(point_list)

point_list.sort(key = lambda p: abs(p[0]) + abs(p[1]))                  #sortuje punkty wg sumy wartości bezwględnych współrzędnych
print(point_list)