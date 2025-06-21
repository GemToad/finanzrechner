import tkinter as tk
from rechner import Rechner
from tkinter import ttk

rechner = Rechner()

class FinanzRechnerGUI():

    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        self.root.title("Finanzrechner")

        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=1, pady=10, sticky="n")

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")

        self.income_label = tk.Label(self.middle_frame, text="Einnahmen", font=("Arial", 14, "bold"))
        self.income_label.grid(row=0, column=0)
        self.income_tree = ttk.Treeview(self.middle_frame, columns=("Bezeichnung", "Betrag", "Datum"), show="headings")
        self.income_tree.heading("Bezeichnung", text="Bezeichnung")
        self.income_tree.heading("Betrag", text="Betrag (€)")
        self.income_tree.heading("Datum", text="Datum")
        self.income_tree.grid(row=1, column=0)


        self.expense_label = tk.Label(self.middle_frame, text="Ausgaben", font=("Arial", 14, "bold"))
        self.expense_label.grid(row=2, column=0)
        self.expense_tree = ttk.Treeview(self.middle_frame, columns=("Betrag", "Bezeichnung", "Datum"), show="headings")
        self.expense_tree.heading("Betrag", text="Betrag (€)")
        self.expense_tree.heading("Bezeichnung", text="Bezeichnung")
        self.expense_tree.heading("Datum", text="Datum")
        self.expense_tree.grid(row=3, column=0)

        self.kontostand_label = tk.Label(self.right_frame, text=f"Kontostand: {rechner.berechne_kontostand()} €")
        self.kontostand_label.grid(row=0, column=0)

        self.einnahme_betrag_label = tk.Label(self.left_frame, text="Einnahme Betrag (€):")
        self.einnahme_betrag_label.grid(row=0, column=0)
        self.einnahme_betrag_entry = tk.Entry(self.left_frame)
        self.einnahme_betrag_entry.grid(row=0, column=1)

        self.einnahme_bezeichnung_label = tk.Label(self.left_frame, text="Bezeichnung:")
        self.einnahme_bezeichnung_label.grid(row=1, column=0)
        self.einnahme_bezeichnung_entry = tk.Entry(self.left_frame)
        self.einnahme_bezeichnung_entry.grid(row=1, column=1)

        self.einnahme_datum_label = tk.Label(self.left_frame, text="Datum (DD.MM.YYYY):")
        self.einnahme_datum_label.grid(row=2, column=0)
        self.einnahme_datum_entry = tk.Entry(self.left_frame)
        self.einnahme_datum_entry.grid(row=2, column=1)

        self.einnahme_button = tk.Button(self.left_frame, text="Einnahme hinzufügen", command=self.add_income)
        self.einnahme_button.grid(row=3, column=0)

        self.ausgabe_betrag_label = tk.Label(self.left_frame, text="Ausgabe Betrag (€):")
        self.ausgabe_betrag_label.grid(row=4, column=0)
        self.ausgabe_betrag_entry = tk.Entry(self.left_frame)
        self.ausgabe_betrag_entry.grid(row=4, column=1)

        self.ausgabe_bezeichnung_label = tk.Label(self.left_frame, text="Bezeichnung:")
        self.ausgabe_bezeichnung_label.grid(row=5, column=0)
        self.ausgabe_bezeichnung_entry = tk.Entry(self.left_frame)
        self.ausgabe_bezeichnung_entry.grid(row=5, column=1)

        self.ausgabe_datum_label = tk.Label(self.left_frame, text="Datum (DD.MM.YYYY):")
        self.ausgabe_datum_label.grid(row=6, column=0)
        self.ausgabe_datum_entry = tk.Entry(self.left_frame)
        self.ausgabe_datum_entry.grid(row=6, column=1)

        self.ausgabe_button = tk.Button(self.left_frame, text="Ausgabe hinzufügen", command=self.add_expense)
        self.ausgabe_button.grid(row=7, column=0)

        # Schließen-Button
        self.schliessen_button = tk.Button(self.root, text="Schließen", command=self.root.quit)
        self.schliessen_button.grid(row=20, column=3)

        # Starte GUI Loop
        self.root.mainloop()

    def add_income(self):
        betrag = float(self.einnahme_betrag_entry.get())
        bezeichnung = self.einnahme_bezeichnung_entry.get()
        datum = self.einnahme_datum_entry.get()
        rechner.add_einnahme(betrag, bezeichnung, datum)
        self.income_tree.insert("", "end", values=(bezeichnung, betrag, datum))
        self.update_kontostand()
        self.einnahme_betrag_entry.delete(0, tk.END)
        self.einnahme_bezeichnung_entry.delete(0, tk.END)
        self.einnahme_datum_entry.delete(0, tk.END)



    # Ausgaben
    def add_expense(self):
        betrag = float(self.ausgabe_betrag_entry.get())
        bezeichnung = self.ausgabe_bezeichnung_entry.get()
        datum = self.ausgabe_datum_entry.get()
        rechner.add_ausgabe(betrag, bezeichnung, datum)
        self.income_tree.insert("", "end", values=(bezeichnung, betrag, datum))
        self.update_kontostand()
        self.ausgabe_betrag_entry.delete(0, tk.END)
        self.ausgabe_bezeichnung_entry.delete(0, tk.END)
        self.ausgabe_datum_entry.delete(0, tk.END)


    def update_kontostand(self):
        self.kontostand_label.config(text=f"Kontostand: {rechner.berechne_kontostand()}")

if __name__ == "__main__":
    app = FinanzRechnerGUI()