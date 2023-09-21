from random import choice as rd
from maps import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space


def spl(word):
    return [char for char in word]


abc = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
    " ": space
}
inp = input("WORD : ")

wo = spl(inp)
print('PATTERN : SPLIT :' + str(wo))
encl = []
for letter in wo:
    enc = rd(abc.get(letter))
    encl.append(enc)

final_string = ''

connectors = ('1B2', '01h2', 'i2j383h', 'nU4', '02er', '2o1jJHijwqj2', 'd?/e', '(83=-1u3')

for item in encl:
    final_string += rd(connectors) + item

print(final_string)
