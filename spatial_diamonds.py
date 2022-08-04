def pattern_func(cnt):
    if cnt%2 and cnt>=9:
        # +2 for every diamond space layer
        #max space char to be manufactured -> cnt-2
        
        #first half
        
        #defualt statement 
        max = 0
        
        #while keyword with conditions
        while max<=cnt-2:
            #body
            if max==0:
                print('*'*cnt)
            else: 
                cal = (cnt-max)//2
                print('*' * cal, ' ' * max, '*' * cal, sep='')
            
            #update statement
            if max:
                max+=2
            else:
                max+=1
            
        #second half
        ref = cnt-4
        
        while ref>=0:
            #body
            space_cnt = (cnt-ref)//2
            print('*'*space_cnt, ' '* ref,'*'*space_cnt, sep='') 
             
            #update statement        
            ref-=2
            
            if ref==-1:
                print('*'*cnt)
                
        
                
    else:
        raise Exception('Error -> enter odd number or number wasn\'t >= 9')
    
if __name__ == '__main__':
    pass
