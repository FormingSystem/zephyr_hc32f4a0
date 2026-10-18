---
id: learning.zephyr-docs.api-protocol-topic-reference.page-41
title: NPCX 转速计（Tachometer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_NPCX 转速计（Tachometer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nuvoton NPCX 转速计（Tachometer）

<a id="details"></a>

Nuvoton NPCX 转速计（Tachometer）

<a id="header-files"></a>
<a id="files"></a>

## 41.1\_文件（Files）

<a id="r_npcx_5Ftach_2Eh"></a>

```c
file npcx_tach.h
```

相关声明：[npcx_tach.h](../api_file_interface_reference/P039_zephyr__dt-bindings__sensor__npcx_tach.h_文件参考.md)。

the Nuvoton NPCX tachometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 41.2\_转速计端口（Tachometer port）

设备树 `port` 属性的取值。

<a id="r_ga0f22a7498d8b876d1bf191bfb85e8c78"></a>

```c
#define NPCX_TACH_PORT_A 0
```

相关声明：[NPCX_TACH_PORT_A](#ga0f22a7498d8b876d1bf191bfb85e8c78)。

转速计（Tachometer）端口 A。

<a id="r_gaada5fd466d3b151241cf01e5cd7785b5"></a>

```c
#define NPCX_TACH_PORT_B 1
```

相关声明：[NPCX_TACH_PORT_B](#gaada5fd466d3b151241cf01e5cd7785b5)。

转速计端口 B。

## 41.3\_运行频率（Operating frequency）

设备树 `sample-clk` 属性的取值。

<a id="r_ga3b5656c1babd52fbe087d2426f8bc3fe"></a>

```c
#define NPCX_TACH_FREQ_LFCLK 32768
```

相关声明：[NPCX_TACH_FREQ_LFCLK](#ga3b5656c1babd52fbe087d2426f8bc3fe)。

低频时钟（low-frequency clock），32768 Hz。

## 41.4\_详细说明（Detailed Documentation）

<a id="ga3b5656c1babd52fbe087d2426f8bc3fe"></a>

### `NPCX_TACH_FREQ_LFCLK`

```c
#define NPCX_TACH_FREQ_LFCLK 32768
```

```c
#include <zephyr/dt-bindings/sensor/npcx_tach.h>
```

低频时钟（low-frequency clock），32768 Hz。

<a id="ga0f22a7498d8b876d1bf191bfb85e8c78"></a>

### `NPCX_TACH_PORT_A`

```c
#define NPCX_TACH_PORT_A 0
```

```c
#include <zephyr/dt-bindings/sensor/npcx_tach.h>
```

转速计（Tachometer）端口 A。

<a id="gaada5fd466d3b151241cf01e5cd7785b5"></a>

### `NPCX_TACH_PORT_B`

```c
#define NPCX_TACH_PORT_B 1
```

```c
#include <zephyr/dt-bindings/sensor/npcx_tach.h>
```

转速计端口 B。


## 41.5\_原页交叉引用（Cross References）

- [npcx_tach.h](../api_file_interface_reference/P039_zephyr__dt-bindings__sensor__npcx_tach.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P040_网络二层抽象层（Network L2 Abstraction Layer）.md) · [返回大纲](大纲.md) · [下一章](P042_Nunchuk API主题.md)
