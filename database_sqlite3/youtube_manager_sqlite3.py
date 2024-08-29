import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id  INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL 
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name , time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (? , ?)", (name, time))
    con.commit()

def update_video(videoId, newName , newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (videoId, newName, newTime))
    con.commit()

def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoId,))
    con.commit()

def main():
    while True:
        print("\n youtube manager app with DB")
        print("1. List a favorite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        option = input("Enter you option: ")
    
        if option == '1':
            list_videos()
        elif option == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name , time)
        elif option == '3':
            videoId = input("Enter video id to update the video: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(videoId, name , time)
        elif option == '4':
            videoId = input("Enter video id to update the video: ")
            delete_video(videoId)
        elif option == '5':
            break
        else:
            print("Invalid option")
    con.close()

if __name__ == "__main__":
    main()