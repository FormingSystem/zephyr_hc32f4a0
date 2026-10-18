---
id: learning.zephyr-docs.api-file-supplement-reference.page-47
title: zephyr__input__input_analog_axis_settings.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis__settings_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_input\_\_input\_analog\_axis\_settings.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__analog__axis__settings_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可保存模拟轴校准数据（Analog Axis Calibration Data）的API公共头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

可保存模拟轴校准数据（Analog Axis Calibration Data）的API公共头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.1\_函数（Functions）

<a id="r_ga56973ef7c7a465defdb7bd2934c86778"></a>

```c
int analog_axis_calibration_save (const struct device *dev)
```

相关声明：[analog_axis_calibration_save](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga56973ef7c7a465defdb7bd2934c86778)、[device](../device_reference/P002_设备对象结构.md)。

保存校准数据（Calibration Data）。


## 47.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P378_input_analog_axis_settings.h_源码浏览.md)
- [analog_axis_calibration_save](https://docs.zephyrproject.org/latest/doxygen/html/group__input__analog__axis.html#ga56973ef7c7a465defdb7bd2934c86778)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P046_zephyr__net__openthread.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__input__input_pat912x.h_文件参考.md)
