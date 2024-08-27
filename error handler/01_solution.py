import json


def load_data():
    try:
        with open('youtube,txt', 'r') as file:
            test = json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, videos in enumerate(videos, start=1):
        print(f"{index}.")
    
def add_videos(videos):
    name = input("Enter video name")
    time = input("Enter video time")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    pass

def delete_videos(video):
    pass

def main():
    videos = load_data()

    while True:
        print("\n Youtube manager | chose an option by enter option number")
        print("1. List a favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        option = input("Enter you option")
        print(videos)
        
        
        match option:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("Invalid option please select from the option")

if __name__ == "__main__":
    main()

