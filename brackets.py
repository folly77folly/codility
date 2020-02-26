# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

# def solution(S):
#     right_side_count = 0
#     #length of string
#     len_string = len(S)
    
#     #check is string is odd length
#     if len_string % 2 != 0:
#         return 0

#     #get middle position of string
#     middle_way = len_string / 2
#     i = 0
#     if len_string == 2:
#         left_side = check_string(S[0])
#         right_side = check_string(S[1])
#         if left_side == "open1" and right_side == "close1" or left_side == "open2" and right_side == "close2" or left_side == "open3" and right_side == "close3" :
#             return 1
#         return 0


#     while i < middle_way:
#         left_side = check_string(S[i])
#         right_side_count -= 1
#         right_side = check_string(S[right_side_count])

#         if left_side == "open1" and right_side == "close1":
#             print(left_side, right_side )

#         elif left_side == "open2" and right_side == "close2":
#             print(left_side, right_side )

#         elif left_side == "open3" and right_side == "close3":
#             print(left_side, right_side )
#         elif left_side == "close1" and right_side =="open1" or left_side == "close2" and right_side =="open2" or left_side == "close3" and right_side =="open3":
#             print(left_side,right_side)            
#         else:
#             return 0
#         i += 1
#     return 1

# def check_string(S):
#     if S == "(" :
#         return "open1"
#     if S == ")" :
#         return "close1"

#     if S == "{" :
#         return "open2"
#     if S == "}" :
#         return "close2"

#     if S == "[" :
#         return "open3"
#     if S == "]" :
#         return "close3"

# A = ")("
# print(solution(A))
def solution(S):
  if len(S) == 0:
    return 1
  
  if len(S) % 2 != 0:
    return 0

  close_brackets = ["}", ")", "]"]
  open_brackets = ["{", "(", "["]


  if S[0] in close_brackets:
    return 0

  bracket_pair = {
    "{": "}",
    "[": "]",
    "(": ")"
  }

  def is_valid_pair(open_brac, close_brac):
    if bracket_pair[open_brac] == close_brac:
      return True
    else:
      return False

  check_stack = []
  for new_item in S:
    if new_item in open_brackets:
      check_stack.append(new_item)
      print(check_stack)
    else:
      if len(check_stack) == 0:
        return 0
      last_item = check_stack.pop()
      if not is_valid_pair(last_item, new_item):
        return 0
  
  if len(check_stack) != 0:
    return 0
  
  return 1

A = "([()({)])"
print(solution(A))