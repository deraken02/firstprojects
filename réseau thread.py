#Définition d'un client réseau gérant en parallèle l'émission
#et la réception des messages (utilisation de 2 THREADS).

host='192.168.1.168'
port=46000

import socket, sys, threading

class ThreadReception (threading.Thread):
    """objet thread gérant la réception des messages"""
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.connexion == conn
        
    def run(self):
        while 1:
            message_recu=self.connexion.recv(1024).decode("Utf8")
            print ("*"+message_recu+"*")
            if not message_recu or message_recu.upper()=="FIN":
                break
            #le thread<reception> se termine ici
            #On force la fermeture du thread<émission>
            th.E._stop()
            print("Client arrété. Connexion interompue.")
            self.connexion.close()

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission de message"""
    def __init__(self,conn):
        threading.Thread.__init__(self)
        self.connexion=conn
        
    def run(self):
        while 1:
            message_emis=input()
            self.connexion.send(message_emis.encode("Utf8"))

#Programme principal - etablissement de la connexion:
connexion= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print ("Connexion établie avec le serveur.")

#Dialogue avec le serveur: on lance deux threads pour gérer indépendemment l'émission et la réception des messages :
th_E= ThreadEmission(connexion)
th_R= ThreadReception(connexion)
th_E.start()
th_R.start