from types import new_class

NewTuples = (1,2,3,"Anamul",False,)  # immutable
print(type(NewTuples))
print(len(NewTuples))


# Negative Indexing use Access Tuple Items
print( NewTuples[-3] )

print(NewTuples[-4:-1])


# Range of Indexes use Access Tuple Items
A = ('Anamul','Abir','Rayhan','Foysal','Shown','Pagla','Aziz')
print(A [2:5] )


# Update Tuples
ThisTuple  = ('Anamul','Abir','Rayhan','Foysal','Shown','Pagla','Aziz')


#print(type(list(ThisTuple)))
B = list(ThisTuple)
B[0]="Haque"
B.append("iqooo")
B.remove('Abir')
ThisTuple = tuple(B)
print(B)
print(ThisTuple)

