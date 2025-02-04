import tkinter as tk
from tkinter import ttk, messagebox
from supabase import create_client
import os
from dotenv import load_dotenv
from passlib.hash import bcrypt

# Initialize global variables
current_user = None
supabase = None

def initialize_supabase():
    global supabase
    load_dotenv()
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def show_login_screen(root):
    clear_window(root)
    
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)
    
    ttk.Label(frame, text="Email:").grid(row=0, column=0)
    email_entry = ttk.Entry(frame)
    email_entry.grid(row=0, column=1)
    
    ttk.Label(frame, text="Password:").grid(row=1, column=0)
    pass_entry = ttk.Entry(frame, show="*")
    pass_entry.grid(row=1, column=1)
    
    ttk.Button(frame, text="Login", command=lambda: handle_login(root, email_entry.get(), pass_entry.get())).grid(row=2, column=1)
    ttk.Button(frame, text="Create Account", command=lambda: show_signup(root)).grid(row=3, column=1)

def show_signup(root):
    clear_window(root)
    
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)
    
    ttk.Label(frame, text="New Email:").grid(row=0, column=0)
    email_entry = ttk.Entry(frame)
    email_entry.grid(row=0, column=1)
    
    ttk.Label(frame, text="Password:").grid(row=1, column=0)
    pass_entry = ttk.Entry(frame, show="*")
    pass_entry.grid(row=1, column=1)
    
    ttk.Button(frame, text="Register", command=lambda: handle_signup(root, email_entry.get(), pass_entry.get())).grid(row=2, column=1)
    ttk.Button(frame, text="Back", command=lambda: show_login_screen(root)).grid(row=3, column=1)

def show_dashboard(root):
    clear_window(root)
    
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True)
    
    data = supabase.table("users").select("energy_data").eq("email", current_user).execute().data
    energy_data = data[0]["energy_data"] if data else {}
    
    ttk.Label(frame, text=f"Welcome {current_user}").pack()
    ttk.Label(frame, text="Energy Consumption:").pack()
    
    if energy_data:
        for device, usage in energy_data.items():
            ttk.Label(frame, text=f"{device}: {usage}kWh").pack()
    
    ttk.Button(frame, text="Optimize", command=trigger_optimization).pack()

def handle_login(root, email, password):
    global current_user
    try:
        user = supabase.table("users").select("*").eq("email", email).execute().data
        if user and bcrypt.verify(password, user[0]["password"]):
            current_user = email
            show_dashboard(root)
        else:
            messagebox.showerror("Error", "Invalid credentials")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_signup(root, email, password):
    try:
        hashed_pw = bcrypt.hash(password)
        supabase.table("users").insert({
            "email": email,
            "password": hashed_pw,
            "energy_data": {}
        }).execute()
        messagebox.showinfo("Success", "Account created!")
        show_login_screen(root)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def trigger_optimization():
    data = supabase.table("users").select("energy_data").eq("email", current_user).execute().data
    if data:
        with open("optimize.py", "w") as f:
            f.write(f"# Optimization data\nenergy_data = {data[0]['energy_data']}")
        messagebox.showinfo("Success", "Optimization file created!")

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

def main():
    initialize_supabase()
    root = tk.Tk()
    root.title("OptiSync AI")
    root.geometry("800x600")
    show_login_screen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
