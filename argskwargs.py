def why_would_i_ever_do_this(*args,**kwargs):
    sum = 0
    mul = 1
    for x in args :
        sum += x
    if kwargs :
        for k,v in kwargs.items():
            print(v)
            mul *= v
    else :
        mul = 1
    sub = mul - sum
    return sub

if __name__ == '__main__':
    assert why_would_i_ever_do_this() == 1
    assert why_would_i_ever_do_this(1, 2, 3) == -5
    assert why_would_i_ever_do_this(a=1, b=2, c=3) == 6
    assert why_would_i_ever_do_this(1, x=2, y=3) == 5
    assert why_would_i_ever_do_this(1, 2, r=3) == 0
    assert why_would_i_ever_do_this(0, a=3) == 3


    
