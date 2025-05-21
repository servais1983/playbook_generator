# 🛡️ Générateur de Playbooks Cybersécurité

Outil en ligne de commande permettant de générer des playbooks d'incidents de cybersécurité structurés.

## 📋 Fonctionnalités

- Interface CLI interactive pour collecter les informations d'incident
- Génération de playbooks au format Markdown
- Export PDF (via pandoc) et JSON pour intégration avec d'autres outils
- Support des IoCs (IP, URL, Hashs)
- Classification MITRE ATT&CK

## 🔧 Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/servais1983/playbook_generator.git
cd playbook_generator
```

2. Installer pandoc (requis pour l'export PDF) :
```bash
sudo apt install pandoc
```

## 🚀 Utilisation

Lancez le générateur :
```bash
python3 playbook_generator.py
```

L'outil vous guidera à travers une série de questions pour collecter les informations sur l'incident.

## 📁 Structure du projet

- `playbook_generator.py` : Script principal
- `templates/` : Modèles Markdown pour les playbooks
- `utils/` : Utilitaires pour l'export (PDF, JSON)
- `output/` : Playbooks générés (MD, PDF, JSON)

## 📊 Types d'incidents supportés

- Phishing
- Malware
- Fuite de données
- Intrusion réseau
- Compte compromis
- Déni de service (DDoS)
- Utilisation non autorisée d'un système

## 🔄 Intégration

Les fichiers JSON générés peuvent être utilisés pour l'intégration avec d'autres outils comme :
- Plateformes SOAR
- Systèmes de ticketing (JIRA, TheHive)
- Bases de connaissances internes