#Challenge: 21-shortest_word
#Difficulty:  Intermediate
#Prompt:
#- Write a function called shortest_word that accepts a single string as argument.
#- The shortest_word function should return the length of the shortest word(s). String will never be empty, and you do not need to account for different data types.
#Example:
#shortest_word("I don't think that word means what you think it means") // => '1'

# Your solution for 21-shortest_word here:

def shortest_word(s): 
    pass

shortest_word_string="I don't think that word means what you think it means"
print(f'shortest_word solution: \n > {shortest_word(shortest_word_string)} = 1')

#Challenge: 22-reverse_a_string
#Difficulty:  Intermediate
#Prompt:
#- Reverse a string manually. Don't use s[::-1] (even though that's awesome). Create a new variable storing an empty string and add the letters from the first string one by one. The for loop should iterate over the length of the string and you should access letters individually.

#Hint:
## Python offers several ways to reverse a String. This is a classic thing that lots of people want to do. It's probably easy to look up this answer on Stack Overflow.

# Your solution for 22-reverse_a_string here:

def reverse_a_string(s):
    new_string = ''

    for char in s:
        new_string = char + new_string

    return (new_string)
    
backwards_string="snaem ti kniht uoy tahw snaem drow taht kniht t'nod I"
print(f'reverse_a_string solution: \n > {reverse_a_string(backwards_string)} = {shortest_word_string}')

#Challenge: 23-shortest_word
#Difficulty:  Intermediate
#Prompt:
#- Write a function called sum_of_minimums that accepts a single list as an argument.
#- Given a 2D list of size m * n, your task is to find the sum of the minimum value in each row.
#- You will always be given non-empty lists containing positive values.

# Your solution for 23-sum_of_minimums here:

def sum_of_minimums(list):
    # your lovely code goes here!
    min_array = []
    for i in range(0, len(list)):
        # an empty list for new array
        
        sub_arrays = list[i]
        min_numbers = min(sub_arrays)
        min_array.append(min_numbers)


    # min_num = min(list)
    return sum(min_array)

my_list = [ [1,2,3,4,5], [5,6,7,8,9], [20,21,34,56,100] ]
print(f'sum_of_minimums solution: \n > {sum_of_minimums(my_list)} = 26')

#Challenge: 24-palindrome_number
#Difficulty:  Basic
#Prompt:
#- Write a function called palindrome_number that, given an integer x, return true if x is a palindrome, and false otherwise.

# Your solution for 24-palindrome_number:

def is_palindrome(x):
        x_array = list(str(x))
        x_array_reverse = list(str(x))
        x_array_reverse.reverse()
        if x_array == x_array_reverse:
            return True
        return False

print(f'is_palindrome solution: \n > {is_palindrome(101)} = True \n > {is_palindrome(10)} = False')

#Challenge: 25-fizz_buzz
#Difficulty:  Basic
#Prompt:
#- Write a function called fizz_buzz that, given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

#Example:
#Input: n = 15
#Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Your solution for 25-fizz_buzz:

def fizz_buzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for i in range(1, n + 1):
            if (i % 3 == 0) and (i % 5) == 0:
                results.append("FizzBuzz")
            elif (i % 3) == 0:
                results.append("Fizz")
            elif (i % 5) == 0:
                results.append("Buzz")
            else:
                results.append(str(i))
        return results

n=15
fizz_buzz_res=['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
print(f'fizz_buzz solution: \n > {fizz_buzz(n)} \n > = \n > {fizz_buzz_res}')

#Challenge: 26-alphabetical
#Difficulty:  Intermediate
#Prompt:
#- Create a function that takes a string and returns the string with the letters in alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation symbols will not be included in the string.

#```
#Give me a string to alphabetize
#supercalifragilisticexpialidocious
#Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
#```

#Hint:
## You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for lists and strings instead.

# Your solution for 26-alphabetical here:

def alphabetical(s): 

    word_li = list(word)

    word_li.sort()

    new_string = ''.join(word_li)

    return new_string

word = 'supercalifragilisticexpialicosious'
print(f'alphabetical solution: \n > {alphabetical(word)} = aaaccceefgiiiiiiillloopprrsssstuux')

#Challenge: 27-two_sum
#Difficulty:  Intermediate
#Prompt:
#- Write a function called two_sum that given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#Example:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Your solution for 27-two_sum here:

def two_sum(nums, target): 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
nums=[2,7,11,15]
target=9
print(f'two_sum solution: \n > {two_sum(nums, target)} = [0, 1]')

#Challenge: 28-roman_to_integer
#Difficulty:  Intermediate
#Prompt:
#- Write a function called roman_to_int that, given a Roman numeral, convert it to an integer.

#- https://en.wikipedia.org/wiki/Roman_numerals

#Example 1:
#Input: s = "III"
#Output: 3
#Explanation: III = 3.

#Example 2:
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.

# Your solution for 28-roman_to_integer here:

def roman_to_int(s):
        map_romans = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000
        }
        num = 0
        value = 0
        for letter in s[::-1]:
            preValue = value
            value = map_romans.get(letter)
            if value <= preValue:
                if (preValue == value * 5 or preValue == value * 10):
                    num -= value
                else:
                    num += value
            else:
                num += value
        return num 
		
r='LVIII'
print(f'roman_to_int solution: \n > {roman_to_int(r)} = 58')