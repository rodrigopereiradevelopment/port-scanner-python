# 🔍 Python Port Scanner

Um scanner de portas TCP simples e eficiente desenvolvido em Python. Esta ferramenta foi criada para realizar auditorias de rede e identificar serviços ativos em dispositivos locais ou remotos.

## 🛡️ O que este projeto demonstra
- **Conhecimento de Redes**: Uso de Sockets para comunicação TCP/IP.
- **Segurança Ofensiva/Defensiva**: Capacidade de identificar portas abertas e protocolos (como HTTP, FTP, SSH).
- **Tratamento de Erros**: Gestão de exceções para IPs inválidos e interrupções de usuário.

## 🚀 Como Funciona
O script tenta realizar um "aperto de mão" (TCP Handshake) em um intervalo de portas definido. Se a conexão for bem-sucedida, a porta é marcada como **ABERTA**.

## 🔧 Como Usar

**1. Clone o repositório:**

   bash
   
   git clone [https://github.com/rodrigopereiradevelopment/port-scanner-python.git](https://github.com/rodrigopereiradevelopment/port-scanner-python.git)

**2. Execute o script:**

Bash

python3 scanner.py

**3. Digite o IP do alvo:**

(Exemplo: seu roteador ou localhost).

⚠️ **Aviso Legal**

Este projeto foi desenvolvido para fins estritamente educacionais e de auditoria em redes próprias.

## ⚖️ Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
