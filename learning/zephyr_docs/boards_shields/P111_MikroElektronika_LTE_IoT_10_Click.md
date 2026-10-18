---
id: learning.zephyr-docs.boards-shields.page-111
title: MikroElektronika LTE IoT 10 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_lte_iot10_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-lte-iot-10-click"></a>

<a id="mikroe-lte-iot10-click-shield"></a>

# 第111章\_MikroElektronika LTE IoT 10 Click蜂窝通信扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lte_iot10_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

LTE IoT 10 Click是紧凑附加板，为工业及商业物联网提供可靠LTE-M及NB-IoT连接。

它采用Sequans Monarch 2 GM02S双模LTE-M／NB-IoT模块，基于SQN3430芯片组，支持617 MHz～2.2 GHz全球频段。

<a id="id1"></a>

![官方原图：MikroElektronika LTE IoT 10 Click](images/mikroe_lte_iot10_click.webp)

MikroElektronika LTE IoT 10 Click蜂窝通信扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS连接器配置，并为UART定义mikrobus_serial节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

更多GM02S模块及LTE IoT 10 Click信息见：


- <a id="id3"></a>

  GM02S数据手册[注1](#id2)（[GM02S 数据手册](https://www.sequans.com/products-solutions/gm02s/)）
- <a id="id5"></a>

  [LTE IoT 10 Click](https://www.mikroe.com/lte-iot-10-click)扩展板[注2](#id4)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_lte_iot10_click，下面以蜂窝调制解调器示例为例：（[蜂窝调制解调器（Cellular Modem）](../networking/P214_蜂窝调制解调器示例.md#cellular-modem)）

```text
# From the root of the zephyr repository
west build -b ek_ra6m4 --shield mikroe_lte_iot10_click samples/net/cellular_modem
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.sequans.com/products-solutions/gm02s/](https://www.sequans.com/products-solutions/gm02s/)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.mikroe.com/lte-iot-10-click](https://www.mikroe.com/lte-iot-10-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [lte-iot-10-click](https://www.mikroe.com/lte-iot-10-click)：HTTP Error 403: Forbidden。

---

[上一章](P110_MikroElektronika_LSM6DSL_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P112_MikroElektronika_LTE_IoT_7_Click.md)
