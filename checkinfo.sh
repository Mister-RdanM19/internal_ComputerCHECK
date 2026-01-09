#!/bin/bash

# Menampilkan Informasi Sistem
echo "System Info:"
uname -a

# Menampilkan Informasi CPU
echo -e "\nCPU Info:"
lscpu

# Menampilkan Informasi RAM
echo -e "\nRAM Info:"
free -h

# Menampilkan Disk Info
echo -e "\nDisk Info:"
df -h

# Menampilkan Informasi GPU (Jika ada)
echo -e "\nGPU Info:"
lspci | grep -i vga

# Menampilkan Informasi Jaringan
echo -e "\nNetwork Info:"
ifconfig
