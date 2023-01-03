# Installation et configuration d'un environnement LAMP et une instance wordpress

[![forthebadge](https://forthebadge.com/images/badges/uses-git.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-wordpress.svg)](https://forthebadge.com)


#### Informations concernant le script ####

Le langage de programmation utilisé pour l'écriture de ce programme est le python en version 3.

Il a été développer dans le but d'automatiser les taches suivantes :

- Installation et configuration d'un environnement LAMP (Linux, Apache, Mysql, Php)
            
- Installation et configuration de wordpress



#### Pré-requis ####

Les prérequis pour l'utilisation de ce script sont :

- Systeme d'exploitation Linux : Je précise que le script a été tester sur une distribution Ubuntu server 22.04 en version LTS

- Avoir le programme Git d'installer sur la distribution,  si il n'est pas installé, vous pourrez le faire avec cette commande : apt install git-all -y

- S'assurer de la version python installer sur le système, pour notre cas nous avons besoin de Python3, qui est normalement disponible par defaut sur ubuntu-server 
  Si pour une raison ou une autre il ne l'est pas, vous pouvez toujours l'installer a l'aide de la commande  : apt-get install python -y



### Utilisation du script ###

Alors, pour pouvoir utiliser de ce script,  il est nécessaire d'avoir un accès root sur le serveur sur lequel vous souhaitez installer wordpress.

- 1 - Ouvrez une ligne de commande et passez root dessus (su root)

- 2 - Vous clonez le projet en question en tapant : git clone https://github.com/SMAINI-Smail/project6.git (le projet sera cloner exactement la ou la commande git clone sera exécutée)
  
- 3 - Vous allez ensuite accéder au projet avec : cd ./projet6
  
- 4 - Vous lancer la commande suivante pour lancer l'installation du script : python3 script_projet6.py
  
Le script va ce lancer, vous laissez dérouler jusqu'a la fin de l'installation. Des messages informatifs vont ce déroulés durant tous le processus de l'installation vous informant de ce que le script est en train de faire et ce jusqu'a la fin de la procédure de l'installation de la stack LAMP et de l'instance Wordpress.


  
#### Outils utilisés pour développer ce script ####

* [python](https://www.python.org) - Langage de programmation 
* [visualstudiocode](https://code.visualstudio.com) - Editeur de textes

LAMP 
* [linux](https://linuxfr.org) - Systeme d'exploitation
* [apache2](https://httpd.apache.org) - Serveur Web
* [mariadb](https://mariadb.org) - Système de gestion de base de données relationnelle 
* [php](https://www.php.net) - Langage de programmation en version 8

wordpress
* [wp-cli](https://wp-cli.org) - Interface de ligne de commande pour WordPress


#### Auteurs ####

SMAINI Smail  
  
  [@SMAINI-Smail](https://github.com/SMAINI-Smail)

#### License ####

Ce projet est sous licence [GNU General Public Licence v3.0] - voir le fichier [License.md](License.md) pour plus d'informations


