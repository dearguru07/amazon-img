def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number

# Example Usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example Usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Example Usage
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")


def longest_subarray_with_sum_multiple_of_k(arr, k):
    # Map to store the first occurrence of the modulo result
    mod_map = {}
    prefix_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        # Update the prefix sum
        prefix_sum += arr[i]
        
        # Calculate modulo of the current prefix sum with k
        mod = prefix_sum % k
        
        # If the modulo is negative, adjust it to be positive
        if mod < 0:
            mod += k
        
        # If mod is 0, it means the subarray from the start to current index is divisible by k
        if mod == 0:
            max_len = i + 1
        elif mod in mod_map:
            # If mod has been seen before, calculate the length of the subarray
            max_len = max(max_len, i - mod_map[mod])
        else:
            # If mod hasn't been seen, store its first occurrence
            mod_map[mod] = i
    
    return max_len
