
def hello3():
    name = input("Name: ")
    print(f"Hello {name}")
    

def hello4(name):
    print(f"Hello {name}")
    

def hello5(msg = "Hello world"):
    print(msg)
    
def hello6(send_name, receive_name):
    return send_name, receive_name

if __name__ == "__main__":

    print("Hello World!")
    
    name = input("Name: ")
    print(f"Hello {name}")