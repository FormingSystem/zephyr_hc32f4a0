---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-3
title: devmux_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdevmux__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_devmux\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdevmux__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：设备多路复用（DEVMUX）驱动操作。

```c
#include <zephyr/drivers/misc/devmux/devmux.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：设备多路复用器（DEVMUX）驱动操作。这是每个 DEVMUX 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a883b6973a6109c189f7f82f38aace760"></a>

```c
int(* select_get )(const struct device *dev)
```

相关声明：[select_get](#a883b6973a6109c189f7f82f38aace760)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：获取设备多路复用器（devmux）当前选择项的回调 API。

<a id="r_a9e9453dbb5639b6df48f75905b539583"></a>

```c
int(* select_set )(struct device *dev, size_t index)
```

相关声明：[select_set](#a9e9453dbb5639b6df48f75905b539583)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：设置 devmux 设备选择项的回调 API。

## 3.2\_详细说明（Detailed Documentation）

<a id="a883b6973a6109c189f7f82f38aace760"></a>

### `select_get`

```c
int(* devmux_driver_api::select_get) (const struct device *dev)
```

`REQ`：获取设备多路复用器（devmux）当前选择项的回调 API。

<a id="a9e9453dbb5639b6df48f75905b539583"></a>

### `select_set`

```c
int(* devmux_driver_api::select_set) (struct device *dev, size_t index)
```

`REQ`：设置 devmux 设备选择项的回调 API。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/devmux/devmux.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/devmux/devmux.h](https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_dali_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_disk_info_结构体.md)
