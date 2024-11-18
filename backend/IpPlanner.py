import ipaddress

class IPPlanner:
    @staticmethod
    def compute_ip_details( network, subnet_mask):
        """Compute network details based on network address and mask."""
        try:
            network_address = ipaddress.IPv4Network(f"{network}/{subnet_mask}", strict=False)
            return {
                "Network Address" : str(network_address.network_address),
                "Broadcast Address" : str(network_address.broadcast_address),
                "Number of available Hosts" : len(list(network_address.hosts())),
                "Available Hosts": list(network_address.hosts())
            }
        except ValueError as e:
            return str(e)
    @staticmethod
    def menu():
        print("\nIP Planner")
        print("Enter network address and subnet mask to calculate details.")

    def run(self):
        while True:
            self.menu()
            network = input("Enter Network Address (e.g., 192.168.1.0): ")
            subnet_mask = input("Enter Subnet Mask (e.g., 24): ")

            result = self.compute_ip_details(network, subnet_mask)
            if isinstance(result, dict):
                print("\n--- IP Details ---")
                for key, value in result.items():
                    print(f"{key}: {value}")
            else:
                print(f"Error: {result}")

            choice = input("Do you want to calculate again? (yes/no): ")
            if choice.lower() != 'yes':
                break
