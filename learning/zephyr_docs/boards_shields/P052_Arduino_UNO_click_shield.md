---
id: learning.zephyr-docs.boards-shields.page-52
title: Arduino UNO click shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/arduino_uno_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arduino-uno-click-shield"></a>

<a id="arduino-uno-click"></a>

# 第52章\_Arduino UNO click扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/arduino_uno_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Arduino UNO click将Arduino UNO R3排针扩展为2个mikroBUS主机插座，可连接多种click扩展板；因此通常用作其他mikroBUS扩展板的转接板。

覆盖文件提供mikrobus_header_1及mikrobus_header_2，分别对应两个插座。

第一个插座mikrobus_header_1为默认插座，在覆盖文件中赋予mikrobus_header节点标签。

<a id="id2"></a>

更多信息见Arduino UNO click扩展板网站[注1](#id1)。（[Arduino UNO click模块 扩展板 网站](https://www.mikroe.com/arduino-uno-click-shield)）

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino R3连接器配置的开发板。

开发板还必须定义Arduino串口、SPI及I2C接口的节点别名，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

连接的扩展板应使用第一个插座mikrobus_header_1，其节点标签为mikrobus_header。

<a id="programming"></a>

## 编程（Programming）

与其他mikroBUS扩展板一起构建时，添加--shield arduino_uno_click，例如：

```text
# From the root of the zephyr repository
west build -b sam_v71_xult/samv71q21 --shield arduino_uno_click --shield atmel_rf2xx_mikrobus samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-802154.conf
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.mikroe.com/arduino-uno-click-shield](https://www.mikroe.com/arduino-uno-click-shield)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [arduino-uno-click-shield](https://www.mikroe.com/arduino-uno-click-shield)：HTTP Error 403: Forbidden。

---

[上一章](P051_Arduino_Modulino_Thermo.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P053_Atmel_AT86RF2XX_Transceivers.md)
