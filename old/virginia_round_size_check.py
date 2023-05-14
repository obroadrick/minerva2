from round_size_bravo import round_size_bravo

alpha=.1
p_1 = 2413568/(2413568+1962430+64761+19765)
p_0 = .5
print(p_1)
rsize = round_size_bravo(1, 0, 0, p_1, p_0, alpha, sprob=.8, lower=1, upper=10**100, skip=10000)

print(rsize)
print(rsize * (2413568+1962430+64761+19765)/(2413568+1962430) )

"""
alpha=.1
p_1 = 14487/(13061+14487)
p_0 = .5
print(p_1)
rsize = round_size_bravo(1, 0, 0, p_1, p_0, alpha, sprob=.85, lower=1, upper=10**100, skip=10000)

print(rsize)
print(rsize / ((13061+14487)/27585))
"""

