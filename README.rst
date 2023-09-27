.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/cs-picgo-server.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/cs-picgo-server
    .. image:: https://readthedocs.org/projects/cs-picgo-server/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://cs-picgo-server.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/cs-picgo-server/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/cs-picgo-server
    .. image:: https://img.shields.io/pypi/v/cs-picgo-server.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/cs-picgo-server/
    .. image:: https://img.shields.io/conda/vn/conda-forge/cs-picgo-server.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/cs-picgo-server
    .. image:: https://pepy.tech/badge/cs-picgo-server/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/cs-picgo-server
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/cs-picgo-server

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

===============
cs-picgo-server
===============


    pypicgo的api封装

   pip install git+https://gitee.com/supernatural-fork/cs-picgo-server.git

   pip install git+https://github.com/supernatural-fork/cs-picgo-server.git

   use cs-picgo-server to start

   示例配置文件

.. code-block:: yaml

   default: # 默认配置
     uploader: gitee # 默认图床
     plugins: # 全局插件
       - module: pypicgo.plugins.rename.ReNamePlugin # 图床插件加载地址
         config:
           format: cs-{date}-{filename}
       - module: pypicgo.plugins.compress.CompressPlugin
       - module: pypicgo.plugins.notify.NotifyPlugin

   uploaders: # 可用图床
     gitee: # gitee 图床配置
       module: pypicgo.uploaders.gitee.uploader.GiteeUploader
       config:
         domain: https://gitee.com
         owner: m986883511
         repo: picture-bed
         img_path: PyPicGo
         access_token: ***************************************
       plugins:
     github: # github图床配置
       module: pypicgo.uploaders.github.uploader.GithubUploader
       config:
         domain: https://api.github.com
         owner: xxx
         repo: xxx
         img_path: xxx
         oauth_token: xxx
       plugins: # github 图床私有插件
         - module: pypicgo.plugins.jsdelivr.JsDelivrPlugin


.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
