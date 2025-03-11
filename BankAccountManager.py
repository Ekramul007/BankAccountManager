import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, account_value, account_nu):
        self.account_Value = account_value
        self.account_Number = account_nu

    def debit_value(self, amount):
        if amount > self.account_Value:
            messagebox.showerror("Error", "Insufficient funds!")
        else:
            self.account_Value -= amount
            messagebox.showinfo("Transaction Successful", f"{amount} Rs debited.\nRemaining Balance: {self.account_Value} Rs")

    def credit_value(self, amount):
        self.account_Value += amount
        messagebox.showinfo("Transaction Successful", f"{amount} Rs credited.\nNew Balance: {self.account_Value} Rs")

def create_account():
    global acc
    acc_no = acc_number_entry.get()
    acc_value = acc_value_entry.get()
    if acc_no.isdigit() and acc_value.isdigit():
        acc = Account(int(acc_value), int(acc_no))
        messagebox.showinfo("Account Created", "Your account has been created successfully!")
    else:
        messagebox.showerror("Error", "Please enter valid numeric values!")

def withdraw_money():
    if not acc:
        messagebox.showerror("Error", "No account found! Create an account first.")
        return
    amount = withdraw_entry.get()
    if amount.isdigit():
        acc.debit_value(int(amount))
    else:
        messagebox.showerror("Error", "Please enter a valid amount!")

def deposit_money():
    if not acc:
        messagebox.showerror("Error", "No account found! Create an account first.")
        return
    amount = deposit_entry.get()
    if amount.isdigit():
        acc.credit_value(int(amount))
    else:
        messagebox.showerror("Error", "Please enter a valid amount!")

# GUI Setup
root = tk.Tk()
root.title("Bank Account Manager")
root.geometry("400x450")
root.configure(bg="#2c3e50")

# Labels and Entries
tk.Label(root, text="Enter Account Number:", fg="white", bg="#2c3e50", font=("Arial", 12)).pack(pady=5)
acc_number_entry = tk.Entry(root, font=("Arial", 12))
acc_number_entry.pack(pady=5)

tk.Label(root, text="Enter Account Value (Salary):", fg="white", bg="#2c3e50", font=("Arial", 12)).pack(pady=5)
acc_value_entry = tk.Entry(root, font=("Arial", 12))
acc_value_entry.pack(pady=5)

tk.Button(root, text="Create Account", command=create_account, bg="#27ae60", fg="white", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Enter Amount to Withdraw:", fg="white", bg="#2c3e50", font=("Arial", 12)).pack(pady=5)
withdraw_entry = tk.Entry(root, font=("Arial", 12))
withdraw_entry.pack(pady=5)

tk.Button(root, text="Withdraw Money", command=withdraw_money, bg="#e74c3c", fg="white", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Enter Amount to Deposit:", fg="white", bg="#2c3e50", font=("Arial", 12)).pack(pady=5)
deposit_entry = tk.Entry(root, font=("Arial", 12))
deposit_entry.pack(pady=5)

tk.Button(root, text="Deposit Money", command=deposit_money, bg="#2980b9", fg="white", font=("Arial", 12)).pack(pady=10)

acc = None
root.mainloop()