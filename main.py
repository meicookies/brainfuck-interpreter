import sys
petunjuk_tersimpan = None
# kode = open("brainfuck.txt", 'r').read()
kode = ">,[>,]<[<]>[.>]"
sel, petunjuk, pengenal = [0], 0, 0
while petunjuk < len(kode):
    if kode[petunjuk] == ">":
        pengenal += 1
        if pengenal == len(sel): sel.append(0)
    elif kode[petunjuk] == "<":
        pengenal = 0 if pengenal <= 0 else pengenal - 1
    elif kode[petunjuk] == "+":
        sel[pengenal] = sel[pengenal] + 1 if sel[pengenal] <= 255 else 0
    elif kode[petunjuk] == "-":
        sel[pengenal] = sel[pengenal] - 1 if sel[pengenal] > 0 else 255
    elif kode[petunjuk] == "[":
        petunjuk_tersimpan = petunjuk
    elif kode[petunjuk] == "]":
        if sel[pengenal] != 0:
            petunjuk = petunjuk_tersimpan
    elif kode[petunjuk] == ".":
        sys.stdout.write(chr(sel[pengenal]))
    elif kode[petunjuk] == ",":
        karakter = ord(sys.stdin.read(1))
        sel[pengenal] = karakter if karakter != 10 else 0
    petunjuk += 1
