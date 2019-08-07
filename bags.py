import turtle
import random

TIME_STEP = 500
bag_list=[]
bag_pos=[]
bag=turtle.clone()
def make_bag():
    line=random.randint(1,3)
    if line==1:
        bag.goto(rightedge,seaturtle.ycore()+30)        
    if line==2:
        bag.goto(rightedge,seaturtle.ycore())        
    if line==3:
        bag.goto(rightedge,seaturtle.ycore()-30)        
    bag_pos.append(bag.pos())
    
   
   
def move_bag():
    
    bag_pos=bag_pos.pop()
    x_bag=bag_pos[0]
    y_bag=bag_pos[1]
    bag.goto(x_bag-1000,y_bag)
    turtle.ontimer(move_bag,TIME_STEP)
move_bag()
