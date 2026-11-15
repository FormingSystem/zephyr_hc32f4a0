---
id: learning.zephyr-docs.api-file-supplement-reference.page-70
title: zephyr__drivers__sensor__mlx90394.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mlx90394_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_zephyr\_\_drivers\_\_sensor\_\_mlx90394.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mlx90394_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MLX90394传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

MLX90394传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 70.1\_枚举（Enumerations）

<a id="r_gad3f71775143081e44d323e3886617e3f"></a>

```c
enum mlx90394_sensor_attribute { MLX90394_SENSOR_ATTR_MAGN_LOW_NOISE = SENSOR_ATTR_PRIV_START , MLX90394_SENSOR_ATTR_MAGN_FILTER_XY , MLX90394_SENSOR_ATTR_MAGN_FILTER_Z , MLX90394_SENSOR_ATTR_MAGN_OSR , MLX90394_SENSOR_ATTR_TEMP_FILTER , MLX90394_SENSOR_ATTR_TEMP_OSR }
```

相关声明：[mlx90394_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#gad3f71775143081e44d323e3886617e3f)、[MLX90394_SENSOR_ATTR_MAGN_LOW_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa8d57f0f77e31edd3d9d1c3610f31ee93)、[MLX90394_SENSOR_ATTR_MAGN_FILTER_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa9b0e8eab5d12fa2bd32114d6453f1908)、[MLX90394_SENSOR_ATTR_MAGN_FILTER_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3faa3f86f83470b4936876aa0b42a881228)、[MLX90394_SENSOR_ATTR_MAGN_OSR](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa7c6e652d6f49f5aa6c4f7a56cb7427f0)、[MLX90394_SENSOR_ATTR_TEMP_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa4a594a201de0d6a147697f57797efa27)、[MLX90394_SENSOR_ATTR_TEMP_OSR](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fafcf90d5b6495cc754307a0b021b5cd0b)。

MLX90394 的自定义传感器属性（Custom Sensor Attributes）。


## 70.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P534_mlx90394.h_源码浏览.md)
- [mlx90394_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#gad3f71775143081e44d323e3886617e3f)
- [MLX90394_SENSOR_ATTR_MAGN_LOW_NOISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa8d57f0f77e31edd3d9d1c3610f31ee93)
- [MLX90394_SENSOR_ATTR_MAGN_FILTER_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa9b0e8eab5d12fa2bd32114d6453f1908)
- [MLX90394_SENSOR_ATTR_MAGN_FILTER_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3faa3f86f83470b4936876aa0b42a881228)
- [MLX90394_SENSOR_ATTR_MAGN_OSR](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa7c6e652d6f49f5aa6c4f7a56cb7427f0)
- [MLX90394_SENSOR_ATTR_TEMP_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fa4a594a201de0d6a147697f57797efa27)
- [MLX90394_SENSOR_ATTR_TEMP_OSR](https://docs.zephyrproject.org/latest/doxygen/html/group__mlx90394__interface.html#ggad3f71775143081e44d323e3886617e3fafcf90d5b6495cc754307a0b021b5cd0b)

<a id="header-details"></a>

---

[上一章](P069_zephyr__drivers__sensor__mhz19b.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P071_zephyr__modem__ubx__protocol.h_文件参考.md)
