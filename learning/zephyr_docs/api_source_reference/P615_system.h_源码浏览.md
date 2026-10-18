---
id: learning.zephyr-docs.api-source-reference.page-615
title: system.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第615章\_system.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html)。

## 615.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="astdint_8h_html"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_SYSTEM_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_SYSTEM_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif


#define SCMI_NXP_SYSTEM_POWER_STATE_WAKE           0x80000000U
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN  0x80000001U
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET     0x80000002U
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND   0x80000003U
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE      0x80000004U
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN   0x80000005U
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET      0x80000006U
#define SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET   0x80000007U
#define SCMI_NXP_SYSTEM_POWER_STATE_MODE           0xC0000000U


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_SYSTEM_H_ */
```

## 615.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_SYSTEM_H_`。

## 615.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)

---

[上一章](P614_nxp,flexram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P616_nxp_clock_control.h_源码浏览.md)
