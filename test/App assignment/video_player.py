from tkinter import *
from check_videos import checkVideos
from create_video_list import createVideoList
from update_video import updateVideo

window = Tk()
window.title('Video player')
window.geometry('600x200')

def openCheckVideo():
    checkVideos()

def create_video_list():
    createVideoList()

def update_video():
    updateVideo()

check_video_button = Button(window, text="Check Videos", font=16, command=openCheckVideo)
create_video_button = Button(window, text="Create Video List", font=16, command=create_video_list)
up_date_video_button = Button(window, text="Update Video", font=16, command= update_video)

label = Label(master=window, font= 1, text='Select an option by clicking one of the buttons below')

label.place(x=50, y=50)
check_video_button.place(x=50, y=100)
create_video_button.place(x=200, y=100)
up_date_video_button.place(x=380, y=100)

window.mainloop()