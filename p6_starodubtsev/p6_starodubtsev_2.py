town = {
    'A': "Newfoundland",
    'B': "Nova Scotia",
    'C': "Prince Edward Island",
    'E': "New Brunswick",
    'G': "Quebec",
    'H': "Quebec",
    'J': "Quebec",
    'K': "Ontario",
    'L': "Ontario",
    'M': "Ontario",
    'N': "Ontario",
    'P': "Ontario",
    'R': "Manitoba",
    'S': "Saskatchewan",
    'T': "Alberta",
    'V': "British Columbia",
    'X': "Nunavut or Northwest Territories",
    'Y': "Yukon"
    }
s = input("Enter tree symbols")
s = s.upper()
if len(s)==3 and  s[0].isalpha() and s[2].isalpha() and s[1].isdigit():
    if s[0]=='D' or s[0]=='F' or s[0]=='I' or s[0]=='O' or s[0]=='Q' or s[0]=='U' or s[0]=='W' or s[0]=='Z':
        print("First letter hasn't town")
    else:
        if s[1]==0:
            d="it is a countryside of "
        else:
            d = "it is a urban of "
        d = d + town[s[0]]
        print(d)

else:
    print("You haven't entered right symbols")
