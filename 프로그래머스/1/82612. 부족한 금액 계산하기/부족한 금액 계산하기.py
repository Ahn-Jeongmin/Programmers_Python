def solution(price, money, count):
    
    for i in range(1, count+1):
        money-=price*i
        
    if money>=0:
        money=0
    return money*(-1)