def fahrenheit_to_celcius():
    print('Press 1 to F-C or 2 to C-F:', end=" ")
    check=int(input())
    if check==1:
        x=float(input())
        x=((x-32)*5)/9
        return x
    elif check==2:
        x=float(input())
        x=(x*9/5)+32
        return x
    else:
        return "Wrong choce"
print(fahrenheit_to_celcius())