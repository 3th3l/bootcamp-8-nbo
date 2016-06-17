
primes = [2]

def prime_numbers(n):
		if num > 1:
			for i in range(3,num):
				if (num % i) == 0:
					break
       			else:
       				primes.append(num)
			return primes