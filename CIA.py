import random
list1 = ["Edward","Ethan","Benji","Sean","James"]
list2 = ["Smith","Hunt","Dunn","Ambrose","Bond"]
class CIA:
    def AgentName(self):
        self.first = random.choice(list1)
        self.last = random.choice(list2)

    @property
    def fullname(self):
        return f"the full name of the agent is {self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        first,last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        del self.first,self.last
agent = CIA()
agent.AgentName()
print(agent.fullname) #getter
del agent.fullname   #deleter
# print(agent.fullname)

agent.fullname = f"{random.choice(list1)} {random.choice(list2)}" #setter
print(agent.fullname)


