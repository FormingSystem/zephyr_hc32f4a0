---
id: learning.zephyr-docs.api-device-topic-reference.page-23
title: 视频流（Video Stream）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_视频流（Video Stream）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__stream.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频流状态控制。

<a id="details"></a>

视频流状态控制。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.1\_函数（Functions）

<a id="r_gaa4d62da5137d0392ce8a19f794478610"></a>

```c
int video_stream_start (const struct device *dev, enum video_buf_type type)
```

相关声明：[video_stream_start](#gaa4d62da5137d0392ce8a19f794478610)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)。

启动视频设备功能（video device function）。

<a id="r_ga77c694bfc3ff8d51a5a74dcd211b2563"></a>

```c
int video_stream_stop (const struct device *dev, enum video_buf_type type)
```

相关声明：[video_stream_stop](#ga77c694bfc3ff8d51a5a74dcd211b2563)、[device](../device_reference/P002_设备对象结构.md)、[video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)。

停止视频设备功能。

## 23.2\_详细说明（Detailed Documentation）

<a id="gaa4d62da5137d0392ce8a19f794478610"></a>

### `video_stream_start()`

```c
int video_stream_start ( const struct device * dev, enum video_buf_type type )
```

```c
#include <zephyr/video/video.h>
```

启动视频设备功能（video device function）。

调用 `video_stream_start` 以进入流式传输状态（streaming），例如采集或输出。调用 `video_stream_start` 之前，驱动可能已通过 `video_enqueue()` 收到缓冲区。如果驱动／设备需要达到最少缓冲区数量才能开始流式传输，驱动就会在相关端点能力（endpoint capabilities）中设置 `min_vbuf_count`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `type` | 要启动的缓冲区流类型。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（invalid parameters）。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga77c694bfc3ff8d51a5a74dcd211b2563"></a>

### `video_stream_stop()`

```c
int video_stream_stop ( const struct device * dev, enum video_buf_type type )
```

```c
#include <zephyr/video/video.h>
```

停止视频设备功能。

执行 `video_stream_stop` 时，驱动必须停止所有事务（transactions），或等待它们完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `type` | 要停止的缓冲区流类型。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（invalid parameters）。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |


## 23.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [video_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__video__types.html#gad386b2994b56844ebe713f156b9dfe4e)
- [zephyr/video/video.h](https://docs.zephyrproject.org/latest/doxygen/html/video_2video_8h.html)
- [video_enqueue()](https://docs.zephyrproject.org/latest/doxygen/html/group__video__api__buffers.html#ga036c42c1e7dbaa97eb2789dfc3a3c1d7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_传感器坐标轴对齐（Sensor axis alignment）.md) · [返回大纲](大纲.md) · [下一章](P024_视频接口总线类型（Video interface bus types）.md)
