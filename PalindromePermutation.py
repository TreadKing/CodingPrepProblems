'''
Palindrome Permutation:

Given a String, write a function to check if it is a Permutation of a palindrome.

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat". "atco cta". etc.)

Notes:
- you must have an even number of characters per character
- only one char can be odd
- even is just the first one
- odd is both

'''

def palPerm(s):
    s = s.lower()
    seen = {}
    for char in s:
        if char in seen:
            seen[char] += 1
        elif char == ' ':
            continue
        else:
            seen[char] = 1

    odd = False
    for item in seen.values():
        if (len(s) % 2) == 0:
            if (item % 2) != 0:
                return False
        else:
            if (item % 2) != 0:
                if odd == False:
                    odd = True
                else:
                    return False
    return True

print(palPerm('Tact Coa '))