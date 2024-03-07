from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

win=Tk()
win.geometry('500x500')
i=0
z=0
frames=[]
btns=[]
costs=[]
descs=[]


image1=Image.open('apple.png')
img1=image1.resize((100,100))
my_img1=ImageTk.PhotoImage(img1,master=win)

image2=Image.open('mango.png')
img2=image2.resize((100,100))
my_img2=ImageTk.PhotoImage(img2,master=win)


image3=Image.open('guava.jpg')
img3=image3.resize((100,100))
my_img3=ImageTk.PhotoImage(img3,master=win)

image4=Image.open('strawberry.jpg')
img4=image4.resize((100,100))
my_img4=ImageTk.PhotoImage(img4,master=win)


image5=Image.open('onion.png')
img5=image5.resize((100,100))
my_img5=ImageTk.PhotoImage(img5,master=win)



image6=Image.open('green_chilli.png')
img6=image6.resize((100,100))
my_img6=ImageTk.PhotoImage(img6,master=win)


image7=Image.open('tomato.png')
img7=image7.resize((100,100))
my_img7=ImageTk.PhotoImage(img7,master=win)

image8=Image.open('potato.jpg')
img8=image8.resize((100,100))
my_img8=ImageTk.PhotoImage(img8,master=win)

image9=Image.open('pepper.png')
img9=image9.resize((100,100))
my_img9=ImageTk.PhotoImage(img9,master=win)

image10=Image.open('clove.png')
img10=image10.resize((100,100))
my_img10=ImageTk.PhotoImage(img10,master=win)

image11=Image.open('almond.png')
img11=image11.resize((100,100))
my_img11=ImageTk.PhotoImage(img11,master=win)

image12=Image.open('dates.png')
img12=image12.resize((100,100))
my_img12=ImageTk.PhotoImage(img12,master=win)


my_images=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10,my_img11,my_img12]
cost=['$7.00', '$4.00', '$5.00','$13.00','$4.50','$9.00','$8.00','$5.00','$5.0','$8.00','$4.00','$6.00']
desc=['Organic Apples','Juicy Mangoes','Tasty Guava','Strawberries','Onions 1pac','Chilli 1pac','Tomato 1 pac','Potato 1pac','Pepper 100gms','clove 100gms','dates 1 pac','almonds 1 pac']

def display_forward():
    global i
    i+=1
    
    if i==1:
        for k in range(0,4):
            
           btns[k].config(image=my_images[k+4])
           costs[k].config(text=cost[k+4])
           descs[k].config(text=desc[k+4])
           back_btn.config(state='normal') 
                   
                    
    elif i==2:
        for m in range(0,4):
            btns[m].config(image=my_images[m+8])
            costs[m].config(text=cost[m+8])
            descs[m].config(text=desc[m+8])
            back_btn.config(state='normal') 
            
    else:
        fore_btn.config(state='disabled')
        
            
def display_backward():
    global i
    i-=1
    if i ==0:    
        for l in range(0,4):
            btns[l].config(image=my_images[l])
            costs[l].config(text=cost[l])
            descs[l].config(text=desc[l])
            back_btn.config(state='disabled')
            
    elif i==1:
        for g in range(0,4):
            btns[g].config(image=my_images[g+4])
            costs[g].config(text=cost[g+4])
            descs[g].config(text=desc[g+4])
            fore_btn.config(state='normal')
    else:
        pass
          
if i==0:
     for j in range(0,4):
           
         frame_display=Frame(win,bg='white',width=250,height=300)
         frame_display.place(x=20+z,y=40)
     
         button_display=Button(frame_display,cursor='hand2',image=my_images[j],width=150,height=100)
         button_display.place(x=10,y=10)
         
                 
         cost_display=Button(frame_display,cursor='hand2',bd=0,bg='yellow',fg='black',text=cost[j],width=20,height=2)
         cost_display.place(x=10,y=125)
                    
       
         desc_display=Button(frame_display,cursor='hand2',bd=0,text=desc[j],width=20,height=2)
         desc_display.place(x=10,y=200)
         
         frames.append(frame_display)
         btns.append(button_display)
         costs.append(cost_display)
         descs.append(desc_display)
         
         z+=250

back_btn=Button(win,text='<',bd=0,state='disabled',command=display_backward)
back_btn.place(x=1000,y=10)

fore_btn=Button(win,text='>',bd=0,state='normal',command=display_forward)
fore_btn.place(x=1025,y=10)


back_btn.bind("<Enter>",lambda e: back_btn.config(bg='chartreuse4',activebackground='chartreuse4',fg='white'))
back_btn.bind("<Leave>", lambda e: back_btn.config(bg='SystemButtonFace',activebackground='SystemButtonFace',fg='black'))


fore_btn.bind("<Enter>",lambda e: fore_btn.config(bg='chartreuse4',activebackground='chartreuse4',fg='white'))
fore_btn.bind("<Leave>", lambda e: fore_btn.config(bg='SystemButtonFace',activebackground='SystemButtonFace',fg='black'))

win.mainloop()
