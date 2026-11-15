---
id: learning.zephyr-docs.api-file-configuration-reference.page-68
title: zephyr__drivers__sensor__sgp40.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sgp40_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_zephyr\_\_drivers\_\_sensor\_\_sgp40.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sgp40_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SGP40传感器的扩展API头文件（Extended Sensor API Header）。

查看此文件的源码。

<a id="details"></a>

SGP40 传感器扩展应用程序编程接口（Extended Sensor API）的头文件。它公开 SGP40 的两个属性（Attributes），可用于设置片上温度和湿度补偿参数（On-Chip Temperature and Humidity Compensation Parameters）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 68.1\_枚举（Enumerations）

<a id="r_gae5259bb652233f89852c45961f58faa9"></a>

```c
enum sensor_attribute_sgp40 { SENSOR_ATTR_SGP40_TEMPERATURE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SGP40_HUMIDITY }
```

相关声明：[sensor_attribute_sgp40](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#gae5259bb652233f89852c45961f58faa9)、[SENSOR_ATTR_SGP40_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#ggae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419)、[SENSOR_ATTR_SGP40_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#ggae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3)。

SGP40 的自定义传感器属性（Custom Sensor Attributes）。


## 68.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P779_sgp40.h_源码浏览.md)
- [sensor_attribute_sgp40](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#gae5259bb652233f89852c45961f58faa9)
- [SENSOR_ATTR_SGP40_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#ggae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419)
- [SENSOR_ATTR_SGP40_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html#ggae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3)

<a id="header-details"></a>

---

[上一章](P067_zephyr__dt-bindings__gpio__semtech-sx1509b.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P069_zephyr__mgmt__ec_host_cmd__simulator.h_文件参考.md)
