# 🤖 Chatbot Simples em Python (sem frameworks)

Este é um **chatbot de terminal feito 100% em Python puro**, sem uso de frameworks. Ideal para praticar lógica de programação, condicionais, tratamento de texto e entrada/saída com o usuário.

---

## 📌 Objetivo

- Mostrar domínio básico da linguagem Python
- Usar lógica de decisão (`if`, `elif`, `else`)
- Simular uma conversa interativa no terminal
- Projeto leve e fácil para iniciantes

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/chatbot-python-simples.git
cd chatbot-python-simples
````

### 2. Execute o código
````
python chatbot.py
````

💡 Certifique-se de ter o Python instalado (3.6 ou superior).

# 💬 Como conversar com o chatbot

Ao iniciar, o terminal exibirá uma mensagem de boas-vindas. Você pode digitar mensagens como:
````
Você: oi
Bot: Olá! Tudo bem com você?

Você: qual seu nome?
Bot: Eu sou um chatbot simples feito em Python!

Você: sair
Bot: Até logo! 👋
````

Digite sair a qualquer momento para encerrar a conversa.

# 🧠 Lógica usada no bot

O chatbot faz comparações básicas com if/elif para responder com base em palavras-chave. Tudo está contido em uma única função:
````
def responder(mensagem):
    mensagem = mensagem.lower()

    if "oi" in mensagem or "olá" in mensagem:
        return "Olá! Tudo bem com você?"
    elif "tudo" in mensagem or "bem" in mensagem:
        return "Que bom! Como posso te ajudar hoje?"
    elif "nome" in mensagem:
        return "Eu sou um chatbot simples feito em Python!"
    elif "obrigado" in mensagem or "valeu" in mensagem:
        return "De nada! 😊"
    elif "sair" in mensagem:
        return "Até logo!"
    else:
        return "Desculpe, não entendi. Pode repetir?"
````

### 💼 Ideal para

✅ Quem está começando na programação

✅ Portfólio simples e didático

✅ Mostrar domínio de lógica e Python básico

# ✨ Autor

## Salomão Davi Cardoso Barros

### Desenvolvedor júnior com foco em projetos práticos e APIs.

LinkedIn: www.linkedin.com/in/salomao-davi


  








