"""
shoma tooye in tamrin yek adad vared mikonid va barname
hameye adad ghabl adad shoma ro ba khode adad jam mikone.
"""
def bernoli(num):
    if num > 0:
        result = num + bernoli(num - 1)
        print(result)
    else:
        result = 0
        print(result)
    return result
number = int(input("Yek adad vared konid : "))
bernoli(number)