# B. same_first_last
# retorna True se a lista nums possui pelo menos um elemento
# e o primeiro elemento é igual ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True

#len serve para ler a Lista.

def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums [-1]:
    return True
  else:
    return False

def test_ex02():
  print ('Same_first_last')
  assert same_first_last([1, 2, 3]) == False
  assert same_first_last([1, 2, 3, 1]) == True
  assert same_first_last([1, 2, 1]) == True
  assert same_first_last([7]) == True
  assert same_first_last([]) == False
  assert same_first_last([7, 7]) == True
