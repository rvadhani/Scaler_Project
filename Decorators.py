

def decr(func):

    def wrapper(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Good Afternoon")

    return wrapper

def decr1(func):

    def wrapper(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Good Afternoon")

    return wrapper


def is_admin(func):

    def wrapper(is_admin_value,*args, **kwargs):
        if not is_admin_value:
            print("not admin")
            return False
        return func(*args,**kwargs)
    return wrapper


# below is similar to decr1(decr(print_name(name)))

@decr1
@decr
def print_name(name):
    print(name)

def print_name1(name):
    print("hello " + name)

@is_admin
def print_name3(name):
    print("hi", name)

if __name__ == '__main__':
    print_name('Rohit')
    print_name1('Dipti')
    print_name3(False,'Vishal')

# Args and kwargs :https://www.scaler.com/topics/python/args-and-kwargs-in-python/
