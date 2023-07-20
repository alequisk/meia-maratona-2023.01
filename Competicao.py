while True:
  N, M = list(map(int, input().split(' ')))
  if N + M == 0:
    break
  
  solved_all = False
  solved_at_least_one = True
  problem_solved_for_all = False
  participants_solved_one = True
  
  cnt_solved_problem = [0] * M
  for participant in range(N):
    problems = list(map(int, input().split()))
    cnt_solved = 0
    for i in range(M):
      if problems[i] == 1:
        cnt_solved_problem[i] += 1
        cnt_solved += 1
    # computing values
    if cnt_solved == M:
      solved_all = True
    participants_solved_one = participants_solved_one and (cnt_solved > 0) 

  for cnt in cnt_solved_problem:
    if cnt == N:
      problem_solved_for_all = True
    solved_at_least_one = solved_at_least_one and (cnt > 0)

  answer = 0
  if solved_all == False:
    answer += 1
  if solved_at_least_one:
    answer += 1
  if problem_solved_for_all == False:
    answer += 1
  if participants_solved_one:
    answer += 1
  print(answer)