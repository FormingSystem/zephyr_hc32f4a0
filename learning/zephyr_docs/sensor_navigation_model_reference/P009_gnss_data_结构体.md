---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-9
title: gnss_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_gnss\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全球导航卫星系统（GNSS）的数据结构。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

全球导航卫星系统（GNSS）的数据结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a2470031921179cb30172441163d80052"></a>

```c
struct navigation_data nav_data
```

相关声明：[navigation_data](P018_navigation_data_结构体.md)、[nav_data](#a2470031921179cb30172441163d80052)。

采集到的导航数据（Navigation data）。

<a id="r_a78155e6d2c981b9121b2ee42c1700988"></a>

```c
struct gnss_info info
```

相关声明：[gnss_info](P012_gnss_info_结构体.md)、[info](#a78155e6d2c981b9121b2ee42c1700988)。

采集导航数据时的全球导航卫星系统（GNSS）信息。

<a id="r_ae6bfc0c6a53901963a1d20bad025fb99"></a>

```c
struct gnss_time utc
```

相关声明：[gnss_time](P017_gnss_time_结构体.md)、[utc](#ae6bfc0c6a53901963a1d20bad025fb99)。

采集数据时的协调世界时（UTC）。

## 9.2\_详细说明（Detailed Documentation）

<a id="a78155e6d2c981b9121b2ee42c1700988"></a>

### `info`

```c
struct gnss_info gnss_data::info
```

采集导航数据时的全球导航卫星系统（GNSS）信息。

<a id="a2470031921179cb30172441163d80052"></a>

### `nav_data`

```c
struct navigation_data gnss_data::nav_data
```

采集到的导航数据（Navigation data）。

<a id="ae6bfc0c6a53901963a1d20bad025fb99"></a>

### `utc`

```c
struct gnss_time gnss_data::utc
```

采集数据时的协调世界时（UTC）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [navigation_data](P018_navigation_data_结构体.md)
- [gnss_info](P012_gnss_info_结构体.md)
- [gnss_time](P017_gnss_time_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_ft8xx_touch_transform_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_gnss_data_callback_结构体.md)
