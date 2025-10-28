import os
from ytdl import linuxytdl, windowsytdl, checkForUpdate
# it's better to give browser name to constructor


def ask():
    print("choose operation")
    choice = input(
        "q to quit\n1_download best quality of video\n2_download best quality of audio\n3_download section of video\n4_update (if download fails)\n>"
    )
    if choice == "q":
        return -1

    elif choice == "1":
        return 1

    elif choice == "2":
        return 2

    elif choice == "3":
        return 3

    elif choice == "4":
        return 4
    else:
        print("bad input")
        ask()


def main(browsername):
    if os.name == "posix":  # linux check
        session = linuxytdl(browsername)
    elif os.name == "nt":  # windows check
        session = windowsytdl(browsername)
    else:
        print("os not supported")
        return 404

    # get link
    storeAsk = ask()

    if storeAsk == -1:
        return -1

    elif storeAsk == "q":
        return -1

    elif storeAsk == 1:
        link = input("enter the link for video\n>")
        if link == "q":
            return -1
        session.setLink(link)
        session.downVideo()

    elif storeAsk == 2:
        link = input("enter the link for video\n>")
        if link == "q":
            return -1
        session.setLink(link)
        session.downAudio()

    elif storeAsk == 3:
        link = input("enter the link for video\n>")
        if link == "q":
            return -1
        session.setLink(link)
        session.downSectionOfVideo()

    elif storeAsk == 4:
        checkForUpdate(session)

    os.system("clear")
    main(browsername)


# band aid fix for folder management, big room for improving
if os.path.exists("./ytdl-downloads/") is False:
    os.system("mkdir ytdl-downloads")
    os.chdir("ytdl-downloads")
else:
    os.chdir("ytdl-downloads")

browser = int(input("browser name: \n1_firefox\n2_chrome"))
os.system("clear")
if browser == 1:
    main("firefox")

elif browser == 2:
    main("chrome")
