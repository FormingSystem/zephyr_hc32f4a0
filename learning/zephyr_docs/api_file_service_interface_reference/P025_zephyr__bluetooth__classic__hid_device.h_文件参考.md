---
id: learning.zephyr-docs.api-file-service-interface-reference.page-25
title: zephyr__bluetooth__classic__hid_device.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_bluetooth\_\_classic\_\_hid\_device.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hid__device_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

人机接口设备端协议（HID Device Protocol）的处理。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/bluetooth/classic/hid.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

人机接口设备端协议（HID Device Protocol）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_bt_5Fhid_5Fdevice_5Fcb"></a>

```c
struct bt_hid_device_cb
```

相关声明：[bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)。

由人机接口设备（HID）应用提供的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_ga296d1b9695091507438261035d067c02"></a>

```c
int bt_hid_device_register (const struct bt_hid_device_cb *cb)
```

相关声明：[bt_hid_device_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga296d1b9695091507438261035d067c02)、[bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)。

注册人机接口设备（HID）回调。

<a id="r_ga35b0ec48658daa94010bef0c91503491"></a>

```c
int bt_hid_device_unregister (void)
```

相关声明：[bt_hid_device_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga35b0ec48658daa94010bef0c91503491)。

注销 HID 设备回调并禁用 HID 服务。

<a id="r_gaf30d808e9903988d72d831c3c4aab617"></a>

```c
int bt_hid_device_connect (struct bt_conn *conn, struct bt_hid_device **hid)
```

相关声明：[bt_hid_device_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gaf30d808e9903988d72d831c3c4aab617)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

在指定连接上发起向外建立的 HID 关联（Association）。

<a id="r_gae2000b4d39ed956cb37298bfcab351ed"></a>

```c
int bt_hid_device_disconnect (struct bt_hid_device *hid)
```

相关声明：[bt_hid_device_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gae2000b4d39ed956cb37298bfcab351ed)。

断开此前已连接的 HID 关联（Association）。

<a id="r_gad6bc5203aa9a2c8e4e217005f8f58b2e"></a>

```c
struct net_buf * bt_hid_device_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_hid_device_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gad6bc5203aa9a2c8e4e217005f8f58b2e)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

分配／创建适用于通过 L2CAP 传输 HID 的协议数据单元（PDU）缓冲区。

<a id="r_ga1034935eec4ff6a466990ee5f0c1ba2c"></a>

```c
int bt_hid_device_input_report (struct bt_hid_device *hid, struct net_buf *buf)
```

相关声明：[bt_hid_device_input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga1034935eec4ff6a466990ee5f0c1ba2c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 HID 主机发送 HID 中断输入报告（Interrupt Input Report）。

<a id="r_gab5b6b5f1047961ed5164f4e1059201ad"></a>

```c
int bt_hid_device_virtual_cable_unplug (struct bt_hid_device *hid)
```

相关声明：[bt_hid_device_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gab5b6b5f1047961ed5164f4e1059201ad)。

为指定 HID 关联触发虚拟电缆拔除（Virtual Cable Unplug）过程。

<a id="r_ga63608252095d8c0638c6c43809e42553"></a>

```c
struct bt_conn * bt_hid_device_get_conn (struct bt_hid_device *hid)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hid_device_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga63608252095d8c0638c6c43809e42553)。

获取与 HID 设备关联的异步无连接链路（ACL）连接。


## 25.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/classic/hid.h](../api_source_reference/P070_hid.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P318_hid_device.h_源码浏览.md)
- [bt_hid_device_cb](../bluetooth_service_model_reference/P091_bt_hid_device_cb_结构体.md)
- [bt_hid_device_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga296d1b9695091507438261035d067c02)
- [bt_hid_device_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga35b0ec48658daa94010bef0c91503491)
- [bt_hid_device_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gaf30d808e9903988d72d831c3c4aab617)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hid_device_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gae2000b4d39ed956cb37298bfcab351ed)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hid_device_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gad6bc5203aa9a2c8e4e217005f8f58b2e)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_hid_device_input_report](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga1034935eec4ff6a466990ee5f0c1ba2c)
- [bt_hid_device_virtual_cable_unplug](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#gab5b6b5f1047961ed5164f4e1059201ad)
- [bt_hid_device_get_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html#ga63608252095d8c0638c6c43809e42553)

<a id="header-details"></a>

---

[上一章](P024_zephyr__mgmt__hawkbit__hawkbit.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__dt-bindings__sensor__iis2iclx.h_文件参考.md)
