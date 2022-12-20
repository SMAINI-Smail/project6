import subprocess
import os
from pathlib import Path
from os import chdir as cd
list_fichier_usr_bin = os.listdir('/usr/bin')
list_fichier_usr_sbin = os.listdir('/usr/sbin')


list_fichier = os.listdir('.')
if "install.log" in list_fichier : 
    Path('./install.log').touch()  
else :
    Path('./install.log').touch()

### Ouverture du fichier Install.log 
fichier = open("./install.log", "w")

### Mise a jour du systeme d'exploitation 
print("------------------------------------- Mise a jour du systeme d'exploitation -------------------------------------")
fichier.write("------------------------------------- Mise a jour du systeme d'exploitation ------------------------------------- \n")
update_system= subprocess.Popen(["apt", "update"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("1%")
update_system.stdin.write(update_system.stdout.encoding)
update_system.stdin.close()
for line in update_system.stdout.read():     
    fichier.write(line)
print("50%")

update_system_2= subprocess.Popen(["apt", "full-upgrade", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("51%")
update_system_2.stdin.write(update_system_2.stdout.encoding)
update_system_2.stdin.close()
for line in update_system_2.stdout.read():       
    fichier.write(line)
fichier.write("------------------------------------- fin de la mise à jour du systeme -------------------------------------\n")
print("100%")
print("------------------------------------- fin de la mise à jour du systeme -------------------------------------")



### Installation et configuration du serveur apache 2
fichier.write("------------------------------------- Installation et configuration du serveur apache 2 -------------------------------------- \n")
print("------------------------------------- Installation et configuration du serveur apache 2 --------------------------------------")

# Vérifier si Apache2 existe
if "apache2" in list_fichier_usr_sbin :

    # desinstallation d'Apache2
    print("Le serveur web apache2 est dèja installé\n")
    fichier.write("Le serveur web apache2 est dèja installé\n")
    print("desinstallation du serveur apache2 ...\n")
    fichier.write("desinstallation du serveur apache2 ...\n")
    fichier.write("___________________ desinstaller apache2 ______________ \n")
    remove_apache= subprocess.Popen(["apt-get", "autoremove", "--purge", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_apache.stdin.write(remove_apache.stdout.encoding)
    remove_apache.stdin.close()
    for line in remove_apache.stdout.read():       
        fichier.write(line)
    print("Fin de desinstallation du serveur apache2")

## Installation d'Apache2
print("Debut d'installation du serveur apache2 ")
message_apache= "_________________________________ Installation du serveur web appache en cours __________________________ \n"
fichier.write(message_apache)
install_apache= subprocess.Popen(["apt", "install", "apache2", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_apache.stdin.write(install_apache.stdout.encoding)
install_apache.stdin.close()
for line in install_apache.stdout.read():       
    fichier.write(line)
fichier.write("___________________ fin d'installation du serveur _______________\n")
print("Fin d'installation du serveur apache2 ")

## lancement du serveur apache 2
print("lancement  du serveur apache 2 au démarrage du system ")
fichier.write("___________________ lancement  du serveur apache 2 au démarrage du system_______________ \n")
lance_apache= subprocess.Popen(["systemctl", "enable", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
lance_apache.stdin.write(lance_apache.stdout.encoding)
lance_apache.stdin.close()
for line in lance_apache.stdout.read():          
    fichier.write(line)

## Activation des modules:  headers,deflate,rewrite, SSL
fichier.write("___________________ Activation des modules: headers, deflate, rewrite, SSL_______________ \n\n\n")
fichier.write("___________________ Activation de headers _______________ \n")
print(" activation de headers")
os.system("a2enmod headers")
fichier.write("___________________ Activation de rewrite _______________ \n")
print(" activation de rewrite")
os.system("a2enmod rewrite")
fichier.write("___________________ Activation de deflate _______________ \n")
print(" activation de deflate")
os.system("a2enmod deflate")
fichier.write("___________________ Activation de SSL _______________ \n")
print(" activation de ssl")
os.system("a2enmod ssl")

## Configuration du fichier apache2.conf pour  cacher la version du serveur apache2 sur le navigateur 
fichier.write("___________________ configurer le fichier apache2.conf_______________ \n")
print("___________________ configurer le fichier apache2.conf_______________ ")
droit_apache= subprocess.Popen(["chmod", " +w ", "/etc/apache2/apache2.conf"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_apache.stdin.write(droit_apache.stdout.encoding)
droit_apache.stdin.close()
for line in droit_apache.stdout.read(): 
    fichier.write(line)
apache_conf = open("/etc/apache2/apache2.conf", "a")
apache_conf.write("\n \n  ServerTokens Prod")
apache_conf.close()

## redemarrer le serveur apache 2
print("redemarrer le serveur  apache2 ")
fichier.write("___________________ Redemarrage du serveur apache 2 _______________ \n")
reboot_apache= subprocess.Popen([  "systemctl", "restart", "apache2"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
reboot_apache.stdin.write(reboot_apache.stdout.encoding)
reboot_apache.stdin.close()
for line in reboot_apache.stdout.read():   
    fichier.write(line)

## supprimer le fichier /var/www/html/index.html 
fichier.write("___________________ supprimer le fichier /var/www/html/index.html _______________ \n")
print("supprimer le fichier /var/www/html/index.html ")
delete_index= subprocess.Popen([  "rm","-f" "/var/www/html/index.html"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
delete_index.stdin.write(delete_index.stdout.encoding)
delete_index.stdin.close()
for line in delete_index.stdout.read(): 
    fichier.write(line)

## creation du dossier /var/www/html/wordpress/ 
fichier.write("___________________ creation du dossier /var/www/html/wordpress/_______________ \n")
print("creation du dossier /var/www/html/wordpress/ ")
cree_dossier= subprocess.Popen([  "mkdir", "/var/www/html/wordpress/"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
cree_dossier.stdin.write(cree_dossier.stdout.encoding)
cree_dossier.stdin.close()
for line in cree_dossier.stdout.read():   
    fichier.write(line)

## Configuration du fichier /etc/apache2/sites-enabled/000-default.conf   
fichier.write("___________________ configuration du fichier /etc/apache2/sites-enabled/000-default.conf _______________ \n")
print("configuration du fichier /etc/apache2/sites-enabled/000-default.conf")

delete_index= subprocess.Popen([  "rm","-f" "/etc/apache2/sites-enabled/000-default.conf"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
delete_index.stdin.write(delete_index.stdout.encoding)
delete_index.stdin.close()
for line in delete_index.stdout.read(): 
    fichier.write(line)

Path('/etc/apache2/sites-enabled/000-default.conf').touch()

# ouvrir le fichier /etc/apache2/sites-enabled/000-default.conf
apache_config = open("/etc/apache2/sites-enabled/000-default.conf", "w")
apache_config.write("<VirtualHost *:80> \n\n")
apache_config.write("ServerAdmin webmaster@localhost   \n")
apache_config.write("DocumentRoot /var/www/html/wordpress/ \n\n")
apache_config.write("ErrorLog ${APACHE_LOG_DIR}/error.log \n")
apache_config.write("CustomLog ${APACHE_LOG_DIR}/access.log combined\n\n")
apache_config.write("  </VirtualHost> \n")
apache_config.close()

fichier.write("------------------------------------- Fin de l'installation et de la configuration du serveur apache 2 -------------------------------------- \n")
print("------------------------------------- Fin de l'installation et de la configuration du serveur apache 2 -------------------------------------- ")




fichier.write("------------------------------------- Installation et configuration PHP -------------------------------------- \n")
print("------------------------------------- Installation et configuration PHP --------------------------------------")

# Vérifier si PHP existe
if "php" in list_fichier_usr_bin  :
    ## desinsatller php
    fichier.write( " ___________________  Le programme PHP est dèja installé sur le serveur ___________________ \n")
    print( " ___________________  Le programme PHP est dèja installé sur le serveur ___________________ \n")
    fichier.write("___________________ desinstaller php ______________ \n")
    print("___________________ desinstaller php ______________")
    purge_php= subprocess.Popen(["apt-get","remove", "--purge", "php7.*","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    purge_php.stdin.write(purge_php.stdout.encoding) 
    purge_php.stdin.close()
    for line in purge_php.stdout.read():       
        fichier.write(line)
    remove_php= subprocess.Popen(["apt-get", "autoremove","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_php.stdin.write(remove_php.stdout.encoding)
    remove_php.stdin.close()
    for line in remove_php.stdout.read():       
        fichier.write(line) 
    os.system("apt-get update -y")
    print("Fin de desinstallation de php")

## installer php 
fichier.write("___________________ Debut d'installation de php ___________________  ")
print("___________________ Debut d'installation de php ___________________  ")
# installation des dependances 
fichier.write("___________________ Installation des dépendances___________________  ")
print("___________________ Installation des dépendances___________________  ")
install_dependance= subprocess.Popen(["apt-get", "install", "ca-certificates", "apt-transport-https", "software-properties-common", "wget", "curl", "lsb-release", "-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_dependance.stdin.write(install_dependance.stdout.encoding)
install_dependance.stdin.close()
for line in install_dependance.stdout.read(): 
    fichier.write(line)

# install php7.4
fichier.write("___________________ Installation de php7.4___________________  ")
print("___________________ Installation de php7.4____________________  ")
install_php= subprocess.Popen(["apt", "install", "php7.4","php-mysql","-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_php.stdin.write(install_php.stdout.encoding)
install_php.stdin.close()
for line in install_php.stdout.read(): 
    fichier.write(line)
fichier.write("___________________ Installation de libapache2-mod-php7.4 __________________  ")
print("___________________ Installation de libapache2-mod-php7.4 ____________________  ")
install_libapache2= subprocess.Popen([  "apt", "install", "libapache2-mod-php7.4", "-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_libapache2.stdin.write(install_libapache2.stdout.encoding)
install_libapache2.stdin.close()
for line in install_libapache2.stdout.read(): 
    fichier.write(line)

os.system("systemctl restart apache2")

## installer les dependance de php dont a besoin l'application                                               
install_php_2= subprocess.Popen(["apt", "install","php7.4-common","php7.4-curl","php7.4-bcmath","php7.4-intl","php7.4-mbstring","php7.4-xmlrpc","php7.4-gd","php7.4-xml","php7.4-cli","php7.4-zip","-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_php_2.stdin.write(install_php_2.stdout.encoding)
install_php_2.stdin.close()
for line in install_php_2.stdout.read(): 
    fichier.write(line)

fichier.write("___________________ Améliorer les performances ___________________  ")
print("___________________Améliorer les performances____________________  ")
install_performance= subprocess.Popen(["apt", "install", "php7.4-fpm", "libapache2-mod-fcgid","-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_performance.stdin.write(install_performance.stdout.encoding)
install_performance.stdin.close()
for line in install_performance.stdout.read(): 
    fichier.write(line)
os.system("a2enmod proxy_fcgi setenvif ")
os.system("a2enconf php7.4-fpm")
os.system("systemctl restart apache2")

fichier.write("------------------------------------- Fin de l'installation et de la configuration PHP -------------------------------------- \n")
print("------------------------------------- Fin de l'installation et de la configuration PHP --------------------------------------")




fichier.write("------------------------------------- Installation et configuration du serveur mariadb -------------------------------------- \n")
print("------------------------------------- Installation et configuration du serveur mariadb --------------------------------------")

if "mariadb" in list_fichier_usr_bin  :
    #Desinstallation de mariadb 
    print(" Le serveur MariaDB est dèja installé sur le serveur, on procede a sa desinstallation ")
    fichier.write("___________________ Le serveur MariaDB est dèja installé sur le serveur, on procede a sa desinstallation______________ \n")
    stop_maria= subprocess.Popen(["systemctl", "stop", "mysql"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stop_maria.stdin.write(stop_maria.stdout.encoding)
    stop_maria.stdin.close()
    for line in stop_maria.stdout.read():     
        fichier.write(line)
    remove_maria= subprocess.Popen(["apt-get", "--purge","remove", "mariadb-server","-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    remove_maria.stdin.write(remove_maria.stdout.encoding)
    remove_maria.stdin.close()
    for line in remove_maria.stdout.read():       
        fichier.write(line)
    os.system("apt remove --purge  mysql-common -y")
    os.system("apt-get autoremove -y")

    print("Fin de desinstallation de  mariadb")

## installation de mariadb-serveur    
fichier.write("_____________________ Début de l'installation de MariaDB ___________________________ \n")
print(" Installation de MariaDB en cours ... \n")
install_maria= subprocess.Popen([  "apt", "install", "mariadb-server","-y" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_maria.stdin.write(install_maria.stdout.encoding)
install_maria.stdin.close()
for line in install_maria.stdout.read():   
    fichier.write(line)
fichier.write("_____________________ Fin de l'installation de MariaDB ___________________________ \n")
print(" Fin de l'installation de MariaDB \n")

## Autoriser mariadb a démarrer avec le boot du système
fichier.write("___________________ lancement  de MariaDb au démarrage du system_______________ \n")
print("  lancement  de MariaDb au démarrage du systeme ")
lance_maria= subprocess.Popen(["systemctl", "enable", "mariadb"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
lance_maria.stdin.write(lance_maria.stdout.encoding)
lance_maria.stdin.close()
for line in lance_maria.stdout.read():     
    fichier.write(line)
    
## reboot du maria
fichier.write("___________________ redemarré le serveur MariaDB _______________ \n")
print(" redemarré le serveur MariaDB  ")
reboot_maria= subprocess.Popen(["systemctl", "restart", "mariadb"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
reboot_maria.stdin.write(reboot_maria.stdout.encoding)
reboot_maria.stdin.close()
for line in reboot_maria.stdout.read():
    fichier.write(line)
    
## Securisé l'instance de mariaDB 
fichier.write("___________________ creer un nouveau USER (admin_wp,passwd_wp) _______________ \n")
print(" creer un nouveau USER (admin_wp,passwd_wp) ")
new_user= subprocess.Popen(["mariadb", "-e", "CREATE USER 'admin_wp'@'localhost' IDENTIFIED BY 'passwd_wp';" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
new_user.stdin.write(new_user.stdout.encoding)
new_user.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

## Creation d'une base de donnée
fichier.write("___________________ creer une nouvelle base de donnée (database_wp) _______________ \n")
print(" creer une nouvelle base de donnée (database_wp) ")
new_database= subprocess.Popen(["mariadb", "-e", "CREATE DATABASE database_wp;" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
new_database.stdin.write(new_database.stdout.encoding)
new_database.stdin.close()
for line in new_database.stdout.read():
    fichier.write(line)

## Ajouter les privileges
fichier.write("___________________ ajouter les privileges pour le nouveau utilisateur sur la nouvelle base de donnée _______________ \n")
print(" ajouter les privileges pour le nouveau utilisateur sur la nouvelle base de donnée  ")
privileges= subprocess.Popen(["mariadb", "-e", "GRANT ALL PRIVILEGES ON database_wp.* TO 'admin_wp'@'localhost' ;" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
privileges.stdin.write(privileges.stdout.encoding)
privileges.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

fichier.write("___________________ FLUSH PRIVILEGES _______________ \n")
flush_privileges= subprocess.Popen(["mariadb", "-e", "FLUSH PRIVILEGES;" ] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
flush_privileges.stdin.write(flush_privileges.stdout.encoding)
flush_privileges.stdin.close()
for line in new_user.stdout.read():
    fichier.write(line)

fichier.write("------------------------------------- Fin de l'installation et de la configuration du serveur mariadb -------------------------------------- \n")
print("------------------------------------- Fin de l'installation et de la configuration du serveur mariadb --------------------------------------")




fichier.write("------------------------------------- Installation et configuration de Wordpress -------------------------------------- \n")
print("------------------------------------- Installation et configuration de Wordpress --------------------------------------")

##  installation de wp cli

fichier.write("___________________ ajouter le repository _______________ \n")
print("___________________ ajouter le repository _______________ ")
cd('/')
os.system("add-apt-repository ppa:tiagohillebrandt/wp-cli" )


fichier.write("___________________ mettre a jours le systeme _______________ \n")
print("___________________ mettre a jours le systeme _______________ ")
update= subprocess.Popen(["apt-get","update", "-y"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
update.stdin.write(update.stdout.encoding)
update.stdin.close()
for line in update.stdout.read(): 
    fichier.write(line)

fichier.write("___________________ installer wp-cli _______________ \n")
print("___________________ installer wp-cli_______________ ")
install_wp= subprocess.Popen(["apt-get","install", "wp-cli"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_wp.stdin.write(install_wp.stdout.encoding)
install_wp.stdin.close()
for line in install_wp.stdout.read(): 
    fichier.write(line)

## acceder au dossier /var/www/html/wordpress/
cd('/var/www/html/wordpress/')
fichier.write("___________________ telecharger wordpress _______________ \n")
print("___________________ telecharger wordpress _______________ ")
download_wp= subprocess.Popen(["wp","--allow-root", "core", "download"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
download_wp.stdin.write(download_wp.stdout.encoding)
download_wp.stdin.close()
for line in download_wp.stdout.read(): 
    fichier.write(line)

## donner les droits pour le fichier /var/www/html/wordpress/
fichier.write("___________________ donner les droits pour le fichier /var/www/html/wordpress/ _______________ \n")
print("___________________ donner les droits pour le fichier /var/www/html/wordpress/ _______________ ")
droit_html= subprocess.Popen(["chown", "-R", "www-data:www-data", "/var/www/html/wordpress/"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
droit_html.stdin.write(droit_html.stdout.encoding)
droit_html.stdin.close()
for line in droit_html.stdout.read(): 
    fichier.write(line)

## generation du fichier /var/www/html/wordpress/wp-config.php (ou se trouve toute les configurations necessaire pour une application wordpress)
fichier.write("___________________ generation du fichier /var/www/html/wordpress/wp-config.php_______________ \n")
print("generation du fichier /var/www/html/wordpress/wp-config.php ")
generate_config_php= subprocess.Popen(["wp","--allow-root", "config", "create", "--dbname=database_wp","--dbuser=admin_wp", "--dbpass=passwd_wp", "--dbhost=localhost", "--dbprefix=projet6_"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
generate_config_php.stdin.write(generate_config_php.stdout.encoding)
generate_config_php.stdin.close()
for line in generate_config_php.stdout.read(): 
    fichier.write(line)
    print(line)
os.system("chown -R www-data:www-data /var/www/html/wordpress/wp-config.php")
os.system("chmod 600 /var/www/html/wordpress/wp-config.php")
os.system("chmod -R 755 $(find /var/www/html/wordpress/ -type d)")
os.system("chmod -R 644 $(find /var/www/html/wordpress/ -type f)")

## Recuperation de la base de donnée de wordpress
fichier.write("___________________ injection de la base de donnée wordpress dans la base de donnée cree auparavant  _______________\n")
print("___________________ injection de la base de donnée wordpress dans la base de donnée cree auparavant  _______________")
create_data_base= subprocess.Popen(["wp", "--allow-root","db", "create"] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
create_data_base.stdin.write(create_data_base.stdout.encoding)
create_data_base.stdin.close()
for line in create_data_base.stdout.read():
    fichier.write(line)

## Supprission du fichier /var/www/html/wordpress/wp-config-sample.php qui a fait office d'exemple pour le fichier wp-config.php
fichier.write("___________________ Supprission du fichier /var/www/html/wordpress/wp-config-sample.php  _______________ \n")
print("Supprission du fichier /var/www/html/wordpress/wp-config-sample.php ")
os.system("rm -f /var/www/html/wordpress/wp-config-sample.php")

## Creation du premier site de l'application installer 
fichier.write("___________________ Creation du site de l'application_______________ \n")
print("Creation du site de l'application ")
install_site= subprocess.Popen(["wp", "--allow-root","core", "install","--url=http://localhost", "--title='Projet_6'", "--admin_user=admin", "--admin_password=passwd_wp" ,"--admin_email=admin@gmail.fr",] ,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
install_site.stdin.write(install_site.stdout.encoding)
install_site.stdin.close()
for line in install_site.stdout.read(): 
    fichier.write(line)

fichier.write("------------------------------------- Fin de l'installation et de la configuration de wordpress-------------------------------------- \n")
print("------------------------------------- Fin de l'installation et de la configuration de wordpress--------------------------------------")



fichier.write("------------------------------------- Fin de l'installation de l'environnement -------------------------------------- \n")
fichier.close()
print("------------------------------------- Fin de l'installation de l'environnement --------------------------------------")