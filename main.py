import pandas as pd
import csv
import matplotlib.pyplot as plt

PathFileCompany = "./Data/fileCompany.csv"
PathFileCovid = "./Data/fileCovid.csv"

col_list = ["date", "tx_pos", "tx_incid", "TO", "R", "rea", "hosp", "rad", "dchosp", "incid_rea", "incid_hosp",
            "incid_rad", "incid_dchosp", "conf", "conf_j1", "pos", "esms_dc", "dc_tot", "pos_7j", "cv_dose1",
            "esms_cas"]
df = pd.read_csv(PathFileCovid, sep=',', usecols=col_list, encoding='utf-8')

# Ne sert pas pour le graphique
df['date'] = pd.to_datetime(df['date'], errors='coerce')
covidCaseByMonth = df.set_index('date').resample('M')["pos"].sum()
print(covidCaseByMonth)

# le graphique
df["date"] = df["date"].astype("datetime64")
covidCaseByMonth = df.set_index('date').resample('M')["pos"].sum().plot(kind="bar")

plt.show()
plt.close()



# print(covidCaseByMonth)


# with open(PathFileCompany, "r") as fichier:

#     csv_reader = csv.reader(fichier, delimiter=",")

#     for ligne in csv_reader:
#         print(ligne)

# siren,nic,siret,dateFin,dateDebut,etatAdministratifEtablissement,changementEtatAdministratifEtablissement,enseigne1Etablissement,enseigne2Etablissement,enseigne3Etablissement,changementEnseigneEtablissement,denominationUsuelleEtablissement,changementDenominationUsuelleEtablissement,activitePrincipaleEtablissement,nomenclatureActivitePrincipaleEtablissement,changementActivitePrincipaleEtablissement,caractereEmployeurEtablissement,changementCaractereEmployeurEtablissement
# date,tx_pos,tx_incid,TO,R,rea,hosp,rad,dchosp,incid_rea,incid_hosp,incid_rad,incid_dchosp,conf,conf_j1,pos,esms_dc,dc_tot,pos_7j,cv_dose1,esms_cas
