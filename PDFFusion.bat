@echo off
echo --- Fusionner vos PDF ---

:: Dossier source
set /p src="Copier le chemin du dossier avec les pdf sources:"

:: Nom du fichier final
set /p nom="Entrez le nom du fichier final (ex: fusion.pdf) :"

:: Dossier cible (Optionnel: dossier source si vide)
set /p dest="Copier le chemin du dossier de destination (Optionnel: dans le dossier souce si vous appuyez sur entrée):"

:: Ajout d'une page de garde (Oui/Non, par défaut: Non)
set pagegarde="N"
set /p pagegarde="page de garde entre les fichiers(O: Oui/N: Non)[par défaut: Non]:"

:: Ajout d'une option pour fusionner par lot (0 pour désactiver, par défaut: 0)
set lot_size=0
set /p lot_size="Regrouper les fichiers par lot (0 pour désactiver, un entier pour le nombre de fichiers par lot) [par défaut: 0]:"

:: Lancer le script Python avec les arguments
:: On utilise les guillemets au cas où il y aurait des espaces
if "%dest%"=="" (
    set dest=%src%
)
if /I "%pagegarde%"=="O" (
    set "add_file_name=True"
) else (
    set "add_file_name=False"
)
python C:\devs_source\python\PDFFusion\pdffusion.py "%src%" "%nom%" "%dest%" "%add_file_name%" "%lot_size%"
echo Operation terminee !
pause