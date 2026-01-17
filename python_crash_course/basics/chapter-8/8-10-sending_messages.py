def show_messages(ceci_messages, sent_messages):
    """Imprimimos cada mensaje en mayúsculas y lo movemos de lista"""
    while ceci_messages:
        message_printed = ceci_messages.pop()
        print(f"Y Ceci un día mas dijo: {message_printed.upper()}")
        sent_messages.append(message_printed)

ceci_messages = ["tu no me entiendes", "hoy me siento rara", "hoy no me diste un beso"]
sent_messages = []

show_messages(ceci_messages, sent_messages)

for message_sent in sent_messages:
    print(f"El siguiente mensaje fue mostrado: {message_sent.upper()}")