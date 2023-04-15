

# Complete the solve function below.
def solve(s):
    capitalized = ""
    capitalize_next = True
    for c in s:
        if c.isspace():
            capitalized += c
            capitalize_next = True
        elif c.isalnum() and capitalize_next:
            capitalized += c.upper()
            capitalize_next = False
        else:
            capitalized += c.lower()
    return capitalized
