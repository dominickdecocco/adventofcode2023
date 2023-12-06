#!/usr/bin/env python3
# adventofcode day1
# dominickdecocco

# does not pass. need to convert alpha digits into int before defining cvalues

with open("puzzle-input.txt") as f:
  lines = [line.rstrip() for line in f]
  digits = [[int(d) for d in l if d.isdigit()] for l in lines]
  cvalues = [[d[::len(d)-1] if len(d) > 1 else d for d in digits]]
  [calibration] = [[sum(v) for v in d] for d in cvalues]
  print(sum(calibration))