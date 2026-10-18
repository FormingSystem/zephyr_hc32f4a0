---
id: learning.zephyr-docs.platform-security-model-reference.page-75
title: xen_domctl_pt_irq_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structxen__domctl__pt__irq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_xen\_domctl\_pt\_irq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structxen__domctl__pt__irq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

物理中断直通（Physical Interrupt Passthrough）描述符。

```c
#include <zephyr/xen/dom0/domctl.h>
```

<a id="details"></a>

物理中断直通（Physical Interrupt Passthrough）描述符。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_ad30d0377c24cb436398c1038116a2640"></a>

```c
uint32_t machine_irq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[machine_irq](#ad30d0377c24cb436398c1038116a2640)。

要绑定或解绑的机器 IRQ 编号。

<a id="r_a22a173359bdeacec66c8b26208004a43"></a>

```c
uint8_t irq_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irq_type](#a22a173359bdeacec66c8b26208004a43)。

Xen 直通中断类型（Passthrough IRQ type）。

<a id="r_a56fa5e12491dbc3b262c93a8773a6339"></a>

```c
uint8_t bus
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bus](#a56fa5e12491dbc3b262c93a8773a6339)。

PCI 直通模式使用的 PCI 总线号。

<a id="r_a791e52092d506100c8fcb1b7f206e305"></a>

```c
uint8_t device
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[device](#a791e52092d506100c8fcb1b7f206e305)。

PCI 直通模式使用的 PCI 设备号。

<a id="r_a83da71ec34e53945eeed31b289b87822"></a>

```c
uint8_t intx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[intx](#a83da71ec34e53945eeed31b289b87822)。

PCI 直通模式使用的 PCI INTx 中断线。

<a id="r_a4aa75c8809786e3bec6604e8bf6f7ff2"></a>

```c
uint8_t isa_irq
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[isa_irq](#a4aa75c8809786e3bec6604e8bf6f7ff2)。

ISA 直通模式使用的 ISA IRQ 编号。

<a id="r_aaf73e967e9436059327c368df28c1436"></a>

```c
uint16_t spi
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spi](#aaf73e967e9436059327c368df28c1436)。

与 `PT_IRQ_TYPE_SPI` 配合使用的共享外设中断（SPI）编号。

## 75.2\_详细说明（Detailed Documentation）

<a id="a56fa5e12491dbc3b262c93a8773a6339"></a>

### `bus`

```c
uint8_t xen_domctl_pt_irq::bus
```

PCI 直通模式使用的 PCI 总线号。

<a id="a791e52092d506100c8fcb1b7f206e305"></a>

### `device`

```c
uint8_t xen_domctl_pt_irq::device
```

PCI 直通模式使用的 PCI 设备号。

<a id="a83da71ec34e53945eeed31b289b87822"></a>

### `intx`

```c
uint8_t xen_domctl_pt_irq::intx
```

PCI 直通模式使用的 PCI INTx 中断线。

<a id="a22a173359bdeacec66c8b26208004a43"></a>

### `irq_type`

```c
uint8_t xen_domctl_pt_irq::irq_type
```

Xen 直通中断类型（Passthrough IRQ type）。

<a id="a4aa75c8809786e3bec6604e8bf6f7ff2"></a>

### `isa_irq`

```c
uint8_t xen_domctl_pt_irq::isa_irq
```

ISA 直通模式使用的 ISA IRQ 编号。

<a id="ad30d0377c24cb436398c1038116a2640"></a>

### `machine_irq`

```c
uint32_t xen_domctl_pt_irq::machine_irq
```

要绑定或解绑的机器 IRQ 编号。

<a id="aaf73e967e9436059327c368df28c1436"></a>

### `spi`

```c
uint16_t xen_domctl_pt_irq::spi
```

与 `PT_IRQ_TYPE_SPI` 配合使用的共享外设中断（SPI）编号。

本数据类型文档由以下文件生成：

- `zephyr/xen/dom0/domctl.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/xen/dom0/domctl.h](https://docs.zephyrproject.org/latest/doxygen/html/domctl_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_vtd_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_acpi_dmar_id_联合体.md)
