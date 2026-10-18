---
id: learning.zephyr-docs.api-platform-topic-reference.page-117
title: Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m55m1x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__nuvoton__m55m1x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

M55M1X 设备的外设复位单元（reset-cell）标识符。

<a id="details"></a>

M55M1X 设备的外设复位单元标识（Peripheral Reset-Cell Identifiers）。复位标识遵循 `NUMAKER_SYS_<PERIPHERAL>RST` 格式，其中 `<PERIPHERAL>` 为 M55M1X 外设名称。例如，`NUMAKER_SYS_UART0RST` 复位 UART0。将这些标识直接传入 `resets` 属性。

<a id="header-files"></a>
<a id="files"></a>

## 117.1\_文件（Files）

<a id="r_numaker_5Fm55m1x_5Freset_2Eh"></a>

```c
file numaker_m55m1x_reset.h
```

相关声明：[numaker_m55m1x_reset.h](../api_file_reference/P272_zephyr__dt-bindings__reset__numaker_m55m1x_reset.h_文件参考.md)。

Nuvoton NuMaker M55M1X的外设复位标识符（Peripheral Reset Identifiers）。


## 117.2\_原页交叉引用（Cross References）

- [numaker_m55m1x_reset.h](../api_file_reference/P272_zephyr__dt-bindings__reset__numaker_m55m1x_reset.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P116_Nuvoton M48X 复位控制器设备树辅助工具（Reset controller Devicetree helpers）.md) · [返回大纲](大纲.md) · [下一章](P118_Raspberry Pi RP2040复位控制器辅助定义.md)
