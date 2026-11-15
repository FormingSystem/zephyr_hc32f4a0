---
id: learning.zephyr-docs.api-file-configuration-reference.page-55
title: zephyr__drivers__sensor__mmc56x3.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mmc56x3_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_drivers\_\_sensor\_\_mmc56x3.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mmc56x3_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MMC56X3传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

MMC56X3 传感器扩展应用程序编程接口（Extended Sensor API）的头文件。它公开 MMC56X3 的属性（Attributes），可用于设置连续模式（Continuous Mode）和带宽选择位（Bandwidth Selection Bits）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 55.1\_枚举（Enumerations）

<a id="r_gaf722f9a8bf8bae84c57aaa1ece387ad8"></a>

```c
enum sensor_attribute_mmc56x3 { SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0 = SENSOR_ATTR_PRIV_START + 1 , SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1 , SENSOR_ATTR_AUTOMATIC_SELF_RESET }
```

相关声明：[sensor_attribute_mmc56x3](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#gaf722f9a8bf8bae84c57aaa1ece387ad8)、[SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b)、[SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630)、[SENSOR_ATTR_AUTOMATIC_SELF_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f)。

MMC56X3 的自定义传感器属性（Custom Sensor Attributes）。


## 55.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P536_mmc56x3.h_源码浏览.md)
- [sensor_attribute_mmc56x3](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#gaf722f9a8bf8bae84c57aaa1ece387ad8)
- [SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b)
- [SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630)
- [SENSOR_ATTR_AUTOMATIC_SELF_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html#ggaf722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f)

<a id="header-details"></a>

---

[上一章](P054_zephyr__net__mld.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__mpipe__mpipe_fake_src.h_文件参考.md)
