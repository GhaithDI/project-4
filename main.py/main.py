#width=800,height=512

##Screen setup##
import turtle,pandas
screen=turtle.Screen()
screen.setup(height=512,width=800)
screen.bgpic('project_map.gif')
##End screen Setup##

##data bulid ##
data=pandas.read_csv('state_number.csv')
countries=data.country.to_list()
user_number=0
state_number=21
gussed=[]
miising_cuntries=[]
##End data build###

##main loop##
while len(gussed)<21:
          answer=screen.textinput(title='Gusse a cauntry!',prompt=f'you have {user_number} gussed.\nYou still a have {state_number} to guss!!').title()
          if answer in countries:
                  gussed.append(answer)
                  user_number+=1
                  state_number -=1
                  countrt_x=data[data.country==answer]['x'].item()
                  countrt_y=data[data.country==answer]['y'].item()
                  t=turtle.Turtle()
                  t.hideturtle()
                  t.penup()
                  t.speed('fast')
                  t.goto(countrt_x,countrt_y)
                  t.fillcolor('red')
                  t.begin_fill()
                  t.circle(10)
                  t.end_fill()
                  t.write(answer,font=('arial',10))
          elif answer=='Exit':
                  for conutry in countries:
                          if conutry not in gussed:
                                  miising_cuntries.append(conutry)
                  fincal_csv=pandas.DataFrame(miising_cuntries).to_csv('Wrong_answer.csv')
                  break
## end loop##         

      