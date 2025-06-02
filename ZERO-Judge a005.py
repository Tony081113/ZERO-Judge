#ZERO-Judge a005

n = int(input())
for i in range(n):
    ip = input().split()
    for j in range(len(ip)):
        ip[j] = int(ip[j])
    if ip[1] - ip[0] == ip[2] - ip[1] == ip[3] - ip[2]:
        print(*ip, ip[3] + (ip[3] - ip[2]))
    elif ip[1] / ip[0] == ip[2] / ip[1] == ip[3] / ip[2]:
        print(*ip, ip[3] * (ip[3] // ip[2]))