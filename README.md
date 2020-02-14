# ProjetBigData

## hadoop-S3.py

Ce fichier contient le code Python permettant, depuis la VM Hadoop, de récuperer les fichier "train.csv" et "predict.csv" qui sont initialement sur HDFS pour les rapatrier sur la VM Linux puis les envoie sur le S3 de AWS via Boto 3. La VM nécessite alors Python et Boto d'installés.

## test.ipynb

Ce fichier est le notebook Jupyter sur lequel nous avons effectué nos tests. Il n'est pas nécessaire à la mise en production, mais il permet de reprendre la partie finale de nos travaux. Les tests présents dans le notebook ne sont pas représentatifs de l'ensemble des tests réalisés.

## predict.py

Ce fichier en Python contient le code permettant, à partir d'un modèle entraîné d'algorithme de classification, de prédire les risques des personnes du fichier "predict.csv" et les ajoute dans une nouvelle colonne à la fin du fichier.

## ec2-mongo.bat

Ce script en Batch est lancable depuis un système Windows sur lequel vous avez MongoDB d'installé et son service lancé. Il va récupérer sur la machine Linux de AWS EC2 et rapatrier en local le fichier result.csv que l'algorithme a créé. Ce fichier est ensuite importé dans MongoDB dans une nouvelle base de donnée "pbd_cty" dans une nouvelle Collection "result". Certaines valeurs dans ce script sont à remplacer en fonction de votre installation (DNS de l'instance, chemin du fichier, etc) et sont sous la forme "_VARIABLE_A_REMPLACER_".

## Scripts MongoDB.txt

Ce fichier contient un exemple de ligne à entrer dans votre interface (Classique ou Robo 3T) MongoDB afin de chercher les entités (personnes) ayant un et un seul certain risque (entre 1 et 8).
