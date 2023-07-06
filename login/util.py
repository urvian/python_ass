def read_credentials():
    try:
        with open("login_back.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("An error occurred while opening the file. Our deep apologies.")
    except Exception:
        raise Exception("An error has occurred.")