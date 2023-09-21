inp = input('CODE : ')
from maps import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, space


connectors = ['1B2', '01h2', 'i2j383h', 'nU4', '02er', '2o1jJHijwqj2', 'd?/e', '(83=-1u3']

rem_connectors = inp

for x in connectors:
    print('[i] : REMOVING CONNECTOR : ' + x)

    remove = rem_connectors.replace(x, 'XSPLIT')
    rem_connectors = remove

print('[i] : REMOVE_CONNECTOR : ' + str(rem_connectors))
clean = rem_connectors.split('XSPLIT')

clean.remove('')

print('PATTERN : CLEAN : ' + str(clean))

alpha_map = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

reverse_map = {
    a: 'a',
    b: 'b',
    c: 'c',
    d: 'd',
    e: 'e',
    f: 'f',
    g: 'g',
    h: 'h',
    i: 'i',
    j: 'j',
    k: 'k',
    l: 'l',
    m: 'm',
    n: 'n',
    o: 'o',
    p: 'p',
    q: 'q',
    r: 'r',
    s: 's',
    t: 't',
    u: 'u',
    v: 'v',
    w: 'w',
    x: 'x',
    y: 'y',
    z: 'z',
    space: " "

}

DECRYPTED = ''
for letter in clean:
    for alphabet in alpha_map:
        if letter in alphabet:
            try:
                DECRYPTED += reverse_map.get(alphabet)
            except TypeError:
                print('[w] : Skipping ' + letter)
                print('[e] : Error : ' + letter + ' : Not in Map')
        else:
            pass
print("================================")
print(DECRYPTED)
