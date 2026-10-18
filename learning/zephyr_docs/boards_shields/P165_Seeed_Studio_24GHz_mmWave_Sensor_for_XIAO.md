---
id: learning.zephyr-docs.boards-shields.page-165
title: Seeed Studio 24GHz mmWave Sensor for XIAO
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_hsp24/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="seeed-studio-24ghz-mmwave-sensor-for-xiao"></a>

<a id="seeed-xiao-hsp24"></a>

# 第165章\_Seeed Studio XIAO 24 GHz毫米波传感器（mmWave Sensor）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_hsp24/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Seeed Studio XIAO 24 GHz毫米波传感器是UART雷达模块，用于报告人体存在及距离。（[Seeed Studio XIAO 24 GHz毫米波传感器（mmWave Sensor）](https://wiki.seeedstudio.com/mmwave_for_xiao/)）

<a id="id2"></a>

![官方原图：Seeed Studio 24GHz mmWave Sensor for XIAO](images/seeed_xiao_hsp24.webp)

Seeed Studio XIAO 24 GHz毫米波传感器，图片来源：Seeed Studio

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板可用于提供XIAO连接器标签及xiao_serial节点标签的开发板。模块UART RX／TX连接XIAO接口D2／D3，因此使用时可能需要覆盖开发板默认引脚复用配置。

雷达模块与开发板UART波特率必须一致。模块出厂默认波特率为256000，因此此扩展板默认将xiao_serial设为256000。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield seeed_xiao_hsp24。

例如，使用[Iclegend S3KM1110毫米波传感器](../sensors/P067_S3KM1110毫米波传感器示例.md#s3km1110)示例：

```text
# From the root of the zephyr repository
west build -b xiao_esp32c6/esp32c6/hpcore --shield seeed_xiao_hsp24 samples/sensor/s3km1110
```

## 译注

默认256000波特率；模块RX／TX占用D2／D3，常需覆盖主板默认引脚复用。

---

[上一章](P164_Seeed_Studio_XIAO_Expansion_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P166_Seeed_Studio_XIAO_Round_Display.md)
