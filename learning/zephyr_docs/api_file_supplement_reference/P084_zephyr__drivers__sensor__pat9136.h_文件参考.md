---
id: learning.zephyr-docs.api-file-supplement-reference.page-84
title: zephyr__drivers__sensor__pat9136.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pat9136_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_zephyr\_\_drivers\_\_sensor\_\_pat9136.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pat9136_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAT9136传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

PAT9136传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 84.1\_枚举（Enumerations）

<a id="r_ga6e9d013c0dc687f05c27dc907bb56c65"></a>

```c
enum sensor_channel_pat9136 { SENSOR_CHAN_POS_DX_MM = SENSOR_CHAN_PRIV_START + 1 , SENSOR_CHAN_POS_DY_MM , SENSOR_CHAN_POS_DXYZ_MM = SENSOR_CHAN_POS_DY_MM + 2 }
```

相关声明：[sensor_channel_pat9136](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#ga6e9d013c0dc687f05c27dc907bb56c65)、[SENSOR_CHAN_POS_DX_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65a9ba6c90758d4c7565e0aa785da00c953)、[SENSOR_CHAN_POS_DY_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba)、[SENSOR_CHAN_POS_DXYZ_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65aa0b2726e0262199b579c5bb66d542e70)。

PAT9136 的自定义传感器通道（Custom Sensor Channels）。


## 84.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P643_pat9136.h_源码浏览.md)
- [sensor_channel_pat9136](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#ga6e9d013c0dc687f05c27dc907bb56c65)
- [SENSOR_CHAN_POS_DX_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65a9ba6c90758d4c7565e0aa785da00c953)
- [SENSOR_CHAN_POS_DY_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65a12172a3b5c7d79da0f5ee8305c7837ba)
- [SENSOR_CHAN_POS_DXYZ_MM](https://docs.zephyrproject.org/latest/doxygen/html/group__pat9136__interface.html#gga6e9d013c0dc687f05c27dc907bb56c65aa0b2726e0262199b579c5bb66d542e70)

<a id="header-details"></a>

---

[上一章](P083_zephyr__dt-bindings__flash_controller__ospi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P085_zephyr__dt-bindings__pinctrl__renesas__pinctrl-r8a779g0.h_文件参考.md)
