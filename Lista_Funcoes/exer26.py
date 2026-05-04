def erro(n):
    return n * erro(n - 1)

# O erro é que não tem caso base, então irá chamar infinitamente RecursionError
# O correto seria:
def erro(n):
    if n == 0:
        return 1
    return n * erro(n - 1)