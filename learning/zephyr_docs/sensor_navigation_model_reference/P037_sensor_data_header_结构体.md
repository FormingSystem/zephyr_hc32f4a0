---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-37
title: sensor_data_header_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__data__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_sensor\_data\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__data__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

<a id="r_a1db93386466e8e4778f448ae0d8ca556"></a>

```c
uint64_t base_timestamp_ns
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[base_timestamp_ns](#a1db93386466e8e4778f448ae0d8ca556)。

通过 `k_uptime_ticks` 获取的、最接近第一帧生成时刻的时间戳。

<a id="r_ad31873d402a02842eb3098431591c151"></a>

```c
uint16_t reading_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reading_count](#ad31873d402a02842eb3098431591c151)。

`readings` 数组中的元素数量。

## 37.2\_详细说明（Detailed Documentation）

<a id="a1db93386466e8e4778f448ae0d8ca556"></a>

### `base_timestamp_ns`

```c
uint64_t sensor_data_header::base_timestamp_ns
```

通过 `k_uptime_ticks` 获取的、最接近第一帧生成时刻的时间戳。

<a id="ad31873d402a02842eb3098431591c151"></a>

### `reading_count`

```c
uint16_t sensor_data_header::reading_count
```

`readings` 数组中的元素数量。

此值必须至少为 1。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [k_uptime_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga8f143af2ee4ad42d9f7817ef161cbd13)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_sensor_data_generic_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_sensor_decode_context_结构体.md)
