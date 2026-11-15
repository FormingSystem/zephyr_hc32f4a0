---
id: learning.zephyr-docs.bluetooth-samples.page-31
title: Eddystone信标
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/eddystone/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_eddystone"></a>

# 第31章\_Eddystone 信标（Eddystone）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/eddystone/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/eddystone/README.rst/..)

<a id="overview"></a>

## 31.1 概述（Overview）

本应用演示 [Eddystone 配置服务（Eddystone Configuration Service）](https://github.com/google/eddystone/tree/master/configuration-service)。

> 译注——服务用途：本例重点是可连接信标上的 GATT 配置服务，不等于只发出一个固定广播包。广播、连接后发现配置服务、写入配置分别是不同观察点；使用的客户端也须支持对应服务。

当信标可连接时，Eddystone 配置服务作为 GATT 服务运行，允许配置广播数据、发射功率等级及广播间隔。该服务也构成 Eddystone-EID 信标配置方法及向可信解析器（Trusted resolver）注册方法的一部分。

<a id="requirements"></a>

## 31.2 前提条件（Requirements）

- 主机上运行 BlueZ；或者

- 一块支持 Bluetooth LE 的开发板。

<a id="building-and-running"></a>

## 31.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/eddystone
west flash
```

烧录后，设备作为可连接的 Eddystone 信标开始广播。使用兼容 Eddystone 配置服务的应用，例如 nRF Connect，连接并配置广播数据、发射功率等级及广播间隔。

<a id="see-also"></a>

## 31.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/eddystone/src/main.c)、[prj.conf](../../../samples/bluetooth/eddystone/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/eddystone/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/eddystone/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/eddystone/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P030_定向广播.md) · [返回大纲](大纲.md) · [下一章](P032_加密广播.md)
