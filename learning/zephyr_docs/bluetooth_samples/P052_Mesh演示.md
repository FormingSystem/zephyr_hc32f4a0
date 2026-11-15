---
id: learning.zephyr-docs.bluetooth-samples.page-52
title: Mesh演示
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_demo/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_mesh_demo"></a>

# 第52章\_Mesh 演示（Mesh Demo）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_demo/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/mesh_demo/README.rst/..)

<a id="overview"></a>

## 52.1 概述（Overview）

本示例是仅用于演示的蓝牙 Mesh 应用。它使用写死的网络密钥与应用密钥，自行配网并配置，无须外部配网器。本地单播地址可通过 NODE_ADDR 构建变量设置，例如 NODE_ADDR=0x0001 对应单播地址 0x0001；也可手工修改 `board.h` 中的值。

> 译注——构建变量与节点身份：`NODE_ADDR` 是示例 CMakeLists.txt 读取的构建变量，不是 Kconfig 符号。地址与硬编码密钥共同参与这个演示网络；为多个节点选择不同地址，不能把相同默认地址复制到所有设备后期待正常单播。`0x000f` 的特殊功能是本应用约定，不是蓝牙 Mesh 对该地址的通用定义。

由于采用写死的值，本应用不适合直接用于生产，但很适合快速演示 Mesh 功能。

应用包含专为 BBC micro:bit 设计的功能，例如通过板载按钮发送消息，在 5×5 LED 显示屏上显示收到消息的信息。通常建议 micro:bit 使用 0x0001～0x0009 的单播地址范围，便于显示地址，也便于用按钮循环选择目标地址列表。

特殊地址 0x000f 会使应用成为心跳发布者（Heartbeat publisher），并让其他节点显示收到的心跳消息信息。

<a id="requirements"></a>

## 52.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板；或者

- QEMU，以及主机上运行的 BlueZ。

<a id="building-and-running"></a>

## 52.3 构建与运行（Building and Running）

> 译注——执行环境：以下官方命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门文档](../getting_started/大纲.md)准备工具链、west工作区、板定义与所需蓝牙控制器；`samples/...` 是官方已有目录，`<board>` 需替换为实际板目标。构建成功后才按板文档烧录，并通过本页描述的连接、服务发现、订阅或配网步骤观察结果；失败时分别回查构建配置、烧录器或对端角色与功能支持。构建输出由工具生成，中文目录不作为固件工作目录。本次仅核对文档，未执行这些操作。

在 QEMU 中运行示例的详情，参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

其他开发板可按以下方式构建并烧录应用：

```text
west build -b <board> samples/bluetooth/mesh_demo
west flash
```

若开发板不支持 `flash` 目标，请查阅[该板文档](https://docs.zephyrproject.org/latest/boards/index.html#boards)中的其他烧录方法。

在 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk) 上运行本应用时，网络核还必须运行蓝牙控制器应用，可以使用 [HCI IPC](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) 示例。构建该示例时加入 [samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf) 附加配置，以启用 Mesh 支持。

> 译注——双核职责：本段 HCI IPC 指网络核上的控制器应用，附加配置也用于该控制器构建；应用核运行本页 Mesh 应用。两核固件及目标须分别核对，不能只给应用核添加控制器选项就认为网络核已具备 Mesh 支持。配置原件见[HCI IPC附加配置](../../../samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf)，版本和核间连接方法参见[HCI IPC译文](../intercore_reference/P189_蓝牙HCI的IPC示例.md)。

<a id="see-also"></a>

## 52.4 另请参阅（See also）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：本仓库的[src/main.c](../../../samples/bluetooth/mesh_demo/src/main.c)与[prj.conf](../../../samples/bluetooth/mesh_demo/prj.conf)供相对路径跟踪；源码版本可能不同于本次官方网页快照。

对应官方文档源码：[samples/bluetooth/mesh_demo/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/mesh_demo/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/mesh_demo/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P051_Mesh基本示例.md) · [返回大纲](大纲.md) · [下一章](P053_Mesh配网器.md)
