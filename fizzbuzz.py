from itertools import cycle
print("\n".join(str(y) if not x else x for x, y in zip(cycle([None, None, "fizz", None, "buzz", "fizz", None, "None", "fizz", "buzz", None, "fizz", None, None, "fizzbuzz"]), range(1, 100))))
