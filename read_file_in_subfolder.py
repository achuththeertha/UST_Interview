import os

def read_file(filename):
  """Reads a file and returns its contents."""
  with open(filename, "r") as f:
    return f.read()

def main():
  """Reads a file from a sub-folder and prints its contents."""
  # Get the path to the sub-folder.
  subfolder_path = os.path.join(os.getcwd(), "subfolder")

  # Get the path to the file in the sub-folder.
  file_path = os.path.join(subfolder_path, "file.txt")

  # Read the file and print its contents.
  file_contents = read_file(file_path)
  print(file_contents)

if __name
