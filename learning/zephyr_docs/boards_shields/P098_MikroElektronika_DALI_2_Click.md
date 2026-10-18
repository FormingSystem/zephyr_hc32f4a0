---
id: learning.zephyr-docs.boards-shields.page-98
title: MikroElektronika DALI 2 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_dali_2_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-dali-2-click"></a>

<a id="mikroe-dali-2-click-shield"></a>

# 第98章\_MikroElektronika DALI 2 Click照明总线扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_dali_2_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

DALI 2 Click提供DALI总线物理接口，使用独立RX及TX信号通信，并用光耦隔离DALI总线与主板。

<a id="id3"></a>

更多信息见Mikroe DALI 2 Click [注1](#id2)。（[Mikroe DALI 2 click模块](https://www.mikroe.com/dali-2-click)）

<a id="id1"></a>

[![官方原图：MikroElektronika DALI 2 Click](images/dali_2_click.webp)](images/dali_2_click.webp)

MikroElektronika DALI 2 Click照明总线扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板使用mikroBUS，目标板须定义mikrobus_header节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_dali_2_click，例如：

```text
# From the root of the zephyr repository
west build -b <board> --shield mikroe_dali_2_click samples/drivers/dali/
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/dali-2-click](https://www.mikroe.com/dali-2-click)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [dali-2-click](https://www.mikroe.com/dali-2-click)：HTTP Error 403: Forbidden。

---

[上一章](P097_MikroElektronika_CAN_FD_6_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P099_MikroElektronika_EEPROM_13_Click.md)
