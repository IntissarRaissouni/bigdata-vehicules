# 🚗 Big Data – Analyse des Véhicules

Projet académique réalisé dans le cadre du Master SITBD – Module Big Data  
Université Abdelmalek Essaâdi, Faculté des Sciences et Techniques de Tanger

## 👥 Membres du groupe
- Intissar Raissouni  
- Kaoutar Boudribila  
- Nizar Senbati  

Encadré par : **Pr. Anouar Abdelhakim BOUDHIR**

---

## 🎯 Objectifs du projet

- Mettre en place un environnement Big Data complet (Hadoop + Spark)
- Stocker et traiter des données volumineuses via HDFS
- Effectuer une analyse descriptive sur un dataset de véhicules
- Créer un dashboard de visualisation avec **Apache Superset**

---

## 🛠️ Technologies & Outils

| Outil                | Version / Détail                |
|----------------------|----------------------------------|
| OS                   | Ubuntu Server 22.04              |
| Cluster              | Hadoop 3.3.6 + Spark 3.5.0       |
| Traitement           | Python, PySpark                  |
| Stockage             | HDFS (Hadoop Distributed FS)     |
| Visualisation        | Apache Superset                  |
| Contrôle distant     | SSH                              |
| Versionning          | Git + GitHub                     |

---

## ⚙️ Architecture du cluster

- Cluster pseudo-distribué sur une seule machine
- 1 NameNode + 1 DataNode
- 1 Spark Master + 1 Worker (simulé)

---

## 📁 Arborescence du projet

![image](https://github.com/user-attachments/assets/86808853-e203-4c4f-8087-0cdd1c7239f5)



---

## 🔍 Analyse Réalisée

- **Dataset utilisé :** `vehicles.csv` (> 1 Go, supprimé du dépôt GitHub)
- **Colonnes clés :** region, price, fuel, transmission, drive, etc.

### Traitements Spark :

- Nettoyage des données (nulls, incohérences)
- Agrégations :
  - Prix moyen par région
  - Prix moyen par type de carburant
  - Répartition des transmissions
- Détection de valeurs extrêmes (ex: `price > 500000`)
- Statistiques : moyenne, min, max, std...

---

## 📊 Dashboard Superset : _Analyse Véhicules_

**Graphiques créés :**
- 📈 Bar chart : prix moyen par région
- 🧁 Pie chart : part des transmissions
- 📊 Grouped bar : prix moyen selon carburant et transmission

![image](https://github.com/user-attachments/assets/8e34b7b8-928c-4120-bd26-d783d264757b)


**Fichiers utilisés :**
- `region_avg.csv`
- `fuel_avg.csv`
- `drive_avg.csv`

---

## 🧪 Exécution locale

### Lancer l’environnement :

```bash
./start_bigdata_env.sh
```
### Lancer Superset :
```bash
superset run -h 0.0.0.0 -p 8088 --with-threads --reload
```
Accès via : http://localhost:8080

## 📌 Remarques
Le fichier vehicles.csv dépasse 1 Go et n’est pas inclus dans ce dépôt Git.
