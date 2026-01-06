# Lembrete por Notificação em Python

Um script simples em **Python** que cria **lembretes com notificações do sistema**, funcionando em **Windows, macOS e Linux**, utilizando a biblioteca `plyer`.

Ideal para estudos, automação pessoal ou como base para projetos maiores.

## Funcionalidades

- Cria lembretes com atraso em segundos  
- Exibe notificação nativa do sistema operacional  
- Compatível com Windows, macOS e Linux  
- Código simples e fácil de adaptar  

## Tecnologias utilizadas

- Python 3.x  
- Biblioteca [`plyer`](https://pypi.org/project/plyer/)

**Licença**

MIT

## Código do projeto

````
import time
from plyer import notification

def lembrete(mensagem, segundos):
    print(f"Lembrete agendado para {segundos} segundos...")
    time.sleep(segundos)

    notification.notify(
        title="🔔 Lembrete",
        message=mensagem,
        timeout=10
    )

if __name__ == "__main__":
    lembrete("Hora de beber água 💧", 10)
`````

**Projeto simples, mais é útil em muitos casos. Ainda da para melhoras ainda mais esse projeto**





