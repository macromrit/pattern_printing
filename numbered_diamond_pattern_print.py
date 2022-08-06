#number diamond pattern printin 
#expected output -> 
#numbered_diamond_pattern(9) ->
'''
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1  
'''


#source snippet ->
def numbered_diamond_pattern(cnt: int)->None:
    if cnt%2!=0 and 9>=cnt>=3:
        
        #errect pyramid -> top phase
        for i in range(1, cnt+1, 2):
            print(' '*((cnt-i)//2), end='')
            for z in range(1, i+1):
                print(z,end='')
            print(' '*((cnt-i)//2))
        
        #inverted pyramid -> bottom phase
        for i in range(cnt-2, 0, -2): #having 0 as upper since upper limit's are exclusive
            print(' '*((cnt-i)//2), end='')
            for z in range(1, i+1):
                print(z, end='')
            print(' '*((cnt-i)//2))
            
            
    else:
        raise Exception('layer count too small to be framed(should be >= 3 and <= 9(to maintain the stability))... or entered an even number')    


if __name__ == '__main__':
    pass
