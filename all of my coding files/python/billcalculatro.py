import pygame,pygwidgets,sys
# Make a electricity bill calculator model:
# For the first 100 units, the rate is $0.5 per unit.
# For the second 100 units, the rate is $0.75 per unit.
# For the third 100 units, the rate is $1.20 per unit.
# For anything more than 300 units, the rate is $1.50 per unit.

# Ask user what was their monthly unit consumption and give back the bill amount as answer.
# units = 450 ---> 470$
# units = int(input())
# def electric_bill_calculator(units):
#     if units<=100:
#         bill = units*0.5
#     elif units<=200:
#         bill= (100*0.5)+((units-100)*0.75)
#     elif units<=300:
#         bill=(100*0.5)+(100*0.75)+((units-200)*1.2)
#     else:
#         bill=((100*0.5)+(100*0.75)+(100*1.2)+((units-300)*1.5))
#     print(bill)
# electric_bill_calculator(units)

# 1 - main code



# 2 - Define constants

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BLACK = (0,0,250)
FRAMES_PER_SECOND = 20

# 3 - Initialize the world
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock()


# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables

heading = pygwidgets.DisplayText(window,(150,50),"Bill Calculator", fontSize=60,textColor="lime", )
questiontext = pygwidgets.DisplayText(window,(100,200),"What is your montly unit consumption?",fontSize=30 ,textColor="lime")
inputtext= pygwidgets.InputText(window,(100,300),width=200,fontSize=30,textColor="lime",backgroundColor="blue",initialFocus=True,)
textbutton= pygwidgets.TextButton(window,(100,400),"calculate total cost",300,40,textColor="lime",downColor="blue",fontSize=40,upColor="blue",overColor="blue")
answertext=pygwidgets.DisplayText(window,(150,500),"",fontSize=30,textColor="white")
units=""

# 6 - Loop forever

while True:
    

    # 7 - Check for and handle events
    for event in pygame.event.get():

        # clicked the close button to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if inputtext.handleEvent(event):
            unit=inputtext.getValue()


    # 8 - Do any "per frame" actions



    # 9 - Clear the window
    window.fill(BLACK)



    # 10 - Draw all window elements
    heading.draw()
    questiontext.draw()
    inputtext.draw()
    textbutton.draw()
    answertext.draw()


    # 11 - Update the window
    pygame.display.update()


    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)





