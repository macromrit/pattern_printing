#expected output->
#pattern function-> revr_triangle_print(11, '*')
'''
***********
**********
*********
********
*******
******
*****
****
***
**
*
'''

#source snippet
def revr_triangle_print(cnt: int, char: str)->int:
    if cnt==0:
        return 
    else:
        print(char*cnt)
        revr_triangle_print(cnt-1, char)


if __name__ == "__main__":
    pass
