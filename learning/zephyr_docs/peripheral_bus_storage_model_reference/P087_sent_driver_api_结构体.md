---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-87
title: sent_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsent__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_sent\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsent__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：单边沿半字节传输（SENT）驱动操作。

```c
#include <zephyr/drivers/sent/sent.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：单边沿半字节传输（SENT）驱动操作。这是每个 SENT 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 87.1\_数据成员（Data Fields）

<a id="r_a832b061c8e6ae38199d54f9702fb39a7"></a>

```c
sent_start_listening_t start_listening
```

相关声明：[sent_start_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga4d4cc8870210e37bdac56d15f5979a32)、[start_listening](#a832b061c8e6ae38199d54f9702fb39a7)。

`OPT`：启用指定通道，使其开始从总线接收。

<a id="r_a355a318c08625c99bb1b2adf193bf577"></a>

```c
sent_stop_listening_t stop_listening
```

相关声明：[sent_stop_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#gad13f1bbd1eb6b6300780596b94bff6ac)、[stop_listening](#a355a318c08625c99bb1b2adf193bf577)。

`OPT`：禁用指定通道，使其停止从总线接收。

<a id="r_a0be794c9fb93ff9e04fa22cf2aeea4b9"></a>

```c
sent_register_callback_t register_callback
```

相关声明：[sent_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga3b72c0fafbb177264d20df089ff5c38c)、[register_callback](#a0be794c9fb93ff9e04fa22cf2aeea4b9)。

`OPT`：添加回调函数，以处理指定通道接收到的消息。

## 87.2\_详细说明（Detailed Documentation）

<a id="a0be794c9fb93ff9e04fa22cf2aeea4b9"></a>

### `register_callback`

```c
sent_register_callback_t sent_driver_api::register_callback
```

`OPT`：添加回调函数，以处理指定通道接收到的消息。

<a id="a832b061c8e6ae38199d54f9702fb39a7"></a>

### `start_listening`

```c
sent_start_listening_t sent_driver_api::start_listening
```

`OPT`：启用指定通道，使其开始从总线接收。

<a id="a355a318c08625c99bb1b2adf193bf577"></a>

### `stop_listening`

```c
sent_stop_listening_t sent_driver_api::stop_listening
```

`OPT`：禁用指定通道，使其停止从总线接收。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sent/sent.h`

## 87.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sent/sent.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)
- [sent_start_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga4d4cc8870210e37bdac56d15f5979a32)
- [sent_stop_listening_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#gad13f1bbd1eb6b6300780596b94bff6ac)
- [sent_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface__backend.html#ga3b72c0fafbb177264d20df089ff5c38c)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P086_sdio_func_结构体.md) · [返回大纲](大纲.md) · [下一章](P088_sent_frame_结构体.md)
