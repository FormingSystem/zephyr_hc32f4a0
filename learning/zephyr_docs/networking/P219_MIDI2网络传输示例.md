---
id: learning.zephyr-docs.networking.page-219
title: MIDI2网络传输示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/midi2/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="netmidi2"></a>

# 第219章\_MIDI2网络传输示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/midi2/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 219.1 概述（Overview）

本示例演示Network MIDI 2.0协议栈的用法：

- 启动能够从网络访问的通用MIDI数据包（Universal MIDI Packet，UMP）端点主机。
- 响应UMP流发现消息（UMP Stream discovery message），使客户端能够发现设备树描述的拓扑（Topology）。
- 如果设备树定义了`midi_serial`端口，将UMP组9的MIDI1数据发送到该端口。
- 如果设备树定义了`midi_green_led`节点，在串口发送数据时点亮LED，对应`CONFIG_NET_SAMPLE_MIDI2_ACTIVITY_LED`。

<a id="requirements"></a>

## 219.2 要求（Requirements）

需要支持IP网络的开发板。要与运行中的示例进行实际交互，还需使用Network MIDI 2.0客户端连接目标，例如[pymidi2](https://github.com/titouanc/pymidi2)。

<a id="building-and-running"></a>

## 219.3 构建与运行（Building and Running）

无需硬件即可尝试此示例的最简方式是`native_sim`。先按[native_sim以太网驱动说明](../native_reference/P004_Native_Simulator本机模拟器.md#nsim-per-ethe)配置主机网络：

```sh
# From the root of the zephyr repository
west build -b native_sim samples/net/midi2/
west build -t run
```

此时应能从网络访问Network MIDI 2.0端点：

```text
$ pymidi2 find
Zephyr-UDP-MIDI2 (udp://192.0.2.1:45486)
- Block #0 [io : Recv/Send] 'Synthesizer' UMP groups {0, 1, 2, 3} [MIDI1 + MIDI2]
- Block #1 [i- : Recv     ] 'Keyboard' UMP groups {8} [MIDI1 only]
- Block #2 [-o :      Send] 'External output (MIDI DIN-5)' UMP groups {9} [MIDI1 31.25kb/s]
```

示例也适合配合[Olimex SHIELD-MIDI](https://docs.zephyrproject.org/latest/boards/shields/olimex_shield_midi/doc/index.html#olimex-shield-midi)使用，该扩展板方便地定义了外部MIDI OUT及其LED的设备树节点。例如，在ST Nucleo F429zi上使用该扩展板：

```sh
# From the root of the zephyr repository
west build -b nucleo_f429zi --shield olimex_shield_midi samples/net/midi2
west flash
```

<a id="using-authentication"></a>

## 219.4 使用认证（Using authentication）

要使用共享秘密（Shared secret）认证连接UMP端点主机，启用`CONFIG_NET_SAMPLE_MIDI2_AUTH_SHARED_SECRET`，并在`CONFIG_NET_SAMPLE_MIDI2_SHARED_SECRET`中配置所需秘密值。

如果改用用户名／密码（User/password）认证，启用`CONFIG_NET_SAMPLE_MIDI2_AUTH_USER_PASSWORD`，并设置`CONFIG_NET_SAMPLE_MIDI2_USERNAME`与`CONFIG_NET_SAMPLE_MIDI2_PASSWORD`。

> 译注——默认与编号：当前Kconfig默认选择不认证模式（`CONFIG_NET_SAMPLE_MIDI2_AUTH_NONE`）；原文两种认证方案都需要显式选择。`app.overlay`定义组0—3的合成器、组8的键盘与组9的外部输出，这些是UMP组编号，不是网络接口编号。实际端口号以客户端发现结果为准，原输出中的`45486`不是所有运行环境固定使用的值。

<a id="see-also"></a>

## 219.5 另请参阅（See also）

[MIDI2通用MIDI数据包定义（MIDI2 Universal MIDI Packet definitions）](../usb/P098_通用MIDI数据包定义.md)、[Network MIDI 2.0](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html)。


> 译注——实现依据：[samples/net/midi2/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/midi2/Kconfig)、[samples/net/midi2/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/midi2/app.overlay)、[samples/net/midi2/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/midi2/src/main.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/midi2/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/midi2/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/midi2/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/midi2/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P218_TagoIO的HTTP上报示例.md) · [返回大纲](大纲.md) · [下一章](P220_Prometheus指标示例.md)
