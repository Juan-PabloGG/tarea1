class BaseConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Hola": "¡Hola! ¿Cómo estás?",
            "Como estas?": "Estoy bien, gracias por preguntar.",
            "de que te gustaría hablar?": "Me gusta hablar de muchos temas. ¿Hay algo específico en lo que estés interesado?"
        }

    def obtener_respuesta(self, pregunta):
        return self.conocimiento.get(pregunta, "Lo siento, no entiendo.")

def chat():
    base = BaseConocimiento()
    print("¡Bienvenido al chatbot! Puedes escribir 'Salir' en cualquier momento para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
        print("Bot:", base.obtener_respuesta(entrada))

if __name__ == "__main__":
    chat()