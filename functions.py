# Functions & Fibonacci Sequence
# Question
# Write a Python program to generate the Fibonacci sequence up to a specified term n. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.
#We have provided  you with in-complete code, from the Knowledge learned from week 1 to week 3 please complete the missing parts to achieve the goal of the question.
def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    return n
  else:
    a, b = 0, 1 # Initializing the 1st two terms of the sequence.
    for _ in range(2, n + 1):
      c = a + b
      a, b = b, c # updated the value of a and b for the nxt iteration.
    return b # Returning the last term of the sequence.

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms):
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)
# Printed the generated Fibonacci sequence.
