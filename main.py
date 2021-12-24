from Window import Window
import pyaudio


def getdevice():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(i, p.get_device_info_by_index(i)['name'])


def main():
    app = Window()


if __name__ == '__main__':
    getdevice()
    main()
