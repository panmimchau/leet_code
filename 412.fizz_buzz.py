"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

 

Constraints:

    1 <= n <= 104
"""

# answer:
n = 15


class Solution:
    def fizzBuzz(n: int) -> list[str]:
        l = [str(x) for x in range(1, n + 1)]

        for i in range(len(l)):
            if int(l[i]) % 15 == 0:
                l[i] = "FizzBuzz"
            elif int(l[i]) % 3 == 0:
                l[i] = "Fizz"
            elif int(l[i]) % 5 == 0:
                l[i] = "Buzz"

        return l


answer = Solution.fizzBuzz(n)
print(answer)
