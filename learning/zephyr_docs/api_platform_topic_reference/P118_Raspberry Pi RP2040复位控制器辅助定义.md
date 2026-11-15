---
id: learning.zephyr-docs.api-platform-topic-reference.page-118
title: Raspberry Pi RP2040复位控制器辅助定义
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2040.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_Raspberry Pi RP2040复位控制器辅助定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__raspberrypi__rp2040.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RP2040片上系统（System on Chip，SoC）的外设复位说明单元标识符。

<a id="details"></a>

RP2040 片上系统（SoC）的外设复位单元标识（Peripheral Reset-Cell Identifiers）。Raspberry Pi RP2040 设备使用这些设备树宏（Devicetree Macros），与 `raspberrypi,pico-reset` 兼容复位控制器配合。复位标识遵循 `RPI_PICO_RESETS_RESET_<PERIPHERAL>` 格式，其中 `<PERIPHERAL>` 为 RP2040 外设名称，例如 `RPI_PICO_RESETS_RESET_UART0` 复位 UART0。每个标识是该外设在 RP2040 RESETS 寄存器中的位位置（Bit Position）。将这些标识直接传入 `resets` 属性。

```c
#include <zephyr/dt-bindings/reset/rp2040_reset.h>

&uart0 {
        // ...
        resets = <&reset RPI_PICO_RESETS_RESET_UART0>;
        // ...
};
```

<a id="header-files"></a>
<a id="files"></a>

## 118.1\_文件（Files）

<a id="r_rp2040_5Freset_2Eh"></a>

```c
file rp2040_reset.h
```

相关声明：[rp2040_reset.h](../api_file_reference/P358_zephyr__dt-bindings__reset__rp2040_reset.h_文件参考.md)。

Raspberry Pi RP2040的外设复位标识符（Peripheral Reset Identifiers）。


## 118.2\_原页交叉引用（Cross References）

- [rp2040_reset.h](../api_file_reference/P358_zephyr__dt-bindings__reset__rp2040_reset.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P117_Nuvoton NuMaker M55M1X 复位控制器辅助工具（Reset controller helpers）.md) · [返回大纲](大纲.md) · [下一章](P119_Raspberry Pi RP2350复位控制器辅助定义.md)
