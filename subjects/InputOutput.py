def disp(*txt, p):
    print(*txt)
ask = lambda p : p.b(input())
functions = {">>":disp,"?":ask}
