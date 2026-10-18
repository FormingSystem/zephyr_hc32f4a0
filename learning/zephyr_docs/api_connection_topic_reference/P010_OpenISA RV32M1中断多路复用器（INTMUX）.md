---
id: learning.zephyr-docs.api-connection-topic-reference.page-10
title: OpenISA RV32M1中断多路复用器（INTMUX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__openisa__intmux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_OpenISA RV32M1中断多路复用器（INTMUX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__openisa__intmux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

OpenISA RV32M1 中断多路复用器（Interrupt Multiplexer，INTMUX）的设备树宏。

<a id="details"></a>

OpenISA RV32M1 中断多路复用器（Interrupt Multiplexer，INTMUX）的设备树宏。定义兼容 `openisa,rv32m1-intmux` 的中断控制器中各 INTMUX 通道的一级 IRQ 偏移量。每个通道将一组二级中断聚合到一条一级中断线上；`INTMUX_CHx_IRQ` 值给出通道 x 的一级中断线编号，并设置在对应的 `openisa,rv32m1-intmux-ch` 中断控制器节点上。下方保留原始配置示例。

```c
intmux0_ch0: interrupt-controller@0 {
        compatible = "openisa,rv32m1-intmux-ch";
        #address-cells = <0>;
        #interrupt-cells = <1>;
        interrupt-controller;
        interrupts = <INTMUX_CH0_IRQ>;
        reg = <0x0 0x40>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_openisa-intmux_2Eh"></a>

```c
file openisa-intmux.h
```

相关声明：[openisa-intmux.h](https://docs.zephyrproject.org/latest/doxygen/html/openisa-intmux_8h.html)。

OpenISA RV32M1中断多路复用器（INTMUX）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.2\_宏定义（Macros）

<a id="r_ga3118debb396d89fc28d1a75c2c1411a9"></a>

```c
#define INTMUX_CH0_IRQ 24
```

相关声明：[INTMUX_CH0_IRQ](#ga3118debb396d89fc28d1a75c2c1411a9)。

INTMUX 通道 0 的一级 IRQ。

<a id="r_gac80c956b39ea66891b0058cdbbaf3d25"></a>

```c
#define INTMUX_CH1_IRQ 25
```

相关声明：[INTMUX_CH1_IRQ](#gac80c956b39ea66891b0058cdbbaf3d25)。

INTMUX 通道 1 的一级 IRQ。

<a id="r_ga13adbfc363e8c3b782eb600e5df8fbab"></a>

```c
#define INTMUX_CH2_IRQ 26
```

相关声明：[INTMUX_CH2_IRQ](#ga13adbfc363e8c3b782eb600e5df8fbab)。

INTMUX 通道 2 的一级 IRQ。

<a id="r_ga7921514c0f8f387a572335ba0a84362e"></a>

```c
#define INTMUX_CH3_IRQ 27
```

相关声明：[INTMUX_CH3_IRQ](#ga7921514c0f8f387a572335ba0a84362e)。

INTMUX 通道 3 的一级 IRQ。

<a id="r_gac01c50d1d3326c225f505306f0724c04"></a>

```c
#define INTMUX_CH4_IRQ 28
```

相关声明：[INTMUX_CH4_IRQ](#gac01c50d1d3326c225f505306f0724c04)。

INTMUX 通道 4 的一级 IRQ。

<a id="r_gacc49ffa1810f90b9210a950be840c5a8"></a>

```c
#define INTMUX_CH5_IRQ 29
```

相关声明：[INTMUX_CH5_IRQ](#gacc49ffa1810f90b9210a950be840c5a8)。

INTMUX 通道 5 的一级 IRQ。

<a id="r_ga8e4c4343ba85760a08b5d7a268ebb1aa"></a>

```c
#define INTMUX_CH6_IRQ 30
```

相关声明：[INTMUX_CH6_IRQ](#ga8e4c4343ba85760a08b5d7a268ebb1aa)。

INTMUX 通道 6 的一级 IRQ。

<a id="r_gabdbb1949ee8bfba417290500286a9436"></a>

```c
#define INTMUX_CH7_IRQ 31
```

相关声明：[INTMUX_CH7_IRQ](#gabdbb1949ee8bfba417290500286a9436)。

INTMUX 通道 7 的一级 IRQ。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga3118debb396d89fc28d1a75c2c1411a9"></a>

### `INTMUX_CH0_IRQ`

```c
#define INTMUX_CH0_IRQ 24
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 0 的一级 IRQ。

<a id="gac80c956b39ea66891b0058cdbbaf3d25"></a>

### `INTMUX_CH1_IRQ`

```c
#define INTMUX_CH1_IRQ 25
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 1 的一级 IRQ。

<a id="ga13adbfc363e8c3b782eb600e5df8fbab"></a>

### `INTMUX_CH2_IRQ`

```c
#define INTMUX_CH2_IRQ 26
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 2 的一级 IRQ。

<a id="ga7921514c0f8f387a572335ba0a84362e"></a>

### `INTMUX_CH3_IRQ`

```c
#define INTMUX_CH3_IRQ 27
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 3 的一级 IRQ。

<a id="gac01c50d1d3326c225f505306f0724c04"></a>

### `INTMUX_CH4_IRQ`

```c
#define INTMUX_CH4_IRQ 28
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 4 的一级 IRQ。

<a id="gacc49ffa1810f90b9210a950be840c5a8"></a>

### `INTMUX_CH5_IRQ`

```c
#define INTMUX_CH5_IRQ 29
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 5 的一级 IRQ。

<a id="ga8e4c4343ba85760a08b5d7a268ebb1aa"></a>

### `INTMUX_CH6_IRQ`

```c
#define INTMUX_CH6_IRQ 30
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 6 的一级 IRQ。

<a id="gabdbb1949ee8bfba417290500286a9436"></a>

### `INTMUX_CH7_IRQ`

```c
#define INTMUX_CH7_IRQ 31
```

```c
#include <zephyr/dt-bindings/interrupt-controller/openisa-intmux.h>
```

INTMUX 通道 7 的一级 IRQ。


## 10.4\_原页交叉引用（Cross References）

- [openisa-intmux.h](https://docs.zephyrproject.org/latest/doxygen/html/openisa-intmux_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_分布式交换架构（Distributed Switch Architecture，DSA）。.md) · [返回大纲](大纲.md) · [下一章](P011_闪存映像 API（Flash image API）.md)
