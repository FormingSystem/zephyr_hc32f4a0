---
id: learning.zephyr-docs.api-file-clock-network-reference.page-16
title: zephyr__bluetooth__l2cap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_bluetooth\_\_l2cap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙逻辑链路控制与适配协议（L2CAP）的处理。

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

蓝牙逻辑链路控制与适配协议（L2CAP）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_bt_5Fl2cap_5Fchan"></a>

```c
struct bt_l2cap_chan
```

相关声明：[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)。

逻辑链路控制与适配协议（L2CAP）的信道结构。

<a id="r_bt_5Fl2cap_5Fle_5Fendpoint"></a>

```c
struct bt_l2cap_le_endpoint
```

相关声明：[bt_l2cap_le_endpoint](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md)。

低功耗（LE）L2CAP端点结构。

<a id="r_bt_5Fl2cap_5Fle_5Fchan"></a>

```c
struct bt_l2cap_le_chan
```

相关声明：[bt_l2cap_le_chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md)。

低功耗（LE）L2CAP信道结构。

<a id="r_bt_5Fl2cap_5Ffixed_5Fchan"></a>

```c
struct bt_l2cap_fixed_chan
```

相关声明：[bt_l2cap_fixed_chan](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md)。

固定L2CAP信道（Fixed L2CAP Channel）结构。

<a id="r_bt_5Fl2cap_5Fbr_5Fendpoint"></a>

```c
struct bt_l2cap_br_endpoint
```

相关声明：[bt_l2cap_br_endpoint](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md)。

基本速率/增强数据速率（BR/EDR）的L2CAP端点结构。

<a id="r_bt_5Fl2cap_5Fbr_5Fwindow"></a>

```c
struct bt_l2cap_br_window
```

相关声明：[bt_l2cap_br_window](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md)。

非基本模式（non-BASIC mode）L2CAP已连接信道的信息帧（I-Frame）发送窗口。

<a id="r_bt_5Fl2cap_5Fbr_5Fchan"></a>

```c
struct bt_l2cap_br_chan
```

相关声明：[bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)。

基本速率/增强数据速率（BR/EDR）的L2CAP信道结构。

<a id="r_bt_5Fl2cap_5Fchan_5Fops"></a>

```c
struct bt_l2cap_chan_ops
```

相关声明：[bt_l2cap_chan_ops](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md)。

逻辑链路控制与适配协议（L2CAP）的信道操作结构。

<a id="r_bt_5Fl2cap_5Fserver"></a>

```c
struct bt_l2cap_server
```

相关声明：[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

L2CAP服务器（Server）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.2\_宏定义（Macros）

<a id="r_gab33b91052026973180356640b7310659"></a>

```c
#define BT_L2CAP_HDR_SIZE 4
```

相关声明：[BT_L2CAP_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab33b91052026973180356640b7310659)。

L2CAP 协议数据单元头部大小（PDU Header Size），用于计算缓冲区大小。

<a id="r_ga45ef5aee4ed4dd705cad6d234562c660"></a>

```c
#define BT_L2CAP_TX_MTU (CONFIG_BT_L2CAP_TX_MTU)
```

相关声明：[BT_L2CAP_TX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga45ef5aee4ed4dd705cad6d234562c660)。

出站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="r_ga6e458a1758e5012755f3b97f8348c966"></a>

```c
#define BT_L2CAP_RX_MTU (CONFIG_BT_BUF_ACL_RX_SIZE - BT_L2CAP_HDR_SIZE)
```

相关声明：[BT_L2CAP_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e458a1758e5012755f3b97f8348c966)、[BT_L2CAP_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab33b91052026973180356640b7310659)。

入站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="r_gab95b119de4757588074e367a90a7136a"></a>

```c
#define BT_L2CAP_BUF_SIZE(mtu)
```

相关声明：[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

计算 L2CAP 协议数据单元（PDUs）所需缓冲区大小的辅助接口。

<a id="r_ga967c4c3f9b9beba1d0ce8516c5d1c659"></a>

```c
#define BT_L2CAP_SDU_HDR_SIZE 2
```

相关声明：[BT_L2CAP_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

L2CAP 服务数据单元头部大小（SDU Header Size），用于计算缓冲区大小。

<a id="r_gaa6fcd053d918db7005bc058501c2a598"></a>

```c
#define BT_L2CAP_SDU_TX_MTU (BT_L2CAP_TX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_SDU_TX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaa6fcd053d918db7005bc058501c2a598)、[BT_L2CAP_TX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga45ef5aee4ed4dd705cad6d234562c660)、[BT_L2CAP_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

未分段出站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

<a id="r_ga13b93a8f09157fbcf739fa4949840efe"></a>

```c
#define BT_L2CAP_SDU_RX_MTU (BT_L2CAP_RX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_SDU_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga13b93a8f09157fbcf739fa4949840efe)、[BT_L2CAP_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e458a1758e5012755f3b97f8348c966)、[BT_L2CAP_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

未分段入站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

<a id="r_ga1c76618c32bbe86b18fd8663760fb220"></a>

```c
#define BT_L2CAP_SDU_BUF_SIZE(mtu)
```

相关声明：[BT_L2CAP_SDU_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1c76618c32bbe86b18fd8663760fb220)。

计算 L2CAP 服务数据单元（SDUs）所需缓冲区大小的辅助接口。

<a id="r_gac201afc0f1f55b89a023f03162ba57fe"></a>

```c
#define BT_L2CAP_ECRED_MIN_MTU 64
```

相关声明：[BT_L2CAP_ECRED_MIN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gac201afc0f1f55b89a023f03162ba57fe)。

L2CAP 增强型信用模式（ECRED）的最小 MTU。

<a id="r_ga11933f5a909578f0768f60ce0c8e4c86"></a>

```c
#define BT_L2CAP_ECRED_MIN_MPS 64
```

相关声明：[BT_L2CAP_ECRED_MIN_MPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga11933f5a909578f0768f60ce0c8e4c86)。

L2CAP 增强型信用模式（ECRED）的最小 MPS。

<a id="r_gaff00540eea0d1b9bdbf634856be135e5"></a>

```c
#define BT_L2CAP_MAX_MTU UINT16_MAX
```

相关声明：[BT_L2CAP_MAX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaff00540eea0d1b9bdbf634856be135e5)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)。

L2CAP 最大传输单元（Maximum MTU）。

<a id="r_gaf2979b9cfa7658130b51a7a8da6dce7c"></a>

```c
#define BT_L2CAP_MAX_MPS 65533
```

相关声明：[BT_L2CAP_MAX_MPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaf2979b9cfa7658130b51a7a8da6dce7c)。

L2CAP 最大 MPS。

<a id="r_gaf4c98aa3e9f5293b2ff693fb69dc71c9"></a>

```c
#define BT_L2CAP_ECRED_CHAN_MAX_PER_REQ 5
```

相关声明：[BT_L2CAP_ECRED_CHAN_MAX_PER_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaf4c98aa3e9f5293b2ff693fb69dc71c9)。

增强型信用模式 L2CAP 信令 PDU（ECRED L2CAP Signaling PDUs）中的最大通道数量。

<a id="r_gacff77dc842b18b2d10c29183be72db77"></a>

```c
#define BT_L2CAP_CID_BR_SIG 0x0001
```

相关声明：[BT_L2CAP_CID_BR_SIG](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gacff77dc842b18b2d10c29183be72db77)。

蓝牙基本速率（BR）信令通道（signaling channel）。

<a id="r_gac463a009cf61bcb7cf23ba19885ea16d"></a>

```c
#define BT_L2CAP_CID_ATT 0x0004
```

相关声明：[BT_L2CAP_CID_ATT](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gac463a009cf61bcb7cf23ba19885ea16d)。

属性协议（Attribute Protocol，ATT）通道。

<a id="r_ga4d09da498948b233713f833900ee2d1f"></a>

```c
#define BT_L2CAP_CID_LE_SIG 0x0005
```

相关声明：[BT_L2CAP_CID_LE_SIG](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#ga4d09da498948b233713f833900ee2d1f)。

蓝牙低功耗（LE）信令通道。

<a id="r_gae72ebddd803464009967c1f4e6683f25"></a>

```c
#define BT_L2CAP_CID_SMP 0x0006
```

相关声明：[BT_L2CAP_CID_SMP](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gae72ebddd803464009967c1f4e6683f25)。

安全管理协议（Security Manager Protocol，SMP）通道。

<a id="r_ga225fc18663e6a0c0e1c8f420ef0688e3"></a>

```c
#define BT_L2CAP_CID_BR_SMP 0x0007
```

相关声明：[BT_L2CAP_CID_BR_SMP](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#ga225fc18663e6a0c0e1c8f420ef0688e3)。

BR 安全管理协议通道。

<a id="r_gac936761e661a5c65d65ee9b4c185679b"></a>

```c
#define BT_L2CAP_LE_CHAN(_ch)
```

相关声明：[BT_L2CAP_LE_CHAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gac936761e661a5c65d65ee9b4c185679b)。

辅助宏：根据给定对象的 chan 容器成员地址，获取具有相同 chan 成员地址的 bt_l2cap_le_chan 类型容器对象（Container Object）的地址。

<a id="r_ga334ced39f199394971d1600fac42abc8"></a>

```c
#define BT_L2CAP_FIXED_CHANNEL_DEFINE(_name)
```

相关声明：[BT_L2CAP_FIXED_CHANNEL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga334ced39f199394971d1600fac42abc8)。

注册固定 L2CAP 通道（Fixed Channel）。

<a id="r_gae8b0ef3d8fbadc2e50759f3409196478"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_BASIC 0x00
```

相关声明：[BT_L2CAP_BR_LINK_MODE_BASIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gae8b0ef3d8fbadc2e50759f3409196478)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga9e524a5a8037eb8d7b6fbdd841635baa"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_RET 0x01
```

相关声明：[BT_L2CAP_BR_LINK_MODE_RET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9e524a5a8037eb8d7b6fbdd841635baa)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga1c203f6b730bbb5f045d72a2875e9b75"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_FC 0x02
```

相关声明：[BT_L2CAP_BR_LINK_MODE_FC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1c203f6b730bbb5f045d72a2875e9b75)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_gacd3f015557ae273dba9255377350b55a"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_ERET 0x03
```

相关声明：[BT_L2CAP_BR_LINK_MODE_ERET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gacd3f015557ae273dba9255377350b55a)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_gaee76903b4b152d0c91fceee162abe8b4"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_STREAM 0x04
```

相关声明：[BT_L2CAP_BR_LINK_MODE_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaee76903b4b152d0c91fceee162abe8b4)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga180d1d5cc2cab3d04836fcb556c06463"></a>

```c
#define BT_L2CAP_BR_FCS_NO 0x00
```

相关声明：[BT_L2CAP_BR_FCS_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga180d1d5cc2cab3d04836fcb556c06463)。

帧校验序列类型（Frame Check Sequence Type）。

<a id="r_ga6e9cfa54d0a08ab33ba420e8ff099dba"></a>

```c
#define BT_L2CAP_BR_FCS_16BIT 0x01
```

相关声明：[BT_L2CAP_BR_FCS_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e9cfa54d0a08ab33ba420e8ff099dba)。

帧校验序列类型（Frame Check Sequence Type）。

<a id="r_ga281232ec622c626c0be2be23bae18d8d"></a>

```c
#define BT_L2CAP_CHAN_SEND_RESERVE (BT_L2CAP_BUF_SIZE(0))
```

相关声明：[BT_L2CAP_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga281232ec622c626c0be2be23bae18d8d)、[BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)。

出站 L2CAP 协议数据单元（PDUs）所需的头部空间（Headroom）。

<a id="r_gabdb3983d3862f6654a1653dd45c4157d"></a>

```c
#define BT_L2CAP_SDU_CHAN_SEND_RESERVE (BT_L2CAP_SDU_BUF_SIZE(0))
```

相关声明：[BT_L2CAP_SDU_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gabdb3983d3862f6654a1653dd45c4157d)、[BT_L2CAP_SDU_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1c76618c32bbe86b18fd8663760fb220)。

出站 L2CAP 服务数据单元（SDUs）所需的头部空间（Headroom）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.3\_类型定义（Typedefs）

<a id="r_ga88baae9c159f3de4ccb34fd0e3cc8c3b"></a>

```c
typedef void(* bt_l2cap_chan_destroy_t) (struct bt_l2cap_chan *chan)
```

相关声明：[bt_l2cap_chan_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga88baae9c159f3de4ccb34fd0e3cc8c3b)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)。

通道销毁回调（Channel Destroy Callback）。

<a id="r_ga5a80330e52ea0fa4ee3266094570bb16"></a>

```c
typedef enum bt_l2cap_chan_state bt_l2cap_chan_state_t
```

相关声明：[bt_l2cap_chan_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga642436bdf29f79495763b10231c6b25b)、[bt_l2cap_chan_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5a80330e52ea0fa4ee3266094570bb16)。

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

<a id="r_ga3a1a88a8e87aefe9bea1dd01aa193b42"></a>

```c
typedef enum bt_l2cap_chan_status bt_l2cap_chan_status_t
```

相关声明：[bt_l2cap_chan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga371a747c8939a1156111dc03c774015c)、[bt_l2cap_chan_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3a1a88a8e87aefe9bea1dd01aa193b42)。

L2CAP 通道状态（Channel Status）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.4\_枚举（Enumerations）

<a id="r_ga642436bdf29f79495763b10231c6b25b"></a>

```c
enum bt_l2cap_chan_state { BT_L2CAP_DISCONNECTED , BT_L2CAP_CONNECTING , BT_L2CAP_CONFIG , BT_L2CAP_CONNECTED , BT_L2CAP_DISCONNECTING }
```

相关声明：[bt_l2cap_chan_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga642436bdf29f79495763b10231c6b25b)、[BT_L2CAP_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)、[BT_L2CAP_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)、[BT_L2CAP_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)、[BT_L2CAP_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)、[BT_L2CAP_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)。

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

<a id="r_ga371a747c8939a1156111dc03c774015c"></a>

```c
enum bt_l2cap_chan_status { BT_L2CAP_STATUS_OUT , BT_L2CAP_STATUS_SHUTDOWN , BT_L2CAP_STATUS_ENCRYPT_PENDING , BT_L2CAP_NUM_STATUS }
```

相关声明：[bt_l2cap_chan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga371a747c8939a1156111dc03c774015c)、[BT_L2CAP_STATUS_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)、[BT_L2CAP_STATUS_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e)、[BT_L2CAP_STATUS_ENCRYPT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)、[BT_L2CAP_NUM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)。

L2CAP 通道状态（Channel Status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.5\_函数（Functions）

<a id="r_ga1a5e8c81c086872d7fb8da5329f982c6"></a>

```c
int bt_l2cap_server_register (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1a5e8c81c086872d7fb8da5329f982c6)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

注册 L2CAP 服务器（Server）。

<a id="r_ga5b0ae2abd714f46e6bb2394bce33e613"></a>

```c
int bt_l2cap_br_server_register (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_br_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5b0ae2abd714f46e6bb2394bce33e613)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

在面向 BR/EDR 的连接上注册 L2CAP 服务器（Server）。

<a id="r_ga723f47b211cd446d0980332f07211638"></a>

```c
int bt_l2cap_br_server_unregister (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_br_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga723f47b211cd446d0980332f07211638)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

在面向 BR/EDR 的连接上注销 L2CAP 服务器（Server）。

<a id="r_gaebc2d157fb5f013722e9c332b3d81804"></a>

```c
int bt_l2cap_ecred_chan_connect (struct bt_conn *conn, struct bt_l2cap_chan **chans, uint16_t psm)
```

相关声明：[bt_l2cap_ecred_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaebc2d157fb5f013722e9c332b3d81804)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

连接增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga05d28a51d9fba08d609287957ea4c7ec"></a>

```c
int bt_l2cap_ecred_chan_reconfigure (struct bt_l2cap_chan **chans, uint16_t mtu)
```

相关声明：[bt_l2cap_ecred_chan_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga05d28a51d9fba08d609287957ea4c7ec)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga67e13b0048eb68ef35c315a5276d832d"></a>

```c
int bt_l2cap_ecred_chan_reconfigure_explicit (struct bt_l2cap_chan **chans, size_t chan_count, uint16_t mtu, uint16_t mps)
```

相关声明：[bt_l2cap_ecred_chan_reconfigure_explicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga67e13b0048eb68ef35c315a5276d832d)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga3c3cfb4b151c808c0a3d2562a5c26a20"></a>

```c
int bt_l2cap_chan_connect (struct bt_conn *conn, struct bt_l2cap_chan *chan, uint16_t psm)
```

相关声明：[bt_l2cap_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3c3cfb4b151c808c0a3d2562a5c26a20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

连接 L2CAP 通道（Channel）。

<a id="r_ga7165f82a05e3a19d6b2baf0ba292a3fe"></a>

```c
int bt_l2cap_chan_disconnect (struct bt_l2cap_chan *chan)
```

相关声明：[bt_l2cap_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga7165f82a05e3a19d6b2baf0ba292a3fe)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)。

断开 L2CAP 通道（Channel）。

<a id="r_ga97b7909749667f910f83e6fcb54495c3"></a>

```c
int bt_l2cap_chan_send (struct bt_l2cap_chan *chan, struct net_buf *buf)
```

相关声明：[bt_l2cap_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga97b7909749667f910f83e6fcb54495c3)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 L2CAP 通道发送数据。

<a id="r_ga9bc950a929fc2bdb1463c268cea478b6"></a>

```c
int bt_l2cap_chan_give_credits (struct bt_l2cap_chan *chan, uint16_t additional_credits)
```

相关声明：[bt_l2cap_chan_give_credits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9bc950a929fc2bdb1463c268cea478b6)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向远端提供信用额度（Credits）。

<a id="r_gad53f5fc31314121ff84e740879eae3cf"></a>

```c
int bt_l2cap_chan_recv_complete (struct bt_l2cap_chan *chan, struct net_buf *buf)
```

相关声明：[bt_l2cap_chan_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

完成 L2CAP 通道数据的接收。


## 16.6\_原页交叉引用（Cross References）

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
- [查看此文件的源码。](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)
- [bt_l2cap_le_endpoint](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md)
- [bt_l2cap_le_chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md)
- [bt_l2cap_fixed_chan](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md)
- [bt_l2cap_br_endpoint](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md)
- [bt_l2cap_br_window](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md)
- [bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)
- [bt_l2cap_chan_ops](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md)
- [bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)
- [BT_L2CAP_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab33b91052026973180356640b7310659)
- [BT_L2CAP_TX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga45ef5aee4ed4dd705cad6d234562c660)
- [BT_L2CAP_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e458a1758e5012755f3b97f8348c966)
- [BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)
- [BT_L2CAP_SDU_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga967c4c3f9b9beba1d0ce8516c5d1c659)
- [BT_L2CAP_SDU_TX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaa6fcd053d918db7005bc058501c2a598)
- [BT_L2CAP_SDU_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga13b93a8f09157fbcf739fa4949840efe)
- [BT_L2CAP_SDU_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1c76618c32bbe86b18fd8663760fb220)
- [BT_L2CAP_ECRED_MIN_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gac201afc0f1f55b89a023f03162ba57fe)
- [BT_L2CAP_ECRED_MIN_MPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga11933f5a909578f0768f60ce0c8e4c86)
- [BT_L2CAP_MAX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaff00540eea0d1b9bdbf634856be135e5)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [BT_L2CAP_MAX_MPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaf2979b9cfa7658130b51a7a8da6dce7c)
- [BT_L2CAP_ECRED_CHAN_MAX_PER_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaf4c98aa3e9f5293b2ff693fb69dc71c9)
- [BT_L2CAP_CID_BR_SIG](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gacff77dc842b18b2d10c29183be72db77)
- [BT_L2CAP_CID_ATT](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gac463a009cf61bcb7cf23ba19885ea16d)
- [BT_L2CAP_CID_LE_SIG](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#ga4d09da498948b233713f833900ee2d1f)
- [BT_L2CAP_CID_SMP](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#gae72ebddd803464009967c1f4e6683f25)
- [BT_L2CAP_CID_BR_SMP](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md#ga225fc18663e6a0c0e1c8f420ef0688e3)
- [BT_L2CAP_LE_CHAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gac936761e661a5c65d65ee9b4c185679b)
- [BT_L2CAP_FIXED_CHANNEL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga334ced39f199394971d1600fac42abc8)
- [BT_L2CAP_BR_LINK_MODE_BASIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gae8b0ef3d8fbadc2e50759f3409196478)
- [BT_L2CAP_BR_LINK_MODE_RET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9e524a5a8037eb8d7b6fbdd841635baa)
- [BT_L2CAP_BR_LINK_MODE_FC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1c203f6b730bbb5f045d72a2875e9b75)
- [BT_L2CAP_BR_LINK_MODE_ERET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gacd3f015557ae273dba9255377350b55a)
- [BT_L2CAP_BR_LINK_MODE_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaee76903b4b152d0c91fceee162abe8b4)
- [BT_L2CAP_BR_FCS_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga180d1d5cc2cab3d04836fcb556c06463)
- [BT_L2CAP_BR_FCS_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga6e9cfa54d0a08ab33ba420e8ff099dba)
- [BT_L2CAP_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga281232ec622c626c0be2be23bae18d8d)
- [BT_L2CAP_SDU_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gabdb3983d3862f6654a1653dd45c4157d)
- [bt_l2cap_chan_destroy_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga88baae9c159f3de4ccb34fd0e3cc8c3b)
- [bt_l2cap_chan_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga642436bdf29f79495763b10231c6b25b)
- [bt_l2cap_chan_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5a80330e52ea0fa4ee3266094570bb16)
- [bt_l2cap_chan_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga371a747c8939a1156111dc03c774015c)
- [bt_l2cap_chan_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3a1a88a8e87aefe9bea1dd01aa193b42)
- [BT_L2CAP_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)
- [BT_L2CAP_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)
- [BT_L2CAP_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)
- [BT_L2CAP_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)
- [BT_L2CAP_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)
- [BT_L2CAP_STATUS_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)
- [BT_L2CAP_STATUS_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e)
- [BT_L2CAP_STATUS_ENCRYPT_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)
- [BT_L2CAP_NUM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)
- [bt_l2cap_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga1a5e8c81c086872d7fb8da5329f982c6)
- [bt_l2cap_br_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5b0ae2abd714f46e6bb2394bce33e613)
- [bt_l2cap_br_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga723f47b211cd446d0980332f07211638)
- [bt_l2cap_ecred_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gaebc2d157fb5f013722e9c332b3d81804)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_l2cap_ecred_chan_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga05d28a51d9fba08d609287957ea4c7ec)
- [bt_l2cap_ecred_chan_reconfigure_explicit](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga67e13b0048eb68ef35c315a5276d832d)
- [bt_l2cap_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga3c3cfb4b151c808c0a3d2562a5c26a20)
- [bt_l2cap_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga7165f82a05e3a19d6b2baf0ba292a3fe)
- [bt_l2cap_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga97b7909749667f910f83e6fcb54495c3)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_l2cap_chan_give_credits](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga9bc950a929fc2bdb1463c268cea478b6)
- [bt_l2cap_chan_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gad53f5fc31314121ff84e740879eae3cf)

<a id="header-details"></a>

---

[上一章](P015_zephyr__drivers__interrupt_controller__intc_mchp_xec_ecia.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__lora.h_文件参考.md)
