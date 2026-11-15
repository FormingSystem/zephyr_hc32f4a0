---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-6
title: zephyr__bluetooth__iso.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_bluetooth\_\_iso.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙等时通信（ISO）的处理。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙等时通信（ISO）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga15c9cafd39e89f07eef115e147741098"></a>

```c
#define BT_ISO_CHAN_SEND_RESERVE BT_BUF_ISO_SIZE(0)
```

相关声明：[BT_ISO_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga15c9cafd39e89f07eef115e147741098)、[BT_BUF_ISO_SIZE](../api_buffer_paging_topic_reference/P002_数据缓冲区（Data buffers）.md#gaa820dee05a7202304e1aaa9a36386ca4)。

发送等时服务数据单元（ISO SDU）所需的头部预留空间（Headroom）。

<a id="r_ga3c0af738d118341da7d370aaa48a89d1"></a>

```c
#define BT_ISO_SDU_BUF_SIZE(mtu)
```

相关声明：[BT_ISO_SDU_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3c0af738d118341da7d370aaa48a89d1)。

用于计算等时服务数据单元（ISO SDU）所需缓冲区大小的辅助宏。

<a id="r_ga01b975b441fa5d8f039562ab66857bbf"></a>

```c
#define BT_ISO_BIS_INDEX_BIT(x)
```

相关声明：[BT_ISO_BIS_INDEX_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga01b975b441fa5d8f039562ab66857bbf)。

将广播等时流（BIS）索引转换为对应位（Bit）。

<a id="r_gadd421c69edccfd695d728ded5feb6862"></a>

```c
#define BT_ISO_DATA_PATH_HCI 0x00
```

相关声明：[BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)。

用于将等时数据路径（ISO Data Path）设为经 HCI 传输的值。

<a id="r_ga4f0cc6262171fbee9d0ef173123b8f3d"></a>

```c
#define BT_ISO_SDU_INTERVAL_UNKNOWN 0x000000U
```

相关声明：[BT_ISO_SDU_INTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4f0cc6262171fbee9d0ef173123b8f3d)。

未知的服务数据单元间隔（SDU Interval）。

<a id="r_ga9f26e30d05e571d3fc33dec8ae693e45"></a>

```c
#define BT_ISO_DATA_PATH_VS_ID_MIN 0x01
```

相关声明：[BT_ISO_DATA_PATH_VS_ID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga9f26e30d05e571d3fc33dec8ae693e45)。

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最小值。

<a id="r_gae5e1f7c86165b26fc6d93bc922676f9a"></a>

```c
#define BT_ISO_DATA_PATH_VS_ID_MAX 0xFE
```

相关声明：[BT_ISO_DATA_PATH_VS_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae5e1f7c86165b26fc6d93bc922676f9a)。

厂商特定数据路径标识符（Vendor Specific Data Path ID）的最大值。

<a id="r_ga29bf2b36a4ab4e1325f626bbcf52a9a6"></a>

```c
#define BT_ISO_CONTROLLER_DELAY_MIN 0x000000
```

相关声明：[BT_ISO_CONTROLLER_DELAY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga29bf2b36a4ab4e1325f626bbcf52a9a6)。

最小控制器延迟（Controller Delay），单位为微秒：0 µs。

<a id="r_gae6ba7c8ea447112bcd7798d0351a9a91"></a>

```c
#define BT_ISO_CONTROLLER_DELAY_MAX 0x3D0900
```

相关声明：[BT_ISO_CONTROLLER_DELAY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae6ba7c8ea447112bcd7798d0351a9a91)。

最大控制器延迟（Controller Delay），单位为微秒：4,000,000 µs。

<a id="r_ga8122de88b6e5423dca653b1f0a484316"></a>

```c
#define BT_ISO_SDU_INTERVAL_MIN 0x0000FFU
```

相关声明：[BT_ISO_SDU_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8122de88b6e5423dca653b1f0a484316)。

最小间隔（Interval），单位为微秒：255 µs。

<a id="r_ga077eb6d219bba947d363e2cce8e0080c"></a>

```c
#define BT_ISO_SDU_INTERVAL_MAX 0x0FFFFFU
```

相关声明：[BT_ISO_SDU_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga077eb6d219bba947d363e2cce8e0080c)。

最大间隔（Interval），单位为微秒：1,048,575 µs。

<a id="r_ga5cc5e9fd5e7af83eeaab8fe2fd16b9de"></a>

```c
#define BT_ISO_ISO_INTERVAL_MIN 0x0004U
```

相关声明：[BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)。

最小等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 5 ms。

<a id="r_gabc381a7f565061ec91d23b7783521da3"></a>

```c
#define BT_ISO_ISO_INTERVAL_MAX 0x0C80U
```

相关声明：[BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)。

最大等时间隔（ISO Interval），以 1.25 ms 为单位表示，对应 4,000 ms。

<a id="r_ga77ae350543eb05617c590c0ad9cb0048"></a>

```c
#define BT_ISO_LATENCY_MIN 0x0005
```

相关声明：[BT_ISO_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga77ae350543eb05617c590c0ad9cb0048)。

最小延迟（Latency），单位为毫秒：5 ms。

<a id="r_gad5e89d05d8706509d8d9d8dac40e3347"></a>

```c
#define BT_ISO_LATENCY_MAX 0x0FA0
```

相关声明：[BT_ISO_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad5e89d05d8706509d8d9d8dac40e3347)。

最大延迟（Latency），单位为毫秒：4,000 ms。

<a id="r_ga6275e8d805e2366522a78f18ca47ac19"></a>

```c
#define BT_ISO_PACKING_SEQUENTIAL 0x00
```

相关声明：[BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)。

分组将在组内各通道之间顺序发送（Sequentially）。

<a id="r_ga35b037fcce858857642b4c54bae8dd79"></a>

```c
#define BT_ISO_PACKING_INTERLEAVED 0x01
```

相关声明：[BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)。

分组将在组内各通道之间交错发送（Interleaved）。

<a id="r_ga696a81180ae25aa686a53b73e352c9d2"></a>

```c
#define BT_ISO_FRAMING_UNFRAMED 0x00
```

相关声明：[BT_ISO_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga696a81180ae25aa686a53b73e352c9d2)。

分组可以成帧（Framed），也可以不成帧（Unframed）。

<a id="r_ga8f9aba389529ad2a3667ca378e99de2b"></a>

```c
#define BT_ISO_FRAMING_FRAMED 0x01
```

相关声明：[BT_ISO_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8f9aba389529ad2a3667ca378e99de2b)。

分组始终成帧（Framed）。

<a id="r_gae9dc30b300e2c309d646e3227e8cc00e"></a>

```c
#define BT_ISO_MAX_GROUP_ISO_COUNT 0x1F
```

相关声明：[BT_ISO_MAX_GROUP_ISO_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae9dc30b300e2c309d646e3227e8cc00e)。

单个组内等时通道（Isochronous Channels）的最大数量：31。

<a id="r_ga4cc5565eeda9a3661d49d485637d1db2"></a>

```c
#define BT_ISO_MIN_SDU 0x0001
```

相关声明：[BT_ISO_MIN_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4cc5565eeda9a3661d49d485637d1db2)。

最小服务数据单元（SDU）大小：1 八位组（Octet）。

<a id="r_gaa5d5588e7229db16219b0c44921bbcf7"></a>

```c
#define BT_ISO_MAX_SDU 0x0FFF
```

相关声明：[BT_ISO_MAX_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa5d5588e7229db16219b0c44921bbcf7)。

最大服务数据单元（SDU）大小：4095 八位组（Octets）。

<a id="r_ga4e29d5966f959114754d62a8763c8c1e"></a>

```c
#define BT_ISO_CONNECTED_PDU_MIN 0x0000U
```

相关声明：[BT_ISO_CONNECTED_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4e29d5966f959114754d62a8763c8c1e)。

最小协议数据单元（PDU）大小：0 八位组（Octet）。

<a id="r_gaee766ff789f1bf01f75c88112ddd2afa"></a>

```c
#define BT_ISO_BROADCAST_PDU_MIN 0x0001U
```

相关声明：[BT_ISO_BROADCAST_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaee766ff789f1bf01f75c88112ddd2afa)。

最小协议数据单元（PDU）大小：1 八位组（Octet）。

<a id="r_ga88fb5690cd1cab4e5e8d5c025cc1af00"></a>

```c
#define BT_ISO_PDU_MAX 0x00FBU
```

相关声明：[BT_ISO_PDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga88fb5690cd1cab4e5e8d5c025cc1af00)。

最大协议数据单元（PDU）大小：251 八位组（Octets）。

<a id="r_ga2905cddfa456fc846f0c8025487b404d"></a>

```c
#define BT_ISO_BN_MIN 0x01U
```

相关声明：[BT_ISO_BN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2905cddfa456fc846f0c8025487b404d)。

最小突发数量（Burst Number）：1。

<a id="r_gac05f4f51ea04962679f616bb167b724d"></a>

```c
#define BT_ISO_BN_MAX 0x0FU
```

相关声明：[BT_ISO_BN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac05f4f51ea04962679f616bb167b724d)。

最大突发数量（Burst Number）：15。

<a id="r_ga2d3bde6b34f6b15474926ed97ad11d98"></a>

```c
#define BT_ISO_FT_MIN 0x01U
```

相关声明：[BT_ISO_FT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2d3bde6b34f6b15474926ed97ad11d98)。

最小刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：1。

<a id="r_ga011c9d5840658fd0ef244f47893ec70e"></a>

```c
#define BT_ISO_FT_MAX 0xFFU
```

相关声明：[BT_ISO_FT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga011c9d5840658fd0ef244f47893ec70e)。

最大刷新超时（Flush Timeout），以等时间隔（ISO Interval）的倍数表示：255。

<a id="r_ga3eba4c20b4203b0323b14178522e6159"></a>

```c
#define BT_ISO_NSE_MIN 0x01U
```

相关声明：[BT_ISO_NSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3eba4c20b4203b0323b14178522e6159)。

最小子事件数量（Number of Subevents）：1。

<a id="r_gab7637d96bde7a41123b34f487eec3436"></a>

```c
#define BT_ISO_NSE_MAX 0x1FU
```

相关声明：[BT_ISO_NSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab7637d96bde7a41123b34f487eec3436)。

最大子事件数量（Number of Subevents）：31。

<a id="r_gaa1bd6484a248a6fb5abc31202e5076d4"></a>

```c
#define BT_ISO_SYNC_TIMEOUT_MIN 0x000A
```

相关声明：[BT_ISO_SYNC_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa1bd6484a248a6fb5abc31202e5076d4)。

最小广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 100 ms。

<a id="r_gaeb66806b649bf828afbd83d15c9823eb"></a>

```c
#define BT_ISO_SYNC_TIMEOUT_MAX 0x4000
```

相关声明：[BT_ISO_SYNC_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaeb66806b649bf828afbd83d15c9823eb)。

最大广播等时组同步超时（BIG Sync Timeout），以 10 ms 为单位表示，对应 163,840 ms。

<a id="r_ga47802144b8523b3d46af9ef97e744bbd"></a>

```c
#define BT_ISO_SYNC_MSE_ANY 0x00
```

相关声明：[BT_ISO_SYNC_MSE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga47802144b8523b3d46af9ef97e744bbd)。

由控制器决定的最大子事件计数值（Maximum Subevent Count）。

<a id="r_gafef299e43e0f58ac23e1a1e75ccd0163"></a>

```c
#define BT_ISO_SYNC_MSE_MIN 0x01
```

相关声明：[BT_ISO_SYNC_MSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafef299e43e0f58ac23e1a1e75ccd0163)。

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最小值：1。

<a id="r_gafd6e7b48394d6f6c8ddd485927b02b4b"></a>

```c
#define BT_ISO_SYNC_MSE_MAX 0x1F
```

相关声明：[BT_ISO_SYNC_MSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafd6e7b48394d6f6c8ddd485927b02b4b)。

广播等时组同步最大子事件计数（BIG Sync Maximum Subevent Count）的最大值：31。

<a id="r_ga39c034475b03f8b228916a27912d6724"></a>

```c
#define BT_ISO_CONNECTED_RTN_MIN 0x00
```

相关声明：[BT_ISO_CONNECTED_RTN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga39c034475b03f8b228916a27912d6724)。

连接等时重传值（Connected ISO Retransmission）的最小值：0。

<a id="r_ga1b52aba83eff5d6ae14169d1d3afa1a7"></a>

```c
#define BT_ISO_CONNECTED_RTN_MAX 0xFF
```

相关声明：[BT_ISO_CONNECTED_RTN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga1b52aba83eff5d6ae14169d1d3afa1a7)。

连接等时重传值（Connected ISO Retransmission）的最大值：255。

<a id="r_ga6297a9444ecab7aee170ef44ba21d744"></a>

```c
#define BT_ISO_BROADCAST_RTN_MIN 0x00
```

相关声明：[BT_ISO_BROADCAST_RTN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6297a9444ecab7aee170ef44ba21d744)。

广播等时重传值（Broadcast ISO Retransmission）的最小值：0。

<a id="r_ga3a579a5d752d4b19dcb668dd7ef27333"></a>

```c
#define BT_ISO_BROADCAST_RTN_MAX 0x1E
```

相关声明：[BT_ISO_BROADCAST_RTN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3a579a5d752d4b19dcb668dd7ef27333)。

广播等时重传值（Broadcast ISO Retransmission）的最大值：30。

<a id="r_ga5551cab9896764eec39b8e6102e561e5"></a>

```c
#define BT_ISO_BROADCAST_CODE_SIZE 0x10
```

相关声明：[BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)。

广播码（Broadcast Code）大小：16 八位组（Octets）。

<a id="r_ga0333b406b29a0a3c355db4f52815ff1a"></a>

```c
#define BT_ISO_BIS_INDEX_MIN 0x01
```

相关声明：[BT_ISO_BIS_INDEX_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0333b406b29a0a3c355db4f52815ff1a)。

广播等时流（BIS）的最低索引：1。

<a id="r_ga834652af6ceef1824799ab0bfa0e426f"></a>

```c
#define BT_ISO_BIS_INDEX_MAX 0x1F
```

相关声明：[BT_ISO_BIS_INDEX_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga834652af6ceef1824799ab0bfa0e426f)。

广播等时流（BIS）的最高索引：31。

<a id="r_ga52df7bd114b77872c084e28ca86e0b2e"></a>

```c
#define BT_ISO_IRC_MIN 0x01U
```

相关声明：[BT_ISO_IRC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga52df7bd114b77872c084e28ca86e0b2e)。

最小立即重复次数（Immediate Repetition Count）：1。

<a id="r_ga0f412f1593bcdcfa2b323b285bd508a4"></a>

```c
#define BT_ISO_IRC_MAX 0x0FU
```

相关声明：[BT_ISO_IRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0f412f1593bcdcfa2b323b285bd508a4)。

最大立即重复次数（Immediate Repetition Count）：15。

<a id="r_ga3f19aaa432290d67fdf4911d1d044dd8"></a>

```c
#define BT_ISO_PTO_MIN 0x00U
```

相关声明：[BT_ISO_PTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3f19aaa432290d67fdf4911d1d044dd8)。

最小预传输偏移（Pre-Transmission Offset）：0。

<a id="r_ga27e812e35a1f12329310851eb9c056f2"></a>

```c
#define BT_ISO_PTO_MAX 0x0FU
```

相关声明：[BT_ISO_PTO_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga27e812e35a1f12329310851eb9c056f2)。

最大预传输偏移（Pre-Transmission Offset）：15。

<a id="r_ga4fb7985aa35292671abe881c1570c445"></a>

```c
#define BT_ISO_SUBINTERVAL_NONE 0x00000000U
```

相关声明：[BT_ISO_SUBINTERVAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4fb7985aa35292671abe881c1570c445)。

无子间隔（No Subinterval）。

<a id="r_ga8085b01de2d1facb666215282690d674"></a>

```c
#define BT_ISO_SUBINTERVAL_UNKNOWN 0xFFFFFFFFU
```

相关声明：[BT_ISO_SUBINTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8085b01de2d1facb666215282690d674)。

未知子间隔（Unknown Subinterval）。

<a id="r_gab3e9a2596b11d372edef3f356008c1b4"></a>

```c
#define BT_ISO_SUBINTERVAL_MIN 0x00000190U
```

相关声明：[BT_ISO_SUBINTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab3e9a2596b11d372edef3f356008c1b4)。

最小子间隔（Subinterval），单位为微秒：400 µs。

<a id="r_gace8679596f279f31c66e206909de47d9"></a>

```c
#define BT_ISO_SUBINTERVAL_MAX 0x00009C3FU
```

相关声明：[BT_ISO_SUBINTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gace8679596f279f31c66e206909de47d9)。

最大子间隔（Subinterval），单位为微秒：3,999,999 µs。

<a id="r_ga9becee6d629b8f54f55d2264b6d1baef"></a>

```c
#define BT_ISO_VALID_BIS_BITFIELD(_bis_bitfield)
```

相关声明：[BT_ISO_VALID_BIS_BITFIELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga9becee6d629b8f54f55d2264b6d1baef)。

检查广播等时流位字段（ISO BIS Bitfield）是否有效：`BT_ISO_BIS_INDEX_BIT(1)|..|BT_ISO_BIS_INDEX_BIT(31)`。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_gaf2925460cc22cc4220dc376bcbee6201"></a>

```c
enum bt_iso_state { BT_ISO_STATE_DISCONNECTED , BT_ISO_STATE_CONNECTING , BT_ISO_STATE_CONNECTED , BT_ISO_STATE_DISCONNECTING }
```

相关声明：[bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)、[BT_ISO_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d)、[BT_ISO_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22)、[BT_ISO_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d)、[BT_ISO_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)。

等时通道（ISO Channel）的生命周期状态（Life-Span States）。

<a id="r_gafcbd720c67c6a6e5f1cae1395e1e06f0"></a>

```c
enum bt_iso_chan_type { BT_ISO_CHAN_TYPE_NONE , BT_ISO_CHAN_TYPE_CENTRAL , BT_ISO_CHAN_TYPE_PERIPHERAL , BT_ISO_CHAN_TYPE_BROADCASTER , BT_ISO_CHAN_TYPE_SYNC_RECEIVER }
```

相关声明：[bt_iso_chan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafcbd720c67c6a6e5f1cae1395e1e06f0)、[BT_ISO_CHAN_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17)、[BT_ISO_CHAN_TYPE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)、[BT_ISO_CHAN_TYPE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)、[BT_ISO_CHAN_TYPE_BROADCASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)、[BT_ISO_CHAN_TYPE_SYNC_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)。

等时通道类型（ISO Channel Type）。

<a id="r_ga2c62af103a71aa8f5f8aa103b1245866"></a>

```c
enum { BT_ISO_FLAGS_VALID = (1UL << (0)) , BT_ISO_FLAGS_ERROR = (1UL << (1)) , BT_ISO_FLAGS_LOST = (1UL << (2)) , BT_ISO_FLAGS_TS = (1UL << (3)) }
```

相关声明：[BT_ISO_FLAGS_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382)、[BT_ISO_FLAGS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218)、[BT_ISO_FLAGS_LOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff)、[BT_ISO_FLAGS_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)。

等时分组状态标志位（ISO Packet Status Flag Bits）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gaa3407502145a77e08993220f7ce51b4a"></a>

```c
struct bt_iso_chan * bt_iso_get_chan_by_conn (const struct bt_conn *iso)
```

相关声明：[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_get_chan_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3407502145a77e08993220f7ce51b4a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

通过 `bt_iso_chan::iso` 引用查找 `bt_iso_chan` 对象。

<a id="r_gaff0e52777b2140519c63b54b9618bca8"></a>

```c
int bt_iso_server_register (struct bt_iso_server *server)
```

相关声明：[bt_iso_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaff0e52777b2140519c63b54b9618bca8)、[bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)。

注册等时服务器（ISO Server）。

<a id="r_ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6"></a>

```c
int bt_iso_server_unregister (struct bt_iso_server *server)
```

相关声明：[bt_iso_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)、[bt_iso_server](../bluetooth_connection_model_reference/P087_bt_iso_server_结构体.md)。

注销等时服务器（ISO Server）。

<a id="r_gaea03fc251206f18de320506064c1631f"></a>

```c
int bt_iso_cig_create (const struct bt_iso_cig_param *param, struct bt_iso_cig **out_cig)
```

相关声明：[bt_iso_cig_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaea03fc251206f18de320506064c1631f)、[bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)。

以中央设备（Central）身份创建连接等时组（CIG）。

<a id="r_ga98f557c183a82066b81f0265c225bebe"></a>

```c
int bt_iso_cig_reconfigure (struct bt_iso_cig *cig, const struct bt_iso_cig_param *param)
```

相关声明：[bt_iso_cig_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98f557c183a82066b81f0265c225bebe)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)、[bt_iso_cig_param](../bluetooth_connection_model_reference/P083_bt_iso_cig_param_结构体.md)。

以中央设备（Central）身份重新配置连接等时组（CIG）。

<a id="r_gad4b6a7286593ff099117113b6ca996f8"></a>

```c
int bt_iso_cig_terminate (struct bt_iso_cig *cig)
```

相关声明：[bt_iso_cig_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad4b6a7286593ff099117113b6ca996f8)、[bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)。

以中央设备（Central）身份终止连接等时组（CIG）。

<a id="r_ga98953a261f3699b62cd19ab4977e0b4c"></a>

```c
int bt_iso_chan_connect (const struct bt_iso_connect_param *param, size_t count)
```

相关声明：[bt_iso_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98953a261f3699b62cd19ab4977e0b4c)、[bt_iso_connect_param](../bluetooth_connection_model_reference/P084_bt_iso_connect_param_结构体.md)。

在 ACL 连接上连接等时通道（ISO Channels）。

<a id="r_ga94c5c788b099284219e5a303b4b8ea69"></a>

```c
int bt_iso_chan_disconnect (struct bt_iso_chan *chan)
```

相关声明：[bt_iso_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga94c5c788b099284219e5a303b4b8ea69)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)。

断开已连接的等时通道（ISO Channel）。

<a id="r_ga0dbb89a133011a833be7d18161471c6a"></a>

```c
int bt_iso_chan_send (struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num)
```

相关声明：[bt_iso_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0dbb89a133011a833be7d18161471c6a)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向等时通道（ISO Channel）发送不带时间戳（Timestamp）的数据。

<a id="r_gab75b817770e3b685920587afde39d6cd"></a>

```c
int bt_iso_chan_send_ts (struct bt_iso_chan *chan, struct net_buf *buf, uint16_t seq_num, uint32_t ts)
```

相关声明：[bt_iso_chan_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab75b817770e3b685920587afde39d6cd)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向等时通道（ISO Channel）发送带时间戳（Timestamp）的数据。

<a id="r_gaa74c762451cfb5d04ffcd8d396a75447"></a>

```c
int bt_iso_setup_data_path (const struct bt_iso_chan *chan, uint8_t dir, const struct bt_iso_chan_path *path)
```

相关声明：[bt_iso_setup_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa74c762451cfb5d04ffcd8d396a75447)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_iso_chan_path](../bluetooth_connection_model_reference/P080_bt_iso_chan_path_结构体.md)。

为等时通道（ISO Channel）建立等时数据路径（ISO Data Path）。

<a id="r_ga53be464e005392676830feeddd8cdc22"></a>

```c
int bt_iso_remove_data_path (const struct bt_iso_chan *chan, uint8_t dir)
```

相关声明：[bt_iso_remove_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga53be464e005392676830feeddd8cdc22)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

移除等时通道（ISO Channel）的等时数据路径（ISO Data Path）。

<a id="r_ga75e58ed5bfa48f84000f1ce974d649c6"></a>

```c
int bt_iso_chan_get_info (const struct bt_iso_chan *chan, struct bt_iso_info *info)
```

相关声明：[bt_iso_chan_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga75e58ed5bfa48f84000f1ce974d649c6)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_info](../bluetooth_connection_model_reference/P085_bt_iso_info_结构体.md)。

获取等时通道信息（ISO Channel Info）。

<a id="r_gaa3942147fdeebc36039cc35c4e984411"></a>

```c
int bt_iso_chan_get_tx_sync (const struct bt_iso_chan *chan, struct bt_iso_tx_info *info)
```

相关声明：[bt_iso_chan_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3942147fdeebc36039cc35c4e984411)、[bt_iso_chan](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md)、[bt_iso_tx_info](../bluetooth_connection_model_reference/P089_bt_iso_tx_info_结构体.md)。

获取等时传输定时信息（ISO Transmission Timing Info）。

<a id="r_ga8a01a56e4a4555ed65a67065facfca76"></a>

```c
int bt_iso_big_register_cb (struct bt_iso_big_cb *cb)
```

相关声明：[bt_iso_big_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8a01a56e4a4555ed65a67065facfca76)、[bt_iso_big_cb](../bluetooth_connection_model_reference/P072_bt_iso_big_cb_结构体.md)。

注册广播源（Broadcast Sources）的回调。

<a id="r_gac9937316382d257493c7d0359f1341f5"></a>

```c
int bt_iso_big_create (struct bt_le_ext_adv *padv, struct bt_iso_big_create_param *param, struct bt_iso_big **out_big)
```

相关声明：[bt_iso_big_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac9937316382d257493c7d0359f1341f5)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_iso_big_create_param](../bluetooth_connection_model_reference/P073_bt_iso_big_create_param_结构体.md)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以广播者（Broadcaster）身份创建广播等时组（BIG）。

<a id="r_gab9c06a86bf5cc023f5f9bd16c5d3265b"></a>

```c
int bt_iso_big_terminate (struct bt_iso_big *big)
```

相关声明：[bt_iso_big_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab9c06a86bf5cc023f5f9bd16c5d3265b)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以广播者（Broadcaster）或接收者（Receiver）身份终止广播等时组（BIG）。

<a id="r_ga790cfeb8516020f317802e019dca4754"></a>

```c
int bt_iso_big_sync (struct bt_le_per_adv_sync *sync, struct bt_iso_big_sync_param *param, struct bt_iso_big **out_big)
```

相关声明：[bt_iso_big_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga790cfeb8516020f317802e019dca4754)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_iso_big_sync_param](../bluetooth_connection_model_reference/P074_bt_iso_big_sync_param_结构体.md)、[bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)。

以接收者（Receiver）身份创建广播等时组（BIG）。

<a id="r_ga4d4c9b8d6d83abcc8d3b337101922800"></a>

```c
const char * bt_iso_chan_state_str (enum bt_iso_state state)
```

相关声明：[bt_iso_chan_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4d4c9b8d6d83abcc8d3b337101922800)、[bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

返回等时通道状态（ISO Channel State）的字符串表示。


## 6.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/buf.h](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/hci.h](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P415_iso.h_源码浏览.md)
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
- [BT_ISO_CHAN_SEND_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga15c9cafd39e89f07eef115e147741098)
- [BT_BUF_ISO_SIZE](../api_buffer_paging_topic_reference/P002_数据缓冲区（Data buffers）.md#gaa820dee05a7202304e1aaa9a36386ca4)
- [BT_ISO_SDU_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3c0af738d118341da7d370aaa48a89d1)
- [BT_ISO_BIS_INDEX_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga01b975b441fa5d8f039562ab66857bbf)
- [BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)
- [BT_ISO_SDU_INTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4f0cc6262171fbee9d0ef173123b8f3d)
- [BT_ISO_DATA_PATH_VS_ID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga9f26e30d05e571d3fc33dec8ae693e45)
- [BT_ISO_DATA_PATH_VS_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae5e1f7c86165b26fc6d93bc922676f9a)
- [BT_ISO_CONTROLLER_DELAY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga29bf2b36a4ab4e1325f626bbcf52a9a6)
- [BT_ISO_CONTROLLER_DELAY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae6ba7c8ea447112bcd7798d0351a9a91)
- [BT_ISO_SDU_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8122de88b6e5423dca653b1f0a484316)
- [BT_ISO_SDU_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga077eb6d219bba947d363e2cce8e0080c)
- [BT_ISO_ISO_INTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)
- [BT_ISO_ISO_INTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gabc381a7f565061ec91d23b7783521da3)
- [BT_ISO_LATENCY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga77ae350543eb05617c590c0ad9cb0048)
- [BT_ISO_LATENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad5e89d05d8706509d8d9d8dac40e3347)
- [BT_ISO_PACKING_SEQUENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6275e8d805e2366522a78f18ca47ac19)
- [BT_ISO_PACKING_INTERLEAVED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga35b037fcce858857642b4c54bae8dd79)
- [BT_ISO_FRAMING_UNFRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga696a81180ae25aa686a53b73e352c9d2)
- [BT_ISO_FRAMING_FRAMED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8f9aba389529ad2a3667ca378e99de2b)
- [BT_ISO_MAX_GROUP_ISO_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae9dc30b300e2c309d646e3227e8cc00e)
- [BT_ISO_MIN_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4cc5565eeda9a3661d49d485637d1db2)
- [BT_ISO_MAX_SDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa5d5588e7229db16219b0c44921bbcf7)
- [BT_ISO_CONNECTED_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4e29d5966f959114754d62a8763c8c1e)
- [BT_ISO_BROADCAST_PDU_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaee766ff789f1bf01f75c88112ddd2afa)
- [BT_ISO_PDU_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga88fb5690cd1cab4e5e8d5c025cc1af00)
- [BT_ISO_BN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2905cddfa456fc846f0c8025487b404d)
- [BT_ISO_BN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac05f4f51ea04962679f616bb167b724d)
- [BT_ISO_FT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga2d3bde6b34f6b15474926ed97ad11d98)
- [BT_ISO_FT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga011c9d5840658fd0ef244f47893ec70e)
- [BT_ISO_NSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3eba4c20b4203b0323b14178522e6159)
- [BT_ISO_NSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab7637d96bde7a41123b34f487eec3436)
- [BT_ISO_SYNC_TIMEOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa1bd6484a248a6fb5abc31202e5076d4)
- [BT_ISO_SYNC_TIMEOUT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaeb66806b649bf828afbd83d15c9823eb)
- [BT_ISO_SYNC_MSE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga47802144b8523b3d46af9ef97e744bbd)
- [BT_ISO_SYNC_MSE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafef299e43e0f58ac23e1a1e75ccd0163)
- [BT_ISO_SYNC_MSE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafd6e7b48394d6f6c8ddd485927b02b4b)
- [BT_ISO_CONNECTED_RTN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga39c034475b03f8b228916a27912d6724)
- [BT_ISO_CONNECTED_RTN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga1b52aba83eff5d6ae14169d1d3afa1a7)
- [BT_ISO_BROADCAST_RTN_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga6297a9444ecab7aee170ef44ba21d744)
- [BT_ISO_BROADCAST_RTN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3a579a5d752d4b19dcb668dd7ef27333)
- [BT_ISO_BROADCAST_CODE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga5551cab9896764eec39b8e6102e561e5)
- [BT_ISO_BIS_INDEX_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0333b406b29a0a3c355db4f52815ff1a)
- [BT_ISO_BIS_INDEX_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga834652af6ceef1824799ab0bfa0e426f)
- [BT_ISO_IRC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga52df7bd114b77872c084e28ca86e0b2e)
- [BT_ISO_IRC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0f412f1593bcdcfa2b323b285bd508a4)
- [BT_ISO_PTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga3f19aaa432290d67fdf4911d1d044dd8)
- [BT_ISO_PTO_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga27e812e35a1f12329310851eb9c056f2)
- [BT_ISO_SUBINTERVAL_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4fb7985aa35292671abe881c1570c445)
- [BT_ISO_SUBINTERVAL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8085b01de2d1facb666215282690d674)
- [BT_ISO_SUBINTERVAL_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab3e9a2596b11d372edef3f356008c1b4)
- [BT_ISO_SUBINTERVAL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gace8679596f279f31c66e206909de47d9)
- [BT_ISO_VALID_BIS_BITFIELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga9becee6d629b8f54f55d2264b6d1baef)
- [bt_iso_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaf2925460cc22cc4220dc376bcbee6201)
- [BT_ISO_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d)
- [BT_ISO_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22)
- [BT_ISO_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d)
- [BT_ISO_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)
- [bt_iso_chan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafcbd720c67c6a6e5f1cae1395e1e06f0)
- [BT_ISO_CHAN_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17)
- [BT_ISO_CHAN_TYPE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)
- [BT_ISO_CHAN_TYPE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)
- [BT_ISO_CHAN_TYPE_BROADCASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)
- [BT_ISO_CHAN_TYPE_SYNC_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)
- [BT_ISO_FLAGS_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382)
- [BT_ISO_FLAGS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218)
- [BT_ISO_FLAGS_LOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff)
- [BT_ISO_FLAGS_TS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)
- [bt_iso_get_chan_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3407502145a77e08993220f7ce51b4a)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_iso_chan::iso](../bluetooth_connection_model_reference/P077_bt_iso_chan_结构体.md#a7fd728385a3aec11be8883bdee8aedea)
- [bt_iso_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaff0e52777b2140519c63b54b9618bca8)
- [bt_iso_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)
- [bt_iso_cig_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaea03fc251206f18de320506064c1631f)
- [bt_iso_cig](../bluetooth_connection_model_reference/P082_bt_iso_cig_结构体.md)
- [bt_iso_cig_reconfigure](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98f557c183a82066b81f0265c225bebe)
- [bt_iso_cig_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gad4b6a7286593ff099117113b6ca996f8)
- [bt_iso_chan_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga98953a261f3699b62cd19ab4977e0b4c)
- [bt_iso_chan_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga94c5c788b099284219e5a303b4b8ea69)
- [bt_iso_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga0dbb89a133011a833be7d18161471c6a)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_iso_chan_send_ts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab75b817770e3b685920587afde39d6cd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_iso_setup_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa74c762451cfb5d04ffcd8d396a75447)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_iso_remove_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga53be464e005392676830feeddd8cdc22)
- [bt_iso_chan_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga75e58ed5bfa48f84000f1ce974d649c6)
- [bt_iso_chan_get_tx_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gaa3942147fdeebc36039cc35c4e984411)
- [bt_iso_big_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga8a01a56e4a4555ed65a67065facfca76)
- [bt_iso_big_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gac9937316382d257493c7d0359f1341f5)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_iso_big](../bluetooth_connection_model_reference/P071_bt_iso_big_结构体.md)
- [bt_iso_big_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gab9c06a86bf5cc023f5f9bd16c5d3265b)
- [bt_iso_big_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga790cfeb8516020f317802e019dca4754)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_iso_chan_state_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga4d4c9b8d6d83abcc8d3b337101922800)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="header-details"></a>

---

[上一章](P005_zephyr__bluetooth__hci_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__sensor__lsm9ds1.h_文件参考.md)
