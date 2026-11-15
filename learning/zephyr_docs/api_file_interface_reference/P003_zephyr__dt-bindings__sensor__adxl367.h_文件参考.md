---
id: learning.zephyr-docs.api-file-interface-reference.page-3
title: zephyr__dt-bindings__sensor__adxl367.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adxl367_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_sensor\_\_adxl367.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adxl367_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Analog Devices ADXL367 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Analog Devices ADXL367 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### FIFO 模式选项（FIFO mode options）

设备树 `fifo-mode` 属性的取值。

<a id="r_ga263ef6fecf67b97692d04c51add47138"></a>

```c
#define ADXL367_FIFO_MODE_DISABLED 0x0
```

相关声明：[ADXL367_FIFO_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga263ef6fecf67b97692d04c51add47138)。

禁用先进先出缓冲区（FIFO）。

<a id="r_ga8f5ce6faf0e0839661e9b036d51979ce"></a>

```c
#define ADXL367_FIFO_MODE_OLDEST_SAVED 0x1
```

相关声明：[ADXL367_FIFO_MODE_OLDEST_SAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga8f5ce6faf0e0839661e9b036d51979ce)。

缓冲区满时停止，保留最早的样本（samples）。

<a id="r_gaaeff202cb640db5129bf014434a01857"></a>

```c
#define ADXL367_FIFO_MODE_STREAM 0x2
```

相关声明：[ADXL367_FIFO_MODE_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#gaaeff202cb640db5129bf014434a01857)。

连续流（continuous stream）模式，覆盖最早的样本。

<a id="r_ga3348f6dce35164f80a6d5da50760ba12"></a>

```c
#define ADXL367_FIFO_MODE_TRIGGERED 0x3
```

相关声明：[ADXL367_FIFO_MODE_TRIGGERED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga3348f6dce35164f80a6d5da50760ba12)。

采集触发事件（trigger event）前后的样本。


## 3.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P014_adxl367.h_源码浏览.md)
- [ADXL367_FIFO_MODE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga263ef6fecf67b97692d04c51add47138)
- [ADXL367_FIFO_MODE_OLDEST_SAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga8f5ce6faf0e0839661e9b036d51979ce)
- [ADXL367_FIFO_MODE_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#gaaeff202cb640db5129bf014434a01857)
- [ADXL367_FIFO_MODE_TRIGGERED](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl367__interface.html#ga3348f6dce35164f80a6d5da50760ba12)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__sensor__adxl362.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__sensor__adxl372.h_文件参考.md)
