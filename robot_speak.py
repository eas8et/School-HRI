from naoqi import ALProxy, ALBroker, ALModule


# word_pattern = re.compile(r"> (.+?) <")

class RobotSpeak(ALModule):
    def __init__(self, name, ip, port):
        print(" ------ RobotSpeak __init__")
        ALModule.__init__(self, name)
        self.ip = ip
        self.port = port
        self.speak = ALProxy("ALTextToSpeech", self.ip, self.port)
        self.anim_speak = ALProxy("ALAnimatedSpeech", self.ip, self.port)

    def say_words(self, words):
        print(" ------ say_words")
        self.speak.say(words)

    def anim_say(self, words):
        print(" ------ anim_say")
        self.anim_speak.say(words)