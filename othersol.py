import tkinter as tk
from tkinter import messagebox, font
import time
class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x300")
        self.root.configure(bg="#87CEEB")  # Sky blue background
        self.sample_text = "The quick brown fox jumps over the lazy dog"
        self.start_time = None
        self.create_widgets()
    def create_widgets(self):
        # Define custom fonts
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        sample_font = font.Font(family="Arial", size=12)
        text_font = font.Font(family="Courier New", size=12)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")
        # Title Label
        self.title_label = tk.Label(self.root, text="Typing Speed Test", font=title_font, bg="#f0f0f0")
        self.title_label.pack(pady=10)
        # Sample Text Label
        self.sample_text_label = tk.Label(self.root, text=self.sample_text, font=sample_font, bg="#f0f0f0", wraplength=450, justify="left")
        self.sample_text_label.pack(pady=10)

        # Text Entry
        self.text_entry = tk.Text(self.root, height=5, width=60, font=text_font, wrap="word", bd=2, relief="solid")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_timer)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", font=button_font, bg="#4CAF50", fg="white", relief="raised", command=self.calculate_speed)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showinfo("Info", "You need to start typing first!")
            return

        typed_text = self.text_entry.get("1.0", "end-1c").strip()
        elapsed_time = time.time() - self.start_time

        # Calculate words per minute (WPM)
        words = len(typed_text.split())
        wpm = (words / (elapsed_time / 60))

        # Display result
        messagebox.showinfo("Typing Speed", f"You typed {words} words in {elapsed_time:.2f} seconds.\nTyping Speed: {wpm:.2f} WPM")

        # Reset the timer for the next test
        self.start_time = None
        self.text_entry.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()





# from tkinter import *
# from tkinter import messagebox
# import random
# import time



# def check(pas1,pas2):
#     pass


# def countdown(count):
#     while count>0:
#     # change text in label        
#         label['text'] = count
#         print(count)

#         # if count==0:
            
#         # if count > 0:
#             # call countdown again after 1000ms (1s)
#         # window.after(1000)
#         count-=1
#     else:
#         return True
#     # elif count==0:
    
        
        
# window=Tk()
# window.minsize(200,200)

# seconds=StringVar()
# seconds.set("00")
# seconds_entry=Entry(width=3,textvariable=seconds)

# et=Entry(width=30,justify=CENTER,)
# et.pack()
# t=10
# while t>=0:

#     window.update()
#     time.sleep(1)
#     if t==0:
#         messagebox.showinfo("Time'sup")
#         # show_time=Label("Mudichiduchu")
#         # show_time.pack()
#     t-=1

# window.mainloop()
# # def passage():
    
# #     with open("test1sp.txt","r") as f:
# #     # w=f.writelines(["At first the professor scowled with concern. But then he said, that's all right. Run to my house. Tell my wife to give you one of my shirts. 'Mrs. Esputa quickly fetched one of her husband's white shirts. \nBut when Philip put it on, she began to exclaim, 'Oh, dear! Gracious!' The shirt was so large that Philip was almost lost in it. \nHastily Mrs. Esputa found a box of pins. In a twinkling, her nimble fingers pinned enough tucks in the shirt to make it fit Philip","\nThey both heaved a big sigh of relief when the job was finished. Then, free from anxiety, Philip hurried back to the school. The concert finally began, and soon it was time for Philip's also. \nStood up, placed the violin under his chin, and raised his bow. With horror he felt a pin pulling loose in the back of his shirt. \nBut he recalled how many pins had been inserted in the shirt and thought, 'Losing one won't matter.' Philip started to play. At first his right arm moved back and forth slowly, then more swiftly.","\nBefore long the pins that were holding his collar pulled out, The loose, large shirt collar began to creep up the back of Philip's head. Then the unruly sleeves grew looser and longer. \nSuddenly the shirt fell away from his neck. The audience began to laugh. In embarrassed confusion, \nPhilip forgot what he was playing and stopped completely. The disaster so upset him that he rushed off the stage and sulked in a dark corner. \nFighting back tears, he mumbled gloomily, 'I wish I were dead Refreshments were served after the concert, but Philip was too busy to have any.","\nHe mingled with the crowd as quickly as he could, hoping to avoid Mr. Esputa. After a wistful look at the ice cream, Phillip was about to slink out when a booming voice behind him scoffed, \n'Well, Philip, you made a nice mess of it. ' Philip turned and found himself face to face with his glowering teacher. \nWith no sympathy for poor Philip, Mr. Esputa continued unreasonably, \n'No refreshments for you! You shouldn't have spent the day playing ball. You should have been preparing for the important work of the evening."," \nYou ought to be ashamed! MP hung his head, sighed heavily, and trudged home. \nThe incident at Such an impression on him that he always remembered it. He never gain tried to mix work and play."])
# #     # f.close()
# #         w=f.read().split("\n\n")
# #         print(w)
# #         f.close()
# #     return w[0]



# # window=Tk()
# # window.title("Type Speed Test⌛")
# # window.minsize(900,560)

# # title_=Label(text="Type Speed Test⌛",font=("arial",40))

# # title_.grid(column=5,row=1)

# # disc_=Label(text="How fast are your fingers? \nDo the one-minute typing test to find out! Press the space bar after each word. \nAt the end, you'll get your typing speed in CPM and WPM. \nGood luck!",font=("arial",15))
# # disc_.grid(column=5,row=3)

# # words_=Label(text=f"\n\nSample text:\n\n{passage()}",font=("arial",14))
# # words_.grid(column=5,row=6)




# # text_entry=Entry( width=40, font=('arial', 20),justify=CENTER)
# # text_entry.grid(column=5,row=8)



# # t = 10
# # label = Label(window,font=("arial",20))
# # # label.place(x=35, y=15)
# # label.grid(column=5,row=7)
# # is_time_up=False
# # # countdown(t)
# # if countdown(t):
# #     print("Mudichuduchu")
 


# # window.mainloop()