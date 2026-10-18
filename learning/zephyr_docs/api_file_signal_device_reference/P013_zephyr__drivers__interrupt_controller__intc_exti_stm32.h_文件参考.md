---
id: learning.zephyr-docs.api-file-signal-device-reference.page-13
title: zephyr__drivers__interrupt_controller__intc_exti_stm32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_exti\_stm32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__exti__stm32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.1\_枚举（Enumerations）

<a id="r_a86d158bbfe92d326ef6ef9a623bf6b8c"></a>

```c
enum stm32_exti_trigger_type { STM32_EXTI_TRIG_NONE = 0x0 , STM32_EXTI_TRIG_RISING = 0x1 , STM32_EXTI_TRIG_FALLING = 0x2 , STM32_EXTI_TRIG_BOTH = 0x3 }
```

相关声明：[stm32_exti_trigger_type](#a86d158bbfe92d326ef6ef9a623bf6b8c)、[STM32_EXTI_TRIG_NONE](#a86d158bbfe92d326ef6ef9a623bf6b8caa44b00e6dd732140f0c152ec6a5ad0e0)、[STM32_EXTI_TRIG_RISING](#a86d158bbfe92d326ef6ef9a623bf6b8cac1ab9fda0db1fb1a852bfe358c7e6485)、[STM32_EXTI_TRIG_FALLING](#a86d158bbfe92d326ef6ef9a623bf6b8ca8a53325045c0825c5fd379d83a04f5e4)、[STM32_EXTI_TRIG_BOTH](#a86d158bbfe92d326ef6ef9a623bf6b8ca013afe4b3bfc4921f30dad835e7f87cc)。

STM32 外部中断（EXTI）控制器 API。

<a id="r_a7780746237de7f19b5a0457f83b9208f"></a>

```c
enum stm32_exti_mode { STM32_EXTI_MODE_IT = 0x0 , STM32_EXTI_MODE_EVENT = 0x1 , STM32_EXTI_MODE_BOTH = 0x2 , STM32_EXTI_MODE_NONE = 0x3 }
```

相关声明：[stm32_exti_mode](#a7780746237de7f19b5a0457f83b9208f)、[STM32_EXTI_MODE_IT](#a7780746237de7f19b5a0457f83b9208fa21e081ba1d5f8cc28758ddbd89dcf554)、[STM32_EXTI_MODE_EVENT](#a7780746237de7f19b5a0457f83b9208faabd817ddd666342876a7f45a22599f9c)、[STM32_EXTI_MODE_BOTH](#a7780746237de7f19b5a0457f83b9208fabbb2a1012aa1fea7568a33537702beb6)、[STM32_EXTI_MODE_NONE](#a7780746237de7f19b5a0457f83b9208fa1440b42239fcd4a958700da120c5de5f)。

外部中断线模式（EXTI Line Mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.2\_函数（Functions）

<a id="r_a9ed083565b9d11549c9841aee10d85fc"></a>

```c
int stm32_exti_enable (uint32_t line_num, stm32_exti_trigger_type trigger, stm32_exti_mode mode)
```

相关声明：[stm32_exti_enable](#a9ed083565b9d11549c9841aee10d85fc)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[stm32_exti_trigger_type](#a86d158bbfe92d326ef6ef9a623bf6b8c)、[stm32_exti_mode](#a7780746237de7f19b5a0457f83b9208f)。

使能外部中断线（EXTI Line）。

<a id="r_a1ca2a35dc6232df5abb6086d1a5e9264"></a>

```c
int stm32_exti_disable (uint32_t line_num)
```

相关声明：[stm32_exti_disable](#a1ca2a35dc6232df5abb6086d1a5e9264)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用外部中断线（EXTI Line）。

<a id="r_aaee82d8a7f1a4e88c507872eb6639e7b"></a>

```c
bool stm32_exti_is_pending (uint32_t line_num)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[stm32_exti_is_pending](#aaee82d8a7f1a4e88c507872eb6639e7b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查指定外部中断线（EXTI Line）的中断挂起位（Interrupt Pending Bit）。

<a id="r_a5b88085adfd3e17587b7c1f7a2c09501"></a>

```c
int stm32_exti_clear_pending (uint32_t line_num)
```

相关声明：[stm32_exti_clear_pending](#a5b88085adfd3e17587b7c1f7a2c09501)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除指定外部中断线（EXTI Line）的中断挂起位（Interrupt Pending Bit）。

<a id="r_a8ff30ebf5f3a25aa21ddc1aae8a0d96b"></a>

```c
int stm32_exti_sw_interrupt (uint32_t line_num)
```

相关声明：[stm32_exti_sw_interrupt](#a8ff30ebf5f3a25aa21ddc1aae8a0d96b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为指定编号的外部中断线（EXTI Line）生成软件中断（Software Interrupt）。

## 13.3\_详细说明（Detailed Documentation）

<a id="a7780746237de7f19b5a0457f83b9208f"></a>

### `stm32_exti_mode`

```c
enum stm32_exti_mode
```

外部中断线模式（EXTI Line Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `STM32_EXTI_MODE_IT` |  |
| `STM32_EXTI_MODE_EVENT` |  |
| `STM32_EXTI_MODE_BOTH` |  |
| `STM32_EXTI_MODE_NONE` |  |

<a id="a86d158bbfe92d326ef6ef9a623bf6b8c"></a>

### `stm32_exti_trigger_type`

```c
enum stm32_exti_trigger_type
```

STM32 外部中断（EXTI）控制器 API。

此 API 用于与 STM32 外部中断（EXTI）控制器交互。

EXTI 中断触发类型（Interrupt Trigger Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `STM32_EXTI_TRIG_NONE` |  |
| `STM32_EXTI_TRIG_RISING` |  |
| `STM32_EXTI_TRIG_FALLING` |  |
| `STM32_EXTI_TRIG_BOTH` |  |

<a id="a5b88085adfd3e17587b7c1f7a2c09501"></a>

### `stm32_exti_clear_pending()`

```c
int stm32_exti_clear_pending ( uint32_t line_num)
```

清除指定外部中断线（EXTI Line）的中断挂起位（Interrupt Pending Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line_num` | 外部中断线编号（EXTI Line Number）。 |

**返回（Returns）**：返回值：成功返回 0；若中断线无效，则返回 `-EINVAL`。

<a id="a1ca2a35dc6232df5abb6086d1a5e9264"></a>

### `stm32_exti_disable()`

```c
int stm32_exti_disable ( uint32_t line_num)
```

禁用外部中断线（EXTI Line）。

调用此函数后，外部中断线（EXTI Line）`line_num` 将不再产生中断或事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line_num` | 外部中断线编号（EXTI Line Number）。 |

**返回（Returns）**：返回值：成功返回 0；若中断线无效，则返回 `-EINVAL`。

<a id="a9ed083565b9d11549c9841aee10d85fc"></a>

### `stm32_exti_enable()`

```c
int stm32_exti_enable ( uint32_t line_num, stm32_exti_trigger_type trigger, stm32_exti_mode mode )
```

使能外部中断线（EXTI Line）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line_num` | 外部中断线编号（EXTI Line Number）。 |
| `trigger` | EXTI 触发类型（Trigger Type），参见 `stm32_exti_trigger_type`。 |
| `mode` | EXTI 模式（Mode），参见 `stm32_exti_mode`。 |

**说明（Note）**：注意：选择 `MODE_IT` 时，调用此 API 的驱动负责注册中断服务例程（ISR）并使能相应中断。

**返回（Returns）**：返回值：成功返回 0；若 `line_num` 无效，则返回 `-EINVAL`。

<a id="aaee82d8a7f1a4e88c507872eb6639e7b"></a>

### `stm32_exti_is_pending()`

```c
bool stm32_exti_is_pending ( uint32_t line_num)
```

检查指定外部中断线（EXTI Line）的中断挂起位（Interrupt Pending Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line_num` | 外部中断线编号（EXTI Line Number）。 |

**返回（Returns）**：返回值：中断线处于挂起状态（Pending）时返回 `true`，否则返回 `false`。

<a id="a8ff30ebf5f3a25aa21ddc1aae8a0d96b"></a>

### `stm32_exti_sw_interrupt()`

```c
int stm32_exti_sw_interrupt ( uint32_t line_num)
```

为指定编号的外部中断线（EXTI Line）生成软件中断（Software Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `line_num` | 外部中断线编号（EXTI Line Number）。 |

**返回（Returns）**：返回值：成功返回 0；若中断线无效，则返回 `-EINVAL`。


## 13.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P015_intc_exti_stm32.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a7780746237de7f19b5a0457f83b9208fa21e081ba1d5f8cc28758ddbd89dcf554"></a>
<a id="a7780746237de7f19b5a0457f83b9208faabd817ddd666342876a7f45a22599f9c"></a>
<a id="a7780746237de7f19b5a0457f83b9208fabbb2a1012aa1fea7568a33537702beb6"></a>
<a id="a7780746237de7f19b5a0457f83b9208fa1440b42239fcd4a958700da120c5de5f"></a>
<a id="a86d158bbfe92d326ef6ef9a623bf6b8caa44b00e6dd732140f0c152ec6a5ad0e0"></a>
<a id="a86d158bbfe92d326ef6ef9a623bf6b8cac1ab9fda0db1fb1a852bfe358c7e6485"></a>
<a id="a86d158bbfe92d326ef6ef9a623bf6b8ca8a53325045c0825c5fd379d83a04f5e4"></a>
<a id="a86d158bbfe92d326ef6ef9a623bf6b8ca013afe4b3bfc4921f30dad835e7f87cc"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_zephyr__drivers__interrupt_controller__intc_bcm283x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__comparator__nrf_comp.h_文件参考.md)
