prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.10, 0.20, 0.15, 0.05]
for i in range(len(prices)):
    price = prices[i]
    discount = discounts[i]
    prices[i] = price * (1 -discount)
    print(f'Updated price at index {i}: ${prices[i]:.2f}')