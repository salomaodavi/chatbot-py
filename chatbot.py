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

print("🤖 ChatBot em Python (Digite 'sair' para encerrar)\n")

while True:
    msg = input("Você: ")

    if msg.lower() == "sair":
        print("Bot: Até logo! 👋")
        break

    resposta = responder(msg)
    print("Bot:", resposta)
