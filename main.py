import Program1
import Program2


def main():

    value = 1221
    class_obj1 = Program2.Integer(value)
    print(class_obj1.is_palindrome())

    x = 3
    y = 4
    class_obj2 = Program1.Interchange_values(x, y)
    class_obj2.swap(x, y)
    print("Value of x = ", class_obj2.x)
    print("Value of x = ", class_obj2.y)


if __name__ == "__main__":
    main()
