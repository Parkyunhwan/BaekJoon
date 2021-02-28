n, m, k = map(int, input().split())

except_intern = n + m - k
result = 0
for m_val in range(1, m + 1):
    n_val = 2 * m_val
    if n_val <= n:
        sm = n_val + m_val
        if except_intern >= sm:
            result = m_val
print(result)