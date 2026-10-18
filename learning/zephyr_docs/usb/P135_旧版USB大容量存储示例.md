---
id: learning.zephyr-docs.usb.page-135
title: 旧版USB大容量存储示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/mass/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第135章\_旧版USB大容量存储示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/mass/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 135.1\_概述

此应用演示 Zephyr 提供的 USB 大容量存储（Mass Storage）驱动。这个简单驱动把带有 RAM 磁盘（RAM Disk）的开发板枚举为 USB 磁盘。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 135.2\_运行要求

此项目需要 USB 设备驱动，以及 96 KiB RAM 或一个闪存（Flash）设备。

## 135.3\_构建与运行

配置选择基于 RAM 的磁盘，不包含文件系统（File System）。

```shell
west build -b reel_board samples/subsys/usb/legacy/mass
```

> 译注：命令在已准备工具链与依赖的 Zephyr 源码根目录执行，目标为官方 `reel_board`。当前 `app.overlay` 声明名为 `RAM` 的 `zephyr,ram-disk`，扇区大小为 512 字节、数量为 192，总计 96 KiB；这仅是磁盘数据容量，不代表整个固件只需 96 KiB RAM。默认配置没有自动改用闪存，若选用闪存需另外核对存储配置与目标分区。本页原文只给出构建命令，没有提供格式化或文件读写验证步骤。

## 135.4\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/mass/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/mass/src/main.c)、[samples/subsys/usb/legacy/mass/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/mass/prj.conf)、[samples/subsys/usb/legacy/mass/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/mass/app.overlay)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/mass/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-usb-mass"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P134_旧版USB示例目录.md) · [返回大纲](大纲.md) · [下一章](P136_旧版USB网络设备示例.md)
