noms=input("Entrer les noms des deux enfants (séparés d'un espace)")
noms=noms.split(" ")
somme=0
for loop in range(2) :
	somme=0
	for i in range(len(noms[loop])):
		somme+=ord(noms[i][k])-65
	if somme>10:
		somme=somme%9
	print(somme," ",end="")
print()
