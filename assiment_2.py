
def table(num):
    for i in range(1, 201):
        print(num * i, end='\t')  
        if i % 10 == 0:
         print()
table(7)