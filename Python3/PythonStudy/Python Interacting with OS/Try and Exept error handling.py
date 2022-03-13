def character_frequency(filename):
    try:
        f = open(filename)
    except OSError:
        return None


character_frequency("file1.txt")


# you can raise your own Errors using the raise key word

def validiatenum(username,minlen):
    assert type(username) == str,"username must be a string"
    if minlen <1 :  raise ValueError("minlen must be positive number")
    print(username)



validiatenum(1,-1)