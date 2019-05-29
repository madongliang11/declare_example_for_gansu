from common.Container import Container
from common.Start import Start


class Main(Start):

    def __init__(self):
        super(Main, self).__init__()
        # Container.PAGE_LOGIN_URL = 'http://www.baidu.com'
        # Container.PAGE_HOME_URL = 'http://www.baidu.com'
        Container.TAX_AREA_CODE = 42

    def main(self):
        self.start()


if __name__ == '__main__':
    Main().main()

# pip install -r requirements.txt
