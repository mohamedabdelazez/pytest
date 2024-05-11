def get_host_bits(num_hosts):
    # Calculates the number of host bits required for a given number of usable hosts.

    if num_hosts < 2 or num_hosts > 2**32 - 2:
        raise ValueError("Number of hosts must be between 2 and 2**32 - 2")

    # Find the smallest 'host' value such that 2^host - 2 is greater than or equal to num_hosts
    host = 0
    while 2**host - 2 < num_hosts:
        host += 1
    return host

def get_subnet_mask(host_bits):
    if host_bits < 1:
        raise ValueError("Number of hosts must be greater than or equal to 1")

    # Calculate the subnet mask based on host bits
    subnet_mask_binary = "1" * (32 - host_bits) + "0" * host_bits

    # Convert subnet mask binary to dotted decimal
    subnet_mask_octets = []
    for i in range(0, len(subnet_mask_binary), 8):
        subnet_mask_octet = int(subnet_mask_binary[i:i+8], 2)
        subnet_mask_octets.append(str(subnet_mask_octet))
    subnet_mask_dotted = ".".join(subnet_mask_octets)

    # Calculate CIDR prefix length
    cidr_prefix = 32 - host_bits
    return subnet_mask_binary, subnet_mask_dotted, cidr_prefix

def get_subnet_details(num_hosts, network_address, convert_to_binary=False):
    host_bits = get_host_bits(num_hosts)
    subnet_mask_binary, subnet_mask_dotted, cidr_prefix = get_subnet_mask(host_bits)

    # Convert network address to binary if requested
    if convert_to_binary:
        network_address_binary = ''.join([bin(int(x))[2:].zfill(8) for x in network_address.split('.')])

        # Perform bitwise AND operation between network address and subnet mask
        subnet_address_binary = ''.join(str(int(network_address_binary[i]) & int(subnet_mask_binary[i])) for i in range(32))

        # Convert subnet address binary to dotted decimal
        subnet_address_octets = []
        for i in range(0, len(subnet_address_binary), 8):
            subnet_address_octet = int(subnet_address_binary[i:i+8], 2)
            subnet_address_octets.append(str(subnet_address_octet))
        subnet_address_dotted = ".".join(subnet_address_octets)

        # Calculate broadcast IP
        broadcast_ip_binary = subnet_address_binary[:-host_bits] + '1' * host_bits
        broadcast_ip_dotted = '.'.join(str(int(broadcast_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

        # Calculate first valid IP
        first_valid_ip_binary = subnet_address_binary[:-host_bits] + '0' * (host_bits - 1) + '1'
        first_valid_ip_dotted = '.'.join(str(int(first_valid_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

        # Calculate last valid IP
        last_valid_ip_binary = broadcast_ip_binary[:-1] + '0'
        last_valid_ip_dotted = '.'.join(str(int(last_valid_ip_binary[i:i+8], 2)) for i in range(0, 32, 8))

        # Calculate the number of valid IPs
        num_valid_ips = 2 ** host_bits - 2

        return (host_bits, subnet_mask_binary, subnet_mask_dotted, cidr_prefix, 
                network_address_binary, subnet_address_binary, subnet_address_dotted,
                first_valid_ip_binary, first_valid_ip_dotted,
                last_valid_ip_binary, last_valid_ip_dotted,
                broadcast_ip_binary, broadcast_ip_dotted,
                num_valid_ips)
    else:
        return host_bits, subnet_mask_binary, subnet_mask_dotted, cidr_prefix

# User input
num_hosts = int(input("Enter the number of usable hosts: "))
network_address = input("Enter the network address (e.g., 10.50.88.0): ")

convert_to_binary = True
(host_bits, subnet_mask_binary, subnet_mask_dotted, cidr_prefix, 
 network_address_binary, subnet_address_binary, subnet_address_dotted,
 first_valid_ip_binary, first_valid_ip_dotted,
 last_valid_ip_binary, last_valid_ip_dotted,
 broadcast_ip_binary, broadcast_ip_dotted,
 num_valid_ips) = get_subnet_details(num_hosts, network_address, convert_to_binary)

print(f"Number of host bits required for {num_hosts} usable hosts: {host_bits}")
print(f"Subnet mask (dotted decimal): {subnet_mask_dotted}")
print(f"CIDR prefix length: /{cidr_prefix}")
print(f"Subnet address (dotted decimal): {subnet_address_dotted}")
print(f"First valid IP (dotted decimal): {first_valid_ip_dotted}")
print(f"Last valid IP (dotted decimal): {last_valid_ip_dotted}")
print(f"Broadcast IP (dotted decimal): {broadcast_ip_dotted}")
print(f"Number of valid IPs: {num_valid_ips}")
