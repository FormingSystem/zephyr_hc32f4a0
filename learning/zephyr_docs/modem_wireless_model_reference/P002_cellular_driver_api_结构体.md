---
id: learning.zephyr-docs.modem-wireless-model-reference.page-2
title: cellular_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_cellular\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：蜂窝通信（Cellular）驱动操作。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：蜂窝网络（Cellular）驱动操作。这是每个蜂窝网络驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_ac219c2c960f838bc8c0fd41307a3ff05"></a>

```c
cellular_api_configure_networks configure_networks
```

相关声明：[cellular_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga71ddc5b9e09da398d02caadc91ef3cfc)、[configure_networks](#ac219c2c960f838bc8c0fd41307a3ff05)。

可选（OPT）：配置设备的蜂窝网络。

<a id="r_a32ede01e742a2e7c18e9cb4f963b90fe"></a>

```c
cellular_api_get_supported_networks get_supported_networks
```

相关声明：[cellular_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga6aa2c51fa80d5420593021c35444308a)、[get_supported_networks](#a32ede01e742a2e7c18e9cb4f963b90fe)。

可选（OPT）：获取设备支持的蜂窝网络。

<a id="r_a7d64a630e4dafd57c00b04d3dfea1b79"></a>

```c
cellular_api_get_signal get_signal
```

相关声明：[cellular_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga75cac77838970288d4d23647eaafd30b)、[get_signal](#a7d64a630e4dafd57c00b04d3dfea1b79)。

可选（OPT）：获取设备的信号信息。

<a id="r_ab03cc8706fafd729c21cec9569eae8db"></a>

```c
cellular_api_get_modem_info get_modem_info
```

相关声明：[cellular_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga03095206ae2b77ce232dd05b172bd56d)、[get_modem_info](#ab03cc8706fafd729c21cec9569eae8db)。

可选（OPT）：获取设备的调制解调器（modem）信息。

<a id="r_a7641d06668b65b007fd4a3a900bbde0e"></a>

```c
cellular_api_get_registration_status get_registration_status
```

相关声明：[cellular_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga08a0966933caa70d7044342ed2ad8eb6)、[get_registration_status](#a7641d06668b65b007fd4a3a900bbde0e)。

可选（OPT）：获取设备的网络注册状态（network registration status）。

<a id="r_a17153560e19ddd9a64991780372a2531"></a>

```c
cellular_api_get_network_status get_network_status
```

相关声明：[cellular_api_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga30f5fef993f17b001e2df9c89bdaf288)、[get_network_status](#a17153560e19ddd9a64991780372a2531)。

可选（OPT）：获取最近报告的网络或服务小区（serving cell）状态。

<a id="r_a40a6b2d890790e1a521f227e5c296b5b"></a>

```c
cellular_api_set_apn set_apn
```

相关声明：[cellular_api_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gabf5bd5a939a300b8493f7c803b9128f0)、[set_apn](#a40a6b2d890790e1a521f227e5c296b5b)。

可选（OPT）：设置分组数据协议（PDP）上下文使用的接入点名称（APN）。

<a id="r_a4982b88e4342abd6582d10b02f2e6ed0"></a>

```c
cellular_api_set_callback set_callback
```

相关声明：[cellular_api_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gacbf9c85b2ea95321beee0ba75d5977f7)、[set_callback](#a4982b88e4342abd6582d10b02f2e6ed0)。

可选（OPT）：订阅异步蜂窝网络事件。

<a id="r_a0bf599ed34ee55aacf4be01e22d86b30"></a>

```c
cellular_api_get_stats get_stats
```

相关声明：[cellular_api_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga975fe3a63ed2dd936faa619846f8b701)、[get_stats](#a0bf599ed34ee55aacf4be01e22d86b30)。

可选（OPT）：读取蜂窝网络设备的运行统计信息。

## 2.2\_详细说明（Detailed Documentation）

<a id="ac219c2c960f838bc8c0fd41307a3ff05"></a>

### `configure_networks`

```c
cellular_api_configure_networks cellular_driver_api::configure_networks
```

可选（OPT）：配置设备的蜂窝网络。

<a id="ab03cc8706fafd729c21cec9569eae8db"></a>

### `get_modem_info`

```c
cellular_api_get_modem_info cellular_driver_api::get_modem_info
```

可选（OPT）：获取设备的调制解调器（modem）信息。

<a id="a17153560e19ddd9a64991780372a2531"></a>

### `get_network_status`

```c
cellular_api_get_network_status cellular_driver_api::get_network_status
```

可选（OPT）：获取最近报告的网络或服务小区（serving cell）状态。

<a id="a7641d06668b65b007fd4a3a900bbde0e"></a>

### `get_registration_status`

```c
cellular_api_get_registration_status cellular_driver_api::get_registration_status
```

可选（OPT）：获取设备的网络注册状态（network registration status）。

<a id="a7d64a630e4dafd57c00b04d3dfea1b79"></a>

### `get_signal`

```c
cellular_api_get_signal cellular_driver_api::get_signal
```

可选（OPT）：获取设备的信号信息。

<a id="a0bf599ed34ee55aacf4be01e22d86b30"></a>

### `get_stats`

```c
cellular_api_get_stats cellular_driver_api::get_stats
```

可选（OPT）：读取蜂窝网络设备的运行统计信息。

<a id="a32ede01e742a2e7c18e9cb4f963b90fe"></a>

### `get_supported_networks`

```c
cellular_api_get_supported_networks cellular_driver_api::get_supported_networks
```

可选（OPT）：获取设备支持的蜂窝网络。

<a id="a40a6b2d890790e1a521f227e5c296b5b"></a>

### `set_apn`

```c
cellular_api_set_apn cellular_driver_api::set_apn
```

可选（OPT）：设置分组数据协议（PDP）上下文使用的接入点名称（APN）。

<a id="a4982b88e4342abd6582d10b02f2e6ed0"></a>

### `set_callback`

```c
cellular_api_set_callback cellular_driver_api::set_callback
```

可选（OPT）：订阅异步蜂窝网络事件。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [cellular_api_configure_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga71ddc5b9e09da398d02caadc91ef3cfc)
- [cellular_api_get_supported_networks](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga6aa2c51fa80d5420593021c35444308a)
- [cellular_api_get_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga75cac77838970288d4d23647eaafd30b)
- [cellular_api_get_modem_info](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga03095206ae2b77ce232dd05b172bd56d)
- [cellular_api_get_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga08a0966933caa70d7044342ed2ad8eb6)
- [cellular_api_get_network_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga30f5fef993f17b001e2df9c89bdaf288)
- [cellular_api_set_apn](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gabf5bd5a939a300b8493f7c803b9128f0)
- [cellular_api_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#gacbf9c85b2ea95321beee0ba75d5977f7)
- [cellular_api_get_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface__backend.html#ga975fe3a63ed2dd936faa619846f8b701)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_cc1200_rf_registers_set_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_cellular_evt_modem_comms_check_result_结构体.md)
