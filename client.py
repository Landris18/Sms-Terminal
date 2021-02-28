import socket

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('192.168.10.103', 12800))

print("Connexion etablie sur le port {}".format(12800))

msg_a_envoyer = b"Starting..."

while  msg_a_envoyer != b"fin":
        msg_a_envoyer = str(input(">>> "))
        msg_a_envoyer.encode()
        connexion_avec_serveur.send(msg_a_envoyer.encode())
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu.decode())

print("Fin de la connexion")

connexion_avec_serveur.close()
