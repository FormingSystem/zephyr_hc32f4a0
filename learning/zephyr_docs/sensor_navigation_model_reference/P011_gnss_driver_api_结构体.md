---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-11
title: gnss_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgnss__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_gnss\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgnss__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：全球导航卫星系统（GNSS）驱动操作。

```c
#include <zephyr/drivers/gnss.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：全球导航卫星系统（GNSS）驱动操作。这是每个 GNSS 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a6ab6ea8cb9588ad1a64c1ca6e99be137"></a>

```c
gnss_start_t start
```

相关声明：[gnss_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga8f617e5c8a0938e5eef4d69a3f753303)、[start](#a6ab6ea8cb9588ad1a64c1ca6e99be137)。

可选（OPT）：启动 GNSS 接收机引擎。

<a id="r_ae62ee87f9380b9ea28bf9efa75f04352"></a>

```c
gnss_stop_t stop
```

相关声明：[gnss_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga906cecc7e7173893106d6154c7421fc6)、[stop](#ae62ee87f9380b9ea28bf9efa75f04352)。

可选（OPT）：停止 GNSS 接收机引擎。

<a id="r_a0d79083d56a7a35c3a2c858e2c6627f5"></a>

```c
gnss_set_fix_rate_t set_fix_rate
```

相关声明：[gnss_set_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga79e5975d5ec6c0557af4a71004a6da93)、[set_fix_rate](#a0d79083d56a7a35c3a2c858e2c6627f5)。

可选（OPT）：设置 GNSS 定位更新率（fix rate）。

<a id="r_abd0d989e810fa0bdffe0f68a10622bbf"></a>

```c
gnss_get_fix_rate_t get_fix_rate
```

相关声明：[gnss_get_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga63a98e08bc7e4b9c70a27de48dc9cd8c)、[get_fix_rate](#abd0d989e810fa0bdffe0f68a10622bbf)。

可选（OPT）：获取 GNSS 定位更新率。

<a id="r_a7b77dbf9b49fec76dd9374b97a025b08"></a>

```c
gnss_set_navigation_mode_t set_navigation_mode
```

相关声明：[gnss_set_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gae946fce6ecced7c8fa09e06d75855abe)、[set_navigation_mode](#a7b77dbf9b49fec76dd9374b97a025b08)。

可选（OPT）：设置 GNSS 导航模式（navigation mode）。

<a id="r_a77247b70ca41bea5b29f579e67c878a9"></a>

```c
gnss_get_navigation_mode_t get_navigation_mode
```

相关声明：[gnss_get_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga9705b36019161fde431e78d943eff604)、[get_navigation_mode](#a77247b70ca41bea5b29f579e67c878a9)。

可选（OPT）：获取 GNSS 导航模式。

<a id="r_a1f4c78c928301ede626a9bcb92c5050d"></a>

```c
gnss_set_enabled_systems_t set_enabled_systems
```

相关声明：[gnss_set_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga91948cc0567c343bee62b6c70a2f461d)、[set_enabled_systems](#a1f4c78c928301ede626a9bcb92c5050d)。

可选（OPT）：设置启用的 GNSS 系统。

<a id="r_abc82a5f3ede200cd40982581ddf9d02f"></a>

```c
gnss_get_enabled_systems_t get_enabled_systems
```

相关声明：[gnss_get_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad87bd07c46ea1f79caf9a484c51ec0c9)、[get_enabled_systems](#abc82a5f3ede200cd40982581ddf9d02f)。

可选（OPT）：获取已启用的 GNSS 系统。

<a id="r_af3ad59e6495183f9b45dfbfe0e54fbb6"></a>

```c
gnss_get_supported_systems_t get_supported_systems
```

相关声明：[gnss_get_supported_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaf52a65dee0d28286ac40e5c8bc86825a)、[get_supported_systems](#af3ad59e6495183f9b45dfbfe0e54fbb6)。

可选（OPT）：获取支持的 GNSS 系统。

<a id="r_a2a1604472e2a0249a766534b05a11133"></a>

```c
gnss_get_latest_timepulse_t get_latest_timepulse
```

相关声明：[gnss_get_latest_timepulse_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaa482aa8a996b743aba7e68f36b4780a8)、[get_latest_timepulse](#a2a1604472e2a0249a766534b05a11133)。

可选（OPT）：获取最近一次秒脉冲（PPS）时间脉冲的时间戳。

## 11.2\_详细说明（Detailed Documentation）

<a id="abc82a5f3ede200cd40982581ddf9d02f"></a>

### `get_enabled_systems`

```c
gnss_get_enabled_systems_t gnss_driver_api::get_enabled_systems
```

可选（OPT）：获取已启用的 GNSS 系统。

<a id="abd0d989e810fa0bdffe0f68a10622bbf"></a>

### `get_fix_rate`

```c
gnss_get_fix_rate_t gnss_driver_api::get_fix_rate
```

可选（OPT）：获取 GNSS 定位更新率。

<a id="a2a1604472e2a0249a766534b05a11133"></a>

### `get_latest_timepulse`

```c
gnss_get_latest_timepulse_t gnss_driver_api::get_latest_timepulse
```

可选（OPT）：获取最近一次秒脉冲（PPS）时间脉冲的时间戳。

<a id="a77247b70ca41bea5b29f579e67c878a9"></a>

### `get_navigation_mode`

```c
gnss_get_navigation_mode_t gnss_driver_api::get_navigation_mode
```

可选（OPT）：获取 GNSS 导航模式。

<a id="af3ad59e6495183f9b45dfbfe0e54fbb6"></a>

### `get_supported_systems`

```c
gnss_get_supported_systems_t gnss_driver_api::get_supported_systems
```

可选（OPT）：获取支持的 GNSS 系统。

<a id="a1f4c78c928301ede626a9bcb92c5050d"></a>

### `set_enabled_systems`

```c
gnss_set_enabled_systems_t gnss_driver_api::set_enabled_systems
```

可选（OPT）：设置启用的 GNSS 系统。

<a id="a0d79083d56a7a35c3a2c858e2c6627f5"></a>

### `set_fix_rate`

```c
gnss_set_fix_rate_t gnss_driver_api::set_fix_rate
```

可选（OPT）：设置 GNSS 定位更新率（fix rate）。

<a id="a7b77dbf9b49fec76dd9374b97a025b08"></a>

### `set_navigation_mode`

```c
gnss_set_navigation_mode_t gnss_driver_api::set_navigation_mode
```

可选（OPT）：设置 GNSS 导航模式（navigation mode）。

<a id="a6ab6ea8cb9588ad1a64c1ca6e99be137"></a>

### `start`

```c
gnss_start_t gnss_driver_api::start
```

可选（OPT）：启动 GNSS 接收机引擎。

<a id="ae62ee87f9380b9ea28bf9efa75f04352"></a>

### `stop`

```c
gnss_stop_t gnss_driver_api::stop
```

可选（OPT）：停止 GNSS 接收机引擎。

本数据类型文档由以下文件生成：

- `zephyr/drivers/gnss.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h_source.html)
- [gnss_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga8f617e5c8a0938e5eef4d69a3f753303)
- [gnss_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga906cecc7e7173893106d6154c7421fc6)
- [gnss_set_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga79e5975d5ec6c0557af4a71004a6da93)
- [gnss_get_fix_rate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga63a98e08bc7e4b9c70a27de48dc9cd8c)
- [gnss_set_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gae946fce6ecced7c8fa09e06d75855abe)
- [gnss_get_navigation_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga9705b36019161fde431e78d943eff604)
- [gnss_set_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#ga91948cc0567c343bee62b6c70a2f461d)
- [gnss_get_enabled_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gad87bd07c46ea1f79caf9a484c51ec0c9)
- [gnss_get_supported_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaf52a65dee0d28286ac40e5c8bc86825a)
- [gnss_get_latest_timepulse_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface__backend.html#gaa482aa8a996b743aba7e68f36b4780a8)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_gnss_data_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_gnss_info_结构体.md)
