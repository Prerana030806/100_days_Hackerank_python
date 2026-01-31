def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    
    for i in range(size-1, -1, -1):
        row = letters[size-1:i:-1] + letters[i:size]
        print("-".join(row).center(width, "-"))
        
    for i in range(1, size):
        row = letters[size-1:i:-1] + letters[i:size]
        print("-".join(row).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
