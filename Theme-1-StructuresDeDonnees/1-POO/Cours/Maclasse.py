class Eleve:
    '''
    Création d’une instance eleve :
    eleve = Eleve(nom, prenom, date, note1, note2, note3)
    avec :
        - nom, prenom et date de type str
        - note1, note2 et note3 de type float
    Attributs d’instance : nom, prenom, date, note_mat1 (pour la programmation), note_mat2 (pour l’algo) et note_mat3 (pour le projet)
    Attributs de classe : matiere1, matiere2, matiere3
    Méthode : moyenne() retourne la moyenne de l’élève
    '''

    matiere1 = "Programmation"
    matiere2 = "Algorithmique"
    matiere3 = "Projet"
    def __init__(self,Nom, Prenom, Date, Note1, Note2, Note3):
        self.nom = Nom
        self.prenom=Prenom
        self.date=Date
        self.note_mat1=Note1
        self.note_mat2=Note2
        self.note_mat3=Note3

    def moyenne(self):
        return (self.note_mat1 + self.note_mat2 + self.note_mat3)/3