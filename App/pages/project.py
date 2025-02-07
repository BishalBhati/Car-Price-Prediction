import psutil
import time
import os

class SystemMonitor:
    def __init__(self):  # Correct constructor method
        pass

    # CPU Usage
    def cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    # Memory Usage
    def memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent, memory.used, memory.total

    # Network Usage
    def network_usage(self):
        net = psutil.net_io_counters()
        return net.bytes_sent, net.bytes_recv

    # Display System Stats
    def display_stats(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for each update
            print("System Monitor")
            print("-----------------------------")

            # CPU Usage
            cpu = self.cpu_usage()
            print(f"CPU Usage: {cpu}%")

            # Memory Usage
            mem_percent, mem_used, mem_total = self.memory_usage()
            print(f"Memory Usage: {mem_percent}% ({self.bytes_to_human(mem_used)} used of {self.bytes_to_human(mem_total)})")

            # Network Usage
            net_sent, net_recv = self.network_usage()
            print(f"Network Sent: {self.bytes_to_human(net_sent)} | Network Received: {self.bytes_to_human(net_recv)}")

            print("\nPress Ctrl+C to exit.")
            time.sleep(8)  # Pause before updating

    # Convert bytes to human-readable format
    def bytes_to_human(self, size):
        power = 2**10
        n = 0
        power_labels = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

        while size > power:
            size /= power
            n += 1
        return f"{size:.2f} {power_labels[n]}"

if __name__ == "__main__":  # Correct name block
    monitor = SystemMonitor()
    try:
        monitor.display_stats()
    except KeyboardInterrupt:
        print("\nSystem Monitor stopped.")
