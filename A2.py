cost = float(input("enter a decimal value"))
sold = float(input("enter a decimal value"))

if cost<sold :
    profitorloss = sold-cost
    print("You made a profit of: ", profitorloss)

else:
    loss = sold - cost
    print("You make no profit you lost: ", loss)
    