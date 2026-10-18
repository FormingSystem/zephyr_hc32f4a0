---
id: learning.zephyr-docs.boards-shields.page-109
title: MikroElektronika LIN Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_lin_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-lin-click"></a>

<a id="mikroe-lin-click-shield"></a>

# 第109章\_MikroElektronika LIN Click总线扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_lin_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id4"></a>

LIN Click采用Infineon [TLE7259-3GE](https://www.infineon.com/part/TLE7259-3GE) LIN收发器[注2](#id3)，集成唤醒及保护功能。

通过设置板上的相应模式选择寄存器，可配置LIN指挥节点（Commander）或响应节点（Responder）应用；寄存器一词按原文保留。

<a id="id2"></a>

更多信息见Mikroe LIN Click [注1](#id1)。（[Mikroe LIN click模块](https://www.mikroe.com/lin-click)）

<a id="requirements"></a>

### 前置要求（Requirements）

扩展板使用mikroBUS，目标板须定义mikrobus_header及mikrobus_lin节点标签，分别提供GPIO及LIN接口，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

### 编程（Programming）

调用west build时设置--shield mikroe_lin_click，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8m1 --shield mikroe_lin_click samples/drivers/lin/ncv7430
west flash
```

<a id="references"></a>

### 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://www.mikroe.com/lin-click](https://www.mikroe.com/lin-click)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.infineon.com/part/TLE7259-3GE](https://www.infineon.com/part/TLE7259-3GE)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [lin-click](https://www.mikroe.com/lin-click)：HTTP Error 403: Forbidden。

---

[上一章](P108_MikroElektronika_IR_Gesture_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P110_MikroElektronika_LSM6DSL_Click.md)
