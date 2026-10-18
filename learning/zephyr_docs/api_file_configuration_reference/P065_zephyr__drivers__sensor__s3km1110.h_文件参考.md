---
id: learning.zephyr-docs.api-file-configuration-reference.page-65
title: zephyr__drivers__sensor__s3km1110.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/s3km1110_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_zephyr\_\_drivers\_\_sensor\_\_s3km1110.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/s3km1110_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Iclegend S3KM1110传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

Iclegend S3KM1110传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 65.1\_枚举（Enumerations）

<a id="r_ga490cac4394a0d2dce5c095eaf1b9a207"></a>

```c
enum s3km1110_target_status { S3KM1110_TARGET_NO_TARGET = 0x00 , S3KM1110_TARGET_MOVING = 0x01 , S3KM1110_TARGET_STATIC = 0x02 , S3KM1110_TARGET_BOTH = 0x03 , S3KM1110_TARGET_ERROR = 0x04 }
```

相关声明：[s3km1110_target_status](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#ga490cac4394a0d2dce5c095eaf1b9a207)、[S3KM1110_TARGET_NO_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207a8c6ca499099aeda4fc310b90f1355869)、[S3KM1110_TARGET_MOVING](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aef0844ec3aeefb0049ed40bc78bc640e)、[S3KM1110_TARGET_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aeb01dab2ad8f7d2f54fca829b610a36d)、[S3KM1110_TARGET_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207a22fda04d1d3d1c204f724a9f15c32465)、[S3KM1110_TARGET_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aad1c636614b9b5a03af1ae924d5cd062)。

S3KM1110 报告的雷达目标状态值（Radar Target Status Values）。

<a id="r_ga246184cf5aba644fdefa52d7eea07ee5"></a>

```c
enum sensor_channel_s3km1110 { SENSOR_CHAN_S3KM1110_TARGET_STATUS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_S3KM1110_MOVING_DISTANCE , SENSOR_CHAN_S3KM1110_STATIC_DISTANCE , SENSOR_CHAN_S3KM1110_MOVING_ENERGY , SENSOR_CHAN_S3KM1110_STATIC_ENERGY }
```

相关声明：[sensor_channel_s3km1110](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#ga246184cf5aba644fdefa52d7eea07ee5)、[SENSOR_CHAN_S3KM1110_TARGET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a62d06b042d9e07e302ce21b6b48e80c1)、[SENSOR_CHAN_S3KM1110_MOVING_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a49aeaaf493be20cd2ac70666344259a1)、[SENSOR_CHAN_S3KM1110_STATIC_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a5e9c481a82e32ffdc28f80558d2e9ee5)、[SENSOR_CHAN_S3KM1110_MOVING_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a2318a4db392087b678b04ce63f829ae9)、[SENSOR_CHAN_S3KM1110_STATIC_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a16ee99536316fc8d26186fe4e6634f3d)。

S3KM1110 的自定义传感器通道（Custom Sensor Channels）。


## 65.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P744_s3km1110.h_源码浏览.md)
- [s3km1110_target_status](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#ga490cac4394a0d2dce5c095eaf1b9a207)
- [S3KM1110_TARGET_NO_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207a8c6ca499099aeda4fc310b90f1355869)
- [S3KM1110_TARGET_MOVING](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aef0844ec3aeefb0049ed40bc78bc640e)
- [S3KM1110_TARGET_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aeb01dab2ad8f7d2f54fca829b610a36d)
- [S3KM1110_TARGET_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207a22fda04d1d3d1c204f724a9f15c32465)
- [S3KM1110_TARGET_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga490cac4394a0d2dce5c095eaf1b9a207aad1c636614b9b5a03af1ae924d5cd062)
- [sensor_channel_s3km1110](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#ga246184cf5aba644fdefa52d7eea07ee5)
- [SENSOR_CHAN_S3KM1110_TARGET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a62d06b042d9e07e302ce21b6b48e80c1)
- [SENSOR_CHAN_S3KM1110_MOVING_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a49aeaaf493be20cd2ac70666344259a1)
- [SENSOR_CHAN_S3KM1110_STATIC_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a5e9c481a82e32ffdc28f80558d2e9ee5)
- [SENSOR_CHAN_S3KM1110_MOVING_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a2318a4db392087b678b04ce63f829ae9)
- [SENSOR_CHAN_S3KM1110_STATIC_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html#gga246184cf5aba644fdefa52d7eea07ee5a16ee99536316fc8d26186fe4e6634f3d)

<a id="header-details"></a>

---

[上一章](P064_zephyr__dt-bindings__clock__renesas_rzv_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P066_zephyr__drivers__disk__sdmmc_stm32.h_文件参考.md)
