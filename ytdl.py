import os


class ytdl:
    def __init__(self):
        self.linuxTerminal = "gnome-terminal -- bash -c '"
        self.windowsTerminal = None
        self.browserName = "firefox"
        self.link = None

        self.ytdlp_command = "yt-dlp --cookies-from-browser " + self.browserName
        self.extras = ""
        self.combined_command = ""

        # now special little commands
        self.bestQualityVideo = "-S res,ext:mp4:m4a --recode mp4 "

    def downVideo(self):
        self.extras += self.bestQualityVideo

    def downSectionOfVideo(self):
        first = input("enter starting point's time(xx:xx)")
        last = input("enter end point's time(xx:xx)")
        # imagine theres error handling here
        section = first + "-" + last + " "
        self.extras += "--download-sections *" + section

    def downAudio(self):
        self.extras += (
            "-f bestaudio --extract-audio --audio-format mp3 --audio-quality 320k "
        )

    def setLink(self, link):
        link = input(("enter the youtube video's link!"))
        # imagine theres some link validation here
        self.link = link

    def getBrowserName(self):
        pass

    def construct_final_command(self):
        self.combined_command += self.linuxTerminal + self.ytdlp_command + self.extras

    def download(self):
        self.construct_final_command()
        print(self.combined_command)  # temporary surely
        os.system(self.combined_command)
