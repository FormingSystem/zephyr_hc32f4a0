---
id: learning.zephyr-docs.network-service-model-reference.page-54
title: ptp_clock_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structptp__clock__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_ptp\_clock\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structptp__clock__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：精确时间协议时钟（PTP Clock）驱动操作。

```c
#include <zephyr/drivers/ptp_clock.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：精确时间协议时钟（PTP Clock）驱动操作。这是每个 PTP 时钟驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a9ef8a7a3ece8012c12fcb4510fa20e71"></a>

```c
ptp_clock_api_set_t set
```

相关声明：[ptp_clock_api_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gaeda56e624ddc47b5f23ebd090031982a)、[set](#a9ef8a7a3ece8012c12fcb4510fa20e71)。

必需（REQ）：设置 PTP 时钟时间。

<a id="r_aaf9ba9cb7af6c77a0cf53e2c576f7106"></a>

```c
ptp_clock_api_get_t get
```

相关声明：[ptp_clock_api_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#ga59a1c7530e59fd19b3fa25ff6f4e346c)、[get](#aaf9ba9cb7af6c77a0cf53e2c576f7106)。

必需（REQ）：获取 PTP 时钟时间。

<a id="r_af0bb3479e2b165500cbe602bd71e9e84"></a>

```c
ptp_clock_api_adjust_t adjust
```

相关声明：[ptp_clock_api_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gad3b345ba7db470f274cffa33b1128810)、[adjust](#af0bb3479e2b165500cbe602bd71e9e84)。

必需（REQ）：调整 PTP 时钟时间。

<a id="r_aef67c906d97a1b9453ffd5d0e35d44c9"></a>

```c
ptp_clock_api_rate_adjust_t rate_adjust
```

相关声明：[ptp_clock_api_rate_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gae94ee94813969d15f8dc841814562ac3)、[rate_adjust](#aef67c906d97a1b9453ffd5d0e35d44c9)。

必需（REQ）：根据标称频率调整 PTP 时钟的速率比（rate ratio）。

## 54.2\_详细说明（Detailed Documentation）

<a id="af0bb3479e2b165500cbe602bd71e9e84"></a>

### `adjust`

```c
ptp_clock_api_adjust_t ptp_clock_driver_api::adjust
```

必需（REQ）：调整 PTP 时钟时间。

<a id="aaf9ba9cb7af6c77a0cf53e2c576f7106"></a>

### `get`

```c
ptp_clock_api_get_t ptp_clock_driver_api::get
```

必需（REQ）：获取 PTP 时钟时间。

<a id="aef67c906d97a1b9453ffd5d0e35d44c9"></a>

### `rate_adjust`

```c
ptp_clock_api_rate_adjust_t ptp_clock_driver_api::rate_adjust
```

必需（REQ）：根据标称频率调整 PTP 时钟的速率比（rate ratio）。

<a id="a9ef8a7a3ece8012c12fcb4510fa20e71"></a>

### `set`

```c
ptp_clock_api_set_t ptp_clock_driver_api::set
```

必需（REQ）：设置 PTP 时钟时间。

本数据类型文档由以下文件生成：

- `zephyr/drivers/ptp_clock.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/drivers/ptp_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__clock_8h_source.html)
- [ptp_clock_api_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gaeda56e624ddc47b5f23ebd090031982a)
- [ptp_clock_api_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#ga59a1c7530e59fd19b3fa25ff6f4e346c)
- [ptp_clock_api_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gad3b345ba7db470f274cffa33b1128810)
- [ptp_clock_api_rate_adjust_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface__backend.html#gae94ee94813969d15f8dc841814562ac3)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_prometheus_summary_quantile_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_socket_dns_offload_结构体.md)
