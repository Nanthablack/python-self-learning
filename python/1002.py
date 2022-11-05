def toRoman(num):
    out = ""
    m = {
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
    }
    for t in m.keys():
        while num>=t:
            out+=m[t]
            num-=t
    return out
n = int(input())
o = ""
for i in range(1,n+1):
    o+=toRoman(i)
print(f"{o.count('I')} {o.count('V')} {o.count('X')} {o.count('L')} {o.count('C')}")