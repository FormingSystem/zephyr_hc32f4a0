---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-8
title: RFCOMM API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_RFCOMM API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFCOMM

<a id="details"></a>

RFCOMM。引入版本（Since）：1.6；API 版本（Version）：0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_bt_5Frfcomm_5Fdlc_5Fops"></a>

```c
struct bt_rfcomm_dlc_ops
```

相关声明：[bt_rfcomm_dlc_ops](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md)。

RFCOMM数据链路连接（DLC）的操作结构。

<a id="r_bt_5Frfcomm_5Fdlc"></a>

```c
struct bt_rfcomm_dlc
```

相关声明：[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)。

RFCOMM数据链路连接（DLC）结构。

<a id="r_bt_5Frfcomm_5Fserver"></a>

```c
struct bt_rfcomm_server
```

相关声明：[bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)。

<a id="r_bt_5Frfcomm_5Frpn"></a>

```c
struct bt_rfcomm_rpn
```

相关声明：[bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)。

RFCOMM远程端口协商（Remote Port Negotiation，RPN）结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_ga8d7b15c80fc69a25b105aadf6f3a6a6d"></a>

```c
#define BT_RFCOMM_HDR_MAX_SIZE 4
```

相关声明：[BT_RFCOMM_HDR_MAX_SIZE](#ga8d7b15c80fc69a25b105aadf6f3a6a6d)。

RFCOMM 最大头部大小（Maximum Header Size）。

<a id="r_gaea26fe8eac8c5792a4cb78404dc4f7c1"></a>

```c
#define BT_RFCOMM_FCS_SIZE 1
```

相关声明：[BT_RFCOMM_FCS_SIZE](#gaea26fe8eac8c5792a4cb78404dc4f7c1)。

RFCOMM 帧校验序列大小（FCS Size）。

<a id="r_ga90af70151ba4581d74422c9c79bee320"></a>

```c
#define BT_RFCOMM_CREDITS_SIZE 1
```

相关声明：[BT_RFCOMM_CREDITS_SIZE](#ga90af70151ba4581d74422c9c79bee320)。

RFCOMM 信用值字段大小（Credits Size）。

<a id="r_ga99d36ccceccf03b011fbee0690d6565c"></a>

```c
#define BT_RFCOMM_OVERHEAD_SIZE (BT_RFCOMM_HDR_MAX_SIZE + BT_RFCOMM_FCS_SIZE + BT_RFCOMM_CREDITS_SIZE)
```

相关声明：[BT_RFCOMM_OVERHEAD_SIZE](#ga99d36ccceccf03b011fbee0690d6565c)、[BT_RFCOMM_HDR_MAX_SIZE](#ga8d7b15c80fc69a25b105aadf6f3a6a6d)、[BT_RFCOMM_FCS_SIZE](#gaea26fe8eac8c5792a4cb78404dc4f7c1)、[BT_RFCOMM_CREDITS_SIZE](#ga90af70151ba4581d74422c9c79bee320)。

RFCOMM 协议开销大小（Overhead Size）。

<a id="r_gabb568d7f32dbd0720f203538e3aa345c"></a>

```c
#define BT_RFCOMM_BUF_SIZE(mtu)
```

相关声明：[BT_RFCOMM_BUF_SIZE](#gabb568d7f32dbd0720f203538e3aa345c)。

计算 RFCOMM 协议数据单元（PDU）所需缓冲区大小的辅助接口。

<a id="r_gacbb625b129afb33fceafe5ddf61c839a"></a>

```c
#define BT_RFCOMM_SET_LINE_SETTINGS(data, stop, parity)
```

相关声明：[BT_RFCOMM_SET_LINE_SETTINGS](#gacbb625b129afb33fceafe5ddf61c839a)。

将数据位（Data Bits）、停止位（Stop Bits）与奇偶校验（Parity）合并为单个线路设置字节（Line Settings Byte）。

<a id="r_gaef902e774d1a6279a117968a32cc5878"></a>

```c
#define BT_RFCOMM_RPN_FLOW_NONE 0x00
```

相关声明：[BT_RFCOMM_RPN_FLOW_NONE](#gaef902e774d1a6279a117968a32cc5878)。

<a id="r_ga90ab80687e32da0f8164292cd63b0623"></a>

```c
#define BT_RFCOMM_RPN_XON_CHAR 0x11
```

相关声明：[BT_RFCOMM_RPN_XON_CHAR](#ga90ab80687e32da0f8164292cd63b0623)。

<a id="r_gacdca9e597689b3de20b1df3616ad523c"></a>

```c
#define BT_RFCOMM_RPN_XOFF_CHAR 0x13
```

相关声明：[BT_RFCOMM_RPN_XOFF_CHAR](#gacdca9e597689b3de20b1df3616ad523c)。

<a id="r_ga71099379ed90d3d6ce9d4c1eed3be827"></a>

```c
#define BT_RFCOMM_RPN_PARAM_MASK_ALL 0x3f7f
```

相关声明：[BT_RFCOMM_RPN_PARAM_MASK_ALL](#ga71099379ed90d3d6ce9d4c1eed3be827)。

<a id="r_gad98eed7203cbf79f2b97ba695af1ae06"></a>

```c
#define BT_RFCOMM_RLS_NO_ERR (0x00U)
```

相关声明：[BT_RFCOMM_RLS_NO_ERR](#gad98eed7203cbf79f2b97ba695af1ae06)。

远端线路状态（Remote Line Status）值：无错误。

<a id="r_ga4e3f4fdb6841de8796f7598055cca1ae"></a>

```c
#define BT_RFCOMM_RLS_ERR(err)
```

相关声明：[BT_RFCOMM_RLS_ERR](#ga4e3f4fdb6841de8796f7598055cca1ae)。

远端线路状态（Remote Line Status）值：发生错误。

<a id="r_ga14064eb94c14aa984eb36cf8a9656ba9"></a>

```c
#define BT_RFCOMM_RLS_ERR_OVERRUN_ERROR BIT(1)
```

相关声明：[BT_RFCOMM_RLS_ERR_OVERRUN_ERROR](#ga14064eb94c14aa984eb36cf8a9656ba9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

溢出错误（Overrun Error）：接收的字符覆盖了尚未读取的字符。

<a id="r_ga551b453e00b81289f239335d07bc62f2"></a>

```c
#define BT_RFCOMM_RLS_ERR_PARITY_ERROR BIT(2)
```

相关声明：[BT_RFCOMM_RLS_ERR_PARITY_ERROR](#ga551b453e00b81289f239335d07bc62f2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

奇偶校验错误（Parity Error）：接收字符的奇偶校验不正确。

<a id="r_gad4b245fdc58379a9617200921f29dd77"></a>

```c
#define BT_RFCOMM_RLS_ERR_FRAMING_ERROR BIT(3)
```

相关声明：[BT_RFCOMM_RLS_ERR_FRAMING_ERROR](#gad4b245fdc58379a9617200921f29dd77)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧格式错误（Framing Error）：字符未以停止位结束。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga11f290d34ad631afaa10caf2cefd72b9"></a>

```c
typedef enum bt_rfcomm_role bt_rfcomm_role_t
```

相关声明：[bt_rfcomm_role](#gaa70d7971435dc7e6421372d7385811b2)、[bt_rfcomm_role_t](#ga11f290d34ad631afaa10caf2cefd72b9)。

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_gafccaaeb8f4d4f3e3834f358ccfdfb86b"></a>

```c
enum { BT_RFCOMM_CHAN_HFP_HF = 1 , BT_RFCOMM_CHAN_HFP_AG , BT_RFCOMM_CHAN_HSP_AG , BT_RFCOMM_CHAN_HSP_HS , BT_RFCOMM_CHAN_SPP , BT_RFCOMM_CHAN_DYNAMIC_START }
```

相关声明：[BT_RFCOMM_CHAN_HFP_HF](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4)、[BT_RFCOMM_CHAN_HFP_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd)、[BT_RFCOMM_CHAN_HSP_AG](#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b)、[BT_RFCOMM_CHAN_HSP_HS](#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25)、[BT_RFCOMM_CHAN_SPP](#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)、[BT_RFCOMM_CHAN_DYNAMIC_START](#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)。

<a id="r_gaa70d7971435dc7e6421372d7385811b2"></a>

```c
enum bt_rfcomm_role { BT_RFCOMM_ROLE_ACCEPTOR , BT_RFCOMM_ROLE_INITIATOR }
```

相关声明：[bt_rfcomm_role](#gaa70d7971435dc7e6421372d7385811b2)、[BT_RFCOMM_ROLE_ACCEPTOR](#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)、[BT_RFCOMM_ROLE_INITIATOR](#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)。

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

<a id="r_ga61637d261987529c219dcd1179ed1711"></a>

```c
enum { BT_RFCOMM_RPN_BAUD_RATE_2400 = 0x0 , BT_RFCOMM_RPN_BAUD_RATE_4800 = 0x1 , BT_RFCOMM_RPN_BAUD_RATE_7200 = 0x2 , BT_RFCOMM_RPN_BAUD_RATE_9600 = 0x3 , BT_RFCOMM_RPN_BAUD_RATE_19200 = 0x4 , BT_RFCOMM_RPN_BAUD_RATE_38400 = 0x5 , BT_RFCOMM_RPN_BAUD_RATE_57600 = 0x6 , BT_RFCOMM_RPN_BAUD_RATE_115200 = 0x7 , BT_RFCOMM_RPN_BAUD_RATE_230400 = 0x8 }
```

相关声明：[BT_RFCOMM_RPN_BAUD_RATE_2400](#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3)、[BT_RFCOMM_RPN_BAUD_RATE_4800](#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60)、[BT_RFCOMM_RPN_BAUD_RATE_7200](#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593)、[BT_RFCOMM_RPN_BAUD_RATE_9600](#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9)、[BT_RFCOMM_RPN_BAUD_RATE_19200](#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c)、[BT_RFCOMM_RPN_BAUD_RATE_38400](#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5)、[BT_RFCOMM_RPN_BAUD_RATE_57600](#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048)、[BT_RFCOMM_RPN_BAUD_RATE_115200](#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33)、[BT_RFCOMM_RPN_BAUD_RATE_230400](#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760)。

RFCOMM 远端端口协商（RPN）的波特率值（Baud Rate Values）。

<a id="r_ga15600feb01d876e319e1d5f93991592b"></a>

```c
enum { BT_RFCOMM_RPN_DATA_BITS_5 = 0x0 , BT_RFCOMM_RPN_DATA_BITS_6 = 0x1 , BT_RFCOMM_RPN_DATA_BITS_7 = 0x2 , BT_RFCOMM_RPN_DATA_BITS_8 = 0x3 }
```

相关声明：[BT_RFCOMM_RPN_DATA_BITS_5](#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1)、[BT_RFCOMM_RPN_DATA_BITS_6](#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc)、[BT_RFCOMM_RPN_DATA_BITS_7](#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867)、[BT_RFCOMM_RPN_DATA_BITS_8](#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83)。

RFCOMM 远端端口协商（RPN）的数据位值（Data Bit Values）。

<a id="r_gabe97ddd372c3b0b44a9b78539ddf9ffc"></a>

```c
enum { BT_RFCOMM_RPN_STOP_BITS_1 = 0 , BT_RFCOMM_RPN_STOP_BITS_1_5 = 1 }
```

相关声明：[BT_RFCOMM_RPN_STOP_BITS_1](#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339)、[BT_RFCOMM_RPN_STOP_BITS_1_5](#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6)。

RFCOMM 远端端口协商（RPN）的停止位值（Stop Bit Values）。

<a id="r_gad1794db284f7b39f4816f04f21ed3f4b"></a>

```c
enum { BT_RFCOMM_RPN_PARITY_NONE = 0x0 , BT_RFCOMM_RPN_PARITY_ODD = 0x1 , BT_RFCOMM_RPN_PARITY_EVEN = 0x3 , BT_RFCOMM_RPN_PARITY_MARK = 0x5 , BT_RFCOMM_RPN_PARITY_SPACE = 0x7 }
```

相关声明：[BT_RFCOMM_RPN_PARITY_NONE](#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b)、[BT_RFCOMM_RPN_PARITY_ODD](#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169)、[BT_RFCOMM_RPN_PARITY_EVEN](#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18)、[BT_RFCOMM_RPN_PARITY_MARK](#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9)、[BT_RFCOMM_RPN_PARITY_SPACE](#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1)。

RFCOMM 远端端口协商（RPN）的奇偶校验位值（Parity Bit Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_gafd0ffcff41e233f74dc2726e889f5401"></a>

```c
int bt_rfcomm_server_register (struct bt_rfcomm_server *server)
```

相关声明：[bt_rfcomm_server_register](#gafd0ffcff41e233f74dc2726e889f5401)、[bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)。

注册 RFCOMM 服务器（Server）。

<a id="r_gaf6bb5c563ba32fa76fc774271d958fe4"></a>

```c
int bt_rfcomm_server_unregister (struct bt_rfcomm_server *server)
```

相关声明：[bt_rfcomm_server_unregister](#gaf6bb5c563ba32fa76fc774271d958fe4)、[bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)。

注销 RFCOMM 服务器（Server）。

<a id="r_ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7"></a>

```c
int bt_rfcomm_dlc_connect (struct bt_conn *conn, struct bt_rfcomm_dlc *dlc, uint8_t channel)
```

相关声明：[bt_rfcomm_dlc_connect](#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

连接 RFCOMM 通道（Channel）。

<a id="r_ga593841aef52027598977b7b2bbd0237d"></a>

```c
int bt_rfcomm_dlc_send (struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

相关声明：[bt_rfcomm_dlc_send](#ga593841aef52027598977b7b2bbd0237d)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 RFCOMM 发送数据。

<a id="r_ga998328b021ec53f7e291ab76856ffa18"></a>

```c
int bt_rfcomm_dlc_disconnect (struct bt_rfcomm_dlc *dlc)
```

相关声明：[bt_rfcomm_dlc_disconnect](#ga998328b021ec53f7e291ab76856ffa18)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)。

断开 RFCOMM 数据链路连接（DLC）。

<a id="r_ga2ce765351798976136c3096a9a7f9465"></a>

```c
int bt_rfcomm_dlc_recv_complete (struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

相关声明：[bt_rfcomm_dlc_recv_complete](#ga2ce765351798976136c3096a9a7f9465)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

完成 RFCOMM 通道数据的接收。

<a id="r_gaed05e67dc975d94e1209372d5817077a"></a>

```c
struct net_buf * bt_rfcomm_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_rfcomm_create_pdu](#gaed05e67dc975d94e1209372d5817077a)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 RFCOMM、L2CAP 和 ACL 头部预留头部空间（Headroom）后，从池中分配缓冲区。

<a id="r_gab38378db71d7f4631e47742ce4a5c59d"></a>

```c
int bt_rfcomm_send_rpn_cmd (struct bt_rfcomm_dlc *dlc, struct bt_rfcomm_rpn *rpn)
```

相关声明：[bt_rfcomm_send_rpn_cmd](#gab38378db71d7f4631e47742ce4a5c59d)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)。

发送远端端口协商命令（Remote Port Negotiation Command）。

<a id="r_ga1a46f58b41dab9a81b8d2b88f0f22547"></a>

```c
int bt_rfcomm_send_rls_cmd (struct bt_rfcomm_dlc *dlc, uint8_t line_status)
```

相关声明：[bt_rfcomm_send_rls_cmd](#ga1a46f58b41dab9a81b8d2b88f0f22547)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送远端线路状态命令（Remote Line Status Command）。

## 8.6\_详细说明（Detailed Documentation）

<a id="gabb568d7f32dbd0720f203538e3aa345c"></a>

### `BT_RFCOMM_BUF_SIZE`

```c
#define BT_RFCOMM_BUF_SIZE ( mtu)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

展开值（Value）：

```c
BT_L2CAP_BUF_SIZE(BT_RFCOMM_OVERHEAD_SIZE + (mtu))
```

计算 RFCOMM 协议数据单元（PDU）所需缓冲区大小的辅助接口。

可用于创建缓冲池（Buffer Pools）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mtu` | 所需 RFCOMM PDU 最大传输单元（MTU）。 |

**返回（Returns）**：返回值（Returns）：满足所请求 RFCOMM PDU MTU 的缓冲区大小。

<a id="ga90af70151ba4581d74422c9c79bee320"></a>

### `BT_RFCOMM_CREDITS_SIZE`

```c
#define BT_RFCOMM_CREDITS_SIZE 1
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 信用值字段大小（Credits Size）。

<a id="gaea26fe8eac8c5792a4cb78404dc4f7c1"></a>

### `BT_RFCOMM_FCS_SIZE`

```c
#define BT_RFCOMM_FCS_SIZE 1
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 帧校验序列大小（FCS Size）。

<a id="ga8d7b15c80fc69a25b105aadf6f3a6a6d"></a>

### `BT_RFCOMM_HDR_MAX_SIZE`

```c
#define BT_RFCOMM_HDR_MAX_SIZE 4
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 最大头部大小（Maximum Header Size）。

长度可能为 2 字节，取决于信息长度（Information Length）。

<a id="ga99d36ccceccf03b011fbee0690d6565c"></a>

### `BT_RFCOMM_OVERHEAD_SIZE`

```c
#define BT_RFCOMM_OVERHEAD_SIZE (BT_RFCOMM_HDR_MAX_SIZE + BT_RFCOMM_FCS_SIZE + BT_RFCOMM_CREDITS_SIZE)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 协议开销大小（Overhead Size）。

RFCOMM 开销大小（Overhead Size）包括最大头部大小、帧校验序列（FCS）大小及信用字段大小（Credits Size）。

支持基于信用的流量控制（CFC）时，信用字段占用的空间应从最大帧大小中扣除，避免包含信用字段后 SDU 长度超过最大帧大小。

<a id="ga4e3f4fdb6841de8796f7598055cca1ae"></a>

### `BT_RFCOMM_RLS_ERR`

```c
#define BT_RFCOMM_RLS_ERR ( err)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

展开值（Value）：

```c
(BIT(0) | (err))
```

远端线路状态（Remote Line Status）值：发生错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 要设置到远端线路状态（RLS）值中的错误码，必须为 BT_RFCOMM_RLS_ERR_OVERRUN_ERROR、BT_RFCOMM_RLS_ERR_PARITY_ERROR 或 BT_RFCOMM_RLS_ERR_FRAMING_ERROR 之一。 |

**返回（Returns）**：返回值（Returns）：已设置错误码的 RLS 值。

<a id="gad4b245fdc58379a9617200921f29dd77"></a>

### `BT_RFCOMM_RLS_ERR_FRAMING_ERROR`

```c
#define BT_RFCOMM_RLS_ERR_FRAMING_ERROR BIT(3)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

帧格式错误（Framing Error）：字符未以停止位结束。

<a id="ga14064eb94c14aa984eb36cf8a9656ba9"></a>

### `BT_RFCOMM_RLS_ERR_OVERRUN_ERROR`

```c
#define BT_RFCOMM_RLS_ERR_OVERRUN_ERROR BIT(1)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

溢出错误（Overrun Error）：接收的字符覆盖了尚未读取的字符。

<a id="ga551b453e00b81289f239335d07bc62f2"></a>

### `BT_RFCOMM_RLS_ERR_PARITY_ERROR`

```c
#define BT_RFCOMM_RLS_ERR_PARITY_ERROR BIT(2)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

奇偶校验错误（Parity Error）：接收字符的奇偶校验不正确。

<a id="gad98eed7203cbf79f2b97ba695af1ae06"></a>

### `BT_RFCOMM_RLS_NO_ERR`

```c
#define BT_RFCOMM_RLS_NO_ERR (0x00U)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

远端线路状态（Remote Line Status）值：无错误。

<a id="gaef902e774d1a6279a117968a32cc5878"></a>

### `BT_RFCOMM_RPN_FLOW_NONE`

```c
#define BT_RFCOMM_RPN_FLOW_NONE 0x00
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="ga71099379ed90d3d6ce9d4c1eed3be827"></a>

### `BT_RFCOMM_RPN_PARAM_MASK_ALL`

```c
#define BT_RFCOMM_RPN_PARAM_MASK_ALL 0x3f7f
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="gacdca9e597689b3de20b1df3616ad523c"></a>

### `BT_RFCOMM_RPN_XOFF_CHAR`

```c
#define BT_RFCOMM_RPN_XOFF_CHAR 0x13
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="ga90ab80687e32da0f8164292cd63b0623"></a>

### `BT_RFCOMM_RPN_XON_CHAR`

```c
#define BT_RFCOMM_RPN_XON_CHAR 0x11
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="gacbb625b129afb33fceafe5ddf61c839a"></a>

### `BT_RFCOMM_SET_LINE_SETTINGS`

```c
#define BT_RFCOMM_SET_LINE_SETTINGS ( data, stop, parity )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

展开值（Value）：

```c
((data & 0x3) | \
((stop & 0x1) << 2) | \
((parity & 0x7) << 3))
```

将数据位（Data Bits）、停止位（Stop Bits）与奇偶校验（Parity）合并为单个线路设置字节（Line Settings Byte）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 数据位值（Data Bits Value），0～3。 |
| `stop` | 停止位值（Stop Bits Value），0～1。 |
| `parity` | 奇偶校验值（Parity Value），0～7。 |

**返回（Returns）**：返回值（Returns）：组合后的线路设置字节（Line Settings Byte）。

<a id="ga11f290d34ad631afaa10caf2cefd72b9"></a>

### `bt_rfcomm_role_t`

```c
typedef enum bt_rfcomm_role bt_rfcomm_role_t
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

仅供内部 API 使用。

<a id="ga61637d261987529c219dcd1179ed1711"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 远端端口协商（RPN）的波特率值（Baud Rate Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_RPN_BAUD_RATE_2400` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_4800` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_7200` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_9600` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_19200` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_38400` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_57600` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_115200` |  |
| `BT_RFCOMM_RPN_BAUD_RATE_230400` |  |

<a id="ga15600feb01d876e319e1d5f93991592b"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 远端端口协商（RPN）的数据位值（Data Bit Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_RPN_DATA_BITS_5` |  |
| `BT_RFCOMM_RPN_DATA_BITS_6` |  |
| `BT_RFCOMM_RPN_DATA_BITS_7` |  |
| `BT_RFCOMM_RPN_DATA_BITS_8` |  |

<a id="gafccaaeb8f4d4f3e3834f358ccfdfb86b"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_CHAN_HFP_HF` |  |
| `BT_RFCOMM_CHAN_HFP_AG` |  |
| `BT_RFCOMM_CHAN_HSP_AG` |  |
| `BT_RFCOMM_CHAN_HSP_HS` |  |
| `BT_RFCOMM_CHAN_SPP` |  |
| `BT_RFCOMM_CHAN_DYNAMIC_START` |  |

<a id="gad1794db284f7b39f4816f04f21ed3f4b"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 远端端口协商（RPN）的奇偶校验位值（Parity Bit Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_RPN_PARITY_NONE` |  |
| `BT_RFCOMM_RPN_PARITY_ODD` |  |
| `BT_RFCOMM_RPN_PARITY_EVEN` |  |
| `BT_RFCOMM_RPN_PARITY_MARK` |  |
| `BT_RFCOMM_RPN_PARITY_SPACE` |  |

<a id="gabe97ddd372c3b0b44a9b78539ddf9ffc"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 远端端口协商（RPN）的停止位值（Stop Bit Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_RPN_STOP_BITS_1` |  |
| `BT_RFCOMM_RPN_STOP_BITS_1_5` |  |

<a id="gaa70d7971435dc7e6421372d7385811b2"></a>

### `bt_rfcomm_role`

```c
enum bt_rfcomm_role
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

仅供内部 API 使用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_RFCOMM_ROLE_ACCEPTOR` |  |
| `BT_RFCOMM_ROLE_INITIATOR` |  |

<a id="gaed05e67dc975d94e1209372d5817077a"></a>

### `bt_rfcomm_create_pdu()`

```c
struct net_buf * bt_rfcomm_create_pdu ( struct net_buf_pool * pool)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

为 RFCOMM、L2CAP 和 ACL 头部预留头部空间（Headroom）后，从池中分配缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 应从哪个缓冲池取得缓冲区。 |

**返回（Returns）**：**返回值（Returns）：**新缓冲区（New Buffer）。

<a id="ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7"></a>

### `bt_rfcomm_dlc_connect()`

```c
int bt_rfcomm_dlc_connect ( struct bt_conn * conn, struct bt_rfcomm_dlc * dlc, uint8_t channel )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

连接 RFCOMM 通道（Channel）。

按通道连接 RFCOMM 数据链路连接（DLC）。连接完成后调用 dlc 的 connected() 回调；连接被拒绝则调用 disconnected() 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `dlc` | 数据链路连接对象（DLC Object）。 |
| `channel` | 要连接的服务器通道（Server Channel）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga998328b021ec53f7e291ab76856ffa18"></a>

### `bt_rfcomm_dlc_disconnect()`

```c
int bt_rfcomm_dlc_disconnect ( struct bt_rfcomm_dlc * dlc)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

断开 RFCOMM 数据链路连接（DLC）。

断开 RFCOMM 数据链路连接（DLC）；若连接尚在等待建立，则取消连接并调用 dlc 的 disconnected() 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 数据链路连接对象（DLC Object）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga2ce765351798976136c3096a9a7f9465"></a>

### `bt_rfcomm_dlc_recv_complete()`

```c
int bt_rfcomm_dlc_recv_complete ( struct bt_rfcomm_dlc * dlc, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

完成 RFCOMM 通道数据的接收。

对于每次返回 -EINPROGRESS 的 bt_rfcomm_dlc_ops::recv 调用，必须恰好调用一次此函数。传回该回调收到的同一个 buf 指针，无需额外调用 net_buf_ref 或 net_buf_unref。

此函数返回时，无论返回值如何，协议栈都会释放自身对 buf 的引用；但 dlc 或 buf 为 NULL 时例外，此时立即返回 -EINVAL，不操作 buf。

调用成功后的流量控制行为（Flow-control Behavior）：

- 基于信用的流量控制会话（CFC Sessions）：协议栈此时可向远端对等方发送更多接收信用额度（RX Credits），允许其发送更多帧。
- 非 CFC 会话（Non-CFC Sessions）：只有全部进行中的缓冲区均完成后，才向远端对等方发送 FC=0，即恢复（Resume）的 MSC 命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 指向正在完成接收操作的 RFCOMM DLC 的指针。 |
| `buf` | 传给 bt_rfcomm_dlc_ops::recv 且该回调返回 -EINPROGRESS 时的缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | dlc 或 buf 为 NULL、DLC 的 CFC 状态未知，或进行中计数器将下溢（完成次数多于进行中调用次数）。 |
| `-ENOTCONN` | DLC 没有关联会话，或不处于已连接状态。 |

**说明（Note）**：注意（Note）：只能在线程上下文调用，绝不能从 ISR 调用。必须在 bt_rfcomm_dlc_ops::recv 返回之后调用；在 recv 回调内部、返回之前调用，会导致进行中计数器下溢，并返回 -EINVAL。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga593841aef52027598977b7b2bbd0237d"></a>

### `bt_rfcomm_dlc_send()`

```c
int bt_rfcomm_dlc_send ( struct bt_rfcomm_dlc * dlc, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

向 RFCOMM 发送数据。

将缓冲区数据发送到 DLC，长度应小于或等于 mtu。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 数据链路连接对象（DLC Object）。 |
| `buf` | 数据缓冲区（Data Buffer） |

**返回（Returns）**：返回值（Returns）：成功返回已发送字节数，错误返回负值。

<a id="ga1a46f58b41dab9a81b8d2b88f0f22547"></a>

### `bt_rfcomm_send_rls_cmd()`

```c
int bt_rfcomm_send_rls_cmd ( struct bt_rfcomm_dlc * dlc, uint8_t line_status )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

发送远端线路状态命令（Remote Line Status Command）。

向 RFCOMM DLC 发送指定 line_status 值的远端线路状态（Remote Line Status）。BIT(4-7) 保留，必须设为 0；BIT(0-3) 表示线路状态。BIT(0) 为 0 表示无错误；为 1 时，BIT(1-3) 用以下值指示错误：BT_RFCOMM_RLS_ERR_OVERRUN_ERROR 为接收字符覆盖未读字符；BT_RFCOMM_RLS_ERR_PARITY_ERROR 为接收字符奇偶校验不正确；BT_RFCOMM_RLS_ERR_FRAMING_ERROR 为字符未以停止位结束。

可以使用 BT_RFCOMM_RLS_NO_ERR 和 BT_RFCOMM_RLS_ERR 宏创建 line_status。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 指向 RFCOMM DLC 的指针 |
| `line_status` | 线路状态值（Line Status Value） |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab38378db71d7f4631e47742ce4a5c59d"></a>

### `bt_rfcomm_send_rpn_cmd()`

```c
int bt_rfcomm_send_rpn_cmd ( struct bt_rfcomm_dlc * dlc, struct bt_rfcomm_rpn * rpn )
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

发送远端端口协商命令（Remote Port Negotiation Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dlc` | 指向 RFCOMM DLC 的指针 |
| `rpn` | 指向待发送远端端口协商参数（RPN Parameters）的指针 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gafd0ffcff41e233f74dc2726e889f5401"></a>

### `bt_rfcomm_server_register()`

```c
int bt_rfcomm_server_register ( struct bt_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

注册 RFCOMM 服务器（Server）。

为通道注册 RFCOMM 服务器。每个新连接通过 accept() 回调授权，成功时该回调应为新连接分配要使用的 dlc 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf6bb5c563ba32fa76fc774271d958fe4"></a>

### `bt_rfcomm_server_unregister()`

```c
int bt_rfcomm_server_unregister ( struct bt_rfcomm_server * server)
```

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

注销 RFCOMM 服务器（Server）。

注销通道的 RFCOMM 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 服务器结构体（Server Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。


## 8.7\_原页交叉引用（Cross References）

- [bt_rfcomm_dlc_ops](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md)
- [bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)
- [bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)
- [bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [zephyr/bluetooth/classic/rfcomm.h](../api_file_audio_gateway_reference/P024_zephyr__bluetooth__classic__rfcomm.h_文件参考.md)
- [BT_L2CAP_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#gab95b119de4757588074e367a90a7136a)
- [bt_rfcomm_dlc_ops::recv](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#ab8ef2f8c1d27eee20d0b5e7fce6f7354)
- [net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [accept()](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a66e3de379c18201b21c889035ec54864)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__l2cap_html_gab95b119de4757588074e367a90a7136a"></a>
<a id="agroup__bt__rfcomm_html_ga99d36ccceccf03b011fbee0690d6565c"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3"></a>
<a id="gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60"></a>
<a id="gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593"></a>
<a id="gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9"></a>
<a id="gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c"></a>
<a id="gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5"></a>
<a id="gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048"></a>
<a id="gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33"></a>
<a id="gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760"></a>
<a id="gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1"></a>
<a id="gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc"></a>
<a id="gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867"></a>
<a id="gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495"></a>
<a id="ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302"></a>
<a id="ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b"></a>
<a id="ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169"></a>
<a id="ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18"></a>
<a id="ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9"></a>
<a id="ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1"></a>
<a id="ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339"></a>
<a id="ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6"></a>
<a id="ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d"></a>
<a id="ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_消息（Message）。.md) · [返回大纲](大纲.md) · [下一章](P009_音量控制配置文件（Volume Control Profile，VCP）.md)
