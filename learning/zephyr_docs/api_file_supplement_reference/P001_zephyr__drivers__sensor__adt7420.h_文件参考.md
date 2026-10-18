---
id: learning.zephyr-docs.api-file-supplement-reference.page-1
title: zephyr__drivers__sensor__adt7420.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adt7420_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_sensor\_\_adt7420.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adt7420_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ADT7420传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

ADT7420传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gaed0418f1aaea93e6026dccbe8e0ce39d"></a>

```c
#define SENSOR_CHAN_ADT7420_CRIT_TEMP SENSOR_CHAN_PRIV_START
```

相关声明：[SENSOR_CHAN_ADT7420_CRIT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__adt7420__interface.html#gaed0418f1aaea93e6026dccbe8e0ce39d)、[SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)。

供 `sensor_trigger_set()` 使用的临界温度触发通道（Critical Temperature Trigger Channel）。


## 1.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P010_adt7420.h_源码浏览.md)
- [SENSOR_CHAN_ADT7420_CRIT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__adt7420__interface.html#gaed0418f1aaea93e6026dccbe8e0ce39d)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor_trigger_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7c72aca732e0641612d2f9437c2e41b7)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__clock_control__ameba_clock_control.h_文件参考.md)
