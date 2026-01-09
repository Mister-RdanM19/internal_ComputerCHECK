package main

import (
	"fmt"
	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/mem"
	"github.com/shirou/gopsutil/disk"
	"github.com/shirou/gopsutil/net"
)

func main() {
	// CPU Info
	cpuInfo, _ := cpu.Info()
	fmt.Println("CPU Info:")
	for _, info := range cpuInfo {
		fmt.Println("Model:", info.ModelName)
	}

	// RAM Info
	memInfo, _ := mem.VirtualMemory()
	fmt.Println("\nRAM Info:")
	fmt.Println("Total RAM:", memInfo.Total/1024/1024/1024, "GB")
	fmt.Println("Used RAM:", memInfo.Used/1024/1024/1024, "GB")

	// Disk Info
	diskInfo, _ := disk.Usage("/")
	fmt.Println("\nDisk Info:")
	fmt.Println("Total Disk Space:", diskInfo.Total/1024/1024/1024, "GB")
	fmt.Println("Free Disk Space:", diskInfo.Free/1024/1024/1024, "GB")
	
	// Network Info
	netInfo, _ := net.IOCounters(true)
	fmt.Println("\nNetwork Info:")
	for _, info := range netInfo {
		fmt.Println("Interface:", info.Name, "Bytes Sent:", info.BytesSent, "Bytes Received:", info.BytesRecv)
	}
}
