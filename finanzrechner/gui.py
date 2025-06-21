import tkinter as tk
from tkinter import ttk
from rechner import Rechner
from tkinter import messagebox
from datetime import datetime


rechner = Rechner()

class FinanzRechnerGUI:
    root: tk.Tk

    left_frame: tk.Frame
    middle_frame: tk.Frame
    right_frame: tk.Frame

    income_label: tk.Label
    income_tree: ttk.Treeview
    expense_label: tk.Label
    expense_tree: ttk.Treeview

    einnahme_betrag_label: tk.Label
    einnahme_betrag_entry: tk.Entry
    einnahme_bezeichnung_label: tk.Label
    einnahme_bezeichnung_entry: tk.Entry
    einnahme_datum_label: tk.Label
    einnahme_datum_entry: tk.Entry

    ausgabe_betrag_label: tk.Label
    ausgabe_betrag_entry: tk.Entry
    ausgabe_bezeichnung_label: tk.Label
    ausgabe_bezeichnung_entry: tk.Entry
    ausgabe_datum_label: tk.Label
    ausgabe_datum_entry: tk.Entry

    einnahme_button: tk.Button
    ausgabe_button: tk.Button
    schliessen_button: tk.Button
    einnahme_loeschen_button: tk.Button
    einnahme_bearbeiten_button: tk.Button
    ausgabe_loeschen_button: tk.Button
    ausgabe_bearbeiten_button: tk.Button


    kontostand_label: tk.Label
    income_total_label: tk.Label
    expense_total_label: tk.Label

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Finanzrechner")

        self.create_frames()
        self.create_income_section()
        self.create_expense_section()

        rechner.load_data()

        for t in rechner.transactions:
            if t["type"] == "einkommen":
                self.income_tree.insert("", "end", values=(t["date"], t["bezeichnung"], t["betrag"]))
            elif t["type"] == "ausgabe":
                self.expense_tree.insert("", "end", values=(t["date"], t["bezeichnung"], t["betrag"]))

        self.create_summary_label()
        self.create_buttons()

        # Dropdown für Monate
        self.month_var = tk.StringVar()
        self.month_combobox = ttk.Combobox(self.right_frame, textvariable=self.month_var, state="readonly")
        self.month_combobox.grid(row=3, column=0, sticky="w", pady=10)

        # Alle Monate ermitteln und für Dropdown vorbereiten
        self.monate = self.get_month_list()
        self.mapping = {self.month_year_to_name(m): m for m in self.monate}
        werte_fuer_dropdown = ["Alle"] + list(self.mapping.keys())
        self.month_combobox['values'] = werte_fuer_dropdown
        self.month_combobox.current(0)  # "Alle" vorauswählen

        # Event binden: Filter bei Auswahländerung
        self.month_combobox.bind("<<ComboboxSelected>>", self.filter_by_month)

        self.schliessen_button = tk.Button(self.root, text="Schließen", command=self.root.quit)
        self.schliessen_button.grid(row=20, column=3)

        self.root.mainloop()
        self.filter_by_month()

    def create_frames(self):
        self.left_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=1, pady=10, sticky="n")

        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        self.middle_frame.grid_columnconfigure(0, weight=1)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=0, column=2, padx=10, pady=10, sticky="n")

    def create_income_section(self):
        self.income_label = tk.Label(self.middle_frame, text="Einnahmen", font=("Arial", 14, "bold"))
        self.income_label.grid(row=0, column=0)

        self.income_tree = ttk.Treeview(self.middle_frame, columns=("Datum", "Bezeichnung", "Betrag"), show="headings")
        self.income_tree.heading("Bezeichnung", text="Bezeichnung")
        self.income_tree.heading("Betrag", text="Betrag (€)")
        self.income_tree.heading("Datum", text="Datum")
        self.income_tree.grid(row=1, column=0)

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

    def create_expense_section(self):
        self.expense_label = tk.Label(self.middle_frame, text="Ausgaben", font=("Arial", 14, "bold"))
        self.expense_label.grid(row=2, column=0)

        self.expense_tree = ttk.Treeview(self.middle_frame, columns=("Datum","Bezeichnung","Betrag"), show="headings")
        self.expense_tree.heading("Betrag", text="Betrag (€)")
        self.expense_tree.heading("Bezeichnung", text="Bezeichnung")
        self.expense_tree.heading("Datum", text="Datum")
        self.expense_tree.grid(row=3, column=0)

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

    def create_buttons(self):
        self.einnahme_button = tk.Button(self.left_frame, text="Einnahme hinzufügen", command=self.add_income)
        self.einnahme_button.grid(row=3, column=0)

        self.ausgabe_button = tk.Button(self.left_frame, text="Ausgabe hinzufügen", command=self.add_expense)
        self.ausgabe_button.grid(row=7, column=0)

        # Für Einnahme löschen
        self.einnahme_loeschen_button = tk.Button(self.left_frame, text="Einnahme löschen", command=self.delete_income)
        self.einnahme_loeschen_button.grid(row=3, column=1)

        # Für Einnahme bearbeiten
        self.einnahme_bearbeiten_button = tk.Button(self.left_frame, text="Einnahme bearbeiten",
                                                    command=self.edit_income)
        self.einnahme_bearbeiten_button.grid(row=3, column=2)

        self.ausgabe_loeschen_button = tk.Button(self.left_frame, text="Ausgabe löschen", command=self.delete_expense)
        self.ausgabe_loeschen_button.grid(row=7, column=1)

        self.ausgabe_bearbeiten_button = tk.Button(self.left_frame, text="Ausgabe bearbeiten",
                                                   command=self.edit_expense)
        self.ausgabe_bearbeiten_button.grid(row=7, column=2)

    def create_summary_label(self):
        self.kontostand_label = tk.Label(self.right_frame, text=f"Kontostand: {rechner.berechne_kontostand()} €")
        self.kontostand_label.grid(row=0, column=0, sticky="w")

        self.income_total_label = tk.Label(self.right_frame, text=f"Einkommen insgesamt: {rechner.get_total_income()} €")
        self.income_total_label.grid(row=1, column=0, sticky="w")

        self.expense_total_label = tk.Label(self.right_frame, text=f"Ausgaben insgesamt: {rechner.get_total_expense()} €")
        self.expense_total_label.grid(row=2, column=0, sticky="w")

    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def add_income(self):
        try:
            betrag = float(self.einnahme_betrag_entry.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte einen gültigen Betrag eingeben.")
            return

        bezeichnung = self.einnahme_bezeichnung_entry.get()
        datum = self.einnahme_datum_entry.get()

        if not bezeichnung.strip():
            messagebox.showerror("Fehler", "Bezeichnung darf nicht leer sein.")
            return

        if not FinanzRechnerGUI.is_valid_date(datum):
            messagebox.showerror("Fehler", "Datum muss im Format DD.MM.YYYY sein.")
            return

        rechner.add_einnahme(betrag, bezeichnung, datum)
        rechner.save_data()
        self.income_tree.insert("", "end", values=(datum, bezeichnung, betrag))
        self.update_month_filter()
        self.filter_by_month()
        self.update_kontostand()

        self.einnahme_betrag_entry.delete(0, tk.END)
        self.einnahme_bezeichnung_entry.delete(0, tk.END)
        self.einnahme_datum_entry.delete(0, tk.END)

    def add_expense(self):
        try:
            betrag = float(self.ausgabe_betrag_entry.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte einen gültigen Betrag eingeben.")
            return

        bezeichnung = self.ausgabe_bezeichnung_entry.get()
        datum = self.ausgabe_datum_entry.get()

        if not bezeichnung.strip():
            messagebox.showerror("Fehler", "Bezeichnung darf nicht leer sein.")
            return

        if not FinanzRechnerGUI.is_valid_date(datum):
            messagebox.showerror("Fehler", "Datum muss im Format DD.MM.YYYY sein.")
            return

        rechner.add_ausgabe(betrag, bezeichnung, datum)
        rechner.save_data()
        self.expense_tree.insert("", "end", values=(datum, bezeichnung, betrag))
        self.update_month_filter()
        self.filter_by_month()
        self.update_kontostand()
        self.ausgabe_betrag_entry.delete(0, tk.END)
        self.ausgabe_bezeichnung_entry.delete(0, tk.END)
        self.ausgabe_datum_entry.delete(0, tk.END)

    def delete_income(self):
        selected_item = self.income_tree.selection()
        if selected_item:
            item_id = selected_item[0]
            values = self.income_tree.item(item_id, 'values')
            datum, bezeichnung, betrag = values
            # Treeview löschen
            self.income_tree.delete(item_id)
            # Liste filtern
            rechner.transactions = [
                t for t in rechner.transactions
                if not (t["type"] == "einkommen" and str(t["date"]) == datum and str(
                    t["bezeichnung"]) == bezeichnung and str(t["betrag"]) == str(betrag))
            ]
            rechner.save_data()
            self.update_month_filter()
            self.filter_by_month()
            self.update_kontostand()

    def edit_income(self):
        selected_item = self.income_tree.selection()
        if selected_item:
            item_id = selected_item[0]
            values = self.income_tree.item(item_id, 'values')
            datum, bezeichnung, betrag = values

            # Alte Werte in Entry-Felder laden
            self.einnahme_datum_entry.delete(0, tk.END)
            self.einnahme_datum_entry.insert(0, datum)

            self.einnahme_bezeichnung_entry.delete(0, tk.END)
            self.einnahme_bezeichnung_entry.insert(0, bezeichnung)

            self.einnahme_betrag_entry.delete(0, tk.END)
            self.einnahme_betrag_entry.insert(0, betrag)

            # Alten Eintrag löschen
            self.income_tree.delete(item_id)
            rechner.transactions = [
                t for t in rechner.transactions
                if not (t["type"] == "einkommen" and str(t["date"]) == datum and str(
                    t["bezeichnung"]) == bezeichnung and str(t["betrag"]) == str(betrag))
            ]
            rechner.save_data()
            self.update_month_filter()
            self.filter_by_month()
            self.update_kontostand()

    def delete_expense(self):
        selected_item = self.expense_tree.selection()
        if selected_item:
            item_id = selected_item[0]
            values = self.expense_tree.item(item_id, 'values')
            datum, bezeichnung, betrag = values
            # Treeview löschen
            self.expense_tree.delete(item_id)
            # Liste filtern
            rechner.transactions = [
                t for t in rechner.transactions
                if not (t["type"] == "ausgabe" and str(t["date"]) == datum and str(
                    t["bezeichnung"]) == bezeichnung and str(t["betrag"]) == str(betrag))
            ]
            rechner.save_data()
            self.update_month_filter()
            self.filter_by_month()
            self.update_kontostand()

    def edit_expense(self):
        selected_item = self.expense_tree.selection()
        if selected_item:
            item_id = selected_item[0]
            values = self.expense_tree.item(item_id, 'values')
            datum, bezeichnung, betrag = values

            # Alte Werte in Entry-Felder laden
            self.ausgabe_datum_entry.delete(0, tk.END)
            self.ausgabe_datum_entry.insert(0, datum)

            self.ausgabe_bezeichnung_entry.delete(0, tk.END)
            self.ausgabe_bezeichnung_entry.insert(0, bezeichnung)

            self.ausgabe_betrag_entry.delete(0, tk.END)
            self.ausgabe_betrag_entry.insert(0, betrag)

            # Alten Eintrag löschen
            self.expense_tree.delete(item_id)
            rechner.transactions = [
                t for t in rechner.transactions
                if not (t["type"] == "ausgabe" and str(t["date"]) == datum and str(
                    t["bezeichnung"]) == bezeichnung and str(t["betrag"]) == str(betrag))
            ]
            rechner.save_data()
            self.update_month_filter()
            self.filter_by_month()
            self.update_kontostand()

    def update_kontostand(self):
        self.kontostand_label.config(text=f"Kontostand: {rechner.berechne_kontostand()} €")
        self.income_total_label.config(text=f"Einnahmen insgesamt: {rechner.get_total_income()} €")
        self.expense_total_label.config(text=f"Ausgaben insgesamt: {rechner.get_total_expense()} €")

    def create_month_dropdown(self):
        self.month_var = tk.StringVar()
        self.month_dropdown = ttk.Combobox(self.left_frame, textvariable=self.month_var, state="readonly")
        self.month_dropdown['values'] = self.get_month_list()
        self.month_dropdown.current(0)  # Standard auf "Alle" setzen
        self.month_dropdown.grid(row=8, column=0, columnspan=3, sticky="we")
        self.month_dropdown.bind("<<ComboboxSelected>>", self.filter_by_month)

    def get_month_list(self):
        monate = set()
        for t in rechner.transactions:
            datum = t["date"]  # "DD.MM.YYYY"
            if len(datum) >= 7:
                monat_jahr = datum[3:]  # "MM.YYYY"
                monate.add(monat_jahr)

        def sort_key(m):
            monat, jahr = m.split('.')
            return (int(jahr), int(monat))

        return sorted(monate, key=sort_key)

    def month_year_to_name(self, monat_jahr):
        monate_namen = ["Januar", "Februar", "März", "April", "Mai", "Juni",
                        "Juli", "August", "September", "Oktober", "November", "Dezember"]
        monat, jahr = monat_jahr.split('.')
        monat_name = monate_namen[int(monat) - 1]
        return f"{monat_name} {jahr}"

    def filter_by_month(self, event=None):
        auswahl = self.month_var.get()
        if auswahl == "Alle":
            filter_str = None
        else:
            filter_str = self.mapping[auswahl]

        self.income_tree.delete(*self.income_tree.get_children())
        self.expense_tree.delete(*self.expense_tree.get_children())

        for t in rechner.transactions:
            datum = t["date"]
            monat_jahr = datum[3:] if len(datum) >= 7 else None
            if filter_str is None or monat_jahr == filter_str:
                values = (datum, t["bezeichnung"], t["betrag"])
                if t["type"] == "einkommen":
                    self.income_tree.insert("", "end", values=values)
                elif t["type"] == "ausgabe":
                    self.expense_tree.insert("", "end", values=values)

        self.update_summaries(filter_str)

    def update_summaries(self, filter_str=None):
        """Aktualisiert die Label für Einnahmen und Ausgaben mit Filter."""
        einkommen, ausgaben = self.get_filtered_totals(filter_str)
        self.income_total_label.config(text=f"Einnahmen insgesamt: {einkommen:.2f} €")
        self.expense_total_label.config(text=f"Ausgaben insgesamt: {ausgaben:.2f} €")

    def get_filtered_totals(self, filter_str=None):
        """Gibt Tupel (summe_einnahmen, summe_ausgaben) zurück, gefiltert nach Monat."""
        summe_einnahmen = 0.0
        summe_ausgaben = 0.0
        for t in rechner.transactions:
            datum = t["date"]
            monat_jahr = datum[3:] if len(datum) >= 7 else None
            if filter_str is None or monat_jahr == filter_str:
                if t["type"] == "einkommen":
                    summe_einnahmen += float(t["betrag"])
                elif t["type"] == "ausgabe":
                    summe_ausgaben += float(t["betrag"])
        return summe_einnahmen, summe_ausgaben

    def update_month_filter(self):
        # Neue Monate berechnen
        self.monate = self.get_month_list()
        self.mapping = {self.month_year_to_name(m): m for m in self.monate}

        # Neue Werte für Combobox
        werte_fuer_dropdown = ["Alle"] + list(self.mapping.keys())
        self.month_combobox['values'] = werte_fuer_dropdown

        # Auswahl prüfen und ggf. setzen
        if self.month_var.get() not in werte_fuer_dropdown:
            self.month_var.set("Alle")



if __name__ == "__main__":
    FinanzRechnerGUI()
