class Eleve:
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

camilleO = Eleve('Onette','Camille','01/07/2004',7,14,11)
modesteO = Eleve('Oma','Modeste','01/11/2002',13,8,17)
alainT = Eleve("Térieur","Alain","01/01/2000",12,10,15)

def moyenne_mat(lst_eleve):
    moy = {lst_eleve[0].matiere1:0,lst_eleve[0].matiere2:0,lst_eleve[0].matiere3:0}
    nb_eleve = len(lst_eleve)
    for eleve in lst_eleve:
        moy[eleve.matiere1] += eleve.note_mat1
        moy[eleve.matiere2] += eleve.note_mat2
        moy[eleve.matiere3] += eleve.note_mat3
    moy[eleve.matiere1] = moy[eleve.matiere1] / nb_eleve
    moy[eleve.matiere2] = moy[eleve.matiere2] / nb_eleve
    moy[eleve.matiere3] = moy[eleve.matiere3] / nb_eleve
    return moy


