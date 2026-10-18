---
id: learning.zephyr-docs.api-iso-dns-lin-topic-reference.page-3
title: 等时通道（Isochronous channels，ISO）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_等时通道（Isochronous channels，ISO）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时通道（Isochronous channels，ISO）

<a id="details"></a>

等时信道（Isochronous Channels，ISO）。自 2.3 引入，版本 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fiso_5Fchan"></a>

```c
struct bt_iso_chan
```

相关声明：[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)。

等时信道（ISO Channel）结构。

<a id="r_bt_5Fiso_5Fchan_5Fio_5Fqos"></a>

```c
struct bt_iso_chan_io_qos
```

相关声明：[bt_iso_chan_io_qos](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md)。

等时信道（ISO Channel）的输入输出服务质量（IO QoS）结构。

<a id="r_bt_5Fiso_5Fchan_5Fqos"></a>

```c
struct bt_iso_chan_qos
```

相关声明：[bt_iso_chan_qos](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md)。

等时信道（ISO Channel）的服务质量（QoS）结构。

<a id="r_bt_5Fiso_5Fchan_5Fpath"></a>

```c
struct bt_iso_chan_path
```

相关声明：[bt_iso_chan_path](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md)。

等时信道（ISO Channel）的数据路径（Data Path）结构。

<a id="r_bt_5Fiso_5Frecv_5Finfo"></a>

```c
struct bt_iso_recv_info
```

相关声明：[bt_iso_recv_info](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md)。

接收等时数据包（ISO Packet）的元数据结构。

<a id="r_bt_5Fiso_5Ftx_5Finfo"></a>

```c
struct bt_iso_tx_info
```

相关声明：[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

发送等时数据包（ISO Packet）的元数据结构。

<a id="r_bt_5Fiso_5Fcig_5Fparam"></a>

```c
struct bt_iso_cig_param
```

相关声明：[bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)。

连接等时组（Connected Isochronous Group，CIG）参数。

<a id="r_bt_5Fiso_5Fconnect_5Fparam"></a>

```c
struct bt_iso_connect_param
```

相关声明：[bt_iso_connect_param](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md)。

等时连接（ISO Connection）的参数结构。

<a id="r_bt_5Fiso_5Fbig_5Fcreate_5Fparam"></a>

```c
struct bt_iso_big_create_param
```

相关声明：[bt_iso_big_create_param](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md)。

广播等时组（Broadcast Isochronous Group，BIG）的创建参数。

<a id="r_bt_5Fiso_5Fbig_5Fsync_5Fparam"></a>

```c
struct bt_iso_big_sync_param
```

相关声明：[bt_iso_big_sync_param](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md)。

广播等时组（Broadcast Isochronous Group，BIG）的同步参数。

<a id="r_bt_5Fiso_5Fbiginfo"></a>

```c
struct bt_iso_biginfo
```

相关声明：[bt_iso_biginfo](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md)。

广播等时组（Broadcast Isochronous Group，BIG）的信息。

<a id="r_bt_5Fiso_5Fchan_5Fops"></a>

```c
struct bt_iso_chan_ops
```

相关声明：[bt_iso_chan_ops](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md)。

等时信道（ISO Channel）的操作结构。

<a id="r_bt_5Fiso_5Faccept_5Finfo"></a>

```c
struct bt_iso_accept_info
```

相关声明：[bt_iso_accept_info](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md)。

等时通信（ISO）接入信息结构。

<a id="r_bt_5Fiso_5Fserver"></a>

```c
struct bt_iso_server
```

相关声明：[bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)。

等时通信服务器（ISO Server）结构。

<a id="r_bt_5Fiso_5Funicast_5Ftx_5Finfo"></a>

```c
struct bt_iso_unicast_tx_info
```

相关声明：[bt_iso_unicast_tx_info](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md)。

等时单播发送（ISO Unicast TX）的信息结构。

<a id="r_bt_5Fiso_5Funicast_5Finfo"></a>

```c
struct bt_iso_unicast_info
```

相关声明：[bt_iso_unicast_info](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md)。

等时单播（ISO Unicast）的信息结构。

<a id="r_bt_5Fiso_5Fbroadcaster_5Finfo"></a>

```c
struct bt_iso_broadcaster_info
```

相关声明：[bt_iso_broadcaster_info](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md)。

等时通信广播端（ISO Broadcaster）的信息结构。

<a id="r_bt_5Fiso_5Fsync_5Freceiver_5Finfo"></a>

```c
struct bt_iso_sync_receiver_info
```

相关声明：[bt_iso_sync_receiver_info](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md)。

等时通信同步接收端（ISO Synchronized Receiver）的信息结构。

<a id="r_bt_5Fiso_5Finfo"></a>

```c
struct bt_iso_info
```

相关声明：[bt_iso_info](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md)。

等时信道（ISO Channel）的信息结构。

<a id="r_bt_5Fiso_5Fbig_5Fcb"></a>

```c
struct bt_iso_big_cb
```

相关声明：[bt_iso_big_cb](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md)。

保存广播等时组（Broadcast Isochronous Group）回调的结构。

<a id="r_bt_5Fiso_5Fcig"></a>

```c
struct bt_iso_cig
```

相关声明：[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)。

表示连接等时组（Connected Isochronous Group，CIG）的不透明类型。

<a id="r_bt_5Fiso_5Fbig"></a>

```c
struct bt_iso_big
```

相关声明：[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

表示广播等时组（Broadcast Isochronous Group，BIG）的不透明类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga15c9cafd39e89f07eef115e147741098"></a>

```c
#define BT_ISO_CHAN_SEND_RESERVE BT_BUF_ISO_SIZE(0)
```

相关声明：[BT_ISO_CHAN_SEND_RESERVE](#ga15c9cafd39e89f07eef115e147741098)、[BT_BUF_ISO_SIZE](../api_buffer_paging_topic_reference/P002_数据缓冲区（Data buffers）.md#gaa820dee05a7202304e1aaa9a36386ca4)。

发送等时服务数据单元（ISO SDU）所需的头部预留空间（Headroom）。

<a id="r_ga3c0af738d118341da7d370aaa48a89d1"></a>

```c
#define BT_ISO_SDU_BUF_SIZE(mtu)
```

相关声明：[BT_ISO_SDU_BUF_SIZE](#ga3c0af738d118341da7d370aaa48a89d1)。

用于计算等时服务数据单元（ISO SDU）所需缓冲区大小的辅助宏。

<a id="r_ga01b975b441fa5d8f039562ab66857bbf"></a>

```c
#define BT_ISO_BIS_INDEX_BIT(x)
```

相关声明：[BT_ISO_BIS_INDEX_BIT](#ga01b975b441fa5d8f039562ab66857bbf)。

将广播等时流（BIS）索引转换为对应位（Bit）。

<a id="r_gadd421c69edccfd695d728ded5feb6862"></a>

```c
#define BT_ISO_DATA_PATH_HCI 0x00
```

相关声明：[BT_ISO_DATA_PATH_HCI](#gadd421c69edccfd695d728ded5feb6862)。

用于将等时数据路径（ISO Data Path）设为经 HCI 传输的值。

<a id="r_ga4f0cc6262171fbee9d0ef173123b8f3d"></a>

```c
#define BT_ISO_SDU_INTERVAL_UNKNOWN 0x000000U
```

相关声明：[BT_ISO_SDU_INTERVAL_UNKNOWN](#ga4f0cc6262171fbee9d0ef173123b8f3d)。

未知的服务数据单元间隔（SDU Interval）。

<a id="r_ga9f26e30d05e571d3fc33dec8ae693e45"></a>

```c
#define BT_ISO_DATA_PATH_VS_ID_MIN 0x01
```

相关声明：[BT_ISO_DATA_PATH_VS_ID_MIN](#ga9f26e30d05e571d3fc33dec8ae693e45)。

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最小值。

<a id="r_gae5e1f7c86165b26fc6d93bc922676f9a"></a>

```c
#define BT_ISO_DATA_PATH_VS_ID_MAX 0xFE
```

相关声明：[BT_ISO_DATA_PATH_VS_ID_MAX](#gae5e1f7c86165b26fc6d93bc922676f9a)。

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最大值。

<a id="r_ga29bf2b36a4ab4e1325f626bbcf52a9a6"></a>

```c
#define BT_ISO_CONTROLLER_DELAY_MIN 0x000000
```

相关声明：[BT_ISO_CONTROLLER_DELAY_MIN](#ga29bf2b36a4ab4e1325f626bbcf52a9a6)。

最小控制器延迟（Controller Delay），单位为微秒：0 µs。

<a id="r_gae6ba7c8ea447112bcd7798d0351a9a91"></a>

```c
#define BT_ISO_CONTROLLER_DELAY_MAX 0x3D0900
```

相关声明：[BT_ISO_CONTROLLER_DELAY_MAX](#gae6ba7c8ea447112bcd7798d0351a9a91)。

最大控制器延迟（Controller Delay），单位为微秒：4,000,000 µs。

<a id="r_ga8122de88b6e5423dca653b1f0a484316"></a>

```c
#define BT_ISO_SDU_INTERVAL_MIN 0x0000FFU
```

相关声明：[BT_ISO_SDU_INTERVAL_MIN](#ga8122de88b6e5423dca653b1f0a484316)。

最小间隔（Interval），单位为微秒：255 µs。

<a id="r_ga077eb6d219bba947d363e2cce8e0080c"></a>

```c
#define BT_ISO_SDU_INTERVAL_MAX 0x0FFFFFU
```

相关声明：[BT_ISO_SDU_INTERVAL_MAX](#ga077eb6d219bba947d363e2cce8e0080c)。

最大间隔（Interval），单位为微秒：1,048,575 µs。

<a id="r_ga5cc5e9fd5e7af83eeaab8fe2fd16b9de"></a>

```c
#define BT_ISO_ISO_INTERVAL_MIN 0x0004U
```

相关声明：[BT_ISO_ISO_INTERVAL_MIN](#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)。

最小等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 5 ms。

<a id="r_gabc381a7f565061ec91d23b7783521da3"></a>

```c
#define BT_ISO_ISO_INTERVAL_MAX 0x0C80U
```

相关声明：[BT_ISO_ISO_INTERVAL_MAX](#gabc381a7f565061ec91d23b7783521da3)。

最大等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 4,000 ms。

<a id="r_ga77ae350543eb05617c590c0ad9cb0048"></a>

```c
#define BT_ISO_LATENCY_MIN 0x0005
```

相关声明：[BT_ISO_LATENCY_MIN](#ga77ae350543eb05617c590c0ad9cb0048)。

最小延迟（Latency），单位为毫秒：5 ms。

<a id="r_gad5e89d05d8706509d8d9d8dac40e3347"></a>

```c
#define BT_ISO_LATENCY_MAX 0x0FA0
```

相关声明：[BT_ISO_LATENCY_MAX](#gad5e89d05d8706509d8d9d8dac40e3347)。

最大延迟（Latency），单位为毫秒：4,000 ms。

<a id="r_ga6275e8d805e2366522a78f18ca47ac19"></a>

```c
#define BT_ISO_PACKING_SEQUENTIAL 0x00
```

相关声明：[BT_ISO_PACKING_SEQUENTIAL](#ga6275e8d805e2366522a78f18ca47ac19)。

分组将在组内各通道之间顺序发送（Sequentially）。

<a id="r_ga35b037fcce858857642b4c54bae8dd79"></a>

```c
#define BT_ISO_PACKING_INTERLEAVED 0x01
```

相关声明：[BT_ISO_PACKING_INTERLEAVED](#ga35b037fcce858857642b4c54bae8dd79)。

分组将在组内各通道之间交错发送（Interleaved）。

<a id="r_ga696a81180ae25aa686a53b73e352c9d2"></a>

```c
#define BT_ISO_FRAMING_UNFRAMED 0x00
```

相关声明：[BT_ISO_FRAMING_UNFRAMED](#ga696a81180ae25aa686a53b73e352c9d2)。

分组可以成帧（Framed），也可以不成帧（Unframed）。

<a id="r_ga8f9aba389529ad2a3667ca378e99de2b"></a>

```c
#define BT_ISO_FRAMING_FRAMED 0x01
```

相关声明：[BT_ISO_FRAMING_FRAMED](#ga8f9aba389529ad2a3667ca378e99de2b)。

分组始终成帧（Framed）。

<a id="r_gae9dc30b300e2c309d646e3227e8cc00e"></a>

```c
#define BT_ISO_MAX_GROUP_ISO_COUNT 0x1F
```

相关声明：[BT_ISO_MAX_GROUP_ISO_COUNT](#gae9dc30b300e2c309d646e3227e8cc00e)。

单个组内等时通道（Isochronous Channels）的最大数量：31。

<a id="r_ga4cc5565eeda9a3661d49d485637d1db2"></a>

```c
#define BT_ISO_MIN_SDU 0x0001
```

相关声明：[BT_ISO_MIN_SDU](#ga4cc5565eeda9a3661d49d485637d1db2)。

最小服务数据单元（SDU）大小：1 八位组（Octet）。

<a id="r_gaa5d5588e7229db16219b0c44921bbcf7"></a>

```c
#define BT_ISO_MAX_SDU 0x0FFF
```

相关声明：[BT_ISO_MAX_SDU](#gaa5d5588e7229db16219b0c44921bbcf7)。

最大服务数据单元（SDU）大小：4095 八位组（Octets）。

<a id="r_ga4e29d5966f959114754d62a8763c8c1e"></a>

```c
#define BT_ISO_CONNECTED_PDU_MIN 0x0000U
```

相关声明：[BT_ISO_CONNECTED_PDU_MIN](#ga4e29d5966f959114754d62a8763c8c1e)。

最小协议数据单元（PDU）大小：0 八位组（Octet）。

<a id="r_gaee766ff789f1bf01f75c88112ddd2afa"></a>

```c
#define BT_ISO_BROADCAST_PDU_MIN 0x0001U
```

相关声明：[BT_ISO_BROADCAST_PDU_MIN](#gaee766ff789f1bf01f75c88112ddd2afa)。

最小协议数据单元（PDU）大小：1 八位组（Octet）。

<a id="r_ga88fb5690cd1cab4e5e8d5c025cc1af00"></a>

```c
#define BT_ISO_PDU_MAX 0x00FBU
```

相关声明：[BT_ISO_PDU_MAX](#ga88fb5690cd1cab4e5e8d5c025cc1af00)。

最大协议数据单元（PDU）大小：251 八位组（Octets）。

<a id="r_ga2905cddfa456fc846f0c8025487b404d"></a>

```c
#define BT_ISO_BN_MIN 0x01U
```

相关声明：[BT_ISO_BN_MIN](#ga2905cddfa456fc846f0c8025487b404d)。

最小突发数量（Burst Number）：1。

<a id="r_gac05f4f51ea04962679f616bb167b724d"></a>

```c
#define BT_ISO_BN_MAX 0x0FU
```

相关声明：[BT_ISO_BN_MAX](#gac05f4f51ea04962679f616bb167b724d)。

最大突发数量（Burst Number）：15。

<a id="r_ga2d3bde6b34f6b15474926ed97ad11d98"></a>

```c
#define BT_ISO_FT_MIN 0x01U
```

相关声明：[BT_ISO_FT_MIN](#ga2d3bde6b34f6b15474926ed97ad11d98)。

最小刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：1。

<a id="r_ga011c9d5840658fd0ef244f47893ec70e"></a>

```c
#define BT_ISO_FT_MAX 0xFFU
```

相关声明：[BT_ISO_FT_MAX](#ga011c9d5840658fd0ef244f47893ec70e)。

最大刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：255。

<a id="r_ga3eba4c20b4203b0323b14178522e6159"></a>

```c
#define BT_ISO_NSE_MIN 0x01U
```

相关声明：[BT_ISO_NSE_MIN](#ga3eba4c20b4203b0323b14178522e6159)。

最小子事件数量（Number of Subevents）：1。

<a id="r_gab7637d96bde7a41123b34f487eec3436"></a>

```c
#define BT_ISO_NSE_MAX 0x1FU
```

相关声明：[BT_ISO_NSE_MAX](#gab7637d96bde7a41123b34f487eec3436)。

最大子事件数量（Number of Subevents）：31。

<a id="r_gaa1bd6484a248a6fb5abc31202e5076d4"></a>

```c
#define BT_ISO_SYNC_TIMEOUT_MIN 0x000A
```

相关声明：[BT_ISO_SYNC_TIMEOUT_MIN](#gaa1bd6484a248a6fb5abc31202e5076d4)。

最小广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 100 ms。

<a id="r_gaeb66806b649bf828afbd83d15c9823eb"></a>

```c
#define BT_ISO_SYNC_TIMEOUT_MAX 0x4000
```

相关声明：[BT_ISO_SYNC_TIMEOUT_MAX](#gaeb66806b649bf828afbd83d15c9823eb)。

最大广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 163,840 ms。

<a id="r_ga47802144b8523b3d46af9ef97e744bbd"></a>

```c
#define BT_ISO_SYNC_MSE_ANY 0x00
```

相关声明：[BT_ISO_SYNC_MSE_ANY](#ga47802144b8523b3d46af9ef97e744bbd)。

由控制器决定的最大子事件计数值（Maximum Subevent Count）。

<a id="r_gafef299e43e0f58ac23e1a1e75ccd0163"></a>

```c
#define BT_ISO_SYNC_MSE_MIN 0x01
```

相关声明：[BT_ISO_SYNC_MSE_MIN](#gafef299e43e0f58ac23e1a1e75ccd0163)。

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最小值：1。

<a id="r_gafd6e7b48394d6f6c8ddd485927b02b4b"></a>

```c
#define BT_ISO_SYNC_MSE_MAX 0x1F
```

相关声明：[BT_ISO_SYNC_MSE_MAX](#gafd6e7b48394d6f6c8ddd485927b02b4b)。

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最大值：31。

<a id="r_ga39c034475b03f8b228916a27912d6724"></a>

```c
#define BT_ISO_CONNECTED_RTN_MIN 0x00
```

相关声明：[BT_ISO_CONNECTED_RTN_MIN](#ga39c034475b03f8b228916a27912d6724)。

连接等时重传值（Connected ISO Retransmission）的最小值：0。

<a id="r_ga1b52aba83eff5d6ae14169d1d3afa1a7"></a>

```c
#define BT_ISO_CONNECTED_RTN_MAX 0xFF
```

相关声明：[BT_ISO_CONNECTED_RTN_MAX](#ga1b52aba83eff5d6ae14169d1d3afa1a7)。

连接等时重传值（Connected ISO Retransmission）的最大值：255。

<a id="r_ga6297a9444ecab7aee170ef44ba21d744"></a>

```c
#define BT_ISO_BROADCAST_RTN_MIN 0x00
```

相关声明：[BT_ISO_BROADCAST_RTN_MIN](#ga6297a9444ecab7aee170ef44ba21d744)。

广播等时重传值（Broadcast ISO Retransmission）的最小值：0。

<a id="r_ga3a579a5d752d4b19dcb668dd7ef27333"></a>

```c
#define BT_ISO_BROADCAST_RTN_MAX 0x1E
```

相关声明：[BT_ISO_BROADCAST_RTN_MAX](#ga3a579a5d752d4b19dcb668dd7ef27333)。

广播等时重传值（Broadcast ISO Retransmission）的最大值：30。

<a id="r_ga5551cab9896764eec39b8e6102e561e5"></a>

```c
#define BT_ISO_BROADCAST_CODE_SIZE 0x10
```

相关声明：[BT_ISO_BROADCAST_CODE_SIZE](#ga5551cab9896764eec39b8e6102e561e5)。

广播码（Broadcast Code）大小：16 八位组（Octets）。

<a id="r_ga0333b406b29a0a3c355db4f52815ff1a"></a>

```c
#define BT_ISO_BIS_INDEX_MIN 0x01
```

相关声明：[BT_ISO_BIS_INDEX_MIN](#ga0333b406b29a0a3c355db4f52815ff1a)。

广播等时流（BIS）的最低索引：1。

<a id="r_ga834652af6ceef1824799ab0bfa0e426f"></a>

```c
#define BT_ISO_BIS_INDEX_MAX 0x1F
```

相关声明：[BT_ISO_BIS_INDEX_MAX](#ga834652af6ceef1824799ab0bfa0e426f)。

广播等时流（BIS）的最高索引：31。

<a id="r_ga52df7bd114b77872c084e28ca86e0b2e"></a>

```c
#define BT_ISO_IRC_MIN 0x01U
```

相关声明：[BT_ISO_IRC_MIN](#ga52df7bd114b77872c084e28ca86e0b2e)。

最小立即重复次数（Immediate Repetition Count）：1。

<a id="r_ga0f412f1593bcdcfa2b323b285bd508a4"></a>

```c
#define BT_ISO_IRC_MAX 0x0FU
```

相关声明：[BT_ISO_IRC_MAX](#ga0f412f1593bcdcfa2b323b285bd508a4)。

最大立即重复次数（Immediate Repetition Count）：15。

<a id="r_ga3f19aaa432290d67fdf4911d1d044dd8"></a>

```c
#define BT_ISO_PTO_MIN 0x00U
```

相关声明：[BT_ISO_PTO_MIN](#ga3f19aaa432290d67fdf4911d1d044dd8)。

最小预传输偏移（Pre-Transmission Offset）：0。

<a id="r_ga27e812e35a1f12329310851eb9c056f2"></a>

```c
#define BT_ISO_PTO_MAX 0x0FU
```

相关声明：[BT_ISO_PTO_MAX](#ga27e812e35a1f12329310851eb9c056f2)。

最大预传输偏移（Pre-Transmission Offset）：15。

<a id="r_ga4fb7985aa35292671abe881c1570c445"></a>

```c
#define BT_ISO_SUBINTERVAL_NONE 0x00000000U
```

相关声明：[BT_ISO_SUBINTERVAL_NONE](#ga4fb7985aa35292671abe881c1570c445)。

无子间隔（No Subinterval）。

<a id="r_ga8085b01de2d1facb666215282690d674"></a>

```c
#define BT_ISO_SUBINTERVAL_UNKNOWN 0xFFFFFFFFU
```

相关声明：[BT_ISO_SUBINTERVAL_UNKNOWN](#ga8085b01de2d1facb666215282690d674)。

未知子间隔（Unknown Subinterval）。

<a id="r_gab3e9a2596b11d372edef3f356008c1b4"></a>

```c
#define BT_ISO_SUBINTERVAL_MIN 0x00000190U
```

相关声明：[BT_ISO_SUBINTERVAL_MIN](#gab3e9a2596b11d372edef3f356008c1b4)。

最小子间隔（Subinterval），单位为微秒：400 µs。

<a id="r_gace8679596f279f31c66e206909de47d9"></a>

```c
#define BT_ISO_SUBINTERVAL_MAX 0x00009C3FU
```

相关声明：[BT_ISO_SUBINTERVAL_MAX](#gace8679596f279f31c66e206909de47d9)。

最大子间隔（Subinterval），单位为微秒：3,999,999 µs。

<a id="r_ga9becee6d629b8f54f55d2264b6d1baef"></a>

```c
#define BT_ISO_VALID_BIS_BITFIELD(_bis_bitfield)
```

相关声明：[BT_ISO_VALID_BIS_BITFIELD](#ga9becee6d629b8f54f55d2264b6d1baef)。

检查广播等时流位字段（ISO BIS Bitfield）是否有效：`BT_ISO_BIS_INDEX_BIT(1)|..|BT_ISO_BIS_INDEX_BIT(31)`。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_gaf2925460cc22cc4220dc376bcbee6201"></a>

```c
enum bt_iso_state { BT_ISO_STATE_DISCONNECTED , BT_ISO_STATE_CONNECTING , BT_ISO_STATE_CONNECTED , BT_ISO_STATE_DISCONNECTING }
```

相关声明：[bt_iso_state](#gaf2925460cc22cc4220dc376bcbee6201)、[BT_ISO_STATE_DISCONNECTED](#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d)、[BT_ISO_STATE_CONNECTING](#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22)、[BT_ISO_STATE_CONNECTED](#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d)、[BT_ISO_STATE_DISCONNECTING](#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)。

等时通道（ISO Channel）的生命周期状态（Life-Span States）。

<a id="r_gafcbd720c67c6a6e5f1cae1395e1e06f0"></a>

```c
enum bt_iso_chan_type { BT_ISO_CHAN_TYPE_NONE , BT_ISO_CHAN_TYPE_CENTRAL , BT_ISO_CHAN_TYPE_PERIPHERAL , BT_ISO_CHAN_TYPE_BROADCASTER , BT_ISO_CHAN_TYPE_SYNC_RECEIVER }
```

相关声明：[bt_iso_chan_type](#gafcbd720c67c6a6e5f1cae1395e1e06f0)、[BT_ISO_CHAN_TYPE_NONE](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17)、[BT_ISO_CHAN_TYPE_CENTRAL](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)、[BT_ISO_CHAN_TYPE_PERIPHERAL](#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)、[BT_ISO_CHAN_TYPE_BROADCASTER](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)、[BT_ISO_CHAN_TYPE_SYNC_RECEIVER](#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)。

等时通道类型（ISO Channel Type）。

<a id="r_ga2c62af103a71aa8f5f8aa103b1245866"></a>

```c
enum { BT_ISO_FLAGS_VALID = (1UL << (0)) , BT_ISO_FLAGS_ERROR = (1UL << (1)) , BT_ISO_FLAGS_LOST = (1UL << (2)) , BT_ISO_FLAGS_TS = (1UL << (3)) }
```

相关声明：[BT_ISO_FLAGS_VALID](#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382)、[BT_ISO_FLAGS_ERROR](#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218)、[BT_ISO_FLAGS_LOST](#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff)、[BT_ISO_FLAGS_TS](#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)。

等时分组状态标志位（ISO Packet Status Flag Bits）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gaa3407502145a77e08993220f7ce51b4a"></a>

```c
struct bt_iso_chan * bt_iso_get_chan_by_conn (const struct bt_conn *iso)
```

相关声明：[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_get_chan_by_conn](#gaa3407502145a77e08993220f7ce51b4a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通过 `bt_iso_chan::iso` 引用查找 `bt_iso_chan` 对象。

<a id="r_gaff0e52777b2140519c63b54b9618bca8"></a>

```c
int bt_iso_server_register (struct bt_iso_server *server)
```

相关声明：[bt_iso_server_register](#gaff0e52777b2140519c63b54b9618bca8)、[bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)。

注册等时服务器（ISO Server）。

<a id="r_ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6"></a>

```c
int bt_iso_server_unregister (struct bt_iso_server *server)
```

相关声明：[bt_iso_server_unregister](#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)、[bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)。

注销等时服务器（ISO Server）。

<a id="r_gaea03fc251206f18de320506064c1631f"></a>

```c
int bt_iso_cig_create (const struct bt_iso_cig_param *param, struct bt_iso_cig **out_cig)
```

相关声明：[bt_iso_cig_create](#gaea03fc251206f18de320506064c1631f)、[bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)。

以中央设备（Central）身份创建连接等时组（CIG）。

<a id="r_ga98f557c183a82066b81f0265c225bebe"></a>

```c
int bt_iso_cig_reconfigure (struct bt_iso_cig *cig, const struct bt_iso_cig_param *param)
```

相关声明：[bt_iso_cig_reconfigure](#ga98f557c183a82066b81f0265c225bebe)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)、[bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)。

以中央设备（Central）身份重新配置连接等时组（CIG）。

<a id="r_gad4b6a7286593ff099117113b6ca996f8"></a>

```c
int bt_iso_cig_terminate (struct bt_iso_cig *cig)
```

相关声明：[bt_iso_cig_terminate](#gad4b6a7286593ff099117113b6ca996f8)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)。

以中央设备（Central）身份终止连接等时组（CIG）。

<a id="r_ga98953a261f3699b62cd19ab4977e0b4c"></a>

```c
int bt_iso_chan_connect (const struct bt_iso_connect_param *param, size_t count)
```

相关声明：[bt_iso_chan_connect](#ga98953a261f3699b62cd19ab4977e0b4c)、[bt_iso_connect_param](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md)。

在 ACL 连接上连接等时通道（ISO Channels）。

<a id="r_ga94c5c788b099284219e5a303b4b8ea69"></a>

```c
int bt_iso_chan_disconnect (struct bt_iso_chan *chan)
```

相关声明：[bt_iso_chan_disconnect](#ga94c5c788b099284219e5a303b4b8ea69)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)。

断开已连接的等时通道（ISO Channel）。

<a id="r_ga0dbb89a133011a833be7d18161471c6a"></a>

```c
int bt_iso_chan_send (struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_iso_chan_send](#ga0dbb89a133011a833be7d18161471c6a)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向等时通道（ISO Channel）发送不带时间戳（Timestamp）的数据。

<a id="r_gab75b817770e3b685920587afde39d6cd"></a>

```c
int bt_iso_chan_send_ts (struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_iso_chan_send_ts](#gab75b817770e3b685920587afde39d6cd)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向等时通道（ISO Channel）发送带时间戳（Timestamp）的数据。

<a id="r_gaa74c762451cfb5d04ffcd8d396a75447"></a>

```c
int bt_iso_setup_data_path (const struct bt_iso_chan *chan, uint8_t dir, const struct bt_iso_chan_path *path)
```

相关声明：[bt_iso_setup_data_path](#gaa74c762451cfb5d04ffcd8d396a75447)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_iso_chan_path](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md)。

为等时通道（ISO Channel）建立等时数据路径（ISO Data Path）。

<a id="r_ga53be464e005392676830feeddd8cdc22"></a>

```c
int bt_iso_remove_data_path (const struct bt_iso_chan *chan, uint8_t dir)
```

相关声明：[bt_iso_remove_data_path](#ga53be464e005392676830feeddd8cdc22)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除等时通道（ISO Channel）的等时数据路径（ISO Data Path）。

<a id="r_ga75e58ed5bfa48f84000f1ce974d649c6"></a>

```c
int bt_iso_chan_get_info (const struct bt_iso_chan *chan, struct bt_iso_info *info)
```

相关声明：[bt_iso_chan_get_info](#ga75e58ed5bfa48f84000f1ce974d649c6)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_info](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md)。

获取等时通道信息（ISO Channel Info）。

<a id="r_gaa3942147fdeebc36039cc35c4e984411"></a>

```c
int bt_iso_chan_get_tx_sync (const struct bt_iso_chan *chan, struct bt_iso_tx_info *info)
```

相关声明：[bt_iso_chan_get_tx_sync](#gaa3942147fdeebc36039cc35c4e984411)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取等时传输定时信息（ISO Transmission Timing Info）。

<a id="r_ga8a01a56e4a4555ed65a67065facfca76"></a>

```c
int bt_iso_big_register_cb (struct bt_iso_big_cb *cb)
```

相关声明：[bt_iso_big_register_cb](#ga8a01a56e4a4555ed65a67065facfca76)、[bt_iso_big_cb](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md)。

注册广播源（Broadcast Sources）的回调。

<a id="r_gac9937316382d257493c7d0359f1341f5"></a>

```c
int bt_iso_big_create (struct bt_le_ext_adv *padv, struct bt_iso_big_create_param *param, struct bt_iso_big **out_big)
```

相关声明：[bt_iso_big_create](#gac9937316382d257493c7d0359f1341f5)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_iso_big_create_param](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以广播者（Broadcaster）身份创建广播等时组（BIG）。

<a id="r_gab9c06a86bf5cc023f5f9bd16c5d3265b"></a>

```c
int bt_iso_big_terminate (struct bt_iso_big *big)
```

相关声明：[bt_iso_big_terminate](#gab9c06a86bf5cc023f5f9bd16c5d3265b)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以广播者（Broadcaster）或接收者（Receiver）身份终止广播等时组（BIG）。

<a id="r_ga790cfeb8516020f317802e019dca4754"></a>

```c
int bt_iso_big_sync (struct bt_le_per_adv_sync *sync, struct bt_iso_big_sync_param *param, struct bt_iso_big **out_big)
```

相关声明：[bt_iso_big_sync](#ga790cfeb8516020f317802e019dca4754)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_iso_big_sync_param](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以接收者（Receiver）身份创建广播等时组（BIG）。

<a id="r_ga4d4c9b8d6d83abcc8d3b337101922800"></a>

```c
const char * bt_iso_chan_state_str (enum bt_iso_state state)
```

相关声明：[bt_iso_chan_state_str](#ga4d4c9b8d6d83abcc8d3b337101922800)、[bt_iso_state](#gaf2925460cc22cc4220dc376bcbee6201)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回等时通道状态（ISO Channel State）的字符串表示。

## 3.5\_详细说明（Detailed Documentation）

<a id="ga01b975b441fa5d8f039562ab66857bbf"></a>

### `BT_ISO_BIS_INDEX_BIT`

```c
#define BT_ISO_BIS_INDEX_BIT ( x)
```

```c
#include <zephyr/bluetooth/iso.h>
```

展开值（Value）：

```c
(BIT((x) - 1))
```

将广播等时流（BIS）索引转换为对应位（Bit）。

广播等时流（BIS）索引从 0x01 开始，因此允许的最低位为 BIT(0)，对应索引 0x01。例如，要同步到 BIS 索引 0x01 和 0x02，位域值应为 BIT(0) | BIT(1)。一般而言，同步到 BIS 索引 N 时应使用 BIT(N - 1)。

<a id="ga834652af6ceef1824799ab0bfa0e426f"></a>

### `BT_ISO_BIS_INDEX_MAX`

```c
#define BT_ISO_BIS_INDEX_MAX 0x1F
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时流（BIS）的最高索引：31。

<a id="ga0333b406b29a0a3c355db4f52815ff1a"></a>

### `BT_ISO_BIS_INDEX_MIN`

```c
#define BT_ISO_BIS_INDEX_MIN 0x01
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时流（BIS）的最低索引：1。

<a id="gac05f4f51ea04962679f616bb167b724d"></a>

### `BT_ISO_BN_MAX`

```c
#define BT_ISO_BN_MAX 0x0FU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大突发数量（Burst Number）：15。

<a id="ga2905cddfa456fc846f0c8025487b404d"></a>

### `BT_ISO_BN_MIN`

```c
#define BT_ISO_BN_MIN 0x01U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小突发数量（Burst Number）：1。

<a id="ga5551cab9896764eec39b8e6102e561e5"></a>

### `BT_ISO_BROADCAST_CODE_SIZE`

```c
#define BT_ISO_BROADCAST_CODE_SIZE 0x10
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播码（Broadcast Code）大小：16 八位组（Octets）。

<a id="gaee766ff789f1bf01f75c88112ddd2afa"></a>

### `BT_ISO_BROADCAST_PDU_MIN`

```c
#define BT_ISO_BROADCAST_PDU_MIN 0x0001U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小协议数据单元（PDU）大小：1 八位组（Octet）。

<a id="ga3a579a5d752d4b19dcb668dd7ef27333"></a>

### `BT_ISO_BROADCAST_RTN_MAX`

```c
#define BT_ISO_BROADCAST_RTN_MAX 0x1E
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时重传值（Broadcast ISO Retransmission）的最大值：30。

<a id="ga6297a9444ecab7aee170ef44ba21d744"></a>

### `BT_ISO_BROADCAST_RTN_MIN`

```c
#define BT_ISO_BROADCAST_RTN_MIN 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时重传值（Broadcast ISO Retransmission）的最小值：0。

<a id="ga15c9cafd39e89f07eef115e147741098"></a>

### `BT_ISO_CHAN_SEND_RESERVE`

```c
#define BT_ISO_CHAN_SEND_RESERVE BT_BUF_ISO_SIZE(0)
```

```c
#include <zephyr/bluetooth/iso.h>
```

发送等时服务数据单元（ISO SDU）所需的头部预留空间（Headroom）。

<a id="ga4e29d5966f959114754d62a8763c8c1e"></a>

### `BT_ISO_CONNECTED_PDU_MIN`

```c
#define BT_ISO_CONNECTED_PDU_MIN 0x0000U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小协议数据单元（PDU）大小：0 八位组（Octet）。

<a id="ga1b52aba83eff5d6ae14169d1d3afa1a7"></a>

### `BT_ISO_CONNECTED_RTN_MAX`

```c
#define BT_ISO_CONNECTED_RTN_MAX 0xFF
```

```c
#include <zephyr/bluetooth/iso.h>
```

连接等时重传值（Connected ISO Retransmission）的最大值：255。

<a id="ga39c034475b03f8b228916a27912d6724"></a>

### `BT_ISO_CONNECTED_RTN_MIN`

```c
#define BT_ISO_CONNECTED_RTN_MIN 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

连接等时重传值（Connected ISO Retransmission）的最小值：0。

<a id="gae6ba7c8ea447112bcd7798d0351a9a91"></a>

### `BT_ISO_CONTROLLER_DELAY_MAX`

```c
#define BT_ISO_CONTROLLER_DELAY_MAX 0x3D0900
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大控制器延迟（Controller Delay），单位为微秒：4,000,000 µs。

<a id="ga29bf2b36a4ab4e1325f626bbcf52a9a6"></a>

### `BT_ISO_CONTROLLER_DELAY_MIN`

```c
#define BT_ISO_CONTROLLER_DELAY_MIN 0x000000
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小控制器延迟（Controller Delay），单位为微秒：0 µs。

<a id="gadd421c69edccfd695d728ded5feb6862"></a>

### `BT_ISO_DATA_PATH_HCI`

```c
#define BT_ISO_DATA_PATH_HCI 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

用于将等时数据路径（ISO Data Path）设为经 HCI 传输的值。

<a id="gae5e1f7c86165b26fc6d93bc922676f9a"></a>

### `BT_ISO_DATA_PATH_VS_ID_MAX`

```c
#define BT_ISO_DATA_PATH_VS_ID_MAX 0xFE
```

```c
#include <zephyr/bluetooth/iso.h>
```

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最大值。

<a id="ga9f26e30d05e571d3fc33dec8ae693e45"></a>

### `BT_ISO_DATA_PATH_VS_ID_MIN`

```c
#define BT_ISO_DATA_PATH_VS_ID_MIN 0x01
```

```c
#include <zephyr/bluetooth/iso.h>
```

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最小值。

<a id="ga8f9aba389529ad2a3667ca378e99de2b"></a>

### `BT_ISO_FRAMING_FRAMED`

```c
#define BT_ISO_FRAMING_FRAMED 0x01
```

```c
#include <zephyr/bluetooth/iso.h>
```

分组始终成帧（Framed）。

<a id="ga696a81180ae25aa686a53b73e352c9d2"></a>

### `BT_ISO_FRAMING_UNFRAMED`

```c
#define BT_ISO_FRAMING_UNFRAMED 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

分组可以成帧（Framed），也可以不成帧（Unframed）。

<a id="ga011c9d5840658fd0ef244f47893ec70e"></a>

### `BT_ISO_FT_MAX`

```c
#define BT_ISO_FT_MAX 0xFFU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：255。

<a id="ga2d3bde6b34f6b15474926ed97ad11d98"></a>

### `BT_ISO_FT_MIN`

```c
#define BT_ISO_FT_MIN 0x01U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：1。

<a id="ga0f412f1593bcdcfa2b323b285bd508a4"></a>

### `BT_ISO_IRC_MAX`

```c
#define BT_ISO_IRC_MAX 0x0FU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大立即重复次数（Immediate Repetition Count）：15。

<a id="ga52df7bd114b77872c084e28ca86e0b2e"></a>

### `BT_ISO_IRC_MIN`

```c
#define BT_ISO_IRC_MIN 0x01U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小立即重复次数（Immediate Repetition Count）：1。

<a id="gabc381a7f565061ec91d23b7783521da3"></a>

### `BT_ISO_ISO_INTERVAL_MAX`

```c
#define BT_ISO_ISO_INTERVAL_MAX 0x0C80U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 4,000 ms。

<a id="ga5cc5e9fd5e7af83eeaab8fe2fd16b9de"></a>

### `BT_ISO_ISO_INTERVAL_MIN`

```c
#define BT_ISO_ISO_INTERVAL_MIN 0x0004U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 5 ms。

<a id="gad5e89d05d8706509d8d9d8dac40e3347"></a>

### `BT_ISO_LATENCY_MAX`

```c
#define BT_ISO_LATENCY_MAX 0x0FA0
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大延迟（Latency），单位为毫秒：4,000 ms。

<a id="ga77ae350543eb05617c590c0ad9cb0048"></a>

### `BT_ISO_LATENCY_MIN`

```c
#define BT_ISO_LATENCY_MIN 0x0005
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小延迟（Latency），单位为毫秒：5 ms。

<a id="gae9dc30b300e2c309d646e3227e8cc00e"></a>

### `BT_ISO_MAX_GROUP_ISO_COUNT`

```c
#define BT_ISO_MAX_GROUP_ISO_COUNT 0x1F
```

```c
#include <zephyr/bluetooth/iso.h>
```

单个组内等时通道（Isochronous Channels）的最大数量：31。

<a id="gaa5d5588e7229db16219b0c44921bbcf7"></a>

### `BT_ISO_MAX_SDU`

```c
#define BT_ISO_MAX_SDU 0x0FFF
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大服务数据单元（SDU）大小：4095 八位组（Octets）。

<a id="ga4cc5565eeda9a3661d49d485637d1db2"></a>

### `BT_ISO_MIN_SDU`

```c
#define BT_ISO_MIN_SDU 0x0001
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小服务数据单元（SDU）大小：1 八位组（Octet）。

<a id="gab7637d96bde7a41123b34f487eec3436"></a>

### `BT_ISO_NSE_MAX`

```c
#define BT_ISO_NSE_MAX 0x1FU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大子事件数量（Number of Subevents）：31。

<a id="ga3eba4c20b4203b0323b14178522e6159"></a>

### `BT_ISO_NSE_MIN`

```c
#define BT_ISO_NSE_MIN 0x01U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小子事件数量（Number of Subevents）：1。

<a id="ga35b037fcce858857642b4c54bae8dd79"></a>

### `BT_ISO_PACKING_INTERLEAVED`

```c
#define BT_ISO_PACKING_INTERLEAVED 0x01
```

```c
#include <zephyr/bluetooth/iso.h>
```

分组将在组内各通道之间交错发送（Interleaved）。

<a id="ga6275e8d805e2366522a78f18ca47ac19"></a>

### `BT_ISO_PACKING_SEQUENTIAL`

```c
#define BT_ISO_PACKING_SEQUENTIAL 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

分组将在组内各通道之间顺序发送（Sequentially）。

<a id="ga88fb5690cd1cab4e5e8d5c025cc1af00"></a>

### `BT_ISO_PDU_MAX`

```c
#define BT_ISO_PDU_MAX 0x00FBU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大协议数据单元（PDU）大小：251 八位组（Octets）。

<a id="ga27e812e35a1f12329310851eb9c056f2"></a>

### `BT_ISO_PTO_MAX`

```c
#define BT_ISO_PTO_MAX 0x0FU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大预传输偏移（Pre-Transmission Offset）：15。

<a id="ga3f19aaa432290d67fdf4911d1d044dd8"></a>

### `BT_ISO_PTO_MIN`

```c
#define BT_ISO_PTO_MIN 0x00U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小预传输偏移（Pre-Transmission Offset）：0。

<a id="ga3c0af738d118341da7d370aaa48a89d1"></a>

### `BT_ISO_SDU_BUF_SIZE`

```c
#define BT_ISO_SDU_BUF_SIZE ( mtu)
```

```c
#include <zephyr/bluetooth/iso.h>
```

展开值（Value）：

```c
BT_BUF_ISO_SIZE(mtu)
```

用于计算等时服务数据单元（ISO SDU）所需缓冲区大小的辅助宏。

可用于创建缓冲池（Buffer Pools）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mtu` | 所需的 ISO 服务数据单元（SDU）大小。 |

**返回（Returns）**：返回：满足所请求 ISO SDU 最大传输单元（MTU）所需的缓冲区大小。

<a id="ga077eb6d219bba947d363e2cce8e0080c"></a>

### `BT_ISO_SDU_INTERVAL_MAX`

```c
#define BT_ISO_SDU_INTERVAL_MAX 0x0FFFFFU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大间隔（Interval），单位为微秒：1,048,575 µs。

<a id="ga8122de88b6e5423dca653b1f0a484316"></a>

### `BT_ISO_SDU_INTERVAL_MIN`

```c
#define BT_ISO_SDU_INTERVAL_MIN 0x0000FFU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小间隔（Interval），单位为微秒：255 µs。

<a id="ga4f0cc6262171fbee9d0ef173123b8f3d"></a>

### `BT_ISO_SDU_INTERVAL_UNKNOWN`

```c
#define BT_ISO_SDU_INTERVAL_UNKNOWN 0x000000U
```

```c
#include <zephyr/bluetooth/iso.h>
```

未知的服务数据单元间隔（SDU Interval）。

<a id="gace8679596f279f31c66e206909de47d9"></a>

### `BT_ISO_SUBINTERVAL_MAX`

```c
#define BT_ISO_SUBINTERVAL_MAX 0x00009C3FU
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大子间隔（Subinterval），单位为微秒：3,999,999 µs。

该最大值取决于等时间隔（ISO Interval），因为子间隔（Subinterval）须小于等时间隔。

<a id="gab3e9a2596b11d372edef3f356008c1b4"></a>

### `BT_ISO_SUBINTERVAL_MIN`

```c
#define BT_ISO_SUBINTERVAL_MIN 0x00000190U
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小子间隔（Subinterval），单位为微秒：400 µs。

<a id="ga4fb7985aa35292671abe881c1570c445"></a>

### `BT_ISO_SUBINTERVAL_NONE`

```c
#define BT_ISO_SUBINTERVAL_NONE 0x00000000U
```

```c
#include <zephyr/bluetooth/iso.h>
```

无子间隔（No Subinterval）。

<a id="ga8085b01de2d1facb666215282690d674"></a>

### `BT_ISO_SUBINTERVAL_UNKNOWN`

```c
#define BT_ISO_SUBINTERVAL_UNKNOWN 0xFFFFFFFFU
```

```c
#include <zephyr/bluetooth/iso.h>
```

未知子间隔（Unknown Subinterval）。

<a id="ga47802144b8523b3d46af9ef97e744bbd"></a>

### `BT_ISO_SYNC_MSE_ANY`

```c
#define BT_ISO_SYNC_MSE_ANY 0x00
```

```c
#include <zephyr/bluetooth/iso.h>
```

由控制器决定的最大子事件计数值（Maximum Subevent Count）。

<a id="gafd6e7b48394d6f6c8ddd485927b02b4b"></a>

### `BT_ISO_SYNC_MSE_MAX`

```c
#define BT_ISO_SYNC_MSE_MAX 0x1F
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最大值：31。

<a id="gafef299e43e0f58ac23e1a1e75ccd0163"></a>

### `BT_ISO_SYNC_MSE_MIN`

```c
#define BT_ISO_SYNC_MSE_MIN 0x01
```

```c
#include <zephyr/bluetooth/iso.h>
```

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最小值：1。

<a id="gaeb66806b649bf828afbd83d15c9823eb"></a>

### `BT_ISO_SYNC_TIMEOUT_MAX`

```c
#define BT_ISO_SYNC_TIMEOUT_MAX 0x4000
```

```c
#include <zephyr/bluetooth/iso.h>
```

最大广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 163,840 ms。

<a id="gaa1bd6484a248a6fb5abc31202e5076d4"></a>

### `BT_ISO_SYNC_TIMEOUT_MIN`

```c
#define BT_ISO_SYNC_TIMEOUT_MIN 0x000A
```

```c
#include <zephyr/bluetooth/iso.h>
```

最小广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 100 ms。

<a id="ga9becee6d629b8f54f55d2264b6d1baef"></a>

### `BT_ISO_VALID_BIS_BITFIELD`

```c
#define BT_ISO_VALID_BIS_BITFIELD ( _bis_bitfield)
```

```c
#include <zephyr/bluetooth/iso.h>
```

展开值（Value）：

```c
((_bis_bitfield) != 0U && (_bis_bitfield) <= BIT_MASK(BT_ISO_BIS_INDEX_MAX))
```

检查广播等时流位字段（ISO BIS Bitfield）是否有效：`BT_ISO_BIS_INDEX_BIT(1)|..|BT_ISO_BIS_INDEX_BIT(31)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_bis_bitfield` | BIS 索引位域（Index Bitfield），类型为 uint32。 |

<a id="ga2c62af103a71aa8f5f8aa103b1245866"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/iso.h>
```

等时分组状态标志位（ISO Packet Status Flag Bits）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ISO_FLAGS_VALID` | ISO 数据包有效（Valid）。 |
| `BT_ISO_FLAGS_ERROR` | ISO 数据包可能包含错误，可能由循环冗余校验（CRC）失败或 SDU 的部分数据缺失引起。 |
| `BT_ISO_FLAGS_LOST` | ISO 数据包已丢失（Lost）。 |
| `BT_ISO_FLAGS_TS` | 时间戳有效（Timestamp Valid）。若未设置此标志，则 bt_iso_recv_info.ts 的值无效，不应使用。 |

<a id="gafcbd720c67c6a6e5f1cae1395e1e06f0"></a>

### `bt_iso_chan_type`

```c
enum bt_iso_chan_type
```

```c
#include <zephyr/bluetooth/iso.h>
```

等时通道类型（ISO Channel Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ISO_CHAN_TYPE_NONE` | 无信道类型（Channel Type）。 |
| `BT_ISO_CHAN_TYPE_CENTRAL` | 作为中心设备（Central）连接。 |
| `BT_ISO_CHAN_TYPE_PERIPHERAL` | 作为外围设备（Peripheral）连接。 |
| `BT_ISO_CHAN_TYPE_BROADCASTER` | 等时广播者（Isochronous Broadcaster）。 |
| `BT_ISO_CHAN_TYPE_SYNC_RECEIVER` | 同步接收者（Synchronized Receiver）。 |

<a id="gaf2925460cc22cc4220dc376bcbee6201"></a>

### `bt_iso_state`

```c
enum bt_iso_state
```

```c
#include <zephyr/bluetooth/iso.h>
```

等时通道（ISO Channel）的生命周期状态（Life-Span States）。

仅供根据操作上下文（Operational Context）将信道设置为相应状态的内部 API 使用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ISO_STATE_DISCONNECTED` | 信道已断开（Disconnected）。 |
| `BT_ISO_STATE_CONNECTING` | 信道处于正在连接状态（Connecting）。 |
| `BT_ISO_STATE_CONNECTED` | 信道已就绪，可承载上层流量（Upper Layer Traffic）。 |
| `BT_ISO_STATE_DISCONNECTING` | 信道处于正在断开状态（Disconnecting）。 |

<a id="gac9937316382d257493c7d0359f1341f5"></a>

### `bt_iso_big_create()`

```c
int bt_iso_big_create ( struct bt_le_ext_adv * padv, struct bt_iso_big_create_param * param, struct bt_iso_big ** out_big )
```

```c
#include <zephyr/bluetooth/iso.h>
```

以广播者（Broadcaster）身份创建广播等时组（BIG）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] padv` | 指向用于发送 BIGInfo 的周期性广播对象（Periodic Advertising Object）的指针。 |
| `[in] param` | 用于创建并启用广播等时组（BIG）的参数。服务质量（QoS）参数由此参数中 BIS 列表的第一个 BIS 的 QOS 字段决定。 |
| `[out] out_big` | 成功时返回广播等时组对象（Broadcast Isochronous Group Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga8a01a56e4a4555ed65a67065facfca76"></a>

### `bt_iso_big_register_cb()`

```c
int bt_iso_big_register_cb ( struct bt_iso_big_cb * cb)
```

```c
#include <zephyr/bluetooth/iso.h>
```

注册广播源（Broadcast Sources）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EEXIST` | cb 已注册时。 |

<a id="ga790cfeb8516020f317802e019dca4754"></a>

### `bt_iso_big_sync()`

```c
int bt_iso_big_sync ( struct bt_le_per_adv_sync * sync, struct bt_iso_big_sync_param * param, struct bt_iso_big ** out_big )
```

```c
#include <zephyr/bluetooth/iso.h>
```

以接收者（Receiver）身份创建广播等时组（BIG）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] sync` | 指向收到 BIGInfo 的周期性广播同步对象（Periodic Advertising Sync Object）的指针。 |
| `[in] param` | 用于创建并启用 BIG 同步（BIG Sync）的参数。 |
| `[out] out_big` | 成功时返回广播等时组对象（Broadcast Isochronous Group Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gab9c06a86bf5cc023f5f9bd16c5d3265b"></a>

### `bt_iso_big_terminate()`

```c
int bt_iso_big_terminate ( struct bt_iso_big * big)
```

```c
#include <zephyr/bluetooth/iso.h>
```

以广播者（Broadcaster）或接收者（Receiver）身份终止广播等时组（BIG）。

不能在 bt_iso_big_cb::started、bt_iso_big_cb::stopped、bt_iso_chan_ops::connected 或 bt_iso_chan_ops::disconnected 回调内调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `big` | 指向 BIG 结构体的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga98953a261f3699b62cd19ab4977e0b4c"></a>

### `bt_iso_chan_connect()`

```c
int bt_iso_chan_connect ( const struct bt_iso_connect_param * param, size_t count )
```

```c
#include <zephyr/bluetooth/iso.h>
```

在 ACL 连接上连接等时通道（ISO Channels）。

连接 ISO 信道（ISO Channels）。必须先调用 bt_iso_cig_create()，在连接等时组（CIG）中初始化这些 ISO 信道。

连接完成后，将调用各信道的 connected() 回调。如果连接被拒绝，则改为调用 disconnected() 回调。

此函数还会根据每个信道的 bt_iso_chan_io_qos 中的 path 参数设置 ISO 数据路径（Data Path）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 指向连接参数数组（Connect Parameter Array）的指针；数组元素包含 ISO 和 ACL 指针。 |
| `count` | 连接参数（Connect Parameters）的数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功启动连接过程（Connecting Procedure）。 |
| `-EINVAL` | 提供了无效参数（Invalid Parameters）。 |
| `-EBUSY` | 某些 ISO 信道已在连接中。不允许同时存在多个未完成的连接请求。如果启用了 CONFIG_BT_SMP，且配对过程（Pairing Procedure）已在进行，也可能返回此错误。 |
| `-ENOBUFS` | 没有可用缓冲区向控制器发送请求；或者启用了 CONFIG_BT_SMP，但无法再存储更多密钥（Keys）。 |
| `-ENOMEM` | 启用了 CONFIG_BT_SMP，但无法再存储更多密钥（Keys）。 |
| `-EIO` | 控制器拒绝了请求；或者启用了 CONFIG_BT_SMP，但配对（Pairing）已超时。 |
| `-ENOTCONN` | 启用了 CONFIG_BT_SMP，但 ACL 尚未连接。 |

<a id="ga94c5c788b099284219e5a303b4b8ea69"></a>

### `bt_iso_chan_disconnect()`

```c
int bt_iso_chan_disconnect ( struct bt_iso_chan * chan)
```

```c
#include <zephyr/bluetooth/iso.h>
```

断开已连接的等时通道（ISO Channel）。

断开已连接的等时通道（ISO Channel）。

如果设备是中心设备（Central）且连接尚未完成，则取消该连接，并由此调用信道的 bt_iso_chan_ops.disconnected() 回调。

如果设备是外围设备（Peripheral）且连接尚未完成，则拒绝该连接；外围设备须等待 CIS Established 事件，发生错误时该事件可能触发 bt_iso_chan_ops.disconnected() 回调。

有关输入参数的详细信息，参见 bt_iso_chan_connect() API 的参考说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga75e58ed5bfa48f84000f1ce974d649c6"></a>

### `bt_iso_chan_get_info()`

```c
int bt_iso_chan_get_info ( const struct bt_iso_chan * chan, struct bt_iso_info * info )
```

```c
#include <zephyr/bluetooth/iso.h>
```

获取等时通道信息（ISO Channel Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |
| `info` | 信道信息对象（Channel Info Object）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaa3942147fdeebc36039cc35c4e984411"></a>

### `bt_iso_chan_get_tx_sync()`

```c
int bt_iso_chan_get_tx_sync ( const struct bt_iso_chan * chan, struct bt_iso_tx_info * info )
```

```c
#include <zephyr/bluetooth/iso.h>
```

获取等时传输定时信息（ISO Transmission Timing Info）。

读取 ISO 信道（ISO Channel）上已发送 ISO 数据包的时序信息（Timing Information）。通过 HCI_LE_Read_ISO_TX_Sync HCI 命令从控制器获取此信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chan` | 信道对象（Channel Object）。 |
| `[out] info` | 发送信息对象（Transmit Info Object）。 |

**说明（Note）**：注意：此函数要成功返回，必须已在该 ISO 信道上成功发送过一个服务数据单元（SDU）。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga0dbb89a133011a833be7d18161471c6a"></a>

### `bt_iso_chan_send()`

```c
int bt_iso_chan_send ( struct bt_iso_chan * chan, struct net_buf * buf, uint16_t seq_num )
```

```c
#include <zephyr/bluetooth/iso.h>
```

向等时通道（ISO Channel）发送不带时间戳（Timestamp）的数据。

将缓冲区中的数据发送到信道。若没有可用额度（Credits），则将 buf 排队，待收到对端提供的额度后发送。有关第一个输入参数的详细信息，参见 bt_iso_chan_connect() API 的参考说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：返回：成功时为发送的八位字节数（Octets），发生错误时为负值。

<a id="gab75b817770e3b685920587afde39d6cd"></a>

### `bt_iso_chan_send_ts()`

```c
int bt_iso_chan_send_ts ( struct bt_iso_chan * chan, struct net_buf * buf, uint16_t seq_num, uint32_t ts )
```

```c
#include <zephyr/bluetooth/iso.h>
```

向等时通道（ISO Channel）发送带时间戳（Timestamp）的数据。

将缓冲区中的数据发送到信道。若没有可用额度（Credits），则将 buf 排队，待收到对端提供的额度后发送。有关第一个输入参数的详细信息，参见 bt_iso_chan_connect() API 的参考说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 信道对象（Channel Object）。 |
| `buf` | 包含待发送数据的缓冲区。 |
| `seq_num` | 分组序列号（Packet Sequence Number）。对此函数的每次调用都必须递增该值；对于特定通道，每个 SDU 间隔内至少递增一次。 |
| `ts` | 服务数据单元（SDU）的时间戳，单位为微秒（µs）。可使用此值，在连接等时组（CIG）或广播等时组（BIG）的同一个 SDU 间隔内发送多个 SDU。 |

**说明（Note）**：注意：成功时，缓冲区所有权（Buffer Ownership）转交给协议栈；发生错误时，调用者保留缓冲区所有权。

**返回（Returns）**：返回：成功时为发送的八位字节数（Octets），发生错误时为负值。

<a id="ga4d4c9b8d6d83abcc8d3b337101922800"></a>

### `bt_iso_chan_state_str()`

```c
const char * bt_iso_chan_state_str ( enum bt_iso_state state)
```

```c
#include <zephyr/bluetooth/iso.h>
```

返回等时通道状态（ISO Channel State）的字符串表示。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 信道状态（Channel State）。 |

**返回（Returns）**：返回：状态的字符串表示；若状态未知，则返回 "unknown"。

<a id="gaea03fc251206f18de320506064c1631f"></a>

### `bt_iso_cig_create()`

```c
int bt_iso_cig_create ( const struct bt_iso_cig_param * param, struct bt_iso_cig ** out_cig )
```

```c
#include <zephyr/bluetooth/iso.h>
```

以中央设备（Central）身份创建连接等时组（CIG）。

可在任何时候调用，包括连接远端设备之前。连接任何连接等时流（CIS）信道之前，必须先调用此函数。

创建连接等时组（CIG）后，可通过 bt_iso_chan_connect() 连接 param 中提供的信道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 用于创建并启用连接等时组（CIG）的参数。 |
| `[out] out_cig` | 成功时返回连接等时组对象（Connected Isochronous Group Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga98f557c183a82066b81f0265c225bebe"></a>

### `bt_iso_cig_reconfigure()`

```c
int bt_iso_cig_reconfigure ( struct bt_iso_cig * cig, const struct bt_iso_cig_param * param )
```

```c
#include <zephyr/bluetooth/iso.h>
```

以中央设备（Central）身份重新配置连接等时组（CIG）。

此函数可更新连接等时组（CIG）。它会更新组级参数；若提供了相应参数，还会修改各个 CIS 的服务质量（QoS）参数。如果 param 中的 cis_channels 包含原先调用 bt_iso_cig_create() 时没有的 CIS，将把这些 CIS 添加到组中。组创建后不能从中移除任何 CIS。

可在将 ISO 连接到远端设备前的任何时候调用。一旦组内任意 CIS 已连接，就不能再修改该组。

创建连接等时组（CIG）后，可通过 bt_iso_chan_connect() 连接 param 中提供的信道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cig` | 连接等时组对象（Connected Isochronous Group Object）。 |
| `param` | 用于重新配置连接等时组（CIG）的参数。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gad4b6a7286593ff099117113b6ca996f8"></a>

### `bt_iso_cig_terminate()`

```c
int bt_iso_cig_terminate ( struct bt_iso_cig * cig)
```

```c
#include <zephyr/bluetooth/iso.h>
```

以中央设备（Central）身份终止连接等时组（CIG）。

必须先断开连接等时组（CIG）中的所有 CIS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cig` | 指向 CIG 结构体的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaa3407502145a77e08993220f7ce51b4a"></a>

### `bt_iso_get_chan_by_conn()`

```c
struct bt_iso_chan * bt_iso_get_chan_by_conn ( const struct bt_conn * iso)
```

```c
#include <zephyr/bluetooth/iso.h>
```

通过 `bt_iso_chan::iso` 引用查找 `bt_iso_chan` 对象。

例如使用 bt_conn_foreach 时，可借此获取对应的 bt_iso_chan 对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iso` | 类型为 BT_CONN_TYPE_ISO 的连接对象（Connection Object）。 |

**返回（Returns）**：返回：对应的 bt_iso_chan 对象，或 NULL。

<a id="ga53be464e005392676830feeddd8cdc22"></a>

### `bt_iso_remove_data_path()`

```c
int bt_iso_remove_data_path ( const struct bt_iso_chan * chan, uint8_t dir )
```

```c
#include <zephyr/bluetooth/iso.h>
```

移除等时通道（ISO Channel）的等时数据路径（ISO Data Path）。

移除由 bt_iso_setup_data_path() 为给定 dir 配置的 ISO 数据路径（Data Path）。

根据《蓝牙核心规范》（Bluetooth Core Specification）6.0 第 4 卷 E 部分 7.7.5 节，外围设备（Peripheral）的 CIS 数据路径由控制器删除，因此外围设备的 CIS 断开后，无需也不能再移除其数据路径。中心设备（Central）的 CIS 数据路径在断开后仍然有效，因此中心设备若不再使用该 CIS，应在断开时调用 bt_iso_remove_data_path()。通过 bt_iso_cig_terminate() 移除 CIG 时，中心设备创建的全部数据路径都会被移除。

根据《蓝牙核心规范》（Bluetooth Core Specification）6.0 第 4 卷 E 部分 7.7.65.30 节，当 BIG 同步丢失或终止时，控制器会移除与 ISO 同步接收者（Sync Receiver）BIG 关联的所有数据路径，因此同步接收者无需也不能再移除该 BIG 关联 ISO 信道的数据路径。

根据《蓝牙核心规范》（Bluetooth Core Specification）6.0 第 4 卷 E 部分 7.8.105 节，通过 bt_iso_big_terminate() 终止 BIG 时，会移除与 ISO 广播者（Broadcaster）BIG 关联的所有数据路径，因此广播者无需也不能再移除该 BIG 关联 ISO 信道的数据路径。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要为其设置 ISO 数据路径（Data Path）的信道。 |
| `dir` | 要设置的方向（Direction），为 BT_HCI_DATAPATH_DIR_CTLR_TO_HOST 或 BT_HCI_DATAPATH_DIR_HOST_TO_CTLR。对于 ISO 广播信道，只能使用 BT_HCI_DATAPATH_DIR_HOST_TO_CTLR；对于 ISO 同步接收信道，只能使用 BT_HCI_DATAPATH_DIR_CTLR_TO_HOST。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（Invalid Parameters）。 |
| `-ENOBUFS` | 无法分配 HCI 命令缓冲区（Command Buffer）。 |
| `-EIO` | 控制器拒绝了请求，或响应包含无效数据。 |
| `-ENODEV` | chan 未关联 CIS 或 BIS 句柄（Handle）。 |
| `-EACCES` | 控制器因不允许此操作而拒绝了请求。 |
| `-ENOEXEC` | 发生了意外错误（Unexpected Error）。 |

<a id="gaff0e52777b2140519c63b54b9618bca8"></a>

### `bt_iso_server_register()`

```c
int bt_iso_server_register ( struct bt_iso_server * server)
```

```c
#include <zephyr/bluetooth/iso.h>
```

注册等时服务器（ISO Server）。

注册 ISO 服务器（ISO Server）。每个新连接均通过 accept() 回调授权；授权成功时，该回调须分配供新连接使用的信道结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6"></a>

### `bt_iso_server_unregister()`

```c
int bt_iso_server_unregister ( struct bt_iso_server * server)
```

```c
#include <zephyr/bluetooth/iso.h>
```

注销等时服务器（ISO Server）。

注销先前注册的 ISO 服务器（ISO Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaa74c762451cfb5d04ffcd8d396a75447"></a>

### `bt_iso_setup_data_path()`

```c
int bt_iso_setup_data_path ( const struct bt_iso_chan * chan, uint8_t dir, const struct bt_iso_chan_path * path )
```

```c
#include <zephyr/bluetooth/iso.h>
```

为等时通道（ISO Channel）建立等时数据路径（ISO Data Path）。

信道必须先关联 BIS 或 CIS 句柄（Handle）；调用 bt_iso_chan_ops.connected() 回调时，这一条件已满足。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan` | 要为其设置 ISO 数据路径（Data Path）的信道。 |
| `dir` | 要设置的方向（Direction），为 BT_HCI_DATAPATH_DIR_CTLR_TO_HOST 或 BT_HCI_DATAPATH_DIR_HOST_TO_CTLR。对于 ISO 广播信道，只能使用 BT_HCI_DATAPATH_DIR_HOST_TO_CTLR；对于 ISO 同步接收信道，只能使用 BT_HCI_DATAPATH_DIR_CTLR_TO_HOST。 |
| `path` | 数据路径（Data Path）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 参数无效（Invalid Parameters）。 |
| `-ENOBUFS` | 无法分配 HCI 命令缓冲区（Command Buffer）。 |
| `-EIO` | 控制器拒绝了请求，或响应包含无效数据。 |
| `-ENODEV` | chan 未关联 CIS 或 BIS 句柄（Handle）。 |
| `-EACCES` | 控制器因不允许此操作而拒绝了请求。 |
| `-ENOEXEC` | 发生了意外错误（Unexpected Error）。 |


## 3.6\_原页交叉引用（Cross References）

- [bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)
- [bt_iso_chan_io_qos](../bluetooth_connection_model_reference/P078_bt_iso_chan_io_qos_结构体.md)
- [bt_iso_chan_qos](../bluetooth_connection_model_reference/P081_bt_iso_chan_qos_结构体.md)
- [bt_iso_chan_path](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md)
- [bt_iso_recv_info](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md)
- [bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)
- [bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)
- [bt_iso_connect_param](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md)
- [bt_iso_big_create_param](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md)
- [bt_iso_big_sync_param](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md)
- [bt_iso_biginfo](../bluetooth_connection_model_reference/P075_bt_iso_biginfo_结构体.md)
- [bt_iso_chan_ops](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md)
- [bt_iso_accept_info](../bluetooth_connection_model_reference/P070_bt_iso_accept_info_结构体.md)
- [bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)
- [bt_iso_unicast_tx_info](../bluetooth_connection_model_reference/P091_bt_iso_unicast_tx_info_结构体.md)
- [bt_iso_unicast_info](../bluetooth_connection_model_reference/P090_bt_iso_unicast_info_结构体.md)
- [bt_iso_broadcaster_info](../bluetooth_connection_model_reference/P076_bt_iso_broadcaster_info_结构体.md)
- [bt_iso_sync_receiver_info](../bluetooth_connection_model_reference/P088_bt_iso_sync_receiver_info_结构体.md)
- [bt_iso_info](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md)
- [bt_iso_big_cb](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md)
- [bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)
- [bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)
- [BT_BUF_ISO_SIZE](../api_buffer_paging_topic_reference/P002_数据缓冲区（Data buffers）.md#gaa820dee05a7202304e1aaa9a36386ca4)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_iso_chan::iso](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a7fd728385a3aec11be8883bdee8aedea)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [zephyr/bluetooth/iso.h](../api_file_mesh_acpi_reference/P006_zephyr__bluetooth__iso.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [bt_iso_recv_info.ts](../bluetooth_connection_model_reference/P086_bt_iso_recv_info_结构体.md#a4bf778ae9be39eb4a740c2eb9670d98a)
- [bt_iso_big_cb::started](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#ac84e00545dbb330311482eb5abd4a78b)
- [bt_iso_big_cb::stopped](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md#a43d6ee745f7852460f843ced33c777c2)
- [bt_iso_chan_ops::connected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a6b0e51770158da7b728e1084a8e44504)
- [bt_iso_chan_ops::disconnected](../bluetooth_connection_model_reference/P079_bt_iso_chan_ops_结构体.md#a2069849352019362e5dc7d68f835f359)
- [CONFIG_BT_SMP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)
- [BT_CONN_TYPE_ISO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)
- [BT_HCI_DATAPATH_DIR_CTLR_TO_HOST](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#af8d89c712a3d27f9b6f92a31bea2a8c3)
- [BT_HCI_DATAPATH_DIR_HOST_TO_CTLR](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a0f74c19fabbcb3088e1a819d33a05a1c)
- [accept()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__bt__buf_html_gaa820dee05a7202304e1aaa9a36386ca4"></a>
<a id="agroup__bt__iso_html_ga834652af6ceef1824799ab0bfa0e426f"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382"></a>
<a id="gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218"></a>
<a id="gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff"></a>
<a id="gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23"></a>
<a id="ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17"></a>
<a id="ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a"></a>
<a id="ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb"></a>
<a id="ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b"></a>
<a id="ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2"></a>
<a id="ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d"></a>
<a id="ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22"></a>
<a id="ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d"></a>
<a id="ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_编解码器配置解析 API（Codec config parsing APIs）.md) · [返回大纲](大纲.md) · [下一章](P004_逻辑链路控制与适配协议（L2CAP）.md)
