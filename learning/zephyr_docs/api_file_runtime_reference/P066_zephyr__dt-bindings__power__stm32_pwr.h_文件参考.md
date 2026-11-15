---
id: learning.zephyr-docs.api-file-runtime-reference.page-66
title: zephyr__dt-bindings__power__stm32_pwr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__pwr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_zephyr\_\_dt-bindings\_\_power\_\_stm32\_pwr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__pwr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 66.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 唤醒引脚源标志（Wake-Up Pin Source Flags）

STM32 电源控制器（Power Controller）。

<a id="r_adf19445e60cddb3648576b0d00286037"></a>

```c
#define STM32_PWR_WKUP_PIN_NOT_MUXED STM32_PWR_WKUP_EVT_SRC_0
```

相关声明：[STM32_PWR_WKUP_PIN_NOT_MUXED](#adf19445e60cddb3648576b0d00286037)、[STM32_PWR_WKUP_EVT_SRC_0](#ae42d060e1acd34b67f6abafd1c3beb0c)。

<a id="r_ae42d060e1acd34b67f6abafd1c3beb0c"></a>

```c
#define STM32_PWR_WKUP_EVT_SRC_0 0
```

相关声明：[STM32_PWR_WKUP_EVT_SRC_0](#ae42d060e1acd34b67f6abafd1c3beb0c)。

<a id="r_afe3257abb473831116e1a4de37967643"></a>

```c
#define STM32_PWR_WKUP_EVT_SRC_1 1
```

相关声明：[STM32_PWR_WKUP_EVT_SRC_1](#afe3257abb473831116e1a4de37967643)。

<a id="r_ab8da300a49d90c217e7ca5636f728579"></a>

```c
#define STM32_PWR_WKUP_EVT_SRC_2 2
```

相关声明：[STM32_PWR_WKUP_EVT_SRC_2](#ab8da300a49d90c217e7ca5636f728579)。

<a id="r_a29a7331dcd38fbaf1b96dfafc4f5f94f"></a>

```c
#define STM32_PWR_WKUP_LINE_SRC_MASK (0x3)
```

相关声明：[STM32_PWR_WKUP_LINE_SRC_MASK](#a29a7331dcd38fbaf1b96dfafc4f5f94f)。

STM32 唤醒线源选择位掩码（Wake-Up Line Source Selection Bitmask）。

## 66.2\_详细说明（Detailed Documentation）

<a id="ae42d060e1acd34b67f6abafd1c3beb0c"></a>

### `STM32_PWR_WKUP_EVT_SRC_0`

```c
#define STM32_PWR_WKUP_EVT_SRC_0 0
```

<a id="afe3257abb473831116e1a4de37967643"></a>

### `STM32_PWR_WKUP_EVT_SRC_1`

```c
#define STM32_PWR_WKUP_EVT_SRC_1 1
```

<a id="ab8da300a49d90c217e7ca5636f728579"></a>

### `STM32_PWR_WKUP_EVT_SRC_2`

```c
#define STM32_PWR_WKUP_EVT_SRC_2 2
```

<a id="a29a7331dcd38fbaf1b96dfafc4f5f94f"></a>

### `STM32_PWR_WKUP_LINE_SRC_MASK`

```c
#define STM32_PWR_WKUP_LINE_SRC_MASK (0x3)
```

STM32 唤醒线源选择位掩码（Wake-Up Line Source Selection Bitmask）。

**说明（Note）**：注意（Note）：目前最多支持四个源（Sources），编号为 0～3。

<a id="adf19445e60cddb3648576b0d00286037"></a>

### `STM32_PWR_WKUP_PIN_NOT_MUXED`

```c
#define STM32_PWR_WKUP_PIN_NOT_MUXED STM32_PWR_WKUP_EVT_SRC_0
```


## 66.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P190_stm32_pwr.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P065_zephyr__drivers__stepper__stepper_tmcm3216.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P067_zephyr__dt-bindings__power__stm32h5_iocell.h_文件参考.md)
