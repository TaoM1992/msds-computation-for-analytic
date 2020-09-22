"String formatting examples"

from math import tau

# Signficant digits
print(f"τ: {tau:.4%}")

# Print only 2 deciminals
print(f"{tau:.2f}")

# Print as integer
print(f"{tau:.0f}")

# Currency
print(f"${3.66666:.2f}")

# Padding
day = 1
print(f"{day:04}") # Padd to 4 places with zeros

# Align
print("Options: \t {:>6} {:>6} {:>6} {:>6}".format(*"A B C D".split()))

# Center text
print(f"{'foo':^10}") #=> ' foo '

# Unpack list, then format
data = [1, 2, 3, 4]
print("The numbers are {}, {}, {}, and {}".format(*data))

# Pretty print function name
def my_function():
    pass

print(f" ".join(my_function.__name__.title().split("_")))

# Unicode names
print(f' \N{Hatching Chick} ') # 🐣
print(f' \N{long rightwards arrow} ')  # ⟶
print(f' \N{Vulgar Fraction One Quarter} ') # ¼ 

# Replace datetime.stftime()
print(f"{datetime.now():%m/%d/%y}") #=> '05/15/19'

# Show numbers in another base / notation
print(f"{878:b}") #=> '1101101110'

print(f"{878:x}") #=> '36e'

print(f"{878:e}") #=> '8.780000e+02'

