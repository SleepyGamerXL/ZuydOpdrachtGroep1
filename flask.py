from flask import Flask
import socket

app = Flask(__name__)

def get_ip(): #Functie om het IP te krijgen van Host
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Gebruikt IPv4 en het UDP Protocol
    s.settimeout(0) #Als de connectie hieronder sloom is, of de host kan niet verbinden, komt het programma niet vast te lopen
    try:
        s.connect(('10.10.10.100', 1))  #Dit is een "nep" IP, wij gaan er van uit dat dit IP niet in het netwerk staat
        ip = s.getsockname()[0]  #Kijkt naar het IP van de Host wat is gebruikt om een packet te sturen naar 10.10.10.100:1 en verkrijgt hier het IP van
    except Exception: 
        ip = '127.0.0.1' #Als er iets fout gaat, wordt er een redirect gebruikt naar localhost  
    finally:
        s.close()
    return ip

@app.route('/')
def home():
    return 'Dit is een test' #Dit is wat er op de webpagina staat 

if __name__ == '__main__':
    ip_address = get_ip()  
    print(f"Flask is running on {ip_address}:5000") #Laat de Host zien welk IP er wordt gebruikt.Hiermee kunnen users inloggen
    app.run(host=ip_address, port=5000) #De webpagina wordt gestart met het IP adres van de Host, en poort 5000
