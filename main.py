import os
from ytdl import linuxytdl, windowsytdl
# it's better to give browser name to constructor


def ask():
    print("choose operation")
    choice = input(
        "q to quit\n1_download best quality of video\n2_download best quality of audio\n3_download section of video\n>"
    )
    if choice == "q":
        return -1

    elif choice == "1":
        return 1

    elif choice == "2":
        return 2

    elif choice == "3":
        return 3
    else:
        print("bad input")
        ask()


def main():
    print("q to quit when you're entering the link!\n")
    # get browsers name

    # vvv remove after uncommenting main lines below
    session = windowsytdl()
    # vvv main lines
    """
    if os.name == "posix":  # linux check
        session = linuxytdl()
    elif os.name == "nt":  # windows check
        session = windowsytdl()
    else:
        print("os not supported")
        return 404
    """

    # get link
    link = input("enter the link for video\n>")
    if link == "q":
        return -1

    # imagine validation of link here
    session.setLink(link)

    storeAsk = ask()
    if storeAsk == -1:
        return -1

    elif storeAsk == 1:
        session.downVideo()

    elif storeAsk == 2:
        session.downAudio()

    elif storeAsk == 3:
        session.downSectionOfVideo()

    #    os.system("clear")
    main()


# band aid fix for folder management, big room for improving
if os.path.exists("./ytdl-downloads/") is False:
    os.system("mkdir ytdl-downloads")
    os.chdir("ytdl-downloads")
else:
    os.chdir("ytdl-downloads")

main()
