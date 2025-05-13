# Importation des modules nécessaires
from flask import Flask, request
from flask_mysqldb import MySQL
import socket
import requests
import os
import netifaces # Importation de la nouvelle bibliothèque


# Initialisation de l'application Flask
app = Flask(__name__)

# --- Configuration de la base de données MySQL ---

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'reseau_users' 
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' 

#animation HTML CSS JS
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading . . .</title>
    <style>
        p{margin-top: 0;
            margin-bottom: 0;;}

        .mainFrame{
            display: grid;
            grid-template-columns: 200px;
            justify-content: center;
            align-items: center;
            height: 800px;
        }
        .jFrame1{
            justify-content: flex-start;
        }
        .loader {
            padding-top: 50px;
            --w:10ch;
            font-weight: bold;
            font-family: monospace;
            font-size: 50px;
            line-height: 1.2em;
            letter-spacing: var(--w);
            width: var(--w);
            overflow: hidden;
            white-space: nowrap;
            color: #0000;
            animation: l19 2s infinite linear;
          }
          .loader:before {
            content:"Loading...";
          }
          
          @keyframes l19 {
             0% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
             4% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
             8% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            12% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            16% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            20% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            24% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            28% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            32% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
            36% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0}
            40%,
            60% {text-shadow: 
                  calc( 0*var(--w)) 0 #000,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            64% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0 #000,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            68% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0 #000,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            72% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0 #000,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            76% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0 #000, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            80% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0 #000,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            84% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0 #000,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            88% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0 #000,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            92% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0 #000,calc(-9*var(--w)) 0 #000}
            96% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0 #000}
            100% {text-shadow: 
                  calc( 0*var(--w)) 0,calc(-1*var(--w)) 0,calc(-2*var(--w)) 0,calc(-3*var(--w)) 0,calc(-4*var(--w)) 0, 
                  calc(-5*var(--w)) 0,calc(-6*var(--w)) 0,calc(-7*var(--w)) 0,calc(-8*var(--w)) 0,calc(-9*var(--w)) 0}
          }
    </style>
</head>
<body>
    <div class="mainFrame">
        <div class="jFrame1">
            <div class="loader"></div>
        </div>
    </div>
</body>
</html>

"""

mysql = MySQL(app)

# Fonction pour obtenir l'adresse IP privée
def get_private_ip():
    try:
        # Liste toutes les interfaces réseau disponibles
        interfaces = netifaces.interfaces()

        for iface in interfaces:
            # Tente d'obtenir les adresses pour l'interface
            try:
                addresses = netifaces.ifaddresses(iface)
            except ValueError:
                # L'interface n'existe pas ou n'a pas d'adresses
                continue

            # Vérification d'adresses IPv4 
            if netifaces.AF_INET in addresses:
                # Parcourt toutes les adresses IPv4 associées à cette interface
                for link in addresses[netifaces.AF_INET]:
                    ip_address = link['addr']

                    # Manala an'ilay loopback(localhost) adresse ip(trillage)
                    
                    if not ip_address.startswith('127.') and iface != 'lo' and 'docker' not in iface and 'veth' not in iface:
                        # Retourne la première adresse IP privée non-loopback trouvée
                        return ip_address

        # Parcours d'interfaces reseaux
        return "N/A"

    except Exception as e:
        print(f"Erreur lors de l'obtention de l'IP privée via netifaces : {e}")
        return "N/A"

# IP publiques
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        return response.text
    except Exception as e:
        print(f"Erreur lors de l'obtention de l'IP publique : {e}")
        return "N/A"

# device name
def get_hostname():
    try:
        return socket.gethostname()
    except Exception as e:
        print(f"Erreur lors de l'obtention du nom d'hôte : {e}")
        return "N/A"

# Route principale de l'application web
@app.route('/')
def index():
    # Récupère les informations de l'utilisateur
    public_ip = get_public_ip()
    private_ip = get_private_ip() 
    hostname = get_hostname()

    try:
        # Connexion à la base de données
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users_info (public_ip, private_ip, hostname) VALUES (%s, %s, %s)",
                    (public_ip, private_ip, hostname))

        # Valide la transaction
        mysql.connection.commit()

        cur.close()

        return HTML_PAGE

    except Exception as e:
        
        print(f"Erreur lors de l'insertion dans la base de données : {e}")
        return "Une erreur est survenue lors de l'enregistrement de vos informations.", 500

if __name__ == '__main__':
    app.run(debug=True)
