import psutil, time
while True:
    print("\n" * 3)
    print("--- System Monitoring ---")
    print("1. Hardware (CPU, RAM, DISK)")
    print("2. Network-Traffic")
    print("3. Processes/Services")
    choice = input("Option: ")
    
    #CPU Usage
    if choice == "1":
        while True:
            CPU_Perc = psutil.cpu_percent(interval=1)
            print (f"CPU Usage: {CPU_Perc} %")
            if CPU_Perc > 85:
                print("WARNING: CPU Usage too high!")
            #RAM- TotalRAM/AvailableRAM
            mem = psutil.virtual_memory()
            total_memory = (mem.total / 1024**3)
            print (f"Total memory: {total_memory:.2f} GB")
        

            #Available RAM
            available_memory = (mem.available / 1024**3)
            print(f"Total available memory: {available_memory:.2f} GB")
            if mem.percent > 80 :
                print("WARNING: RAM usage too high!")

            #Disks
            disk = psutil.disk_usage('/')
            io_counters = psutil.disk_io_counters(perdisk=True, nowrap=True)

            #Disk_storage
            total_storage = (disk.total / 1024**3)
            used_storage = (disk.used / 1024**3)
            storage_used_percentage = (disk.percent)

            print(f"total existing storage: {total_storage:.0f} GB")
            print(f"used storage: {used_storage:.0f} GB")
            print(f"{storage_used_percentage} % of storage is used")
            if storage_used_percentage > 90:
                print("WARNING: Only 10% Of Storage left!")
            print()

            #Disk_counters and Disk_times
            for disk_name, counters in io_counters.items():
                disk_readtime = counters.read_time
                disk_writetime = counters.write_time

                print (f"[{disk_name}]")
                print (f"time it took to read : {disk_readtime} ms")
                print (f"time it took to write : {disk_writetime} ms")
            print()
            choice_back = input("Press Enter to refresh or type 'quit' to go back ")
            if choice_back == "quit":
                break
    

    #Network monitoring - Bytes/Packets/Errors/Dropping
    elif choice == "2":
        first_network= psutil.net_io_counters()
    
        while True:
            second_network= psutil.net_io_counters(pernic= False, nowrap= True)

            packets_sent = second_network.packets_sent
            packets_recv = second_network.packets_recv

            errin = second_network.errin
            errout = second_network.errout

            dropin = second_network.dropin
            dropout = second_network.dropout

            total_bytes_send = (second_network.bytes_sent / 1024**2)
            total_bytes_recv = (second_network.bytes_recv  / 1024**2)
            interval_bytes_send = ((second_network.bytes_sent - first_network.bytes_sent) / 1024**2)
            interval_bytes_recv = ((second_network.bytes_recv - first_network.bytes_recv) / 1024**2)


            first_network = second_network
            time.sleep(3)
            print(f"Number of total bytes sent : {total_bytes_send:.2f} Mb")
            print(f"Number of total bytes received : {total_bytes_recv:.2f} Mb")
            print()
            print(f"Number of bytes sent : {interval_bytes_send:.2f} Mb")
            print(f"Number of bytes received : {interval_bytes_recv:.2f} Mb")
            print()
            print(f"Number of packets sent : {packets_sent}")
            print(f"Number of packets received : {packets_recv}")
            print()
            print(f"{errin} errors occured while receiving")
            print(f"{errout} errors occured while sending")
            print()
            print(f"total of {dropin} incoming packets were dropped")
            print(f"total of {dropout} outgoing packets were dropped")
            print()
            
            choice_back = input("Press Enter to refresh or type 'quit' to go back ")
            if choice_back == "quit":
                break
    



    elif choice == "3": 
        psutil.cpu_percent()
        while True:
            for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
                #print (proc.info)
                print(f"PID: {proc.info['pid']} Name: {proc.info['name']}      CPU: {proc.info['cpu_percent']:.2f}%  RAM:  {proc.info['memory_percent']:.2f} %")
            
            choice_back = input("Press Enter to refresh or type 'quit' to go back ")
            if choice_back == "quit":
                break
    