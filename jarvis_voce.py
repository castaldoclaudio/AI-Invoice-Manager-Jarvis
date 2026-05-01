import os
import csv
import PyPDF2
import pyttsx3
from cryptography.fernet import Fernet

# --- CONFIGURAZIONE SICUREZZA ---
def inizializza_sicurezza():
    if not os.path.exists("segreta.key"):
        chiave = Fernet.generate_key()
        with open("segreta.key", "wb") as key_file:
            key_file.write(chiave)
    with open("segreta.key", "rb") as key_file:
        chiave = key_file.read()
    return Fernet(chiave)

fernet = inizializza_sicurezza()

# --- CONFIGURAZIONE VOCE ---
engine = pyttsx3.init()
def parla(testo):
    print(f"Jarvis: {testo}")
    engine.say(testo)
    engine.runAndWait()

# --- FUNZIONE SALVATAGGIO SUL DESKTOP ---
def salva_dato_sicuro(data, fornitore, importo):
    # Criptiamo l'importo
    importo_criptato = fernet.encrypt(str(importo).encode()).decode()
    
    # Percorso dinamico per il tuo Desktop
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    percorso_csv = os.path.join(desktop, 'family_manager_database.csv')
    
    with open(percorso_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, fornitore, importo_criptato])
    
    parla(f"Dato di {fornitore} salvato e criptato con successo sul Desktop.")

# --- AVVIO TEST ---
if __name__ == "__main__":
    parla("Inizializzazione sistema Jarvis completata.")
    # Testiamo il salvataggio
    salva_dato_sicuro("2024-05-01", "TEST_AZIENDA", "100.00")