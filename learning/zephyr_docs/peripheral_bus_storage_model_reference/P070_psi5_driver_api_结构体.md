---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-70
title: psi5_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_psi5\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：外设传感器接口5（PSI5）驱动操作。

```c
#include <zephyr/drivers/psi5/psi5.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：外设传感器接口 5（PSI5）驱动操作。这是每个 PSI5 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a5ca6bfb70c91a39fb5aadc9194371383"></a>

```c
psi5_start_sync_t start_sync
```

相关声明：[psi5_start_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gaf86804dd3befe78878ed2d9b3bad9a49)、[start_sync](#a5ca6bfb70c91a39fb5aadc9194371383)。

`OPT`：启动指定通道上的同步脉冲发生器（Sync pulse generator）。

<a id="r_adf7ff27e095d3d81e7a25ce5ad3e575f"></a>

```c
psi5_stop_sync_t stop_sync
```

相关声明：[psi5_stop_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga44a73fc30fb29d688d761b8d23eb0da6)、[stop_sync](#adf7ff27e095d3d81e7a25ce5ad3e575f)。

`OPT`：停止指定通道上的同步脉冲发生器。

<a id="r_a50bf202d1bea4c2bf17b2ba3b0668cf8"></a>

```c
psi5_send_t send
```

相关声明：[psi5_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga1ddcb06317f425a9d97defb1e4ccd677)、[send](#a50bf202d1bea4c2bf17b2ba3b0668cf8)。

`OPT`：在指定通道上传输 PSI5 数据。

<a id="r_a195bc96d912854955b591b5e2911cb98"></a>

```c
psi5_register_callback_t register_callback
```

相关声明：[psi5_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gae9b98f6b16ed1364364e1d63f18bb479)、[register_callback](#a195bc96d912854955b591b5e2911cb98)。

`OPT`：添加回调函数，以处理指定通道接收到的消息。

## 70.2\_详细说明（Detailed Documentation）

<a id="a195bc96d912854955b591b5e2911cb98"></a>

### `register_callback`

```c
psi5_register_callback_t psi5_driver_api::register_callback
```

`OPT`：添加回调函数，以处理指定通道接收到的消息。

<a id="a50bf202d1bea4c2bf17b2ba3b0668cf8"></a>

### `send`

```c
psi5_send_t psi5_driver_api::send
```

`OPT`：在指定通道上传输 PSI5 数据。

<a id="a5ca6bfb70c91a39fb5aadc9194371383"></a>

### `start_sync`

```c
psi5_start_sync_t psi5_driver_api::start_sync
```

`OPT`：启动指定通道上的同步脉冲发生器（Sync pulse generator）。

<a id="adf7ff27e095d3d81e7a25ce5ad3e575f"></a>

### `stop_sync`

```c
psi5_stop_sync_t psi5_driver_api::stop_sync
```

`OPT`：停止指定通道上的同步脉冲发生器。

本数据类型文档由以下文件生成：

- `zephyr/drivers/psi5/psi5.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/drivers/psi5/psi5.h](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)
- [psi5_start_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gaf86804dd3befe78878ed2d9b3bad9a49)
- [psi5_stop_sync_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga44a73fc30fb29d688d761b8d23eb0da6)
- [psi5_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#ga1ddcb06317f425a9d97defb1e4ccd677)
- [psi5_register_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface__backend.html#gae9b98f6b16ed1364364e1d63f18bb479)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_ps2_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_psi5_frame_结构体.md)
