---
id: learning.zephyr-docs.audio-video-model-reference.page-58
title: video_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_video\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：视频（Video）驱动操作。

```c
#include <zephyr/drivers/video.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：视频（Video）驱动操作。这是每个视频驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a1859e3a1db99d97c38ea24f2f9cd00be"></a>

```c
video_api_format_t set_format
```

相关声明：[video_api_format_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga964b301e45a42aa78799a1d9c9297ab1)、[set_format](#a1859e3a1db99d97c38ea24f2f9cd00be)。

必需（REQ）：设置驱动的视频格式。

<a id="r_a8daefeec3cfc01de56f0168b32cdb640"></a>

```c
video_api_format_t get_format
```

相关声明：[video_api_format_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga964b301e45a42aa78799a1d9c9297ab1)、[get_format](#a8daefeec3cfc01de56f0168b32cdb640)。

必需（REQ）：获取驱动的视频格式。

<a id="r_adc08ef9eeeaac584c1b9ae5e6fb70c04"></a>

```c
video_api_set_stream_t set_stream
```

相关声明：[video_api_set_stream_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gacda90bacb17a53e0bd11e5bfd37be57a)、[set_stream](#adc08ef9eeeaac584c1b9ae5e6fb70c04)。

必需（REQ）：启动或停止视频驱动功能。

<a id="r_a6ab4deb345d2138e63e0c6126eeb5078"></a>

```c
video_api_get_caps_t get_caps
```

相关声明：[video_api_get_caps_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga070cb5f5bf35b98e2e7dda3378114780)、[get_caps](#a6ab4deb345d2138e63e0c6126eeb5078)。

必需（REQ）：获取视频驱动端点的能力。

<a id="r_a4762a3f103ca5999e3d3f790bb74af75"></a>

```c
video_api_enqueue_t enqueue
```

相关声明：[video_api_enqueue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gae6849a22140b3507bab219b579bc3d40)、[enqueue](#a4762a3f103ca5999e3d3f790bb74af75)。

可选（OPT）：将视频缓冲区交给驱动。

<a id="r_a96ba1bb4b76c7efc445b3071ef3a05ef"></a>

```c
video_api_dequeue_t dequeue
```

相关声明：[video_api_dequeue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga4265087c8faf62bbc36e88c0587022a1)、[dequeue](#a96ba1bb4b76c7efc445b3071ef3a05ef)。

可选（OPT）：从驱动中取出已出队的视频缓冲区。

<a id="r_a963927cc38174c4703470df04ec73dc6"></a>

```c
video_api_flush_t flush
```

相关声明：[video_api_flush_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga990ba001531c7300a06ca02d64c31eaa)、[flush](#a963927cc38174c4703470df04ec73dc6)。

可选（OPT）：清空驱动的端点缓冲区。

<a id="r_a41cd20fbb013bdb6b28d79822733695c"></a>

```c
video_api_ctrl_t set_ctrl
```

相关声明：[video_api_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga522b4027fc6f22bf59f4face3c97e303)、[set_ctrl](#a41cd20fbb013bdb6b28d79822733695c)。

可选（OPT）：设置驱动的视频控制项值。

<a id="r_af50329fd41db78f4c5a945f57a7c091e"></a>

```c
video_api_ctrl_t get_volatile_ctrl
```

相关声明：[video_api_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga522b4027fc6f22bf59f4face3c97e303)、[get_volatile_ctrl](#af50329fd41db78f4c5a945f57a7c091e)。

可选（OPT）：获取驱动的易变视频控制项（volatile video control）值。

<a id="r_a59dbaa93982c354c16d5de63c0d03ec2"></a>

```c
video_api_set_signal_t set_signal
```

相关声明：[video_api_set_signal_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gad5aacb1386785a3587d41844c7854f83)、[set_signal](#a59dbaa93982c354c16d5de63c0d03ec2)。

可选（OPT）：为视频端点注册或注销 `k_poll` 信号。

<a id="r_ac4b155a56c07bd8f7ecff9ec75dd0792"></a>

```c
video_api_frmival_t set_frmival
```

相关声明：[video_api_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gaf63180944041a9e934c9f7567bdc1b88)、[set_frmival](#ac4b155a56c07bd8f7ecff9ec75dd0792)。

可选（OPT）：向驱动应用视频帧间隔。

<a id="r_abddf2db6034d10f76ac90ed5974df788"></a>

```c
video_api_frmival_t get_frmival
```

相关声明：[video_api_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gaf63180944041a9e934c9f7567bdc1b88)、[get_frmival](#abddf2db6034d10f76ac90ed5974df788)。

可选（OPT）：获取驱动的视频帧间隔。

<a id="r_a6481a76f3f4d33629bbebb29ef9e8726"></a>

```c
video_api_enum_frmival_t enum_frmival
```

相关声明：[video_api_enum_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga026c9a4531a125339e69b81f75343555)、[enum_frmival](#a6481a76f3f4d33629bbebb29ef9e8726)。

可选（OPT）：列出视频帧间隔。

<a id="r_a800a2e8aaf59fc3fbd4bd2caaaf40f51"></a>

```c
video_api_selection_t set_selection
```

相关声明：[video_api_selection_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gab4d2eb34f8ccc95fa6dcda7848f4408a)、[set_selection](#a800a2e8aaf59fc3fbd4bd2caaaf40f51)。

可选（OPT）：设置视频选择区域（selection），用于裁剪或合成（crop/compose）。

<a id="r_a6ad8559ae0c2f6dc102e26e3714ded5d"></a>

```c
video_api_selection_t get_selection
```

相关声明：[video_api_selection_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gab4d2eb34f8ccc95fa6dcda7848f4408a)、[get_selection](#a6ad8559ae0c2f6dc102e26e3714ded5d)。

可选（OPT）：获取视频选择区域（selection），用于裁剪或合成（crop/compose）。

<a id="r_a0d35d1501b91f9c6116cf38f85a342cc"></a>

```c
video_api_transform_cap_t transform_cap
```

相关声明：[video_api_transform_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga0a9e2ed76720f172b1b668e79220e968)、[transform_cap](#a0d35d1501b91f9c6116cf38f85a342cc)。

可选（OPT）：将内存到内存（m2m）视频设备一端的视频格式能力变换到另一端。

## 58.2\_详细说明（Detailed Documentation）

<a id="a96ba1bb4b76c7efc445b3071ef3a05ef"></a>

### `dequeue`

```c
video_api_dequeue_t video_driver_api::dequeue
```

可选（OPT）：从驱动中取出已出队的视频缓冲区。

<a id="a4762a3f103ca5999e3d3f790bb74af75"></a>

### `enqueue`

```c
video_api_enqueue_t video_driver_api::enqueue
```

可选（OPT）：将视频缓冲区交给驱动。

<a id="a6481a76f3f4d33629bbebb29ef9e8726"></a>

### `enum_frmival`

```c
video_api_enum_frmival_t video_driver_api::enum_frmival
```

可选（OPT）：列出视频帧间隔。

<a id="a963927cc38174c4703470df04ec73dc6"></a>

### `flush`

```c
video_api_flush_t video_driver_api::flush
```

可选（OPT）：清空驱动的端点缓冲区。

<a id="a6ab4deb345d2138e63e0c6126eeb5078"></a>

### `get_caps`

```c
video_api_get_caps_t video_driver_api::get_caps
```

必需（REQ）：获取视频驱动端点的能力。

<a id="a8daefeec3cfc01de56f0168b32cdb640"></a>

### `get_format`

```c
video_api_format_t video_driver_api::get_format
```

必需（REQ）：获取驱动的视频格式。

<a id="abddf2db6034d10f76ac90ed5974df788"></a>

### `get_frmival`

```c
video_api_frmival_t video_driver_api::get_frmival
```

可选（OPT）：获取驱动的视频帧间隔。

<a id="a6ad8559ae0c2f6dc102e26e3714ded5d"></a>

### `get_selection`

```c
video_api_selection_t video_driver_api::get_selection
```

可选（OPT）：获取视频选择区域（selection），用于裁剪或合成（crop/compose）。

<a id="af50329fd41db78f4c5a945f57a7c091e"></a>

### `get_volatile_ctrl`

```c
video_api_ctrl_t video_driver_api::get_volatile_ctrl
```

可选（OPT）：获取驱动的易变视频控制项（volatile video control）值。

<a id="a41cd20fbb013bdb6b28d79822733695c"></a>

### `set_ctrl`

```c
video_api_ctrl_t video_driver_api::set_ctrl
```

可选（OPT）：设置驱动的视频控制项值。

<a id="a1859e3a1db99d97c38ea24f2f9cd00be"></a>

### `set_format`

```c
video_api_format_t video_driver_api::set_format
```

必需（REQ）：设置驱动的视频格式。

<a id="ac4b155a56c07bd8f7ecff9ec75dd0792"></a>

### `set_frmival`

```c
video_api_frmival_t video_driver_api::set_frmival
```

可选（OPT）：向驱动应用视频帧间隔。

<a id="a800a2e8aaf59fc3fbd4bd2caaaf40f51"></a>

### `set_selection`

```c
video_api_selection_t video_driver_api::set_selection
```

可选（OPT）：设置视频选择区域（selection），用于裁剪或合成（crop/compose）。

<a id="a59dbaa93982c354c16d5de63c0d03ec2"></a>

### `set_signal`

```c
video_api_set_signal_t video_driver_api::set_signal
```

可选（OPT）：为视频端点注册或注销 `k_poll` 信号。

<a id="adc08ef9eeeaac584c1b9ae5e6fb70c04"></a>

### `set_stream`

```c
video_api_set_stream_t video_driver_api::set_stream
```

必需（REQ）：启动或停止视频驱动功能。

<a id="a0d35d1501b91f9c6116cf38f85a342cc"></a>

### `transform_cap`

```c
video_api_transform_cap_t video_driver_api::transform_cap
```

可选（OPT）：将内存到内存（m2m）视频设备一端的视频格式能力变换到另一端。

本数据类型文档由以下文件生成：

- `zephyr/drivers/video.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h_source.html)
- [video_api_format_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga964b301e45a42aa78799a1d9c9297ab1)
- [video_api_set_stream_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gacda90bacb17a53e0bd11e5bfd37be57a)
- [video_api_get_caps_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga070cb5f5bf35b98e2e7dda3378114780)
- [video_api_enqueue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gae6849a22140b3507bab219b579bc3d40)
- [video_api_dequeue_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga4265087c8faf62bbc36e88c0587022a1)
- [video_api_flush_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga990ba001531c7300a06ca02d64c31eaa)
- [video_api_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga522b4027fc6f22bf59f4face3c97e303)
- [video_api_set_signal_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gad5aacb1386785a3587d41844c7854f83)
- [video_api_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gaf63180944041a9e934c9f7567bdc1b88)
- [video_api_enum_frmival_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga026c9a4531a125339e69b81f75343555)
- [video_api_selection_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#gab4d2eb34f8ccc95fa6dcda7848f4408a)
- [video_api_transform_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface__backend.html#ga0a9e2ed76720f172b1b668e79220e968)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_video_device_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_video_format_结构体.md)
