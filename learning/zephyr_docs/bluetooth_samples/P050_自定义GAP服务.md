---
id: learning.zephyr-docs.bluetooth-samples.page-50
title: 自定义GAP服务
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_gap_svc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_gap_svc"></a>

# 第50章\_外设侧自定义 GAP 服务（Peripheral GAP service custom implementation）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/peripheral_gap_svc/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/peripheral_gap_svc/README.rst/..)

<a id="overview"></a>

## 50.1 概述（Overview）

本示例演示在应用侧实现通用访问配置文件（Generic Access Profile，GAP）服务。这里限制设备名写入操作：名称必须以大写字母开头。用户连接设备并尝试设置名称时，只接受以大写字母开头的名称，并在名称改变后立即记录日志。

> 译注——校验规则的边界：本次 `write_name()` 实际检查首字节是否处于 ASCII `A`～`Z`；这是示例自定义规则，不是蓝牙核心规范对设备名的要求。非零写入偏移、超长内容和不合规则的首字节会分别返回 ATT 错误，名称并非仅凭任意语言中的“大写”概念就会被接受。

<a id="requirements"></a>

## 50.2 前提条件（Requirements）

- 主机上运行 BlueZ；或者

- 一块支持 Bluetooth LE 的开发板。

<a id="building-and-running"></a>

## 50.3 构建与运行（Building and Running）

> 译注——执行环境：以下官方命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门文档](../getting_started/大纲.md)准备工具链、west工作区、板定义与所需蓝牙控制器；`samples/...` 是官方已有目录，`<board>` 需替换为实际板目标。构建成功后才按板文档烧录，并通过本页描述的连接、服务发现、订阅或配网步骤观察结果；失败时分别回查构建配置、烧录器或对端角色与功能支持。构建输出由工具生成，中文目录不作为固件工作目录。本次仅核对文档，未执行这些操作。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/peripheral_gap_svc
west flash
```

烧录后，使用蓝牙扫描应用，例如 nRF Connect，连接设备，尝试通过 GAP Device Name（GAP 设备名）特征写入新名称。不是以大写字母开头的名称会被拒绝，接受的名称会记录到设备控制台。

<a id="see-also"></a>

## 50.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——源码入口：本仓库的[src/main.c](../../../samples/bluetooth/peripheral_gap_svc/src/main.c)与[prj.conf](../../../samples/bluetooth/peripheral_gap_svc/prj.conf)供相对路径跟踪；源码版本可能不同于本次官方网页快照。

对应官方文档源码：[samples/bluetooth/peripheral_gap_svc/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/peripheral_gap_svc/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/peripheral_gap_svc/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P049_经过时间服务外设.md) · [返回大纲](大纲.md) · [下一章](P051_Mesh基本示例.md)
