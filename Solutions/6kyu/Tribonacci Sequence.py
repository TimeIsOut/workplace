def tribonacci(signature, n):
    if n < len(signature):
        return signature[:n]
    for i in range(n - 3):
        signature.append(signature[-1] + signature[-2] + signature[-3])
    return signature