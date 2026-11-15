---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-22
title: zephyr__drivers__interrupt_controller__intc_renesas_rx_grp_int.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_renesas\_rx\_grp\_int.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX分组中断控制器（Group Interrupt Controller）的头文件。

<a id="details"></a>

```c
#include "platform.h"
```

查看此文件的源码。

Renesas RX分组中断控制器（Group Interrupt Controller）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.1\_函数（Functions）

<a id="r_ae526fa393cc27cfe87467667dff111d6"></a>

```c
int rx_grp_intc_set_grp_int (const struct device *dev, bsp_int_src_t vector, bool set)
```

相关声明：[rx_grp_intc_set_grp_int](#ae526fa393cc27cfe87467667dff111d6)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为给定中断向量（Interrupt Vector）启用或禁用组中断（Group Interrupt）。

<a id="r_a8a63db97f47dd788a268a9651d43347f"></a>

```c
int rx_grp_intc_set_gen (const struct device *dev, uint8_t vector_num, bool set)
```

相关声明：[rx_grp_intc_set_gen](#a8a63db97f47dd788a268a9651d43347f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过设置或清除组中断寄存器中对应的位（`vector_num`），启用或禁用指定组中断源（Group Interrupt Source）。

<a id="r_a349020f5fe0ecc410821be66f87367b7"></a>

```c
int rx_grp_intc_set_callback (const struct device *dev, bsp_int_src_t vector, bsp_int_cb_t callback, void *context)
```

相关声明：[rx_grp_intc_set_callback](#a349020f5fe0ecc410821be66f87367b7)、[device](../device_reference/P002_设备对象结构.md)。

为指定组中断源，即向量（Vector），注册回调函数。

## 22.2\_详细说明（Detailed Documentation）

<a id="a349020f5fe0ecc410821be66f87367b7"></a>

### `rx_grp_intc_set_callback()`

```c
int rx_grp_intc_set_callback ( const struct device * dev, bsp_int_src_t vector, bsp_int_cb_t callback, void * context )
```

为指定组中断源，即向量（Vector），注册回调函数。

触发中断时，使用关联的上下文（Context）执行给定回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RX 组中断设备（Group Interrupt Device）。 |
| `vector` | 要附加回调的中断源（Interrupt Source）。 |
| `callback` | 发生中断时调用的函数（Function）。 |
| `context` | 指向传递给回调的用户定义数据（User-defined Data）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 回调注册（Callback Registration）失败时。 |

<a id="a8a63db97f47dd788a268a9651d43347f"></a>

### `rx_grp_intc_set_gen()`

```c
int rx_grp_intc_set_gen ( const struct device * dev, uint8_t vector_num, bool set )
```

通过设置或清除组中断寄存器中对应的位（`vector_num`），启用或禁用指定组中断源（Group Interrupt Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RX 组中断设备（Group Interrupt Device）。 |
| `vector_num` | 组内中断源索引（Interrupt Source Index），范围 `0–31`。 |
| `set` | 表示启用或禁用的布尔值（Boolean）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 中断控制操作（Interrupt Control Operation）失败时。 |

<a id="ae526fa393cc27cfe87467667dff111d6"></a>

### `rx_grp_intc_set_grp_int()`

```c
int rx_grp_intc_set_grp_int ( const struct device * dev, bsp_int_src_t vector, bool set )
```

为给定中断向量（Interrupt Vector）启用或禁用组中断（Group Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RX 组中断设备（Group Interrupt Device）。 |
| `vector` | 要控制的中断向量（Interrupt Vector），类型为 `bsp_int_src_t`。 |
| `set` | 表示启用或禁用的布尔值（Boolean）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 中断控制操作（Interrupt Control Operation）失败时。 |


## 22.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P399_intc_renesas_rx_grp_int.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_zephyr__net__ieee802154_ie.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__irq_nextlevel.h_文件参考.md)
