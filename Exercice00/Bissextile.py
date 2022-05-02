annee = int (input("Entrez l annee a verifier"))

if(annee%4==0 and annee%100!=0 or annee%400==0):
 print("l'annee est une annee bissextile!")
else:
 print("l'anne n'est pas du tout bissextile!!") 