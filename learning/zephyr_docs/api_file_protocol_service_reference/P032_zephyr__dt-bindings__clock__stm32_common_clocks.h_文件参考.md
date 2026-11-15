---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-32
title: zephyr__dt-bindings__clock__stm32_common_clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_dt-bindings\_\_clock\_\_stm32\_common\_clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__common__clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="r_a79a13b49235b90035b5ed7f62c9bf9bf"></a>

```c
#define STM32_SRC_SYSCLK 0x001
```

相关声明：[STM32_SRC_SYSCLK](#a79a13b49235b90035b5ed7f62c9bf9bf)。

使用系统时钟（System Clock）作为源时钟（Source Clock）的 ID。

<a id="r_a42412accdd52b7ef9460583db634a4b1"></a>

```c
#define STM32_SRC_LSE 0x002
```

相关声明：[STM32_SRC_LSE](#a42412accdd52b7ef9460583db634a4b1)。

使用低速外部时钟（LSE）作为源时钟（Source Clock）的 ID。

<a id="r_ac6233dbbaff45f6862b21debbf180640"></a>

```c
#define STM32_SRC_LSI 0x003
```

相关声明：[STM32_SRC_LSI](#ac6233dbbaff45f6862b21debbf180640)。

使用低速内部时钟（LSI）作为源时钟（Source Clock）的 ID。

<a id="r_ae998967c5f8ed059e757a6906b46ed4e"></a>

```c
#define NO_SEL 0xFF
```

相关声明：[NO_SEL](#ae998967c5f8ed059e757a6906b46ed4e)。

占位（Dummy）：没有可选项时添加说明符（Specifier）。

<a id="r_a49981976097d7e684ac5e5e094ecdf9b"></a>

```c
#define STM32_CLOCK_DIV(div)
```

相关声明：[STM32_CLOCK_DIV](#a49981976097d7e684ac5e5e094ecdf9b)。

时钟分频器（Clock divider）。

<a id="r_a7ed7d3d8d30b4f029a3df34ab7b49089"></a>

```c
#define STM32_DT_CLOCK_SELECT(val, msb, lsb, reg)
```

相关声明：[STM32_DT_CLOCK_SELECT](#a7ed7d3d8d30b4f029a3df34ab7b49089)。

为设备树（DT）打包 STM32 源时钟选择所需的 RCC 寄存器位域（Register Bit Fields）。

<a id="r_a0fec36253cbc233df3b564feb5d873a4"></a>

```c
#define STM32_CLOCK(bus, bit)
```

相关声明：[STM32_CLOCK](#a0fec36253cbc233df3b564feb5d873a4)。

将 RCC 时钟寄存器偏移量（Register Offset）和位（Bit）打包为两个 32 位值，符合 STM32 设备树 `clocks` 属性的格式。

## 32.2\_详细说明（Detailed Documentation）

<a id="ae998967c5f8ed059e757a6906b46ed4e"></a>

### `NO_SEL`

```c
#define NO_SEL 0xFF
```

占位（Dummy）：没有可选项时添加说明符（Specifier）。

<a id="a0fec36253cbc233df3b564feb5d873a4"></a>

### `STM32_CLOCK`

```c
#define STM32_CLOCK ( bus, bit )
```

展开值（Value）：

```c
(STM32_CLOCK_BUS_##bus) (1 << bit)
```

将 RCC 时钟寄存器偏移量（Register Offset）和位（Bit）打包为两个 32 位值，符合 STM32 设备树 `clocks` 属性的格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus` | STM32 总线名称（Bus Name），展开为 `STM32_CLOCK_BUS_{bus}`。 |
| `bit` | 时钟位（Clock Bit）。 |

<a id="a49981976097d7e684ac5e5e094ecdf9b"></a>

### `STM32_CLOCK_DIV`

```c
#define STM32_CLOCK_DIV ( div)
```

展开值（Value）：

```c
(((div) - 1) << STM32_CLOCK_DIV_SHIFT)
```

时钟分频器（Clock divider）。

<a id="a7ed7d3d8d30b4f029a3df34ab7b49089"></a>

### `STM32_DT_CLOCK_SELECT`

```c
#define STM32_DT_CLOCK_SELECT ( val, msb, lsb, reg )
```

展开值（Value）：

```c
((((reg) & STM32_DT_CLKSEL_REG_MASK) << STM32_DT_CLKSEL_REG_SHIFT) |                    \
 (((lsb) & STM32_DT_CLKSEL_SHIFT_MASK) << STM32_DT_CLKSEL_SHIFT_SHIFT) |                \
 ((((msb) - (lsb)) & STM32_DT_CLKSEL_WIDTH_MASK) << STM32_DT_CLKSEL_WIDTH_SHIFT) |      \
 (((val) & STM32_DT_CLKSEL_VAL_MASK) << STM32_DT_CLKSEL_VAL_SHIFT))
```

为设备树（DT）打包 STM32 源时钟选择所需的 RCC 寄存器位域（Register Bit Fields）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 时钟配置字段值（Clock Configuration Field Value）。 |
| `msb` | 字段最高有效位（MSB）的索引。 |
| `lsb` | 字段最低有效位（LSB）的索引。 |
| `reg` | RCC 中目标时钟配置寄存器（Clock Configuration Register）的偏移量。 |

**说明（Note）**：**注意（Note）：**内部数据布局如下：`reg` 范围 `0x0–0xFFFF`，位 `[00:15]`；`shift` 范围 `0–31`，位 `[16:20]`；`width` 范围 `0–7`，位 `[21:23]`，其值编码位域宽度减 `1`；`val` 范围 `0x00–0xFF`，位 `[24:31]`。

<a id="a42412accdd52b7ef9460583db634a4b1"></a>

### `STM32_SRC_LSE`

```c
#define STM32_SRC_LSE 0x002
```

使用低速外部时钟（LSE）作为源时钟（Source Clock）的 ID。

<a id="ac6233dbbaff45f6862b21debbf180640"></a>

### `STM32_SRC_LSI`

```c
#define STM32_SRC_LSI 0x003
```

使用低速内部时钟（LSI）作为源时钟（Source Clock）的 ID。

<a id="a79a13b49235b90035b5ed7f62c9bf9bf"></a>

### `STM32_SRC_SYSCLK`

```c
#define STM32_SRC_SYSCLK 0x001
```

使用系统时钟（System Clock）作为源时钟（Source Clock）的 ID。


## 32.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P830_stm32_common_clocks.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P031_zephyr__net__http__service.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_capture.h_文件参考.md)
