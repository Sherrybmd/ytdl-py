import os


# todo: add update/install and add to path for ytdlp command,
# add different quality of video command,
# add error handling in downSectionOfVideo,
# add installation and adding of FFMPEG in path,
# test on windows with none of the above installed,


class linuxytdl:
    def __init__(self):
        self.folder = "ytdl-downloads"

        self.linuxTerminal = "gnome-terminal -- bash -c '"
        self.linuxTerminalJank = "; exec bash'"
        self.windowsTerminal = None
        self.browserName = "firefox"
        self.link = ""

        self.ytdlp_command = "yt-dlp --cookies-from-browser " + self.browserName + " "
        self.extras = ""
        self.combined_command = ""

        # special little commands
        self.bestQualityVideo = "-S res,ext:mp4:m4a --recode mp4 "

    def downVideo(self):
        self.extras += self.bestQualityVideo
        self.download()

    def downSectionOfVideo(self):
        first = input("enter starting point's time(xx:xx)")
        last = input("enter end point's time(xx:xx)")
        # imagine theres error handling here
        section = first + "-" + last + " "
        self.extras += "--download-sections *" + section
        self.downVideo()

    def downAudio(self):
        self.extras += (
            "-f bestaudio --extract-audio --audio-format mp3 --audio-quality 320k "
        )
        self.download()

    def setLink(self, link):
        # add space too otherwise commands stick together and return error
        self.link = link + " "

    def getBrowserName(self):
        pass

    def construct_final_command(self):
        # for linux
        self.combined_command = (
            self.linuxTerminal
            + self.ytdlp_command
            + self.link
            + self.extras
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
    def __init__(self):
        super().__init__()
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
        print(self.combined_command)


"""
window command cmd open:  

For me this seems to work
os.system("cmd /k {command}")

With /k cmd executes and then remain open
With /c executes and close

To open a new command window and then execute the command
os.system("start cmd /k {command}")
"""
