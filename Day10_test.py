D = sorted(int(i) for i in open('data/Day10Input'))

# Diffs between adjacent items:
δ = [i-j for i,j in zip(D, [0]+D)] + [3]

# Lengths between two diffs of 3:
Δ = [1+p for p,d in enumerate(δ) if d==3]
L = [hi-lo-1 for lo, hi in zip([0]+Δ[:-1], Δ)]

𝓣 = [1, 1, 2] # seed for Tribonacci sequence
while len(𝓣) <= max(L): 𝓣 += [sum(𝓣[-3:])]

import numpy
print('Part 1:', len(Δ)*(len(δ)-len(Δ)),
      '\nPart 2:', numpy.prod([𝓣[l] for l in L]))