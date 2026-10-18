---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-1
title: dali_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdali__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_dali\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdali__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：数字可寻址照明接口（DALI）驱动操作。

```c
#include <zephyr/drivers/dali.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：数字可寻址照明接口（DALI）驱动操作。这是每个 DALI 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a46e38012b78f141dad104f780a029161"></a>

```c
dali_api_set_receive_callback_t set_receive_callback
```

相关声明：[dali_api_set_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#ga00ceb1581576430fa6864a073eaa73b0)、[set_receive_callback](#a46e38012b78f141dad104f780a029161)。

`REQ`：设置接收 DALI 总线帧的回调函数。

<a id="r_a5f4fd21a37c64adb724e0f1986b2097c"></a>

```c
dali_api_transmit_t transmit
```

相关声明：[dali_api_transmit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#gac6b54d7e448fd97e8936d4fd04177da0)、[transmit](#a5f4fd21a37c64adb724e0f1986b2097c)。

`REQ`：在 DALI 总线上发送帧。

## 1.2\_详细说明（Detailed Documentation）

<a id="a46e38012b78f141dad104f780a029161"></a>

### `set_receive_callback`

```c
dali_api_set_receive_callback_t dali_driver_api::set_receive_callback
```

`REQ`：设置接收 DALI 总线帧的回调函数。

<a id="a5f4fd21a37c64adb724e0f1986b2097c"></a>

### `transmit`

```c
dali_api_transmit_t dali_driver_api::transmit
```

`REQ`：在 DALI 总线上发送帧。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dali.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dali.h](https://docs.zephyrproject.org/latest/doxygen/html/dali_8h_source.html)
- [dali_api_set_receive_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#ga00ceb1581576430fa6864a073eaa73b0)
- [dali_api_transmit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface__backend.html#gac6b54d7e448fd97e8936d4fd04177da0)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_dali_frame_结构体.md)
