import json
import nmap3
import socket

# nmap = nmap3.Nmap()
# os_results = nmap.nmap_os_detection("10.0.0.0/24")
# router_results = json.dumps(results, indent=4)
# print(router_results)

# TODO Grabs open ports for ISP router
# nmap = nmap3.Nmap()
# results = nmap.scan_top_ports("<public_ip>")
# for data in results['<public_ip>']['ports']:
#     if data['state'] != 'closed':
#         print(data)

# results = nmap.nmap_subnet_scan("10.0.0.0/24")

# router_results = nmap.nmap_subnet_scan("<public_ip>")
# print(router_results)


# TODO grabs all network IP's that are up
def query_listening_ips(network_subnet):
    nmaph = nmap3.NmapHostDiscovery()
    results = nmaph.nmap_no_portscan(network_subnet)
    scan_ip_list = []
    for ip_address in results:
        try:
            if socket.inet_aton(ip_address):
                if results[ip_address]['state']['state'] == 'up':
                    # print(f'{ip_address}, {results[ip_address]}')
                    scan_ip_list.append(ip_address)
        except OSError as error:
            pass
            # print(f'non ip address {error}')
    return scan_ip_list


def get_version(ip_list):

    try:
        for ip in ip_list:
            os_results = nmap.nmap_os_detection(ip)
            # print(f'{ip} {os_results}')
            # data = json.dumps(version_results, indent=4)
            # print(data)
            print(f'INFO FOR {ip}')
            print('---------------------------------')
            for os_data in os_results[ip]['osmatch']:
                print(f'{os_data}')
            print('---------------------------------')
            print(f'PORT DATA')
            for os_port_data in os_results[ip]['ports']:
                print(f'{os_port_data}')
            print('---------------------------------')
    except Exception as e:
        print('exception {e')


def scan_top_ports(scan_ip_list):
    # nmap = nmap3.Nmap()
    for ip in scan_ip_list:
        results = nmap.scan_top_ports(ip)
        for data in results[ip]['ports']:
            pass
            # print(data)
            # if data['state'] != 'closed':
            #     version = get_version(ip)
                # print(f'{ip} {data} {version}')
                # print(f'{ip} {version}')

                # data = json.dumps(results, indent=4)
                # print(data)


if __name__ == '__main__':
    nmap = nmap3.Nmap()
    subnet = "10.0.0.0/24"
    open_ip_list = query_listening_ips(subnet)
    print(f'got list {open_ip_list}')
    # scan_top_ports(ip_list)
    get_version(open_ip_list)