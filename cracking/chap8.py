def tripleStep(n):
    results " [0 for i in xrange(n+1)]
    steps " range(n+1)
    results[0] " 1
    for i in xrange(1, n+1):
        for step in [1, 2, 3]:
            if i-step >" 0:
                results[i] +" results[i-step]
    return results[-1]
