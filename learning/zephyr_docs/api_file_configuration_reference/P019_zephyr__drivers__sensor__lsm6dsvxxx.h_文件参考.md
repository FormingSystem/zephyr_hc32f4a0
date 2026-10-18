---
id: learning.zephyr-docs.api-file-configuration-reference.page-19
title: zephyr__drivers__sensor__lsm6dsvxxx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_sensor\_\_lsm6dsvxxx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lsm6dsvxxx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LSM6DSVXXX传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

LSM6DSVXXX传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.1\_枚举（Enumerations）

<a id="r_gaa40abf78652db54d4b43b41c7750b558"></a>

```c
enum sensor_attribute_lsm6dsvxxx { SENSOR_ATTR_GET_SELF_TEST_RESULT = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_lsm6dsvxxx](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa40abf78652db54d4b43b41c7750b558)、[SENSOR_ATTR_GET_SELF_TEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d)。

LSM6DSVXXX 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_ga0e2d73310764e4ad782f20f9e2b2da46"></a>

```c
enum lsm6dsvxxx_self_test_result { LSM6DSVXXX_ST_OK = 0 , LSM6DSVXXX_ST_FAIL = 1 }
```

相关声明：[lsm6dsvxxx_self_test_result](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0e2d73310764e4ad782f20f9e2b2da46)、[LSM6DSVXXX_ST_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349)、[LSM6DSVXXX_ST_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36)。

LSM6DSVXXX 的自检结果（Self-Test Result）。


## 19.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P178_lsm6dsvxxx.h_源码浏览.md)
- [sensor_attribute_lsm6dsvxxx](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gaa40abf78652db54d4b43b41c7750b558)
- [SENSOR_ATTR_GET_SELF_TEST_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ggaa40abf78652db54d4b43b41c7750b558a3b1d8afe96e306670568008d1f8b5a5d)
- [lsm6dsvxxx_self_test_result](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#ga0e2d73310764e4ad782f20f9e2b2da46)
- [LSM6DSVXXX_ST_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a01c6e9bb517b46bd18e2d69b1eb02349)
- [LSM6DSVXXX_ST_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html#gga0e2d73310764e4ad782f20f9e2b2da46a18d5155644c60de23dde8bf2ca3f5a36)

<a id="header-details"></a>

---

[上一章](P018_zephyr__drivers__sensor__lis2dh.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__dt-bindings__dma__dma_smartbond.h_文件参考.md)
