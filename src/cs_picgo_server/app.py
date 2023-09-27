import json
import os
import shutil
import threading
import time
import traceback

from PIL import ImageGrab
from PIL.PngImagePlugin import PngImageFile
from flask import Flask, request
from pypicgo.core.base.uploader import CommonUploader
from pypicgo.core.config import Settings
from pypicgo.core.execute import create_uploader
from pypicgo.core.logger import logger
from pypicgo import BASE_DIR

from cs_picgo_server import utils

app = Flask(__name__)


# bug
def clean_tempfile(self, file):
    if file.origin_file.resolve() != file.tempfile.resolve():
        if os.path.exists(file.tempfile.resolve()):
            os.remove(file.tempfile.resolve())


CommonUploader.clean_tempfile = clean_tempfile


def run_action(uploader_name, filepath):
    settings = Settings(uploader_name=uploader_name)
    uploader = settings.uploader_class
    uploader_config = settings.uploader_config
    plugins = settings.plugins
    CommonUploader.results = []
    try:
        with create_uploader(uploader, uploader_config, plugins) as uploader:
            logger.info('upload start')
            logger.info(f'upload file [{filepath}]')
            uploader.do(filepath)
            remote_url = uploader.result.remote_url
            logger.info(f'remote_url is {remote_url}')
            logger.info(f'uploader.results is {uploader.results}')
            return remote_url
    except Exception as e:
        logger.error(f'have error, err={str(e)}')
        logger.error(traceback.format_exc())


def copy_image(src):
    file_extension = os.path.splitext(src)[1]
    if file_extension.lower() not in ('.png', '.jpg', '.jpeg', '.bmp'):
        raise Exception(f'not support file_extension={file_extension}')
    tmp_image = os.path.join(BASE_DIR, f'tmp{file_extension}')
    shutil.copy(src, tmp_image)
    logger.info(f'tmp_image path is {tmp_image}')
    return tmp_image


@app.route('/upload', methods=['POST'])
def upload():
    get_data = request.get_data()
    logger.info(f"upload interface get_data={get_data}")
    image = ImageGrab.grabclipboard()
    logger.info(f"upload interface get_image_clipboard={image}")

    if isinstance(image, PngImageFile):
        path = os.path.join(BASE_DIR, 'tmp.png')
        image.save(path)
    elif isinstance(image, list):
        path = image[0]
        path = copy_image(path)
    else:
        raise Exception(f'can not get path, image clipboard is {image}')

    remote_url = run_action('gitee', path)
    data = {'success': True, 'result': remote_url}
    logger.info(f'return request.body is {data}')
    return json.dumps(data, ensure_ascii=False)


class Backend(threading.Thread):
    def __init__(self, hook=None):
        super().__init__()
        self.hook = hook or logger.info
        self.wait_to_start_time = 3

    def run(self) -> None:
        port = 36677
        test_result = utils.test_bind_port(port)
        logger.info(f'wait {self.wait_to_start_time} seconds to start')
        time.sleep(self.wait_to_start_time)
        if test_result:
            self.hook(f'start success')
            app.run(debug=True, port=port, use_reloader=False)
        else:
            while True:
                self.hook(f'start failed, bind port={port} failed')
                time.sleep(30)


if __name__ == '__main__':
    Backend().start()
