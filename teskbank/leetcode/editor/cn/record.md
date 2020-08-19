# recode
1. 最大公约数
```python
def gcd(a, b):
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a % b
    return a
```
2. 