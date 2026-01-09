import psutil
import platform
import os

# Menampilkan Informasi Sistem
def get_system_info():
    uname = platform.uname()
    print("System:", uname.system)
    print("Node Name:", uname.node)
    print("Release:", uname.release)
    print("Version:", uname.version)
    print("Machine:", uname.machine)
    print("Processor:", uname.processor)

# Menampilkan CPU Info
def get_cpu_info():
    print("\nCPU Info:")
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    print("CPU Frequency (GHz):", psutil.cpu_freq().max)
    print("CPU Usage (%):", psutil.cpu_percent(interval=1))

# Menampilkan RAM Info
def get_ram_info():
    print("\nRAM Info:")
    ram = psutil.virtual_memory()
    print("Total RAM (GB):", round(ram.total / (1024 ** 3), 2))
    print("Available RAM (GB):", round(ram.available / (1024 ** 3), 2))
    print("Used RAM (GB):", round(ram.used / (1024 ** 3), 2))
    print("RAM Usage (%):", ram.percent)

# Menampilkan Disk Info
def get_disk_info():
    print("\nDisk Info:")
    disk = psutil.disk_partitions()
    for partition in disk:
        print("Device:", partition.device)
        print("Mount point:", partition.mountpoint)
        print("File system type:", partition.fstype)
        usage = psutil.disk_usage(partition.mountpoint)
        print("Total space (GB):", round(usage.total / (1024 ** 3), 2))
        print("Used space (GB):", round(usage.used / (1024 ** 3), 2))
        print("Free space (GB):", round(usage.free / (1024 ** 3), 2))
        print("Disk Usage (%):", usage.percent)
        print("-" * 50)

# Menampilkan Jaringan Info
def get_network_info():
    print("\nNetwork Info:")
    net = psutil.net_if_addrs()
    for interface in net:
        print(f"Interface: {interface}")
        for addr in net[interface]:
            print(f"  {addr.family}: {addr.address}")

if __name__ == '__main__':
    get_system_info()
    get_cpu_info()
    get_ram_info()
    get_disk_info()
    get_network_info()
