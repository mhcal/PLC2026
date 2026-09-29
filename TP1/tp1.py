import re

r = r"1*(0+1?)*"

# xs = ["", "a", "10", "01", "010", "110", "011", "100", "0010", "0110", "0101", "0000011"]

# for x in xs:
#     if re.fullmatch(r, x):
#         print(f"match: {x}")

while True:
    x = input("Enter a string (type 'q' to stop): ")
    if x.lower() == 'q':
        break
        
    if re.fullmatch(r, x):
        print(f"match: {x}")
    else:
        print(f"no match: {x}")
