
"""
Luhn algorithm
https://en.wikipedia.org/wiki/Luhn_algorithm
Validating credit card:
Start double every second digit starting from the right

If doubling the number results in a number greater than 9 then subtract 9 from the product.

If the sum is divisible by 10, then number is valid (x % 10 == 0)

"""

class Card:
    
    def __init__(self, number):
        self.number = number
    
    def Validity(self):
            self.number = self.number.strip().replace(" ", "")
            self.number = list(map(int,self.number))
            if len(self.number)==16:
                self.number = self.number[::-1]
                self.number[1::2] = list(map(lambda x: x*2  if x*2<9 else(x*2-9), self.number[1::2]))
                if sum(self.number)%10==0:
                    print('Valid')
                else:
                    print('Invalid card number')
            else:
                print('You are missing something...')
card1 = Card("8273 1232 7352 0569")
card1.Validity()