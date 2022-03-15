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

def dict_approach(chars):
  char_dict = {}
  for char in chars:
    char_dict[char] = 0

  for char in chars:
    char_dict[char]+=1
    if char_dict[char] > 1:
      return False

  return True

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

result = dict_approach('abccddefg')
if result is True:
  print("All unique.")
else:
  print("Not all unique.")
