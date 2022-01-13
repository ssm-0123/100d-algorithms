def next(current , myList):
    '''
    determine the next item from the list. The list contains False/True Boolean values
    that indicate whether the current item can be used
    '''
    tried = 0
    current = int(current)+1
    if current >= len(myList):
        current = 0
    while True:
        if myList[current] == False:
            current = current+1
            tried = tried + 1
            if current >= len(myList):
                current = 0
        if myList[current] == True:
            return current
        if tried == len(myList):
            return None




def main():
  data = [False, True, True, False, True, False]
  assert next( 3 , data ) == 4
  assert next( 4 , data ) == 1
  assert next( 1 , data ) == 2
  data = [True, True, False, False, True, False, True]
  assert next( 1 , data ) == 4
  assert next( 6 , data ) == 0
  assert next( 0 , data ) == 1
  assert next( 3 , data ) == 4
  data = [True, True, False]
  assert next( 1 , data ) == 0
  assert next( 0 , data ) == 1
  data = [False, False, False]
  assert next( 1, data ) == None
  
  
  
  
  
  
  


main()