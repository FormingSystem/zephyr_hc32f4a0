---
id: learning.zephyr-docs.api-platform-topic-reference.page-100
title: FocalTech FT9001 复位控制器辅助工具（Reset controller helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__focaltech__ft9001.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_FocalTech FT9001 复位控制器辅助工具（Reset controller helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__focaltech__ft9001.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FocalTech FT9001复位控制器辅助定义。

<a id="details"></a>

FocalTech FT9001 复位控制器辅助宏（Reset Controller Helpers）。用于编码 FT9001 设备外设复位单元（Peripheral Reset Cells）的设备树宏（Devicetree Macros），与 `focaltech,ft9001-cpm-rctl` 兼容复位控制器配合使用。复位标识（Reset Identifiers）遵循 `FOCALTECH_RESET_<PERIPHERAL>` 格式，其中 `<PERIPHERAL>` 为参考手册中的 FT9001 外设名称。例如，`FOCALTECH_RESET_SCI2` 复位 SCI2，`FOCALTECH_RESET_EPORT0` 复位 EPORT0。将这些标识直接传入 `resets` 属性。

```c
#include <zephyr/dt-bindings/reset/focaltech_ft9001_reset.h>

&sci2 {
        resets = <&rctl FOCALTECH_RESET_SCI2>;
};
```

<a id="header-groups"></a>
<a id="groups"></a>

## 100.1\_主题（Topics）

<a id="r_focaltech_5Freset_5Fregs"></a>

相关声明：[FocalTech 复位控制模块寄存器（Reset Control Module Registers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html)。

复位控制模块寄存器的偏移量。

<a id="r_focaltech_5Freset_5Fenables"></a>

相关声明：[FocalTech 复位使能/禁用定义（Reset Enable/Disable Definitions）](../api_topic_reference/P038_FocalTech 复位使能_禁用定义（Reset Enable_Disable Definitions）.md)。

外设的复位使能/禁用定义。

<a id="header-files"></a>
<a id="files"></a>

## 100.2\_文件（Files）

<a id="r_focaltech_5Fft9001_5Freset_2Eh"></a>

```c
file focaltech_ft9001_reset.h
```

相关声明：[focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)。

FocalTech FT9001的外设复位标识符（Peripheral Reset Identifiers）。


## 100.3\_原页交叉引用（Cross References）

- [FocalTech 复位控制模块寄存器（Reset Control Module Registers）](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__reset__regs.html)
- [FocalTech 复位使能/禁用定义（Reset Enable/Disable Definitions）](../api_topic_reference/P038_FocalTech 复位使能_禁用定义（Reset Enable_Disable Definitions）.md)
- [focaltech_ft9001_reset.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__reset_8h.html)

<a id="header-details"></a>

---

[上一章](P099_瑞萨（Renesas）RA.md) · [返回大纲](大纲.md) · [下一章](P101_GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）.md)
