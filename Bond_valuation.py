# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:29:14 2022

@author: Giri
"""
from math import exp as e
class CouponBond:
    
    def __init__(self,principal, rate, maturity, interest_rate):
        #interest_rate- rsk free rate of return
        #coupon rate and rrfr in ercentage terms hence divided by 100
        self.principal= principal
        self.rate= rate/100
        self.maturity = maturity
        self.interest_rate= interest_rate/100
        
#calculate pv factor which will be multiplied with coupon payment and principal 
#to find out the PV
        
    def present_value(self,x,n):
       return x / (1+self.interest_rate)**n
    
    def Present_continuous_value(self,x,t):
        return x/e(-self.interest_rate*t)    
    
    def calculate_price_continuous(self):
        
        price_Cv =0 
        #discount coupon payments
        
        #for loop to calculate pv of cashflows for all periods
        # maturity+1 to run loop until maturity as 1 is included and self.maturity is excluded in a range
        for t in range (1,self.maturity+1):
       
         price_Cv=price_Cv+self.Present_continuous_value(self.principal*self.rate,t)
        
        #dicount principal
        
         price_Cv=price_Cv+self.Present_continuous_value(self.principal,self.maturity)
       
         return price_Cv
    
    def calculate_price(self):
        
      price = 0

      for t in range(1, self.maturity+1):
          price = price + self.present_value(self.principal * self.rate, t)

      price = price + self.present_value(self.principal, self.maturity)

      return price
        
      
        
     # price =0
        
        #for t in range (1,self.maturity+1):
         #price=price+self.Present_discret_value(self.principal*self.coupon_rate,t)
         
        #dicount principal
        
         #price=price+self.Present_discret_value(self.principal,self.maturity)
        
         #return price
   

if __name__ == '__main__':    
    
    bond =CouponBond(1000,10,3,4)
    
   
    print("Bond price(continuous model): %.2f" % bond.calculate_price_continuous())
    print("Bond price(discrete model): %.2f" % bond.calculate_price())
    
    
   
    
   
        
        
        