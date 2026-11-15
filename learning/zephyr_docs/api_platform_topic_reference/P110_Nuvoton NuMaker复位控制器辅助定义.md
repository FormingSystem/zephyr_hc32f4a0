---
id: learning.zephyr-docs.api-platform-topic-reference.page-110
title: Nuvoton NuMaker复位控制器辅助定义
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__numaker.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_Nuvoton NuMaker复位控制器辅助定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__numaker.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nuvoton NuMaker设备的外设复位说明单元标识符。

<a id="details"></a>

Nuvoton NuMaker 设备的外设复位单元标识（Peripheral Reset-Cell Identifiers）。这些设备树宏（Devicetree Macros）与 `nuvoton,numaker-rst` 兼容复位控制器配合使用。每个 SoC 系列头文件定义的标识都编码了外设复位寄存器位置（Register Location）和位位置（Bit Position）。编码方式因系列而异；请直接使用提供的标识，不要手动构造复位单元值。

```c
#include <zephyr/dt-bindings/reset/numaker_m031x_reset.h>

&uart0 {
        // ...
        resets = <&rst NUMAKER_UART0_RST>;
        // ...
};
```

<a id="header-groups"></a>
<a id="groups"></a>

## 110.1\_主题（Topics）

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm031x"></a>

相关声明：[Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）](P111_Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）.md)。

M031X 设备的外设复位单元（reset-cell）标识符。

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm2l31x"></a>

相关声明：[Nuvoton NuMaker M2L31X 复位控制器辅助工具（Reset controller helpers）](P112_Nuvoton NuMaker M2L31X 复位控制器辅助工具（Reset controller helpers）.md)。

M2L31X 设备的外设复位单元（reset-cell）标识符。

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm333x"></a>

相关声明：[Nuvoton NuMaker M333X 复位控制器辅助工具（Reset controller helpers）](P113_Nuvoton NuMaker M333X 复位控制器辅助工具（Reset controller helpers）.md)。

M333X 设备的外设复位单元（reset-cell）标识符。

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm335x"></a>

相关声明：[Nuvoton NuMaker M335X 复位控制器辅助工具（Reset controller helpers）](P114_Nuvoton NuMaker M335X 复位控制器辅助工具（Reset controller helpers）.md)。

M335X 设备的外设复位单元（reset-cell）标识符。

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm46x"></a>

相关声明：[Nuvoton NuMaker M46X 复位控制器辅助工具（Reset controller helpers）](P115_Nuvoton NuMaker M46X 复位控制器辅助工具（Reset controller helpers）.md)。

M46X 设备的外设复位单元（reset-cell）标识符。

<a id="r_reset_5Fcontroller_5Fnuvoton_5Fm55m1x"></a>

相关声明：[Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）](P117_Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）.md)。

M55M1X 设备的外设复位单元（reset-cell）标识符。


## 110.2\_原页交叉引用（Cross References）

- [Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）](P111_Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）.md)
- [Nuvoton NuMaker M2L31X 复位控制器辅助工具（Reset controller helpers）](P112_Nuvoton NuMaker M2L31X 复位控制器辅助工具（Reset controller helpers）.md)
- [Nuvoton NuMaker M333X 复位控制器辅助工具（Reset controller helpers）](P113_Nuvoton NuMaker M333X 复位控制器辅助工具（Reset controller helpers）.md)
- [Nuvoton NuMaker M335X 复位控制器辅助工具（Reset controller helpers）](P114_Nuvoton NuMaker M335X 复位控制器辅助工具（Reset controller helpers）.md)
- [Nuvoton NuMaker M46X 复位控制器辅助工具（Reset controller helpers）](P115_Nuvoton NuMaker M46X 复位控制器辅助工具（Reset controller helpers）.md)
- [Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）](P117_Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）.md)

<a id="header-details"></a>

---

[上一章](P109_GigaDevice复位控制器辅助定义.md) · [返回大纲](大纲.md) · [下一章](P111_Nuvoton NuMaker M031X 复位控制器辅助工具（Reset controller helpers）.md)
