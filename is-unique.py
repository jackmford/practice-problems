def brute_force(chars):
  print(chars[0])
  for i in range(len(chars)):
    for j in range(i+1, len(chars)):
      if chars[i] == chars[j]:
        return True
  return False

result = brute_force('aabcdefg')
if result is True:
  print("Not all unique.")
else:
  print("All unique.")
