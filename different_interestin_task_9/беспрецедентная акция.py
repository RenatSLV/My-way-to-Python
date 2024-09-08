def sort(price):
    price.sort(reverse=True)
    total_cost = 0

    for i in range(0,len(price),3):
        total_cost += price[i]
        if i + 1 < len(price):
            total_cost += price[i + 1]

    return total_cost

num = int(input())
price = list(map(int,input().split()))

print(sort(price))

