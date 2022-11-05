text = input()
a = ""
b = ""
c = ""
d = ""
e = ""
setA = "..#."
setB = ".#.#"
setD = ".#.#"
setE = "..#."
lastC = ""
for i in range(1,len(text)+1):
    setC = "#." + text[i-1] + "."
    if i % 3 == 0:
        a += "..*."
        b += ".*.*"
        c += "*." + text[i-1] + ".*"
        d += ".*.*"
        e += "..*."
    else:
        a += setA
        b += setB
        c += setC
        d += setD
        e += setE
if len(text) % 3 == 0 and len(text) <= 3:
    print(a + ".")
    print(b + ".")
    print(c)
    print(d + ".")
    print(e + ".")
elif len(text) % 3 == 0 and len(text) > 3:
    c = list(c)
    for i in range(len(c)):
        if i % 13 == 0:
            c[i] = ""
    c.insert(0,"#")
    for i in range(len(c)):
        lastC += c[i]
    print(a + ".")
    print(b + ".")
    print(lastC)
    print(d + ".")
    print(e + ".")
elif len(text) < 3:
    print(a + ".")
    print(b + ".")
    print(c + "#")
    print(d + ".")
    print(e + ".")
else:
    c = list(c)
    for i in range(len(c)):
        if i % 13 == 0:
            c[i] = ""
    c.insert(0,"#")
    for i in range(len(c)):
        lastC += c[i]
    print(a + ".")
    print(b + ".")
    print(lastC + "#")
    print(d + ".")
    print(e + ".")