---
id: learning.zephyr-docs.boards-shields.page-117
title: MikroElektronika RS485 Isolator 5 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_rs485_isolator_5_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-rs485-isolator-5-click"></a>

<a id="mikroe-rs485-isolator-5-click-shield"></a>

# 第117章\_MikroElektronika RS485 Isolator 5 Click隔离扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_rs485_isolator_5_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[RS485 Isolator 5 Click](https://www.mikroe.com/rs485-isolator-5-click)是隔离RS-485收发器扩展板，在UART侧与RS-485总线侧之间提供电气隔离（Galvanic Isolation）。

<a id="id1"></a>

[![官方原图：RS485 Isolator 5 Click](images/mikroe_rs485_isolator_5_click.webp)](images/mikroe_rs485_isolator_5_click.webp)

RS485 Isolator 5 Click隔离扩展板

Zephyr将其建模为使用zephyr,modbus-serial兼容字符串的Modbus RTU串口后端，方向控制连接以下mikroBUS信号：


- AN用作驱动使能DE
- RST用作低有效接收使能RE

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板要求开发板提供以下mikroBUS别名：


- `mikrobus_uart`
- `mikrobus_header`

插座选择由开发板DTS别名控制，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_rs485_isolator_5_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_2/stm32f407xx --shield mikroe_rs485_isolator_5_click samples/subsys/modbus/rtu_client -- -DDTC_OVERLAY_FILE=""
```


---


- [RS485 Isolator 5 Click隔离扩展板](https://www.mikroe.com/rs485-isolator-5-click)
- [RS485 Isolator 5 Click原理图](https://download.mikroe.com/documents/add-on-boards/click/rs485-isolator-5/rs485-isolator-5-click-schematic-v100.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [rs485-isolator-5-click-schematic-v100.pdf](https://download.mikroe.com/documents/add-on-boards/click/rs485-isolator-5/rs485-isolator-5-click-schematic-v100.pdf)：HTTP Error 403: Forbidden。
- [rs485-isolator-5-click](https://www.mikroe.com/rs485-isolator-5-click)：HTTP Error 403: Forbidden。

---

[上一章](P116_MikroElektronika_Proximity_9_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P118_MikroElektronika_RTC_18_Click.md)
