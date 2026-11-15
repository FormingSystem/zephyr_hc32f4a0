---
id: learning.zephyr-docs.api-file-configuration-reference.page-76
title: zephyr__drivers__uart_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_zephyr\_\_drivers\_\_uart\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uart__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

UART设备仿真驱动（Device Emulation Drivers）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

UART设备仿真驱动（Device Emulation Drivers）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 76.1\_数据结构（Data Structures）

<a id="r_uart_5Femul"></a>

```c
struct uart_emul
```

相关声明：[uart_emul](../hardware/P342_UART模拟器结构.md)。

UART设备仿真器链表（Linked List）中的节点。

<a id="r_uart_5Femul_5Fdevice_5Fapi"></a>

```c
struct uart_emul_device_api
```

相关声明：[uart_emul_device_api](../hardware/P343_UART模拟函数表.md)。

仿真器（Emulator）API的定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 76.2\_类型定义（Typedefs）

<a id="r_gab4b5940f6e0c55c594a9ccddae04c8ae"></a>

```c
typedef void(* uart_emul_device_tx_data_ready_t) (const struct device *dev, size_t size, const struct emul *target)
```

相关声明：[uart_emul_device_tx_data_ready_t](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gab4b5940f6e0c55c594a9ccddae04c8ae)、[device](../device_reference/P002_设备对象结构.md)、[emul](../hardware/P477_仿真器实例结构.md)。

定义仿真回调函数签名（Emulation Callback Function Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 76.3\_函数（Functions）

<a id="r_gaa457b7ca5ac20a588a6fce562221e824"></a>

```c
int uart_emul_register (const struct device *dev, struct uart_emul *emul)
```

相关声明：[uart_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gaa457b7ca5ac20a588a6fce562221e824)、[device](../device_reference/P002_设备对象结构.md)、[uart_emul](../hardware/P342_UART模拟器结构.md)、[emul](../hardware/P477_仿真器实例结构.md)。

在控制器（Controller）上注册仿真设备（Emulated Device）。


## 76.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P002_UART驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P880_uart_emul.h_源码浏览.md)
- [uart_emul](../hardware/P342_UART模拟器结构.md)
- [uart_emul_device_api](../hardware/P343_UART模拟函数表.md)
- [uart_emul_device_tx_data_ready_t](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gab4b5940f6e0c55c594a9ccddae04c8ae)
- [device](../device_reference/P002_设备对象结构.md)
- [emul](../hardware/P477_仿真器实例结构.md)
- [uart_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__emul__interface.html#gaa457b7ca5ac20a588a6fce562221e824)

<a id="header-details"></a>

---

[上一章](P075_zephyr__drivers__haptics__tm6605.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P077_zephyr__usb__class__usbd_msc.h_文件参考.md)
