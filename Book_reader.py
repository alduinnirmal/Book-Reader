import io
from gtts import gTTS
from playsound import playsound
fp = io.open("Book.txt",mode="r",encoding="utf-8")
content = fp.read()
ob = gTTS(content,lang="ml")
ob.save("book.mp3")
playsound("book.mp3")