import os
import sys
import io

from pypdf import PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# --- CONFIGURATION ---
# Remplacez par le chemin de votre dossier contenant les PDF
if len(sys.argv) < 3:
    print("Usage: python script.py <dossier_source> <nom_fichier_final> [dossier_cible] [page de garde entre les fichiers(True/False)]")
    sys.exit(1)
# Dossier source contenant les PDF à fusionner
dossier_source = sys.argv[1]
# Nom du fichier de sortie
nom_fichier_final = sys.argv[2]
# Dossier cible pour le fichier de sortie (optionnel, par défaut le même que le dossier source)
dossier_cible = sys.argv[3] if len(sys.argv) > 3 else sys.argv[1] 
# Permet d'ajouter une page de garde avec le nom du fichier entre chaque PDF (optionnel, par défaut False)
add_file_name = sys.argv[4].lower() == "true" if len(sys.argv) > 4 else False
# Permet de lotir le résultat par paquet de la taille donnée(optionnel, par défaut 0)
lot_size = int(sys.argv[5]) if len(sys.argv) > 5 else 0

# ---------------------
# Fonction d'ajout d'une page de garde
# ---------------------
def ajouter_page_de_garde(writer, fichier):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFont("Helvetica-Bold", 18)
    can.drawCentredString(297, 500, f"Document : {fichier}")
    can.save()
    packet.seek(0)
    writer.append(packet)
# ---------------------
# Fonction de fusion des PDF
# ---------------------
def fusionner_pdfs(repertoire_source, repertoire_cible, nom_sortie, add_file_name=False, lot_size=0):
    merger = PdfWriter()
    file_number = 1
    # Récupérer et trier la liste des fichiers PDF
    fichiers = [f for f in os.listdir(repertoire_source) if f.endswith('.pdf')]
    fichiers.sort() # Trie par ordre alphabétique

    if not fichiers:
        print("Aucun fichier PDF trouvé dans le dossier.")
        return
    idx=0
    for fichier in fichiers:
        if lot_size > 0 and idx >= lot_size:
            # Sauvegarder le lot actuel
            chemin_sortie = os.path.join(repertoire_cible, f"{nom_sortie}_{file_number}")
            with open(chemin_sortie, "wb") as f_sortie:
                merger.write(f_sortie)
            merger.close()
            merger = PdfWriter()
            file_number += 1
            idx = 0
        idx += 1
        chemin_complet = os.path.join(repertoire_source, fichier)
        print(f"Ajout de : {fichier}")
        if add_file_name:
            ajouter_page_de_garde(merger, fichier)
        merger.append(chemin_complet)

    # Sauvegarde du résultat
    chemin_sortie = os.path.join(repertoire_cible,  f"{nom_sortie}_{file_number}")
    with open(chemin_sortie, "wb") as f_sortie:
        merger.write(f_sortie)
    
    merger.close()
    print(f"\nSuccès ! Fichier(s) fusionné(s) créé(s) ici : {repertoire_cible}")

if __name__ == "__main__":
    fusionner_pdfs(dossier_source, dossier_cible, nom_fichier_final, add_file_name, lot_size)
