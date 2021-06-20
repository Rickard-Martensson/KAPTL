# https://kth.kattis.com/problems/longincsubseq

# Authors: Andreas Wallström <awallst@kth.se>, Rickard Mårtensson <rmarte@kth.se>


import lis

import sys

for line in sys.stdin:
    N = int(line)
    vec = [int(s) for s in input().split()]

    indices = lis.lis(vec)
    print(len(indices))
    print(" ".join(map(str, indices)))
