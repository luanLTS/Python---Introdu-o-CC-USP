def vogal(char):
    vogais= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    while i < len(vogais): 
        if char == vogais[i]:
            return True
        else:
            return False
    i += 1

c = input()
print(vogal(c))