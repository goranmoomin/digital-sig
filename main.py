temp1 = "FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551"
temp2 = "E45054EB5B1ABD976650F7F395BF51D0D8DD193E0174E7A14A1C8C127FBDF2DB"
temp3 = "09371E411284D26B4FAE3BD85B9545BBBFACE1FFE0868BD7701660A50C6E3F17"
temp4 = "B84ABC62455C570D5500186D83BFD1E1C23CB3135D4A32CE19B3DB61F1680EDC"
temp5 = "389FA4507CD536C67DB35B80B06AB0B0B034B7A5C67CF9A2D06ED00876D568F9"
temp6 = "1A2FC26DC7EA5A2A4748B7CB2B1EF193D96AB2C99F93092F69E63075B28D1278"

n = int(temp1, 16)
r = int(temp2, 16)
s1 = int(temp3, 16)
s2 = int(temp4, 16)
m1 = int(temp5, 16)
m2 = int(temp6, 16)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if abs(g) != 1:
        raise Exception("modular inverse does not exist")
    elif g == -1:
        return ((x % m) * (x % m) * a) % m
    else:
        return x % m


rinv = modinv(r, n)
k = modinv((s1 - s2), n) * (m1 - m2) % n

privateKey = ((s1 * k - m1) * rinv) % n
print(hex(privateKey))
