class toRoman:
    @staticmethod
    def convertNum(num):
        # Check if input is an integer
        if not isinstance(num, int):
            # raise TypeError('"' + str(num) + '" is not a valid input. Input an integer between 1 and 3999.')
            return -1

        # Check if input is within the allowed range
        if num > 3999 or num < 1:
            # raise ValueError('Number "' + str(num) + '" is out of range. Input an integer between 1 and 3999.')
            return -2

        # The max allowed number to be converted is 3999
        numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000] 
        symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"] 

        # Begin dividing with the largest number in the array
        counter = len(numbers) - 1
        # Initialize a string to return at end of conversion
        romanStr = ""

        while num > 0:
            quotient = num // numbers[counter]
            # Set the remainder to be the new number to be divided and repeat the process
            num = num % numbers[counter]
            romanStr += symbols[counter] * quotient
            counter-=1

        return romanStr

def test_file1():
    assert 1==1

if __name__ == "__main__":
    # Passed Test Cases
    print(toRoman.convertNum(1))
    print(toRoman.convertNum(100))
    print(toRoman.convertNum(541))
    print(toRoman.convertNum(3999))

    # Failed Test Cases
    #toRoman.convertNum(5000)
    #toRoman.convertNum(-123)
    #toRoman.convertNum("#")