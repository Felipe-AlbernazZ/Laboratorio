import tkinter as tk


class EstoqueRoupas:
    def __init__(self, master):
        self.master = master
        self.master.title("Estoque de Roupas Masculinas")
        self.estoque = {tamanho: 0 for tamanho in range(1, 17)}
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para adicionar roupas
        adicionar_frame = tk.Frame(self.master)
        adicionar_frame.pack(pady=10)

        adicionar_label = tk.Label(
            adicionar_frame, text="Adicionar Roupas", font=("Courier", 16))
        adicionar_label.pack(side=tk.LEFT)

        self.adicionar_entry = tk.Entry(adicionar_frame, font=("Courier", 16))
        self.adicionar_entry.pack(side=tk.LEFT, padx=10)

        adicionar_button = tk.Button(adicionar_frame, text="Adicionar", font=(
            "Courier", 16), command=self.adicionar_roupas)
        adicionar_button.pack(side=tk.LEFT)

        # Label e Entry para remover roupas
        remover_frame = tk.Frame(self.master)
        remover_frame.pack(pady=10)

        remover_label = tk.Label(
            remover_frame, text="Remover Roupas", font=("Courier", 16))
        remover_label.pack(side=tk.LEFT)

        self.remover_entry = tk.Entry(remover_frame, font=("Courier", 16))
        self.remover_entry.pack(side=tk.LEFT, padx=10)

        remover_button = tk.Button(remover_frame, text="Remover", font=(
            "Courier", 16), command=self.remover_roupas)
        remover_button.pack(side=tk.LEFT)

        # Botão para visualizar o estoque
        visualizar_button = tk.Button(self.master, text="Visualizar Estoque", font=(
            "Courier", 16), command=self.visualizar_estoque)
        visualizar_button.pack(pady=10)

    def adicionar_roupas(self):
        quantidade = int(self.adicionar_entry.get())
        tamanho = self.get_tamanho_selecionado()

        if tamanho:
            self.estoque[tamanho] += quantidade
            self.adicionar_entry.delete(0, tk.END)

    def remover_roupas(self):
        quantidade = int(self.remover_entry.get())
        tamanho = self.get_tamanho_selecionado()

        if tamanho and self.estoque[tamanho] >= quantidade:
            self.estoque[tamanho] -= quantidade
            self.remover_entry.delete(0, tk.END)

    def get_tamanho_selecionado(self):
        return self.tamanhos_listbox.get(tk.ACTIVE)

    def visualizar_estoque(self):
        visualizar_window = tk.Toplevel(self.master)
        visualizar_window.title("Estoque Atual")

        scrollbar = tk.Scrollbar(visualizar_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(
            visualizar_window, yscrollcommand=scrollbar.set, font=("Courier", 12))

        for tamanho, quantidade in self.estoque.items():
            listbox.insert(tk.END, f"Tamanho {tamanho}: {quantidade}")

        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)


if __name__ == "__main__":
    root = tk.Tk()
    estoque_roupas = EstoqueRoupas(root)
    root.mainloop()
