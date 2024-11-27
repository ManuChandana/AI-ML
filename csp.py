import itertools
def solve(words, result):
    unique = ''.join(set(''.join(words) + result))
    if len(unique) > 10:
        return "No solution"
    for perm in itertools.permutations('0123456789', len(unique)):
        mapping = dict(zip(unique, perm))
        if any(mapping[w[0]] == '0' for w in words + [result]):
            continue
        to_num = lambda w: int(''.join(mapping[c] for c in w))
        if sum(map(to_num, words)) == to_num(result):
            return {w: to_num(w) for w in words + [result]}, mapping
    return "No solution"
words = input("Enter words: ").upper().split()
result = input("Enter result: ").upper()
print(solve(words, result))
