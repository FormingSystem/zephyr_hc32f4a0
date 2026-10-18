---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-12
title: zephyr__pmci__mctp__mctp_uart.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_uart.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于Zephyr异步UART接口的MCTP总线绑定（Bus Binding）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <libmctp.h>
```

查看此文件的源码。

基于Zephyr异步UART接口的MCTP总线绑定（Bus Binding）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_mctp_5Fbinding_5Fuart"></a>

```c
struct mctp_binding_uart
```

相关声明：[mctp_binding_uart](../peripheral_bus_storage_model_reference/P030_mctp_binding_uart_结构体.md)。

Zephyr异步UART接口的管理组件传输协议（MCTP）绑定。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_a2678ea91b3b7f2a0a4f2f3c8618c8d72"></a>

```c
#define MCTP_UART_DT_DEFINE(_name, _dev)
```

相关声明：[MCTP_UART_DT_DEFINE](#a2678ea91b3b7f2a0a4f2f3c8618c8d72)。

静态定义 UART 的 MCTP 总线绑定。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_ad4c5c12a116c6b1ed671887c5bd7ff94"></a>

```c
void mctp_uart_start_rx (struct mctp_binding_uart *uart)
```

相关声明：[mctp_uart_start_rx](#ad4c5c12a116c6b1ed671887c5bd7ff94)、[mctp_binding_uart](../peripheral_bus_storage_model_reference/P030_mctp_binding_uart_结构体.md)。

开始接收 MCTP 消息。

<a id="r_aee9f5132cc9cfbc3c5223a89e59dc667"></a>

```c
int mctp_uart_stop_rx (struct mctp_binding_uart *uart)
```

相关声明：[mctp_uart_stop_rx](#aee9f5132cc9cfbc3c5223a89e59dc667)、[mctp_binding_uart](../peripheral_bus_storage_model_reference/P030_mctp_binding_uart_结构体.md)。

停止接收 MCTP 消息。

## 12.4\_详细说明（Detailed Documentation）

<a id="a2678ea91b3b7f2a0a4f2f3c8618c8d72"></a>

### `MCTP_UART_DT_DEFINE`

```c
#define MCTP_UART_DT_DEFINE ( _name, _dev )
```

展开值（Value）：

```c
struct mctp_binding_uart _name = {                                                         \
        .binding =                                                                         \
                {                                                                          \
                        .name = STRINGIFY(_name), .version = 1,                            \
                                          .pkt_size = MCTP_PACKET_SIZE(MCTP_BTU),          \
                                          .pkt_header = 0, .pkt_trailer = 0,               \
                                          .tx_storage = _name.tx_storage,          \
                                          .start = mctp_uart_start, .tx = mctp_uart_tx,    \
                        },                                                                 \
                        .dev = _dev,                                                       \
                        .rx_state = STATE_WAIT_SYNC_START,                                 \
                        .rx_pkt = NULL,                                                    \
                        .rx_res = 0,                                                       \
                        .tx_res = 0,                                                       \
};
```

静态定义 UART 的 MCTP 总线绑定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 总线绑定变量的符号名称（Symbolic name）。 |
| `_dev` | UART 设备。 |

<a id="ad4c5c12a116c6b1ed671887c5bd7ff94"></a>

### `mctp_uart_start_rx()`

```c
void mctp_uart_start_rx ( struct mctp_binding_uart * uart)
```

开始接收 MCTP 消息。

将从 UART 读取 MCTP 消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uart` | MCTP UART 绑定（Binding）。 |

<a id="aee9f5132cc9cfbc3c5223a89e59dc667"></a>

### `mctp_uart_stop_rx()`

```c
int mctp_uart_stop_rx ( struct mctp_binding_uart * uart)
```

停止接收 MCTP 消息。

将停止从 UART 读取 MCTP 消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uart` | MCTP UART 绑定（Binding）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回 `uart_rx_disable` 的结果。 |

**参阅（See Also）**：另请参阅 `uart_rx_disable`。


## 12.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h_source.html)
- [mctp_binding_uart](../peripheral_bus_storage_model_reference/P030_mctp_binding_uart_结构体.md)
- [uart_rx_disable](../hardware/P334_UART异步接口.md#gafd4753bee51b230091a3c6ddb26ea734)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructmctp__binding__uart_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md)
