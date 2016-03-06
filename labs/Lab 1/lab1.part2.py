base_10 = 128
base_2 = (base_10 * (10**9)) / (2**30)
difference = base_10 - base_2
print base_10, "GB in base 10 is actually", base_2, "GB in base 2, ", difference, "GB less than advertised."