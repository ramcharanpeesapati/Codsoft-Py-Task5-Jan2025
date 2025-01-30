import csv

class Connectly:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, group="General"):
        """Add a new contact."""
        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Group": group})
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Group: {contact['Group']}")

    def search_contact(self, name):
        """Search for a contact by name."""
        results = [c for c in self.contacts if name.lower() in c["Name"].lower()]
        if results:
            for contact in results:
                print(f"Found: {contact}")
        else:
            print("No contacts found.")

    def export_contacts(self, filename="contacts.csv"):
        """Export contacts to a CSV file."""
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Group"])
            writer.writeheader()
            writer.writerows(self.contacts)
        print(f"Contacts exported to {filename}.")

# Example Usage
cb = Connectly()
cb.add_contact("Subramanyam", "9848032919", "KothagaCellPhoneKonnanu@gmail.com", "Passport Office Karnool")
cb.view_contacts()
cb.search_contact("Subramanyam")
cb.export_contacts()
