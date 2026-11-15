---
id: learning.zephyr-docs.bluetooth-samples.page-53
title: Mesh配网器
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_provisioner/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_mesh_provisioner"></a>

# 第53章\_Mesh 配网器（Mesh Provisioner）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/mesh_provisioner/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/mesh_provisioner/README.rst/..)

<a id="overview"></a>

## 53.1 概述（Overview）

本示例演示蓝牙 Mesh 配网及配置数据库（Configuration Database，CDB）相关 API，应与可被配网的设备一起测试，例如 [samples/bluetooth/mesh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/mesh) 或 [tests/bluetooth/mesh_shell](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bluetooth/mesh_shell) 中的应用。

应用先自行配网，并向 CDB 载入应用密钥，然后等待设备发出未配网信标（Unprovisioned Beacon）。若板上有 GPIO 按钮且通过[设备树](../devicetree/P013_设备树文档入口.md#dt-guide)别名 `sw0` 配置，应用会等待用户按键，以 PB-ADV 触发配网；没有该按钮时，则自动为检测到的设备配网。配网完成后，节点已存在于 CDB，但尚未标记为已配置。应用发现未配置节点后开始配置，没有遇到错误时，才将节点标记为已配置。

> 译注——按钮开关：本次实现通过 `CONFIG_MESH_PROVISIONER_USE_SW0` 控制等待按键的路径，该选项依赖启用的 `sw0` 别名并默认开启。按键模式中，检测到设备后等待三十秒，超时返回检测流程；关闭此选项则可自动配网。应结合[示例Kconfig](../../../samples/bluetooth/mesh_provisioner/Kconfig)和实际生成配置判断，不能只看板上是否焊了按钮。

节点配置包括添加应用密钥、获取组成数据（Composition data），并将节点的全部模型绑定到该应用密钥。

> 译注——模型绑定例外与状态：原文概述写“全部模型”，但本次官方 `configure_node()` 跳过 Configuration Client／Server 模型，它们不按普通应用模型绑定 AppKey。其他 SIG／厂商模型的部分绑定失败只打印错误后继续，循环结束仍可能设置 `BT_MESH_CDB_NODE_CONFIGURED`。因此 CDB 的已配置标记或 Configuration complete 日志不能单独证明每个模型绑定成功，应逐项核对配置响应与目标模型状态；源码见[main.c](../../../samples/bluetooth/mesh_provisioner/src/main.c)。

<a id="requirements"></a>

## 53.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板；或者

- QEMU，以及主机上运行的 BlueZ。

<a id="building-and-running"></a>

## 53.3 构建与运行（Building and Running）

> 译注——执行环境：以下官方命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门文档](../getting_started/大纲.md)准备工具链、west工作区、板定义与所需蓝牙控制器；`samples/...` 是官方已有目录，`<board>` 需替换为实际板目标。构建成功后才按板文档烧录，并通过本页描述的连接、服务发现、订阅或配网步骤观察结果；失败时分别回查构建配置、烧录器或对端角色与功能支持。构建输出由工具生成，中文目录不作为固件工作目录。本次仅核对文档，未执行这些操作。

在 QEMU 中运行示例的详情，参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

其他开发板可按以下方式构建并烧录应用：

```text
west build -b <board> samples/bluetooth/mesh_provisioner
west flash
```

若开发板不支持 `flash` 目标，请查阅[该板文档](https://docs.zephyrproject.org/latest/boards/index.html#boards)中的其他烧录方法。

在 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk) 上运行本应用时，网络核还必须运行蓝牙控制器应用，可以使用 [HCI IPC](../intercore_reference/P189_蓝牙HCI的IPC示例.md#bluetooth_hci_ipc) 示例。构建该示例时加入 [samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf) 附加配置，以启用 Mesh 支持。

> 译注——双核职责：本段 HCI IPC 指网络核上的控制器应用，附加配置也用于该控制器构建；应用核运行本页 Mesh 应用。两核固件及目标须分别核对，不能只给应用核添加控制器选项就认为网络核已具备 Mesh 支持。配置原件见[HCI IPC附加配置](../../../samples/bluetooth/hci_ipc/extra-bt_mesh-bt_ll_sw_split.conf)，版本和核间连接方法参见[HCI IPC译文](../intercore_reference/P189_蓝牙HCI的IPC示例.md)。

<a id="see-also"></a>

## 53.4 另请参阅（See also）

[蓝牙 Mesh（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：本仓库的[src/main.c](../../../samples/bluetooth/mesh_provisioner/src/main.c)与[prj.conf](../../../samples/bluetooth/mesh_provisioner/prj.conf)供相对路径跟踪；源码版本可能不同于本次官方网页快照。

对应官方文档源码：[samples/bluetooth/mesh_provisioner/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/mesh_provisioner/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/mesh_provisioner/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P052_Mesh演示.md) · [返回大纲](大纲.md) · [下一章](P054_测向中心设备.md)
