noms=input("Entrer les noms des deux enfants (séparer d'un espace)")
noms=noms.split(" ")
somme=0
for i in range(2) :
	somme=0
	for k in range(len(noms[i])):
		somme+=ord(noms[i][k])-65
	if somme>10:
		somme=somme%9
	print(somme," ",end="")
print()
