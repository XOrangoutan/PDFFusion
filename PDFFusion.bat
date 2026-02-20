@echo off
echo --- Fusionner vos PDF ---

:: Dossier source
set /p src="Copier le chemin du dossier avec les pdf sources:"

:: Nom du fichier final
set /p nom="Entrez le nom du fichier final (ex: fusion.pdf) :"

:: Dossier cible (Optionnel: dossier source si vide)
set /p dest="Copier le chemin du dossier de destination (Optionnel: dans le dossier souce si vous appuyez sur entrée):"

:: Lancer le script Python avec les arguments
:: On utilise les guillemets au cas où il y aurait des espaces
if "%dest%"=="" (
    python C:\devs_source\python\PDFFusion\pdffusion.py "%src%" "%nom%"
) else (
    python C:\devs_source\python\PDFFusion\pdffusion.py "%src%" "%nom%" "%dest%"
)
echo Operation terminee !
pause