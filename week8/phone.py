# Object
# -> Specific intance of a class

# Class
# -> General definition
"""
1. Create 2 instances of the iPhone.

2. Change iPhone names through set_name()

3. Send a iMessage from phone1 to phone2

4. phone2 should be able to check messages. Print the messages on screen.

"""


class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []

    def check_messages(self):
        print(f'All the messages are {self.messages}')

    def call(self, number):
        pass

    def airdrop(self, filename, recipient):
        print(f"Dropping '{filename}' To: {recipient.name}")
        recipient.airreceive(filename, self.name)

    def airreceive(self,message, sender):
        self.messages.append(message)
        print(f'{self.name} has received a message from {sender}')
        

    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 character")
        self.name = new_name


# 1. Create 2 instances of the iPhone.
nbs_iphone = iPhone(
    name="nb's iPhone",
    version="18",
    phone_number="123-123-5200",
    color="blue",
    model="iPhone 16 Pro",
)

jason_iphone = iPhone(
    name="jason's iPhone",
    version="18",
    phone_number="425-231-213",
    color="pink",
    model="iPhone 16 Pro",
)
print(nbs_iphone.name)

# 2. Change iPhone names through set_name()
nbs_iphone.set_name("nb's second iPhone")
print(nbs_iphone.name)


# 3. Send a iMessage from phone1 to phone2
nbs_iphone.airdrop("jason, do you want to eat with me?", recipient=jason_iphone)

# 4. phone2 should be able to check messages. Print the messages on screen.
jason_iphone.check_messages()
