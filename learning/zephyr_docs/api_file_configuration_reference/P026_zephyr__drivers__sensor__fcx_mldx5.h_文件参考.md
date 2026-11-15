---
id: learning.zephyr-docs.api-file-configuration-reference.page-26
title: zephyr__drivers__sensor__fcx_mldx5.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_drivers\_\_sensor\_\_fcx\_mldx5.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FCX-MLDX5传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

FCX-MLDX5传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.1\_枚举（Enumerations）

<a id="r_ga61852fad03f2a92a59a20cdc7bbbdd49"></a>

```c
enum sensor_attribute_fcx_mldx5 { SENSOR_ATTR_FCX_MLDX5_STATUS = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_FCX_MLDX5_RESET }
```

相关声明：[sensor_attribute_fcx_mldx5](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga61852fad03f2a92a59a20cdc7bbbdd49)、[SENSOR_ATTR_FCX_MLDX5_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7)、[SENSOR_ATTR_FCX_MLDX5_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585)。

FCX-MLDX5 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_ga413367eb7215e5c3e509e3cd039d37b1"></a>

```c
enum fcx_mldx5_status { FCX_MLDX5_STATUS_STANDBY = 2 , FCX_MLDX5_STATUS_RAMP_UP = 3 , FCX_MLDX5_STATUS_RUN = 4 , FCX_MLDX5_STATUS_ERROR = 5 , FCX_MLDX5_STATUS_UNKNOWN }
```

相关声明：[fcx_mldx5_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga413367eb7215e5c3e509e3cd039d37b1)、[FCX_MLDX5_STATUS_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00)、[FCX_MLDX5_STATUS_RAMP_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4)、[FCX_MLDX5_STATUS_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179)、[FCX_MLDX5_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540)、[FCX_MLDX5_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7)。

传感器状态（Sensor Status）。


## 26.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P256_fcx_mldx5.h_源码浏览.md)
- [sensor_attribute_fcx_mldx5](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga61852fad03f2a92a59a20cdc7bbbdd49)
- [SENSOR_ATTR_FCX_MLDX5_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7)
- [SENSOR_ATTR_FCX_MLDX5_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585)
- [fcx_mldx5_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga413367eb7215e5c3e509e3cd039d37b1)
- [FCX_MLDX5_STATUS_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00)
- [FCX_MLDX5_STATUS_RAMP_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4)
- [FCX_MLDX5_STATUS_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179)
- [FCX_MLDX5_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540)
- [FCX_MLDX5_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7)

<a id="header-details"></a>

---

[上一章](P025_zephyr__drivers__sensor__ens160.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__authentication__fido2__fido2_storage.h_文件参考.md)
