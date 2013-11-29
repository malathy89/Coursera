# implementation of card game - Memory

import simplegui
import random
tlx=0
tly=0
blx=0
bly=100
brx=50
bry=100
trx=50
trz=0
l=[]
val=[]
state=0
cards=[-1,-1]
deck1=range(8)
deck2=range(8)
turn=0
# helper function to initialize globals
def new_game():
    global l,val,state,turn,cards
    cards=[-1,-1]
    state=0
    turn=0
    l=[]
    val=[]
    random.shuffle(deck1)
    random.shuffle(deck2)
    for n in range(16):
        l.append(False)
        if(n<8):
            val.append(deck1[n])
        else:
            val.append(deck2[n-8])
    
    random.shuffle(val)
    label.set_text("Turns = "+str(turn))
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,cards,l,turn
    n=pos[0]//50
    if(l[n]==False):
        if state == 0:
                state = 1
                cards[0]=n
        elif state == 1:
            state = 2
            cards[1]=n
            turn=turn+1
        else:
            state = 1
            if(val[cards[0]]!=val[cards[1]]):
                for n1 in cards:
                    if(n1>=0):
                        l[n1]=False
            
            cards[0]=n
            cards[1]=-1
        
        
    label.set_text("Turns = "+str(turn))
    
    for n2 in cards:
        if(n2>=0):
            l[n2]=True
    
    
    #l[n]=True
    #print 'click' + str(n)
    #canvas.draw_text('5',[50,50],20,'White')
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global tlx,tly,blx,bly,brx,bry,trx,trz,l,val

    for n in range(16):
        if(l[n]):
            canvas.draw_text(str(val[n]),[(tlx+(n*50))+15,60],40,'White')
           # print n
        else:
            canvas.draw_polygon([[tlx+(n*50), tly], [blx+(n*50), bly], [brx+(n*50), bry], [trx+(n*50), trz]], 2, 'Yellow','Green')

    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric