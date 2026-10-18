---
id: learning.zephyr-docs.api-file-service-interface-reference.page-6
title: zephyr__mgmt__ec_host_cmd__backend.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_mgmt\_\_ec\_host\_cmd\_\_backend.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

响应主机命令的主机命令后端（Host Command Backends）的公共API。

<a id="details"></a>

```c
#include <zephyr/sys/__assert.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
```

查看此文件的源码。

响应主机命令的主机命令后端（Host Command Backends）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

## 6.2\_类型定义（Typedefs）

<a id="r_ga811b9c355942811f0fee22c1fa8a5787"></a>

```c
typedef int(* ec_host_cmd_backend_api_init) (const struct ec_host_cmd_backend *backend, struct ec_host_cmd_rx_ctx *rx_ctx, struct ec_host_cmd_tx_buf *tx)
```

相关声明：[ec_host_cmd_backend_api_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga811b9c355942811f0fee22c1fa8a5787)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)、[ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)。

初始化主机命令后端（Host Command Backend）。

<a id="r_ga1097b2148a5e7e6bf9f2a67e54dd5ba5"></a>

```c
typedef int(* ec_host_cmd_backend_api_send) (const struct ec_host_cmd_backend *backend)
```

相关声明：[ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)、[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)。

向主机（Host）发送数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_ga32d7a58724694ab753efbf7f81e8d940"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_espi (const struct device *dev)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_espi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga32d7a58724694ab753efbf7f81e8d940)、[device](../device_reference/P002_设备对象结构.md)。

获取 eSPI 主机命令后端（Host Command Backend）的指针。

<a id="r_gaa4562dd46503cf8844a546b102ce01e9"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_npcx (void)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_shi_npcx](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaa4562dd46503cf8844a546b102ce01e9)。

获取 SHI NPCX 主机命令后端（Host Command Backend）的指针。

<a id="r_ga892fec4587de508805fdf5ace9dd1050"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_shi_ite (void)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_shi_ite](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga892fec4587de508805fdf5ace9dd1050)。

获取 SHI ITE 主机命令后端（Host Command Backend）的指针。

<a id="r_ga558b7690dad9a9a5eb8771fcfeba3b63"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_uart (const struct device *dev)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_uart](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga558b7690dad9a9a5eb8771fcfeba3b63)、[device](../device_reference/P002_设备对象结构.md)。

获取 UART 主机命令后端（Host Command Backend）的指针。

<a id="r_ga12574d2eff8f07fd36967ccbc7600e1c"></a>

```c
struct ec_host_cmd_backend * ec_host_cmd_backend_get_spi (struct gpio_dt_spec *cs)
```

相关声明：[ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)、[ec_host_cmd_backend_get_spi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga12574d2eff8f07fd36967ccbc7600e1c)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)。

获取 SPI 主机命令后端（Host Command Backend）的指针。

<a id="r_gaba4d3e1fd2b723448be2cb4b7f6293ac"></a>

```c
void ec_host_cmd_backend_usb_trigger_event (void)
```

相关声明：[ec_host_cmd_backend_usb_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaba4d3e1fd2b723448be2cb4b7f6293ac)。

通过 USB 发出事件信号（Signal Event）。


## 6.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P050_backend.h_源码浏览.md)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [ec_host_cmd_backend_api](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md)
- [ec_host_cmd_backend_api_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga811b9c355942811f0fee22c1fa8a5787)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [ec_host_cmd_backend_get_espi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga32d7a58724694ab753efbf7f81e8d940)
- [device](../device_reference/P002_设备对象结构.md)
- [ec_host_cmd_backend_get_shi_npcx](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaa4562dd46503cf8844a546b102ce01e9)
- [ec_host_cmd_backend_get_shi_ite](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga892fec4587de508805fdf5ace9dd1050)
- [ec_host_cmd_backend_get_uart](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga558b7690dad9a9a5eb8771fcfeba3b63)
- [ec_host_cmd_backend_get_spi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga12574d2eff8f07fd36967ccbc7600e1c)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [ec_host_cmd_backend_usb_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaba4d3e1fd2b723448be2cb4b7f6293ac)

<a id="header-details"></a>

---

[上一章](P005_zephyr__dt-bindings__interrupt-controller__arm-gic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dsp__basicmath.h_文件参考.md)
