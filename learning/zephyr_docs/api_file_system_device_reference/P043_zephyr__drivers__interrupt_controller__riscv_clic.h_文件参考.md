---
id: learning.zephyr-docs.api-file-system-device-reference.page-43
title: zephyr__drivers__interrupt_controller__riscv_clic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_clic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__clic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内核本地中断控制器（Core-Local Interrupt Controller，CLIC）的驱动。

查看此文件的源码。

<a id="details"></a>

内核本地中断控制器（Core-Local Interrupt Controller，CLIC）的驱动。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.1\_函数（Functions）

<a id="r_a97a6fb5c16f1542d7c3010212a5efa05"></a>

```c
void riscv_clic_irq_enable (uint32_t irq)
```

相关声明：[riscv_clic_irq_enable](#a97a6fb5c16f1542d7c3010212a5efa05)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用中断（interrupt）。

<a id="r_ac46870266793fabffd76b29c06834b35"></a>

```c
void riscv_clic_irq_disable (uint32_t irq)
```

相关声明：[riscv_clic_irq_disable](#ac46870266793fabffd76b29c06834b35)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用中断。

<a id="r_aabf4e38a154115fb4ee112b0c04af71f"></a>

```c
int riscv_clic_irq_is_enabled (uint32_t irq)
```

相关声明：[riscv_clic_irq_is_enabled](#aabf4e38a154115fb4ee112b0c04af71f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查中断是否已启用。

<a id="r_a58034939d55cac9197e0494ef40f0276"></a>

```c
void riscv_clic_irq_priority_set (uint32_t irq, uint32_t prio, uint32_t flags)
```

相关声明：[riscv_clic_irq_priority_set](#a58034939d55cac9197e0494ef40f0276)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置中断优先级（priority）。

<a id="r_aefcfc1008aba2e0f98f24b26113b776e"></a>

```c
void riscv_clic_irq_vector_set (uint32_t irq)
```

相关声明：[riscv_clic_irq_vector_set](#aefcfc1008aba2e0f98f24b26113b776e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置中断的向量模式（vector mode）。

## 43.2\_详细说明（Detailed Documentation）

<a id="ac46870266793fabffd76b29c06834b35"></a>

### `riscv_clic_irq_disable()`

```c
void riscv_clic_irq_disable ( uint32_t irq)
```

禁用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="a97a6fb5c16f1542d7c3010212a5efa05"></a>

### `riscv_clic_irq_enable()`

```c
void riscv_clic_irq_enable ( uint32_t irq)
```

启用中断（interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="aabf4e38a154115fb4ee112b0c04af71f"></a>

### `riscv_clic_irq_is_enabled()`

```c
int riscv_clic_irq_is_enabled ( uint32_t irq)
```

检查中断是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

**返回（Returns）**：返回值：中断已启用时返回 true，否则返回 false。

<a id="a58034939d55cac9197e0494ef40f0276"></a>

### `riscv_clic_irq_priority_set()`

```c
void riscv_clic_irq_priority_set ( uint32_t irq, uint32_t prio, uint32_t flags )
```

设置中断优先级（priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |
| `prio` | 中断优先级。 |
| `flags` | 中断标志（interrupt flags）。 |

<a id="aefcfc1008aba2e0f98f24b26113b776e"></a>

### `riscv_clic_irq_vector_set()`

```c
void riscv_clic_irq_vector_set ( uint32_t irq)
```

设置中断的向量模式（vector mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |


## 43.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P718_riscv_clic.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P042_zephyr__dt-bindings__gpio__renesas-rx-gpio-ioport.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__dt-bindings__sensor__sensor_axis_align.h_文件参考.md)
