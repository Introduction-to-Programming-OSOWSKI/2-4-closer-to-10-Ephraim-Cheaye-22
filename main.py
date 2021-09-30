#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if abs(x) < abs(y):
        return x

    elif abs(x) > abs(y):
        return y 

    else:
        return 0

print (close10(5,12))