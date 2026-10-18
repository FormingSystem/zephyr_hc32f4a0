---
id: learning.zephyr-docs.board-samples.page-33
title: Mesh开关模型
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff-app/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_bluetooth_mesh_onoff"></a>

# 第33章\_Mesh 开关模型（Mesh OnOff Model）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/mesh/onoff-app/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/mesh/onoff-app/README.rst/..)

<a id="overview"></a>

## 33.1 概述（Overview）

这是一个简单应用，演示蓝牙 Mesh（Bluetooth Mesh）的多元素节点（Multi-element node）。每个元素都有 Mesh 开关客户端与服务端模型，控制四组按钮和 LED 中的一组。

> 译注——节点组成：元素（Element）是节点内具有独立单播地址的组成单元，模型（Model）定义可交换的消息与状态。一块板可以有多个元素，一个元素也可以包含多个模型；不是每个模型各分配一个单播地址。

配网（Provisioning）之前，设备广播未配网信标（Unprovisioned beacon），其中包含唯一的通用唯一标识符（Universally Unique Identifier，UUID）。这个 UUID 来自 Nordic 在工厂信息配置寄存器（Factory Information Configuration Register，FICR）中设置的设备地址。此时，每个按钮控制对应 LED 的状态，不发起任何 Mesh 活动。

按钮 1 与 LED 1 的模型位于节点的根元素（Root element）。其余三组按钮／LED 分别位于元素 1～3。假设配网器（Provisioner）将 0x100 分配给根元素，那么次级元素的地址分别为 0x101、0x102 和 0x103。

配网后，必须将按钮客户端配置为发布（Publish），将 LED 服务端配置为订阅（Subscribe）。

> 译注——配网与配置：配网让节点加入网络，应用密钥绑定、发布和订阅则决定模型如何通信。源码在未配网时本地调用对应 LED 模型；配网后如果客户端没有发布地址，就不发布。原先同一板上的按钮与 LED 也需要正确配置才能继续关联。

如果为 LED 服务端提供发布地址，它也会在开关状态变化时发布自己的状态。

如果在一秒间隔内只按一次按钮，它会发送“开”（on）消息；如果按下超过一次，则发送“关”（off）消息。按钮抖动较明显，因此在 button_pressed() 中断处理函数中进行去抖（Debouncing）：距离上一次中断不足 250 ms 的中断会被丢弃。这个操作方式可能有些不便，但若改为一个按钮负责“开”、另一个负责“关”，开关客户端的数量就会从四个减少为两个。

> 译注——按键时间窗：源码使用一个共享的按键计数器与一秒定时器；250 ms 内的抖动事件被丢弃。实际演示应在同一按钮上按所需次数操作，不能把多按钮同时按下视为四套独立计时器。

<a id="requirements"></a>

## 33.2 前提条件（Requirements）

原示例已在 Nordic nRF52840-PDK 开发板上测试，也可能在 nrf52dk/nrf52832 上运行。

<a id="building-and-running"></a>

## 33.3 构建与运行（Building and Running）

> 译注——执行前提：west 构建和烧录命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具、模块、目标工具链与板卡；应用及配置为官方源码，构建目录由工具生成。构建成功后再烧录，出现错误先检查构建输出和板文档。后续 meshctl 命令属于独立的主机交互工具步骤。原文的板级测试结论不代表本次实测。

以下命令构建该应用。

```text
west build -b nrf52840dk/nrf52840 samples/boards/nordic/mesh/onoff-app
west flash
```

配网之前，每个按钮像实际开关一样控制对应的 LED。

使用 BlueZ 的 meshctl 工具进行配网。下面的示例将按钮 2 与 LED 1 绑定到应用密钥（Application key）1，然后将按钮 2 配置为向组地址 0xc000 发布，将 LED 1 配置为订阅该组。

> 译注——命令位置与示例地址：下方命令输入 Linux 上已启动的 BlueZ meshctl 交互界面，不能粘贴到 Bash 或板端 Zephyr Shell；先确认所用 BlueZ 提供该工具以及主机蓝牙适配器可用。<discovered UUID> 替换为实际发现的目标，0100、0101、c000 和应用密钥索引 1 是本例配置值，已有网络必须以实际分配记录为准。

```text
discover-unprovisioned on
provision <discovered UUID>
menu config
target 0100
appkey-add 1
bind 0 1 1000                # bind appkey 1 to LED server on element 0 (unicast 0100)
sub-add 0100 c000 1000       # add subscription to group address c000 to the LED server
bind 1 1 1001                # bind appkey 1 to button 2 on element 1 (unicast 0101)
pub-set 0101 c000 1 0 0 1001 # publish button 2 to group address c000
```

meshctl 工具维护一个持久化 JSON 数据库，用于保存 Mesh 配置。随着更多节点（开发板）加入配网，它会根据每个节点支持的元素数量，依次分配单播地址（Unicast address）。本示例每个节点支持四个元素。

节点的第一个元素，即根元素，包含配置（Configuration）、健康（Health）和开关（OnOff）模型。次级元素只包含开关模型。用于配置的 meshctl target 必须是根元素的单播地址，因为只有根元素具有配置服务端（Configuration Server）模型。

如果正常退出 meshctl，可以重新启动它，并重新连接网络 0x0。

meshctl 也支持开关模型客户端，可以改变绑定到应用密钥 0x1 的任意 LED 的状态。方法是将 target 设置为包含该 LED 模型的元素的单播地址，然后执行 onoff 命令。此处不支持组地址。

> 译注——地址限制的范围：“不支持组地址”描述这里的 meshctl 开关客户端操作，不是说 Bluetooth Mesh 不支持组地址；上面的 c000 发布／订阅本身就使用组地址。配置操作的 target 指根元素，控制某个 LED 时的 target 则指承载该 LED 模型的元素，二者用途不同。

本应用派生自 [samples/bluetooth/mesh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh) 中的 Mesh 示例骨架。

详情请参阅[蓝牙（Bluetooth）](../bluetooth_samples/P088_蓝牙示例总目录.md#bluetooth)示例。

<a id="see-also"></a>

## 33.4 另请参阅（See also）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

> 译注——源码入口：[main.c](../../../samples/boards/nordic/mesh/onoff-app/src/main.c)；[prj.conf](../../../samples/boards/nordic/mesh/onoff-app/prj.conf)。这些相对链接用于查看本仓库参照实现，版本可能与本次官方页面不同。

对应官方文档源码：[samples/boards/nordic/mesh/onoff-app/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/mesh/onoff-app/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/mesh/onoff-app/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P032_SPIS唤醒.md) · [返回大纲](大纲.md) · [下一章](P034_Mesh多模型演示.md)
