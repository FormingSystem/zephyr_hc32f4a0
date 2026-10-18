---
id: learning.zephyr-docs.api-file-interface-reference.page-23
title: zephyr__dt-bindings__interrupt-controller__infineon-xmc4xxx-intc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_infineon-xmc4xxx-intc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon XMC4xxx中断控制器（Interrupt Controller）的设备树宏。

查看此文件的源码。

<a id="details"></a>

Infineon XMC4xxx中断控制器（Interrupt Controller）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.1\_宏定义（Macros）

<a id="r_ga908ab6f538ea2a135d002b9c4d9bdea0"></a>

```c
#define XMC4XXX_INTC_GET_PORT(mx)
```

相关声明：[XMC4XXX_INTC_GET_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga908ab6f538ea2a135d002b9c4d9bdea0)。

从线路映射值（line mapping value）中提取 GPIO 端口。

<a id="r_ga415130dd3eeae518bb469122bfb44223"></a>

```c
#define XMC4XXX_INTC_GET_PIN(mx)
```

相关声明：[XMC4XXX_INTC_GET_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga415130dd3eeae518bb469122bfb44223)。

从线路映射值中提取 GPIO 引脚。

<a id="r_ga7ff570440afc268c833d4991c58792d2"></a>

```c
#define XMC4XXX_INTC_GET_LINE(mx)
```

相关声明：[XMC4XXX_INTC_GET_LINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga7ff570440afc268c833d4991c58792d2)。

从线路映射值中提取事件请求单元（ERU）的输出线路。

<a id="r_gafe9fae2864cfa87bc9a458c24d6bdc5e"></a>

```c
#define XMC4XXX_INTC_GET_ERU_SRC(mx)
```

相关声明：[XMC4XXX_INTC_GET_ERU_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#gafe9fae2864cfa87bc9a458c24d6bdc5e)。

从线路映射值中提取 ERU 输入源。

<a id="r_gac7cbe5628158a8852ea3ea8fafd4e2b1"></a>

```c
#define XMC4XXX_INTC_SET_LINE_MAP(port, pin, eru_src, line)
```

相关声明：[XMC4XXX_INTC_SET_LINE_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#gac7cbe5628158a8852ea3ea8fafd4e2b1)。

编码 ERU 线路映射值。


## 23.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P373_infineon-xmc4xxx-intc.h_源码浏览.md)
- [XMC4XXX_INTC_GET_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga908ab6f538ea2a135d002b9c4d9bdea0)
- [XMC4XXX_INTC_GET_PIN](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga415130dd3eeae518bb469122bfb44223)
- [XMC4XXX_INTC_GET_LINE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#ga7ff570440afc268c833d4991c58792d2)
- [XMC4XXX_INTC_GET_ERU_SRC](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#gafe9fae2864cfa87bc9a458c24d6bdc5e)
- [XMC4XXX_INTC_SET_LINE_MAP](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__infineon__xmc4xxx__intc.html#gac7cbe5628158a8852ea3ea8fafd4e2b1)

<a id="header-details"></a>

---

[上一章](P022_zephyr__video__types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__input__input_analog_axis.h_文件参考.md)
