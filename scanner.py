import socket
from datetime import datetime

def iniciar_scanner():
    print("-" * 50)
    print("🛡️ PYTHON PORT SCANNER v1.0")
    print("-" * 50)

    # Agora o usuário escolhe o alvo
    alvo = input("Digite o IP ou Hostname para escanear (ex: 127.0.0.1): ")
    
    try:
        # Resolve o nome do host caso o usuário digite algo como 'google.com'
        alvo_ip = socket.gethostbyname(alvo)
    except socket.gaierror:
        print("\n❌ Erro: Nome do host não pôde ser resolvido.")
        return

    print(f"\nEscaneando alvo: {alvo_ip}")
    print(f"Iniciado em: {datetime.now()}")
    print("-" * 50)

    try:
        # Vamos escanear de 1 a 100 por padrão para ser rápido
        # Mas você pode aumentar esse range se quiser
        for porta in range(1, 101):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.05) # Ainda mais rápido!
            
            resultado = s.connect_ex((alvo_ip, porta))
            
            if resultado == 0:
                print(f"Porta {porta} [ABERTA] 🔓")
            
            s.close()

    except KeyboardInterrupt:
        print("\n⚠️ Scan interrompido pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    
    print("-" * 50)
    print("✅ Scan concluído!")

if __name__ == "__main__":
    iniciar_scanner()