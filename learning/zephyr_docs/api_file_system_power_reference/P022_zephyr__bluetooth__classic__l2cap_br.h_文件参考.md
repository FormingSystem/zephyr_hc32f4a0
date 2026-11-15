---
id: learning.zephyr-docs.api-file-system-power-reference.page-22
title: zephyr__bluetooth__classic__l2cap_br.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_bluetooth\_\_classic\_\_l2cap\_br.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/l2cap__br_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙L2CAP基本速率/增强数据速率（BR/EDR）的处理。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <sys/types.h>
```

查看此文件的源码。

蓝牙L2CAP基本速率/增强数据速率（BR/EDR）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 22.1\_数据结构（Data Structures）

<a id="r_bt_5Fl2cap_5Fbr_5Fecho_5Fcb"></a>

```c
struct bt_l2cap_br_echo_cb
```

相关声明：[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

回显（ECHO）请求/响应的回调结构。

<a id="r_bt_5Fl2cap_5Fbr_5Fconnless_5Fcb"></a>

```c
struct bt_l2cap_br_connless_cb
```

相关声明：[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

无连接数据信道（Connectionless Data Channel）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.2\_宏定义（Macros）

<a id="r_ga12c146741591a55dc50d7d07f0755daa"></a>

```c
#define BT_L2CAP_BR_ECHO_REQ_RESERVE BT_L2CAP_BUF_SIZE(4)
```

相关声明：[BT_L2CAP_BR_ECHO_REQ_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga12c146741591a55dc50d7d07f0755daa)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

传出的 L2CAP ECHO 请求协议数据单元（ECHO REQ PDU）所需的头部预留空间（Headroom）。

<a id="r_ga2961971c1f80aa6168f6cd47b991bf4d"></a>

```c
#define BT_L2CAP_BR_ECHO_RSP_RESERVE BT_L2CAP_BUF_SIZE(4)
```

相关声明：[BT_L2CAP_BR_ECHO_RSP_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga2961971c1f80aa6168f6cd47b991bf4d)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

传出的 L2CAP ECHO 响应协议数据单元（ECHO RSP PDU）所需的头部预留空间（Headroom）。

<a id="r_gaf90200c4933ca513eaa8a324f3f09614"></a>

```c
#define BT_L2CAP_CONNLESS_SDU_HDR_SIZE 2
```

相关声明：[BT_L2CAP_CONNLESS_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaf90200c4933ca513eaa8a324f3f09614)。

L2CAP 无连接服务数据单元（Connectionless SDU）的头部大小。

<a id="r_gac0c4332fa7020bdc52a4431c6a506524"></a>

```c
#define BT_L2CAP_CONNLESS_RESERVE BT_L2CAP_BUF_SIZE(BT_L2CAP_CONNLESS_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_CONNLESS_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gac0c4332fa7020bdc52a4431c6a506524)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)、[BT_L2CAP_CONNLESS_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaf90200c4933ca513eaa8a324f3f09614)。

无连接数据通道（Connectionless Data Channel）内传出的 L2CAP PDU 格式所需的头部预留空间（Headroom）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.3\_函数（Functions）

<a id="r_ga62c0115185f5026c1a842848dc5336ce"></a>

```c
int bt_l2cap_br_echo_cb_register (struct bt_l2cap_br_echo_cb *cb)
```

相关声明：[bt_l2cap_br_echo_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga62c0115185f5026c1a842848dc5336ce)、[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

注册回显（ECHO）回调。

<a id="r_ga00ef7d0a42d8e544b195172af44b88b2"></a>

```c
int bt_l2cap_br_echo_cb_unregister (struct bt_l2cap_br_echo_cb *cb)
```

相关声明：[bt_l2cap_br_echo_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga00ef7d0a42d8e544b195172af44b88b2)、[bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)。

注销回显（ECHO）回调。

<a id="r_ga3c6ad17ba18f5c00e39a379ed735de21"></a>

```c
int bt_l2cap_br_echo_req (struct bt_conn *conn, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_echo_req](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3c6ad17ba18f5c00e39a379ed735de21)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过回显请求（ECHO Request）发送回显数据。

<a id="r_ga8ebf537cc7e4c0a68a320f9c65c94b05"></a>

```c
int bt_l2cap_br_echo_rsp (struct bt_conn *conn, uint8_t identifier, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_echo_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga8ebf537cc7e4c0a68a320f9c65c94b05)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过回显响应（ECHO Response）发送回显数据。

<a id="r_gad1b4d59a8849124518bb973233b3f362"></a>

```c
int bt_l2cap_br_connless_register (struct bt_l2cap_br_connless_cb *cb)
```

相关声明：[bt_l2cap_br_connless_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gad1b4d59a8849124518bb973233b3f362)、[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

注册无连接数据通道（Connectionless Data Channel）回调。

<a id="r_gaa83e03f5ea5d62de096e1ebabb530697"></a>

```c
int bt_l2cap_br_connless_unregister (struct bt_l2cap_br_connless_cb *cb)
```

相关声明：[bt_l2cap_br_connless_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaa83e03f5ea5d62de096e1ebabb530697)、[bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)。

注销无连接数据通道（Connectionless Data Channel）回调。

<a id="r_ga3478f19778e657a2d047f68f26b89966"></a>

```c
int bt_l2cap_br_connless_send (struct bt_conn *conn, uint16_t psm, struct net_buf *buf)
```

相关声明：[bt_l2cap_br_connless_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3478f19778e657a2d047f68f26b89966)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

通过无连接数据通道（Connectionless Data Channel）发送数据。


## 22.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/buf.h](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/hci.h](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P433_l2cap_br.h_源码浏览.md)
- [bt_l2cap_br_echo_cb](../bluetooth_service_model_reference/P098_bt_l2cap_br_echo_cb_结构体.md)
- [bt_l2cap_br_connless_cb](../bluetooth_service_model_reference/P097_bt_l2cap_br_connless_cb_结构体.md)
- [BT_L2CAP_BR_ECHO_REQ_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga12c146741591a55dc50d7d07f0755daa)
- [BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)
- [BT_L2CAP_BR_ECHO_RSP_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga2961971c1f80aa6168f6cd47b991bf4d)
- [BT_L2CAP_CONNLESS_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaf90200c4933ca513eaa8a324f3f09614)
- [BT_L2CAP_CONNLESS_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gac0c4332fa7020bdc52a4431c6a506524)
- [bt_l2cap_br_echo_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga62c0115185f5026c1a842848dc5336ce)
- [bt_l2cap_br_echo_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga00ef7d0a42d8e544b195172af44b88b2)
- [bt_l2cap_br_echo_req](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3c6ad17ba18f5c00e39a379ed735de21)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_l2cap_br_echo_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga8ebf537cc7e4c0a68a320f9c65c94b05)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_l2cap_br_connless_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gad1b4d59a8849124518bb973233b3f362)
- [bt_l2cap_br_connless_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#gaa83e03f5ea5d62de096e1ebabb530697)
- [bt_l2cap_br_connless_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html#ga3478f19778e657a2d047f68f26b89966)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P021_zephyr__kernel__smp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__dt-bindings__sensor__lis2ds12.h_文件参考.md)
