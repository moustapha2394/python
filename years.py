a= -1
while a<0:
	annee = input("veuillez entrer une année: ")
	annee=int(annee)
	if annee % 4 == 0:
		if annee % 100 == 0 and annee % 400 == 0 :
			print("l'année ",annee," est bissextile.")
		elif annee % 100 != 0 :
			print("l'année ",annee," est bissextile.")
		else:
			print("l'année ",annee," n'est pas bissextile.")
	else:
		print("l'année ",annee," n'est pas bissextile.")


