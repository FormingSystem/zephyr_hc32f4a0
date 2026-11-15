---
id: learning.zephyr-docs.api-protocol-topic-reference.page-56
title: CH32复位控制器辅助定义（Reset Controller Helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__ch32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_CH32复位控制器辅助定义（Reset Controller Helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__ch32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于编码CH32外设复位说明单元（Reset Cells）的宏。

<a id="details"></a>

用于编码 CH32 外设复位单元（peripheral reset cells）的宏。此设备树宏用于编码 CH32 设备的外设复位，供兼容 `wch,ch32-rcc-rctl` 的复位控制器使用。各 SoC 系列头文件（例如 `ch32v20x_30x-reset.h`）均将该系列的 RCC 总线复位寄存器偏移量定义为 `CH32_RESET_BUS_<bus>` 常量。随后使用 `CH32_RESET()`，将总线常量与外设复位线在该总线复位寄存器中的位位置组合，编码成外设复位单元。下方保留原始配置示例。

```c
#include <zephyr/dt-bindings/reset/ch32v20x_30x-reset.h>

&usart1 {
        resets = <&rctl CH32_RESET(APB2, 14)>;
}
```

<a id="header-files"></a>
<a id="files"></a>

## 56.1\_文件（Files）

<a id="r_ch32-common_2Eh"></a>

```c
file ch32-common.h
```

相关声明：[ch32-common.h](../api_file_supplement_reference/P014_zephyr__dt-bindings__reset__ch32-common.h_文件参考.md)。

CH32复位控制器的设备树通用辅助宏（Reset Controller Devicetree Common Helper Macros）。

<a id="r_ch32v00x-reset_2Eh"></a>

```c
file ch32v00x-reset.h
```

相关声明：[ch32v00x-reset.h](../api_file_reference/P039_zephyr__dt-bindings__reset__ch32v00x-reset.h_文件参考.md)。

CH32V00X的CH32复位控制器设备树辅助宏（Reset Controller Devicetree Helper Macros）。

<a id="r_ch32v20x_5F30x-reset_2Eh"></a>

```c
file ch32v20x_30x-reset.h
```

相关声明：[ch32v20x_30x-reset.h](../api_file_reference/P041_zephyr__dt-bindings__reset__ch32v20x_30x-reset.h_文件参考.md)。

CH32V20X-V30X的CH32复位控制器设备树辅助宏（Reset Controller Devicetree Helper Macros）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 56.2\_宏定义（Macros）

<a id="r_gacc21ffdc9d8b6dc6b20daaf48cda91cc"></a>

```c
#define CH32_RESET(bus, bit)
```

相关声明：[CH32_RESET](#gacc21ffdc9d8b6dc6b20daaf48cda91cc)。

为 `wch,ch32-rcc-rctl` 绑定编码外设复位单元值（Peripheral Reset Cell Value）。

## 56.3\_详细说明（Detailed Documentation）

<a id="gacc21ffdc9d8b6dc6b20daaf48cda91cc"></a>

### `CH32_RESET`

```c
#define CH32_RESET ( bus, bit )
```

```c
#include <zephyr/dt-bindings/reset/ch32-common.h>
```

展开值（Value）：

```c
(((CH32_RESET_BUS_##bus) << 5U) | (bit))
```

为 `wch,ch32-rcc-rctl` 绑定编码外设复位单元值（Peripheral Reset Cell Value）。

将 RCC 总线寄存器偏移量及位位置打包为一个 32 位复位单元值（reset cell value）。

位 `[4:0]` 保存复位位在 32 位 RCC 总线寄存器中的位置；位 `[16:5]` 保存 RCC 寄存器相对于 RCC 基地址的字节偏移量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | RCC 总线名称（bus name）。 |
| `bit` | 外设复位线在总线复位寄存器中的位位置。 |


## 56.4\_原页交叉引用（Cross References）

- [ch32-common.h](../api_file_supplement_reference/P014_zephyr__dt-bindings__reset__ch32-common.h_文件参考.md)
- [ch32v00x-reset.h](../api_file_reference/P039_zephyr__dt-bindings__reset__ch32v00x-reset.h_文件参考.md)
- [ch32v20x_30x-reset.h](../api_file_reference/P041_zephyr__dt-bindings__reset__ch32v20x_30x-reset.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P055_PTP 时间.md) · [返回大纲](大纲.md) · [下一章](P057_STM32复位控制器辅助定义.md)
