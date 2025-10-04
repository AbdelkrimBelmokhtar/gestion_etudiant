liste_etudiants = []
ids_utilises = set()
etudiant = {
    "id":101,
    "nom":"Dupont",
    "prenom":"Alice",
    "notes":[("Math", 15), ("Python", 18),]
}

def AjouterEtudiant(id,nom,prenom,notes):
    if id in ids_utilises:
        print ("ID déja enregistré pour un autre étudiant")
        return 
    
    nouvel_etudiant = {
        "id":id,
        "nom":nom,
        "prenom":prenom,
        "notes":notes}
    liste_etudiants.append(nouvel_etudiant)
    ids_utilises.add(id)
    print(f"{prenom} {nom} ajouté ! ")
    return

def recherche_avancee(**critere):

    resultat = []
    for etudiant in liste_etudiants:
        correspond = True
        if "nom" in critere and etudiant["nom"].lower() != critere["nom"].lower():
            correspond = False
            continue
        if "prenom" in critere and etudiant["prenom"].lower() != critere["prenom"].lower():
            correspond = False
            continue
        if "note_min" in critere:
            note_trouve = False
            for matiere, note in etudiant["notes"]:
                if note >= critere["note_min"]:
                    note_trouve = True
                    break
            if not note_trouve:
                    correspond = False
                    continue

        if "matiere" in critere:
            matiere_trouvee = False
            for matiere, note in etudiant["notes"]:
                if matiere.lower() == critere["matiere"].lower():
                    matiere_trouvee = True
                    break
            if not matiere_trouvee:
                correspond = False
                continue
        
        if correspond:
            resultat.append(etudiant)
    
    return resultat

def demande_recherche():
    print(" Je veux chercher par : ")
    print(" 1- Nom ")
    print(" 2- Prenom ")
    print(" 3 - Note minimale ")
    print("4 - Matière ")

    choix = input(" Faites votres choix : ")
    if choix == "1":
        nom = input(" Nom : ")
        resultats = recherche_avancee(nom=nom)
    elif choix == "2":
        prenom = input("Prenom : ")
        resultats = recherche_avancee(prenom=prenom)
    elif choix == "3":
        try:

            note_min = int(input("Note minimale : "))
            resultats = recherche_avancee(note_min=note_min)
        except ValueError:
            print("La note doit être un nombre ")
    elif choix == "4":
        matiere = input("Matiere : ")
        resultats = recherche_avancee(matiere=matiere) 
    else:
        print("Choix invalide")

    if resultats:
        print(f"{len(resultats)} etudiants trouver ")
        for etudiant in resultats:
            print(f"{etudiant["nom"]} {etudiant["prenom"]} {etudiant["id"]}") 
    else:
        print(" Aucun etudiant trouver ")
          
        
def supprimer(id):
    for etudiant in liste_etudiants:
        if etudiant["id"] == id:
            liste_etudiants.remove(etudiant)
            ids_utilises.remove(id)
            print(f"Etudiant {id} supprimé ! " )
            return 
        else:
            print(" Id non trouvé ")

def modifNotes(id, matiereModif, newNote):
    for etu in liste_etudiants: 
        if etu["id"] == id: 
            for i, (matiere, note) in enumerate(etu["notes"]): 
                if matiere == matiereModif:
                    etu["notes"][i] = (matiere, newNote)
                    print(f"Note modifiée pour {etu["nom"]}: {matiere} = {newNote}")
                    return
            print(f"Matière '{matiereModif}' non trouvée pour cet étudiant.")
            return
    print(f"ID {id} non trouvé dans la liste des étudiants.")


def moyenne_generale(id):
    for etudiant in liste_etudiants:
        if etudiant["id"] == id:
            notes = [note for matiere, note in etudiant["notes"]]
            if notes:
                moyenne = sum([note for note in notes])/len(notes)
                print(f"{etudiant["prenom"]} a une moyenne de : {moyenne:.2F} ")
                return moyenne
            else:
                print(f"{etudiant["prenom"]} n'a aucune note ")
                return 0
    
    print(f"Aucun etudiant trouver avec l'id {id}")
    return 0
                            

def moyenne_matiere():
    note_par_matiere = {}
    for etudiant in liste_etudiants:
        for matiere, note in etudiant["notes"]:
            print(f" {etudiant['prenom']} a eu {note} en {matiere}") 
            if matiere not in note_par_matiere:
                note_par_matiere[matiere] = []
            note_par_matiere[matiere].append(note)
                
    
    for matiere in note_par_matiere:
        notes = note_par_matiere[matiere]
        moyenne_generale = sum([note for note in notes]) / len(notes)
        print(f"{matiere} : {moyenne_generale:.2f}")
        if moyenne_generale > 15:
            print(f"{etudiant} a une moyenne generale de {moyenne_generale:.2f}")
        else:
            print(f"Moyenne generale : {moyenne_generale}")
    return note_par_matiere


def afficher_statistique():
    print(" --------- Statistique ---------")

    print(f" Nombre d'étudiant {len(liste_etudiants)}" )

    if not liste_etudiants:
        print(" Aucun etudiant enregistrer ")
        return
    
    moyenne_promo = []
    for etudiant in liste_etudiants:
        for matiere, note in etudiant["notes"]:
            moyenne_promo.append(note)

    if moyenne_promo:
            moyenne_generale_promo = sum([note for note in moyenne_promo]) / len(moyenne_promo)
            print(f"moyenne generale de la promo : {moyenne_generale_promo:.2f}")

    else:
        print(" Aucune note enregistrée ")
        return

def classement_merite():
    print("-------classement par ordre de merite---------")
    if not liste_etudiants:
        print(" Aucun étudiant à classer ")
        return
    classement = []
    for etudiant in liste_etudiants:
        if etudiant["notes"]:
            notes = []
            for matiere, note in etudiant["notes"]:
                notes.append(note)
            moyenne = sum(notes) / len(notes)
            classement.append((moyenne, etudiant["prenom"] , etudiant["nom"]))
        else:
            classement.append((0, etudiant["prenom"] , etudiant["nom"]))

    classement_trier = sorted(classement, reverse=True)

    print("Classement : ")
    for i, (moyenne, prenom, nom) in enumerate(classement_trier):
        if moyenne > 0:
            print(f" {i+1}.{prenom} {nom} {moyenne:.2f}")
        else:
            print(f"{prenom} {nom} n'a aucune note ")


def main():
    while True:
        print(" Système de Gestion des Étudiants)  " 
        " Choix 1(Ajouter un étudiant). " 
        " choix 2 (Modifier les notes)." 
        " choix 3 (Supprimer un étudiant). " 
        " choix 4 (Afficher les statistiques). "
        " choix 5 (recherche avançée) " 
        " choix 6 (Quitter)  ")
        choix_utilisateur = int(input("Choisissez un chiffre "))
        match choix_utilisateur:
            case 1: 
                note_matiere = []
                nom = input("Choissiez le nom ")
                prenom = input("Choissiez le nom ")
                id = int(input("Choissiez l'ID "))
                nombre_matiere = int(input("Combien l'etudiant a de matière ? "))
                for _ in range(nombre_matiere):
                    matiere = input("Entrer le nom de la matière")
                    notes = int(input("Entrer les notes : "))
                    note_matiere.append((matiere, notes))
                AjouterEtudiant(id, nom, prenom, note_matiere)
            case 2:
                id = int(input(" renseigner l'id "))
                matiere = input("rentrer le nom de la matiere à modifier ")
                note = int(input(" rentrer la nouvelle note "))
                modifNotes(id, matiere, note)
            case 3:
                id = int(input(" Rentrer l'ID de l'eleve à supprimer "))
                supprimer(id)
            case 4:
                afficher_statistique()
                classement_merite()
            
            case 5:
                demande_recherche()
            case 6:
                exit


main()






        

        


        