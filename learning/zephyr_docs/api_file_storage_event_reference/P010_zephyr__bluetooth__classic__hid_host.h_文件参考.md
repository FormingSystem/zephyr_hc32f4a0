---
id: learning.zephyr-docs.api-file-storage-event-reference.page-10
title: zephyr__bluetooth__classic__hid_host.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_bluetooth\_\_classic\_\_hid\_host.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hid__host_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

人机接口主机端协议（HID Host Protocol）的处理。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/bluetooth/classic/hid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

人机接口主机端协议（HID Host Protocol）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_bt_5Fhid_5Fhost_5Fcb"></a>

```c
struct bt_hid_host_cb
```

相关声明：[bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)。

由人机接口设备主机（HID Host）应用提供的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.2\_函数（Functions）

<a id="r_ga86d49efef335609422f23b52717c9e1b"></a>

```c
int bt_hid_host_register (const struct bt_hid_host_cb *cb)
```

相关声明：[bt_hid_host_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga86d49efef335609422f23b52717c9e1b)、[bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)。

注册 HID 主机回调（Host Callbacks）。

<a id="r_gaf1998a703fcf34e51e051a7a4c42937b"></a>

```c
int bt_hid_host_unregister (void)
```

相关声明：[bt_hid_host_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gaf1998a703fcf34e51e051a7a4c42937b)。

注销 HID 主机回调（Host Callbacks）。

<a id="r_ga8911b406dff5b2a0dd21f9abe3a571d5"></a>

```c
int bt_hid_host_connect (struct bt_conn *conn, struct bt_hid_host **hid)
```

相关声明：[bt_hid_host_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga8911b406dff5b2a0dd21f9abe3a571d5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

向远程 HID 设备（Device）发起 HID 连接。

<a id="r_ga5061be29cffeb76c1be0c5f7912f4cc8"></a>

```c
struct bt_conn * bt_hid_host_get_conn (struct bt_hid_host *hid)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hid_host_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga5061be29cffeb76c1be0c5f7912f4cc8)。

获取 HID 关联（Association）的 ACL 连接。

<a id="r_gac0101a4f54d50d6615fc7cce41044107"></a>

```c
int bt_hid_host_disconnect (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gac0101a4f54d50d6615fc7cce41044107)。

断开 HID 关联（Association）。

<a id="r_gae52c3d2ed7dd2a6868f9dff584ac2da4"></a>

```c
int bt_hid_host_get_report (struct bt_hid_host *hid, uint8_t type, uint8_t report_id, uint16_t buffer_size)
```

相关声明：[bt_hid_host_get_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae52c3d2ed7dd2a6868f9dff584ac2da4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 HID 设备发送 `GET_REPORT` 请求。

<a id="r_ga2a7d73c8ad7faff0ece2217f35757576"></a>

```c
int bt_hid_host_set_report (struct bt_hid_host *hid, uint8_t type, struct net_buf *buf)
```

相关声明：[bt_hid_host_set_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga2a7d73c8ad7faff0ece2217f35757576)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 HID 设备发送 `SET_REPORT` 请求。

<a id="r_ga45726162f45815aa9c2dc789e3b2beed"></a>

```c
int bt_hid_host_get_protocol (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_get_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga45726162f45815aa9c2dc789e3b2beed)。

向 HID 设备发送 `GET_PROTOCOL` 请求。

<a id="r_gae13a5ae2473c239b4b109cd8e5b9a210"></a>

```c
int bt_hid_host_set_protocol (struct bt_hid_host *hid, uint8_t protocol)
```

相关声明：[bt_hid_host_set_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae13a5ae2473c239b4b109cd8e5b9a210)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 HID 设备发送 `SET_PROTOCOL` 请求。

<a id="r_ga0415ec8597cb6ccc1016703438ac4f48"></a>

```c
int bt_hid_host_output_report (struct bt_hid_host *hid, struct net_buf *buf)
```

相关声明：[bt_hid_host_output_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga0415ec8597cb6ccc1016703438ac4f48)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在中断通道（Interrupt Channel）发送输出报告（Output Report）。

<a id="r_ga15db8aa5b2e56048a7e513730918ef50"></a>

```c
int bt_hid_host_suspend (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga15db8aa5b2e56048a7e513730918ef50)。

向 HID 设备发送 `SUSPEND` 控制消息。

<a id="r_ga80472c16b68cfb7d1e8d9f73379e612a"></a>

```c
int bt_hid_host_exit_suspend (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_exit_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga80472c16b68cfb7d1e8d9f73379e612a)。

向 HID 设备发送 `EXIT_SUSPEND` 控制消息。

<a id="r_ga6f7f967c1aa2cd15ba434fda1584b511"></a>

```c
int bt_hid_host_virtual_cable_unplug (struct bt_hid_host *hid)
```

相关声明：[bt_hid_host_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga6f7f967c1aa2cd15ba434fda1584b511)。

向 HID 设备发送虚拟线缆拔除（Virtual Cable Unplug）消息。

<a id="r_ga66ce643cbff7dbeb7dc4d4fe2b5476d7"></a>

```c
struct net_buf * bt_hid_host_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hid_host_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga66ce643cbff7dbeb7dc4d4fe2b5476d7)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 HID 主机发送分配 PDU 缓冲区（PDU Buffer）。


## 10.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/classic/hid.h](../api_source_reference/P070_hid.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P319_hid_host.h_源码浏览.md)
- [bt_hid_host_cb](../bluetooth_service_model_reference/P092_bt_hid_host_cb_结构体.md)
- [bt_hid_host_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga86d49efef335609422f23b52717c9e1b)
- [bt_hid_host_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gaf1998a703fcf34e51e051a7a4c42937b)
- [bt_hid_host_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga8911b406dff5b2a0dd21f9abe3a571d5)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hid_host_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga5061be29cffeb76c1be0c5f7912f4cc8)
- [bt_hid_host_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gac0101a4f54d50d6615fc7cce41044107)
- [bt_hid_host_get_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae52c3d2ed7dd2a6868f9dff584ac2da4)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hid_host_set_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga2a7d73c8ad7faff0ece2217f35757576)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hid_host_get_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga45726162f45815aa9c2dc789e3b2beed)
- [bt_hid_host_set_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#gae13a5ae2473c239b4b109cd8e5b9a210)
- [bt_hid_host_output_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga0415ec8597cb6ccc1016703438ac4f48)
- [bt_hid_host_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga15db8aa5b2e56048a7e513730918ef50)
- [bt_hid_host_exit_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga80472c16b68cfb7d1e8d9f73379e612a)
- [bt_hid_host_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga6f7f967c1aa2cd15ba434fda1584b511)
- [bt_hid_host_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html#ga66ce643cbff7dbeb7dc4d4fe2b5476d7)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)

<a id="header-details"></a>

---

[上一章](P009_zephyr__bluetooth__audio__gmap_lc3_preset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__platform__hooks.h_文件参考.md)
