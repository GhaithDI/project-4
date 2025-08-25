#width=800,height=512
import turtle,pandas
screen=turtle.Screen()
screen.bgpic('project_map.gif')
screen.setup(height=512,width=800)
data=pandas.read_csv('state_number.csv')
countrys=data.country.to_list()
user_answer=0
state_number=21
gussed=[]
missing_country=[]
while len(gussed)<21:
          answer=screen.textinput(title='write the name',prompt=f'you have {user_answer} gussed from 21 state\nyou still have {state_number} to guss!!').title()
          if answer in countrys:
                  gussed.append(answer)
                  user_answer +=1
                  state_number -=1
                  countrys_x=data[data.country==answer]['x'].item()
                  countrys_y=data[data.country==answer]['y'].item()
                  t=turtle.Turtle()
                  t.hideturtle()
                  t.penup()
                  t.goto(countrys_x,countrys_y)
                  t.fillcolor('red')
                  t.begin_fill()
                  t.circle(radius=10)
                  t.end_fill()
                  t.write(answer,font=('arila',15,'italic'))
          elif answer =='Exit':
                  for country in countrys:
                          if country not in gussed:
                                  missing_country.append(country)
                          fincal_csv=pandas.DataFrame('wrongasnwer.csv').to_csv()
                          break

