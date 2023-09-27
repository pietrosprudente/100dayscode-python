print("Welcome to the tip counter")
b = float(input("What was the total bill $"))
t = int(input("How much tip would you like to give?(Do not add %) 10, 12, or 15"))
p = int(input("How many Humans do you want to split the bill"))
tp = t / 100
tta = b * tp
tb = b + tta
bpp = tb / p
final = round(bpp, 2)
print(f'Each person should pay: ${final}')

