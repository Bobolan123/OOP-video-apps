from tkinter import *
from video_library import Video
from pg_utils import PostgresDB as pgdb

def updateVideo():
    window = Tk()
    window.title('Update Video')
    window.geometry('500x450')

    def addVideo():
        db = pgdb()
        lenVideosInDB = len(db.select_all_videos())
        id = id_entry.get()
        rate = rating_entry.get()
        if id.isdigit() and int(id) <= lenVideosInDB and int(id) >0 and float(rate) >= 0 and float(rate) <=5:
            error_label.config(text="") 
            video_output.delete(1.0, END) 
            video = Video(id)
            video_infor = getVideoInfor(video, float(rate))
            video_output.insert("1.0", video_infor)
        else:
            error_label.config(text="Invalid input, type again") 

    def getVideoInfor(video, rate):
        # rate = rating_entry.get()
        video.rate = rate
        return f"{video.id} {video.name}\nRate: {video.rate}\nPlay count: {video.play_count}"

    #LABEL
    enter_video_label = Label(window, text='Enter Video Number', font=14)
    enter_video_label.pack()
    enter_rating_label = Label(window, text='Enter New Rating', font=14)
    enter_rating_label.pack()
    error_label = Label(window, text='')
    error_label.pack()

    #ENTRY
    id_entry = Entry(window, width=4)
    id_entry.pack()
    rating_entry = Entry(window, width=4)
    rating_entry.pack()

    #TEXT
    video_output = Text(window, font=13)
    video_output.pack()

    #BUTTON
    font_but = ("Arial", 10)
    update_video_button = Button(window, text="Update Video", font=font_but, command=addVideo)


    enter_video_label.place(x=20, y=14)
    enter_rating_label.place(x=20, y=40)
    id_entry.place(x=210, y=20)
    rating_entry.place(x=210, y=46)
    video_output.place(x=10, y=80, width=480, height=300)  
    update_video_button.place(x=250,y=30)
    error_label.place(x=340, y =33)

    window.mainloop()


