import os
import sys

from pypdf import PdfWriter

# --- CONFIGURATION ---
# Remplacez par le chemin de votre dossier contenant les PDF
if len(sys.argv) < 3:
    print("Usage: python script.py <dossier_source> <nom_fichier_final> [dossier_cible]")
    sys.exit(1)

dossier_source = sys.argv[1]
nom_fichier_final = sys.argv[2]
dossier_cible = sys.argv[3] if len(sys.argv) > 3 else sys.argv[1] 
# ---------------------

def fusionner_pdfs(repertoire_source, repertoire_cible, nom_sortie):
    merger = PdfWriter()
    
    # Récupérer et trier la liste des fichiers PDF
    fichiers = [f for f in os.listdir(repertoire_source) if f.endswith('.pdf')]
    fichiers.sort() # Trie par ordre alphabétique

    if not fichiers:
        print("Aucun fichier PDF trouvé dans le dossier.")
        return

    for fichier in fichiers:
        chemin_complet = os.path.join(repertoire_source, fichier)
        print(f"Ajout de : {fichier}")
        merger.append(chemin_complet)

    # Sauvegarde du résultat
    chemin_sortie = os.path.join(repertoire_cible, nom_sortie)
    with open(chemin_sortie, "wb") as f_sortie:
        merger.write(f_sortie)
    
    merger.close()
    print(f"\nSuccès ! Fichier fusionné créé ici : {chemin_sortie}")

if __name__ == "__main__":
    fusionner_pdfs(dossier_source, dossier_cible, nom_fichier_final)
