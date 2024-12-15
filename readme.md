# 命令行API图床

启动

```shell
ccbs-picbed
```

输出
```shell
(picgo) PS Z:\mine\cc-picgo> ccbs-picbed.exe       
 * Serving Flask app 'ccbs_picbed.main'
 * Debug mode: on
2024-12-15 16:09:33,346 - werkzeug - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:36677
2024-12-15 16:09:33,346 - werkzeug - INFO - Press CTRL+C to quit
```




## 配置

需要准备以下配置，保存为`C:\Users\[你的windows登录用户名]\.PyPicGo`
```yaml
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
      access_token: 9d4ffd225107*******d79e617d7c8e
    plugins:
```
