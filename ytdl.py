import os


class ytdl:
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
        # imagine theres some link validation here
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

        # for windows (WIP)
        #
        #

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
