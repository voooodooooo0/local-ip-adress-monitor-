import tkinter as tk
from tkinter import ttk, messagebox
from scanner import scan
from classifier import classify
import socket

class NetworkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Device Monitor")
        self.root.geometry("700x400")

        self.label = tk.Label(root, text="Enter IP Range (e.g. 192.168.1.0/24):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=30)
        self.entry.pack()

        self.button = tk.Button(root, text="Scan Network", command=self.start_scan)
        self.button.pack(pady=10)

        # TreeView for results
        self.tree = ttk.Treeview(root, columns=("IP", "MAC", "Hostname", "Type", "OS"), show='headings')
        self.tree.heading("IP", text="IP Address")
        self.tree.heading("MAC", text="MAC Address")
        self.tree.heading("Hostname", text="Hostname")
        self.tree.heading("Type", text="Device Type")
        self.tree.heading("OS", text="OS")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def start_scan(self):
        ip_range = self.entry.get()
        if not ip_range:
            messagebox.showwarning("Missing Input", "Please enter an IP range.")
            return

        self.tree.delete(*self.tree.get_children())  # Clear previous results

        try:
            devices = scan(ip_range)
            for device in devices:
                hostname = get_hostname(device['ip'])
                device_type, os_guess = classify(device['mac'])
                self.tree.insert("", "end", values=(device['ip'], device['mac'], hostname, device_type, os_guess))
        except Exception as e:
            messagebox.showerror("Error", str(e))

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Unknown"

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkApp(root)
    root.mainloop()




