---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-4
title: 逻辑链路控制与适配协议（L2CAP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_逻辑链路控制与适配协议（L2CAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

逻辑链路控制与适配协议（L2CAP）

<a id="details"></a>

逻辑链路控制与适配协议（L2CAP）。自 1.0 引入，版本 1.0.1。

<a id="header-groups"></a>
<a id="groups"></a>

## 4.1\_主题（Topics）

<a id="r_l2cap_5Fcid"></a>

相关声明：[L2CAP 通道标识符（L2CAP channel identifiers）](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md)。

标准 L2CAP 通道标识符。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

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

## 4.3\_宏定义（Macros）

<a id="r_gab33b91052026973180356640b7310659"></a>

```c
#define BT_L2CAP_HDR_SIZE 4
```

相关声明：[BT_L2CAP_HDR_SIZE](#gab33b91052026973180356640b7310659)。

L2CAP 协议数据单元头部大小（PDU Header Size），用于计算缓冲区大小。

<a id="r_ga45ef5aee4ed4dd705cad6d234562c660"></a>

```c
#define BT_L2CAP_TX_MTU (CONFIG_BT_L2CAP_TX_MTU)
```

相关声明：[BT_L2CAP_TX_MTU](#ga45ef5aee4ed4dd705cad6d234562c660)。

出站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="r_ga6e458a1758e5012755f3b97f8348c966"></a>

```c
#define BT_L2CAP_RX_MTU (CONFIG_BT_BUF_ACL_RX_SIZE - BT_L2CAP_HDR_SIZE)
```

相关声明：[BT_L2CAP_RX_MTU](#ga6e458a1758e5012755f3b97f8348c966)、[BT_L2CAP_HDR_SIZE](#gab33b91052026973180356640b7310659)。

入站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="r_gab95b119de4757588074e367a90a7136a"></a>

```c
#define BT_L2CAP_BUF_SIZE(mtu)
```

相关声明：[BT_L2CAP_BUF_SIZE](#gab95b119de4757588074e367a90a7136a)。

计算 L2CAP 协议数据单元（PDUs）所需缓冲区大小的辅助接口。

<a id="r_ga967c4c3f9b9beba1d0ce8516c5d1c659"></a>

```c
#define BT_L2CAP_SDU_HDR_SIZE 2
```

相关声明：[BT_L2CAP_SDU_HDR_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

L2CAP 服务数据单元头部大小（SDU Header Size），用于计算缓冲区大小。

<a id="r_gaa6fcd053d918db7005bc058501c2a598"></a>

```c
#define BT_L2CAP_SDU_TX_MTU (BT_L2CAP_TX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_SDU_TX_MTU](#gaa6fcd053d918db7005bc058501c2a598)、[BT_L2CAP_TX_MTU](#ga45ef5aee4ed4dd705cad6d234562c660)、[BT_L2CAP_SDU_HDR_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

未分段出站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

<a id="r_ga13b93a8f09157fbcf739fa4949840efe"></a>

```c
#define BT_L2CAP_SDU_RX_MTU (BT_L2CAP_RX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

相关声明：[BT_L2CAP_SDU_RX_MTU](#ga13b93a8f09157fbcf739fa4949840efe)、[BT_L2CAP_RX_MTU](#ga6e458a1758e5012755f3b97f8348c966)、[BT_L2CAP_SDU_HDR_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)。

未分段入站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

<a id="r_ga1c76618c32bbe86b18fd8663760fb220"></a>

```c
#define BT_L2CAP_SDU_BUF_SIZE(mtu)
```

相关声明：[BT_L2CAP_SDU_BUF_SIZE](#ga1c76618c32bbe86b18fd8663760fb220)。

计算 L2CAP 服务数据单元（SDUs）所需缓冲区大小的辅助接口。

<a id="r_gac201afc0f1f55b89a023f03162ba57fe"></a>

```c
#define BT_L2CAP_ECRED_MIN_MTU 64
```

相关声明：[BT_L2CAP_ECRED_MIN_MTU](#gac201afc0f1f55b89a023f03162ba57fe)。

L2CAP 增强型信用模式（ECRED）的最小 MTU。

<a id="r_ga11933f5a909578f0768f60ce0c8e4c86"></a>

```c
#define BT_L2CAP_ECRED_MIN_MPS 64
```

相关声明：[BT_L2CAP_ECRED_MIN_MPS](#ga11933f5a909578f0768f60ce0c8e4c86)。

L2CAP 增强型信用模式（ECRED）的最小 MPS。

<a id="r_gaff00540eea0d1b9bdbf634856be135e5"></a>

```c
#define BT_L2CAP_MAX_MTU UINT16_MAX
```

相关声明：[BT_L2CAP_MAX_MTU](#gaff00540eea0d1b9bdbf634856be135e5)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)。

L2CAP 最大传输单元（Maximum MTU）。

<a id="r_gaf2979b9cfa7658130b51a7a8da6dce7c"></a>

```c
#define BT_L2CAP_MAX_MPS 65533
```

相关声明：[BT_L2CAP_MAX_MPS](#gaf2979b9cfa7658130b51a7a8da6dce7c)。

L2CAP 最大 MPS。

<a id="r_gaf4c98aa3e9f5293b2ff693fb69dc71c9"></a>

```c
#define BT_L2CAP_ECRED_CHAN_MAX_PER_REQ 5
```

相关声明：[BT_L2CAP_ECRED_CHAN_MAX_PER_REQ](#gaf4c98aa3e9f5293b2ff693fb69dc71c9)。

增强型信用模式 L2CAP 信令 PDU（ECRED L2CAP Signaling PDUs）中的最大通道数量。

<a id="r_gac936761e661a5c65d65ee9b4c185679b"></a>

```c
#define BT_L2CAP_LE_CHAN(_ch)
```

相关声明：[BT_L2CAP_LE_CHAN](#gac936761e661a5c65d65ee9b4c185679b)。

辅助宏：根据给定对象的 chan 容器成员地址，获取具有相同 chan 成员地址的 bt_l2cap_le_chan 类型容器对象（Container Object）的地址。

<a id="r_ga334ced39f199394971d1600fac42abc8"></a>

```c
#define BT_L2CAP_FIXED_CHANNEL_DEFINE(_name)
```

相关声明：[BT_L2CAP_FIXED_CHANNEL_DEFINE](#ga334ced39f199394971d1600fac42abc8)。

注册固定 L2CAP 通道（Fixed Channel）。

<a id="r_gae8b0ef3d8fbadc2e50759f3409196478"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_BASIC 0x00
```

相关声明：[BT_L2CAP_BR_LINK_MODE_BASIC](#gae8b0ef3d8fbadc2e50759f3409196478)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga9e524a5a8037eb8d7b6fbdd841635baa"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_RET 0x01
```

相关声明：[BT_L2CAP_BR_LINK_MODE_RET](#ga9e524a5a8037eb8d7b6fbdd841635baa)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga1c203f6b730bbb5f045d72a2875e9b75"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_FC 0x02
```

相关声明：[BT_L2CAP_BR_LINK_MODE_FC](#ga1c203f6b730bbb5f045d72a2875e9b75)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_gacd3f015557ae273dba9255377350b55a"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_ERET 0x03
```

相关声明：[BT_L2CAP_BR_LINK_MODE_ERET](#gacd3f015557ae273dba9255377350b55a)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_gaee76903b4b152d0c91fceee162abe8b4"></a>

```c
#define BT_L2CAP_BR_LINK_MODE_STREAM 0x04
```

相关声明：[BT_L2CAP_BR_LINK_MODE_STREAM](#gaee76903b4b152d0c91fceee162abe8b4)。

L2CAP 端点链路模式（Endpoint Link Mode）。

<a id="r_ga180d1d5cc2cab3d04836fcb556c06463"></a>

```c
#define BT_L2CAP_BR_FCS_NO 0x00
```

相关声明：[BT_L2CAP_BR_FCS_NO](#ga180d1d5cc2cab3d04836fcb556c06463)。

帧校验序列类型（Frame Check Sequence Type）。

<a id="r_ga6e9cfa54d0a08ab33ba420e8ff099dba"></a>

```c
#define BT_L2CAP_BR_FCS_16BIT 0x01
```

相关声明：[BT_L2CAP_BR_FCS_16BIT](#ga6e9cfa54d0a08ab33ba420e8ff099dba)。

帧校验序列类型（Frame Check Sequence Type）。

<a id="r_ga281232ec622c626c0be2be23bae18d8d"></a>

```c
#define BT_L2CAP_CHAN_SEND_RESERVE (BT_L2CAP_BUF_SIZE(0))
```

相关声明：[BT_L2CAP_CHAN_SEND_RESERVE](#ga281232ec622c626c0be2be23bae18d8d)、[BT_L2CAP_BUF_SIZE](#gab95b119de4757588074e367a90a7136a)。

出站 L2CAP 协议数据单元（PDUs）所需的头部空间（Headroom）。

<a id="r_gabdb3983d3862f6654a1653dd45c4157d"></a>

```c
#define BT_L2CAP_SDU_CHAN_SEND_RESERVE (BT_L2CAP_SDU_BUF_SIZE(0))
```

相关声明：[BT_L2CAP_SDU_CHAN_SEND_RESERVE](#gabdb3983d3862f6654a1653dd45c4157d)、[BT_L2CAP_SDU_BUF_SIZE](#ga1c76618c32bbe86b18fd8663760fb220)。

出站 L2CAP 服务数据单元（SDUs）所需的头部空间（Headroom）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.4\_类型定义（Typedefs）

<a id="r_ga88baae9c159f3de4ccb34fd0e3cc8c3b"></a>

```c
typedef void(* bt_l2cap_chan_destroy_t) (struct bt_l2cap_chan *chan)
```

相关声明：[bt_l2cap_chan_destroy_t](#ga88baae9c159f3de4ccb34fd0e3cc8c3b)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)。

通道销毁回调（Channel Destroy Callback）。

<a id="r_ga5a80330e52ea0fa4ee3266094570bb16"></a>

```c
typedef enum bt_l2cap_chan_state bt_l2cap_chan_state_t
```

相关声明：[bt_l2cap_chan_state](#ga642436bdf29f79495763b10231c6b25b)、[bt_l2cap_chan_state_t](#ga5a80330e52ea0fa4ee3266094570bb16)。

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

<a id="r_ga3a1a88a8e87aefe9bea1dd01aa193b42"></a>

```c
typedef enum bt_l2cap_chan_status bt_l2cap_chan_status_t
```

相关声明：[bt_l2cap_chan_status](#ga371a747c8939a1156111dc03c774015c)、[bt_l2cap_chan_status_t](#ga3a1a88a8e87aefe9bea1dd01aa193b42)。

L2CAP 通道状态（Channel Status）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.5\_枚举（Enumerations）

<a id="r_ga642436bdf29f79495763b10231c6b25b"></a>

```c
enum bt_l2cap_chan_state { BT_L2CAP_DISCONNECTED , BT_L2CAP_CONNECTING , BT_L2CAP_CONFIG , BT_L2CAP_CONNECTED , BT_L2CAP_DISCONNECTING }
```

相关声明：[bt_l2cap_chan_state](#ga642436bdf29f79495763b10231c6b25b)、[BT_L2CAP_DISCONNECTED](#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)、[BT_L2CAP_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)、[BT_L2CAP_CONFIG](#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)、[BT_L2CAP_CONNECTED](#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)、[BT_L2CAP_DISCONNECTING](#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)。

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

<a id="r_ga371a747c8939a1156111dc03c774015c"></a>

```c
enum bt_l2cap_chan_status { BT_L2CAP_STATUS_OUT , BT_L2CAP_STATUS_SHUTDOWN , BT_L2CAP_STATUS_ENCRYPT_PENDING , BT_L2CAP_NUM_STATUS }
```

相关声明：[bt_l2cap_chan_status](#ga371a747c8939a1156111dc03c774015c)、[BT_L2CAP_STATUS_OUT](#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)、[BT_L2CAP_STATUS_SHUTDOWN](#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e)、[BT_L2CAP_STATUS_ENCRYPT_PENDING](#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)、[BT_L2CAP_NUM_STATUS](#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)。

L2CAP 通道状态（Channel Status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.6\_函数（Functions）

<a id="r_ga1a5e8c81c086872d7fb8da5329f982c6"></a>

```c
int bt_l2cap_server_register (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_server_register](#ga1a5e8c81c086872d7fb8da5329f982c6)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

注册 L2CAP 服务器（Server）。

<a id="r_ga5b0ae2abd714f46e6bb2394bce33e613"></a>

```c
int bt_l2cap_br_server_register (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_br_server_register](#ga5b0ae2abd714f46e6bb2394bce33e613)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

在面向 BR/EDR 的连接上注册 L2CAP 服务器（Server）。

<a id="r_ga723f47b211cd446d0980332f07211638"></a>

```c
int bt_l2cap_br_server_unregister (struct bt_l2cap_server *server)
```

相关声明：[bt_l2cap_br_server_unregister](#ga723f47b211cd446d0980332f07211638)、[bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)。

在面向 BR/EDR 的连接上注销 L2CAP 服务器（Server）。

<a id="r_gaebc2d157fb5f013722e9c332b3d81804"></a>

```c
int bt_l2cap_ecred_chan_connect (struct bt_conn *conn, struct bt_l2cap_chan **chans, uint16_t psm)
```

相关声明：[bt_l2cap_ecred_chan_connect](#gaebc2d157fb5f013722e9c332b3d81804)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

连接增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga05d28a51d9fba08d609287957ea4c7ec"></a>

```c
int bt_l2cap_ecred_chan_reconfigure (struct bt_l2cap_chan **chans, uint16_t mtu)
```

相关声明：[bt_l2cap_ecred_chan_reconfigure](#ga05d28a51d9fba08d609287957ea4c7ec)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga67e13b0048eb68ef35c315a5276d832d"></a>

```c
int bt_l2cap_ecred_chan_reconfigure_explicit (struct bt_l2cap_chan **chans, size_t chan_count, uint16_t mtu, uint16_t mps)
```

相关声明：[bt_l2cap_ecred_chan_reconfigure_explicit](#ga67e13b0048eb68ef35c315a5276d832d)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

<a id="r_ga3c3cfb4b151c808c0a3d2562a5c26a20"></a>

```c
int bt_l2cap_chan_connect (struct bt_conn *conn, struct bt_l2cap_chan *chan, uint16_t psm)
```

相关声明：[bt_l2cap_chan_connect](#ga3c3cfb4b151c808c0a3d2562a5c26a20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

连接 L2CAP 通道（Channel）。

<a id="r_ga7165f82a05e3a19d6b2baf0ba292a3fe"></a>

```c
int bt_l2cap_chan_disconnect (struct bt_l2cap_chan *chan)
```

相关声明：[bt_l2cap_chan_disconnect](#ga7165f82a05e3a19d6b2baf0ba292a3fe)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)。

断开 L2CAP 通道（Channel）。

<a id="r_ga97b7909749667f910f83e6fcb54495c3"></a>

```c
int bt_l2cap_chan_send (struct bt_l2cap_chan *chan, struct net_buf *buf)
```

相关声明：[bt_l2cap_chan_send](#ga97b7909749667f910f83e6fcb54495c3)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 L2CAP 通道发送数据。

<a id="r_ga9bc950a929fc2bdb1463c268cea478b6"></a>

```c
int bt_l2cap_chan_give_credits (struct bt_l2cap_chan *chan, uint16_t additional_credits)
```

相关声明：[bt_l2cap_chan_give_credits](#ga9bc950a929fc2bdb1463c268cea478b6)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向远端提供信用额度（Credits）。

<a id="r_gad53f5fc31314121ff84e740879eae3cf"></a>

```c
int bt_l2cap_chan_recv_complete (struct bt_l2cap_chan *chan, struct net_buf *buf)
```

相关声明：[bt_l2cap_chan_recv_complete](#gad53f5fc31314121ff84e740879eae3cf)、[bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

完成 L2CAP 通道数据的接收。

## 4.7\_详细说明（Detailed Documentation）

<a id="ga6e9cfa54d0a08ab33ba420e8ff099dba"></a>

### `BT_L2CAP_BR_FCS_16BIT`

```c
#define BT_L2CAP_BR_FCS_16BIT 0x01
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

帧校验序列类型（Frame Check Sequence Type）。

16 位帧校验序列（FCS）。

<a id="ga180d1d5cc2cab3d04836fcb556c06463"></a>

### `BT_L2CAP_BR_FCS_NO`

```c
#define BT_L2CAP_BR_FCS_NO 0x00
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

帧校验序列类型（Frame Check Sequence Type）。

无帧校验序列（FCS）。

<a id="gae8b0ef3d8fbadc2e50759f3409196478"></a>

### `BT_L2CAP_BR_LINK_MODE_BASIC`

```c
#define BT_L2CAP_BR_LINK_MODE_BASIC 0x00
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 端点链路模式（Endpoint Link Mode）。

基本模式（Basic Mode）。

<a id="gacd3f015557ae273dba9255377350b55a"></a>

### `BT_L2CAP_BR_LINK_MODE_ERET`

```c
#define BT_L2CAP_BR_LINK_MODE_ERET 0x03
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 端点链路模式（Endpoint Link Mode）。

增强重传模式（Enhanced Retransmission Mode）。

<a id="ga1c203f6b730bbb5f045d72a2875e9b75"></a>

### `BT_L2CAP_BR_LINK_MODE_FC`

```c
#define BT_L2CAP_BR_LINK_MODE_FC 0x02
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 端点链路模式（Endpoint Link Mode）。

流量控制模式（Flow Control Mode）。

<a id="ga9e524a5a8037eb8d7b6fbdd841635baa"></a>

### `BT_L2CAP_BR_LINK_MODE_RET`

```c
#define BT_L2CAP_BR_LINK_MODE_RET 0x01
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 端点链路模式（Endpoint Link Mode）。

重传模式（Retransmission Mode）。

<a id="gaee76903b4b152d0c91fceee162abe8b4"></a>

### `BT_L2CAP_BR_LINK_MODE_STREAM`

```c
#define BT_L2CAP_BR_LINK_MODE_STREAM 0x04
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 端点链路模式（Endpoint Link Mode）。

流模式（Streaming Mode）。

<a id="gab95b119de4757588074e367a90a7136a"></a>

### `BT_L2CAP_BUF_SIZE`

```c
#define BT_L2CAP_BUF_SIZE ( mtu)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

展开值（Value）：

```c
BT_BUF_ACL_SIZE(BT_L2CAP_HDR_SIZE + (mtu))
```

计算 L2CAP 协议数据单元（PDUs）所需缓冲区大小的辅助接口。

可用于创建缓冲池（Buffer Pools）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mtu` | 所需的 L2CAP 协议数据单元最大传输单元（PDU MTU）。 |

**返回（Returns）**：返回：满足所请求 L2CAP PDU MTU 所需的缓冲区大小。

<a id="ga281232ec622c626c0be2be23bae18d8d"></a>

### `BT_L2CAP_CHAN_SEND_RESERVE`

```c
#define BT_L2CAP_CHAN_SEND_RESERVE (BT_L2CAP_BUF_SIZE(0))
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

出站 L2CAP 协议数据单元（PDUs）所需的头部空间（Headroom）。

<a id="gaf4c98aa3e9f5293b2ff693fb69dc71c9"></a>

### `BT_L2CAP_ECRED_CHAN_MAX_PER_REQ`

```c
#define BT_L2CAP_ECRED_CHAN_MAX_PER_REQ 5
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

增强型信用模式 L2CAP 信令 PDU（ECRED L2CAP Signaling PDUs）中的最大通道数量。

当前，这是下列协议数据单元（PDU）中引用的信道数上限：

- L2CAP 基于信用额度的连接请求（L2CAP_CREDIT_BASED_CONNECTION_REQ）。
- L2CAP 基于信用额度的重新配置请求（L2CAP_CREDIT_BASED_RECONFIGURE_REQ）。

**警告（Warning）**：警告：这些 PDU 之间的共同上限是根据现有规定推断的。蓝牙规范将其视为各自独立的数字，并不保证未来可能出现的 ECRED L2CAP 信令 PDU 仍具有相同上限。（原文 “does now guarantee” 与该段语义不符，此处按不保证理解并保留此说明。）

<a id="ga11933f5a909578f0768f60ce0c8e4c86"></a>

### `BT_L2CAP_ECRED_MIN_MPS`

```c
#define BT_L2CAP_ECRED_MIN_MPS 64
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 增强型信用模式（ECRED）的最小 MPS。

L2CAP 增强型基于信用额度的连接（Enhanced Credit Based Connection）的最小 MPS。

此要求根据《核心规范》（Core）v6.0 第 3 卷 A 部分 4.25 节的文本推断：

原始示例（Example）：

```c
L2CAP implementations shall support a minimum MPS of 64 and may
support an MPS up to 65533 octets for these channels.
```

<a id="gac201afc0f1f55b89a023f03162ba57fe"></a>

### `BT_L2CAP_ECRED_MIN_MTU`

```c
#define BT_L2CAP_ECRED_MIN_MTU 64
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 增强型信用模式（ECRED）的最小 MTU。

L2CAP 增强型基于信用额度的连接（Enhanced Credit Based Connection）的最小 MTU。

此要求根据《核心规范》（Core）v6.0 第 3 卷 A 部分 4.25 节的文本推断：

原始示例（Example）：

```c
L2CAP implementations shall support a minimum MTU size of 64
octets for these channels.
```

<a id="ga334ced39f199394971d1600fac42abc8"></a>

### `BT_L2CAP_FIXED_CHANNEL_DEFINE`

```c
#define BT_L2CAP_FIXED_CHANNEL_DEFINE ( _name)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(bt_l2cap_fixed_chan,                                  \
                                     _CONCAT(bt_l2cap_fixed_chan, _name))
```

注册固定 L2CAP 通道（Fixed Channel）。

定义并注册类型为 bt_l2cap_fixed_chan 的固定 L2CAP 信道（Fixed L2CAP Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 固定 L2CAP 信道的名称（Name）。信道按字典序排序，并按相同顺序初始化。 |

**说明（Note）**：注意：《核心规范》（Core Specification）v6.0 第 3 卷 A 部分 2.1 节规定固定 L2CAP 信道（Fixed L2CAP Channels）保留给协议栈，但此接口允许应用定义自己的固定信道，例如受内存限制而不适合使用动态信道时。应用必须确保该固定信道的 CID 尚未被占用。

<a id="gab33b91052026973180356640b7310659"></a>

### `BT_L2CAP_HDR_SIZE`

```c
#define BT_L2CAP_HDR_SIZE 4
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 协议数据单元头部大小（PDU Header Size），用于计算缓冲区大小。

<a id="gac936761e661a5c65d65ee9b4c185679b"></a>

### `BT_L2CAP_LE_CHAN`

```c
#define BT_L2CAP_LE_CHAN ( _ch)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

展开值（Value）：

```c
CONTAINER_OF(_ch, struct bt_l2cap_le_chan, chan)
```

辅助宏：根据给定对象的 chan 容器成员地址，获取具有相同 chan 成员地址的 bt_l2cap_le_chan 类型容器对象（Container Object）的地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_ch` | bt_l2cap_chan 类型对象的地址。 |

**返回（Returns）**：返回：内存中包含所指定对象的 bt_l2cap_le_chan 类型对象的地址。

<a id="gaf2979b9cfa7658130b51a7a8da6dce7c"></a>

### `BT_L2CAP_MAX_MPS`

```c
#define BT_L2CAP_MAX_MPS 65533
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 最大 MPS。

L2CAP 连接的最大 MPS。启用或不启用 ECRED 时相同。此要求来自《核心规范》（Core）v6.0 第 3 卷 A 部分 4.22 和 4.26 节。

<a id="gaff00540eea0d1b9bdbf634856be135e5"></a>

### `BT_L2CAP_MAX_MTU`

```c
#define BT_L2CAP_MAX_MTU UINT16_MAX
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 最大传输单元（Maximum MTU）。

L2CAP 连接的最大 MTU。启用或不启用 ECRED 时相同。此要求来自《核心规范》（Core）v6.0 第 3 卷 A 部分 4.22 和 4.26 节。

<a id="ga6e458a1758e5012755f3b97f8348c966"></a>

### `BT_L2CAP_RX_MTU`

```c
#define BT_L2CAP_RX_MTU (CONFIG_BT_BUF_ACL_RX_SIZE - BT_L2CAP_HDR_SIZE)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

入站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="ga1c76618c32bbe86b18fd8663760fb220"></a>

### `BT_L2CAP_SDU_BUF_SIZE`

```c
#define BT_L2CAP_SDU_BUF_SIZE ( mtu)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

展开值（Value）：

```c
BT_L2CAP_BUF_SIZE(BT_L2CAP_SDU_HDR_SIZE + (mtu))
```

计算 L2CAP 服务数据单元（SDUs）所需缓冲区大小的辅助接口。

可用于创建缓冲池（Buffer Pools）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mtu` | 所需的 BT_L2CAP_*_SDU。 |

**返回（Returns）**：返回：满足所请求 L2CAP SDU MTU 所需的缓冲区大小。

<a id="gabdb3983d3862f6654a1653dd45c4157d"></a>

### `BT_L2CAP_SDU_CHAN_SEND_RESERVE`

```c
#define BT_L2CAP_SDU_CHAN_SEND_RESERVE (BT_L2CAP_SDU_BUF_SIZE(0))
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

出站 L2CAP 服务数据单元（SDUs）所需的头部空间（Headroom）。

<a id="ga967c4c3f9b9beba1d0ce8516c5d1c659"></a>

### `BT_L2CAP_SDU_HDR_SIZE`

```c
#define BT_L2CAP_SDU_HDR_SIZE 2
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 服务数据单元头部大小（SDU Header Size），用于计算缓冲区大小。

<a id="ga13b93a8f09157fbcf739fa4949840efe"></a>

### `BT_L2CAP_SDU_RX_MTU`

```c
#define BT_L2CAP_SDU_RX_MTU (BT_L2CAP_RX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

未分段入站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

不分段（Segmentation）发送时，传入 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）；即一个 L2CAP SDU 可装入单个 L2CAP PDU。

分段传入的 L2CAP SDU 的 MTU 由应用缓冲池（Buffer Pool）大小决定。为支持接收分段 L2CAP SDU，应用须为信道定义 alloc_buf 回调。

<a id="gaa6fcd053d918db7005bc058501c2a598"></a>

### `BT_L2CAP_SDU_TX_MTU`

```c
#define BT_L2CAP_SDU_TX_MTU (BT_L2CAP_TX_MTU - BT_L2CAP_SDU_HDR_SIZE)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

未分段出站 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）。

不分段（Segmentation）发送时，传出 L2CAP 服务数据单元（SDU）的最大传输单元（MTU）；即一个 L2CAP SDU 可装入单个 L2CAP PDU。

分段传出的 L2CAP SDU 的 MTU 由应用缓冲池（Buffer Pool）大小决定。

<a id="ga45ef5aee4ed4dd705cad6d234562c660"></a>

### `BT_L2CAP_TX_MTU`

```c
#define BT_L2CAP_TX_MTU (CONFIG_BT_L2CAP_TX_MTU)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

出站 L2CAP 协议数据单元的最大传输单元（MTU）。

<a id="ga88baae9c159f3de4ccb34fd0e3cc8c3b"></a>

### `bt_l2cap_chan_destroy_t`

```c
typedef void(* bt_l2cap_chan_destroy_t) (struct bt_l2cap_chan *chan)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

通道销毁回调（Channel Destroy Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |

<a id="ga5a80330e52ea0fa4ee3266094570bb16"></a>

### `bt_l2cap_chan_state_t`

```c
typedef enum bt_l2cap_chan_state bt_l2cap_chan_state_t
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

仅供根据操作上下文（Operational Context）将信道设置为相应状态的内部 API 使用。

调用 bt_l2cap_chan_connect、bt_l2cap_ecred_chan_connect 或从 bt_l2cap_server::accept 返回时，信道进入 BT_L2CAP_CONNECTING 状态。

信道离开 BT_L2CAP_CONNECTING 状态时，调用 bt_l2cap_chan_ops::connected。

<a id="ga3a1a88a8e87aefe9bea1dd01aa193b42"></a>

### `bt_l2cap_chan_status_t`

```c
typedef enum bt_l2cap_chan_status bt_l2cap_chan_status_t
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 通道状态（Channel Status）。

<a id="ga642436bdf29f79495763b10231c6b25b"></a>

### `bt_l2cap_chan_state`

```c
enum bt_l2cap_chan_state
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 信用通道（CoC Channel）的生命周期状态（Life-span States）。

仅供根据操作上下文（Operational Context）将信道设置为相应状态的内部 API 使用。

调用 bt_l2cap_chan_connect、bt_l2cap_ecred_chan_connect 或从 bt_l2cap_server::accept 返回时，信道进入 BT_L2CAP_CONNECTING 状态。

信道离开 BT_L2CAP_CONNECTING 状态时，调用 bt_l2cap_chan_ops::connected。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_L2CAP_DISCONNECTED` | 信道已断开（Disconnected）。 |
| `BT_L2CAP_CONNECTING` | 信道处于正在连接状态（Connecting）。 |
| `BT_L2CAP_CONFIG` | 信道处于配置状态（Config State），为 BR／EDR 专有。 |
| `BT_L2CAP_CONNECTED` | 信道已就绪，可承载上层流量（Upper Layer Traffic）。 |
| `BT_L2CAP_DISCONNECTING` | 信道处于正在断开状态（Disconnecting）。 |

<a id="ga371a747c8939a1156111dc03c774015c"></a>

### `bt_l2cap_chan_status`

```c
enum bt_l2cap_chan_status
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

L2CAP 通道状态（Channel Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_L2CAP_STATUS_OUT` | 信道至少可发送一个协议数据单元（PDU）。 |
| `BT_L2CAP_STATUS_SHUTDOWN` | 信道关闭状态（Channel Shutdown Status）。一旦通知此状态，信道便不再能够发送或接收数据。 |
| `BT_L2CAP_STATUS_ENCRYPT_PENDING` | 信道加密待完成状态（Channel Encryption Pending Status）。 |
| `BT_L2CAP_NUM_STATUS` |  |

<a id="ga5b0ae2abd714f46e6bb2394bce33e613"></a>

### `bt_l2cap_br_server_register()`

```c
int bt_l2cap_br_server_register ( struct bt_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

在面向 BR/EDR 的连接上注册 L2CAP 服务器（Server）。

为协议／服务复用器（PSM）注册 L2CAP 服务器。每个新连接均通过 accept() 回调授权；授权成功时，该回调须分配供新连接使用的信道结构体。

对于 SIG 分配的固定 PSM（范围 0x0001–0x0eff），应在调用此 API 前将 PSM 赋给 server->psm。对于动态 PSM（范围 0x1000–0xffff），可将 server->psm 预设为给定值，但不推荐；也可保持为 0，此时函数返回前会给它分配一个新值。动态分配的值应通过服务发现协议（SDP）记录公开，L2CAP 客户端据此发现如何连接服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga723f47b211cd446d0980332f07211638"></a>

### `bt_l2cap_br_server_unregister()`

```c
int bt_l2cap_br_server_unregister ( struct bt_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

在面向 BR/EDR 的连接上注销 L2CAP 服务器（Server）。

注销某个协议／服务复用器（PSM）的 L2CAP 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3c3cfb4b151c808c0a3d2562a5c26a20"></a>

### `bt_l2cap_chan_connect()`

```c
int bt_l2cap_chan_connect ( struct bt_conn * conn, struct bt_l2cap_chan * chan, uint16_t psm )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

连接 L2CAP 通道（Channel）。

按 PSM 连接 L2CAP 信道（Channel）。连接完成后调用信道的 connected() 回调；连接被拒绝时改为调用 disconnected() 回调。作为第二个参数按地址传入的信道对象不应在应用中单独实例化。应用应创建传输类型专用的 L2CAP 对象：LE 使用 bt_l2cap_le_chan，BR／EDR 使用 bt_l2cap_br_chan。然后向此 API 传入这两种专用对象中 bt_l2cap_chan 类型成员的位置，即地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `chan` | 信道对象（Channel Object）。 |
| `psm` | 要连接的信道 PSM。 |

**警告（Warning）**：警告：调用者负责将包含 chan 对象的父对象清零（Zero Out）。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga7165f82a05e3a19d6b2baf0ba292a3fe"></a>

### `bt_l2cap_chan_disconnect()`

```c
int bt_l2cap_chan_disconnect ( struct bt_l2cap_chan * chan)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

断开 L2CAP 通道（Channel）。

断开 L2CAP 信道。若连接尚未完成，则取消该连接，并由此调用信道的 disconnected() 回调。有关输入参数的详细信息，参见上文 bt_l2cap_chan_connect() API 的参考说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga9bc950a929fc2bdb1463c268cea478b6"></a>

### `bt_l2cap_chan_give_credits()`

```c
int bt_l2cap_chan_give_credits ( struct bt_l2cap_chan * chan, uint16_t additional_credits )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

向远端提供信用额度（Credits）。

仅适用于使用 bt_l2cap_chan_ops::seg_recv 的信道。必须启用 CONFIG_BT_L2CAP_SEG_RECV 才能使用此函数。

授予的每一个信用额度（Credit）允许对端发送一个分段（Segment）。

此函数依赖有效的 chan 对象。分配对象或将其复用于新连接时，务必对 chan 执行默认初始化或 memset。

不允许添加 0 个信用额度（Credits）。

可在进入 BT_L2CAP_CONNECTING 状态之前授予信用额度（Credits）。这样会调整连接 PDU 中发送的初始信用额度（Initial Credits）。

信道处于 BT_L2CAP_CONNECTING 状态时不得调用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad53f5fc31314121ff84e740879eae3cf"></a>

### `bt_l2cap_chan_recv_complete()`

```c
int bt_l2cap_chan_recv_complete ( struct bt_l2cap_chan * chan, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

完成 L2CAP 通道数据的接收。

完成传入数据的接收。仅当信道的 recv 回调为处理某些传入数据而返回 -EINPROGRESS 时，才能调用此函数。缓冲区须保留原始 user_data，因为它用于保存该数据包所使用的信用额度／分段（Credits / Segments）信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |
| `buf` | 包含数据的缓冲区（Buffer）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga97b7909749667f910f83e6fcb54495c3"></a>

### `bt_l2cap_chan_send()`

```c
int bt_l2cap_chan_send ( struct bt_l2cap_chan * chan, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

向 L2CAP 通道发送数据。

将缓冲区中的数据发送到信道。对于动态信道（Dynamic Channels），若没有可用信用额度（Credits），则将 buf 排队，待收到对端提供的额度后发送。

不支持网络缓冲区分片（Network Buffer Fragments），即 buf->frags。

通过 BR／EDR 连接或固定 L2CAP 信道发送 L2CAP 数据时，应用发送的是 L2CAP PDU。应用必须在发送前在缓冲区预留 BT_L2CAP_CHAN_SEND_RESERVE 字节。应使用 BT_L2CAP_BUF_SIZE() 辅助宏，正确确定发送缓冲池中缓冲区的大小。

通过动态 L2CAP 信道发送 L2CAP 数据时，应用发送的是 L2CAP SDU。应用须在发送前在缓冲区预留 BT_L2CAP_SDU_CHAN_SEND_RESERVE 字节。可使用 BT_L2CAP_SDU_BUF_SIZE() 辅助宏，正确确定包含头部预留空间（Headroom）的缓冲区大小。

将 L2CAP SDU 分段为 L2CAP PDU 时，协议栈首先尝试通过信道的 alloc_seg 回调分配缓冲区，失败时回退到协议栈的全局缓冲池（Global Buffer Pool），其容量由 CONFIG_BT_L2CAP_TX_BUF_COUNT 配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要向其发送数据的信道（Channel）。更多信息参见 bt_l2cap_chan_connect。 |
| `buf` | 包含数据的缓冲区（Buffer）。 |

**警告（Warning）**：警告：此函数会覆盖缓冲区的 user_data，不要在其中存放任何内容。一旦调用此函数，就应视为 user_data 的所有权（Ownership）已转交协议栈。

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**警告（Warning）**：警告：如果缓冲池定义了 destroy 回调，当 HCI 驱动释放缓冲区时，可能从中断服务例程上下文（ISR Context）调用该回调。因此，destroy 回调不得调用在 ISR 上下文中不安全的同步原语（Synchronization Primitives），例如阻塞调用或锁定调度器。

**返回（Returns）**：返回：成功时为 0，发生错误时为负值。buf 或 chan 为 NULL、chan 既不基于 BR／EDR 也不基于 LE、缓冲区预留字节不足以容纳报头，或缓冲区引用计数不等于 1 时，返回 -EINVAL。buf 大于信道 MTU 时返回 -EMSGSIZE；底层 conn 已断开时返回 -ENOTCONN；L2CAP 信道已断开时返回 -ESHUTDOWN；chan 为 BR／EDR 时还可能返回底层的其他负错误码。

<a id="gaebc2d157fb5f013722e9c332b3d81804"></a>

### `bt_l2cap_ecred_chan_connect()`

```c
int bt_l2cap_ecred_chan_connect ( struct bt_conn * conn, struct bt_l2cap_chan ** chans, uint16_t psm )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

连接增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

按 PSM 连接最多 5 个 L2CAP 信道。连接完成后调用每个信道的 connected() 回调；连接被拒绝时改为调用 disconnected() 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `chans` | 信道对象数组（Channel Object Array）。 |
| `psm` | 要连接的信道 PSM。 |

**警告（Warning）**：警告：调用者负责将包含各 chan 对象的父对象清零（Zero Out）。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga05d28a51d9fba08d609287957ea4c7ec"></a>

### `bt_l2cap_ecred_chan_reconfigure()`

```c
int bt_l2cap_ecred_chan_reconfigure ( struct bt_l2cap_chan ** chans, uint16_t mtu )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

重新配置最多 5 个 L2CAP 信道。所有信道必须属于同一个 bt_conn。重新配置完成后调用每个信道的 reconfigured() 回调。不能减小任何所提供信道的 MTU。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chans` | 信道对象数组（Channel Object Array），以 NULL 结束。第 5 个之后的元素会被静默忽略。 |
| `mtu` | 重新配置所用的信道 MTU。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga67e13b0048eb68ef35c315a5276d832d"></a>

### `bt_l2cap_ecred_chan_reconfigure_explicit()`

```c
int bt_l2cap_ecred_chan_reconfigure_explicit ( struct bt_l2cap_chan ** chans, size_t chan_count, uint16_t mtu, uint16_t mps )
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

重新配置增强型基于信用的 L2CAP 通道（Enhanced Credit Based L2CAP Channels）。

使用显式 MPS 和 MTU 值重新配置 L2CAP ECRED 信道的实验性 API（Experimental API）。

为最多 5 个信道提交待处理的 L2CAP ECRED 重新配置（Reconfiguration）。所有提供的信道必须共享同一个连接管理对象（Connection Management）。

此 API 不能减小任何信道的 MTU；提供多个信道时，也不能减小任何信道的 MPS。

此操作没有专用回调，但对端每次响应重新配置请求时，都会调用每个受影响信道的 reconfigured() 回调。

此函数可能阻塞（Block）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chans` | 待重新配置的信道数组（Channel Array）。必须非空，最多包含 5 个元素，即 BT_L2CAP_ECRED_CHAN_MAX_PER_REQ。 |
| `chan_count` | 数组中的信道数量（Number of Channels）。 |
| `mtu` | 期望的 MTU，至少为 BT_L2CAP_ECRED_MIN_MTU。 |
| `mps` | 期望的 MPS，必须处于 BT_L2CAP_ECRED_MIN_MPS 到 BT_L2CAP_RX_MTU 范围内。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功提交待处理操作（Pended Operation）。 |
| `-EINVAL` | 参数错误（Bad Arguments），参见上文要求。 |
| `-ENOTCONN` | 连接对象未处于已连接状态（Connected State）。 |
| `-EBUSY` | 同一连接上还有另一个传出重新配置操作（Outgoing Reconfiguration）待完成。 |
| `-ENOMEM` | 主机（Host）没有可用缓冲区。 |

**警告（Warning）**：警告：已知问题：同一连接已有正在进行的重新配置操作时，实现返回 -EBUSY。调用者可稍后重试，但没有事件通知现有操作何时完成。另一个已知问题：无法分配缓冲区时，实现返回 -ENOMEM。调用者可稍后重试，但没有事件通知缓冲区何时可用。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT。

<a id="ga1a5e8c81c086872d7fb8da5329f982c6"></a>

### `bt_l2cap_server_register()`

```c
int bt_l2cap_server_register ( struct bt_l2cap_server * server)
```

```c
#include <zephyr/bluetooth/l2cap.h>
```

注册 L2CAP 服务器（Server）。

为协议／服务复用器（PSM）注册 L2CAP 服务器。每个新连接均通过 accept() 回调授权；授权成功时，该回调须分配供新连接使用的信道结构体。

对于 SIG 分配的固定 PSM（范围 0x0001–0x007f），应在调用此 API 前将 PSM 赋给 server->psm。对于动态 PSM（范围 0x0080–0x00ff），可将 server->psm 预设为给定值，但不推荐；也可保持为 0，此时函数返回前会给它分配一个新值。动态分配的值应通过 GATT 服务公开，L2CAP 客户端据此发现如何连接服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 4.8\_原页交叉引用（Cross References）

- [L2CAP 通道标识符（L2CAP channel identifiers）](../api_protocol_topic_reference/P022_L2CAP 通道标识符（L2CAP channel identifiers）.md)
- [bt_l2cap_chan](../bluetooth_service_model_reference/P101_bt_l2cap_chan_结构体.md)
- [bt_l2cap_le_endpoint](../bluetooth_service_model_reference/P105_bt_l2cap_le_endpoint_结构体.md)
- [bt_l2cap_le_chan](../bluetooth_service_model_reference/P104_bt_l2cap_le_chan_结构体.md)
- [bt_l2cap_fixed_chan](../bluetooth_service_model_reference/P103_bt_l2cap_fixed_chan_结构体.md)
- [bt_l2cap_br_endpoint](../bluetooth_service_model_reference/P099_bt_l2cap_br_endpoint_结构体.md)
- [bt_l2cap_br_window](../bluetooth_service_model_reference/P100_bt_l2cap_br_window_结构体.md)
- [bt_l2cap_br_chan](../bluetooth_service_model_reference/P096_bt_l2cap_br_chan_结构体.md)
- [bt_l2cap_chan_ops](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md)
- [bt_l2cap_server](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [zephyr/bluetooth/l2cap.h](../api_file_clock_network_reference/P016_zephyr__bluetooth__l2cap.h_文件参考.md)
- [BT_BUF_ACL_SIZE](../api_buffer_paging_topic_reference/P002_数据缓冲区（Data buffers）.md#ga8f570211d5e391be63bd46c189eac637)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [bt_l2cap_server::accept](../bluetooth_service_model_reference/P106_bt_l2cap_server_结构体.md#ad31a1908f7dc733f9497164ccabba2af)
- [bt_l2cap_chan_ops::connected](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a3a4dd75a11c9867adcade6d288dec2de)
- [accept()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)
- [bt_l2cap_chan_ops::seg_recv](../bluetooth_service_model_reference/P102_bt_l2cap_chan_ops_结构体.md#a7759a713038d74748952d5f2eb712429)
- [CONFIG_BT_L2CAP_SEG_RECV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_SEG_RECV)
- [CONFIG_BT_L2CAP_TX_BUF_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_TX_BUF_COUNT)
- [连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)
- [CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__buf_html_ga8f570211d5e391be63bd46c189eac637"></a>
<a id="agroup__bt__l2cap_html_gab33b91052026973180356640b7310659"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__l2cap__fixed__chan_html"></a>
<a id="agroup__sys-util_html_gac5bc561d1bfd1bf68877fe577779bd2f"></a>
<a id="astructbt__l2cap__le__chan_html"></a>
<a id="agroup__bt__l2cap_html_ga967c4c3f9b9beba1d0ce8516c5d1c659"></a>
<a id="agroup__bt__l2cap_html_gab95b119de4757588074e367a90a7136a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c"></a>
<a id="gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd"></a>
<a id="gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064"></a>
<a id="gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68"></a>
<a id="gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8"></a>
<a id="gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5"></a>
<a id="gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e"></a>
<a id="gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af"></a>
<a id="gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_等时通道（Isochronous channels，ISO）.md) · [返回大纲](大纲.md) · [下一章](P005_对象传输服务（Object Transfer Service，OTS）.md)
