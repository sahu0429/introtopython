names = ["Ana", "Benjamin", "Chloé"]
lengths = {n: len(n) for n in names}
print(lengths)
long_names = [n for n in names if len(n) > 3]
print(long_names)