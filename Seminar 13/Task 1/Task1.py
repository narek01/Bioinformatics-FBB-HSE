m = 10
pa = 0.055
a = 6
pb = 0.057
b = 7

print("m =", m)
print("k =", a, " | pvalue =", pa, "| padj =", round(pa * m / a, 3))
print("k =", b, " | pvalue =", pb, "| padj =", round(pb * m / b, 3))
