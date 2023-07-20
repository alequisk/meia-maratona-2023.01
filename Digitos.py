for _ in range(int(input())):
  n, m = list(map(int, input().split(" ")))
  v = str(n ** m)
  print(len(v))