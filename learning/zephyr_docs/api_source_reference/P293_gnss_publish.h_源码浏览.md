---
id: learning.zephyr-docs.api-source-reference.page-293
title: gnss_publish.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第293章\_gnss\_publish.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h.html)。

## 293.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="agnss_8h_html"></a>
<a id="agroup__gnss__interface__backend_html_gad2d05fbf4073b71df054b025b65d51b1"></a>
<a id="agroup__gnss__interface__backend_html_gad55e06af3b36823b48d921df1852ad09"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructgnss__data_html"></a>
<a id="astructgnss__satellite_html"></a>

```c
/*
 * Copyright (c) 2023 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_GNSS_GNSS_H_
#define ZEPHYR_DRIVERS_GNSS_GNSS_H_

#include <zephyr/drivers/gnss.h>


void gnss_publish_data(const struct device *dev, const struct gnss_data *data);

void gnss_publish_satellites(const struct device *dev, const struct gnss_satellite *satellites,
                             uint16_t size);


#endif /* ZEPHYR_DRIVERS_GNSS_GNSS_H_ */
```

## 293.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_GNSS_GNSS_H_`。

## 293.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gnss__publish_8h.html)
- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)
- [gnss_publish_data](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad2d05fbf4073b71df054b025b65d51b1)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_data](../sensor_navigation_model_reference/P009_gnss_data_结构体.md)
- [gnss_publish_satellites](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad55e06af3b36823b48d921df1852ad09)
- [gnss_satellite](../sensor_navigation_model_reference/P015_gnss_satellite_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)

---

[上一章](P292_gnss_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P294_gnttab.h_源码浏览.md)
