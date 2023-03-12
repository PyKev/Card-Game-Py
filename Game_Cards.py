from tkinter import Tk, Label, Button
import random

window = Tk()
window.title("Game")

global scores
scores = [0]

def primary():
    global label_counter1
    global numbers
    global iternumbers1
    global iternumbers0
    global itersymbol1
    global itersymbol0
    global symbolsduplicated
    global itercurrent
    
    itercurrent = iter(range(2, 53))
    
    numbers = []
    for i in range(2,15):
        for j in range(0,4):
            numbers.append(i)

    symbolsduplicated = ['♠','♣','♥','♦']

    tempList = list(symbolsduplicated)
    count = 12
    for r in range(count):
        for element in tempList:
            symbolsduplicated.append(element)
    
    combination = list(zip(numbers,symbolsduplicated))
    random.shuffle(combination)
    numbers,symbolsduplicated = zip(*combination)
    
    print(numbers)
    print(symbolsduplicated)
    label_counter1= numbers[0]    
    label_symbol1 = symbolsduplicated[0]
    
    iternumbers1 = iter(numbers[1:])
    iternumbers0 = iter(numbers)
    
    itersymbol0 = iter(symbolsduplicated) 
    itersymbol1 = iter(symbolsduplicated[1:])
    
    
    label_texto.config(text = str(label_counter1)+' '+ label_symbol1)

def firstCard():
    global firstone
    global firstsymbol
    firstone = next(iternumbers0)
    firstsymbol = next(itersymbol0)
    
def nextCard():
    global nextone
    global nextsymbol
    nextone = next(iternumbers1,'You won')
    nextsymbol = next(itersymbol1,' ')

def enabledbutton():
    button_less["state"] = 'normal'
    button_greater["state"] = 'normal'
    label_current.config(text = 'Current Card: ' + str(1))
    textofthelabel = label_texto.cget('text')
    if textofthelabel[0:2]=='11' or textofthelabel[10:12]=='11':
        newtext=textofthelabel.replace('11','J')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='12' or textofthelabel[10:12]=='12':
        newtext=textofthelabel.replace('12','Q')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='13'or textofthelabel[10:12]=='13':
        newtext=textofthelabel.replace('13','K')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='14' or textofthelabel[10:12]=='14':
        newtext=textofthelabel.replace('14','A')
        label_texto.config(text = newtext)
    
def disablebutton():
    button_less["state"] = 'disabled'
    button_greater["state"] = 'disabled'   

def function(eleccion):
    firstCard()
    nextCard()   
      
    if(firstone>nextone and eleccion=='less'):
        label_texto.config(text =str(nextone)+' '+nextsymbol)
        label_current.config(text = 'Current Card: ' + str(next(itercurrent)))
    elif(firstone<nextone and eleccion=='greater'):
        label_texto.config(text = str(nextone)+' '+nextsymbol)
        label_current.config(text = 'Current Card: ' + str(next(itercurrent)))
    elif(firstone==nextone and (eleccion=='greater' or eleccion=='less')):
        label_texto.config(text = 'Same Card '+str(nextone)+' '+nextsymbol)
        label_current.config(text = 'Current Card: ' + str(next(itercurrent)))
    else:
        if firstone == 14 and nextone == 2 and eleccion =='greater':
            label_texto.config(text =str(nextone)+' '+nextsymbol)
            label_current.config(text = 'Current Card: ' + str(next(itercurrent)))
        else:
            label_texto.config(text = ' You lost')
            disablebutton()
    
    textofthelabel = label_texto.cget('text')
    if textofthelabel[0:2]=='11' or textofthelabel[10:12]=='11':
        newtext=textofthelabel.replace('11','J')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='12' or textofthelabel[10:12]=='12':
        newtext=textofthelabel.replace('12','Q')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='13'or textofthelabel[10:12]=='13':
        newtext=textofthelabel.replace('13','K')
        label_texto.config(text = newtext)
    if textofthelabel[0:2]=='14' or textofthelabel[10:12]=='14':
        newtext=textofthelabel.replace('14','A')
        label_texto.config(text = newtext)
    
    if label_texto.cget("text")==' You lost':
        
        lastcurrent = label_current.cget("text")[-2:]
        
        scores.append(int(lastcurrent))
        
        label_lastscore.config(text = 'Last score: ' + str(scores[-1]))
        label_maxscore.config(text = 'Max score: '+ str(max(scores)))
        
    if label_current.cget("text")=='Current Card: 52':
        label_texto.config(text = 'YOU WONN!')
        disablebutton()
                
#Label
label_current = Label(window, text = 'Current Card: ' + str(1))
label_current.grid(row=0,column=1,padx=20)

label_lastscore = Label(window, text = 'Last score: ' + str(0))
label_lastscore.grid(row=5,column=1,padx=20,pady=5)

label_maxscore = Label(window, text = 'Max score: ' + str(0))
label_maxscore.grid(row=6,column=1,padx=20)

label_texto = Label(window, text = '')
label_texto.grid(row=1,column=1,padx=20,pady=5)
primary()
textofthelabel = label_texto.cget('text')
if textofthelabel[0:2]=='11' or textofthelabel[10:12]=='11':
    newtext=textofthelabel.replace('11','J')
    label_texto.config(text = newtext)
if textofthelabel[0:2]=='12' or textofthelabel[10:12]=='12':
    newtext=textofthelabel.replace('12','Q')
    label_texto.config(text = newtext)
if textofthelabel[0:2]=='13'or textofthelabel[10:12]=='13':
    newtext=textofthelabel.replace('13','K')
    label_texto.config(text = newtext)
if textofthelabel[0:2]=='14'or textofthelabel[10:12]=='14':
    newtext=textofthelabel.replace('14','A')
    label_texto.config(text = newtext)

#Buttons
button_less = Button(window, text="Less",width=9,height=1,command= lambda: function("less"))
button_greater = Button(window, text= "Greater",width=9,height=1,command= lambda: function("greater"))
button_next = Button(window, text= "Try again",width=9,height=1,command=lambda:[primary(), enabledbutton()])

#Adding buttons
button_less.grid(row=2,column=1,padx=20,pady=3)
button_greater.grid(row=3,column=1,padx=20,pady=3)
button_next.grid(row=4,column=1,padx=20,pady=3)

window.mainloop()
