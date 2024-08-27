file = open("youtube.txt", "w")

try: 
    file.write("chai or code")
finally:
    file.close()
    
    
    
with open('youtube.txt', 'w') as file:
    file.write("chai or python")