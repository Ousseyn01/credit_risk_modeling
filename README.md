# 🏦 Credit Risk Prediction App

## 📌 Description du projet

Ce projet vise à **prédire le risque de crédit** d’un client (bon ou mauvais payeur) à partir de ses informations socio-économiques, en utilisant des techniques de **Machine Learning supervisé**.

Une application **Streamlit** interactive permet à l’utilisateur de saisir les caractéristiques d’un demandeur de crédit et d’obtenir instantanément une prédiction.

---

## 🎯 Objectifs

* Comprendre les facteurs influençant le **défaut de paiement**
* Mettre en œuvre un pipeline ML complet :

  * Analyse exploratoire des données (EDA)
  * Prétraitement
  * Entraînement d’un modèle
  * Déploiement via une application web
* Simuler un **cas réel de scoring crédit**, très utilisé en banque et finance

---

## 🧠 Approche Machine Learning

* **Type de problème** : Classification binaire
* **Variable cible** :

  * `1` → Bon risque de crédit
  * `0` → Mauvais risque de crédit
* **Modèle utilisé** : `XGBoost Classifier`
* **Justification du modèle** :

  * Performant sur données tabulaires
  * Gère bien les relations non linéaires
  * Robuste au bruit

---

## 📊 Données utilisées

Les données décrivent le profil d’un client demandant un crédit :

| Variable         | Description                   |
| ---------------- | ----------------------------- |
| Age              | Âge du client                 |
| Sex              | Sexe                          |
| Job              | Niveau de qualification (0–3) |
| Housing          | Type de logement              |
| Saving accounts  | Niveau d’épargne              |
| Checking account | Solde du compte courant       |
| Credit amount    | Montant du crédit             |
| Duration         | Durée du crédit (mois)        |

---

## 🔍 Analyse exploratoire (EDA)

### ✔ Analyse univariée

* Distribution de l’âge, du montant du crédit, de la durée
* Fréquence des variables catégorielles
* Détection d’outliers

### ✔ Analyse bivariée

* Relation entre chaque variable et le risque de défaut
* Identification des variables discriminantes
* Analyse métier (ex : comptes faibles → risque plus élevé)

---

## ⚙️ Prétraitement

* Encodage manuel des variables catégorielles
* Conservation d’un preprocessing **identique entre entraînement et prédiction**
* Séparation train / test
* Évaluation des performances du modèle

---

## 🖥️ Application Streamlit

Fonctionnalités :

* Interface simple et intuitive
* Saisie interactive des informations client
* Prédiction instantanée du risque de crédit
* Affichage clair du résultat (GOOD / BAD)

Lancement de l’application :

```bash
streamlit run app.py
```

---

## 📁 Structure du projet

```
credit-risk-prediction/
│
├── app.py                      # Application Streamlit
├── xgboost_credit_model.pkl    # Modèle entraîné
├── README.md                   # Documentation du projet
├── requirements.txt            # Dépendances
└── notebook/
    └── credit_risk_analysis.ipynb
```

---

## 🛠️ Technologies utilisées

* Python
* Pandas / NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Joblib
* Matplotlib / Seaborn (EDA)

---

## 📈 Résultats

* Modèle performant sur données tabulaires
* Variables les plus influentes :

  * Montant du crédit
  * Durée
  * Compte courant
  * Épargne
* Projet représentatif d’un **cas réel bancaire**

---

## 🚀 Améliorations possibles

* Intégrer un `Pipeline sklearn`
* Déploiement cloud (Streamlit Cloud / Hugging Face)

---

## 👤 Auteur

**Ousseynou NDIAYE**
🎓 Master Mathématiques & Informatique – Big Data
🎯 Objectif : Ingénieur Machine Learning / Data Scientist

---
