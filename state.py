from itertools import permutations
from math import factorial

def solve():
  def combinable(first, second):
    return first[2] & second[2] == 0

  def group(first, second):
    if first[1].isdecimal() and second[1].isdecimal():
      formula = f"{first[1]}{second[1]}"
      return (int(formula), formula, first[2] | second[2])

  def add(first, second):
    return (first[0] + second[0], f"({first[1]} + {second[1]})", first[2] | second[2])

  def subtract(first, second):
    return (first[0] - second[0], f"({first[1]} - {second[1]})", first[2] | second[2])

  def multiply(first, second):
    if first[0] < 1000000000 and second[0] < 1000000000 and first[0] * second[0] < 1000000000:
      return (first[0] * second[0], f"({first[1]} * {second[1]})", first[2] | second[2])

  def divide(first, second):
    if second[0] != 0 and first[0] // second[0] == first[0] / second[0]:
      return (first[0] // second[0], f"({first[1]} / {second[1]})", first[2] | second[2])

  def exp(first, second):
    if second[0] >= 0 and first[0] < 1000000000 and second[0] < 1000 and first[0] ** second[0] < 1000000000:
      return (first[0] ** second[0], f"({first[1]} ^ {second[1]})", first[2] | second[2])

  def root(first, second):
    if 1 < first[0] < 1000000000 and 1 < second[0] < 1000000000 and first[0] ** (1 / second[0]) == int(first[0] ** (1 / second[0])):
      return (int(first[0] ** (1 / second[0])), f"root({first[1]}, {second[1]})", first[2] | second[2])

  def sqrt(first):
    if first[0] > 1 and first[0] ** 0.5 == int(first[0] ** 0.5):
      return (int(first[0] ** 0.5), f"sqrt({first[1]})", first[2])

  def fact(first):
    if 0 <= first[0] < 100:
      return (factorial(first[0]), f"({first[1]})!", first[2])

  results = {
    (2, 8): (2, "2", 8),
    (0, 4): (0, "0", 4),
    (1, 2): (1, "1", 2),
    (9, 1): (9, "9", 1),
  }

  updated = True
  while updated:
    updated = False
    new_results = {}
    for to_group in permutations(results.keys(), 2):
      a, b = to_group
      if combinable(results[a], results[b]):
        new_result = group(results[a], results[b])
        if new_result and (new_result[0], new_result[2]) not in results:
          new_results[(new_result[0], new_result[2])] = new_result
          print(new_result)
          updated = True
    results.update(new_results)

  pre = results.copy()
  updated = True
  while updated:
    updated = False
    new_results = {}
    print(f"===================")
    print(f"results: {len(results)}")
    print(f"latest_results: {len(pre)}")
    for a in pre.keys():
      if results[a][2] < 15:
        for b in results.keys():
#          if results[a][1] == "(1 ^ 2)" and results[b][1] == "09":
#            import pdb; pdb.set_trace()
          if combinable(results[a], results[b]):
            new_result = add(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = add(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = subtract(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = subtract(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = multiply(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = multiply(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = divide(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = divide(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = exp(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = exp(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = root(results[a], results[b])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
            new_result = root(results[b], results[a])
            if new_result and (new_result[0], new_result[2]) not in results:
              if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
                new_results[(new_result[0], new_result[2])] = new_result
                updated = True
      new_result = sqrt(results[a])
      if new_result and (new_result[0], new_result[2]) not in results:
        if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
          new_results[(new_result[0], new_result[2])] = new_result
          updated = True
      new_result = fact(results[a])
      if new_result and (new_result[0], new_result[2]) not in results:
        if (new_result[0], new_result[2]) not in new_results or len(new_result[1]) < len(new_results[(new_result[0], new_result[2])][1]):
          new_results[(new_result[0], new_result[2])] = new_result
          updated = True
    results.update(new_results)
    pre = new_results

    for v in pre.values():
      if v[0] == 1 or v[0] == 9:
        print(f"{v[0]} = {v[1]}")

  final = {}
  for value in results.values():
    if value[2] == 15 and 1 <= value[0] <= 100 and (value[0] not in final or len(value[1]) < len(final[value[0]][1])):
      final[value[0]] = value

  for key in sorted(final.keys()):
    print(f"{final[key][0]} = {final[key][1]}")

  print(f"Found {len(final.keys())}/100")

if __name__ == '__main__':
  solve()
