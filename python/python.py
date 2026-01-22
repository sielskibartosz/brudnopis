from collections import Counter

X = 7
shoe_sizes = Counter(map(int, "1 3 4 4 5 6 1".split()))
print(shoe_sizes)
N = 3
total_price = 0
for i in range(N):
    size, price = list(map(int, input().split()))

    if shoe_sizes[size] != 0:
        total_price += price
        shoe_sizes[size] -= 1

print(total_price)