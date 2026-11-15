---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-30
title: zephyr__drivers__interrupt_controller__sam0_eic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_sam0\_eic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sam0__eic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 30.1\_类型定义（Typedefs）

<a id="r_a689981657e7012bca040dac40c5bf28f"></a>

```c
typedef void(* sam0_eic_callback_t) (uint32_t pins, void *data)
```

相关声明：[sam0_eic_callback_t](#a689981657e7012bca040dac40c5bf28f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 30.2\_枚举（Enumerations）

<a id="r_a679adca86ca5da9a49b88bd3110f2f34"></a>

```c
enum sam0_eic_trigger { SAM0_EIC_RISING , SAM0_EIC_FALLING , SAM0_EIC_BOTH , SAM0_EIC_HIGH , SAM0_EIC_LOW }
```

相关声明：[sam0_eic_trigger](#a679adca86ca5da9a49b88bd3110f2f34)、[SAM0_EIC_RISING](#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511)、[SAM0_EIC_FALLING](#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc)、[SAM0_EIC_BOTH](#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871)、[SAM0_EIC_HIGH](#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486)、[SAM0_EIC_LOW](#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9)。

外部中断控制器（EIC）触发条件（Trigger Condition）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 30.3\_函数（Functions）

<a id="r_a6b6009bc8a688ac395ec579d52c25359"></a>

```c
int sam0_eic_acquire (int port, int pin, enum sam0_eic_trigger trigger, bool filter, sam0_eic_callback_t cb, void *data)
```

相关声明：[sam0_eic_acquire](#a6b6009bc8a688ac395ec579d52c25359)、[sam0_eic_trigger](#a679adca86ca5da9a49b88bd3110f2f34)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sam0_eic_callback_t](#a689981657e7012bca040dac40c5bf28f)。

为指定端口和引脚组合（Port/Pin Combination）获取 EIC 中断。

<a id="r_aa6e652726d154e5cda1108aa31d60f26"></a>

```c
int sam0_eic_release (int port, int pin)
```

相关声明：[sam0_eic_release](#aa6e652726d154e5cda1108aa31d60f26)。

释放指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

<a id="r_a7a65e580827b8e0d3f788cc1aaba7ea7"></a>

```c
int sam0_eic_enable_interrupt (int port, int pin)
```

相关声明：[sam0_eic_enable_interrupt](#a7a65e580827b8e0d3f788cc1aaba7ea7)。

启用指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

<a id="r_a5019df444a31531292fbf2fe5af160ef"></a>

```c
int sam0_eic_disable_interrupt (int port, int pin)
```

相关声明：[sam0_eic_disable_interrupt](#a5019df444a31531292fbf2fe5af160ef)。

禁用指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

<a id="r_a7dd3052cd7fb8074ad0b1233ecaa5708"></a>

```c
uint32_t sam0_eic_interrupt_pending (int port)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sam0_eic_interrupt_pending](#a7dd3052cd7fb8074ad0b1233ecaa5708)。

检查端口是否有待处理（Pending）的 EIC 中断。

## 30.4\_详细说明（Detailed Documentation）

<a id="a689981657e7012bca040dac40c5bf28f"></a>

### `sam0_eic_callback_t`

```c
typedef void(* sam0_eic_callback_t) (uint32_t pins, void *data)
```

<a id="a679adca86ca5da9a49b88bd3110f2f34"></a>

### `sam0_eic_trigger`

```c
enum sam0_eic_trigger
```

外部中断控制器（EIC）触发条件（Trigger Condition）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SAM0_EIC_RISING` |  |
| `SAM0_EIC_FALLING` |  |
| `SAM0_EIC_BOTH` |  |
| `SAM0_EIC_HIGH` |  |
| `SAM0_EIC_LOW` |  |

<a id="a6b6009bc8a688ac395ec579d52c25359"></a>

### `sam0_eic_acquire()`

```c
int sam0_eic_acquire ( int port, int pin, enum sam0_eic_trigger trigger, bool filter, sam0_eic_callback_t cb, void * data )
```

为指定端口和引脚组合（Port/Pin Combination）获取 EIC 中断。

获取指定端口和引脚组合（Port/Pin Combination）的 EIC 中断；若所需线路不可用，则返回错误。每个端口只支持一个回调（Callback）；提供不同回调会更改该端口所有线路使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口索引（Port Index），如 `A=0`。 |
| `pin` | 端口中的引脚（Pin in the Port）。 |
| `trigger` | 触发条件（Trigger condition）。 |
| `filter` | 启用滤波器（Enable Filter）。 |
| `cb` | 中断回调（Interrupt Callback）。 |
| `data` | 传递给中断回调（Interrupt Callback）的参数。 |

<a id="a5019df444a31531292fbf2fe5af160ef"></a>

### `sam0_eic_disable_interrupt()`

```c
int sam0_eic_disable_interrupt ( int port, int pin )
```

禁用指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口索引（Port Index），如 `A=0`。 |
| `pin` | 端口中的引脚（Pin in the Port）。 |

<a id="a7a65e580827b8e0d3f788cc1aaba7ea7"></a>

### `sam0_eic_enable_interrupt()`

```c
int sam0_eic_enable_interrupt ( int port, int pin )
```

启用指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口索引（Port Index），如 `A=0`。 |
| `pin` | 端口中的引脚（Pin in the Port）。 |

<a id="a7dd3052cd7fb8074ad0b1233ecaa5708"></a>

### `sam0_eic_interrupt_pending()`

```c
uint32_t sam0_eic_interrupt_pending ( int port)
```

检查端口是否有待处理（Pending）的 EIC 中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口索引（Port Index），如 `A=0`。 |

<a id="aa6e652726d154e5cda1108aa31d60f26"></a>

### `sam0_eic_release()`

```c
int sam0_eic_release ( int port, int pin )
```

释放指定端口和引脚组合（Port/Pin Combination）的 EIC 中断。

释放指定端口和引脚组合（Port/Pin Combination）的 EIC 配置。若该组合当前未占用关联的 EIC 线路，则无效果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口索引（Port Index），如 `A=0`。 |
| `pin` | 端口中的引脚（Pin in the Port）。 |


## 30.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P018_sam0_eic.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511"></a>
<a id="a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc"></a>
<a id="a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871"></a>
<a id="a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486"></a>
<a id="a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P029_zephyr__drivers__interrupt_controller__riscv_aplic_direct.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__net__http__service.h_文件参考.md)
