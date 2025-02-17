import tkinter as tk
from tkinter import messagebox

class FamilyAccount:
    def __init__(self):
        self.siblings = []  # List to store sibling data
        self.profit_percentage = 5  # Default profit percentage
        self.tax_percentage = 10   # Default tax percentage

    def add_sibling(self, name, amount):
        """Add a sibling's data."""
        self.siblings.append({"name": name, "amount": amount})

    def calculate_profit(self):
        """Calculate profit for each sibling based on the profit percentage."""
        for sibling in self.siblings:
            sibling['profit'] = sibling['amount'] * (self.profit_percentage / 100)

    def calculate_tax(self):
        """Calculate tax deductions for each sibling based on the tax percentage."""
        for sibling in self.siblings:
            sibling['tax'] = sibling['profit'] * (self.tax_percentage / 100)

    def get_total_profit(self):
        """Calculate the total profit from all siblings."""
        return sum(sibling['profit'] for sibling in self.siblings)

    def get_total_tax(self):
        """Calculate the total tax deductions from all siblings."""
        return sum(sibling['tax'] for sibling in self.siblings)
    
    def get_net_balance(self):
        """Calculate the net balance after tax deduction."""
        return self.get_total_profit() - self.get_total_tax()

    def update_profit_percentage(self, new_percentage):
        """Update the profit percentage."""
        self.profit_percentage = new_percentage

    def update_tax_percentage(self, new_percentage):
        """Update the tax percentage."""
        self.tax_percentage = new_percentage


class FamilyAccountGUI:
    def __init__(self, root, family_account):
        self.family_account = family_account
        self.root = root
        self.root.title("Family Bank Account")

        # Profit and Tax percentage fields
        self.profit_label = tk.Label(root, text="Profit Percentage:")
        self.profit_label.grid(row=0, column=0)
        self.profit_entry = tk.Entry(root)
        self.profit_entry.insert(0, str(self.family_account.profit_percentage))
        self.profit_entry.grid(row=0, column=1)

        self.tax_label = tk.Label(root, text="Tax Percentage:")
        self.tax_label.grid(row=1, column=0)
        self.tax_entry = tk.Entry(root)
        self.tax_entry.insert(0, str(self.family_account.tax_percentage))
        self.tax_entry.grid(row=1, column=1)

        # Update button for Profit and Tax Percentage
        self.update_button = tk.Button(root, text="Update Percentages", command=self.update_percentages)
        self.update_button.grid(row=2, column=0, columnspan=2)

        # Sibling Details
        self.sibling_name_label = tk.Label(root, text="Sibling Name:")
        self.sibling_name_label.grid(row=3, column=0)
        self.sibling_name_entry = tk.Entry(root)
        self.sibling_name_entry.grid(row=3, column=1)

        self.sibling_amount_label = tk.Label(root, text="Amount:")
        self.sibling_amount_label.grid(row=4, column=0)
        self.sibling_amount_entry = tk.Entry(root)
        self.sibling_amount_entry.grid(row=4, column=1)

        # Add sibling button
        self.add_button = tk.Button(root, text="Add Sibling", command=self.add_sibling)
        self.add_button.grid(row=5, column=0, columnspan=2)

        # Display Sibling Data
        self.sibling_list_label = tk.Label(root, text="Siblings Data:")
        self.sibling_list_label.grid(row=6, column=0)

        self.sibling_listbox = tk.Listbox(root)
        self.sibling_listbox.grid(row=7, column=0, columnspan=2)

        # Calculate Profit and Tax
        self.calculate_button = tk.Button(root, text="Calculate Profit and Tax", command=self.calculate_profit_tax)
        self.calculate_button.grid(row=8, column=0, columnspan=2)

        self.total_profit_label = tk.Label(root, text="Total Profit:")
        self.total_profit_label.grid(row=9, column=0)

        self.total_tax_label = tk.Label(root, text="Total Tax:")
        self.total_tax_label.grid(row=10, column=0)
        
        self.net_balance_label = tk.Label(root, text="Net Balance:")
        self.net_balance_label.grid(row=11, column=0)

    def update_percentages(self):
        """Update profit and tax percentages based on user input."""
        try:
            new_profit_percentage = float(self.profit_entry.get())
            new_tax_percentage = float(self.tax_entry.get())
            self.family_account.update_profit_percentage(new_profit_percentage)
            self.family_account.update_tax_percentage(new_tax_percentage)
            messagebox.showinfo("Success", "Percentages updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid percentages.")

    def add_sibling(self):
        """Add sibling's name and amount."""
        sibling_name = self.sibling_name_entry.get()
        try:
            sibling_amount = float(self.sibling_amount_entry.get())
            self.family_account.add_sibling(sibling_name, sibling_amount)
            self.sibling_listbox.insert(tk.END, f"{sibling_name}: {sibling_amount} PKR")
            self.sibling_name_entry.delete(0, tk.END)
            self.sibling_amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def calculate_profit_tax(self):
        """Calculate and display profit, tax, and net balance for each sibling."""
        self.family_account.calculate_profit()
        self.family_account.calculate_tax()

        total_profit = self.family_account.get_total_profit()
        total_tax = self.family_account.get_total_tax()
        net_balance = self.family_account.get_net_balance()

        self.total_profit_label.config(text=f"Total Profit: {total_profit:.2f} PKR")
        self.total_tax_label.config(text=f"Total Tax: {total_tax:.2f} PKR")
        self.net_balance_label.config(text=f"Net Balance: {net_balance:.2f} PKR")


if __name__ == "__main__":
    # Create the family account instance
    family_account = FamilyAccount()

    # Create the Tkinter root window
    root = tk.Tk()

    # Create the GUI with the family account
    gui = FamilyAccountGUI(root, family_account)

    # Start the Tkinter event loop
    root.mainloop()
