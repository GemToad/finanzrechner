import json
from datetime import datetime

class Rechner:

    def __init__(self):
        self.transactions = []
        self.load_data()

    def add_einnahme(self, betrag, bezeichnung, datum):
        self.transactions.append({
            "type": "einkommen",
            "betrag": betrag,
            "bezeichnung": bezeichnung,
            "date": datum
        })
        self.save_data()

    def add_ausgabe(self, betrag, bezeichnung, datum):
        self.transactions.append({
            "type": "ausgabe",
            "betrag": betrag,
            "bezeichnung": bezeichnung,
            "date": datum
        })
        self.save_data()

    def berechne_kontostand(self):
        einkommen = sum(t["betrag"] for t in self.transactions if t["type"] == "einkommen")
        ausgaben = sum(t["betrag"] for t in self.transactions if t["type"] == "ausgabe")
        return einkommen - ausgaben

    def save_data(self):
        with open("transactions.json","w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_data(self):
        try:
            with open("transactions.json", "r") as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []
