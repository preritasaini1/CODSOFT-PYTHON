from tkinter import *
from PIL import Image, ImageTk
from random import randint

root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

# Load and resize images-

def resize_image(image_path, size):
    image = Image.open(image_path)
    image = image.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

rock_img = resize_image("rock-user.png", (200, 200))
paper_img = resize_image("paper-user.png", (200, 200))
scissor_img = resize_image("scissor-user.png", (200, 200))
rock_comp_img = resize_image("rock.png", (200, 200))
paper_comp_img = resize_image("paper.png", (200, 200))
scissor_comp_img = resize_image("scissor.png", (200, 200))

user_label=Label(root,image=scissor_img,bg="#9b59b6")
comp_label=Label(root,image=scissor_comp_img,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores-
playscore= Label(root,text=0,font=("Helvetica", 14, "bold"),bg="#9b59b6",fg="white")
computerscore = Label(root,text=0,font=("Helvetica", 14, "bold"),bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playscore.grid(row=1,column=3)

#indicators-
user_indicator= Label(root,font=("Helvetica", 20, "bold"),text="USER",bg="#9b59b6",fg="white").grid(row=0,column=3)
comp_indicator= Label(root,font=("Helvetica", 20, "bold"),text="COMPUTER",bg="#9b59b6",fg="white").grid(row=0,column=1)

#message-
msg= Label(root,font=("Helvetica", 12, "bold"),bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update message-
def updatemessage(x):
    msg['text']=x

#update score-
def updateuserscore():
    score = int(playscore["text"])
    score+=1
    playscore["text"] = str(score)

def updatecompscore():
    score = int(computerscore["text"])
    score+=1
    computerscore["text"] = str(score)

#check winner-
def checkwin(player,computer):
    if player == computer:
        updatemessage("It's a Tie!!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("You Loose!")
            updatecompscore()
        else:
            updatemessage("You Win!!!")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemessage("You Loose!")
            updatecompscore()
        else:
            updatemessage("You Win!!!")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updatemessage("You Loose!")
            updatecompscore()
        else:
            updatemessage("You Win!!!")
            updateuserscore()
    else:
        pass

#update choices--
choices= ["rock","paper","scissor"]
def updatecoice(x):

    #for Computer:
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compchoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)

    #for User:
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwin(x,compchoice)

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",font=("Helvetica", 12, "bold"),
              command=lambda:updatecoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",font=("Helvetica", 12, "bold"),
               command=lambda:updatecoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",font=("Helvetica", 12, "bold"),
                 command=lambda:updatecoice("scissor")).grid(row=2,column=3)



root.mainloop()