---
id: learning.zephyr-docs.api-file-system-device-reference.page-10
title: zephyr__dt-bindings__sensor__mtch9010.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mtch9010_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_sensor\_\_mtch9010.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mtch9010_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Microchip MTCH9010 sensor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Microchip MTCH9010 sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 工作模式（Operating mode）

设备树 `operating-mode` 属性的取值。

<a id="r_gaef5c74953312c81aaf7c2957a23958c7"></a>

```c
#define MTCH9010_CAPACITIVE 0x0
```

相关声明：[MTCH9010_CAPACITIVE](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaef5c74953312c81aaf7c2957a23958c7)。

电容感测（capacitive sensing）。

<a id="r_gab6575fc8f31fec440d4a4b1e3a7ecdf9"></a>

```c
#define MTCH9010_CONDUCTIVE 0x1
```

相关声明：[MTCH9010_CONDUCTIVE](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gab6575fc8f31fec440d4a4b1e3a7ecdf9)。

导电感测（conductive sensing）。

<a id="define-members-1"></a>

### UART 输出数据格式（output data format）

设备树 `extended-output-format` 属性的取值。

<a id="r_gaeeeb7d41b461bae584f72615bc0b95ff"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_DELTA 0x0
```

相关声明：[MTCH9010_OUTPUT_FORMAT_DELTA](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaeeeb7d41b461bae584f72615bc0b95ff)。

相对于参考值的差值（delta from reference）。

<a id="r_gaaa2201ad6438823188b8a23e859fcf09"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_CURRENT 0x1
```

相关声明：[MTCH9010_OUTPUT_FORMAT_CURRENT](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaaa2201ad6438823188b8a23e859fcf09)。

当前测量值（current measurement）。

<a id="r_ga181f25eef9166f7e618b20a47e0552c0"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_BOTH 0x2
```

相关声明：[MTCH9010_OUTPUT_FORMAT_BOTH](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#ga181f25eef9166f7e618b20a47e0552c0)。

差值和当前测量值（delta and current）。

<a id="r_ga0e85d6c483d0ebec61bc297dc0213bb2"></a>

```c
#define MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER 0x3
```

相关声明：[MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#ga0e85d6c483d0ebec61bc297dc0213bb2)。

MPLAB Data Visualizer 数据流。


## 10.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P210_mtch9010.h_源码浏览.md)
- [MTCH9010_CAPACITIVE](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaef5c74953312c81aaf7c2957a23958c7)
- [MTCH9010_CONDUCTIVE](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gab6575fc8f31fec440d4a4b1e3a7ecdf9)
- [MTCH9010_OUTPUT_FORMAT_DELTA](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaeeeb7d41b461bae584f72615bc0b95ff)
- [MTCH9010_OUTPUT_FORMAT_CURRENT](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#gaaa2201ad6438823188b8a23e859fcf09)
- [MTCH9010_OUTPUT_FORMAT_BOTH](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#ga181f25eef9166f7e618b20a47e0552c0)
- [MTCH9010_OUTPUT_FORMAT_MPLAB_DATA_VISUALIZER](../api_auxiliary_topic_reference/P015_MTCH9010 API主题.md#ga0e85d6c483d0ebec61bc297dc0213bb2)

<a id="header-details"></a>

---

[上一章](P009_zephyr__drivers__mdio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__display__ed2208-gca.h_文件参考.md)
