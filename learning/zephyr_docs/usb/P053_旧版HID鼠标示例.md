---
id: learning.zephyr-docs.usb.page-53
title: 旧版HID鼠标示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/hid-mouse/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_旧版HID鼠标示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/hid-mouse/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 53.1\_概述

本示例演示 Zephyr 的 USB 人机接口设备（Human Interface Device，HID）驱动。它把带按钮的开发板枚举成鼠标，支持左键；根据开发板按钮数量，还可支持右键、X轴移动和Y轴移动。原文说明：如果USB外设驱动支持远程唤醒（Remote Wakeup），总线挂起时每次按键都会发起唤醒请求。

> 译注（源码核对）：当前旧版示例只有在 CONFIG_USB_DEVICE_REMOTE_WAKEUP 启用且状态为 USB_DC_SUSPEND 时才请求唤醒；调用位于左右键事件分支，X/Y移动分支没有该调用。左右键释放事件也经过该分支，不能把“每次按键”扩大为所有输入事件均具有相同行为。

> 注意：本示例演示[已弃用的USB设备支持](P008_旧版USB设备支持.md#usb-device-stack)。新版示例见[HID鼠标示例](P052_HID鼠标示例.md)。

## 53.2\_要求

需要 USB 设备驱动，并使用[输入子系统（Input）](../interaction/P003_输入子系统.md) API。板级必须定义可产生输入事件的 [`gpio-keys`](../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys) 按键组；否则示例虽可能构建成功，却不会按预期工作。

示例按键映射如下：

| 输入事件码 | 功能 |
| --- | --- |
| `INPUT_KEY_0` | 鼠标左键。 |
| `INPUT_KEY_1` | 鼠标右键。 |
| `INPUT_KEY_2` | 沿X轴移动鼠标。 |
| `INPUT_KEY_3` | 沿Y轴移动鼠标。 |

还必须通过设备树别名 `led0` 配置一个LED。为不支持的板构建时，原文指出可能看到以下错误：

```text
Unsupported board: led0 devicetree alias is not defined
```

> 译注（源码核对）：当前程序通过GPIO设备树接口取得 led0，缺少该节点或属性时，实际编译错误可能不与这句历史提示完全相同。X/Y按键每次按下在对应方向增加10个相对位移单位，释放按键不再增加位移；LED在报告提交返回0并结束相应等待后翻转；这不单独证明主机应用已经处理报告。

## 53.3\_构建与运行

示例可为多种开发板构建，原文以 `nucleo_f070rb` 为例：

> 译注：在已准备依赖与工具链的 Zephyr 源码根目录、Bash中执行。确认板上UDC或旧USB驱动、按键及LED配置满足本页要求；构建失败先检查这些前提，不继续烧录。

```bash
west build -b nucleo_f070rb samples/subsys/usb/legacy/hid-mouse
```

构建并烧录示例镜像后，将开发板插入主机，例如运行 Linux 的 PC。Linux 的 `dmesg` 会显示类似的检测信息：

> 译注：下方是原文命令及示例输出，只有首行是命令；设备号、序列号、产品文本和路径以本机实际枚举为准。`/devices/...` 是Linux运行时设备路径，不是文档作者的仓库存放地址。

```console
dmesg | tail -10
usb 2-2: new full-speed USB device number 2 using at91_ohci
usb 2-2: New USB device found, idVendor=2fe3, idProduct=0007, bcdDevice= 2.03
usb 2-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 2-2: Product: Zephyr HID mouse sample
usb 2-2: Manufacturer: ZEPHYR
usb 2-2: SerialNumber: 86FE679A598AC47A
input: ZEPHYR Zephyr HID mouse sample as /devices/soc0/ahb/600000.ohci/usb2/2-2/2-2:1.0/0003:2FE3:0100.0001/input/input0
hid-generic 0003:2FE3:0100.0001: input: USB HID v1.10 Mouse [ZEPHYR Zephyr HID mouse sample] on usb-at91-2/input0
```

还可使用标准 Linux `evtest` 命令监视鼠标事件，工具详情见[Ubuntu evtest 手册](https://manpages.ubuntu.com/manpages/trusty/man1/evtest.1.html)：

> 译注：在Linux主机上选择这次鼠标对应的事件节点；`/dev/input/event0` 只是原例，不能默认它就是目标设备。下面首行是命令，后续为原始示例输出。

```console
sudo evtest /dev/input/event0
Input driver version is 1.0.1
Input device ID: bus 0x3 vendor 0x2fe3 product 0x7 version 0x110
Input device name: "ZEPHYR Zephyr HID mouse sample"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 272 (BTN_LEFT)
    Event code 273 (BTN_RIGHT)
    Event code 274 (BTN_MIDDLE)
  Event type 2 (EV_REL)
    Event code 0 (REL_X)
    Event code 1 (REL_Y)
    Event code 8 (REL_WHEEL)
  Event type 4 (EV_MSC)
    Event code 4 (MSC_SCAN)
Properties:
Testing ... (interrupt to exit)
```

按下开发板上的左键按钮时，相当于按下鼠标左键，`evtest` 会显示：

```text
Event: time 1167609663.618515, type 4 (EV_MSC), code 4 (MSC_SCAN), value 90001
Event: time 1167609663.618515, type 1 (EV_KEY), code 272 (BTN_LEFT), value 1
Event: time 1167609663.618515, -------------- SYN_REPORT ------------
Event: time 1167609663.730510, type 4 (EV_MSC), code 4 (MSC_SCAN), value 90001
Event: time 1167609663.730510, type 1 (EV_KEY), code 272 (BTN_LEFT), value 0
Event: time 1167609663.730510, -------------- SYN_REPORT ------------
```

如果开发板有多个按钮，它们还可分别用作右键、X轴移动和Y轴移动。

> 译注（报告对照）：当前源码使用 HID_MOUSE_REPORT_DESC(2)，描述符中有两个按钮及X、Y、滚轮字段；应用并未为滚轮分配按键。原evtest日志中的 BTN_MIDDLE 不能据此证明当前示例实现中键。日志用于说明事件形式，不是本批实测记录。

## 53.4\_参阅

- [USB设备核心API](P155_旧版USB设备栈核心API.md)。
- [HID设备API](P046_旧版HID设备接口API.md)。
- [输入API](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)。


译注核对来源：[samples/subsys/usb/legacy/hid-mouse/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/hid-mouse/src/main.c)、[samples/subsys/usb/legacy/hid-mouse/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/hid-mouse/prj.conf)、[samples/subsys/usb/legacy/hid-mouse/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/hid-mouse/CMakeLists.txt)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/hid-mouse/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-usb-hid-mouse"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P052_HID鼠标示例.md) · [返回大纲](大纲.md) · [下一章](P054_CDCACM串口示例.md)
