---
id: learning.zephyr-docs.boards-shields.page-112
title: MikroElektronika LTE IoT 7 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_lte_iot7_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-lte-iot-7-click"></a>

<a id="mikroe-lte-iot7-click-shield"></a>

# 第112章\_MikroElektronika LTE IoT 7 Click蜂窝通信扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lte_iot7_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[LTE IoT 7 Click](https://www.mikroe.com/lte-iot-7-click)是用于LTE-M及NB-IoT应用的紧凑蜂窝通信扩展板。

Zephyr将其建模为使用u-blox,sara-r4兼容字符串、通过mikroBUS UART连接的调制解调器；方向及控制信号连接如下：


- AN用作电源控制POWER
- RST用作复位RESET
- CS通过固定稳压器节点用作RTS使能控制

<a id="id1"></a>

[![官方原图：LTE IoT 7 Click](images/mikroe_lte_iot7_click.webp)](images/mikroe_lte_iot7_click.webp)

LTE IoT 7 Click蜂窝通信扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板要求开发板提供以下mikroBUS别名：


- `mikrobus_uart`
- `mikrobus_header`

插座选择由开发板DTS别名控制，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-DSHIELD=mikroe_lte_iot7_click，例如：

```text
# From the root of the zephyr repository
west build -b mikroe_clicker_2 --shield mikroe_lte_iot7_click samples/drivers/modem/at_client
```

<a id="references"></a>

## 参考资料（References）


- [LTE IoT 7 Click蜂窝通信扩展板](https://www.mikroe.com/lte-iot-7-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [lte-iot-7-click](https://www.mikroe.com/lte-iot-7-click)：HTTP Error 403: Forbidden。

---

[上一章](P111_MikroElektronika_LTE_IoT_10_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P113_MikroElektronika_MCP251x_Click_shields.md)
