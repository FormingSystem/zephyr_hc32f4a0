---
id: learning.zephyr-docs.api-file-configuration-reference.page-58
title: zephyr__data__navigation.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_zephyr\_\_data\_\_navigation.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

导航数据结构（Navigation Data Structures）的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

导航数据结构（Navigation Data Structures）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 58.1\_数据结构（Data Structures）

<a id="r_navigation_5Fdata"></a>

```c
struct navigation_data
```

相关声明：[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

导航数据结构（Navigation Data Structure）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 58.2\_函数（Functions）

<a id="r_ga99b3460548c6e88cb16391ba77303829"></a>

```c
int navigation_distance (uint64_t *distance, const struct navigation_data *p1, const struct navigation_data *p2)
```

相关声明：[navigation_distance](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga99b3460548c6e88cb16391ba77303829)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

沿两个导航点（Navigation Points）所属球体的表面，计算两点之间的距离（Distance）。

<a id="r_ga36655c6a733ba4e96cc6bfd055a0bf8b"></a>

```c
int navigation_bearing (uint32_t *bearing, const struct navigation_data *from, const struct navigation_data *to)
```

相关声明：[navigation_bearing](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga36655c6a733ba4e96cc6bfd055a0bf8b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

计算从一个导航点（Navigation Point）到另一个导航点的方位角（Bearing）。


## 58.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P572_navigation.h_源码浏览.md)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [navigation_distance](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga99b3460548c6e88cb16391ba77303829)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [navigation_bearing](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga36655c6a733ba4e96cc6bfd055a0bf8b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P057_zephyr__mpipe__mpipe_workqueue.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P059_zephyr__net__net_stats.h_文件参考.md)
