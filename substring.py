 
chars = 256
def max_char(str, n):
  count = [0] * chars
  for i in range(n):
      count[ord(str[i])] += 1
  dis_val = 0
  for i in range(chars):
      if (count[i] != 0):
          dis_val += 1
  return dis_val 

def smallest_substring(str): 
  n = len(str)
  dis_val = max_char(str, n)
  minl = n
  for i in range(n):
      for j in range(n):
          s = str[i:j]
          s_length = len(s)
          sub_char = max_char(s,s_length)
          if (s_length < minl and dis_val == sub_char):
              minl = s_length

  return minl
str1=input()
res= smallest_substring(str1)
print(res)
	
