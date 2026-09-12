import tkinter as tk
from tkinter import messagebox
import document

def adicionar_atendente():
    nome = entrada_nome.get().strip()

    if not nome:
        messagebox.showwarning("Nome vazio", "Digite um nome!")
        return

    if nome in [a["nome"] for a in document.atendentes]:
        messagebox.showwarning("Nome vazio", "Digite um nome!")
        return

    document.adicionar_atendente(nome)
    entrada_nome.delete(0, tk.END)
    atualizar_interface()


def resetar_atendentes():
    if messagebox.askyesno(
        "Resetar",
        "Tem certeza que deseja resetar todos os dados?"
    ):
        document.atendentes.clear()
        atualizar_interface()


def incrementar_vendas(indice):
    document.incrementar_vendas(indice)
    atualizar_interface()


def atualizar_interface():
    for widget in quadro_atendentes.winfo_children():
        widget.destroy()

    for i, atendente in enumerate(document.atendentes):
        texto = f"{atendente['nome']}: {atendente['vendas']} vendas"
        rotulo = tk.Label(quadro_atendentes, text=texto)
        rotulo.grid(row=i, column=0, sticky="w")

        botao = tk.Button(
            quadro_atendentes,
            text="+1 Venda",
            command=lambda indice=i: incrementar_vendas(indice)
        )
        botao.grid(row=i, column=1, padx=5)


# Interface principal
janela = tk.Tk()
janela.title("cantrole de vendas - Smat View")

entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)

botao_adicionar = tk.Button(
    janela,
    text="Adicionar Atendente",
    command=adicionar_atendente
)
botao_adicionar.pack(pady=5)

botao_resetar = tk.Button(
    janela,
    text="Resetar",
    command=resetar_atendentes
)
botao_resetar.pack(pady=5)

quadro_atendentes = tk.Frame(janela)
quadro_atendentes.pack(pady=5)

atualizar_interface()

janela.mainloop()