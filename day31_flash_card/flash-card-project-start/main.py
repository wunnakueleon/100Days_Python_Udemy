import tkinter


BACKGROUND_COLOR = "#B1DDC6"


window = tkinter.Tk()
window.title("Flash Card")


canvas = tkinter.Canvas(width=800, height=800, background=BACKGROUND_COLOR)
canvas.grid(column=0, row=0)

card_front_image = tkinter.PhotoImage(file="flash-card-project-start/images/card_front.png")
card_front_page = tkinter.Canvas(width=800, height=500)
card_front_page.create_image(400, 250, image=card_front_image)
card_front_page.grid(column=0, row=0)

card_back_image = tkinter.PhotoImage(file="flash-card-project-start/images/card_back.png")
card_back_page = tkinter.Canvas(width=800, height=500)
card_back_page.create_image(400, 250, image=card_back_image)
card_back_page.grid(column=0, row=0)

right_image = tkinter.PhotoImage(file="flash-card-project-start/images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0)
right_button.grid(column=0, row=0)












window.mainloop()

