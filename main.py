import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2

import ocr_handwriting

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        img = ocr_handwriting.recongnition(file_path)
        cv2.imwrite("answer.png", img)
        # hiển thị đáp án
        uploaded = Image.open("answer.png")
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        answerImg = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=answerImg)
        sign_image.image = answerImg
        label.configure(text='')

    except:
        pass



# background


top = tk.Tk()
top.geometry('800x600')
top.title('Handwriting Recognition')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

# button upload
upload = Button(top, text="Tải ảnh lên", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='black', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Handwriting Recognition", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='black')
heading.pack()
top.mainloop()
