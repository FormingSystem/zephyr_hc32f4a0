---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-42
title: mspi_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_mspi\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：MSPI驱动操作。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：多线串行外设接口（MSPI）驱动操作。这是每个 MSPI 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a05c3dad20834850a833663dd896fa6eb"></a>

```c
mspi_api_config config
```

相关声明：[mspi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga2ff9209634fb241e2f7323e749df612e)、[config](#a05c3dad20834850a833663dd896fa6eb)。

`REQ`：配置 MSPI 控制器。

<a id="r_a1a4593ada09a204004a11dcb6031c18f"></a>

```c
mspi_api_dev_config dev_config
```

相关声明：[mspi_api_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga7e3bae501067b045e9ed8d0efbe6e61d)、[dev_config](#a1a4593ada09a204004a11dcb6031c18f)。

`REQ`：使用设备特定参数配置 MSPI 控制器。

<a id="r_a31bf25f0ce01b9aada76f6b0030b05be"></a>

```c
mspi_api_get_channel_status get_channel_status
```

相关声明：[mspi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gadd66b118b76a4ee7ef252afc6b830bfa)、[get_channel_status](#a31bf25f0ce01b9aada76f6b0030b05be)。

`REQ`：查询通道是否就绪。

<a id="r_aae8c346182a9c437891044afc0b16e07"></a>

```c
mspi_api_transceive transceive
```

相关声明：[mspi_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga17b551f4d9f980fde8eabcaae3318617)、[transceive](#aae8c346182a9c437891044afc0b16e07)。

`OPT`：通过 MSPI 执行传输请求。

<a id="r_a15a53b61fcd32d0436323ad85c75f62a"></a>

```c
mspi_api_register_callback register_callback
```

相关声明：[mspi_api_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gad6d65ef0d523f22592ff17c04698f663)、[register_callback](#a15a53b61fcd32d0436323ad85c75f62a)。

`OPT`：注册 MSPI 回调函数。

<a id="r_a70c612ee3b997682b7e9f06119d7e756"></a>

```c
mspi_api_memmap_config memmap_config
```

相关声明：[mspi_api_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga002c5d3cc7d6691130dee0f42b928894)、[memmap_config](#a70c612ee3b997682b7e9f06119d7e756)。

`OPT`：配置 MSPI 内存映射（Memory map）设置。

<a id="r_aa0a42a85841370693ce054ed859d1fd8"></a>

```c
mspi_api_scramble_config scramble_config
```

相关声明：[mspi_api_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga092c8bb0879977a8cc8eea5d1662c34b)、[scramble_config](#aa0a42a85841370693ce054ed859d1fd8)。

`OPT`：配置 MSPI 扰码（Scrambling）设置。

<a id="r_a77553c6ea19e8803dcabc4deccf35619"></a>

```c
mspi_api_timing_config timing_config
```

相关声明：[mspi_api_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga407713e07f23756564814402342c9c97)、[timing_config](#a77553c6ea19e8803dcabc4deccf35619)。

`OPT`：配置 MSPI 时序（Timing）设置。

## 42.2\_详细说明（Detailed Documentation）

<a id="a05c3dad20834850a833663dd896fa6eb"></a>

### `config`

```c
mspi_api_config mspi_driver_api::config
```

`REQ`：配置 MSPI 控制器。

<a id="a1a4593ada09a204004a11dcb6031c18f"></a>

### `dev_config`

```c
mspi_api_dev_config mspi_driver_api::dev_config
```

`REQ`：使用设备特定参数配置 MSPI 控制器。

<a id="a31bf25f0ce01b9aada76f6b0030b05be"></a>

### `get_channel_status`

```c
mspi_api_get_channel_status mspi_driver_api::get_channel_status
```

`REQ`：查询通道是否就绪。

<a id="a70c612ee3b997682b7e9f06119d7e756"></a>

### `memmap_config`

```c
mspi_api_memmap_config mspi_driver_api::memmap_config
```

`OPT`：配置 MSPI 内存映射（Memory map）设置。

<a id="a15a53b61fcd32d0436323ad85c75f62a"></a>

### `register_callback`

```c
mspi_api_register_callback mspi_driver_api::register_callback
```

`OPT`：注册 MSPI 回调函数。

<a id="aa0a42a85841370693ce054ed859d1fd8"></a>

### `scramble_config`

```c
mspi_api_scramble_config mspi_driver_api::scramble_config
```

`OPT`：配置 MSPI 扰码（Scrambling）设置。

<a id="a77553c6ea19e8803dcabc4deccf35619"></a>

### `timing_config`

```c
mspi_api_timing_config mspi_driver_api::timing_config
```

`OPT`：配置 MSPI 时序（Timing）设置。

<a id="aae8c346182a9c437891044afc0b16e07"></a>

### `transceive`

```c
mspi_api_transceive mspi_driver_api::transceive
```

`OPT`：通过 MSPI 执行传输请求。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [mspi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga2ff9209634fb241e2f7323e749df612e)
- [mspi_api_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga7e3bae501067b045e9ed8d0efbe6e61d)
- [mspi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gadd66b118b76a4ee7ef252afc6b830bfa)
- [mspi_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga17b551f4d9f980fde8eabcaae3318617)
- [mspi_api_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gad6d65ef0d523f22592ff17c04698f663)
- [mspi_api_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga002c5d3cc7d6691130dee0f42b928894)
- [mspi_api_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga092c8bb0879977a8cc8eea5d1662c34b)
- [mspi_api_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga407713e07f23756564814402342c9c97)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_mspi_dev_id_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_mspi_dt_spec_结构体.md)
