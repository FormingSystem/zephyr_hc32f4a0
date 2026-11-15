---
id: learning.zephyr-docs.usb.page-191
title: MCTPUSB端点示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/usb_endpoint/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_MCTPUSB端点示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/usb_endpoint/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 191.1\_概览（Overview）

本示例建立一个管理组件传输协议（Management Component Transport Protocol，MCTP）端点节点，监听来自端点标识（Endpoint ID，EID）为 20 的 MCTP 总线所有者（Bus Owner）的消息，并回复 `Hello, bus owner`（“你好，总线所有者”）。

译注（源码核对）：EID 20 指总线所有者。示例自身使用 `SELF_ID = 10`，通过 `mctp_register_bus()` 注册；接收回调只对 `BUS_OWNER_ID = 20` 的消息唤醒回复流程。这两个 EID 不能互换。

## 191.2\_要求（Requirements）

需要开发板及片上系统（System on Chip，SoC）提供 USB 设备功能，可以是全速（Full Speed，FS）或高速（High Speed，HS），尽管 DMTF 规范只规定了 HS。测试需要一台能够枚举 MCTP 接口、通过 MCTP 协议与开发板通信的 USB 主机；使用 Python 脚本是一种简单做法。

示例应用随附接口测试脚本。运行前先安装 `pyusb`。原文命令如下：

```bash
pip install requirements.txt
python usb_host_tester.py
```

译注——原命令修正：上面的 `pip install requirements.txt` 缺少读取依赖文件所需的 `-r`。根据 [pip 官方用户指南源码](https://raw.githubusercontent.com/pypa/pip/main/docs/html/user_guide.rst)，从依赖文件安装应使用 `python -m pip install -r requirements.txt`。在已有 Python 环境中，从 Zephyr 源码根目录进入此官方示例目录后执行：

```bash
cd samples/subsys/pmci/mctp/usb_endpoint
python -m pip install -r requirements.txt
python usb_host_tester.py
```

`requirements.txt` 和 `usb_host_tester.py` 都是示例随附文件；当前依赖文件列出 `pyusb`。安装失败时先修复 Python 环境或依赖获取问题，不能把安装失败当成设备通信失败。运行脚本还要求设备固件已经运行并接入主机；源码中的查找条件固定为 VID `0x2FE3`、PID `0x0001`，选择活动配置的接口 `(0, 0)`，并寻找批量输入／输出（Bulk IN/OUT）端点。找不到设备或端点时，应先核对实际描述符与所连设备，不能仅重复发送。

若测试成功，原文预期脚本输出如下：

```text
Sending message with size smaller than USB FS MPS (<64b)
Received: b'\x1a\xb4\x00\x15\x01\x14\n\xc0Hello, bus owner\x00'
Sending message spanning two USB FS packets (>64b)
Received: b'\x1a\xb4\x00\x15\x01\x14\n\xc0Hello, bus owner\x00'
Sending message with two MCTP messages in a single USB FS packet
Received: b'\x1a\xb4\x00\x15\x01\x14\n\xc0Hello, bus owner\x00'
Received: b'\x1a\xb4\x00\x15\x01\x14\n\xc0Hello, bus owner\x00'
```

日志依次表示：发送小于 USB FS 最大包长（Maximum Packet Size，MPS）的消息、发送跨两个 USB FS 包的消息，以及在一个 USB FS 包中发送两条 MCTP 消息。`Received` 表示收到回复；字节转义、帧头和消息文本按原日志保留。

译注（版本差异）：当前保存的 `usb_host_tester.py` 已改为运行时读取端点 MPS，并使用 `Test1`～`Test5` 标题；它还增加零长度包（Zero-length Packet，ZLP）相关压力测试和稳定性测试。第三项标明第二个回复可选，不能要求当前脚本逐行复现上面的旧输出。源码帧长度字段为 1 字节，总帧长限制为 255；涉及整 MPS 的 ZLP 测试在端点 MPS 大于 255 时跳过。以上说明来自源码阅读，不是本次运行结果。

## 191.3\_连接（Wiring）

使用 USB 线连接主机（通常为 PC）和开发板。线缆类型，如 Mini-USB、Micro-USB 或 USB Type-C，由两端连接器决定。

## 191.4\_构建与运行（Building and Running）

原文构建和运行命令如下：

```bash
west build -b frdm_mcxn947_mcxn947_cpu0 samples/subsys/pmci/mctp/usb_endpoint
west build -t run
```

译注——板名与执行位置：原文 `frdm_mcxn947_mcxn947_cpu0` 为旧式写法，当前[官方 FRDM-MCXN947 页面](https://docs.zephyrproject.org/latest/boards/nxp/frdm_mcxn947/doc/index.html)使用 `frdm_mcxn947/mcxn947/cpu0`。读者在自己的 Zephyr 源码根目录、所需模块与工具链准备完成后，可按当前板名构建：

```bash
west build -b frdm_mcxn947/mcxn947/cpu0 samples/subsys/pmci/mctp/usb_endpoint
```

如果刚在示例目录运行过 Python 脚本，应先回到源码根目录再执行此命令。原页的 `west build -t run` 是构建系统的运行目标，不保证所有硬件板都提供该目标；实际烧录与连接方式按所用板的官方说明。设备固件启动后，示例会先等待 USB 配置消息，再建立 MCTP 端点；主机未完成配置时，不能以尚未回复推断 MCTP 收发已经开始。

## 191.5\_参考资料（References）

[MCTP 基础规范（MCTP Base Specification，2019）](https://www.dmtf.org/sites/default/files/standards/documents/DSP0236_1.3.1.pdf)。

## 191.6\_另请参阅（See Also）

[USB 设备核心 API（USB Device Core API）](P015_USB设备核心API.md)。



译注核对来源：[samples/subsys/pmci/mctp/usb_endpoint/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/usb_endpoint/src/main.c)、[samples/subsys/pmci/mctp/usb_endpoint/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/usb_endpoint/prj.conf)、[samples/subsys/pmci/mctp/usb_endpoint/requirements.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/usb_endpoint/requirements.txt)、[samples/subsys/pmci/mctp/usb_endpoint/usb_host_tester.py](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/usb_endpoint/usb_host_tester.py)、[boards/nxp/frdm_mcxn947/board.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/boards/nxp/frdm_mcxn947/board.yml)。

本仓库的[对应源码](../../../samples/subsys/pmci/mctp/usb_endpoint/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="mctp-usb-endpoint"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="wiring"></a>
<a id="building-and-running"></a>
<a id="references"></a>
<a id="see-also"></a>

[上一章](P190_蓝牙HCIUSB控制器示例.md) · [返回大纲](大纲.md) · [下一章](P192_USBIP原生模拟器片段.md)
