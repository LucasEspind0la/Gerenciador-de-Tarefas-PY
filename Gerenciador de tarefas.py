import tkinter as tk
from tkinter import messagebox

# Funções
def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa != "":
        listbox_tarefas.insert(tk.END, tarefa)
        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Você precisa digitar uma tarefa!")

def remover_tarefa():
    try:
        indice_tarefa = listbox_tarefas.curselection()[0]
        listbox_tarefas.delete(indice_tarefa)
    except:
        messagebox.showwarning("Aviso", "Você precisa selecionar uma tarefa para remover!")

def limpar_tarefas():
    listbox_tarefas.delete(0, tk.END)

# Configuração da Janela Principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Entrada de Tarefas
entry_tarefa = tk.Entry(root, width=50)
entry_tarefa.pack(pady=10)

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack()

botao_adicionar = tk.Button(frame_botoes, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT, padx=5)

botao_remover = tk.Button(frame_botoes, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar Tarefas", command=limpar_tarefas)
botao_limpar.pack(side=tk.LEFT, padx=5)

# Lista de Tarefas
listbox_tarefas = tk.Listbox(root, width=50, height=15)
listbox_tarefas.pack(pady=10)

# Inicializar a Janela
root.mainloop()
