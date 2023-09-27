import subprocess
import webbrowser

import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem, Menu, Icon

from cs_picgo_server.app import logger, Backend, BASE_DIR


class TaskBar:
    def __init__(self):
        self.exe_name = 'PicBed'
        self.url = "https://github.com/m986883511/cs-picgo-server"
        self.menu = self.get_menu()
        self.icon: pystray.Icon = self.get_icon()

    def main_page(self):
        logger.info(f'open {self.url}')
        webbrowser.open(self.url)

    def on_exit(self):
        logger.info('on_exit')
        self.icon.stop()

    def notify(self, msg):
        self.icon.notify(msg, self.exe_name)

    def open_dir(self):
        logger.info(f'open dir {BASE_DIR}')
        subprocess.Popen(f'explorer "{BASE_DIR}"')

    @staticmethod
    def create_image(width=64, height=64, color1='black', color2='white'):
        # Generate an image and draw a pattern
        image = Image.new('RGB', (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
        dc.rectangle((0, height // 2, width // 2, height), fill=color2)
        return image

    def get_menu(self):
        menu = (
            MenuItem(text='项目主页', action=self.main_page),
            MenuItem(text='配置目录', action=self.open_dir),
            Menu.SEPARATOR,
            MenuItem(text='退出程序', action=self.on_exit),
        )
        return menu

    def get_icon(self):
        icon = Icon("name", self.create_image(), self.exe_name, self.menu)
        return icon

    def run(self):
        backend = Backend(self.notify)
        backend.setDaemon(True)
        backend.start()
        self.icon.run()


if __name__ == '__main__':
    TaskBar().run()
