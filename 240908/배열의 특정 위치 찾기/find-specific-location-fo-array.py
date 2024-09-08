arr = list(map(int, input().split()))
eveninput = arr[1::2]
triple = arr[2::3]
tripleavg = sum(triple)/len(triple)
print("{0} {1:.1f}".format(sum(eveninput), tripleavg))