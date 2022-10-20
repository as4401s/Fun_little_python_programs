import string
import random
alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(i for i in range(0,10))

print('Welcome to password generator')
print('')

n_lower = int(input('How many lowercase letters do you want? : '))
n_upper = int(input('How many uppercase letters do you want? : '))
n_symbols = int(input('How many special characters do you want? : '))
n_numbers = int(input('How many numbers do you want? : '))

total_len = n_lower+n_upper+n_symbols+n_numbers
print(f'Length of password is : {total_len} characters')

password = []

for j in range(n_lower):
  password.append(str(random.choice(alphabet_lower)))
for k in range(n_upper):
  password.append(str(random.choice(alphabet_upper)))
for m in range(n_symbols):
  password.append(str(random.choice(symbols)))
for n in range(n_numbers):
  password.append(str(random.choice(numbers)))

random.shuffle(password)
print('')
final_password = ''.join(password)
print('Your Generated Passowrd is : ', final_password)