def maior_primo(n):
    count = 2
    if n == 2:
        return True
    while n % count != 0 and count <= n/2:
        count += 1
    if n % count == 0:
        return False
    else:
        return True

a = int(input())
m = 0 
i = 0

while i <= a:
    if maior_primo(i):
        m = i
    i += 1 

print(m)