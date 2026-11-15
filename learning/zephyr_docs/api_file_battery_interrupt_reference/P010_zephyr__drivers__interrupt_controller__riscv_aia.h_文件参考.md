---
id: learning.zephyr-docs.api-file-battery-interrupt-reference.page-10
title: zephyr__drivers__interrupt_controller__riscv_aia.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_aia.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RISC-V高级中断架构（Advanced Interrupt Architecture，AIA）的统一协调器API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/drivers/interrupt_controller/riscv_aplic.h>
#include <zephyr/drivers/interrupt_controller/riscv_imsic.h>
```

查看此文件的源码。

RISC-V 高级中断架构（Advanced Interrupt Architecture，AIA）的统一协调器 API。该协调器为 Zephyr 的中断管理提供封装 APLIC 和 IMSIC 的统一 API，并作为类似 PLIC 的二级中断控制器（Second-level Interrupt Controller）暴露给 Zephyr；APLIC 和 IMSIC 保留为内部实现细节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.1\_函数（Functions）

<a id="r_abf2922519b5ec25a57ded7544c2a401c"></a>

```c
void riscv_aia_irq_enable (uint32_t irq)
```

相关声明：[riscv_aia_irq_enable](#abf2922519b5ec25a57ded7544c2a401c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用 AIA 中断源（Interrupt Source）。

<a id="r_a3598cc5edfbd910b8cb01ffc76c8a17f"></a>

```c
void riscv_aia_irq_disable (uint32_t irq)
```

相关声明：[riscv_aia_irq_disable](#a3598cc5edfbd910b8cb01ffc76c8a17f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用 AIA 中断源（Interrupt Source）。

<a id="r_ac1c545848a8101e24b515a25ba76f65d"></a>

```c
int riscv_aia_irq_is_enabled (uint32_t irq)
```

相关声明：[riscv_aia_irq_is_enabled](#ac1c545848a8101e24b515a25ba76f65d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查 AIA 中断源（Interrupt Source）是否已启用。

<a id="r_a6d06861210dacb74fece7b13699b7327"></a>

```c
void riscv_aia_set_priority (uint32_t irq, uint32_t prio)
```

相关声明：[riscv_aia_set_priority](#a6d06861210dacb74fece7b13699b7327)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 AIA 中断源的优先级（Priority）。

<a id="r_a05cb2cf3fbed778d8fb0f535486155ac"></a>

```c
static const struct device * riscv_aia_get_dev (void)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[riscv_aia_get_dev](#a05cb2cf3fbed778d8fb0f535486155ac)。

获取底层 APLIC 设备（Device）。

<a id="r_a883c641c0c4f933f9956cca1dd058052"></a>

```c
void riscv_aia_config_source (uint32_t irq, uint32_t mode)
```

相关声明：[riscv_aia_config_source](#a883c641c0c4f933f9956cca1dd058052)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 APLIC 中断源模式（Source Mode）。

<a id="r_a778cbf67ab1c36d92a72f72599e99056"></a>

```c
void riscv_aia_route_to_hart (uint32_t irq, uint32_t hart, uint32_t eiid)
```

相关声明：[riscv_aia_route_to_hart](#a778cbf67ab1c36d92a72f72599e99056)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 APLIC 中断源路由到指定硬件线程（Hart）。

<a id="r_a33533234d1b70b765c602c9416b8daee"></a>

```c
void riscv_aia_inject_msi (uint32_t hart, uint32_t eiid)
```

相关声明：[riscv_aia_inject_msi](#a33533234d1b70b765c602c9416b8daee)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 APLIC GENMSI 寄存器注入软件消息信号中断（Message-signaled Interrupt，MSI）。

<a id="r_ac58c781ce90f600f827ff7edc710dc98"></a>

```c
void riscv_aia_enable_source (uint32_t irq)
```

相关声明：[riscv_aia_enable_source](#ac58c781ce90f600f827ff7edc710dc98)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用便捷封装（Convenience Wrapper）启用 APLIC 中断源。

<a id="r_a1405f722d840cbc803a7edbcc1c4c5c7"></a>

```c
void riscv_aia_dispatch_eiid (uint32_t eiid)
```

相关声明：[riscv_aia_dispatch_eiid](#a1405f722d840cbc803a7edbcc1c4c5c7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 AIA 二级中断服务例程表（Second-level ISR Table）分派 IMSIC 外部中断标识（EIID）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a883c641c0c4f933f9956cca1dd058052"></a>

### `riscv_aia_config_source()`

```c
void riscv_aia_config_source ( uint32_t irq, uint32_t mode )
```

配置 APLIC 中断源模式（Source Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |
| `mode` | RISC-V AIA 规范第 4.5.2 节规定的中断源模式（Source Mode，即触发类型）。 |

<a id="a1405f722d840cbc803a7edbcc1c4c5c7"></a>

### `riscv_aia_dispatch_eiid()`

```c
void riscv_aia_dispatch_eiid ( uint32_t eiid)
```

通过 AIA 二级中断服务例程表（Second-level ISR Table）分派 IMSIC 外部中断标识（EIID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eiid` | IMSIC 外部中断标识（External Interrupt Identity，EIID）。 |

<a id="ac58c781ce90f600f827ff7edc710dc98"></a>

### `riscv_aia_enable_source()`

```c
void riscv_aia_enable_source ( uint32_t irq)
```

使用便捷封装（Convenience Wrapper）启用 APLIC 中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="a05cb2cf3fbed778d8fb0f535486155ac"></a>

### `riscv_aia_get_dev()`

```c
const struct device * riscv_aia_get_dev ( void )
```

声明属性：`inline`、`static`。

获取底层 APLIC 设备（Device）。

**返回（Returns）**：返回值（Returns）：指向 APLIC 设备的指针。

<a id="a33533234d1b70b765c602c9416b8daee"></a>

### `riscv_aia_inject_msi()`

```c
void riscv_aia_inject_msi ( uint32_t hart, uint32_t eiid )
```

通过 APLIC GENMSI 寄存器注入软件消息信号中断（Message-signaled Interrupt，MSI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hart` | 目标硬件线程（Hart）的索引。 |
| `eiid` | 待注入的外部中断标识（EIID）。 |

<a id="a3598cc5edfbd910b8cb01ffc76c8a17f"></a>

### `riscv_aia_irq_disable()`

```c
void riscv_aia_irq_disable ( uint32_t irq)
```

禁用 AIA 中断源（Interrupt Source）。

同时禁用 IMSIC 中的 EIID 和 APLIC 中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="abf2922519b5ec25a57ded7544c2a401c"></a>

### `riscv_aia_irq_enable()`

```c
void riscv_aia_irq_enable ( uint32_t irq)
```

启用 AIA 中断源（Interrupt Source）。

在 IMSIC 中启用 EIID，并配置和启用 APLIC 中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

<a id="ac1c545848a8101e24b515a25ba76f65d"></a>

### `riscv_aia_irq_is_enabled()`

```c
int riscv_aia_irq_is_enabled ( uint32_t irq)
```

检查 AIA 中断源（Interrupt Source）是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |

**返回（Returns）**：返回值（Returns）：已启用时返回非零值，已禁用时返回 0。

<a id="a778cbf67ab1c36d92a72f72599e99056"></a>

### `riscv_aia_route_to_hart()`

```c
void riscv_aia_route_to_hart ( uint32_t irq, uint32_t hart, uint32_t eiid )
```

将 APLIC 中断源路由到指定硬件线程（Hart）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |
| `hart` | 目标硬件线程（Hart）的索引。 |
| `eiid` | 要投递到目标硬件线程（Hart）的 IMSIC 的外部中断标识（EIID）。 |

**说明（Note）**：注意（Note）：eiid 用于同时启用 APLIC 和 IMSIC 的情形。APLIC 使用直接投递模式（Direct Delivery Mode）时不存在此参数。

<a id="a6d06861210dacb74fece7b13699b7327"></a>

### `riscv_aia_set_priority()`

```c
void riscv_aia_set_priority ( uint32_t irq, uint32_t prio )
```

设置 AIA 中断源的优先级（Priority）。

APLIC-MSI 模式没有逐中断源的优先级寄存器；优先级由 IMSIC EITHRESHOLD 或隐式 EIID 排序处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 采用多级编码（multi-level encoded）的中断 ID。 |
| `prio` | 优先级值（Priority Value）；目前在 MSI 模式下忽略。 |


## 10.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/drivers/interrupt_controller/riscv_aplic.h](../api_source_reference/P716_riscv_aplic.h_源码浏览.md)
- [zephyr/drivers/interrupt_controller/riscv_imsic.h](../api_source_transport_clock_reference/P023_riscv_imsic.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P715_riscv_aia.h_源码浏览.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_zephyr__dt-bindings__usb-c__nxp_nx20p3483.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__sip_svc__sip_svc_proto.h_文件参考.md)
