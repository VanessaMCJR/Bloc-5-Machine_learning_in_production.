# Bloc-5-Machine_learning_in_production_on_heroku

Wine quality prediction

# ML en production

**Wine-o-meter** est une future application qui permettrait aux viticulteurs de prédire la note de la qualité de leur vin en fonction des caractéristiques physico-chimiques. 
La startup à l'origine de cette innovation est convaincue de sa capacité à bouleverser le monde du vin. 🍷

Une équipe de data-science a travaillé ensemble pour créer le meilleur modèle prédisant le score de qualité (de 0 à 10) de plusieurs vins. (fichier Model_training.ipynb)

A ce stade du projet, mon travail consiste à mettre le modèle en production.

Donc, j'ai utilisé le fichier Model_training.ipynb créer par l'équipe de data-science dans le but de générer un fichier joblib qui se nomme "model.joblib".

Ensuite, à l'aide fichier app.py, j'ai développé une application web grâce framework Flask, qui est capable de prendre en entrée les caractéristiques physico-chimiques d'un ou plusieurs vins sous la forme suivante : 

`import requests

response = requests.post("https://api-wine-quality-prediction.herokuapp.com/predict", json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})`


print(response.json())


Et enfin, grâce à ce même fichier app.py de faire la prédiction suite à l'entrée des données. En effet, app.py est capable de charger ou d'utiliser le modèle de machine learning grâce au fichier model.joblib.

Exemple:

{"predict": [6.0]}


Par ailleurs, il y a aussi le fichier requirements.txt qui contient toutes les librairies nécessaire au bon fonctionnement de l'application.

Et le "dossier templates" a tout le code html qui est une petite documentation permettant aux utilisateurs de savoir comment utiliser l'application accessible directement :
"https://api-wine-quality-prediction.herokuapp.com"

Et le dossier "static" permet d'ajouter du style css au code html.

Et le fichier Procfile permet d'indiquer à l'hébergeur qui est heroku (choisit ici) qu'il s'agit d'une application web.

Au final on retrouve le fichier Test_Endpoint.ipynb qui permet de tester l'application web.









