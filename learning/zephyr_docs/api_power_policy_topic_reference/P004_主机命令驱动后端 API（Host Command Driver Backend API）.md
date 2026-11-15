---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-4
title: 主机命令驱动后端 API（Host Command Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_主机命令驱动后端 API（Host Command Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现主机命令驱动（Host Command Driver）所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口（Helpers）。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_backend_2Eh"></a>

```c
file backend.h
```

相关声明：[backend.h](../api_file_service_interface_reference/P006_zephyr__mgmt__ec_host_cmd__backend.h_文件参考.md)。

响应主机命令的主机命令后端（Host Command Backends）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

<a id="r_ec_5Fhost_5Fcmd_5Fbackend"></a>

```c
struct ec_host_cmd_backend
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)。

嵌入式控制器（EC）的主机命令后端（Host Command Backend）。

<a id="r_ec_5Fhost_5Fcmd_5Frx_5Fctx"></a>

```c
struct ec_host_cmd_rx_ctx
```

相关声明：[ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)。

主机命令后端与处理程序用于传递接收（RX）数据的上下文。

<a id="r_ec_5Fhost_5Fcmd_5Ftx_5Fbuf"></a>

```c
struct ec_host_cmd_tx_buf
```

相关声明：[ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)。

主机命令后端与处理程序用于传递发送（TX）数据的上下文。

<a id="r_ec_5Fhost_5Fcmd_5Fbackend_5Fapi"></a>

```c
struct ec_host_cmd_backend_api
```

相关声明：[ec_host_cmd_backend_api](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md)。

驱动操作（Driver Operations）：主机命令（Host Command）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_ga811b9c355942811f0fee22c1fa8a5787"></a>

```c
typedef int(* ec_host_cmd_backend_api_init) (const struct ec_host_cmd_backend *backend, struct ec_host_cmd_rx_ctx *rx_ctx, struct ec_host_cmd_tx_buf *tx)
```

相关声明：[ec_host_cmd_backend_api_init](#ga811b9c355942811f0fee22c1fa8a5787)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)、[ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)。

初始化主机命令后端（Host Command Backend）。

<a id="r_ga1097b2148a5e7e6bf9f2a67e54dd5ba5"></a>

```c
typedef int(* ec_host_cmd_backend_api_send) (const struct ec_host_cmd_backend *backend)
```

相关声明：[ec_host_cmd_backend_api_send](#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)。

向主机（Host）发送数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga32d7a58724694ab753efbf7f81e8d940"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_espi (const struct device *dev)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_espi](#ga32d7a58724694ab753efbf7f81e8d940)、[device](../device_reference/P002_设备对象结构.md)。

获取 eSPI 主机命令后端（Host Command Backend）的指针。

<a id="r_gaa4562dd46503cf8844a546b102ce01e9"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_npcx (void)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_shi_npcx](#gaa4562dd46503cf8844a546b102ce01e9)。

获取 SHI NPCX 主机命令后端（Host Command Backend）的指针。

<a id="r_ga892fec4587de508805fdf5ace9dd1050"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_ite (void)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_shi_ite](#ga892fec4587de508805fdf5ace9dd1050)。

获取 SHI ITE 主机命令后端（Host Command Backend）的指针。

<a id="r_ga558b7690dad9a9a5eb8771fcfeba3b63"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_uart (const struct device *dev)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_uart](#ga558b7690dad9a9a5eb8771fcfeba3b63)、[device](../device_reference/P002_设备对象结构.md)。

获取 UART 主机命令后端（Host Command Backend）的指针。

<a id="r_ga12574d2eff8f07fd36967ccbc7600e1c"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_spi (struct gpio_dt_spec *cs)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_spi](#ga12574d2eff8f07fd36967ccbc7600e1c)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

获取 SPI 主机命令后端（Host Command Backend）的指针。

<a id="r_gaba4d3e1fd2b723448be2cb4b7f6293ac"></a>

```c
void ec_host_cmd_backend_usb_trigger_event (void)
```

相关声明：[ec_host_cmd_backend_usb_trigger_event](#gaba4d3e1fd2b723448be2cb4b7f6293ac)。

通过 USB 发出事件信号（Signal Event）。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga811b9c355942811f0fee22c1fa8a5787"></a>

### `ec_host_cmd_backend_api_init`

```c
typedef int(* ec_host_cmd_backend_api_init) (const struct ec_host_cmd_backend *backend, struct ec_host_cmd_rx_ctx *rx_ctx, struct ec_host_cmd_tx_buf *tx)
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

初始化主机命令后端（Host Command Backend）。

本例程初始化主机命令后端（Host Command Backend），包括初始化通信所用设备及设置缓冲区。由 `ec_host_cmd_init` 调用本函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] backend` | 指向驱动实例后端结构体（Backend Structure）的指针。 |
| `[in,out] rx_ctx` | 指向接收上下文对象（Receive Context Object）的指针。主机发送数据时，这些对象用于从驱动接收数据。`buf` 成员可由后端赋值。 |
| `[in,out] tx` | 指向发送缓冲区对象（Transmit Buffer Object）的指针。`buf` 和 `len_max` 成员可由后端赋值；后端通过 `ec_host_cmd_backend_api_send` 使用这些对象发送数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga1097b2148a5e7e6bf9f2a67e54dd5ba5"></a>

### `ec_host_cmd_backend_api_send`

```c
typedef int(* ec_host_cmd_backend_api_send) (const struct ec_host_cmd_backend *backend)
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

向主机（Host）发送数据。

从通过 `ec_host_cmd_backend_api_init` 传入的发送缓冲区（TX Buffer）发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `backend` | 指向负责发送数据的后端（Backend）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="ga32d7a58724694ab753efbf7f81e8d940"></a>

### `ec_host_cmd_backend_get_espi()`

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_espi ( const struct device * dev)
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

获取 eSPI 主机命令后端（Host Command Backend）的指针。

获取 eSPI 后端指针（Backend Pointer），并传入将用于主机命令（Host Command）通信的 eSPI 设备实例指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 eSPI 设备实例（Device Instance）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | eSPI 后端指针（Backend Pointer）。 |

<a id="ga892fec4587de508805fdf5ace9dd1050"></a>

### `ec_host_cmd_backend_get_shi_ite()`

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_ite ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

获取 SHI ITE 主机命令后端（Host Command Backend）的指针。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `the` | SHI ITE 后端指针（Backend Pointer）。 |

<a id="gaa4562dd46503cf8844a546b102ce01e9"></a>

### `ec_host_cmd_backend_get_shi_npcx()`

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_npcx ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

获取 SHI NPCX 主机命令后端（Host Command Backend）的指针。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `the` | SHI NPCX 后端指针（Backend Pointer）。 |

<a id="ga12574d2eff8f07fd36967ccbc7600e1c"></a>

### `ec_host_cmd_backend_get_spi()`

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_spi ( struct gpio_dt_spec * cs)
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

获取 SPI 主机命令后端（Host Command Backend）的指针。

获取 SPI 后端指针（Backend Pointer），并传入将用于主机命令（Host Command）通信的片选引脚（Chip Select Pin）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cs` | 片选引脚（Chip Select Pin）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | SPI 后端指针（Backend Pointer）。 |

<a id="ga558b7690dad9a9a5eb8771fcfeba3b63"></a>

### `ec_host_cmd_backend_get_uart()`

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_uart ( const struct device * dev)
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

获取 UART 主机命令后端（Host Command Backend）的指针。

获取 UART 后端指针（Backend Pointer），并传入将用于主机命令（Host Command）通信的 UART 设备实例指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 UART 设备实例（Device Instance）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `The` | UART 后端指针（Backend Pointer）。 |

<a id="gaba4d3e1fd2b723448be2cb4b7f6293ac"></a>

### `ec_host_cmd_backend_usb_trigger_event()`

```c
void ec_host_cmd_backend_usb_trigger_event ( void )
```

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

通过 USB 发出事件信号（Signal Event）。

使用 USB 中断端点（Interrupt Endpoint）发出事件信号，通知主机有待处理事件。必要时执行远程唤醒（Remote Wake-up）。


## 4.6\_原页交叉引用（Cross References）

- [backend.h](../api_file_service_interface_reference/P006_zephyr__mgmt__ec_host_cmd__backend.h_文件参考.md)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [ec_host_cmd_backend_api](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙人机接口设备（Bluetooth HID）.md) · [返回大纲](大纲.md) · [下一章](P005_HTU31D API主题.md)
