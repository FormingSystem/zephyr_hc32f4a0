---
id: learning.zephyr-docs.api-platform-topic-reference.page-109
title: GigaDevice复位控制器辅助定义
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gigadevice.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第109章\_GigaDevice复位控制器辅助定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gigadevice.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于编码GD32外设复位说明单元的宏。

<a id="details"></a>

用于编码 GD32 外设复位单元（Peripheral Reset Cells）的宏。GigaDevice GD32 设备使用这些设备树宏（Devicetree Macros），与 `gd,gd32-rctl` 兼容复位控制器配合。每个 SoC 系列头文件（如 `gd32f4xx.h`）定义该系列的复位和时钟单元（RCU）复位寄存器偏移（Register Offsets），以及以 `GD32_RESET_<peripheral>` 常量表示的外设复位标识（Reset Identifiers）。外设复位单元由 RCU 寄存器偏移与该寄存器内外设复位线的位位置（Bit Position）组合编码。

```c
#include <zephyr/dt-bindings/reset/gd32f4xx.h>

&usart0 {
        resets = <&rctl GD32_RESET_USART0>;
};
```

<a id="header-groups"></a>
<a id="groups"></a>

## 109.1\_主题（Topics）

<a id="r_reset_5Fcontroller_5Fgd32a50x"></a>

相关声明：[GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）](P101_GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32e10x"></a>

相关声明：[GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）](P102_GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32e50x"></a>

相关声明：[GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）](P103_GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32f3x0"></a>

相关声明：[GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）](P104_GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32f403"></a>

相关声明：[GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）](P105_GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32f4xx"></a>

相关声明：[GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）](P106_GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32l23x"></a>

相关声明：[GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）](P107_GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）

<a id="r_reset_5Fcontroller_5Fgd32vf103"></a>

相关声明：[GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）](P108_GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）.md)。

GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）

<a id="header-files"></a>
<a id="files"></a>

## 109.2\_文件（Files）

<a id="r_gd32-common_2Eh"></a>

```c
file gd32-common.h
```

相关声明：[gd32-common.h](../api_file_reference/P116_zephyr__dt-bindings__reset__gd32-common.h_文件参考.md)。

GD32复位控制器（Reset Controller）的设备树辅助宏。


## 109.3\_原页交叉引用（Cross References）

- [GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）](P101_GigaDevice GD32A50x 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）](P102_GigaDevice GD32E10x 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）](P103_GigaDevice GD32E50x 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）](P104_GigaDevice GD32F3x0 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）](P105_GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）](P106_GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）](P107_GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）.md)
- [GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）](P108_GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）.md)
- [gd32-common.h](../api_file_reference/P116_zephyr__dt-bindings__reset__gd32-common.h_文件参考.md)
- [gd32f4xx.h](../api_file_reference/P128_zephyr__dt-bindings__reset__gd32f4xx.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P108_GigaDevice GD32VF103 复位控制器辅助工具（Reset controller helpers）.md) · [返回大纲](大纲.md) · [下一章](P110_Nuvoton NuMaker复位控制器辅助定义.md)
