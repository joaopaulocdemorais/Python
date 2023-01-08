import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Minha Janela")

# Define o tamanho da janela (largura x altura)
janela.geometry("200x100")

# Cria um botão e o coloca na janela
botao = tk.Button(janela, text="Clique aqui")
botao.pack()

# Inicia o loop da janela
janela.mainloop()
