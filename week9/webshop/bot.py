class Echoer:
    def transform(self, message):
        return message


class Reverser:
    def transform(self, message):
        return message[::-1]


class Shouter:
    def transform(self, message):
        return message.upper()


def run(transformer):
    while True:
        request = input("> ")
        if request == "":
            break
        response = transformer.transform(request)
        print("<", response)


run(Reverser())

# test Echoer
echoer = Echoer()
res = echoer.transform("HI")
print(res)

# test Reverser
reverser = Reverser()
res = reverser.transform("HI")
print(res)
