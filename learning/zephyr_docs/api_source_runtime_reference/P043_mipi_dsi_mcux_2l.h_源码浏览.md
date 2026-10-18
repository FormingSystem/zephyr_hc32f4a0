---
id: learning.zephyr-docs.api-source-runtime-reference.page-43
title: mipi_dsi_mcux_2l.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mipi__dsi__mcux__2l_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_mipi\_dsi\_mcux\_2l.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mipi__dsi__mcux__2l_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mipi__dsi__mcux__2l_8h.html)。

## 43.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>

```c
/*
 * Copyright 2023,2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_MCUX_2L_
#define ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_MCUX_2L_

/*
 * HW specific flag- indicates to the MIPI DSI 2L peripheral that the
 * data being sent is framebuffer data, which the DSI peripheral may
 * byte swap depending on KConfig settings
 */
#define MCUX_DSI_2L_FB_DATA BIT(0x1)

/*
 * HW specific flag - user set this bit in message flag and after the
 * transfer bus will enter ULPS.
 */
#define MCUX_DSI_2L_ULPS BIT(0x2)

#endif /* ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_MCUX_2L_ */
```

## 43.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023,2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

硬件专用标志，告知 MIPI DSI 2L 外设正在发送的是帧缓冲区数据（Framebuffer data）；DSI 外设可能根据 Kconfig 设置对这些数据进行字节交换（Byte swap）。

### 注释 3：原第 16 行

硬件专用标志：用户在消息标志中设置此位后，总线将在传输结束后进入超低功耗状态（ULPS）。

### 注释 4：原第 22 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MIPI_DSI_MCUX_2L_`。

## 43.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mipi__dsi__mcux__2l_8h.html)

---

[上一章](P042_media_proxy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P044_mpipe_thread.h_源码浏览.md)
