import collections


def greatest_common_divisor(*args):
  msg1 = 'empty'
  msg2 = 'none'
  args = sorted(args, reverse=True)
  d = collections.defaultdict(list)

  for i, e in enumerate(args):
    rng = range(2, e + 1)
    for j in rng:
      if e % j == 0:
        d[f"{i} divisors:"].append(j)

  gcdlst = [d.get(i) for i in d]

  lenlst = [len(i) - 1 for i in gcdlst]

  cdlst = []
  ctr = 1
  for i, divisors in enumerate(gcdlst[:]):
    R = lenlst[i] + 1
    for ind in range(R):
      try:
        if divisors[:][ind] <= args[i]:
          if divisors[:][ind] in gcdlst[:][ctr]:
            x = divisors[:][ind]
            cdlst.append(x)
      except:
        if gcdlst[-1][ind] in cdlst:
          y = gcdlst[-1][ind]
          cdlst.append(y)

    ctr += 1

  cdlst = sorted(set(cdlst))

  for i, a in enumerate(args):
    for i, e in enumerate(cdlst):
      if a % e != 0:
        cdlst.remove(cdlst[i])

  for c in cdlst:
    if min(args) % cdlst[-1] != 0 or max(args) % cdlst[-1] != 0:
      cdlst.remove(cdlst[-1])

  count = 0
  for i, e in enumerate(args):
    try:
      if e % max(cdlst) == 0:
        count += 1
      if count == len(args):
        return cdlst, max(cdlst), args
    except:
      if not cdlst:
        return msg1, msg2, args

  return msg1, msg2, args


if __name__ == "__main__":

  x, y, z = input("enter three numbers \nseperated by spaces:  \n\n").split()
  x, y, z = int(x), int(y), int(z)

  gcd = greatest_common_divisor(x, y, z)
  plst = [i for i in range(2,max(gcd[2]) + 1) if all(i % j != 0 for j in range(2, i))]

  print("\n\/\/\/\/\/\/\/\/\/\/\/")

  if gcd[1] != "none":
    print(f"\ngcd = {gcd[1]}")
  c = 1
  for i in gcd[2]:
    c *= i

  try:
    print(f"lcm = {c/gcd[1]}\n")
    print(f"other common divisors: {sorted(gcd[0][:-1], reverse=True)}")

    prime_div_lst = []
    for number in gcd[0]:
      if number in plst:
        prime_div_lst.append(number)
    print(f"prime common divisors: {sorted(prime_div_lst, reverse=True)}\n")

    if gcd[0]:
      try:
        with open("records.txt", "x") as f:
          f.write("RECORDS-\n----------------------------\n\n")
          f.write(f"gcd for {gcd[2]} = {gcd[1]}\n")
          f.write(f"lcm = {c/gcd[1]}\n")
          f.write(f"# of common divisors: {len(gcd[0])}\n\n")
          f.close()
      except:
        with open("records.txt", "a+") as f:
          f.write(f"gcd for {gcd[2]} = {gcd[1]}\n")
          f.write(f"lcm = {c/gcd[1]}\n")
          f.write(f"# of common divisors: {len(gcd[0])}\n\n")
          f.close()

  except:
    print("\n")
    for arg in gcd[2]:
      if arg in plst:
        print(f"{arg} is prime")

  finally:
    if gcd[1] == 'none' and gcd[0] == 'empty':
      print(f"\ngcd = {gcd[1]}")
      print(f"lcm = {gcd[1]}")
      print(f"other common divisors: {gcd[0]}")
