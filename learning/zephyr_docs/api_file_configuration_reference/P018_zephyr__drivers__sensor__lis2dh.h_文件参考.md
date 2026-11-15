---
id: learning.zephyr-docs.api-file-configuration-reference.page-18
title: zephyr__drivers__sensor__lis2dh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_sensor\_\_lis2dh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2lis2dh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LIS2DH传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

LIS2DH传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.1\_枚举（Enumerations）

<a id="r_ga3a36ff9fb1f811eb0c1ac853f8c27ddb"></a>

```c
enum lis2dh_self_test { LIS2DH_SELF_TEST_DISABLE = 0 , LIS2DH_SELF_TEST_POSITIVE = 1 , LIS2DH_SELF_TEST_NEGATIVE = 2 }
```

相关声明：[lis2dh_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga3a36ff9fb1f811eb0c1ac853f8c27ddb)、[LIS2DH_SELF_TEST_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69)、[LIS2DH_SELF_TEST_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e)、[LIS2DH_SELF_TEST_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26)。

自定义属性（Custom Attribute）`SENSOR_ATTR_LIS2DH_SELF_TEST` 的可用值。

<a id="r_gaffedeefeb4d8ceda71760226eef1b5cd"></a>

```c
enum sensor_attribute_lis2dh { SENSOR_ATTR_LIS2DH_SELF_TEST = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_lis2dh](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gaffedeefeb4d8ceda71760226eef1b5cd)、[SENSOR_ATTR_LIS2DH_SELF_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6)。

LIS2DH 的自定义传感器属性（Custom Sensor Attributes）。


## 18.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P177_lis2dh.h_源码浏览.md)
- [lis2dh_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ga3a36ff9fb1f811eb0c1ac853f8c27ddb)
- [LIS2DH_SELF_TEST_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69)
- [LIS2DH_SELF_TEST_POSITIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e)
- [LIS2DH_SELF_TEST_NEGATIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26)
- [SENSOR_ATTR_LIS2DH_SELF_TEST](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6)
- [sensor_attribute_lis2dh](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html#gaffedeefeb4d8ceda71760226eef1b5cd)

<a id="header-details"></a>

---

[上一章](P017_zephyr__drivers__sensor__afbr_s50.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__sensor__lsm6dsvxxx.h_文件参考.md)
