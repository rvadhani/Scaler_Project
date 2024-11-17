
def handle_exception():
    try:
        print("A")
        val = 10/0

        print(val)
        print("B")

    except ZeroDivisionError:
        pass
        print("D")

    except Exception as e:

        print("C")




    finally:
        print("E")


if __name__ == "__main__":
    try:
        handle_exception()
    except Exception as e:

        print("G")
        raise
    except ZeroDivisionError:
        print("F")


    finally:
        print("H")


