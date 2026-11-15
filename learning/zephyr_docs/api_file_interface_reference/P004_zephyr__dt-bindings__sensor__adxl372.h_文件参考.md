---
id: learning.zephyr-docs.api-file-interface-reference.page-4
title: zephyr__dt-bindings__sensor__adxl372.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adxl372_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_sensor\_\_adxl372.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adxl372_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Analog Devices ADXL372 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Analog Devices ADXL372 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### FIFO 模式选项（FIFO mode options）

设备树 `fifo-mode` 属性的取值。

<a id="r_gace27031371f0fca13791ad77fb7642d3"></a>

```c
#define ADXL372_FIFO_MODE_BYPASSED 0x0
```

相关声明：[ADXL372_FIFO_MODE_BYPASSED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gace27031371f0fca13791ad77fb7642d3)。

旁路（bypass）FIFO，即禁用 FIFO。

<a id="r_ga28f79424f8d0c8b501b5cb33bbaeca89"></a>

```c
#define ADXL372_FIFO_MODE_STREAMED 0x1
```

相关声明：[ADXL372_FIFO_MODE_STREAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#ga28f79424f8d0c8b501b5cb33bbaeca89)。

连续流（continuous stream）模式，覆盖最早的样本。

<a id="r_gad8c7e3cfad1ec512c41a949a22be1c1b"></a>

```c
#define ADXL372_FIFO_MODE_TRIGGERED 0x2
```

相关声明：[ADXL372_FIFO_MODE_TRIGGERED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gad8c7e3cfad1ec512c41a949a22be1c1b)。

采集触发事件（trigger event）前后的样本。

<a id="r_gae75dd1acf478fb3d0f415691d61f11a9"></a>

```c
#define ADXL372_FIFO_MODE_OLD_SAVED 0x3
```

相关声明：[ADXL372_FIFO_MODE_OLD_SAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gae75dd1acf478fb3d0f415691d61f11a9)。

缓冲区满时停止，保留最早的样本（samples）。


## 4.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P015_adxl372.h_源码浏览.md)
- [ADXL372_FIFO_MODE_BYPASSED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gace27031371f0fca13791ad77fb7642d3)
- [ADXL372_FIFO_MODE_STREAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#ga28f79424f8d0c8b501b5cb33bbaeca89)
- [ADXL372_FIFO_MODE_TRIGGERED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gad8c7e3cfad1ec512c41a949a22be1c1b)
- [ADXL372_FIFO_MODE_OLD_SAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl372__interface.html#gae75dd1acf478fb3d0f415691d61f11a9)

<a id="header-details"></a>

---

[上一章](P003_zephyr__dt-bindings__sensor__adxl367.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__crypto.h_文件参考.md)
