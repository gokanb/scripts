import subprocess

online = []
offline =[]

with open("ip_list.txt", "r") as file:
    ip_adresses=file.readlines() #.split("\n")

for ip in ip_adresses:
    send_ping = subprocess.call(f'ping -c 4 {ip}')

    if(send_ping) == 0:
        online.append(ip)

    else:
        offline.append(ip)

with open("reach.txt" , "w") as file:
    for x in online:
        file.write(x +"\n")

with open("not_reach.txt", "w") as file:
    for y in offline:
        file.write(y +"\n")