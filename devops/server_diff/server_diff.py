server1 = {
    "hostname": "server1",
    "ip": "192.168.1.1",
    "port": 22,
    "environment": "prod",
}

server2 = {
    "hostname": "server2",
    "ip": "192.168.1.2",
    "port": 22,
    "environment": "stage",
}

def compare_servers(server1, server2):
    found = False
    print('\nDifferences:\n')
    for key in server1:
        if server1[key] != server2[key]:
            found = True
            print(f'{key.upper()}: {server1[key]} vs {server2[key]}\n')
    if not found:    
        print('No differences found')
            

compare_servers(server1, server2)