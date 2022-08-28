import Tacka as t

A = t.Tacka(1,0)                             
print(type(A))
print(A.x)                                   
print(type(A.x))
print(A.y)                                   
C = t.Tacka()                                
print(C.x, C.y)

print("------------") 
A = t.Tacka(1,0)
B = t.Tacka(0,1)
C = t.Tacka()
A.predstavi_se()
print(A.rastojanje_do(C))
print(A.rastojanje_do(B))
 
print("------------")
# demonstracija __str__
A = t.Tacka(1,0)
print(A)
print('Tacka A je ' + str(A))
 
A = t.Tacka(1,0)
B = t.Tacka(0,1)
X = t.Tacka(1,0)
print(A == B)                                
print(A == None)
print(A)

print("------------") 
A = t.Tacka(1,0)
B = t.Tacka(0,1)
D = A + B
print(D)
print(t.Tacka(1,0) + t.Tacka(0,1) + D)      