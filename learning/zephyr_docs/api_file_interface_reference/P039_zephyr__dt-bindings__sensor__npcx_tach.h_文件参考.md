---
id: learning.zephyr-docs.api-file-interface-reference.page-39
title: zephyr__dt-bindings__sensor__npcx_tach.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__tach_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_dt-bindings\_\_sensor\_\_npcx\_tach.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcx__tach_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Nuvoton NPCX tachometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Nuvoton NPCX tachometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 39.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 转速计端口（Tachometer port）

设备树 `port` 属性的取值。

<a id="r_ga0f22a7498d8b876d1bf191bfb85e8c78"></a>

```c
#define NPCX_TACH_PORT_A 0
```

相关声明：[NPCX_TACH_PORT_A](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#ga0f22a7498d8b876d1bf191bfb85e8c78)。

转速计（Tachometer）端口 A。

<a id="r_gaada5fd466d3b151241cf01e5cd7785b5"></a>

```c
#define NPCX_TACH_PORT_B 1
```

相关声明：[NPCX_TACH_PORT_B](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#gaada5fd466d3b151241cf01e5cd7785b5)。

转速计端口 B。

<a id="define-members-1"></a>

### 运行频率（Operating frequency）

设备树 `sample-clk` 属性的取值。

<a id="r_ga3b5656c1babd52fbe087d2426f8bc3fe"></a>

```c
#define NPCX_TACH_FREQ_LFCLK 32768
```

相关声明：[NPCX_TACH_FREQ_LFCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#ga3b5656c1babd52fbe087d2426f8bc3fe)。

低频时钟（low-frequency clock），32768 Hz。


## 39.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P595_npcx_tach.h_源码浏览.md)
- [NPCX_TACH_PORT_A](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#ga0f22a7498d8b876d1bf191bfb85e8c78)
- [NPCX_TACH_PORT_B](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#gaada5fd466d3b151241cf01e5cd7785b5)
- [NPCX_TACH_FREQ_LFCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__tach__interface.html#ga3b5656c1babd52fbe087d2426f8bc3fe)

<a id="header-details"></a>

---

[上一章](P038_zephyr__dt-bindings__gpio__nordic-npm6001-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__dt-bindings__gpio__nxp-kinetis-gpio.h_文件参考.md)
