---
id: learning.zephyr-docs.bluetooth-samples.page-51
title: Mesh基本示例
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/mesh/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_mesh"></a>

# 第51章\_Mesh 基本示例（Mesh）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/mesh/README.rst/..)

<a id="overview"></a>

## 51.1 概述（Overview）

本示例演示蓝牙 Mesh 功能，包含若干标准 Mesh 模型（Model），支持通过广播和 GATT 配网承载进行配网，即 PB-ADV 和 PB-GATT。应用还需要可用的串口控制台，用于带外配网（Out-of-Band provisioning，OOB）流程。

> 译注——配网与运行：外部配网器通过 PB-ADV／PB-GATT 将节点加入网络，随后仍需添加并绑定应用密钥；仅看到配网完成，不能据此断言 OnOff 消息可收发。串口中的 OOB Number 是配网认证用数字，需由配网端按实际流程使用。

带 LED 的开发板上，通用开关服务端模型（Generic OnOff Server）可通过 Mesh 控制板上的第一个 LED。

带按钮的开发板上，按键时通用开关客户端模型（Generic OnOff Client）向网络中所有节点发送 OnOff 消息。

<a id="requirements"></a>

## 51.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板；或者

- QEMU，以及主机上运行的 BlueZ。

<a id="building-and-running"></a>

## 51.3 构建与运行（Building and Running）

> 译注——执行环境：以下官方命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门文档](../getting_started/大纲.md)准备工具链、west工作区、板定义与所需蓝牙控制器；`samples/...` 是官方已有目录，`<board>` 需替换为实际板目标。构建成功后才按板文档烧录，并通过本页描述的连接、服务发现、订阅或配网步骤观察结果；失败时分别回查构建配置、烧录器或对端角色与功能支持。构建输出由工具生成，中文目录不作为固件工作目录。本次仅核对文档，未执行这些操作。

在 QEMU 中运行示例的详情，参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

其他开发板可按以下方式构建并烧录应用：

```text
west build -b <board> samples/bluetooth/mesh
west flash
```

若开发板不支持 `flash` 目标，请查阅[该板文档](https://docs.zephyrproject.org/latest/boards/index.html#boards)中的其他烧录方法。

在 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk) 上运行本应用时，网络核还必须运行蓝牙控制器应用，可以使用 [HCI IPC](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) 示例。构建该示例时加入 [samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf) 附加配置，以启用 Mesh 支持。

> 译注——双核职责：本段 HCI IPC 指网络核上的控制器应用，附加配置也用于该控制器构建；应用核运行本页 Mesh 应用。两核固件及目标须分别核对，不能只给应用核添加控制器选项就认为网络核已具备 Mesh 支持。配置原件见[HCI IPC附加配置](../../../samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf)，版本和核间连接方法参见[HCI IPC译文](../intercore_reference/P189_蓝牙HCI的IPC示例.md)。

<a id="interacting-with-the-sample"></a>

## 51.4 与示例交互（Interacting with the sample）

本示例既可由外部配网器设备加入已有 Mesh 网络，也可通过按键自行配网（Self-provisioning）。

使用配网器设备配网时，配网器必须向设备提供应用密钥（Application key），并将其绑定到两个 Generic OnOff 模型。

自行配网时，设备采用随机单播地址（Unicast address），并向这些模型绑定一个演示用应用密钥。

> 译注——演示地址和密钥：原文称“随机地址”，本次源码实际上由设备 UUID 的低位或启动时间低位截取十五位；它不提供网络级唯一分配保证。自行配网使用演示密钥并直接绑定模型，适合演示；正式地址分配与密钥管理应遵循[Mesh指南](../bluetooth/大纲.md)及实际配网流程。

配网完成后，发往 Generic OnOff Server 的消息用于开关 LED；按键则向同一网络的所有节点广播 OnOff 消息。

<a id="see-also"></a>

## 51.5 另请参阅（See also）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：本仓库的[src/main.c](../../../samples/bluetooth/mesh/src/main.c)与[prj.conf](../../../samples/bluetooth/mesh/prj.conf)供相对路径跟踪；源码版本可能不同于本次官方网页快照。

对应官方文档源码：[samples/bluetooth/mesh/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/mesh/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/mesh/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P050_自定义GAP服务.md) · [返回大纲](大纲.md) · [下一章](P052_Mesh演示.md)
