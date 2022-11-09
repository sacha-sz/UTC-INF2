import sqlite3


def requete(req):
    bdd = sqlite3.connect("BDD-exo4.sqlite")  # Connexion à la BDD
    cursor = bdd.cursor()  # Obtenir un curseur (tampon)
    try:
        cursor.execute(req)  # Exécuter la requête
    except:
        print("requête incorrecte")
    else:  # Affichage du resultat
        for enregistrement in cursor:
            print(enregistrement)
        bdd.commit()  # Appliquer toutes les modifs sur la BDD réelle
        bdd.close()  # Fermer la connexion


def main():
    # Req 1
    requete("""
            SELECT * 
            FROM client
            """)  # Affiche tous les attributs de tous les clients

    # Req 2
    id = int(input("Entrez l'ID voulu : "))
    requete(f"""
            SELECT * 
            FROM numero_telephone 
            WHERE client_id={id}
            """)
    #
    # Req 3
    requete("""
            SELECT client.nom, client.prenom, ville.nom 
            FROM client, ville 
            WHERE client.ville_id=ville.ID """)

    requete("""
            SELECT c.nom, c.prenom, v.nom 
            FROM client AS C 
            INNER JOIN ville as V 
            ON c.ville_id=v.ID """)

    # Req 4
    depart = int(input("Entrez le code du département voulu : "))
    requete(f"""
            SELECT c.nom, c.prenom 
            FROM client AS c 
            INNER JOIN ville as V 
            ON v.ID=c.ville_id 
            WHERE v.code_departement={depart}
            """)

    # Req 5
    requete("""
            SELECT * 
            FROM client 
            WHERE id not in (SELECT client_id from numero_telephone as n where n.est_demarche=TRUE)
            """)

    # Req 6
    requete("""
            SELECT c.nom, c.prenom, n.numero
            FROM numero_telephone AS n
            INNER JOIN client AS c ON n.client_id=c.ID
            INNER JOIN operateur AS o ON c.operateur_id=o.ID
            WHERE o.nom="SuperTelecom"
            """)

    #req 8
    requete("""
            INSERT INTO ville (nom, code_departement, code_postal, code_INSEE, nombre_habitants)
            VALUES
            ("Compiègne", "Oise", "60200", "60159", "40200")
            """)

    # req 9
    requete("""
            DELETE FROM ville WHERE code_postal="60200"
            """)

    # req 10
    num = input("Entrez le numéro qui a été démarché : ")
    requete(f"""
            UPDATE numero_telephone
            SET est_demarche=1
            WHERE numero="{num}"
            """)

    # req 11
    requete("""
            UPDATE numero_telephone
            SET operateur_id=4
            WHERE numero="03.11.22.33.44"
            """)

    # req 12
    requete("""
            UPDATE numero_telephone
            SET operateur_id =(SELECT id FROM operateur WHERE nom="SuperTelecom")
            WHERE numero="03.11.22.33.44"
            """)

    # req 13
    requete("""
           DELETE FROM client 
           WHERE id="1"
           """)


if __name__ == "__main__":
    main()