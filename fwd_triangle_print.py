#expected output->
#pattern function -> fwd_triangle_print(11, '*')

'''
*
**
***
****
*****
******
*******
********
*********
**********
***********
'''

#source snippet ->
def fwd_triangle_print(cnt: int, char: str, ini_cnt: int=1) -> None:
    if ini_cnt==cnt:
        print(char*cnt)
        return
    else:
        print(char*ini_cnt)
        fwd_triangle_print(cnt, char,ini_cnt+1)


if __name__ == "__main__":
    pass
