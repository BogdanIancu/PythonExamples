
x = int(input("Insert a value:"))
try:
    print("Starting")

    if x > 1000:
        raise OverflowError
    else:
        list = [1,2,3]
        result = 3/x
        print("Result is "+str(result))

        value = list[x]
        print("The selected value is "+str(value))

except ZeroDivisionError as e:
    print("Avoid 0 !")
except OverflowError:
    print("Stop !")
except:
    print("We have a bug !")
finally:
    print("The end")
