import sys

def parse_ip(str_ip):
    octs = list(map(int, str_ip.split('.')))
    return octs[0] << 24 | octs[1] << 16 | octs[2] << 8 | octs[3]

def ip_num_to_str(num_ip):
    return str(num_ip >> 24) + '.' + str(num_ip >> 16 & 0xFF) + '.' + str(num_ip >> 8 & 0xFF) + '.' + str(num_ip & 0xFF)

def wildcart(ip):
    return ip ^ 0xFFFFFFFF

def main():
   ip_addr = parse_ip(sys.argv[1])
   network_mask = parse_ip(sys.argv[2])
   network_address = ip_addr & network_mask
   broadcact_address = ip_addr | wildcart(network_mask)
   template = '{"networkAddress": "%s", "networkMask": "%s", "hostAddress": "%s"}' % (ip_num_to_str(network_address), ip_num_to_str(network_mask), '%s')
   hosts = ''
   for ip in range(network_address + 2, broadcact_address):
       hosts += template % (ip_num_to_str(ip)) + '\n'
   with open('output.txt', 'w') as text_file:
    text_file.write(hosts)

if __name__ == '__main__':
    main()