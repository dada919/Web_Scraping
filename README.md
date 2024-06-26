# Projet Scraping Site internet Cegef.com

## Objectif du projet

Pour un client (fictif ou non) vous devez coder un (ou plusieurs) script python qui permet d’extraire automatiquement des informations ciblées d’un site web. Votre travail sera comme d’habitude conservé dans un repo github. Dans cette optique, vous avez les specifications suivantes : 

- Choisir un site web avec des données (inscrire votre jeu de donnée dans un google sheet avec toute la classe —> chaque projet devra avoir des data différentes)
- Avoir une problématiques pertinente (cad en lien avec les données ciblées)
- Choisir un outil de scrapping (bs4, selenium, scrappy… )
- Préciser dans un fichier jupyter notebook toutes les étapes de votre récupération de données comme dans  les exercices de cours (wikipedia, welcome to the jungle, kebab …)
- Inclure des temps de pauses pour pouvoir suspendre votre code (pendant une ou deux seconde par exemple). Cela va vous aider à ne pas être signalé comme spam auprès du site.
- Votre projet dispose d’une documentation sous forme de README.md claire et concise qui explique les différentes lignes de code ainsi que comment lancer votre code. 
- Enregistrer votre code dans une base de donnée (vous avez le choix de la technologie) afficher la (les) table(s) de votre base + faire une requête sur vos donnée et printer le résultat 
- Faire une data analyse rapide de vos données récupérées (nombre, format, répartition)
- Paqueter votre script dans un container docker et expliciter les commandes afin de le lancer votre code dans votre README.md a la racine de votre repo 
- (Bonus) Refactorer votre code Jupyter en un main script python orienté objet en utilisant le module argparse afin de permettre l’utilisation d’input utilisateur dans le lancement du script 
- (Bonus) lancer une votre docker dans un vm azure et s’assurer qu’elle a une IP publique afin de pouvoir y accéder  
- (Bonus) utiliser une base de donnée azure pour stocker vos résultats de scrapping 
- (Bonus) deployer votre scrapper dans azure app service
- (Bonus) monitoire vos requête dans azure et envoyer une photo d’un dashboard de votre app en activité

## Lancement du projet
Ouvrir un terminal et se rendre dans le répertoire Projet
```cd .\Projet\```
Puis lancer le docker qui va sraper les données sur le site cegef et les mettre dans une bdd sql
```docker-compose up```
Le projet se lance dans une image python avec scrapy. Les noms et descriptions des formations sont scapé puis enregistrer dans une BDD SQL

### Il est possible de lancer le projet en local et d'enregistrer les données dans un fichier .json
```scrapy crawl cegef -O formation.json```

## Pour afficher toute les formations scrapé
Vous pouvez lancer le fichier **Projet.ipynb** qui va faire un SELECT * From Scraping du fichier scraping.db

![image](https://github.com/dada919/Web_Scraping/assets/77857194/d6030c1f-2b4c-4801-8ca4-2d15a88c5d6f)

## Image Docker du projet

```docker push dada919/webscraping:tagname```
