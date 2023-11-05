from tkinter import *
from video_library import Video, list_all
from pg_utils import PostgresDB as pgdb


list_videos = []

window = Tk()
window.title('Create video list')
window.geometry('500x450')

def addVideo():
    db = pgdb()
    
    id = entry.get()
    if id.isdigit():
        all_videos_output.delete("1.0", "end")
        video = Video(id)
        list_videos.append([id, video])

        videoNames = getVideoNameList()
        all_videos_output.insert("1.0", videoNames) 
    else:
        all_videos_output.insert("1.0", "Invalid input") 


def getVideoNameList():
    video_name_str = ""
    for video in list_videos:
        video_name_str += f"{video[0]} {video[1]}.\n"
    return video_name_str

#LABEL
enter_video_label = Label(window, text='Enter Video Number', font=14)
enter_video_label.pack()

#ENTRY
entry = Entry(window, width=4)
entry.pack()

#TEXT
all_videos_output = Text(window, font=13)
all_videos_output.pack()

#BUTTON
check_video_button = Button(window, text="Check Videos", font=1, command=addVideo)
play_list_button = Button(window, text="Check Videos", font=1, command=addVideo)
reset_list = Button(window, text="Check Videos", font=1, command=addVideo)


enter_video_label.place(x=20, y=14)
entry.place(x=210, y=20)
all_videos_output.place(x=10, y=80, width=480, height=300)  
check_video_button.place(x=250,y=12)

window.mainloop()

