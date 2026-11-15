---
id: learning.zephyr-docs.bluetooth-samples.page-28
title: BTHome传感器模板
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/bthome_sensor_template/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_bthome_sensor_template"></a>

# 第28章\_BTHome 传感器模板（BTHome sensor template）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/bthome_sensor_template/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/bthome_sensor_template/README.rst/..)

<a id="overview"></a>

## 28.1 概述（Overview）

本示例代码提供实现 [BTHome](https://bthome.io/) 传感器的模板。

> 译注——模拟数据：本次官方 [main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/bthome_sensor_template/src/main.c)循环模拟 0～25 °C 的温度，湿度载荷固定为 50.55%，没有读取真实温湿度传感器。Home Assistant 能发现模板不代表传感器硬件已接入；实际测量需要另行接入传感器并更新载荷。

<a id="requirements"></a>

## 28.2 前提条件（Requirements）

- 一块支持 Bluetooth LE 的开发板。

- 兼容 BTHome 的监听端（Listener），例如运行了 BTHome 集成的 [Home Assistant](https://www.home-assistant.io/)。

<a id="building-and-running"></a>

## 28.3 构建与运行（Building and Running）

> 译注——构建位置与前提：以下是官方示例命令，在读者自己的 Zephyr 源码根目录中，使用 UCRT64 Bash 或 Linux Bash 执行；先完成[入门环境](../getting_started/大纲.md)，并确认所选板及控制器支持本文所需蓝牙能力。`samples/...` 是官方已有示例目录，`<board>` 是须替换的板目标占位符；构建输出由工具生成，不在本中文目录创建同名源码。先检查构建成功及板目标，再按板文档烧录并观察本文行为或日志；构建、烧录或通信失败时，分别回查工具链／板配置、烧录器和两端角色／控制器能力。本次未构建或运行示例。

按以下方式构建并烧录，将 `<board>` 替换为目标开发板：

```text
west build -b <board> samples/bluetooth/bthome_sensor_template
west flash
```

示例运行后，在 Home Assistant 的设置中打开 Devices & Services（设备与服务）。如果一切正常，界面将提示配置 BTHome 传感器。

<a id="see-also"></a>

## 28.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[src/main.c](../../../samples/bluetooth/bthome_sensor_template/src/main.c)、[prj.conf](../../../samples/bluetooth/bthome_sensor_template/prj.conf)为本仓库的相对源码入口。与本次上游快照的版本差异须分别核对，不能把译文当作本地硬件已支持的证明。

对应官方文档源码：[samples/bluetooth/bthome_sensor_template/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/bthome_sensor_template/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/bthome_sensor_template/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P027_多实例广播.md) · [返回大纲](大纲.md) · [下一章](P029_中心设备PAST.md)
