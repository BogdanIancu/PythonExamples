def try_catch_function(x,*argv):
    try:
        print(argv[0])
    except Exception:
        print("We have an error")
    finally: 
        print("function finished execution")


try_catch_function(7)
