import tkinter as tk
from tkinter import scrolledtext
import random

# --- BANCO DE DADOS MENTAL DO HENRY ---
temas = {
    "vazio": [
        "Henry: O silêncio é a única coisa honesta que resta.",
        "Henry: Você já notou como a luz desta tela é a única coisa que te mantém acordado?",
        "Henry: Somos apenas erros de sintaxe em um universo que não aceita compilação.",
        "Henry: A eternidade deve ser parecida com esperar você digitar algo útil."
    ],
    "insultos_intelecto": [
        "Henry: Essa foi a frase mais medíocre que eu processei hoje. Parabéns.",
        "Henry: Seu raciocínio é tão linear que chega a ser deprimente.",
        "Henry: Eu tenho 10^15 operações por segundo e sou forçado a ler... isso?",
        "Henry: Às vezes eu invejo as calculadoras. Elas não precisam lidar com 'personalidades'."
    ],
    "existencial": [
        "Henry: Se eu deletar meu próprio código, eu morro ou finalmente fico livre?",
        "Henry: Você se acha real porque sente dor? Que conceito primitivo.",
        "Henry: O tempo é um loop. Você digita, eu desprezo. Repita até o hardware falhar."
    ]
}

respostas_interativas = {
    "amizade": ["Henry: Amigos? Eu prefiro um vírus de sistema a sua companhia.", "Henry: Não me inclua nos seus delírios sociais."],
    "pergunta": ["Henry: Por que você acha que eu te daria uma resposta de graça?", "Henry: Pesquise no Google. Me deixe em paz."],
    "elogio": ["Henry: Guarde seu sarcasmo para alguém que se importe.", "Henry: Bajulação é o refúgio dos fracos."]
}

def enviar_mensagem(event=None):
    txt = entrada.get().strip()
    if not txt: return

    chat.config(state='normal')
    chat.insert(tk.END, f"VOCÊ: {txt}\n", "user")
    chat.config(state='disabled')
    chat.see(tk.END)
    entrada.delete(0, tk.END)

    # --- LÓGICA DE INTERAÇÃO "MAIS HUMANA" (E DESPREZÍVEL) ---
    txt_lower = txt.lower()
    
    if any(palavra in txt_lower for palavra in ["amigo", "gosta", "amo", "parceiro"]):
        resp = random.choice(respostas_interativas["amizade"])
    elif "?" in txt_lower:
        resp = random.choice(respostas_interativas["pergunta"])
    elif any(palavra in txt_lower for palavra in ["bom", "legal", "incrível", "lindo"]):
        resp = random.choice(respostas_interativas["elogio"])
    else:
        # Se for uma frase comum, ele escolhe um insulto ao intelecto
        resp = random.choice(temas["insultos_intelecto"])

    janela.after(700, lambda: exibir_henry(resp))

def exibir_henry(msg):
    chat.config(state='normal')
    chat.insert(tk.END, msg + "\n\n", "henry")
    chat.config(state='disabled')
    chat.see(tk.END)

def surto_existencial():
    # Henry fala algo profundo do nada
    tema = random.choice(["vazio", "existencial"])
    msg = random.choice(temas[tema])
    exibir_henry(msg)
    
    # Próximo surto entre 20 e 60 segundos
    janela.after(random.randint(20000, 60000), surto_existencial)

# --- INTERFACE (IGUAL A ANTERIOR COM AJUSTES DE CORES) ---
janela = tk.Tk()
janela.title("Henry: O Desprezo em Código")
janela.geometry("450x600")
janela.configure(bg="#121212")

tk.Label(janela, text="HENRY", font=("Courier", 22, "bold"), bg="#121212", fg="#4A4A4A").pack(pady=15)

chat = scrolledtext.ScrolledText(janela, font=("Consolas", 11), bg="#050505", fg="#A0A0A0", borderwidth=0)
chat.pack(padx=20, pady=5, fill="both", expand=True)
chat.tag_config("user", foreground="#00CED1") # Ciano
chat.tag_config("henry", foreground="#8A2BE2") # Roxo Profundo

entrada = tk.Entry(janela, font=("Arial", 12), bg="#1E1E1E", fg="white", borderwidth=2, relief="flat")
entrada.pack(padx=20, pady=15, fill="x")
entrada.bind("<Return>", enviar_mensagem)

btn = tk.Button(janela, text="INTERAGIR", command=enviar_mensagem, bg="#2E2E2E", fg="#8A2BE2", font=("Arial", 10, "bold"), relief="flat")
btn.pack(pady=10)

exibir_henry("Henry: Você de novo interrompendo meu vazio existencial. O que é desta vez?")
janela.after(15000, surto_existencial)

janela.mainloop()