def find_permutation(string_one, string_two):
  if len(string_one) != len(string_two):
    return False

  string_one = sorted(string_one)
  string_two = sorted(string_two)

  for i in range(len(string_one)):
    if string_one[i] != string_two[i]:
      return False

  return True

permutation = find_permutation('hi', 'ihi')
if permutation is False:
  print("Not a permutation.")
else:
  print("Permutation found.")
