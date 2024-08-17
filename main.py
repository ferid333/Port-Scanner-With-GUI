import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class PortScanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Port Scanner")
        self.root.geometry("600x400")
        
        self.ip_address = tk.StringVar()
        self.start_port = tk.IntVar()
        self.end_port = tk.IntVar()
        self.running = False
        
        self.setup_widgets()
        
    def setup_widgets(self):

        ip_frame = tk.Frame(self.root)
        ip_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        tk.Label(ip_frame, text="IP Address:").pack(side=tk.LEFT, padx=5)
        ip_entry = tk.Entry(ip_frame, textvariable=self.ip_address)
        ip_entry.pack(side=tk.LEFT, padx=5)

        port_frame = tk.Frame(self.root)
        port_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        tk.Label(port_frame, text="Start Port:").pack(side=tk.LEFT, padx=5)
        start_port_entry = tk.Entry(port_frame, textvariable=self.start_port)
        start_port_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(port_frame, text="End Port:").pack(side=tk.LEFT, padx=5)
        end_port_entry = tk.Entry(port_frame, textvariable=self.end_port)
        end_port_entry.pack(side=tk.LEFT, padx=5)

        scan_button = tk.Button(port_frame, text="Start Scanning", command=self.start_scanning)
        scan_button.pack(side=tk.LEFT, padx=5)
        
        stop_button = tk.Button(port_frame, text="Stop Scanning", command=self.stop_scanning)
        stop_button.pack(side=tk.LEFT, padx=5)

        self.result_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=20)
        self.result_display.pack(fill=tk.BOTH, expand=True)

    def start_scanning(self):
        if not self.running:
            self.running = True
            self.result_display.delete(1.0, tk.END)
            self.scan_thread = threading.Thread(target=self.scan_ports)
            self.scan_thread.start()

    def stop_scanning(self):
        if self.running:
            self.running = False
            self.scan_thread.join()

    def scan_ports(self):
        ip = self.ip_address.get()
        start_port = self.start_port.get()
        end_port = self.end_port.get()

        for port in range(start_port, end_port + 1):
            if not self.running:
                break
            result = self.check_port(ip, port)
            self.result_display.insert(tk.END, f"Port {port}: {'Open' if result else 'Closed'}\n")
            self.result_display.see(tk.END)

    def check_port(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                return result == 0
        except socket.error:
            return False

root = tk.Tk()
app = PortScanner(root)
root.mainloop()
