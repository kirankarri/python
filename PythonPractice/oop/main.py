from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ['PKName','Type']
table.add_row(['Pikachu','Electrics'])
table.add_row(['Squirtle','Water'])
table.add_row(['Charmendar','Fire'])
table.align = 'l'
print(table)