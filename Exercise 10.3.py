import pandas as pd

data = {'Name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'],
    'Symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    'Weight': [1.0, 4.0, 6.9, 9.0, 10.8, 12.0, 14.0, 16.0, 19.0, 20.2]}

periodic_table = pd.DataFrame(data, index=range(1, 11))

print(periodic_table)