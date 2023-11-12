from  junq_daemon import *
from argparse import ArgumentParser

def pargs():
    parser = ArgumentParser()

    parser.add_argument("-p", "--port", type=int, default=1109, help="Порт удаленных подключений")
    parser.add_argument("-v", "--verbose", type=int, default=2, help="Подробное логгирование (0-2)")
    # parser.add_argument("-l", "--local-socket", action="store_const", default=True, const=False, help="Использовать локальный сокет (default=True)")
    parser.add_argument("-u", "--unix-path", type=str, default="/tmp/junq.sock", help="Путь до unix сокета")
    # parser.add_argument("-a", "--add-info", type=int, default=1, help="amount of additional info into the messages")

    return parser.parse_args()

if __name__ == "__main__":
    args = pargs()
    d = Daemon(args)
    d.loop()
