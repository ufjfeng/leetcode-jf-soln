"""
Description:
    Count the number of prime numbers less than a non-negative number, n.

Credits:
    Special thanks to @mithmatt for adding this problem and creating all test
    cases.

Hint:
    Let's start with a isPrime function. To determine if a number is prime, we
    need to check if it is not divisible by any number less than n. The runtime
    complexity of isPrime function would be O(n) and hence counting the total
    prime numbers up to n would be O(n2). Could we do better?
    
    As we know the number must not be divisible by any number > n / 2, we can
    immediately cut the total iterations half by dividing only up to n / 2.
    Could we still do better?
    
    Let's write down all of 12's factors:
        2 × 6 = 12
        3 × 4 = 12
        4 × 3 = 12
        6 × 2 = 12

    As you can see, calculations of 4 × 3 and 6 × 2 are not necessary.
    Therefore, we only need to consider factors up to √n because, if n is
    divisible by some number p, then n = p × q and since p ≤ q, we could derive
    that p ≤ √n.
    
    Our total runtime has now improved to O(n1.5), which is slightly better. Is
    there a faster approach?
    
    public int countPrimes(int n) {
       int count = 0;
       for (int i = 1; i < n; i++) {
          if (isPrime(i)) count++;
       }
       return count;
    }
    
    private boolean isPrime(int num) {
       if (num <= 1) return false;
       // Loop's ending condition is i * i <= num instead of i <= sqrt(num)
       // to avoid repeatedly calling an expensive function sqrt().
       for (int i = 2; i * i <= num; i++) {
          if (num % i == 0) return false;
       }
       return true;
    }
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime=[True]*max(n,2)
        isPrime[0], isPrime[1] = False, False
        x=2
        while x<n:
            if isPrime[x]:
                m=x**2
                while m<n:
                    isPrime[m]=False
                    m+=x
            x+=1
        return sum(isPrime)

"""
too slow, time limit exceeded for n=999983
    def countPrimes(self, n):
        if n<=2:
            return 0
        primes=[2]
        for i in range(3,n):
            lim=i**0.5
            for j in primes:
                if j>lim:
                    primes.append(i)
                    break
                elif i%j==0:
                    break

        return len(primes)
"""
