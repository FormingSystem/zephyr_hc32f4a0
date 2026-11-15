---
id: learning.zephyr-docs.api-file-signal-device-reference.page-15
title: zephyr__drivers__interrupt_controller__nxp_pint.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_nxp\_pint.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__pint_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <fsl_pint.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.1\_类型定义（Typedefs）

<a id="r_a5ceee20d9c423fe9f80e1d72540b4c73"></a>

```c
typedef void(* nxp_pint_cb_t) (uint8_t pin, void *user)
```

相关声明：[nxp_pint_cb_t](#a5ceee20d9c423fe9f80e1d72540b4c73)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.2\_枚举（Enumerations）

<a id="r_aea62e6522d0de4c0ce63ae04b2d36f7c"></a>

```c
enum nxp_pint_trigger { NXP_PINT_NONE = kPINT_PinIntEnableNone , NXP_PINT_RISING = kPINT_PinIntEnableRiseEdge , NXP_PINT_FALLING = kPINT_PinIntEnableFallEdge , NXP_PINT_BOTH = kPINT_PinIntEnableBothEdges , NXP_PINT_LOW = kPINT_PinIntEnableLowLevel , NXP_PINT_HIGH = kPINT_PinIntEnableHighLevel }
```

相关声明：[nxp_pint_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c)、[NXP_PINT_NONE](#aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5)、[NXP_PINT_RISING](#aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40)、[NXP_PINT_FALLING](#aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e)、[NXP_PINT_BOTH](#aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2)、[NXP_PINT_LOW](#aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7)、[NXP_PINT_HIGH](#aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24)。

NXP 微控制器（MCU）中的引脚中断与模式匹配引擎（Pin Interrupt and Pattern Match Engine，PINT）驱动。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_abdfe420166b4d28fd7be112b561228bc"></a>

```c
int nxp_pint_pin_enable (uint8_t pin, enum nxp_pint_trigger trigger, bool wake)
```

相关声明：[nxp_pint_pin_enable](#abdfe420166b4d28fd7be112b561228bc)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nxp_pint_trigger](#aea62e6522d0de4c0ce63ae04b2d36f7c)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使能 PINT 中断源（Interrupt Source）。

<a id="r_a45daffb706e6e51fb805d1bfbd1c4144"></a>

```c
void nxp_pint_pin_disable (uint8_t pin)
```

相关声明：[nxp_pint_pin_disable](#a45daffb706e6e51fb805d1bfbd1c4144)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用 PINT 中断源（Interrupt Source）。

<a id="r_a086336be48bc780034f74dbd5aff0bd9"></a>

```c
int nxp_pint_pin_set_callback (uint8_t pin, nxp_pint_cb_t cb, void *data)
```

相关声明：[nxp_pint_pin_set_callback](#a086336be48bc780034f74dbd5aff0bd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nxp_pint_cb_t](#a5ceee20d9c423fe9f80e1d72540b4c73)。

安装 PINT 回调函数（Callback）。

<a id="r_ad7ec8dddcc5a404f38d8d5bb16775a9a"></a>

```c
void nxp_pint_pin_unset_callback (uint8_t pin)
```

相关声明：[nxp_pint_pin_unset_callback](#ad7ec8dddcc5a404f38d8d5bb16775a9a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除 PINT 回调函数（Callback）。

<a id="r_aaa54294fced53ad82eefe02f8c4250e2"></a>

```c
int nxp_pint_pin_get_slot_index (uint8_t pin)
```

相关声明：[nxp_pint_pin_get_slot_index](#aaa54294fced53ad82eefe02f8c4250e2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取分配给该引脚的 PINT 槽位索引（Slot Index）。

## 15.4\_详细说明（Detailed Documentation）

<a id="a5ceee20d9c423fe9f80e1d72540b4c73"></a>

### `nxp_pint_cb_t`

```c
typedef void(* nxp_pint_cb_t) (uint8_t pin, void *user)
```

<a id="aea62e6522d0de4c0ce63ae04b2d36f7c"></a>

### `nxp_pint_trigger`

```c
enum nxp_pint_trigger
```

NXP 微控制器（MCU）中的引脚中断与模式匹配引擎（Pin Interrupt and Pattern Match Engine，PINT）驱动。

引脚中断与模式匹配引擎（Pin Interrupt and Pattern Match Engine，PINT）可从具有该模块的 NXP 微控制器（MCU）的 GPIO 端口 0 和 1 上的任意引脚获取输入，并据此产生中断。引脚输入可以分别向嵌套向量中断控制器（NVIC）产生独立中断，也可以通过 PINT 基于布尔逻辑（Boolean Logic）的模式匹配引擎组合起来。此驱动目前仅支持 PINT 的引脚中断功能。

引脚中断源（Pin Interrupt Sources）。

可供使用的引脚中断源（Pin Interrupt Sources）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_PINT_NONE` |  |
| `NXP_PINT_RISING` |  |
| `NXP_PINT_FALLING` |  |
| `NXP_PINT_BOTH` |  |
| `NXP_PINT_LOW` |  |
| `NXP_PINT_HIGH` |  |

<a id="a45daffb706e6e51fb805d1bfbd1c4144"></a>

### `nxp_pint_pin_disable()`

```c
void nxp_pint_pin_disable ( uint8_t pin)
```

禁用 PINT 中断源（Interrupt Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 要禁用的引脚中断源（Pin Interrupt Source）。 |

<a id="abdfe420166b4d28fd7be112b561228bc"></a>

### `nxp_pint_pin_enable()`

```c
int nxp_pint_pin_enable ( uint8_t pin, enum nxp_pint_trigger trigger, bool wake )
```

使能 PINT 中断源（Interrupt Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 用作中断源的引脚，范围为 0–64，对应 GPIO0 的引脚 1 至 GPIO1 的引脚 31。译注：数值范围及起止引脚按官方原文保留。 |
| `trigger` | 一个 `nxp_pint_trigger` 触发标志（Trigger Flag）。 |
| `wake` | 指示该引脚是否应唤醒系统（Wakeup）。 |

<a id="aaa54294fced53ad82eefe02f8c4250e2"></a>

### `nxp_pint_pin_get_slot_index()`

```c
int nxp_pint_pin_get_slot_index ( uint8_t pin)
```

获取分配给该引脚的 PINT 槽位索引（Slot Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 要查询其 PINT 槽位索引（Slot Index）的引脚。 |

**返回（Returns）**：返回值：已分配的槽位索引（Slot Index）；若尚未分配，则返回 `-EINVAL`。

<a id="a086336be48bc780034f74dbd5aff0bd9"></a>

### `nxp_pint_pin_set_callback()`

```c
int nxp_pint_pin_set_callback ( uint8_t pin, nxp_pint_cb_t cb, void * data )
```

安装 PINT 回调函数（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 要为其安装回调函数（Callback）的中断源。 |
| `cb` | 要安装的回调（Callback）。 |
| `data` | 要包含在回调中的用户数据（User Data）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="ad7ec8dddcc5a404f38d8d5bb16775a9a"></a>

### `nxp_pint_pin_unset_callback()`

```c
void nxp_pint_pin_unset_callback ( uint8_t pin)
```

移除 PINT 回调函数（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 要为其移除回调函数（Callback）的中断源。 |


## 15.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_network_reference/P014_nxp_pint.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7ca8594c4bbe2858dd19a176d851a6175c5"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7ca20ed11aa9c65c91d30b169ae8a754d40"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7caf77211604686c8e8f16616b25b9ada9e"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7caabce56e3c8a6ba8801b0700bfbf52ec2"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7ca115385d1645fa1901b7ffeab07ff6ce7"></a>
<a id="aea62e6522d0de4c0ce63ae04b2d36f7cad94f208bdf7029063172c88673d28b24"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_zephyr__drivers__comparator__nrf_comp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__net__phy.h_文件参考.md)
