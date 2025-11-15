import time
import os

# in downAudio() we must have alternative formats to mp3, if it doesnt exist we encounter error
# need to store all command and add spaces where they are required at the end
# instead of manually changing in each function which is a mess

# make sure self.extras is empty for each download, theres no such bug, chatgpt is retarded
#
# add installation and adding of FFMPEG in path,
# test on windows with none of the above installed,
# if chrome is being used, avoid extracting cookies
# add custom name output
#
# seems like exec bash keeps terminals that spawn open, removing it leads to them closing after finishing task.


class linuxytdl:
    def __init__(self, browsername):
        self.folder = "ytdl-downloads"

        self.linuxTerminal = "gnome-terminal -- bash -c '"
        self.linuxTerminalJank = ";exec bash'"
        self.browserName = browsername
        self.link = ""

        self.ytdlp_command = "yt-dlp --cookies-from-browser " + self.browserName + " "
        self.extras = ""
        self.combined_command = ""

        # self.bestQualityVideo = "-S res,ext:mp4:m4a --recode mp4 "

    def downVideo(self, quality, name):
        self.extras += quality
        self.getOutputName(name, "mp4")
        self.download()

    def setVidQuality(self):
        choice = input(
            "enter video quality (enter none for best) \n1_480\n2_720\n3_1080"
        )

        if choice == "480" or choice == "1":  # 480
            return '-f "bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]" '
        elif choice == "720" or choice == "2":  # 720
            return '-f "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]" '
        elif choice == "1080" or choice == "3":  # 1080
            return '-f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]" '
        else:
            # choice = "best"
            return "-S res,ext:mp4:m4a --recode mp4 "

    def downSectionOfVideo(self, name):
        first = input("enter starting point's time(xx:xx)")
        last = input("enter end point's time(xx:xx)")
        section = first + "-" + last

        self.extras += "--download-sections *" + section + " "
        quality = self.setVidQuality()
        self.downVideo(quality, name)

    def downAudio(self, name):
        self.extras += (
            "-f bestaudio --extract-audio --audio-format mp3 --audio-quality 320k "
        )
        self.getOutputName(name, "")
        self.download()

    def setLink(self, link):
        # add space too otherwise commands stick together and return error
        self.link = link + " "

    def getOutputName(self, name, format):
        if format == "":
            self.extras += f"-o {name} "
        else:
            self.extras += f"-o {name}.{format} "

    def construct_final_command(self):
        # for linux
        self.combined_command = (
            self.linuxTerminal
            + self.ytdlp_command
            + self.extras
            + self.link
            + self.linuxTerminalJank
        )

    def download(self):
        # opens the terminal, to download using yt-dlp

        self.construct_final_command()
        os.system(self.combined_command)

    def makeFolder(self):
        if (
            os.path.exists("./ytdl-downloads") is False
            and os.path.exists("../ytdl-downloads") is False
        ):
            os.system("mkdir ytdl-downloads")

    def changeToFolder(self):
        os.chdir("ytdl-downloads")


class windowsytdl(linuxytdl):
    def __init__(self, browsername):
        super().__init__(browsername)
        del self.linuxTerminal, self.linuxTerminalJank

        # /c has been suggested for automatic cleanup, however /k is good for debugging as it keeps window open
        self.windowsTerminal = "cmd /k "
        self.windowsTerminalJank = ""

    def construct_final_command(self):
        self.combined_command = (
            self.windowsTerminal
            + self.ytdlp_command
            + self.link
            + self.extras
            + self.windowsTerminalJank
        )
        # return super().construct_final_command()
        # ^^^ why did my LSP auto enter return? it returns an object,
        # who does the object represent? parent?

    # vvv to avoid shell error due to invalid commands, must be removed after fixing windows command
    def download(self):
        self.construct_final_command()
        os.system(self.combined_command)


def checkForUpdate(session):
    print("checking for update", end="")
    for i in range(3):
        time.sleep(1)
        print(".", end="")
    print()

    if os.name == "posix":
        os.system(
            session.linuxTerminal + " pipx upgrade yt-dlp" + session.linuxTerminalJank
        )
    elif os.name == "nt":
        # unclear if it does function correctly
        os.system(session.windowsTerminal + " yt-dlp -U" + session.windowsTerminalJank)
    else:
        print("os not supported, update failed")


"""
window command cmd open:  

For me this seems to work
os.system("cmd /k {command}")

With /k cmd executes and then remain open
With /c executes and close

To open a new command window and then execute the command
os.system("start cmd /k {command}")

but it's not very useful if your command is a complex one with spaces or other control characters. For that I use:
subprocess.run(["start", "/wait", "cmd", "/K", command, "arg /?\\^"], shell=True)

"""
