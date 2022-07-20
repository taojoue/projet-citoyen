import pandas as pd
import csv

Path = "./file.csv"

with open(Path, "r") as fichier:

    csv_reader = csv.reader(fichier, delimiter=",")

    for ligne in csv_reader:
        print(ligne)

# siren,nic,siret,dateFin,dateDebut,etatAdministratifEtablissement,changementEtatAdministratifEtablissement,enseigne1Etablissement,enseigne2Etablissement,enseigne3Etablissement,changementEnseigneEtablissement,denominationUsuelleEtablissement,changementDenominationUsuelleEtablissement,activitePrincipaleEtablissement,nomenclatureActivitePrincipaleEtablissement,changementActivitePrincipaleEtablissement,caractereEmployeurEtablissement,changementCaractereEmployeurEtablissement
