import time 
from plyer import notification 

def lembrete(mensagem, segundos):
    print(f"Lembrete agendado para {segundos} segundos...")
    time.sleep(segundos)

    notification.notify(
        title=" Lembrete",
        message=mensagem,
        timeout=10 
    )

if __name__ == "__main__":
    texto = "Hora de dormir"
    tempo_em_segundos = 10  

    lembrete(texto, tempo_em_segundos)
