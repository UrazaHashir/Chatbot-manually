import time
now = time.ctime()


qn = {
    "hi":"hello",
    "how are you":"i m fine",
    "what is your name":" my name is Chatbot",
    "how old are you":"i m 20 years old",
    "what is the time now": now,
}

while True:
    qs = input()


    if(qs == "quit"):
        break
    else:
        print(qn[qs])
        
