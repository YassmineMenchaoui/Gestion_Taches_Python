
# Algoapplication_de_gestion_des_tâches
taches = []
def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")
def afficher_taches():
    if len(taches) == 0:
        print("La liste des tâches est vide.")
    else:
        print("\n--- LISTE DES TÂCHES ---")
        for i in range(len(taches)):
            print(f"{i + 1} - {taches[i]}")
def rechercher_tache():
    mot_cle = input("Entrez un mot-clé : ").strip()
    if mot_cle == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
    else:
        trouve = False
        for i in range(len(taches)):
            if mot_cle.lower() in taches[i].lower():
                print(f"{i + 1} - {taches[i]}")
                trouve = True
        if trouve == False:
            print("Aucune tâche trouvée.")
while True:
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")
    choix = input("Votre choix : ")
    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Réessayez.")
