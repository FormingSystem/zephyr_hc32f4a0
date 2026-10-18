---
id: learning.zephyr-docs.audio-video-model-reference.page-7
title: dmic_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdmic__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_dmic\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdmic__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：数字麦克风（Digital Microphone）驱动操作。

```c
#include <zephyr/audio/dmic.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：数字麦克风（Digital Microphone）驱动操作。这是每个数字麦克风驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a58d828a7da4feb293b5805f62b30ea78"></a>

```c
dmic_configure_t configure
```

相关声明：[dmic_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gaf8f2d714a8e93df2178b19ba46533909)、[configure](#a58d828a7da4feb293b5805f62b30ea78)。

必需（REQ）：配置 DMIC 驱动及控制器，可涉及多个控制器。

<a id="r_add04e9c034726b05d8e02681be04ddb5"></a>

```c
dmic_trigger_t trigger
```

相关声明：[dmic_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#ga777e407deafee37c7f26039dd3144c4a)、[trigger](#add04e9c034726b05d8e02681be04ddb5)。

必需（REQ）：DMIC 驱动触发命令。

<a id="r_ac6cf5dd47f26ba6fe555969d6a724a4a"></a>

```c
dmic_read_t read
```

相关声明：[dmic_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gab53ad4a4dddc12cdc7d012774f0ef63a)、[read](#ac6cf5dd47f26ba6fe555969d6a724a4a)。

必需（REQ）：读取接收到的、已抽取的脉冲编码调制（PCM）数据流。

## 7.2\_详细说明（Detailed Documentation）

<a id="a58d828a7da4feb293b5805f62b30ea78"></a>

### `configure`

```c
dmic_configure_t dmic_driver_api::configure
```

必需（REQ）：配置 DMIC 驱动及控制器，可涉及多个控制器。

<a id="ac6cf5dd47f26ba6fe555969d6a724a4a"></a>

### `read`

```c
dmic_read_t dmic_driver_api::read
```

必需（REQ）：读取接收到的、已抽取的脉冲编码调制（PCM）数据流。

<a id="add04e9c034726b05d8e02681be04ddb5"></a>

### `trigger`

```c
dmic_trigger_t dmic_driver_api::trigger
```

必需（REQ）：DMIC 驱动触发命令。

本数据类型文档由以下文件生成：

- `zephyr/audio/dmic.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/audio/dmic.h](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)
- [dmic_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gaf8f2d714a8e93df2178b19ba46533909)
- [dmic_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#ga777e407deafee37c7f26039dd3144c4a)
- [dmic_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gab53ad4a4dddc12cdc7d012774f0ef63a)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_dmic_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_i2s_config_结构体.md)
