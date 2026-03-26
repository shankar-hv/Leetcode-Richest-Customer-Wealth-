def maximumWealth(self, accounts: List[List[int]]) -> int:
  sums = 0
  s = []
  for i in accounts:
    sums = sum(i)
    s.append(sums)
            
  return max(s)
