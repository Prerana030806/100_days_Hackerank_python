from collections import Counter
# Number of shoes
X = int(input())
# Shoe sizes in the shop
shoe_sizes = list(map(int, input().split()))
# Number of customers
N = int(input())
# Inventory using Counter
inventory = Counter(shoe_sizes)
earnings = 0
# Process each customer
for _ in range(N):
    size, price = map(int, input().split())
    if inventory[size] > 0:   # Shoe available
        earnings += price
        inventory[size] -= 1  # Reduce stock
print(earnings)
