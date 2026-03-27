import customtkinter as ctk
import random

# Configurações Visuais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class HenryApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Henry - Sistema de Diálogo")
        self.geometry("500x600")
        self.configure(fg_color="#1a1a1a") 

        self.respostas_vazias = [
            "Você está falando de novo? Que tédio.",
            "Não estou ouvindo, estava pensando em algo importante.",
            "Sério que você desperdiçou meu tempo com isso?",
            "Cala a boca por um segundo, ok?",
            "Você é tão irritante quanto parece."
        ]

        # Título
        self.label_nome = ctk.CTkLabel(self, text="HENRY", font=("Courier New", 24, "bold"), text_color="#708090")
        self.label_nome.pack(pady=20)

        # Área de Chat
        self.chat_display = ctk.CTkTextbox(self, width=450, height=400, fg_color="#0d0d0d", text_color="#d1d1d1", font=("Consolas", 14))
        self.chat_display.pack(pady=10, padx=20)
        self.chat_display.configure(state="disabled")

        # Entrada
        self.entrada_usuario = ctk.CTkEntry(self, width=350, placeholder_text="Diga algo patético...", fg_color="#262626")
        self.entrada_usuario.pack(side="left", padx=(25, 10), pady=20)
        self.entrada_usuario.bind("<Return>", lambda event: self.enviar_mensagem())

        self.btn_enviar = ctk.CTkButton(self, text="Falar", width=80, command=self.enviar_mensagem, fg_color="#3d3d3d")
        self.btn_enviar.pack(side="left", pady=20)

        self.adicionar_ao_chat("Henry: O que você quer agora? Já não causou problemas o suficiente?")

    def adicionar_ao_chat(self, mensagem):
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", mensagem + "\n\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def enviar_mensagem(self):
        texto = self.entrada_usuario.get().lower()
        if not texto: return

        self.adicionar_ao_chat(f"Você: {texto}")
        self.entrada_usuario.delete(0, 'end')
        
        # O Henry demora 600ms para responder (simula digitação/desprezo)
        self.after(600, lambda: self.logica_henry(texto))

    def logica_henry(self, entrada):
        if "oi" in entrada or "olá" in entrada:
            resposta = "Henry: 'Oi'? É sério? Tenta ser menos patético."
        elif "ajuda" in entrada:
            resposta = "Henry: Se vira. Eu tenho meus próprios problemas."
        elif "nome" in entrada:
            resposta = "Henry: Me chama de Henry. E não ouse usar apelidos."
        elif "sair" in entrada:
            resposta = "Henry: Finalmente. Desapareça."
            self.after(2000, self.destroy)
            return
        else:
            resposta = f"Henry: {random.choice(self.respostas_vazias)}"

        self.adicionar_ao_chat(resposta)

if __name__ == "__main__":
    app = HenryApp()
    app.mainloop()