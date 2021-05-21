# Fizzbuzz
## The Problem

"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

### NOTE -> Must be in class and method format

#### First iteration
```python
class Fizzbuzz:
    def buzz_of_the_fizz(self, required_range):
        for number in range(required_range + 1):

            if number % 3 == 0 and number % 5 == 0:
                print('FizzBuzz')
            elif number % 3 == 0:
                print('Fizz')
            elif number % 5 == 0:
                print('Buzz')
            else:
                print(number)
fizzbuzz_checker = Fizzbuzz()
fizzbuzz_checker.buzz_of_the_fizz(100)
```

#### second iteration
```python
class Fizzbuzz:  # initialisation of the class
    def buzz_of_the_fizz(self, required_range):  # initialisation of the function, self is required.
        for number in range(required_range + 1):  # looping through the variable + 1

            if number % 3 == 0 and number % 5 == 0:  # if the current value of number can be divided by 3 and 5 with no remainder, print
                print('FizzBuzz')
            elif number % 3 == 0:  # if the current value of number can be divided by 3 with no remainder, print
                print('Fizz')
            elif number % 5 == 0:  # if the current value of number can be divided by 5 with no remainder, prin
                print('Buzz')
            else:
                print(number)  # print the value of number


fizzbuzz_checker = Fizzbuzz()  # sets the class as a local variable
fizzbuzz_checker.buzz_of_the_fizz(100) # calls the class and sets the variable to 100
```