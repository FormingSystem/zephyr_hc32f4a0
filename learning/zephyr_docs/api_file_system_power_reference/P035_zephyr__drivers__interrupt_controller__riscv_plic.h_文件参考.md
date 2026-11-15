---
id: learning.zephyr-docs.api-file-system-power-reference.page-35
title: zephyr__drivers__interrupt_controller__riscv_plic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_plic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__plic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

平台级中断控制器（Platform Level Interrupt Controller，PLIC）的驱动。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

平台级中断控制器（Platform Level Interrupt Controller，PLIC）的驱动。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.1\_函数（Functions）

<a id="r_af7070f20dd4c29eee03f69d7795cced2"></a>

```c
void riscv_plic_irq_complete (uint32_t irq)
```

相关声明：[riscv_plic_irq_complete](#af7070f20dd4c29eee03f69d7795cced2)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将中断标记为已完成（Completed）。

<a id="r_aa2f97f63d37ae4fc381d79bdf78a274d"></a>

```c
void riscv_plic_irq_enable (uint32_t irq)
```

相关声明：[riscv_plic_irq_enable](#aa2f97f63d37ae4fc381d79bdf78a274d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用中断（interrupt）。

<a id="r_a69dafac67e153be3be5f209050bd27ad"></a>

```c
void riscv_plic_irq_disable (uint32_t irq)
```

相关声明：[riscv_plic_irq_disable](#a69dafac67e153be3be5f209050bd27ad)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用中断。

<a id="r_aa6aaaff9f5af0f4acbbea187f13a5e6b"></a>

```c
int riscv_plic_irq_is_enabled (uint32_t irq)
```

相关声明：[riscv_plic_irq_is_enabled](#aa6aaaff9f5af0f4acbbea187f13a5e6b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查中断是否已启用。

<a id="r_aa73cba0daaafa6dc0d1b54abbbc5172a"></a>

```c
void riscv_plic_set_priority (uint32_t irq, uint32_t prio)
```

相关声明：[riscv_plic_set_priority](#aa73cba0daaafa6dc0d1b54abbbc5172a)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置中断优先级（priority）。

<a id="r_a2fe43faade1720a6046550e1175d6351"></a>

```c
int riscv_plic_irq_set_affinity (uint32_t irq, uint32_t cpumask)
```

相关声明：[riscv_plic_irq_set_affinity](#a2fe43faade1720a6046550e1175d6351)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 IRQ 亲和性（Affinity）。

<a id="r_aedeb9961a5d9d85e7084250cd31ca99f"></a>

```c
void riscv_plic_irq_set_pending (uint32_t irq)
```

相关声明：[riscv_plic_irq_set_pending](#aedeb9961a5d9d85e7084250cd31ca99f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将中断设为待处理状态（Pending）。

<a id="r_a1208afc18002e5c1d2539958a0331647"></a>

```c
unsigned int riscv_plic_get_irq (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[riscv_plic_get_irq](#a1208afc18002e5c1d2539958a0331647)。

获取活动中断 ID（Active Interrupt ID）。

<a id="r_a94ba6fdef8d90dae8b184f902519d248"></a>

```c
const struct device * riscv_plic_get_dev (void)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[riscv_plic_get_dev](#a94ba6fdef8d90dae8b184f902519d248)。

获取活动中断控制器设备（Active Interrupt Controller Device）。

## 35.2\_详细说明（Detailed Documentation）

<a id="a94ba6fdef8d90dae8b184f902519d248"></a>

### `riscv_plic_get_dev()`

```c
const struct device * riscv_plic_get_dev ( void )
```

获取活动中断控制器设备（Active Interrupt Controller Device）。

**说明（Note）**：**注意（Note）：**应在中断已锁定（Interrupt Locked）的情况下调用。

**返回（Returns）**：**返回值（Returns）：**活动中断设备（Active Interrupt Device）的设备指针。

<a id="a1208afc18002e5c1d2539958a0331647"></a>

### `riscv_plic_get_irq()`

```c
unsigned int riscv_plic_get_irq ( void )
```

获取活动中断 ID（Active Interrupt ID）。

**说明（Note）**：**注意（Note）：**应在中断已锁定（Interrupt Locked）的情况下调用。

**返回（Returns）**：**返回值（Returns）：**活动中断（Active Interrupt）的 ID。

<a id="af7070f20dd4c29eee03f69d7795cced2"></a>

### `riscv_plic_irq_complete()`

```c
void riscv_plic_irq_complete ( uint32_t irq)
```

将中断标记为已完成（Completed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 要声明为已完成（Completed）的 IRQ 编号。 |

<a id="a69dafac67e153be3be5f209050bd27ad"></a>

### `riscv_plic_irq_disable()`

```c
void riscv_plic_irq_disable ( uint32_t irq)
```

禁用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="aa2f97f63d37ae4fc381d79bdf78a274d"></a>

### `riscv_plic_irq_enable()`

```c
void riscv_plic_irq_enable ( uint32_t irq)
```

启用中断（interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="aa6aaaff9f5af0f4acbbea187f13a5e6b"></a>

### `riscv_plic_irq_is_enabled()`

```c
int riscv_plic_irq_is_enabled ( uint32_t irq)
```

检查中断是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

**返回（Returns）**：返回值：中断已启用时返回 true，否则返回 false。

<a id="a2fe43faade1720a6046550e1175d6351"></a>

### `riscv_plic_irq_set_affinity()`

```c
int riscv_plic_irq_set_affinity ( uint32_t irq, uint32_t cpumask )
```

设置 IRQ 亲和性（Affinity）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | IRQ 线路。 |
| `cpumask` | CPU 位掩码（Bit Mask）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，否则返回负 `errno`。

<a id="aedeb9961a5d9d85e7084250cd31ca99f"></a>

### `riscv_plic_irq_set_pending()`

```c
void riscv_plic_irq_set_pending ( uint32_t irq)
```

将中断设为待处理状态（Pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="aa73cba0daaafa6dc0d1b54abbbc5172a"></a>

### `riscv_plic_set_priority()`

```c
void riscv_plic_set_priority ( uint32_t irq, uint32_t prio )
```

设置中断优先级（priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |
| `prio` | 中断优先级。 |


## 35.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P719_riscv_plic.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P034_zephyr__posix__sys__eventfd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__arch__common__semihost.h_文件参考.md)
