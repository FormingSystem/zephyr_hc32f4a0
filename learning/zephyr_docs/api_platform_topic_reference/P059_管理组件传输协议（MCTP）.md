---
id: learning.zephyr-docs.api-platform-topic-reference.page-59
title: 管理组件传输协议（MCTP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mctp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_管理组件传输协议（MCTP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mctp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理组件传输协议（Management Component Transport Protocol，MCTP）

<a id="details"></a>

管理组件传输协议（Management Component Transport Protocol，MCTP）。将 Zephyr 传输层（Transports）连接到 libmctp 协议栈（Protocol Stack）的总线绑定（Bus Bindings）。

<a id="header-files"></a>
<a id="files"></a>

## 59.1\_文件（Files）

<a id="r_mctp_5Fi2c_5Fgpio_5Fcommon_2Eh"></a>

```c
file mctp_i2c_gpio_common.h
```

相关声明：[mctp_i2c_gpio_common.h](../api_file_reference/P214_zephyr__pmci__mctp__mctp_i2c_gpio_common.h_文件参考.md)。

MCTP I2C GPIO控制器与目标绑定（Controller and Target Bindings）共享的内部定义。

<a id="r_mctp_5Fi2c_5Fgpio_5Fcontroller_2Eh"></a>

```c
file mctp_i2c_gpio_controller.h
```

相关声明：[mctp_i2c_gpio_controller.h](../peripheral_bus_storage_header_reference/P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md)。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于控制器端。

<a id="r_mctp_5Fi2c_5Fgpio_5Ftarget_2Eh"></a>

```c
file mctp_i2c_gpio_target.h
```

相关声明：[mctp_i2c_gpio_target.h](../peripheral_bus_storage_header_reference/P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md)。

基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于目标端。

<a id="r_mctp_5Fi3c_5Fcommon_2Eh"></a>

```c
file mctp_i3c_common.h
```

相关声明：[mctp_i3c_common.h](../api_file_reference/P215_zephyr__pmci__mctp__mctp_i3c_common.h_文件参考.md)。

MCTP I3C控制器与目标绑定（Controller and Target Bindings）共享的内部定义。

<a id="r_mctp_5Fi3c_5Fcontroller_2Eh"></a>

```c
file mctp_i3c_controller.h
```

相关声明：[mctp_i3c_controller.h](../peripheral_bus_storage_header_reference/P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md)。

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于控制器端。

<a id="r_mctp_5Fi3c_5Fendpoint_2Eh"></a>

```c
file mctp_i3c_endpoint.h
```

相关声明：[mctp_i3c_endpoint.h](../api_file_reference/P216_zephyr__pmci__mctp__mctp_i3c_endpoint.h_文件参考.md)。

MCTP I3C端点设备（Endpoint Devices）的内部驱动API。

<a id="r_mctp_5Fi3c_5Ftarget_2Eh"></a>

```c
file mctp_i3c_target.h
```

相关声明：[mctp_i3c_target.h](../peripheral_bus_storage_header_reference/P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md)。

基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于目标端。

<a id="r_mctp_5Fmemory_2Eh"></a>

```c
file mctp_memory.h
```

相关声明：[mctp_memory.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h.html)。

MCTP内存管理函数（Memory Management Functions）。

<a id="r_mctp_5Fuart_2Eh"></a>

```c
file mctp_uart.h
```

相关声明：[mctp_uart.h](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md)。

基于Zephyr异步UART接口的MCTP总线绑定（Bus Binding）。

<a id="r_mctp_5Fusb_2Eh"></a>

```c
file mctp_usb.h
```

相关声明：[mctp_usb.h](../peripheral_bus_storage_header_reference/P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md)。

基于Zephyr USB设备协议栈的MCTP总线绑定（Bus Binding）。


## 59.2\_原页交叉引用（Cross References）

- [mctp_i2c_gpio_common.h](../api_file_reference/P214_zephyr__pmci__mctp__mctp_i2c_gpio_common.h_文件参考.md)
- [mctp_i2c_gpio_controller.h](../peripheral_bus_storage_header_reference/P008_zephyr__pmci__mctp__mctp_i2c_gpio_controller.h_头文件参考.md)
- [mctp_i2c_gpio_target.h](../peripheral_bus_storage_header_reference/P009_zephyr__pmci__mctp__mctp_i2c_gpio_target.h_头文件参考.md)
- [mctp_i3c_common.h](../api_file_reference/P215_zephyr__pmci__mctp__mctp_i3c_common.h_文件参考.md)
- [mctp_i3c_controller.h](../peripheral_bus_storage_header_reference/P010_zephyr__pmci__mctp__mctp_i3c_controller.h_头文件参考.md)
- [mctp_i3c_endpoint.h](../api_file_reference/P216_zephyr__pmci__mctp__mctp_i3c_endpoint.h_文件参考.md)
- [mctp_i3c_target.h](../peripheral_bus_storage_header_reference/P011_zephyr__pmci__mctp__mctp_i3c_target.h_头文件参考.md)
- [mctp_memory.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h.html)
- [mctp_uart.h](../peripheral_bus_storage_header_reference/P012_zephyr__pmci__mctp__mctp_uart.h_头文件参考.md)
- [mctp_usb.h](../peripheral_bus_storage_header_reference/P013_zephyr__pmci__mctp__mctp_usb.h_头文件参考.md)

<a id="header-details"></a>

---

[上一章](P058_MAX17055 API主题.md) · [返回大纲](大纲.md) · [下一章](P060_调制解调器 API（Modem APIs）.md)
