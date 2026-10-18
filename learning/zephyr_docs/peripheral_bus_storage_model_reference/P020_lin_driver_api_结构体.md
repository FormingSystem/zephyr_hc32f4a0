---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-20
title: lin_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_lin\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：LIN控制器（Controller）驱动操作。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：局部互连网络（LIN）控制器驱动操作。这是每个 LIN Controller 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a538f1329573a0919ed908e58ec60c24e"></a>

```c
lin_start_t start
```

相关声明：[lin_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga149ca3972fc800c4fd2bbb0b5d8a85e3)、[start](#a538f1329573a0919ed908e58ec60c24e)。

`REQ`：启动 LIN 控制器。

<a id="r_a72c15ca01a63897758fab966be5f71fe"></a>

```c
lin_stop_t stop
```

相关声明：[lin_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab0f27d3ad3637f9040920b3088c1e239)、[stop](#a72c15ca01a63897758fab966be5f71fe)。

`REQ`：停止 LIN 控制器。

<a id="r_acf01655ffd47f72425ef385745700569"></a>

```c
lin_configure_t configure
```

相关声明：[lin_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga39766c7605a50fcb600e9d72bfcf07d5)、[configure](#acf01655ffd47f72425ef385745700569)。

`REQ`：配置 LIN 控制器。

<a id="r_ada6d4e2661d5b9352d218757a69c7b10"></a>

```c
lin_get_config_t get_config
```

相关声明：[lin_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga305d83d265245ed657a9974c0bab1962)、[get_config](#ada6d4e2661d5b9352d218757a69c7b10)。

`REQ`：获取当前 LIN 配置。

<a id="r_a42abd5bd44fa028a4b2244131e5f17f4"></a>

```c
lin_set_rx_filter_t set_rx_filter
```

相关声明：[lin_set_rx_filter_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga727b0f7fe4949e3fd17a303e239586bb)、[set_rx_filter](#a42abd5bd44fa028a4b2244131e5f17f4)。

`OPT`：设置 LIN 接收过滤器，仅适用于响应方模式（Responder mode）。

<a id="r_af3321e6ce2a598a4bd123b968a608633"></a>

```c
lin_send_t send
```

相关声明：[lin_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga8091d2d225709439f9afb2eddeb73792)、[send](#af3321e6ce2a598a4bd123b968a608633)。

`REQ`：发送 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_a4704606967b3eb5d7ed103e1cccfb2fd"></a>

```c
lin_receive_t receive
```

相关声明：[lin_receive_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad77d365c000a2f9c7f2558ec24d0f455)、[receive](#a4704606967b3eb5d7ed103e1cccfb2fd)。

`REQ`：接收 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="r_a6dbb848a229b52e1d0c005a142d1d2ac"></a>

```c
lin_response_t response
```

相关声明：[lin_response_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga42976918cdbcec388095d77e398e7633)、[response](#a6dbb848a229b52e1d0c005a142d1d2ac)。

`OPT`：响应收到的帧头，仅适用于响应方模式。

<a id="r_adda8aa06d38c6f788eaff9e00978f9a7"></a>

```c
lin_read_t read
```

相关声明：[lin_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gabcad96f6950ec45b71adfd14e4c0c363)、[read](#adda8aa06d38c6f788eaff9e00978f9a7)。

`OPT`：开始数据接收，仅适用于响应方模式。

<a id="r_a4740986a33d152d9b57505334ed0df6b"></a>

```c
lin_wakeup_send_t wakeup_send
```

相关声明：[lin_wakeup_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga16889d5f804b14ef80a608f6b8a86193)、[wakeup_send](#a4740986a33d152d9b57505334ed0df6b)。

`OPT`：发送 LIN 唤醒信号（Wakeup signal）。

<a id="r_a91891ea072a84183ee95f7038a728ded"></a>

```c
lin_set_event_callback_t set_event_callback
```

相关声明：[lin_set_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad1df29d89982f09a9652db231e36c0c4)、[set_event_callback](#a91891ea072a84183ee95f7038a728ded)。

`REQ`：设置 LIN 事件回调。

## 20.2\_详细说明（Detailed Documentation）

<a id="acf01655ffd47f72425ef385745700569"></a>

### `configure`

```c
lin_configure_t lin_driver_api::configure
```

`REQ`：配置 LIN 控制器。

<a id="ada6d4e2661d5b9352d218757a69c7b10"></a>

### `get_config`

```c
lin_get_config_t lin_driver_api::get_config
```

`REQ`：获取当前 LIN 配置。

<a id="adda8aa06d38c6f788eaff9e00978f9a7"></a>

### `read`

```c
lin_read_t lin_driver_api::read
```

`OPT`：开始数据接收，仅适用于响应方模式。

<a id="a4704606967b3eb5d7ed103e1cccfb2fd"></a>

### `receive`

```c
lin_receive_t lin_driver_api::receive
```

`REQ`：接收 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="a6dbb848a229b52e1d0c005a142d1d2ac"></a>

### `response`

```c
lin_response_t lin_driver_api::response
```

`OPT`：响应收到的帧头，仅适用于响应方模式。

<a id="af3321e6ce2a598a4bd123b968a608633"></a>

### `send`

```c
lin_send_t lin_driver_api::send
```

`REQ`：发送 LIN 消息，仅适用于命令方模式（Commander mode）。

<a id="a91891ea072a84183ee95f7038a728ded"></a>

### `set_event_callback`

```c
lin_set_event_callback_t lin_driver_api::set_event_callback
```

`REQ`：设置 LIN 事件回调。

<a id="a42abd5bd44fa028a4b2244131e5f17f4"></a>

### `set_rx_filter`

```c
lin_set_rx_filter_t lin_driver_api::set_rx_filter
```

`OPT`：设置 LIN 接收过滤器，仅适用于响应方模式（Responder mode）。

<a id="a538f1329573a0919ed908e58ec60c24e"></a>

### `start`

```c
lin_start_t lin_driver_api::start
```

`REQ`：启动 LIN 控制器。

<a id="a72c15ca01a63897758fab966be5f71fe"></a>

### `stop`

```c
lin_stop_t lin_driver_api::stop
```

`REQ`：停止 LIN 控制器。

<a id="a4740986a33d152d9b57505334ed0df6b"></a>

### `wakeup_send`

```c
lin_wakeup_send_t lin_driver_api::wakeup_send
```

`OPT`：发送 LIN 唤醒信号（Wakeup signal）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [lin_start_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga149ca3972fc800c4fd2bbb0b5d8a85e3)
- [lin_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab0f27d3ad3637f9040920b3088c1e239)
- [lin_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga39766c7605a50fcb600e9d72bfcf07d5)
- [lin_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga305d83d265245ed657a9974c0bab1962)
- [lin_set_rx_filter_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga727b0f7fe4949e3fd17a303e239586bb)
- [lin_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga8091d2d225709439f9afb2eddeb73792)
- [lin_receive_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad77d365c000a2f9c7f2558ec24d0f455)
- [lin_response_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga42976918cdbcec388095d77e398e7633)
- [lin_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gabcad96f6950ec45b71adfd14e4c0c363)
- [lin_wakeup_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga16889d5f804b14ef80a608f6b8a86193)
- [lin_set_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gad1df29d89982f09a9652db231e36c0c4)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_lin_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_lin_driver_config_结构体.md)
