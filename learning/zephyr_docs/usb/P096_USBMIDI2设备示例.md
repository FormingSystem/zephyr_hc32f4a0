---
id: learning.zephyr-docs.usb.page-96
title: USBMIDI2设备示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/midi/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_USBMIDI2设备示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/midi/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 96.1\_概述（Overview）

本示例演示如何实现 USB 乐器数字接口（Musical Instrument Digital Interface，MIDI）设备，可以运行在具有 USB 设备控制器（USB Device Controller）的开发板上。原文说明，示例会将发送给设备的所有 MIDI1 消息回送给主机；此外，输入按键（例如开发板用户按钮）的按下和释放，会分别作为 MIDI1 音符开启（Note On）和音符关闭（Note Off）事件发送。

应用暴露一个 USB-MIDI 接口，其中包含一个双向组终端（Bidirectional Group Terminal）。这样就能通过承载 MIDI1 消息的“虚拟连线”（Virtual Wire）与主机交换数据，类似标准 USB-MIDI 输入／输出适配器。回环（Loopback）表现得就像在输出与输入之间连接了一根实体 MIDI 电缆，而输入按键则充当 MIDI 键盘。

> 译注（源码核对）：当前 `on_midi_packet()` 实际回送 `UMP_MT_MIDI1_CHANNEL_VOICE`，即 MIDI 1.0 通道语音消息（Channel Voice Messages）；`UMP_MT_UMP_STREAM` 交由 UMP 流响应器处理。不能将原文“所有 MIDI1 消息”理解为该示例已对所有消息类型实现回送。MIDI 2.0 USB 传输接口可以承载封装在 UMP 中的 MIDI1 消息，接口版本与消息内容版本需分别理解。

## 96.2\_构建与运行（Building and Running）

示例代码位于官方源码树的 [`samples/subsys/usb/midi`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/midi)。

以下是官方构建和烧录命令。译注：终端需已准备好 Zephyr 工具链、west 和目标板烧录工具；从 Zephyr 源码根目录执行。Windows 通用工程操作可使用 UCRT64 Bash，Linux 使用 Bash。命令中的目标板是 `nucleo_f429zi`，接好对应开发板后执行烧录。

```shell
west build -b nucleo_f429zi samples/subsys/usb/midi
west flash
```

## 96.3\_使用 MIDI 接口（Using the MIDI Interface）

烧录本示例后，将设备的 USB 端口连接到支持 MIDI 的主机。例如，在 Linux 上可以使用高级 Linux 声音架构（Advanced Linux Sound Architecture，ALSA）访问设备：

```console
$ amidi -l
Dir Device    Name
IO  hw:2,1,0  Group 1 (USBD MIDI Sample)
```

> 译注：以上及下方 `amidi` 命令在 Linux 主机终端执行，工作目录不限；需要主机已安装提供 `amidi` 的工具。`$` 是终端提示符，不属于命令。`hw:2,1,0` 是原文机器枚举出来的 ALSA 设备标识，不是文件路径或固定地址；执行时用本机 `amidi -l` 列出的标识替换。

在 Mac OS 上，可以使用系统工具“音频 MIDI 设置”（Audio MIDI Setup）查看设备，参阅 [Apple 官方 MIDI 设备设置说明](https://support.apple.com/guide/audio-midi-setup/set-up-midi-devices-ams875bae1e0/mac)。

“USBD MIDI Sample”接口也应出现在支持 MIDI 的程序中，例如常用的数字音频工作站（Digital Audio Workstation，DAW）或合成器（Synthesizer）。如果手边没有此类程序，也可以使用在线 Web MIDI 程序；原文举例为 [muted.io 钢琴](https://muted.io/piano/)。

## 96.4\_回环测试（Testing Loopback）

打开第一个终端，开始转储（Dump）MIDI 事件：

```console
$ amidi -p hw:2,1,0 -d
```

然后在第二个终端发送一些 MIDI 事件，例如音符开启和关闭：

```console
$ amidi -p hw:2,1,0 -S "90427f 804200"
```

这些事件随后应出现在第一个终端的转储输出中。

如果开发板有用户按钮，按下按钮，观察第一个终端中收到的音符开启／关闭事件。原文给出的输出如下：

```console
$ amidi -p hw:2,1,0 -d

90 40 7F
80 40 7F
90 40 7F
80 40 7F
[...]
```

> 译注（源码核对）：当前 `key_press()` 只处理 `INPUT_EV_KEY` 且事件代码不大于 `0x7f` 的输入，以事件代码作为音符编号（Note Number），使用组0、通道0，力度（Velocity）固定为100，即十六进制 `0x64`。原文日志末字节是 `7F`，属于保存的示例输出，不是当前源码必然产生的值。按键事件代码也会影响中间的音符字节，不能要求所有开发板都输出 `40`。示例忽略了 `usbd_midi_send()` 的返回值，实际应用需要处理接口未启用与发送队列已满等错误。

## 96.5\_另请参阅（See Also）

- [USB 设备核心 API](P015_USB设备核心API.md)。
- [USB MIDI 2.0 类设备 API](P094_USBMIDI2设备API.md)。
- [输入事件定义（Input Event Definitions）](https://docs.zephyrproject.org/latest/doxygen/html/group__input__events.html)。


译注核对来源：[samples/subsys/usb/midi/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/midi/src/main.c)、[samples/subsys/usb/midi/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/midi/app.overlay)、[samples/subsys/usb/midi/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/midi/prj.conf)、[samples/subsys/usb/midi/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/midi/Kconfig)。

本仓库的[对应源码](../../../samples/subsys/usb/midi/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-midi2-device"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="using-the-midi-interface"></a>
<a id="testing-loopback"></a>
<a id="see-also"></a>

[上一章](P095_USBMIDI回调接口.md) · [返回大纲](大纲.md) · [下一章](P097_USBMIDI2头文件接口.md)
