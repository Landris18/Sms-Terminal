try:

	import socket

	hote = "localhost"
	port = 12500

	connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connexion_principale.bind((hote, port))
	
	msg_a_envoyer = b"Starting..."
	
	while msg_a_envoyer != b"Aborting...":
		msg_a_envoyer = input(">>> ")
		msg_a_envoyer.encode()
		connexion_avec_server.send(msg_a_envoyer)
		msg_recu = connexion_avec_server.recv(1024)
		print(msg_recu.decode())
	
	print("Fin de la connexion...")
	connexion_avec_server.close()

except:
	print("Lancez le serveur")
