import pyttsx3 
import datetime 
#thư viện nhận diện giọng nói
import speech_recognition as sr  # type: ignore
#search google tự động 
import webbrowser as wb 


#khởi tạo pyyttsx3
friday = pyttsx3.init() 

#getProperty() : lấy và đặt thuộc tính giọng nói
voice = friday.getProperty('voices') 

#setProperty() : chọn giọng nam hay nữ 
friday.setProperty('voice', voice[1].id)

def speak(audio): 
    """ Chức năng giọng nói và in thông báo"""
    print('N.H.A.T.L.I.N.H '+ audio )
    friday.say(audio)
    friday.runAndWait() 
# hamf runAndWait trong thu viên pyttsx3 
#dùng để chạy lệnh Speak trong hàng đợi, 
# đợi tất cả các lệnh nói hoàn thnahf mới chạy lệnh khác

def time(): 
    """Thông báo thời gian hiện tại"""
    curent_time = datetime.datetime.now().strftime("%I:%M:%P")
    speak(curent_time)

def welcome():
    hour = datetime.datetime.now().hour 
    if hour >= 6 and hour < 12: 
        speak("Good morning Daddy")
    elif hour >= 12 and hour < 18: 
        speak("Good Afternoon Daddy")
    elif hour >= 18 and hour < 24:
        speak("Good Night Daddy ")

    speak(' How can i help, Daddy ?')

def command():
    #tạo oject nhận giọng nói 
    c = sr.Recognizer() 

    #giọng lấy từ đâu
    with sr.Microphone() as source: 
        c.pause_threshold = 2
        print("Listening...")
        audio = c.listen(source)
    try: 
        query = c.recognize_google(audio,language='en')
        print('Linh Daddy: '+ query)
    except sr.UnknownValueError: # Nếu mà không nghe được
        print(" Please repeat or typing the command ")
        #khi Trợ lý không nghe thấy thì chúng ta có thể gõ lệnh vào luôn         
        query = str(input(' Daddy order is: '))
    return query

if __name__=="__main__":
    welcome() 
    while True: 
        query = command().lower()
        if "google " in query: 
            speak("What should I search, Daddy? ")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        if "Youtube " in query: 
            speak("What should I search daddy? ")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Youtube')
        elif "time" in query: 
            time()
        elif "quit" in query: 
            speak (" Goodbye Daddy moaz moazz moazz ")
            break