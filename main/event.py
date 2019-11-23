from observer import Observer

class Event:
    def __init__(self):
        self.subscriberList = []

    def subscribe(self, observer):
        self.subscriberList.append(observer)

    def notify(self, eventData):
        for subscriber in self.subscriberList:
            subscriber.notify(eventData)

    def unsubscribe(self, observer):
        self.subscriberList.remove()
