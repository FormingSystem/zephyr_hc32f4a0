---
id: learning.zephyr-docs.api-file-interface-reference.page-61
title: zephyr__usb__class__usb_hid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_zephyr\_\_usb\_\_class\_\_usb\_hid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__hid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB人机接口设备类（HID Class）设备API的头文件。

<a id="details"></a>

```c
#include <zephyr/usb/class/hid.h>
#include <zephyr/usb/usb_ch9.h>
```

查看此文件的源码。

USB人机接口设备类（HID Class）设备API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 61.1\_数据结构（Data Structures）

<a id="r_hid_5Fops"></a>

```c
struct hid_ops
```

相关声明：[hid_ops](../usb/P047_旧版HID回调接口.md)。

USB人机接口设备（HID）的接口。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 61.2\_类型定义（Typedefs）

<a id="r_ga04ec088255198d1597df8d70db6257ee"></a>

```c
typedef int(* hid_cb_t) (const struct device *dev, struct usb_setup_packet *setup, int32_t *len, uint8_t **data)
```

相关声明：[hid_cb_t](../usb/P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)、[device](../device_reference/P002_设备对象结构.md)、[usb_setup_packet](../usb/P160_USB控制请求包.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaed433e24f8487d4e451d9f9daa08c5b0"></a>

```c
typedef void(* hid_int_ready_callback) (const struct device *dev)
```

相关声明：[hid_int_ready_callback](../usb/P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gae3d308c55f5594cc0c926b52aaa28fc7"></a>

```c
typedef void(* hid_protocol_cb_t) (const struct device *dev, uint8_t protocol)
```

相关声明：[hid_protocol_cb_t](../usb/P046_旧版HID设备接口API.md#gae3d308c55f5594cc0c926b52aaa28fc7)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga61b4facfbfb729159135f5c7534ca593"></a>

```c
typedef void(* hid_idle_cb_t) (const struct device *dev, uint16_t report_id)
```

相关声明：[hid_idle_cb_t](../usb/P046_旧版HID设备接口API.md#ga61b4facfbfb729159135f5c7534ca593)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 61.3\_函数（Functions）

<a id="r_ga8b08b633472ceb1323f09ef81176520f"></a>

```c
void usb_hid_register_device (const struct device *dev, const uint8_t *desc, size_t size, const struct hid_ops *op)
```

相关声明：[usb_hid_register_device](../usb/P046_旧版HID设备接口API.md#ga8b08b633472ceb1323f09ef81176520f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hid_ops](../usb/P047_旧版HID回调接口.md)。

注册人机接口设备（HID device）。

<a id="r_ga9d82d48c9c6c94ad90e01f44c1f0e72b"></a>

```c
int hid_int_ep_write (const struct device *dev, const uint8_t *data, uint32_t data_len, uint32_t *bytes_ret)
```

相关声明：[hid_int_ep_write](../usb/P046_旧版HID设备接口API.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 USB HID 中断端点（interrupt endpoint）缓冲区写入数据。

<a id="r_ga7d1b97dd70c25c816a2c78447be13c84"></a>

```c
int hid_int_ep_read (const struct device *dev, uint8_t *data, uint32_t max_data_len, uint32_t *ret_bytes)
```

相关声明：[hid_int_ep_read](../usb/P046_旧版HID设备接口API.md#ga7d1b97dd70c25c816a2c78447be13c84)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 USB HID 中断端点缓冲区读取数据。

<a id="r_gafb6073889bf17eb6a93bb8f182cd3f79"></a>

```c
int usb_hid_set_proto_code (const struct device *dev, uint8_t proto_code)
```

相关声明：[usb_hid_set_proto_code](../usb/P046_旧版HID设备接口API.md#gafb6073889bf17eb6a93bb8f182cd3f79)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 USB HID 类的协议代码（Protocol Code）。

<a id="r_ga88c23fc42f45f4ac05d9b2c1f6d7ec9b"></a>

```c
int usb_hid_init (const struct device *dev)
```

相关声明：[usb_hid_init](../usb/P046_旧版HID设备接口API.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)、[device](../device_reference/P002_设备对象结构.md)。

初始化 USB HID 类支持。


## 61.4\_原页交叉引用（Cross References）

- [zephyr/usb/class/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h_source.html)
- [zephyr/usb/usb_ch9.h](../usb/P173_USB第9章头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P237_usb_hid.h_源码浏览.md)
- [hid_ops](../usb/P047_旧版HID回调接口.md)
- [hid_cb_t](../usb/P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)
- [device](../device_reference/P002_设备对象结构.md)
- [usb_setup_packet](../usb/P160_USB控制请求包.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [hid_int_ready_callback](../usb/P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)
- [hid_protocol_cb_t](../usb/P046_旧版HID设备接口API.md#gae3d308c55f5594cc0c926b52aaa28fc7)
- [hid_idle_cb_t](../usb/P046_旧版HID设备接口API.md#ga61b4facfbfb729159135f5c7534ca593)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [usb_hid_register_device](../usb/P046_旧版HID设备接口API.md#ga8b08b633472ceb1323f09ef81176520f)
- [hid_int_ep_write](../usb/P046_旧版HID设备接口API.md#ga9d82d48c9c6c94ad90e01f44c1f0e72b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [hid_int_ep_read](../usb/P046_旧版HID设备接口API.md#ga7d1b97dd70c25c816a2c78447be13c84)
- [usb_hid_set_proto_code](../usb/P046_旧版HID设备接口API.md#gafb6073889bf17eb6a93bb8f182cd3f79)
- [usb_hid_init](../usb/P046_旧版HID设备接口API.md#ga88c23fc42f45f4ac05d9b2c1f6d7ec9b)

<a id="header-details"></a>

---

[上一章](P060_zephyr__drivers__console__uart_console.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P062_zephyr__drivers__usb_c__usbc_vbus.h_文件参考.md)
