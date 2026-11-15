---
id: learning.zephyr-docs.api-file-supplement-reference.page-23
title: zephyr__drivers__sensor__npm10xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_sensor\_\_npm10xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nordic nPM10系列电源管理集成电路（PMIC）传感器驱动的自定义通道和属性。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

Nordic nPM10系列电源管理集成电路（PMIC）传感器驱动的自定义通道和属性。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 23.1\_枚举（Enumerations）

<a id="r_ga5d1bad2f8fe96e651b5637ff59009cab"></a>

```c
enum npm10xx_sensor_chan { NPM10XX_SENSOR_CHAN_VSYS = SENSOR_CHAN_PRIV_START , NPM10XX_SENSOR_CHAN_VBUS , NPM10XX_SENSOR_CHAN_OFFSET }
```

相关声明：[npm10xx_sensor_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#ga5d1bad2f8fe96e651b5637ff59009cab)、[NPM10XX_SENSOR_CHAN_VSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a)、[NPM10XX_SENSOR_CHAN_VBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa)、[NPM10XX_SENSOR_CHAN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18)。

nPM10xx 电源管理芯片传感器（PMIC Sensor）的自定义通道（Custom Channels）。


## 23.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P180_npm10xx.h_源码浏览.md)
- [npm10xx_sensor_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#ga5d1bad2f8fe96e651b5637ff59009cab)
- [NPM10XX_SENSOR_CHAN_VSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a)
- [NPM10XX_SENSOR_CHAN_VBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa)
- [NPM10XX_SENSOR_CHAN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18)

<a id="header-details"></a>

---

[上一章](P022_zephyr__drivers__dma__dma_xilinx_adma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__net__dummy.h_文件参考.md)
