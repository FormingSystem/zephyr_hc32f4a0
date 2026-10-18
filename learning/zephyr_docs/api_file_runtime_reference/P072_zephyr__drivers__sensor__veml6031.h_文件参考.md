---
id: learning.zephyr-docs.api-file-runtime-reference.page-72
title: zephyr__drivers__sensor__veml6031.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veml6031_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_zephyr\_\_drivers\_\_sensor\_\_veml6031.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/veml6031_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

VEML6031传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

查看此文件的源码。

VEML6031传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 72.1\_宏定义（Macros）

<a id="r_ad04dceaadb7305673e301d0ab50fcfb1"></a>

```c
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6031_H_
```

相关声明：[ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6031_H_](#ad04dceaadb7305673e301d0ab50fcfb1)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 72.2\_枚举（Enumerations）

<a id="r_ga8fdeb1ef880fb5a03c121f8d6456a738"></a>

```c
enum veml6031_div4 { VEML6031_SIZE_4_4 = 0x00 , VEML6031_SIZE_1_4 = 0x01 }
```

相关声明：[veml6031_div4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ga8fdeb1ef880fb5a03c121f8d6456a738)、[VEML6031_SIZE_4_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gga8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022)、[VEML6031_SIZE_1_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gga8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3)。

VEML6031 环境光测量（Ambient Light Measurements）的尺寸选项（Size Options）。

<a id="r_gae442c85062217115e03dcebf4fb3cacc"></a>

```c
enum sensor_attribute_veml6031 { SENSOR_ATTR_VEML6031_IT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEML6031_DIV4 , SENSOR_ATTR_VEML6031_GAIN , SENSOR_ATTR_VEML6031_PERS }
```

相关声明：[sensor_attribute_veml6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gae442c85062217115e03dcebf4fb3cacc)、[SENSOR_ATTR_VEML6031_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80)、[SENSOR_ATTR_VEML6031_DIV4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c)、[SENSOR_ATTR_VEML6031_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a)、[SENSOR_ATTR_VEML6031_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07)。

VEML6031 传感器的自定义属性（Custom Sensor Attributes）。

<a id="r_gaf62d29159c2a40cbd8cd1e3d7522afb9"></a>

```c
enum sensor_channel_veml6031 { SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VEML6031_IR_RAW_COUNTS }
```

相关声明：[sensor_channel_veml6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gaf62d29159c2a40cbd8cd1e3d7522afb9)、[SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggaf62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d)、[SENSOR_CHAN_VEML6031_IR_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggaf62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65)。

VEML6031 传感器的自定义通道（Custom Sensor Channels）。

## 72.3\_详细说明（Detailed Documentation）

<a id="ad04dceaadb7305673e301d0ab50fcfb1"></a>

### `ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6031_H_`

```c
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6031_H_
```


## 72.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/veml60xx-common.h](https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P904_veml6031.h_源码浏览.md)
- [veml6031_div4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ga8fdeb1ef880fb5a03c121f8d6456a738)
- [VEML6031_SIZE_4_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gga8fdeb1ef880fb5a03c121f8d6456a738a42ddf6981430a245dbeac297a125f022)
- [VEML6031_SIZE_1_4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gga8fdeb1ef880fb5a03c121f8d6456a738a761d4cb4dfbf7678f2ea6587e24474c3)
- [sensor_attribute_veml6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gae442c85062217115e03dcebf4fb3cacc)
- [SENSOR_ATTR_VEML6031_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3cacca413d3609d2a3c20959d5aa48ae542e80)
- [SENSOR_ATTR_VEML6031_DIV4](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3cacca1a103d0756ba6235e9bdc56e5f4ee68c)
- [SENSOR_ATTR_VEML6031_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3caccaed21ce91c964265a40b0e6ed7395e67a)
- [SENSOR_ATTR_VEML6031_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggae442c85062217115e03dcebf4fb3caccae4c3adafe31112e0ea708ab9e1cf8a07)
- [sensor_channel_veml6031](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#gaf62d29159c2a40cbd8cd1e3d7522afb9)
- [SENSOR_CHAN_VEML6031_ALS_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggaf62d29159c2a40cbd8cd1e3d7522afb9a778749581356d6568c03aa510a36370d)
- [SENSOR_CHAN_VEML6031_IR_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6031__interface.html#ggaf62d29159c2a40cbd8cd1e3d7522afb9ac2834dbc5ba2a39d86461b34d5e06e65)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P071_zephyr__drivers__sensor__tmp451.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P073_zephyr__drivers__sensor__veml6046.h_文件参考.md)
