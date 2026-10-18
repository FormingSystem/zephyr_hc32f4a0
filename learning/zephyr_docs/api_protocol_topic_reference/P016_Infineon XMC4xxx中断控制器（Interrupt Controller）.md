---
id: learning.zephyr-docs.api-protocol-topic-reference.page-16
title: Infineon XMC4xxx中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_Infineon XMC4xxx中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon XMC4xxx 中断控制器的设备树宏。

<a id="details"></a>

Infineon XMC4xxx 中断控制器的设备树宏（devicetree macros）。这些宏用于编码兼容 `infineon,xmc4xxx-intc` 的中断控制器所使用的事件请求单元（Event Request Unit，ERU）线路映射单元（line mapping cells）。`XMC4XXX_INTC_SET_LINE_MAP()` 将 GPIO 端口和引脚、ERU 输入源 `eru_src` 以及 ERU 输出线路打包为一个映射值；对应的 `XMC4XXX_INTC_GET_*` 访问宏则提取各字段。下方保留原始配置示例。

```c
&some_device {
        interrupt-names = "rx";
        interrupts = <XMC4XXX_INTC_SET_LINE_MAP(0, 1, 0, 0) 0>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_infineon-xmc4xxx-intc_2Eh"></a>

```c
file infineon-xmc4xxx-intc.h
```

相关声明：[infineon-xmc4xxx-intc.h](../api_file_interface_reference/P023_zephyr__dt-bindings__interrupt-controller__infineon-xmc4xxx-intc.h_文件参考.md)。

Infineon XMC4xxx中断控制器（Interrupt Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.2\_宏定义（Macros）

<a id="r_ga908ab6f538ea2a135d002b9c4d9bdea0"></a>

```c
#define XMC4XXX_INTC_GET_PORT(mx)
```

相关声明：[XMC4XXX_INTC_GET_PORT](#ga908ab6f538ea2a135d002b9c4d9bdea0)。

从线路映射值（line mapping value）中提取 GPIO 端口。

<a id="r_ga415130dd3eeae518bb469122bfb44223"></a>

```c
#define XMC4XXX_INTC_GET_PIN(mx)
```

相关声明：[XMC4XXX_INTC_GET_PIN](#ga415130dd3eeae518bb469122bfb44223)。

从线路映射值中提取 GPIO 引脚。

<a id="r_ga7ff570440afc268c833d4991c58792d2"></a>

```c
#define XMC4XXX_INTC_GET_LINE(mx)
```

相关声明：[XMC4XXX_INTC_GET_LINE](#ga7ff570440afc268c833d4991c58792d2)。

从线路映射值中提取事件请求单元（ERU）的输出线路。

<a id="r_gafe9fae2864cfa87bc9a458c24d6bdc5e"></a>

```c
#define XMC4XXX_INTC_GET_ERU_SRC(mx)
```

相关声明：[XMC4XXX_INTC_GET_ERU_SRC](#gafe9fae2864cfa87bc9a458c24d6bdc5e)。

从线路映射值中提取 ERU 输入源。

<a id="r_gac7cbe5628158a8852ea3ea8fafd4e2b1"></a>

```c
#define XMC4XXX_INTC_SET_LINE_MAP(port, pin, eru_src, line)
```

相关声明：[XMC4XXX_INTC_SET_LINE_MAP](#gac7cbe5628158a8852ea3ea8fafd4e2b1)。

编码 ERU 线路映射值。

## 16.3\_详细说明（Detailed Documentation）

<a id="gafe9fae2864cfa87bc9a458c24d6bdc5e"></a>

### `XMC4XXX_INTC_GET_ERU_SRC`

```c
#define XMC4XXX_INTC_GET_ERU_SRC ( mx)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/infineon-xmc4xxx-intc.h>
```

展开值（Value）：

```c
((mx >> XMC4XXX_INTC_ERU_SRC_POS) & XMC4XXX_INTC_ERU_SRC_MASK)
```

从线路映射值中提取 ERU 输入源。

<a id="ga7ff570440afc268c833d4991c58792d2"></a>

### `XMC4XXX_INTC_GET_LINE`

```c
#define XMC4XXX_INTC_GET_LINE ( mx)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/infineon-xmc4xxx-intc.h>
```

展开值（Value）：

```c
((mx >> XMC4XXX_INTC_LINE_POS) & XMC4XXX_INTC_LINE_MASK)
```

从线路映射值中提取事件请求单元（ERU）的输出线路。

<a id="ga415130dd3eeae518bb469122bfb44223"></a>

### `XMC4XXX_INTC_GET_PIN`

```c
#define XMC4XXX_INTC_GET_PIN ( mx)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/infineon-xmc4xxx-intc.h>
```

展开值（Value）：

```c
((mx >> XMC4XXX_INTC_PIN_POS) & XMC4XXX_INTC_PIN_MASK)
```

从线路映射值中提取 GPIO 引脚。

<a id="ga908ab6f538ea2a135d002b9c4d9bdea0"></a>

### `XMC4XXX_INTC_GET_PORT`

```c
#define XMC4XXX_INTC_GET_PORT ( mx)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/infineon-xmc4xxx-intc.h>
```

展开值（Value）：

```c
((mx >> XMC4XXX_INTC_PORT_POS) & XMC4XXX_INTC_PORT_MASK)
```

从线路映射值（line mapping value）中提取 GPIO 端口。

<a id="gac7cbe5628158a8852ea3ea8fafd4e2b1"></a>

### `XMC4XXX_INTC_SET_LINE_MAP`

```c
#define XMC4XXX_INTC_SET_LINE_MAP ( port, pin, eru_src, line )
```

```c
#include <zephyr/dt-bindings/interrupt-controller/infineon-xmc4xxx-intc.h>
```

展开值（Value）：

```c
((port) << XMC4XXX_INTC_PORT_POS | (pin) << XMC4XXX_INTC_PIN_POS |                         \
 (eru_src) << XMC4XXX_INTC_ERU_SRC_POS | (line) << XMC4XXX_INTC_LINE_POS)
```

编码 ERU 线路映射值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | GPIO 端口编号（port number）。 |
| `pin` | GPIO引脚编号。 |
| `eru_src` | ERU 输入源（input source）。 |
| `line` | ERU 输出线路（output line）。 |


## 16.4\_原页交叉引用（Cross References）

- [infineon-xmc4xxx-intc.h](../api_file_interface_reference/P023_zephyr__dt-bindings__interrupt-controller__infineon-xmc4xxx-intc.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P015_动态主机配置协议第 6 版（DHCPv6）.md) · [返回大纲](大纲.md) · [下一章](P017_ITE IT8XXX2中断控制器（Interrupt Controller）.md)
