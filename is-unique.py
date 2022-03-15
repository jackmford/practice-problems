def brute_force(chars):
  for i in range(len(chars)):
    for j in range(i+1, len(chars)):
      if chars[i] == chars[j]:
        return False
  return True

def set_approach(chars):
  char_set = set()
  for char in chars:
    char_set.add(char)

  if len(chars) == len(char_set):
    return True
  else:
    return False

result = brute_force('aabcdefg')
if result is False:
  print("Not all unique.")
else:
  print("All unique.")

result = set_approach('abcdefgg')
if result is True:
  print("All unique.")
else:
  print("Not all unique.")
