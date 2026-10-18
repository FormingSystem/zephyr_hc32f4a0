---
id: learning.zephyr-docs.usb.page-70
title: WebUSB浏览器演示
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/webusb/demo.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_WebUSB浏览器演示

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/webusb/demo.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 70.1\_官方演示页与界面译文

原页面是WebUSB HTML演示应用（WebUSB HTML Demo App），直接嵌入示例的 `index.html`，没有独立的使用说明段落。完整使用步骤见[WebUSB示例](P069_WebUSB示例.md)。这里保留原HTML，并翻译全部可见界面文字。

| 原界面文字 | 中文 |
| --- | --- |
| WebUSB Serial Sample Application | WebUSB串行通信示例应用 |
| Connect To WebUSB Device | 连接WebUSB设备 |
| Sender: | 发送区 |
| Send | 发送 |
| Receiver: | 接收区 |
| WebUSB! | 原始默认测试文本，保持不变 |

## 70.2\_随附文件

- [官方原始HTML](examples/webusb/index.original.html)：逐字节保留此次保存的原文件，与官方演示页嵌入的应用核对一致；来源和SHA-256见[来源记录](../SOURCES.md)。
- [中文界面HTML](examples/webusb/index.html)：只翻译界面标题和标签，补充中文语言及UTF-8声明；JavaScript脚本与原件完全一致。

> 译注：HTML是本示例的完整交互应用，不是图片或动图。Markdown负责说明和源码阅读；通过支持WebUSB的浏览器访问应用，仍需对应固件、USB访问权限及实际设备。下载HTML不代表已执行USB通信，预览器显示能力也不影响原文件交付。

## 70.3\_在本机打开随附演示

> 译注：以下为使用随附文件的通用方法。前提是主机已安装Python，并准备了官方WebUSB固件和支持WebUSB的浏览器。终端为Bash，起点为读者自己的仓库根目录；所有文件位置相对于该根目录解析。

```bash
# Bash；从读者的仓库根目录运行，前提是Python已可用
cd learning/zephyr_docs/usb/examples/webusb
python -m http.server 8000 --bind 127.0.0.1
```

在同一主机的浏览器输入 `http://localhost:8000/` 打开中文界面；输入 `http://localhost:8000/index.original.html` 对照原版。服务运行期间保持终端打开，结束后按 `Ctrl+C` 停止。如果端口被占用，先检查已有服务或显式选择另一端口，并使用对应URL；不要因为端口失败改动USB固件配置。

点击“连接WebUSB设备”，在浏览器设备选择器选择示例设备；在发送区输入短文本后点“发送”，接收区应出现相同文本。网页可显示但不能连接时，回到前章核对浏览器支持、安全上下文、设备权限和VID/PID过滤器。这里没有实际连接设备或运行该交互流程。

## 70.4\_脚本行为与使用边界

> 译注（源码跟踪）：以下说明原脚本行为，不改变其实现。

- `serial.requestPort()` 通过 `navigator.usb.requestDevice()` 提示用户选择设备，过滤器包含 `2fe3:0100`、`2fe3:000a` 和 `8086:f8a1` 三组标识；当前新版固件使用第二组。`serial.getPorts()` 封装了 `navigator.usb.getDevices()`，但此页加载流程没有自动调用它连接设备。
- 连接后，如果设备尚无活动配置则选择配置1，再查找第一个接口类为 `0xFF` 的厂商专用接口（Vendor-Specific Interface），取得输入／输出端点号并调用 `claimInterface()`。
- 接收循环使用 `transferIn(..., 64)`，将数据用 `TextDecoder` 解码并追加到接收区；发送用 `TextEncoder` 编码UTF-8，再调用 `transferOut()`。这是USB批量传输，不是操作系统串口设备。
- 原 `connect()` 实现没有将内部 `claimInterface()` 的Promise返回给外层链；外层完成不严格等价于端点已声明完成。连接按钮会在选择设备后隐藏，读取出错才在对应处理里重新显示；其他异常没有完整界面提示。这是原演示的边界，不能把按钮隐藏当成连接成功证据。
- UTF-8解码按每次接收块独立进行，没有流式解码；长文本或跨传输边界的多字节字符不能据短文本回显结果推定正常。原代码保留用于对照，未在译文中悄悄修改。

## 70.5\_原始HTML完整源码

下方保留官方嵌入应用的全部HTML及JavaScript，界面英文的中文含义见首节。代码围栏使其作为文本阅读，不在Markdown中自动调用WebUSB。

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
      this.device_.transferIn(this.inEndpoint, 64).then(result => {
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
      .then(() => {
        const [iface] = this.device_.configuration.interfaces.filter(i => i.alternate.interfaceClass === 0xFF)
        this.device_.claimInterface(iface.interfaceNumber).then(() => {
          this.inEndpoint = iface.alternate.endpoints.find((endpoint) => endpoint.direction === 'in').endpointNumber;
          this.outEndpoint = iface.alternate.endpoints.find((endpoint) => endpoint.direction === 'out').endpointNumber;
          readLoop();
        });
      })
  };

  serial.Port.prototype.disconnect = function() {
    return this.device_.close();
  };

  serial.Port.prototype.send = function(data) {
    return this.device_.transferOut(this.outEndpoint, data);
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


译注核对来源：[samples/subsys/usb/webusb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/main.c)、[samples/subsys/usb/webusb/src/sfunc.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/sfunc.c)、[samples/subsys/usb/webusb/src/webusb.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)、[samples/subsys/usb/webusb/src/msosv2.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)、[samples/subsys/usb/webusb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/prj.conf)、[samples/subsys/usb/webusb/index.html](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/index.html)、[samples/subsys/usb/webusb/demo.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/demo.rst)。

本仓库的[对应源码](../../../samples/subsys/usb/webusb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="webusb-html-demo-app"></a>
<a id="connect"></a>
<a id="input"></a>
<a id="submit"></a>
<a id="output"></a>

[上一章](P069_WebUSB示例.md) · [返回大纲](大纲.md) · [下一章](P071_USB主机API目录.md)
