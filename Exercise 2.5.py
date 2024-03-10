S = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(S) - S.count(" "))    #liczba czarnych znaków
print(S.count(" ") + 1)         #liczba wyrazów
R = S.split()
print(max(R, key=len))          #najdłuższy wyraz
R.sort(key=str.lower)
print(R)                        #wyrazy posortowane wg porządku leksykograficznego
R.sort(key=len)
print(R)                        #wyrazy posortowane wg długości