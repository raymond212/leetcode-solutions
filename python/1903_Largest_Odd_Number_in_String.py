class Solution:
    def largestOddNumber(self, num: str) -> str:
      odd =  {'1', '3', '5', '7', '9'}
    
      for i in range(len(num) - 1, -1, -1):
          if num[i] in odd:
              return num[:i + 1]

      return ''