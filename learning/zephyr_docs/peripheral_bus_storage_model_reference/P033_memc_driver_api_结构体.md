---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-33
title: memc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmemc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_memc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmemc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：内存控制器（MEMC）驱动操作。

```c
#include <zephyr/drivers/memc.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：存储控制器（MEMC）驱动操作。这是每个 MEMC 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_af5091fa43e0227b5038a6f7eae649e72"></a>

```c
memc_api_read read
```

相关声明：[memc_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga1e7138177b931238a4f09a58bf4c765a)、[read](#af5091fa43e0227b5038a6f7eae649e72)。

`OPT`：从外部存储器读取数据。

<a id="r_af64136ddf8e8f569eaf7882e28a5f8c8"></a>

```c
memc_api_write write
```

相关声明：[memc_api_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gac495599a886be46a47dc22f6aaedcfb8)、[write](#af64136ddf8e8f569eaf7882e28a5f8c8)。

`OPT`：向外部存储器写入数据。

<a id="r_a9c6376bec867625f3569ccf2bf379a7b"></a>

```c
memc_api_get_mem_base get_mem_base
```

相关声明：[memc_api_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga0311584e35d2ad24e92bb9999ca76510)、[get_mem_base](#a9c6376bec867625f3569ccf2bf379a7b)。

`OPT`：获取存储控制器（MEMC）设备的内存映射基地址。

<a id="r_ad5ac94768979a4e6100cc26868ef14aa"></a>

```c
memc_api_get_size get_size
```

相关声明：[memc_api_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga2c33e74e81bbc4aaaef0a577737ebdcb)、[get_size](#ad5ac94768979a4e6100cc26868ef14aa)。

`OPT`：获取外部存储器的大小。

<a id="r_afaf23ae48edfd05fbe3366a0750ecfdd"></a>

```c
memc_api_read_id read_id
```

相关声明：[memc_api_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gada700c92c23e9a59eea6012594e8866d)、[read_id](#afaf23ae48edfd05fbe3366a0750ecfdd)。

`OPT`：读取外部存储器的 ID。

## 33.2\_详细说明（Detailed Documentation）

<a id="a9c6376bec867625f3569ccf2bf379a7b"></a>

### `get_mem_base`

```c
memc_api_get_mem_base memc_driver_api::get_mem_base
```

`OPT`：获取存储控制器（MEMC）设备的内存映射基地址。

<a id="ad5ac94768979a4e6100cc26868ef14aa"></a>

### `get_size`

```c
memc_api_get_size memc_driver_api::get_size
```

`OPT`：获取外部存储器的大小。

<a id="af5091fa43e0227b5038a6f7eae649e72"></a>

### `read`

```c
memc_api_read memc_driver_api::read
```

`OPT`：从外部存储器读取数据。

<a id="afaf23ae48edfd05fbe3366a0750ecfdd"></a>

### `read_id`

```c
memc_api_read_id memc_driver_api::read_id
```

`OPT`：读取外部存储器的 ID。

<a id="af64136ddf8e8f569eaf7882e28a5f8c8"></a>

### `write`

```c
memc_api_write memc_driver_api::write
```

`OPT`：向外部存储器写入数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/memc.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/drivers/memc.h](https://docs.zephyrproject.org/latest/doxygen/html/memc_8h_source.html)
- [memc_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga1e7138177b931238a4f09a58bf4c765a)
- [memc_api_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gac495599a886be46a47dc22f6aaedcfb8)
- [memc_api_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga0311584e35d2ad24e92bb9999ca76510)
- [memc_api_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga2c33e74e81bbc4aaaef0a577737ebdcb)
- [memc_api_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gada700c92c23e9a59eea6012594e8866d)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_mctp_usb_class_inst_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_mmc_device_type_结构体.md)
