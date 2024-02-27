class Interchange_values:
    """Swaps the values of two variables.

  Args:
    x: The first variable.
    y: The second variable.
  """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def swap(self, x, y):
        temp = self.x
        self.x = self.y
        self.y = temp


def main():
  """The main function."""

  x = 1
  y = 2

  # Call the swap function.
  my_object = Interchange_values(x, y)
  my_object.swap(x, y)


  # Print the values of x and y.
  print(my_object.x)
  print(my_object.y)

if __name__ == '__main__':
  main()
