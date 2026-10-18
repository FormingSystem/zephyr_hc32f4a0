---
id: learning.zephyr-docs.api-file-configuration-reference.page-33
title: zephyr__drivers__gnss__gnss_publish.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_drivers\_\_gnss\_\_gnss\_publish.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于发布数据和卫星信息的GNSS驱动后端辅助接口（Backend Helpers）。

<a id="details"></a>

```c
#include <zephyr/drivers/gnss.h>
```

查看此文件的源码。

用于发布数据和卫星信息的GNSS驱动后端辅助接口（Backend Helpers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.1\_函数（Functions）

<a id="func-members-0"></a>

<a id="r_gad2d05fbf4073b71df054b025b65d51b1"></a>

```c
void gnss_publish_data (const struct device *dev, const struct gnss_data *data)
```

相关声明：[gnss_publish_data](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad2d05fbf4073b71df054b025b65d51b1)、[device](../device_reference/P002_设备对象结构.md)、[gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)。

向已注册的回调（Callbacks）发布全球导航卫星系统数据（GNSS Data）。

<a id="r_gad55e06af3b36823b48d921df1852ad09"></a>

```c
void gnss_publish_satellites (const struct device *dev, const struct gnss_satellite *satellites, uint16_t size)
```

相关声明：[gnss_publish_satellites](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad55e06af3b36823b48d921df1852ad09)、[device](../device_reference/P002_设备对象结构.md)、[gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向已注册的回调（Callbacks）发布全球导航卫星系统卫星信息（GNSS Satellite Information）。


## 33.2\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](../api_source_reference/P291_gnss.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P293_gnss_publish.h_源码浏览.md)
- [gnss_publish_data](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad2d05fbf4073b71df054b025b65d51b1)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [gnss_publish_satellites](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad55e06af3b36823b48d921df1852ad09)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P032_zephyr__drivers__sensor__generic_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__drivers__gpio__gpio_sx1509b.h_文件参考.md)
