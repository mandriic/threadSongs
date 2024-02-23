import os
import sys
import json
import requests
import time
ex = False
while not ex:
    user_input = input("What you want to do? (get, post, patch, delete, exit): ")
    if user_input == "get":
        url = "http://localhost:8000/songs/"
        response = requests.get(url)
        print(json.dumps(response.json(), indent=4))
    elif user_input == "post":
        url = "http://localhost:8000/songs/"
        title = input("Title: ")
        artist = input("Artist: ")
        album = input("Album: ")
        duration = int(input("Duration: "))
        data = {"title": title, "artist": artist, "album": album, "duration": duration}
        response = requests.post(url, json=data)
        print("Was posted", response.json())
    elif user_input == "patch":
        url = "http://localhost:8000/songs/"
        title = input("Title: ")
        album = input("Album: ")
        duration = int(input("Duration: "))
        data = {"title": title, "album": album, "duration": duration}
        response = requests.patch(url, json=data)
        print("Patched", response.json())
    elif user_input == "delete":
        url = "http://localhost:8000/songs/"
        title = input("Title: ")
        data = {"title": title}
        response = requests.delete(url, json=data)
        print("Deleted")
    elif user_input == "exit":
        sys.exit()
    else:
        print("Invalid input")

        