import os
import json
import subprocess

def export_to_pdf(md_path):
    pdf_path = md_path.replace(".md", ".pdf")
    try:
        subprocess.run(["pandoc", md_path, "-o", pdf_path], check=True)
        print(f"📄 PDF exporté : {pdf_path}")
    except Exception as e:
        print("⚠️ Erreur lors de l'export PDF (pandoc requis) :", e)

def export_to_json(data, filename_base):
    json_path = os.path.join("output", f"{filename_base}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"🧾 JSON exporté : {json_path}")