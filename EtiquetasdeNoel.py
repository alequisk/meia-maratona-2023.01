congrats = {}
for i in range(int(input())):
  language = input()
  greets = input()
  congrats[language] = greets
for i in range(int(input())):
  people = input()
  language = input()
  print(f"{people}\n{congrats[language]}\n")
