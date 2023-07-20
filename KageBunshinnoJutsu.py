while True:
  try:
    N = int(input())
    answer = 0
    qtd = 1
    while qtd < N:
      qtd *= 2
      answer += 1
    print(answer)
  except EOFError:
    break