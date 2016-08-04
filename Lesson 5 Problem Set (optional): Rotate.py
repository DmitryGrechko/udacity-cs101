# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(name, n):
    rotated = ''
    for i in name:
        rotated += (shift_n_letters(i,n))
    return rotated

def shift_n_letters(letter, n):
    if ord(letter) == 32:
        return chr(ord(letter))
    elif ord(letter) + n >= 123:
        return chr(97 + n - (123 - ord(letter)))
    elif ord(letter) + n < 97:
        return chr(123 + n - (97 - ord(letter)))
    return chr(ord(letter) + n)

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???