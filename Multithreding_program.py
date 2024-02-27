import threading

def swap(a, b):
  temp = a
  a = b
  b = temp
  print("Swapped Numbers are ", a, b)

def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

# Create two threads, one for each program
t1 = threading.Thread(target=swap, args=(1, 2))
t2 = threading.Thread(target=is_palindrome, args=(121,))

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

# Print the results
print("Is 121 a palindrome?", is_palindrome(121))
