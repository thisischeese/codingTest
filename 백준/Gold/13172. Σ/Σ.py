import sys
import math

MOD = int(1e9 + 7)

def modinv(a, exp):
    if exp == 1:
        return a
    if exp % 2 == 0:
        half = modinv(a, exp // 2)
        return half * half % MOD
    else:
        return a * modinv(a, exp - 1) % MOD

M = int(sys.stdin.readline())
result = 0

for _ in range(M):
    n, s = map(int, sys.stdin.readline().split())
    g = math.gcd(n, s)
    n //= g
    s //= g

    result += s * modinv(n, MOD - 2) % MOD
    result %= MOD

print(result)
