#Antonio Contreras
from socketserver import BaseRequestHandler, UDPServer
import time


class GestorSolicitudes(BaseRequestHandler): #La clase hereda del metodo BaseRequestHandler

    def handle(self): # Este metodo solo se ejecuta si hay una conexión o se envía un mensaje
        print(f"Se ha recibido una conexión desde {self.client_address} ")  #Se publica la ip y el puerto del usuario
        mensaje, sock = self.request # se almacena el mensaje enviado por el usuario y su socket
        usuario = str(mensaje).split("'")[1].split(":")[0] # metodos para conseguir el usuario, ya que se envia en el mensaje
        valor = str(mensaje).split("'")[1].split(":")[1] # Se envia un valor, pero solo el del emisor importa
        if usuario == "emisor" and len(ip) >= 1: # Se ejecuta si se ha captuado la ip del receptor
            sock.sendto(valor.encode('ascii'), ip[0]) # si el usuario receptor esta conectado y el emisor ha presionado un boton, se envua un mensaje
        if usuario == "receptor": # Toda esta sección es para almacenar la ip del receptor
            if self.client_address not in ip:
                ip.append(self.client_address)


if __name__ == "__main__": #Metodo para iniciar el programa
    ip = [] #arreglo para guardar las ips
    servidor = UDPServer(('', 443), GestorSolicitudes) #Metodo para crear el server, se necesita especificar el host y el puerto y metodo de manejo de los request
    print("Se ha iniciado el servidor.") #indicar que el servidor esta arriba
    servidor.serve_forever() # Metodo para que el servidor este operando por siempre
