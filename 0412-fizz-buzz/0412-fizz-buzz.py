class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = ["x"] * n
        for i in range(1, n + 1):
            div3 = i % 3 == 0
            div5 = i % 5 == 0
            if div3 and div5:
                lst[i - 1] = "FizzBuzz"
            elif div3:
                lst[i - 1] = "Fizz"
            elif div5:
                lst[i - 1] = "Buzz"
            else:
                lst[i - 1] = str(i)

        return lst
