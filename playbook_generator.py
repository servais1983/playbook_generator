import os
import json
from datetime import datetime
from utils.exporters import export_to_pdf, export_to_json

TEMPLATE_PATH = "templates/base_template.md"
OUTPUT_DIR = "output"

SCENARIOS = [
    "Phishing",
    "Malware",
    "Fuite de données",
    "Intrusion réseau",
    "Compte compromis",
    "Déni de service (DDoS)",
    "Utilisation non autorisée d'un système"
]

def get_input_list(prompt):
    print(prompt + " (laisser vide pour terminer)")
    items = []
    while True:
        item = input("> ")
        if not item:
            break
        items.append(item)
    return items

def collect_user_input():
    print("=== Générateur de Playbook Cybersécurité ===\n")

    organisation = input("Nom de l'organisation : ")
    contact = input("Contact principal (email ou nom) : ")

    for idx, scenario in enumerate(SCENARIOS, 1):
        print(f"{idx}. {scenario}")
    choice = int(input("\nChoisir un type d'incident : "))
    incident_type = SCENARIOS[choice - 1]

    detail_level = input("Niveau de détail (Débutant / Expert) : ").capitalize()
    date_detect = input("Date de détection (JJ/MM/AAAA) : ")
    source_detect = input("Source de détection (SIEM, EDR, utilisateur...) : ")
    gravite = input("Gravité estimée (Faible / Moyenne / Critique) : ")
    responsable = input("Nom du responsable ou de l'équipe : ")
    ticket_id = input("ID du ticket associé (TheHive, JIRA...) : ")
    mitre_tags = get_input_list("Tactiques MITRE ATT&CK (ex: TA0001, TA0002...)")

    print("\n--- Indicateurs de compromission (IoC) ---")
    ip_list = get_input_list("Adresses IP suspectes")
    url_list = get_input_list("URLs suspectes")
    hash_list = get_input_list("Hashs de fichiers suspects")

    outils = get_input_list("Outils utilisés (SIEM, EDR, Firewall, etc.)")

    return {
        "incident_type": incident_type,
        "detail_level": detail_level,
        "date_detect": date_detect,
        "source_detect": source_detect,
        "gravite": gravite,
        "responsable": responsable,
        "organisation": organisation,
        "contact": contact,
        "ticket_id": ticket_id,
        "mitre_tags": mitre_tags,
        "ips": ip_list,
        "urls": url_list,
        "hashs": hash_list,
        "outils": outils
    }

def format_iocs(data):
    lines = []
    lines += [f"- IP : {ip}" for ip in data["ips"]]
    lines += [f"- URL : {url}" for url in data["urls"]]
    lines += [f"- Hash : {h}" for h in data["hashs"]]
    return "\n".join(lines) if lines else "Aucun IoC fourni"

def generate_markdown(data):
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    result = template.format(
        incident_type=data["incident_type"],
        date_detect=data["date_detect"],
        source_detect=data["source_detect"],
        gravite=data["gravite"],
        responsable=data["responsable"],
        detail_level=data["detail_level"],
        organisation=data["organisation"],
        contact=data["contact"],
        ticket_id=data["ticket_id"],
        mitre_tags=", ".join(data["mitre_tags"]),
        iocs=format_iocs(data),
        outils=", ".join(data["outils"])
    )

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename_base = f"{data['incident_type'].lower().replace(' ', '_')}_{timestamp}"
    md_path = os.path.join(OUTPUT_DIR, f"{filename_base}.md")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\n✅ Markdown généré : {md_path}")

    export_to_pdf(md_path)
    export_to_json(data, filename_base)

if __name__ == "__main__":
    data = collect_user_input()
    generate_markdown(data)