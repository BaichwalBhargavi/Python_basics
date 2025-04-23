# print all permutations (noob way)
x =3
y=4
z=2

perms= []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            perms.append([i,j,k])

print(perms)
print(len(perms))

# print all permuatations (list comprehension)

x =3
y=4
z=2

perms = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]

print(perms)
