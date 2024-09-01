import pymongo

client = pymongo.MongoClient("mongodb+srv://akashmahto2272003:Akash5060@cluster0.wijkq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsAllowInvalidCertificates=True)

db = client["ytManager"]
video_collections = db["videos"]

print(video_collections)

def list_videos():
    for video in video_collections.find():
        print(f"Id: {video['_id']} \n Name: {video['name']} \n Time: {video['time']}")

def add_video(name , time): 
    video_collections.insert_one({"name": name, "time": time})


def update_video(video_id,name, time):
    video_collections.update_one(
            {'_id': video_id},
            {"$set": {"name": name, "time": time}}
        )

def delete_video(video_id):
    video_collections.delete_one({"_id": video_id})

def main():
    while True:
        print("\n youtueb manager app with mongoDb")
        print("1) list all videos")
        print("2) add new videos")
        print("3) update videos")
        print("4) delete videos")
        print("5) exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("enter updated video name")
            time = input("enter updated video time")
            add_video(name, time)
        elif choice == "3":
            video_id = input("enter video id")
            name = input("enter updated video name")
            time = input("enter updated video time")
            update_video(video_id,name, time)
        elif choice == "4":
            video_id = input("enter video id")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("your choose a wrong one")
        



if __name__ == "__main__":
    main()
    
    