class Employe:
    def __init__(self,numeroPermis,nom,prenom,):
        self.numeroPermis=numeroPermis
        self.nom = nom
        self.prenom=prenom
        self.voitureService=None

    def afficherInformations(self):
        print(f"les informations de cet employe sont : numeroPermis {self.numeroPermis}, nom {self.nom},prenom {self.prenom}")   
        if  self.voitureService == None:
            print(f"Aucune voiture de service a ete attribuee a cet employe ")
        else :
            print(f"une voiture de service a ete attribuee a cet employe")

    def affecterVoiture(self,voiture):
        if self.voitureService != None:
            print(f"Lemploye {self.prenom} {self.nom} possede deja une voiture")
            return
        
        elif voiture.chauffeur != None:
            print(f"la voiture {voiture.matricule} est deja prise par {voiture.chauffeur.prenom} {voiture.chauffeur.prenom}")
            return
        
        else:
            self.voitureService=voiture
            voiture.chauffeur= self 
            print(f"la voiture {voiture.matricule} affecte a {self.prenom} {self.nom}")

    def retirerVoiture(self,voiture):
        if self.voitureService ==None:
            print(f"cet n employe ne peux pas remettre cette voiture car il ne la possede pas")
        else:
            chauffeur=self.voitureService.chauffeur
            self.voitureService.chauffeur =None
            self.voitureService=None
            print(f"le vehicule {voiture.matricule} a ete retire au chauffeur {chauffeur.prenom} {chauffeur.nom}")   

class Voiture:
     def __init__(self,matricule, annee ,marque ,kilometrage,):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.kilometrage=kilometrage
        self.chauffeur=None

     def afficherInformations(self):
        print (f"les informations de la voiture sont: matricule {self.matricule} ,annee {self.annee},marque {self.marque} ,kilometrage {self.kilometrage} ")
        if self.chauffeur == None:
            print(f"cette voiture n' est pas attribue a un employe")
        else:
            print(f"Informations du chauffeur: numeroPermis {self.chauffeur.numeroPermis} nom {self.chauffeur.nom}, prenom {self.chauffeur.prenom}")

e1=Employe("jfhaaa","Eric","Karam")
e2=Employe("jfhbbb","julien","Karim")
e3=Employe("jfhcccc","julie","Karom")


v1=Voiture("ABC-1234",2026,"YARIS",3204)
v2=Voiture("DEF-5678",2025,"TOYOTA",32040)
v3=Voiture("GHI-1234",2024,"MECEDES",32034)

print(f"\n affichage de tous les objets crees")

e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()
print(f"\n")
v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()

print(f"\n")
print(f"\n affectation des voitures aux employes")

e1.affecterVoiture(v1)
print(f"\n")
e2.affecterVoiture(v2)
print(f"\n")
e3.affecterVoiture(v3)

print(f"\n")
print(f"\n retrait des voitures aux employes")
e1.retirerVoiture(v1)
print(f"\n")
e2.retirerVoiture(v2)

print(f"\n")
print(f"\n affichage des informations des employes apres le retait de leur voiture")
print(f"\n")
e1.afficherInformations()
v1.afficherInformations()
print(f"\n")
e2.afficherInformations()
v2.afficherInformations()


print(f"\n")
print(f"\n affectation a un employe d une voiture affecte par un autre")
e2.affecterVoiture(v3)

print(f"\n")
print(f"\n")

