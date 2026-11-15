---
id: learning.zephyr-docs.usb.page-141
title: 旧版WebUSB浏览器演示
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/webusb/demo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_旧版WebUSB浏览器演示

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/webusb/demo.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 141.1\_官方演示页与界面译文

原页为 WebUSB HTML 演示应用（WebUSB HTML Demo App），直接嵌入官方示例的 `index.html`，没有独立的使用说明正文。完整步骤见[旧版 WebUSB 示例](P140_旧版WebUSB示例.md)。全部可见界面文字的译文如下：

| 原界面文字 | 中文 |
| --- | --- |
| WebUSB Serial Sample Application | WebUSB 串行通信示例应用 |
| Connect To WebUSB Device | 连接 WebUSB 设备 |
| Sender: | 发送区 |
| Send | 发送 |
| Receiver: | 接收区 |
| WebUSB! | 原始默认测试文本，保持不变 |

## 141.2\_随附文件

- [官方原始 HTML](examples/legacy_webusb/index.original.html)：逐字节保留下载的文件，并与官方页面内嵌脚本核对。
- [中文界面 HTML](examples/legacy_webusb/index.html)：只翻译界面标题和标签，补充中文语言及 UTF-8 声明；JavaScript 原样保留。

> 译注：这是完整的交互应用，不是截图。Markdown 中保留下方全部源码；使用 WebUSB 需要在支持该 API 的浏览器中访问应用，并具备对应设备、固件和 USB 权限。阅读器是否能运行 HTML，不影响原文件交付。

## 141.3\_使用随附应用

> 译注：以下是访问本地副本的方法。前提为已安装 Python、具备支持 WebUSB 的浏览器和对应固件设备。终端为 Bash，起点为读者自己的仓库根目录。

```bash
# Bash；从读者的仓库根目录执行，前提是 Python 已可用
cd learning/zephyr_docs/usb/examples/legacy_webusb
python -m http.server 8001 --bind 127.0.0.1
```

在同一主机打开 `http://localhost:8001/` 查看中文界面，或打开 `http://localhost:8001/index.original.html` 对照原版。点击连接按钮，在浏览器设备选择器中选择对应设备，再发送短文本检查回显。结束后在服务终端按 `Ctrl+C` 停止服务。端口被占用时，先核对已有服务或选择另一端口，并同步修改访问 URL。

## 141.4\_脚本行为与边界

> 译注（源码跟踪）：以下解释原脚本，未修改其 USB 通信实现。

- `serial.requestPort()` 调用 `navigator.usb.requestDevice()`，过滤器包含 `2fe3:0100`、`2fe3:000a`、`8086:f8a1`。当前旧版固件的 `prj.conf` 使用产品标识（Product ID，PID）`0x000A`。
- 连接时先打开设备，没有活动配置时选择配置 1，然后声明接口 0。脚本固定从 `configuration.interfaces[0].alternate.endpoints[0]` 取接收端点，从 `[1]` 取发送端点；它没有按端点方向重新筛选，不能直接用于任意 USB 接口布局。
- 接收循环调用 `transferIn(..., 64)`，用 `TextDecoder` 解码并追加文本；发送用 `TextEncoder` 编码 UTF-8，再调用 `transferOut()`。接口名称中的 Serial 是原示例用语，这里调用的是 WebUSB API。
- 设备选择完成后连接按钮即隐藏；接收错误回调会重新显示按钮并关闭设备，但外层连接失败没有完整的界面错误处理。按钮隐藏不等于通信成功。
- 每次接收都创建新的解码器，没有流式 UTF-8 解码，跨接收块的多字节字符可能不能按整段文本处理。短文本回显不证明所有长度和字符边界均已验证。

本轮未启动服务器或执行浏览器 USB 交互，也未构建或烧录固件。

## 141.5\_原始 HTML 完整源码

下面保留官方原文件的全部 HTML 与 JavaScript，作为代码文本阅读；界面译文见首节。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>WebUSB Serial Sample Application</title>
  </head>

<body>
  <script>
var serial = {};

(function() {
  'use strict';

  serial.getPorts = function() {
    return navigator.usb.getDevices().then(devices => {
      return devices.map(device => new serial.Port(device));
    });
  };

  serial.requestPort = function() {
    const filters = [
      { 'vendorId': 0x2fe3, 'productId': 0x0100 },
      { 'vendorId': 0x2fe3, 'productId': 0x00a },
      { 'vendorId': 0x8086, 'productId': 0xF8A1 },
    ];
    return navigator.usb.requestDevice({ 'filters': filters }).then(
      device => new serial.Port(device)
    );
  }

  serial.Port = function(device) {
    this.device_ = device;
  };

  serial.Port.prototype.connect = function() {
    let readLoop = () => {
      const {
        endpointNumber
      } = this.device_.configuration.interfaces[0].alternate.endpoints[0]
      this.device_.transferIn(endpointNumber, 64).then(result => {
        this.onReceive(result.data);
        readLoop();
      }, error => {
        this.onReceiveError(error);
      });
    };

    return this.device_.open()
        .then(() => {
          if (this.device_.configuration === null) {
            return this.device_.selectConfiguration(1);
          }
        })
        .then(() => this.device_.claimInterface(0))
        .then(() => {
          readLoop();
        });
  };

  serial.Port.prototype.disconnect = function() {
    return this.device_.close();
  };

  serial.Port.prototype.send = function(data) {
    const {
      endpointNumber
    } = this.device_.configuration.interfaces[0].alternate.endpoints[1]
    return this.device_.transferOut(endpointNumber, data);
  };
})();

let port;

function connect() {
  port.connect().then(() => {
    port.onReceive = data => {
      let textDecoder = new TextDecoder();
      console.log("Received:", textDecoder.decode(data));
      document.getElementById('output').value += textDecoder.decode(data);
    }
    port.onReceiveError = error => {
      console.error(error);
      document.querySelector("#connect").style = "visibility: initial";
      port.disconnect();
    };
  });
}

function send(string) {
  console.log("sending to serial:" + string.length);
  if (string.length === 0)
    return;
  console.log("sending to serial: [" + string +"]\n");

  let view = new TextEncoder('utf-8').encode(string);
  console.log(view);
  if (port) {
    port.send(view);
  }
};

window.onload = _ => {
  document.querySelector("#connect").onclick = function() {
    serial.requestPort().then(selectedPort => {
      port = selectedPort;
      this.style = "visibility: hidden";
      connect();
    });
  }

  document.querySelector("#submit").onclick = () => {
    let source = document.querySelector("#input").value;
    send(source);
  }
}

</script>
 <button id="connect" style="visibility: initial">Connect To WebUSB Device</button>
 <br><br><label for="input">Sender: </label> <br>
 <textarea id="input" rows="25" cols="80">WebUSB!</textarea>
 <br><button id="submit">Send</button>
 <br><br>
 <label for="output">Receiver: </label> <br>
 <textarea id="output" rows="25" cols="80"></textarea>
</body>
</html>
```


译注核对来源：[samples/subsys/usb/legacy/webusb/index.html](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/webusb/index.html)、[samples/subsys/usb/legacy/webusb/demo.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/webusb/demo.rst)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/webusb/index.html)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="webusb-html-demo-app"></a>
<a id="connect"></a>
<a id="input"></a>
<a id="submit"></a>
<a id="output"></a>

[上一章](P140_旧版WebUSB示例.md) · [返回大纲](大纲.md) · [下一章](P142_旧版USB音频头文件接口.md)
