import tkinter as tk
import random

class FlappyBird:
    def __init__(self, master):
        self.master = master
        self.master.title("Flappy Bird (teste)")
        
        # Configurações de tela
        self.largura = 400
        self.altura = 500
        self.canvas = tk.Canvas(master, width=self.largura, height=self.altura, bg="#70c5ce", highlightthickness=0)
        self.canvas.pack()

        # Variáveis de física
        self.gravidade = 1.5
        self.velocidade = 0
        self.jogo_rodando = True
        self.pontos = 0

        # Criar Pássaro (Um quadrado amarelo)
        self.passaro = self.canvas.create_rectangle(50, 250, 80, 280, fill="yellow", outline="black")

        # Lista de canos e placar
        self.canos = []
        self.texto_pontos = self.canvas.create_text(200, 50, text="0", font=("Courier", 30, "bold"), fill="white")

        # Controles
        self.master.bind("<space>", self.pular)
        
        # Iniciar loops
        self.gerar_canos()
        self.atualizar()

    def pular(self, event=None):
        if self.jogo_rodando:
            self.velocidade = -12  # Força do pulo
        else:
            # Reiniciar jogo se bater
            import os
            import sys
            os.execl(sys.executable, sys.executable, *sys.argv)

    def gerar_canos(self):
        if self.jogo_rodando:
            vão = 140
            altura_topo = random.randint(50, 300)
            
            # Cano de cima
            c1 = self.canvas.create_rectangle(self.largura, 0, self.largura + 50, altura_topo, fill="#73bf2e", outline="black")
            # Cano de baixo
            c2 = self.canvas.create_rectangle(self.largura, altura_topo + vão, self.largura + 50, self.altura, fill="#73bf2e", outline="black")
            
            self.canos.append((c1, c2, False)) # O False indica que o ponto ainda não foi contado
            self.master.after(1500, self.gerar_canos)

    def atualizar(self):
        if self.jogo_rodando:
            # Aplicar gravidade
            self.velocidade += self.gravidade
            self.canvas.move(self.passaro, 0, self.velocidade)
            
            pos_passaro = self.canvas.coords(self.passaro)

            # Mover canos e checar colisão
            for i, (c_topo, c_baixo, contado) in enumerate(self.canos):
                self.canvas.move(c_topo, -5, 0)
                self.canvas.move(c_baixo, -5, 0)
                
                pos_topo = self.canvas.coords(c_topo)
                
                # Colisão com canos
                if self.checar_colisao(pos_passaro, pos_topo) or self.checar_colisao(pos_passaro, self.canvas.coords(c_baixo)):
                    self.game_over()

                # Contar pontos
                if pos_topo[2] < pos_passaro[0] and not contado:
                    self.pontos += 1
                    self.canvas.itemconfig(self.texto_pontos, text=str(self.pontos))
                    self.canos[i] = (c_topo, c_baixo, True)

            # Colisão com teto ou chão
            if pos_passaro[1] <= 0 or pos_passaro[3] >= self.altura:
                self.game_over()

            self.master.after(30, self.atualizar)

    def checar_colisao(self, r1, r2):
        # Lógica de intersecção de retângulos
        return not (r1[2] < r2[0] or r1[0] > r2[2] or r1[3] < r2[1] or r1[1] > r2[3])

    def game_over(self):
        self.jogo_rodando = False
        self.canvas.create_text(200, 250, text="GAME OVER\nEspaço para Reiniciar", 
                                font=("Courier", 20, "bold"), fill="red", justify="center")

# Rodar o jogo
root = tk.Tk()
jogo = FlappyBird(root)
root.mainloop()