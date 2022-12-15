#pyramid pattern printin 
#expected output -> 
#print_pyrmd(5)->
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''

def print_pyrmd(n: int, cnt: int = 1)->None:
    if cnt==n:
        print(" "*0+"* "*n)
        return
    else:
        print(" "*(n-cnt)+"* "*cnt)
        print_pyrmd(n, cnt+1)

if __name__=="__main__":
  pass
