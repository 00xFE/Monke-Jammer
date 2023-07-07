import random
import socket
import sys

logo = '''
                                            ______             ________  ________                                                                  
                                        /      \           /        |/        |                                                                 
                                        /$$$$$$  | __    __ $$$$$$$$/ $$$$$$$$/                                                                  
                                        $$$  \$$ |/  \  /  |$$ |__    $$ |__                                                                     
                                        $$$$  $$ |$$  \/$$/ $$    |   $$    |                                                                    
                                        $$ $$ $$ | $$  $$<  $$$$$/    $$$$$/                                                                     
                                        $$ \$$$$ | /$$$$  \ $$ |      $$ |_____                                                                  
                                        $$   $$$/ /$$/ $$  |$$ |      $$       |                                                                 
                                        $$$$$$/  $$/   $$/ $$/       $$$$$$$$/                                                                                                                                                                                           
 __       __   ______   __    __  __    __  ________         _____   ______   __       __  __       __  ________  _______  
/  \     /  | /      \ /  \  /  |/  |  /  |/        |       /     | /      \ /  \     /  |/  \     /  |/        |/       \ 
$$  \   /$$ |/$$$$$$  |$$  \ $$ |$$ | /$$/ $$$$$$$$/        $$$$$ |/$$$$$$  |$$  \   /$$ |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |
$$$  \ /$$$ |$$ |  $$ |$$$  \$$ |$$ |/$$/  $$ |__  ______      $$ |$$ |__$$ |$$$  \ /$$$ |$$$  \ /$$$ |$$ |__    $$ |__$$ |
$$$$  /$$$$ |$$ |  $$ |$$$$  $$ |$$  $$<   $$    |/      |__   $$ |$$    $$ |$$$$  /$$$$ |$$$$  /$$$$ |$$    |   $$    $$< 
$$ $$ $$/$$ |$$ |  $$ |$$ $$ $$ |$$$$$  \  $$$$$/ $$$$$$//  |  $$ |$$$$$$$$ |$$ $$ $$/$$ |$$ $$ $$/$$ |$$$$$/    $$$$$$$  |
$$ |$$$/ $$ |$$ \__$$ |$$ |$$$$ |$$ |$$  \ $$ |_____     $$ \__$$ |$$ |  $$ |$$ |$$$/ $$ |$$ |$$$/ $$ |$$ |_____ $$ |  $$ |
$$ | $/  $$ |$$    $$/ $$ | $$$ |$$ | $$  |$$       |    $$    $$/ $$ |  $$ |$$ | $/  $$ |$$ | $/  $$ |$$       |$$ |  $$ |
$$/      $$/  $$$$$$/  $$/   $$/ $$/   $$/ $$$$$$$$/      $$$$$$/  $$/   $$/ $$/      $$/ $$/      $$/ $$$$$$$$/ $$/   $$/ 
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣶⣶⣤⣀⣀⣀⣠⡴⣿⣦⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣿⠟⠉⠀⠀⠀⠀⠈⠙⠻⣯⡁⠀⠀⠀⠀⠀⠀⠉⠙⣟⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠋⠀⠀⠀⠀⠐⢶⣤⡀⠀⠈⠙⢶⣄⡀⠀⠀⠀⠀⠀⠈⠙⠛⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⢀⣠⣴⣶⣶⣤⣴⣿⣿⣿⣿⣿⡏⠀⠀⢀⣴⠾⠛⠋⠉⠛⢶⣄⠀⠀⠈⠛⠷⣦⣄⣀⠀⠀⠀⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⣰⡿⠛⠉⠁⠀⠈⠙⢿⣿⣿⣿⣿⡇⠀⠀⣸⣿⣦⠀⠀⠀⠀⠀⠉⠻⢦⣀⡀⠀⠈⠙⠛⠿⢶⣶⣤⣤⣤⣤⣾⣷⣶⣤⣀⠀⠀⠀⠀
                                ⢠⡿⠀⠰⠟⣻⣧⠀⠀⠸⣿⣿⣿⣿⠃⠀⠀⣿⠛⠿⢷⣤⣄⡀⠀⠀⠀⠀⢹⡟⠁⠀⠀⠀⣤⣄⣀⡀⣀⣠⣤⣶⣶⣶⠈⢻⣆⠀⠀⠀
                                ⣼⡇⠀⠀⣼⠟⣿⠀⠀⠀⣿⣿⣿⣿⠀⠀⣀⣹⣧⣀⣀⠈⠙⠻⠷⣦⣤⣀⣼⠇⠀⠀⠀⢀⣼⡟⠛⠛⠛⠋⠉⠀⠹⣷⡀⣸⡟⠀⠀⠀
                                ⢿⡇⠀⠀⠉⠀⢻⣇⣠⣴⠿⠟⠛⠉⠀⠈⠉⠀⠀⠉⠉⠙⠛⠶⣤⣤⡿⢟⡁⠀⠀⠀⠀⣾⣿⣿⡀⠀⠀⠀⠀⠀⠀⢻⣿⠟⠁⠀⠀⠀
                                ⢸⣇⠀⠀⢀⣤⡾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣼⠛⢛⡷⠶⠾⠟⢿⣏⠙⠻⠷⢦⣤⣀⣀⠀⣸⣿⣷⣶⣤⡀⠀
                                ⠈⢿⣦⣴⡟⠉⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠙⠇⠙⠻⣦⡀⠀⠈⡻⠿⣶⣤⣄⣈⠉⠛⣿⡿⠃⠀⠀⠙⢿⣄
                                ⠀⠀⢸⡟⢀⠀⠀⠀⠀⣠⡶⠟⠋⠁⢹⡿⣧⠀⠀⠀⠉⠙⠻⢶⣄⡀⠀⠀⠀⠀⠙⣷⡶⠟⠛⠻⢦⣿⠟⠛⠻⢿⣿⣡⡴⠿⡿⠂⠈⣿
                                ⠀⠀⣿⡿⠋⠀⢀⣴⣿⠉⠀⠀⠀⠀⢸⡇⠹⣧⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⠿⠁⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⢸
                                ⢀⣾⠏⠀⢀⣴⣿⠏⣿⠀⠀⠀⠀⠀⣾⠁⠀⢻⣆⠀⠀⠀⠀⠀⠀⣰⣿⡟⠶⣤⣤⣤⣤⣴⠶⠶⠶⠶⣤⣄⡀⠀⠀⠀⠀⢻⣆⠀⠀⣼
                                ⣸⡏⠀⢠⡟⢸⡟⠀⢿⡄⠀⠀⠀⢰⡏⠀⠀⠀⣿⡄⠀⠀⠀⠀⢠⡟⠁⣿⠀⠀⠀⠀⣸⣿⡆⠀⠀⠀⠀⢹⣿⣦⠀⠀⠀⠀⢿⣤⣼⠟
                                ⣿⡇⠀⣿⠀⣼⡇⠀⠸⣧⠀⠀⠀⣾⠃⠀⠀⠀⠸⣧⠀⠀⠀⣰⡟⠀⠀⢹⡆⠀⠀⢰⡟⠹⡇⠀⠀⠀⢀⣿⣿⠈⢧⡀⠀⠀⣸⡟⠁⠀
                                ⣿⡇⠀⢻⣄⣿⡇⠀⠀⢻⣆⠀⣼⡏⠀⠀⠀⠀⠀⢿⡀⢠⣾⠏⠀⠀⠀⢸⡇⠀⣰⡟⠀⠀⣷⠀⠀⢀⣾⠃⢸⡆⠈⣷⠀⢸⣿⡇⠀⠀
                                ⢹⣧⠀⠀⠛⠿⣧⣀⡀⠀⣻⣾⣟⡀⠀⠀⠀⠀⢀⣸⣷⡟⠁⠀⠀⠀⠀⢈⣷⣴⠟⠀⠀⠀⣿⠀⢠⡾⠃⠀⢸⡇⠀⠸⣇⠀⣿⡇⠀⠀
                                ⠈⠻⣷⣄⣀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠾⠿⣧⣤⣀⠀⠀⣿⣴⠟⠀⠀⠀⢸⡇⠀⢀⣿⠀⠸⡇⠀⠀
                                ⠀⠀⠈⠙⠻⠿⣿⣿⡿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⣧⣀⠀⠀⠀⢸⣇⣴⡿⣿⠀⠀⣿⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣤⣿⡿⠋⢠⡿⠀⢸⡏⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣄⠈⠛⠷⠶⠛⠁⣠⣿⠃⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣿⣶⣶⣶⣶⡾⠟⠁⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⠶⣶⣦⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠿⠿⣷⣶⣶⣶⠾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                                              
'''

# Pool di curiosità sulle scimmie
monkey_curiosities = [
    "Le scimmie sono intelligenti e possono imparare a utilizzare strumenti.",
    "Ci sono oltre 260 specie di scimmie nel mondo.",
    "Le scimmie sono molto sociali e vivono in gruppi chiamati bande.",
    "Le scimmie sono onnivore e si nutrono di frutta, foglie, insetti e altro.",
    "Le scimmie comunicano utilizzando suoni, gesti e espressioni facciali.",
    "Alcune specie di scimmie sono in pericolo a causa della distruzione del loro habitat.",
    "Le scimmie hanno una visione binoculare che consente loro di vedere in 3D.",
    "Le scimmie possono avere una vita media di 20-40 anni.",
    "Le scimmie sono molto agili e si arrampicano sugli alberi con facilità.",
    "Le scimmie hanno pollici opponibili che consentono loro di afferrare oggetti.",
    "Le scimmie sono state oggetto di studi scientifici per decenni.",
    "Le scimmie sono simili agli esseri umani dal punto di vista genetico.",
    "Alcune specie di scimmie possono vivere fino a 50 anni in cattività.",
    "Le scimmie sono spesso usate come soggetti di ricerca nel campo della medicina.",
    "Le scimmie hanno un olfatto molto sviluppato e possono individuare cibo a distanza.",
    "Alcune scimmie sono in grado di nuotare e si adattano bene all'ambiente acquatico.",
    "Le scimmie sono animali molto giocosi e si divertono ad interagire con oggetti.",
    "Le scimmie sono in grado di imparare e riprodurre semplici sequenze di suoni.",
    "Alcune specie di scimmie sono in grado di utilizzare utensili rudimentali.",
    "Le scimmie sono animali molto territoriali e difendono il proprio territorio dagli intrusi.",
    "Le scimmie hanno un'ottima memoria visiva e possono ricordare volti per molto tempo.",
    "Le scimmie hanno una dieta varia e si adattano all'alimentazione disponibile.",
    "Le scimmie possono sviluppare legami sociali forti all'interno del proprio gruppo.",
    "Le scimmie sono in grado di riconoscere se stesse allo specchio, un segno di autoconsapevolezza.",
    "Alcune specie di scimmie hanno abitudini notturne e sono attive durante le ore buie.",
    "Le scimmie sono in grado di comunicare concetti di base attraverso segnali e gesti.",
    "Le scimmie hanno un sistema gerarchico all'interno del gruppo, con un capo dominante.",
    "Le scimmie sono animali molto agili e possono saltare tra gli alberi con facilità.",
    "Alcune specie di scimmie sono in grado di planare utilizzando una membrana tra le zampe.",
    "Le scimmie possono sviluppare forti legami familiari e si prendono cura dei cuccioli.",
    "Le scimmie hanno una capacità uditiva molto sviluppata e possono percepire suoni a distanza.",
    "Alcune scimmie sono in grado di distinguere colori e preferiscono certe tonalità.",
    "Le scimmie hanno una gestazione che varia da specie a specie, ma di solito dura diversi mesi.",
    "Le scimmie hanno una buona capacità tattile e utilizzano le mani per esplorare l'ambiente.",
    "Alcune specie di scimmie sono in grado di imparare segnali del linguaggio dei segni.",
    "Le scimmie hanno una vista periferica molto ampia e possono individuare movimenti veloci.",
    "Le scimmie sono animali molto territoriali e segnano il loro territorio con urina e feci.",
    "Alcune specie di scimmie sono in grado di utilizzare strumenti per aprire frutti e noci.",
    "Le scimmie possono vivere in diversi tipi di habitat, dalle foreste alle savane.",
    "Le scimmie possono emettere una vasta gamma di suoni, tra cui grida, urla e versi.",
    "Alcune scimmie sono state addestrate per compiere compiti e assistere le persone con disabilità.",
    "Le scimmie sono molto adattabili e possono sopravvivere in diverse condizioni ambientali.",
    "Le scimmie hanno una gestione sociale complessa e possono risolvere conflitti all'interno del gruppo.",
    "Alcune specie di scimmie hanno una coda prensile che possono utilizzare per arrampicarsi.",
    "Le scimmie hanno una capacità di apprendimento rapida e possono adattarsi a nuove situazioni.",
    "Le scimmie sono state oggetto di venerazione in alcune culture e sono presenti in miti e leggende.",
    "Alcune scimmie sono in grado di imparare a comunicare con gli esseri umani attraverso il linguaggio dei segni.",
    "Le scimmie hanno un metabolismo veloce e richiedono una dieta ricca di nutrienti.",
    "Le scimmie hanno un'ottima coordinazione occhio-mano e possono compiere movimenti precisi.",
    "Alcune specie di scimmie sono in grado di utilizzare strumenti complessi per ottenere cibo.",
    "Le scimmie hanno un comportamento giocoso e trascorrono tempo a interagire tra di loro.",
    "Le scimmie sono state studiate come modelli per comprendere l'evoluzione umana.",
    "Alcune scimmie sono in grado di padroneggiare compiti complessi come il riconoscimento di schemi.",
    "Le scimmie sono animali molto agili e possono spostarsi rapidamente tra gli alberi.",
    "Le scimmie hanno un sistema di comunicazione vocale complesso e possono emettere una varietà di suoni.",
    "Alcune specie di scimmie sono in grado di utilizzare utensili avanzati per svolgere compiti specifici."
]

def generate_random_text():
    random_curiosity = random.choice(monkey_curiosities)
    return random_curiosity

def send_traffic(ip_address, ports):
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                curiosity = generate_random_text()
                sock.sendall(curiosity.encode())
                sock.close()
                print(f"Curiosità mandata a {ip_address}:{port}")
            else:
                print(f"Impossibile stabilire una connessione a {ip_address}:{port}")
    except socket.error as e:
        print(f"Errore: {e}")

def main():
    print(logo)
    print("Benvenuto in Monke-Jammer!")
    cidr = input("Inserisci il CIDR di gara (es. 10.60.0.0/16): ")
    service_ports = input("Inserisci le porte dei servizi separate da virgola: ")
    service_ports = [int(port) for port in service_ports.split(",")]
    numero_quadre = input("Inserisci il numero di squadre partecipanti: ")

    # Ottiene i primi due ottetti dell'indirizzo di rete
    network_address, subnet_mask = cidr.split('/')
    network_address = network_address.strip()
    subnet_mask = int(subnet_mask.strip())
    network_prefix = ".".join(network_address.split(".")[:2])

    tempo_stimato = len(service_ports)*int(numero_quadre)
    print(f"Con i dati inseriti è stimato un tempo di {tempo_stimato} secondi ({tempo_stimato//60}:{tempo_stimato%60} minuti) per completare un giro. \nLancia il Monke-Jammer da più PC in caso non rimanessi sotto il tempo di round.")
    scelta = input("Desideri proseguire? (si/no): ")
    if scelta.lower() == "si":
        print("Libero le scimmie...")
    else:
        print("Chiusura di Monke-Jammer.")
        sys.exit()


    while True:
        # Cicla sui terzi ottetti da 1 a numero_quadre
        for i in range(1, int(numero_quadre)):
            # Costruisce l'indirizzo IP con i primi due ottetti fissi e il terzo ottetto variabile
            ip_address = f"{network_prefix}.{i}.1"
            send_traffic(ip_address, service_ports)

if __name__ == '__main__':
    main()