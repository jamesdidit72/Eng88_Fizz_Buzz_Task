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
