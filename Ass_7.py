def fileHandle(file):
    try:
        z=open(file,"a+")
        z.writelines(["Rollno:5\n","name:Urvi\n","class:TYIF"])
        z.seek(0)
        print(z.readlines())
    except FileNotFoundError:
        print("The exception is handled")
    except FileExistsError:
        print("The exception is handled")
    except IOError:
        print("The exception is handled")
    except Exception:
        print("The exception is handled")
    finally:
        print("This is the finally block")
# fileHandle("Sample1.txt")
fileHandle("src.txt")