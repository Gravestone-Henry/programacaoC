import tkinter as tk
from tkinter import messagebox

def clicar_botao(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(valor))

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END) 
        entrada.insert(0, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não pode dividir por zero, mosh!")
    except Exception:
        messagebox.showerror("Erro", "Expressão inválida!")

janela = tk.Tk()
janela.title("Calculadora Henry´s v1.0 💀")
janela.geometry("300x450")
janela.configure(bg="#1a1a1a")  

entrada = tk.Entry(janela, font=("Courier New", 24, "bold"), bg="#2d2d2d", fg="#ff00ff", 
                  borderwidth=5, relief="flat", justify="right")
entrada.pack(pady=20, padx=10, fill="x")

frame_botoes = tk.Frame(janela, bg="#1a1a1a")
frame_botoes.pack()

estilo_num = {"font": ("Arial", 14, "bold"), "bg": "#4b0082", "fg": "white", "width": 5, "height": 2, "relief": "flat"}
estilo_op = {"font": ("Arial", 14, "bold"), "bg": "#ff00ff", "fg": "black", "width": 5, "height": 2, "relief": "flat"}
estilo_igual = {"font": ("Arial", 14, "bold"), "bg": "#00ffff", "fg": "black", "width": 11, "height": 2, "relief": "flat"}

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
]

for (texto, linha, col) in botoes:
    estilo = estilo_op if texto in ['/', '*', '-', '+', 'C'] else estilo_num
    if texto == 'C':
        action = limpar
    else:
        action = lambda x=texto: clicar_botao(x)
    
    tk.Button(frame_botoes, text=texto, command=action, **estilo).grid(row=linha, column=col, padx=2, pady=2)

tk.Button(janela, text="=", command=calcular, **estilo_igual).pack(pady=10)

tk.Label(janela, text="I’m not waiting for death; I’m feasting upon my own ruin with a grin.", bg="#1a1a1a", fg="#666", font=("Arial", 8, "italic")).pack()

janela.mainloop()
