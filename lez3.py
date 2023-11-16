file = open("shampoo_sales.csv","r")
print(file.readline())
print("no")
print(file.readlines((17+17)))#restituisce una lista di n righe dove n è tutte le righe del file se input è null oppure m righe contando i caratteri delle righe che legge finchè sono uguali o più dell'input
print(2)
print(file.read())
file.close

file=open("output.txt","w")
file.write("banana")
file.close