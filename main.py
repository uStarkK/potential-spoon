def sieve_of_eratosthenes(limit):
    prime = [True for _ in range(limit + 1)]
    p = 2
    while (p * p <= limit):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, limit + 1) if prime[p]]

# Example usage:
limit = 1000000
print(f"Prime numbers up to {limit}:")
sieve_of_eratosthenes(limit)
