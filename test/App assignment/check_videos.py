from tkinter import *
from PIL import Image, ImageTk
from video_library import Video, list_all
from pg_utils import PostgresDB as psdb

def checkVideos():
    window = Tk()
    window.title('Check Videos')
    window.geometry('850x500')

    def appear_all_videos():
        all_videos_output.delete('1.0', END)
        clicked = Label(master=window, font= 1, text='Check videos button was clicked')
        clicked.pack()
        clicked.place(x=10, y=420)
        list_videos = list_all()
        for video in list_videos:
            all_videos_output.insert("1.0", video+"\n")

    def check_video():
        db = psdb()
        length_videos = len(db.select_all_videos())
        id = entry.get()

        if id.isdigit() and int(id) >0 and int(id) <= length_videos:
            video_output.delete('1.0', END)
            error_label.config(text="")
            video = Video(id)
            video_infor_str = video.get_video_info_by_id()  
            video_output.insert("1.0", video_infor_str)
            path = rf"D:\UNI COURSES\COMP1752-OOP\Self code\test\pics\vid{id}.jpg"
            image = Image.open(path)

            image.thumbnail((250, 200))

            photo = ImageTk.PhotoImage(image)
            pic.config(image=photo)
            pic.photo = photo
        else:
            error_label.config(text="Invalid input")
    
    def check_director():
        db = psdb()
        director = director_entry.get()
        all_videos_by_director = db.select_video_by_name(director)
        if len(all_videos_by_director) != 0:
            video_item = f"{director}:\n"
            for row in all_videos_by_director:
                video_item += f"{row[0]} {row[1]} {'*' * int(row[3])}\n"
            all_videos_output.delete('1.0', END)
            all_videos_output.insert("1.0", video_item)
        else:
            error_label.config(text="Invalid input")


    #BUTTON
    list_all_videos = Button(window, text="List All Videos", font=16, command=appear_all_videos)
    check_video_button = Button(window, text="Check", command=check_video)
    check_director_button = Button(window, text="Check", command=check_director)
    check_video_button.config(width=6, height=1)  
    check_director_button.config(width=6, height=1)  

    #LABEL
    enter_video_label = Label(window, text='Enter Video Number', font=14)
    enter_video_label.pack()
    enter_director_label = Label(window, text='Enter Director Number', font=14)
    enter_director_label.pack()
    error_label = Label(window, text='')
    error_label.pack()
    pic = Label(window, text='')
    pic.pack()

    #ENTRY
    entry = Entry(window, width=4)
    entry.pack()
    director_entry = Entry(window, width=4)
    director_entry.pack()

    #TEXT
    all_videos_output = Text(window, font=13)
    all_videos_output.pack()
    video_output = Text(window, font=13)
    video_output.pack()

    # CREATE SCROLLBAR
    scrollbar1 = Scrollbar(window, command=all_videos_output.yview)
    scrollbar2 = Scrollbar(window, command=video_output.yview)

    # CONNECT SCROLLBAR WITH Text widget that will appear all videos output 
    all_videos_output.config(yscrollcommand=scrollbar1.set)
    video_output.config(yscrollcommand=scrollbar2.set)

    #POSITION
    list_all_videos.place(x=10, y=10)
    check_video_button.place(x=615, y=15)
    check_director_button.place(x=615, y=45)
    enter_video_label.place(x=250, y=14)
    enter_director_label.place(x=250, y=40)
    entry.place(x=465, y=20)
    director_entry.place(x=465, y=46,width=100)
    all_videos_output.place(x=10, y=80, width=480, height=300)  
    video_output.place(x=550, y=80, width=250, height=120) 
    scrollbar1.place(x=490, y=80, height=300)  
    scrollbar2.place(x=800, y=80, height=120)  
    error_label.place(x=700, y=30)  
    pic.place(x=550, y=230)

    window.mainloop()

