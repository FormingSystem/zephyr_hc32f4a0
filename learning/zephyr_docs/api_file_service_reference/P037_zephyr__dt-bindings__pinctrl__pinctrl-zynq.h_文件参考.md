---
id: learning.zephyr-docs.api-file-service-reference.page-37
title: zephyr__dt-bindings__pinctrl__pinctrl-zynq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_pinctrl-zynq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-zynq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="define-members-0"></a>

### I/O 缓冲器类型（Buffer Type）

Xilinx Zynq-7000 引脚控制设备树属性（Pinctrl Devicetree Property）`power-source` 的取值定义。

该值对应于写入 MIO_PIN_xx 系统级控制寄存器（SLCR）的 `IO_Type` 字段中的值。

<a id="r_ae50eb80b37c2b6508be7862c720c7c13"></a>

```c
#define IO_STANDARD_LVCMOS18 1
```

相关声明：[IO_STANDARD_LVCMOS18](#ae50eb80b37c2b6508be7862c720c7c13)。

<a id="r_aebe38d401743d61abd001aa8735eba10"></a>

```c
#define IO_STANDARD_LVCMOS25 2
```

相关声明：[IO_STANDARD_LVCMOS25](#aebe38d401743d61abd001aa8735eba10)。

<a id="r_a6015c7b6d1117ad20f8cab5b0f65d06f"></a>

```c
#define IO_STANDARD_LVCMOS33 3
```

相关声明：[IO_STANDARD_LVCMOS33](#a6015c7b6d1117ad20f8cab5b0f65d06f)。

<a id="r_a063cebe926942f2c295d32b5949943af"></a>

```c
#define IO_STANDARD_HSTL 4
```

相关声明：[IO_STANDARD_HSTL](#a063cebe926942f2c295d32b5949943af)。

<a id="define-members-1"></a>

### I/O 缓冲器边沿速率（Buffer Edge Rate）

Xilinx Zynq-7000 引脚控制设备树属性（Pinctrl Devicetree Property）`slew-rate` 的取值定义。

该值对应于写入 MIO_PIN_xx 系统级控制寄存器（SLCR）的 `Speed` 字段中的值。

<a id="r_a6b26a7bf79bd5160c02eb9d53415165f"></a>

```c
#define IO_SPEED_SLOW 0
```

相关声明：[IO_SPEED_SLOW](#a6b26a7bf79bd5160c02eb9d53415165f)。

<a id="r_af298ed3b409d8ce6330fa4ff63c9a82e"></a>

```c
#define IO_SPEED_FAST 1
```

相关声明：[IO_SPEED_FAST](#af298ed3b409d8ce6330fa4ff63c9a82e)。

## 37.2\_详细说明（Detailed Documentation）

<a id="af298ed3b409d8ce6330fa4ff63c9a82e"></a>

### `IO_SPEED_FAST`

```c
#define IO_SPEED_FAST 1
```

<a id="a6b26a7bf79bd5160c02eb9d53415165f"></a>

### `IO_SPEED_SLOW`

```c
#define IO_SPEED_SLOW 0
```

<a id="a063cebe926942f2c295d32b5949943af"></a>

### `IO_STANDARD_HSTL`

```c
#define IO_STANDARD_HSTL 4
```

<a id="ae50eb80b37c2b6508be7862c720c7c13"></a>

### `IO_STANDARD_LVCMOS18`

```c
#define IO_STANDARD_LVCMOS18 1
```

<a id="aebe38d401743d61abd001aa8735eba10"></a>

### `IO_STANDARD_LVCMOS25`

```c
#define IO_STANDARD_LVCMOS25 2
```

<a id="a6015c7b6d1117ad20f8cab5b0f65d06f"></a>

### `IO_STANDARD_LVCMOS33`

```c
#define IO_STANDARD_LVCMOS33 3
```


## 37.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P655_pinctrl-zynq.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P036_zephyr__drivers__regulator__pca9420.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__drivers__pinctrl__pinctrl_soc_sam_common.h_文件参考.md)
