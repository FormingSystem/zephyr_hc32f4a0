---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-2
title: FT9001 IOCTRL 寄存器偏移量（Register offsets）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_FT9001 IOCTRL 寄存器偏移量（Register offsets）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__focaltech__pinctrl__regs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用作 `FOCALTECH_PINMUX` 的 `reg` 参数的寄存器偏移量。

<a id="details"></a>

用作 `FOCALTECH_PINMUX` 的 `reg` 参数的寄存器偏移量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga2db3565c57c0e89edecfd8241e414b7f"></a>

```c
#define FOCALTECH_IOCTRL_SPICR_OFFSET 0x00000U
```

相关声明：[FOCALTECH_IOCTRL_SPICR_OFFSET](#ga2db3565c57c0e89edecfd8241e414b7f)。

SPI 控制寄存器（Control Register）。

<a id="r_ga9f243ac6356e1d2c09b8aa16d6f3487a"></a>

```c
#define FOCALTECH_IOCTRL_I2CCR_OFFSET 0x00008U
```

相关声明：[FOCALTECH_IOCTRL_I2CCR_OFFSET](#ga9f243ac6356e1d2c09b8aa16d6f3487a)。

I2C 控制寄存器（Control Register）。

<a id="r_ga3131554431ba1f6e565906bf9a8c0693"></a>

```c
#define FOCALTECH_IOCTRL_SCICR_OFFSET 0x0000CU
```

相关声明：[FOCALTECH_IOCTRL_SCICR_OFFSET](#ga3131554431ba1f6e565906bf9a8c0693)。

串行通信接口 SCI（UART）控制寄存器（Control Register）。

<a id="r_ga8a382b2f5dcad4a7be11fc9cfd3a8314"></a>

```c
#define FOCALTECH_IOCTRL_SWAPCR_OFFSET 0x0001CU
```

相关声明：[FOCALTECH_IOCTRL_SWAPCR_OFFSET](#ga8a382b2f5dcad4a7be11fc9cfd3a8314)。

焊盘交换控制寄存器（Pad Swap Control Register）。

<a id="r_gab0d09004101c15d2fc858c30ba71879a"></a>

```c
#define FOCALTECH_IOCTRL_CLKRSTCR_OFFSET 0x00044U
```

相关声明：[FOCALTECH_IOCTRL_CLKRSTCR_OFFSET](#gab0d09004101c15d2fc858c30ba71879a)。

时钟／复位控制寄存器（Clock/Reset Control Register）。

<a id="r_gaf8486bdfba828091396fb09d5e05df4e"></a>

```c
#define FOCALTECH_IOCTRL_EPORT2CR_OFFSET 0x00054U
```

相关声明：[FOCALTECH_IOCTRL_EPORT2CR_OFFSET](#gaf8486bdfba828091396fb09d5e05df4e)。

EPORT2 控制寄存器（Control Register）。

<a id="r_ga4bb2ac21789c7cb75dd2eec29e1307d6"></a>

```c
#define FOCALTECH_IOCTRL_EPORT3CR_OFFSET 0x00058U
```

相关声明：[FOCALTECH_IOCTRL_EPORT3CR_OFFSET](#ga4bb2ac21789c7cb75dd2eec29e1307d6)。

EPORT3 控制寄存器（Control Register）。

<a id="r_gaebc543c2997a3b00c31bec5b322125aa"></a>

```c
#define FOCALTECH_IOCTRL_EPORT4CR_OFFSET 0x0005CU
```

相关声明：[FOCALTECH_IOCTRL_EPORT4CR_OFFSET](#gaebc543c2997a3b00c31bec5b322125aa)。

EPORT4 控制寄存器（Control Register）。

<a id="r_ga9da453d7344c1fc67dedf68ec3ed2c0f"></a>

```c
#define FOCALTECH_IOCTRL_EPORT5CR_OFFSET 0x00060U
```

相关声明：[FOCALTECH_IOCTRL_EPORT5CR_OFFSET](#ga9da453d7344c1fc67dedf68ec3ed2c0f)。

EPORT5 控制寄存器（Control Register）。

<a id="r_gabcea3853492a4d8c75164edb027b56c1"></a>

```c
#define FOCALTECH_IOCTRL_EPORT6CR_OFFSET 0x00064U
```

相关声明：[FOCALTECH_IOCTRL_EPORT6CR_OFFSET](#gabcea3853492a4d8c75164edb027b56c1)。

EPORT6 控制寄存器（Control Register）。

<a id="r_ga52aeb69fb33364243221a154af98daf2"></a>

```c
#define FOCALTECH_IOCTRL_EPORT7CR_OFFSET 0x00068U
```

相关声明：[FOCALTECH_IOCTRL_EPORT7CR_OFFSET](#ga52aeb69fb33364243221a154af98daf2)。

EPORT7 控制寄存器（Control Register）。

<a id="r_gafc0a01987337263e943204634207d880"></a>

```c
#define FOCALTECH_IOCTRL_SWAPCR2_OFFSET 0x0006CU
```

相关声明：[FOCALTECH_IOCTRL_SWAPCR2_OFFSET](#gafc0a01987337263e943204634207d880)。

焊盘交换控制寄存器 2（Pad Swap Control Register 2）。

<a id="r_gaadb7e0180ec04bc707904500fa674ade"></a>

```c
#define FOCALTECH_IOCTRL_SWAPCR3_OFFSET 0x00070U
```

相关声明：[FOCALTECH_IOCTRL_SWAPCR3_OFFSET](#gaadb7e0180ec04bc707904500fa674ade)。

焊盘交换控制寄存器 3（Pad Swap Control Register 3）。

<a id="r_ga24eb13707b966284e59d3808777dba78"></a>

```c
#define FOCALTECH_IOCTRL_SWAPCR4_OFFSET 0x00074U
```

相关声明：[FOCALTECH_IOCTRL_SWAPCR4_OFFSET](#ga24eb13707b966284e59d3808777dba78)。

焊盘交换控制寄存器 4（Pad Swap Control Register 4）。

<a id="r_gafc7ac6d153176b91191d203f89f0b98f"></a>

```c
#define FOCALTECH_IOCTRL_SWAPCR5_OFFSET 0x00078U
```

相关声明：[FOCALTECH_IOCTRL_SWAPCR5_OFFSET](#gafc7ac6d153176b91191d203f89f0b98f)。

焊盘交换控制寄存器 5（Pad Swap Control Register 5）。

## 2.2\_详细说明（Detailed Documentation）

<a id="gab0d09004101c15d2fc858c30ba71879a"></a>

### `FOCALTECH_IOCTRL_CLKRSTCR_OFFSET`

```c
#define FOCALTECH_IOCTRL_CLKRSTCR_OFFSET 0x00044U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

时钟／复位控制寄存器（Clock/Reset Control Register）。

<a id="gaf8486bdfba828091396fb09d5e05df4e"></a>

### `FOCALTECH_IOCTRL_EPORT2CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT2CR_OFFSET 0x00054U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT2 控制寄存器（Control Register）。

<a id="ga4bb2ac21789c7cb75dd2eec29e1307d6"></a>

### `FOCALTECH_IOCTRL_EPORT3CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT3CR_OFFSET 0x00058U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT3 控制寄存器（Control Register）。

<a id="gaebc543c2997a3b00c31bec5b322125aa"></a>

### `FOCALTECH_IOCTRL_EPORT4CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT4CR_OFFSET 0x0005CU
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT4 控制寄存器（Control Register）。

<a id="ga9da453d7344c1fc67dedf68ec3ed2c0f"></a>

### `FOCALTECH_IOCTRL_EPORT5CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT5CR_OFFSET 0x00060U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT5 控制寄存器（Control Register）。

<a id="gabcea3853492a4d8c75164edb027b56c1"></a>

### `FOCALTECH_IOCTRL_EPORT6CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT6CR_OFFSET 0x00064U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT6 控制寄存器（Control Register）。

<a id="ga52aeb69fb33364243221a154af98daf2"></a>

### `FOCALTECH_IOCTRL_EPORT7CR_OFFSET`

```c
#define FOCALTECH_IOCTRL_EPORT7CR_OFFSET 0x00068U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

EPORT7 控制寄存器（Control Register）。

<a id="ga9f243ac6356e1d2c09b8aa16d6f3487a"></a>

### `FOCALTECH_IOCTRL_I2CCR_OFFSET`

```c
#define FOCALTECH_IOCTRL_I2CCR_OFFSET 0x00008U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

I2C 控制寄存器（Control Register）。

<a id="ga3131554431ba1f6e565906bf9a8c0693"></a>

### `FOCALTECH_IOCTRL_SCICR_OFFSET`

```c
#define FOCALTECH_IOCTRL_SCICR_OFFSET 0x0000CU
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

串行通信接口 SCI（UART）控制寄存器（Control Register）。

<a id="ga2db3565c57c0e89edecfd8241e414b7f"></a>

### `FOCALTECH_IOCTRL_SPICR_OFFSET`

```c
#define FOCALTECH_IOCTRL_SPICR_OFFSET 0x00000U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

SPI 控制寄存器（Control Register）。

<a id="gafc0a01987337263e943204634207d880"></a>

### `FOCALTECH_IOCTRL_SWAPCR2_OFFSET`

```c
#define FOCALTECH_IOCTRL_SWAPCR2_OFFSET 0x0006CU
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

焊盘交换控制寄存器 2（Pad Swap Control Register 2）。

<a id="gaadb7e0180ec04bc707904500fa674ade"></a>

### `FOCALTECH_IOCTRL_SWAPCR3_OFFSET`

```c
#define FOCALTECH_IOCTRL_SWAPCR3_OFFSET 0x00070U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

焊盘交换控制寄存器 3（Pad Swap Control Register 3）。

<a id="ga24eb13707b966284e59d3808777dba78"></a>

### `FOCALTECH_IOCTRL_SWAPCR4_OFFSET`

```c
#define FOCALTECH_IOCTRL_SWAPCR4_OFFSET 0x00074U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

焊盘交换控制寄存器 4（Pad Swap Control Register 4）。

<a id="gafc7ac6d153176b91191d203f89f0b98f"></a>

### `FOCALTECH_IOCTRL_SWAPCR5_OFFSET`

```c
#define FOCALTECH_IOCTRL_SWAPCR5_OFFSET 0x00078U
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

焊盘交换控制寄存器 5（Pad Swap Control Register 5）。

<a id="ga8a382b2f5dcad4a7be11fc9cfd3a8314"></a>

### `FOCALTECH_IOCTRL_SWAPCR_OFFSET`

```c
#define FOCALTECH_IOCTRL_SWAPCR_OFFSET 0x0001CU
```

```c
#include <zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h>
```

焊盘交换控制寄存器（Pad Swap Control Register）。


## 2.3\_原页交叉引用（Cross References）

- [FOCALTECH_PINMUX](../api_protocol_topic_reference/P045_FocalTech FT9001 引脚控制辅助工具（Pin control helpers）.md#ga7298e4f2acb3abbdbf4e45c54fdc612e)
- [zephyr/dt-bindings/pinctrl/focaltech_ft9001_pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/focaltech__ft9001__pinctrl_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_连接管理器 API（Connection Manager API）.md) · [返回大纲](大纲.md) · [下一章](P003_SYSRSTCR 复位控制（Reset Control）.md)
