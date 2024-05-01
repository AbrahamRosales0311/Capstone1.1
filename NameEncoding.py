import time

class NameEncoding:
    def nameExtension(self, filePath):  # method to better name images
        username = "jdvande"            # placeholder for username
        currentTime = time.strftime('%a%d%b%Y-%HH%MM%SS')
        extension = filePath + username + "-" + currentTime + ".png"

        return str(extension)