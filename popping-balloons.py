# GUESS THE COLOR OF THE LAST BALLOON

# Six options for input: Blue, Red, Yellow, Green, Orange, Violet.
balloons = {"Blue", "Red", "Yellow", "Green", "Orange", "Violet"}

i = input("""Guess the color of the last balloon:
""")
print("*" * 45)

bet_set = list(i)
bet_set = ''.join(bet_set)
bet_set = str.capitalize(bet_set)

if bet_set not in balloons:
    print("\n")
    print("""Wrong input! Choose between: 
        
        PRIMARY COLORS
    - Blue - Red - Yellow
        
        SECONDARY COLORS
    - Green - Orange - Violet""")
    print("\n")
    assert (bet_set in balloons), "Wrong input"

print("\n")
print("Let's start popping balloons!")
while len(balloons) > 1:
    balloons.pop()
    if len(balloons) == 1:
        print(balloons)
        result_str = list(balloons)
        result_str = ''.join(result_str)
    else:
        print(balloons)

print("\n")
print("- Your choice: ", bet_set)
print("- Last balloon: ", result_str)

if result_str == bet_set:
    print("""- Result: CONGRATS! YOU DID IT!""")
else:
    print("""- Result: WRONG! TRY AGAIN!""")
