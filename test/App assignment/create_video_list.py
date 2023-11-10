from tkinter import *
from video_library import Video
from pg_utils import PostgresDB as pgdb

def createVideoList():
    list_videos = []

    window = Tk()
    window.title('Create video list')
    window.geometry('500x220')

    def addVideo():
        db = pgdb()
        lenVideosInDB = len(db.select_all_videos())
        id = entry.get()
        if checkVideoInList(id):
            error_label.config(text="Video was added") 
        elif id.isdigit() and int(id) <= lenVideosInDB and int(id) >0:
            error_label.config(text="") 
            all_videos_output.delete(1.0, END) 
            video = Video(id)
            list_videos.append(video)
            videoNames = getVideoNameList()
            all_videos_output.insert("1.0", videoNames) 
        else:
            error_label.config(text="Invalid input, type again") 

    def checkVideoInList(id):
        for video in list_videos:
            if video.id == id:
                return 

    def getVideoNameList():
        video_name_str = ""
        for video in list_videos:
            video_name_str += f"{video.id} {video.name}.\n"
        return video_name_str

    def playList():
        for video in list_videos:
            video.play_count += 1
            print(video.play_count)

    def clear():
        list_videos.clear()
        all_videos_output.delete('1.0', END)

    #LABEL
    enter_video_label = Label(window, text='Enter Video Number', font=14)
    enter_video_label.pack()
    error_label = Label(window, text='')
    error_label.pack()


    #ENTRY
    entry = Entry(window, width=4)
    entry.pack()

    #TEXT
    all_videos_output = Text(window, font=13)
    all_videos_output.pack()

    #BUTTON
    font_but = ("Arial", 10)
    check_video_button = Button(window, text="Check Videos", font=font_but, command=addVideo)
    play_list_button = Button(window, text="Play the playlist", font=font_but, command=playList)
    reset_list = Button(window, text="Reset", font=font_but, command=clear)

    enter_video_label.place(x=20, y=14)
    entry.place(x=210, y=20)
    all_videos_output.place(x=10, y=80, width=480, height=100)  
    check_video_button.place(x=250,y=15)
    play_list_button.place(x=350,y=15)
    reset_list.place(x=400,y=50)
    error_label.place(x=250,y=50)

    window.mainloop()

createVideoList()
