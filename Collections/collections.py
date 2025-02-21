from collections import deque
d = deque([1, 2, 3])
d.append(4)  # deque([1, 2, 3, 4])
d.popleft()  # 1 → deque([2, 3, 4])

from collections import Counter
c = Counter([1, 2, 2, 3, 3, 3])
print(c)  # Counter({3: 3, 2: 2, 1: 1})
print(c.most_common(2))  # [(3, 3), (2, 2)]

from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  # defaultdict(<class 'int'>, {'a': 1})