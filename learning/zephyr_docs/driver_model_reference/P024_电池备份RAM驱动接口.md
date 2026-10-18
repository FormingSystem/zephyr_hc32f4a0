---
id: learning.zephyr-docs.driver-model-reference.page-24
title: 电池备份RAM驱动接口
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbbram__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_电池备份RAM驱动接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbbram__driver__api.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：电池备份 RAM（Battery-backed RAM，BBRAM）驱动操作。

```c
#include <zephyr/drivers/bbram.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：电池备份 RAM（Battery-backed RAM，BBRAM）驱动操作。所有 BBRAM 驱动都需要定义此驱动 API 结构体。它包含指向驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员则是可选项。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a04c9f9487d35a0c2d264d033ef266fc7"></a>

```c
bbram_api_check_invalid_t check_invalid
```

相关声明：[bbram_api_check_invalid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gac23658302662587043f3587080f798fe)、[check_invalid](#a04c9f9487d35a0c2d264d033ef266fc7)。

可选（OPT）：检查 BBRAM 是否无效。

<a id="r_a4c3813853e2364109ea1b481277f2816"></a>

```c
bbram_api_check_standby_power_t check_standby_power
```

相关声明：[bbram_api_check_standby_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga99adefcb89ab80d8b5e24b8ffad8f43e)、[check_standby_power](#a4c3813853e2364109ea1b481277f2816)。

可选（OPT）：检查待机电源（Volt SBY）是否发生故障。

<a id="r_a6df89dfb1ce05bc557286bc894751702"></a>

```c
bbram_api_check_power_t check_power
```

相关声明：[bbram_api_check_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gaa6edc8a61529edad90de2e6fff619fdf)、[check_power](#a6df89dfb1ce05bc557286bc894751702)。

可选（OPT）：检查 V CC1 电源是否发生故障。

<a id="r_a15809ed9c49ade6de1ddbc7e48072b12"></a>

```c
bbram_api_get_size_t get_size
```

相关声明：[bbram_api_get_size_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gacfa586f705c520a6a05638a2e289fe50)、[get_size](#a15809ed9c49ade6de1ddbc7e48072b12)。

可选（OPT）：获取 BBRAM 的大小，单位为字节。

<a id="r_a50a91db769c65d4e9dceb027c5bc956d"></a>

```c
bbram_api_read_t read
```

相关声明：[bbram_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga8b06a1b3bb9b524597804dd268904881)、[read](#a50a91db769c65d4e9dceb027c5bc956d)。

可选（OPT）：从 BBRAM 读取字节。

<a id="r_a937578d674e8ed1e26026aea7428e616"></a>

```c
bbram_api_write_t write
```

相关声明：[bbram_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga1b111ae421791b9544777c1bab5e2a02)、[write](#a937578d674e8ed1e26026aea7428e616)。

可选（OPT）：向 BBRAM 写入字节。

## 24.2\_详细说明（Detailed Documentation）

<a id="a04c9f9487d35a0c2d264d033ef266fc7"></a>

### `check_invalid`

```c
bbram_api_check_invalid_t bbram_driver_api::check_invalid
```

可选（OPT）：检查 BBRAM 是否无效。

<a id="a6df89dfb1ce05bc557286bc894751702"></a>

### `check_power`

```c
bbram_api_check_power_t bbram_driver_api::check_power
```

可选（OPT）：检查 V CC1 电源是否发生故障。

<a id="a4c3813853e2364109ea1b481277f2816"></a>

### `check_standby_power`

```c
bbram_api_check_standby_power_t bbram_driver_api::check_standby_power
```

可选（OPT）：检查待机电源（Volt SBY）是否发生故障。

<a id="a15809ed9c49ade6de1ddbc7e48072b12"></a>

### `get_size`

```c
bbram_api_get_size_t bbram_driver_api::get_size
```

可选（OPT）：获取 BBRAM 的大小，单位为字节。

<a id="a50a91db769c65d4e9dceb027c5bc956d"></a>

### `read`

```c
bbram_api_read_t bbram_driver_api::read
```

可选（OPT）：从 BBRAM 读取字节。

<a id="a937578d674e8ed1e26026aea7428e616"></a>

### `write`

```c
bbram_api_write_t bbram_driver_api::write
```

可选（OPT）：向 BBRAM 写入字节。

本结构体文档由以下文件生成：

- `zephyr/drivers/bbram.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bbram.h](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h_source.html)
- [bbram_api_check_invalid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gac23658302662587043f3587080f798fe)
- [bbram_api_check_standby_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga99adefcb89ab80d8b5e24b8ffad8f43e)
- [bbram_api_check_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gaa6edc8a61529edad90de2e6fff619fdf)
- [bbram_api_get_size_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gacfa586f705c520a6a05638a2e289fe50)
- [bbram_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga8b06a1b3bb9b524597804dd268904881)
- [bbram_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga1b111ae421791b9544777c1bab5e2a02)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_辅助显示器亮度.md) · [返回大纲](大纲.md) · [下一章](P025_BC12伙伴状态.md)
