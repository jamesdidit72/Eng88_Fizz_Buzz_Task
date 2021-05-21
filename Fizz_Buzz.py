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