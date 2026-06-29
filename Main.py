import tkinter as tk
from tkinter import messagebox
import psutil

first_network = psutil.net_io_counters()
second_network= psutil.net_io_counters(pernic= False, nowrap= True)
cpu_value = psutil.cpu_percent(interval=1)

#cpu_warning_shown = False
label_cpu_warning = None
network_window = None
cpu_window = None
ram_window = None
storage_window = None
label_cpu = None
label_ram = None
label_total_ram = None
label_mem_percentage = None

def show_cpu():
    global cpu_window
    global label_cpu
    global label_cpu_warning
    #global cpu_warning_shown
    cpu_value = psutil.cpu_percent(interval=1)

    if cpu_window is not None and not cpu_window.winfo_exists():
        cpu_window = None
        return

    if cpu_window is None:
        cpu_window = tk.Toplevel(root)
        cpu_window.title("CPU")
        cpu_window.geometry("400x120")
        label_cpu = tk.Label(cpu_window, bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_cpu.place(x=100, y=25)
        cpu_window.configure(bg="#1e1e1e")
        label_cpu_warning = tk.Label(cpu_window, bg="#1e1e1e")
        label_cpu_warning.place(x=100, y=45)

    if cpu_value >= 80:
        label_cpu_warning.config(text="Warning: CPU too high!", fg="#EF0307", font=("Courier", 12, "bold"))
    else: label_cpu_warning.config(text="")

    if cpu_value >= 80:
        label_cpu.config(fg="#EF0307")
    else:
        label_cpu.config(fg="#00ff99")
    
    label_cpu.config(text= f"CPU Usage: {cpu_value} %",bg="#1e1e1e", font=("Courier", 12, "bold"))
    cpu_window.after(3000, show_cpu)
        
    #if cpu_value >= 1 and not cpu_warning_shown:
    #    messagebox.showwarning("WARNING", "CPU Usage too high!")
    #    cpu_warning_shown = True

def show_ram():
    global ram_window
    global label_ram
    global label_total_ram
    global label_mem_percentage
    global label_ram_warning
    mem = psutil.virtual_memory()
    mem_perc = mem.percent

    if ram_window is not None and not ram_window.winfo_exists():
        ram_window = None
        return
    
    total_memory = (mem.total / 1024**3)
    available_mem = (mem.available / 1024**3)

    if ram_window is None:
        ram_window = tk.Toplevel(root)
        ram_window.title("RAM")
        ram_window.geometry("400x150")
        ram_window.configure(bg="#1e1e1e")
                
        label_total_ram = tk.Label(ram_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_total_ram.place(x=50, y=20)

        label_ram = tk.Label(ram_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_ram.place(x=50, y=50)

        label_mem_percentage = tk.Label(ram_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_mem_percentage.place (x=50, y=80)

        label_ram_warning = tk.Label(ram_window, bg="#1e1e1e")
        label_ram_warning.place(x=50, y=110)

    label_total_ram.config(text= f"Total memory: {total_memory:.2f} GB",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_ram.config(text= f"Total available memory: {available_mem:.2f} GB",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_mem_percentage.config(text= f"Using: {mem.percent:.2f} % of RAM",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))

    if mem_perc >= 80:
        label_ram_warning.config(text="Warning: RAM Usage too high!", fg="#EF0307", font=("Courier", 12, "bold"))
    else: label_ram_warning.config(text="")

    if mem_perc >= 80:
        label_mem_percentage.config(fg="#EF0307")
    else:
        label_mem_percentage.config(fg="#00ff99")

    ram_window.after(3000, show_ram)

def show_network():
    global network_window
    global first_network
    global second_network
    global total_bytes_send
    global total_bytes_recv
    global interval_bytes_recv
    global interval_bytes_send
    global label_total_send
    global label_total_received
    global label_interval_send
    global label_interval_received
    second_network = psutil.net_io_counters(pernic=False, nowrap=True)

    total_bytes_send = (second_network.bytes_sent / 1024**2)
    total_bytes_recv = (second_network.bytes_recv  / 1024**2)
    interval_bytes_send = ((second_network.bytes_sent - first_network.bytes_sent) / 1024**2)
    interval_bytes_recv = ((second_network.bytes_recv - first_network.bytes_recv) / 1024**2)
    first_network = second_network
    if network_window is not None and not network_window.winfo_exists():
        network_window = None
        return

    if network_window is None:
        network_window = tk.Toplevel(root)
        network_window.title("Network")
        network_window.geometry("500x200")
        network_window.configure(bg="#1e1e1e")

        label_total_send = tk.Label(network_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_total_send.place(x=50, y=30)

        label_total_received = tk.Label(network_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_total_received.place(x=50, y= 60)

        label_interval_send = tk.Label(network_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_interval_send.place(x=50, y=150)

        label_interval_received = tk.Label(network_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_interval_received.place(x=50, y=120)
    
    label_total_send.config(text= f"Number of total bytes sent : {total_bytes_send:.2f} Mb",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_total_received.config(text= f"Number of total bytes received : {total_bytes_recv:.2f} Mb",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_interval_received.config(text= f"Number of bytes sent : {interval_bytes_send:.2f} Mb",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_interval_send.config(text= f"Number of bytes received : {interval_bytes_recv:.2f} Mb",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))

    network_window.after(3000, show_network)
        
def show_storage():
    global storage_window
    global label_total_storage
    global label_used_storage
    global label_percentage_storage_used

    if storage_window is not None and not storage_window.winfo_exists():
        storage_window = None
        return

    if storage_window is None:
        storage_window = tk.Toplevel(root)
        storage_window.title("Storage Statistics")
        storage_window.geometry("400x200")
        storage_window.configure(bg="#1e1e1e")

        label_total_storage = tk.Label(storage_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_total_storage.place (x=50, y=30)
        label_used_storage = tk.Label(storage_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_used_storage.place (x=50, y= 70)
        label_percentage_storage_used = tk.Label(storage_window,bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
        label_percentage_storage_used.place (x=50, y= 110)

    disk = psutil.disk_usage('/')
    total_storage = (disk.total / 1024**3)
    used_storage = (disk.used / 1024**3)
    storage_used_percentage = (disk.percent)

    label_total_storage.config(text= f"total existing storage: {total_storage:.0f} GB",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_used_storage.config(text= f"used storage: {used_storage:.0f} GB",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
    label_percentage_storage_used.config(text= f"{storage_used_percentage} % of storage is used",bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))

    storage_window.after(3000, show_storage)

# Main Window
root = tk.Tk()

# Window title
root.title("System-Monitoring")

# Main Window Size

root.geometry("400x250")
# Labeling Main Menu

label = tk.Label(root,text = "System Monitoring", bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
label.place(x=90, y=10)

# Networking Button

button_network = tk.Button(root, text= "Network", command= show_network, bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
button_network.place(x= 90, y=50)

# CPU Button

button_cpu = tk.Button(root, text= "CPU", command= show_cpu, bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
button_cpu.place(x= 90, y=90)

# RAM Button

button_ram = tk.Button(root, text= "RAM", command = show_ram, bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
button_ram.place(x= 90, y=130)

# Storage Button

button_storage = tk.Button(root, text= "Storage", command = show_storage, bg="#1e1e1e", fg="#00ff99", font=("Courier", 12, "bold"))
button_storage.place(x= 90, y=170)

# Window Design
root.configure(bg="#1e1e1e")

# Start
root.mainloop()