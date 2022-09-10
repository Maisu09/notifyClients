import time
from TimeServer import TimeServer
from ClientOne import ClientOne
from ClientTwo import ClientTwo


def main():
    subscribers = []
    subscribers.append(ClientOne())
    subscribers.append(ClientTwo())
    subscribers.append(ClientOne())
    subscribers.append(ClientTwo())
    subscribers.append(ClientOne())
    subscribers.append(ClientTwo())

    timeServer = TimeServer(subscribers)

    for i in range(5):
        timeServer.notifySubscribers()
        print('\n')
        time.sleep(1.4)


if __name__ == '__main__':
    main()
