---
id: learning.zephyr-docs.api-protocol-topic-reference.page-39
title: 导航（Navigation）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_导航（Navigation）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

导航工具。

<a id="details"></a>

导航工具。

<a id="header-files"></a>
<a id="files"></a>

## 39.1\_文件（Files）

<a id="r_navigation_2Eh"></a>

```c
file navigation.h
```

相关声明：[navigation.h](../api_file_configuration_reference/P058_zephyr__data__navigation.h_文件参考.md)。

导航数据结构（Navigation Data Structures）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 39.2\_数据结构（Data Structures）

<a id="r_navigation_5Fdata"></a>

```c
struct navigation_data
```

相关声明：[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

导航数据结构（Navigation Data Structure）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.3\_函数（Functions）

<a id="r_ga99b3460548c6e88cb16391ba77303829"></a>

```c
int navigation_distance (uint64_t *distance, const struct navigation_data *p1, const struct navigation_data *p2)
```

相关声明：[navigation_distance](#ga99b3460548c6e88cb16391ba77303829)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

沿两个导航点（Navigation Points）所属球体的表面，计算两点之间的距离（Distance）。

<a id="r_ga36655c6a733ba4e96cc6bfd055a0bf8b"></a>

```c
int navigation_bearing (uint32_t *bearing, const struct navigation_data *from, const struct navigation_data *to)
```

相关声明：[navigation_bearing](#ga36655c6a733ba4e96cc6bfd055a0bf8b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)、[navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)。

计算从一个导航点（Navigation Point）到另一个导航点的方位角（Bearing）。

## 39.4\_详细说明（Detailed Documentation）

<a id="ga36655c6a733ba4e96cc6bfd055a0bf8b"></a>

### `navigation_bearing()`

```c
int navigation_bearing ( uint32_t * bearing, const struct navigation_data * from, const struct navigation_data * to )
```

```c
#include <zephyr/data/navigation.h>
```

计算从一个导航点（Navigation Point）到另一个导航点的方位角（Bearing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bearing` | 用于存储计算所得方位角（bearing angle）的目标位置，单位为毫度。 |
| `from` | 第一个导航点（navigation point）。 |
| `to` | 第二个导航点。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 任一导航点无效。 |

<a id="ga99b3460548c6e88cb16391ba77303829"></a>

### `navigation_distance()`

```c
int navigation_distance ( uint64_t * distance, const struct navigation_data * p1, const struct navigation_data * p2 )
```

```c
#include <zephyr/data/navigation.h>
```

沿两个导航点（Navigation Points）所属球体的表面，计算两点之间的距离（Distance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `distance` | 用于存储计算所得距离的目标位置，单位为毫米。 |
| `p1` | 第一个导航点（navigation point）。 |
| `p2` | 第二个导航点。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 任一导航点无效。 |


## 39.5\_原页交叉引用（Cross References）

- [navigation.h](../api_file_configuration_reference/P058_zephyr__data__navigation.h_文件参考.md)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P038_IPv4 网络地址转换（Network Address Translation）.md) · [返回大纲](大纲.md) · [下一章](P040_网络二层抽象层（Network L2 Abstraction Layer）.md)
