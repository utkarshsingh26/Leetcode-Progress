class Solution:
    def fib(self, n: int) -> int:

        cache = {0:0, 1:1}

        def f(x):
            if x in cache:
                return cache[x]
            else:
                cache[x] = f(x-1) + f(x-2)
                return cache[x]
        
        return f(n)