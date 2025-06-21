import tkinter as tk
from rechner import Rechner
from tkinter import ttk

rechner = Rechner()

class FinanzRechnerGUI():

    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Finanzrechner")

        self.income_label = tk.Label(self.root, text="Einnahmen", font=("Arial", 14, "bold"))
        self.income_label.pack()
        self.income_tree = ttk.Treeview(self.root, columns=("Betrag","Bezeichnung","Datum"), show="headings")
        self.income_tree.heading("Betrag", text="Betrag (€)")
        self.income_tree.heading("Bezeichnung", text="Bezeichnung")
        self.income_tree.heading("Datum", text="Datum")
        self.income_tree.pack()

        self.expense_label = tk.Label(self.root, text="Ausgaben", font=("Arial", 14, "bold"))
        self.expense_label.pack()
        self.expense_tree = ttk.Treeview(self.root, columns=("Betrag", "Bezeichnung", "Datum"), show="headings")
        self.expense_tree.heading("Betrag", text="Betrag (€)")
        self.expense_tree.heading("Bezeichnung", text="Bezeichnung")
        self.expense_tree.heading("Datum", text="Datum")
        self.expense_tree.pack()

        self.kontostand_label = tk.Label(self.root, text=f"Kontostand: {rechner.berechne_kontostand()} €")
        self.kontostand_label.pack()
        self.einnahme_betrag_label = tk.Label(self.root, text="Einnahme Betrag (€):")
        self.einnahme_betrag_label.pack()
        self.einnahme_betrag_entry = tk.Entry(self.root)
        self.einnahme_betrag_entry.pack()

        self.einnahme_bezeichnung_label = tk.Label(self.root, text="Bezeichnung:")
        self.einnahme_bezeichnung_label.pack()
        self.einnahme_bezeichnung_entry = tk.Entry(self.root)
        self.einnahme_bezeichnung_entry.pack()

        self.einnahme_datum_label = tk.Label(self.root, text="Datum (DD.MM.YYYY):")
        self.einnahme_datum_label.pack()
        self.einnahme_datum_entry = tk.Entry(self.root)
        self.einnahme_datum_entry.pack()

        einnahme_button = tk.Button(self.root, text="Einnahme hinzufügen", command=self.add_income)
        einnahme_button.pack()

        self.ausgabe_betrag_label = tk.Label(self.root, text="Ausgabe Betrag (€):")
        self.ausgabe_betrag_label.pack()
        self.ausgabe_betrag_entry = tk.Entry(self.root)
        self.ausgabe_betrag_entry.pack()

        self.ausgabe_bezeichnung_label = tk.Label(self.root, text="Bezeichnung:")
        self.ausgabe_bezeichnung_label.pack()
        self.ausgabe_bezeichnung_entry = tk.Entry(self.root)
        self.ausgabe_bezeichnung_entry.pack()

        self.ausgabe_datum_label = tk.Label(self.root, text="Datum (DD.MM.YYYY):")
        self.ausgabe_datum_label.pack()
        self.ausgabe_datum_entry = tk.Entry(self.root)
        self.ausgabe_datum_entry.pack()

        ausgabe_button = tk.Button(self.root, text="Ausgabe hinzufügen", command=self.add_expense)
        ausgabe_button.pack()

        # Schließen-Button
        schliessen_button = tk.Button(self.root, text="Schließen", command=self.root.quit)
        schliessen_button.pack()

        # Starte GUI Loop
        self.root.mainloop()

    def add_income(self):
        betrag = float(self.einnahme_betrag_entry.get())
        bezeichnung = self.einnahme_bezeichnung_entry.get()
        datum = self.einnahme_datum_entry.get()
        rechner.add_einnahme(betrag, bezeichnung, datum)
        self.income_tree.insert("", "end", values=(betrag, bezeichnung, datum))
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
        self.income_tree.insert("", "end", values=(betrag, bezeichnung, datum))
        self.update_kontostand()
        self.ausgabe_betrag_entry.delete(0, tk.END)
        self.ausgabe_bezeichnung_entry.delete(0, tk.END)
        self.ausgabe_datum_entry.delete(0, tk.END)


    def update_kontostand(self):
        self.kontostand_label.config(text=f"Kontostand: {rechner.berechne_kontostand()}")

if __name__ == "__main__":
    app = FinanzRechnerGUI()