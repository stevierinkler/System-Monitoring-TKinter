import tkinter as tk
import psutil
first_network = psutil.net_io_counters()
network_window = None
cpu_window = None
ram_window = None
storage_window = None

def show_cpu():
    global cpu_window
    if cpu_window is None :
        cpu_window = tk.Toplevel(root)
        cpu_window.title("CPU")
        cpu_window.geometry("300x70")

    label_cpu = tk.Label(cpu_window,text= f"CPU Usage: {psutil.cpu_percent(interval=1)} %")
    label_cpu.place(x=100, y=25)
    cpu_window.after(5000, show_cpu)

def show_ram():
    global ram_window
    if ram_window is None:
        ram_window = tk.Toplevel(root)
        ram_window.title("RAM")
        ram_window.geometry("300x100")

    mem = psutil.virtual_memory()
    total_memory = (mem.total / 1024**3)
    total_ram = tk.Label(ram_window,text= f"Total memory: {total_memory:.2f} GB")
    total_ram.place(x=50, y=30)

    available_mem = (mem.available / 1024**3)
    label_ram = tk.Label(ram_window,text= f"Total available memory: {available_mem:.2f} GB")
    label_ram.place(x=50, y=50)

    label_mem_percentage = tk.Label(ram_window,text = f"Using: {mem.percent:.2f} of RAM")
    label_mem_percentage.place (x=50, y=70)

    ram_window.after(5000, show_ram)

def show_network():
    global network_window
    if network_window is None:
        network_window = tk.Toplevel(root)
        network_window.title("Network")
        network_window.geometry("300x200")
    
    global first_network
    second_network= psutil.net_io_counters(pernic= False, nowrap= True)

    total_bytes_send = (second_network.bytes_sent / 1024**2)
    total_bytes_recv = (second_network.bytes_recv  / 1024**2)
    interval_bytes_send = ((second_network.bytes_sent - first_network.bytes_sent) / 1024**2)
    interval_bytes_recv = ((second_network.bytes_recv - first_network.bytes_recv) / 1024**2)

    label_total_send = tk.Label(network_window,text= f"Number of total bytes sent : {total_bytes_send:.2f} Mb")
    label_total_send.place(x=50, y=30)
    label_total_received = tk.Label(network_window,text= f"Number of total bytes received : {total_bytes_recv:.2f} Mb")
    label_total_received.place(x=50, y= 50)

    label_interval_send = tk.Label(network_window,text= f"Number of bytes sent : {interval_bytes_send:.2f} Mb")
    label_interval_send.place(x=50, y=110)
    label_interval_received = tk.Label(network_window,text= f"Number of bytes received : {interval_bytes_recv:.2f} Mb")
    label_interval_received.place(x=50, y=130)

    network_window.after(5000, show_network)
    first_network = second_network
    
def show_storage():
    global storage_window
    if storage_window is None:
        storage_window = tk.Toplevel(root)
        storage_window.title("Storage Statistics")
        storage_window.geometry("300x200")

    disk = psutil.disk_usage('/')
    io_counters = psutil.disk_io_counters(perdisk= True , nowrap= True)
    total_storage = (disk.total / 1024**3)
    used_storage = (disk.used / 1024**3)
    storage_used_percentage = (disk.percent)

    label_total_storage = tk.Label(storage_window,text= f"total existing storage: {total_storage:.0f} GB")
    label_total_storage.place (x=50, y=30)
    label_used_storage = tk.Label(storage_window,text= f"used storage: {used_storage:.0f} GB")
    label_used_storage.place (x=50, y= 50)
    label_percentage_storage_used = tk.Label(storage_window,text= f"{storage_used_percentage} % of storage is used")
    label_percentage_storage_used.place (x=50, y= 70)


# Main Window
root = tk.Tk()

# Window title
root.title("System-Monitoring")

# Main Window Size

root.geometry("300x200")
# Labeling Main Menu

label = tk.Label(root,text = "System Monitoring")
label.place(x=90, y=10)

# Networking Button

button_network = tk.Button(root, text= "Network", command= show_network)
button_network.place(x= 90, y=40)

# CPU Button

button_cpu = tk.Button(root, text= "CPU", command= show_cpu)
button_cpu.place(x= 90, y=70)

# RAM Button

button_ram = tk.Button(root, text= "RAM", command = show_ram)
button_ram.place(x= 90, y=100)

# Storage Button

button_storage = tk.Button(root, text= "Storage", command = show_storage)
button_storage.place(x= 90, y=130)

# Start
root.mainloop()