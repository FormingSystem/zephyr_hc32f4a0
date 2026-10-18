---
id: learning.zephyr-docs.api-file-configuration-reference.page-11
title: zephyr__drivers__sensor__bmm350.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bmm350_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_sensor\_\_bmm350.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bmm350_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BMM350传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

BMM350传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_bmm350_5Fself_5Ftest_5Fresult"></a>

```c
struct bmm350_self_test_result
```

相关声明：[bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)。

BMM350 用户自检结果（User Self-test Result）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_ga48fad26fc2836975d1fddc7ae7b167b0"></a>

```c
int bmm350_self_test (const struct device *dev, struct bmm350_self_test_result *result)
```

相关声明：[bmm350_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html#ga48fad26fc2836975d1fddc7ae7b167b0)、[device](../device_reference/P002_设备对象结构.md)、[bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)。

运行 BMM350 内置用户自检（Built-In User Self-Test）。

<a id="r_ga482a53ae8c68a549e1436215cbc47302"></a>

```c
int bmm350_magnetic_reset (const struct device *dev)
```

相关声明：[bmm350_magnetic_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html#ga482a53ae8c68a549e1436215cbc47302)、[device](../device_reference/P002_设备对象结构.md)。

执行磁复位（Magnetic Reset）。


## 11.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P074_bmm350.h_源码浏览.md)
- [bmm350_self_test_result](../driver_model_reference/P031_BMM350自检结果.md)
- [bmm350_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html#ga48fad26fc2836975d1fddc7ae7b167b0)
- [device](../device_reference/P002_设备对象结构.md)
- [bmm350_magnetic_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bmm350__interface.html#ga482a53ae8c68a549e1436215cbc47302)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__dma__atmel_samx7x_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__net__coap_link_format.h_文件参考.md)
