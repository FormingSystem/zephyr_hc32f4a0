---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-24
title: zephyr__bluetooth__classic__rfcomm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_bluetooth\_\_classic\_\_rfcomm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙RFCOMM的处理。

<a id="details"></a>

```c
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙RFCOMM的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

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

## 24.2\_宏定义（Macros）

<a id="r_ga8d7b15c80fc69a25b105aadf6f3a6a6d"></a>

```c
#define BT_RFCOMM_HDR_MAX_SIZE 4
```

相关声明：[BT_RFCOMM_HDR_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga8d7b15c80fc69a25b105aadf6f3a6a6d)。

RFCOMM 最大头部大小（Maximum Header Size）。

<a id="r_gaea26fe8eac8c5792a4cb78404dc4f7c1"></a>

```c
#define BT_RFCOMM_FCS_SIZE 1
```

相关声明：[BT_RFCOMM_FCS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaea26fe8eac8c5792a4cb78404dc4f7c1)。

RFCOMM 帧校验序列大小（FCS Size）。

<a id="r_ga90af70151ba4581d74422c9c79bee320"></a>

```c
#define BT_RFCOMM_CREDITS_SIZE 1
```

相关声明：[BT_RFCOMM_CREDITS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga90af70151ba4581d74422c9c79bee320)。

RFCOMM 信用值字段大小（Credits Size）。

<a id="r_ga99d36ccceccf03b011fbee0690d6565c"></a>

```c
#define BT_RFCOMM_OVERHEAD_SIZE (BT_RFCOMM_HDR_MAX_SIZE + BT_RFCOMM_FCS_SIZE + BT_RFCOMM_CREDITS_SIZE)
```

相关声明：[BT_RFCOMM_OVERHEAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga99d36ccceccf03b011fbee0690d6565c)、[BT_RFCOMM_HDR_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga8d7b15c80fc69a25b105aadf6f3a6a6d)、[BT_RFCOMM_FCS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaea26fe8eac8c5792a4cb78404dc4f7c1)、[BT_RFCOMM_CREDITS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga90af70151ba4581d74422c9c79bee320)。

RFCOMM 协议开销大小（Overhead Size）。

<a id="r_gabb568d7f32dbd0720f203538e3aa345c"></a>

```c
#define BT_RFCOMM_BUF_SIZE(mtu)
```

相关声明：[BT_RFCOMM_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gabb568d7f32dbd0720f203538e3aa345c)。

计算 RFCOMM 协议数据单元（PDU）所需缓冲区大小的辅助接口。

<a id="r_gacbb625b129afb33fceafe5ddf61c839a"></a>

```c
#define BT_RFCOMM_SET_LINE_SETTINGS(data, stop, parity)
```

相关声明：[BT_RFCOMM_SET_LINE_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gacbb625b129afb33fceafe5ddf61c839a)。

将数据位（Data Bits）、停止位（Stop Bits）与奇偶校验（Parity）合并为单个线路设置字节（Line Settings Byte）。

<a id="r_gaef902e774d1a6279a117968a32cc5878"></a>

```c
#define BT_RFCOMM_RPN_FLOW_NONE 0x00
```

相关声明：[BT_RFCOMM_RPN_FLOW_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaef902e774d1a6279a117968a32cc5878)。

<a id="r_ga90ab80687e32da0f8164292cd63b0623"></a>

```c
#define BT_RFCOMM_RPN_XON_CHAR 0x11
```

相关声明：[BT_RFCOMM_RPN_XON_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga90ab80687e32da0f8164292cd63b0623)。

<a id="r_gacdca9e597689b3de20b1df3616ad523c"></a>

```c
#define BT_RFCOMM_RPN_XOFF_CHAR 0x13
```

相关声明：[BT_RFCOMM_RPN_XOFF_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gacdca9e597689b3de20b1df3616ad523c)。

<a id="r_ga71099379ed90d3d6ce9d4c1eed3be827"></a>

```c
#define BT_RFCOMM_RPN_PARAM_MASK_ALL 0x3f7f
```

相关声明：[BT_RFCOMM_RPN_PARAM_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga71099379ed90d3d6ce9d4c1eed3be827)。

<a id="r_gad98eed7203cbf79f2b97ba695af1ae06"></a>

```c
#define BT_RFCOMM_RLS_NO_ERR (0x00U)
```

相关声明：[BT_RFCOMM_RLS_NO_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gad98eed7203cbf79f2b97ba695af1ae06)。

远端线路状态（Remote Line Status）值：无错误。

<a id="r_ga4e3f4fdb6841de8796f7598055cca1ae"></a>

```c
#define BT_RFCOMM_RLS_ERR(err)
```

相关声明：[BT_RFCOMM_RLS_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga4e3f4fdb6841de8796f7598055cca1ae)。

远端线路状态（Remote Line Status）值：发生错误。

<a id="r_ga14064eb94c14aa984eb36cf8a9656ba9"></a>

```c
#define BT_RFCOMM_RLS_ERR_OVERRUN_ERROR BIT(1)
```

相关声明：[BT_RFCOMM_RLS_ERR_OVERRUN_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga14064eb94c14aa984eb36cf8a9656ba9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

溢出错误（Overrun Error）：接收的字符覆盖了尚未读取的字符。

<a id="r_ga551b453e00b81289f239335d07bc62f2"></a>

```c
#define BT_RFCOMM_RLS_ERR_PARITY_ERROR BIT(2)
```

相关声明：[BT_RFCOMM_RLS_ERR_PARITY_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga551b453e00b81289f239335d07bc62f2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

奇偶校验错误（Parity Error）：接收字符的奇偶校验不正确。

<a id="r_gad4b245fdc58379a9617200921f29dd77"></a>

```c
#define BT_RFCOMM_RLS_ERR_FRAMING_ERROR BIT(3)
```

相关声明：[BT_RFCOMM_RLS_ERR_FRAMING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gad4b245fdc58379a9617200921f29dd77)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

帧格式错误（Framing Error）：字符未以停止位结束。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 24.3\_类型定义（Typedefs）

<a id="r_ga11f290d34ad631afaa10caf2cefd72b9"></a>

```c
typedef enum bt_rfcomm_role bt_rfcomm_role_t
```

相关声明：[bt_rfcomm_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaa70d7971435dc7e6421372d7385811b2)、[bt_rfcomm_role_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga11f290d34ad631afaa10caf2cefd72b9)。

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.4\_枚举（Enumerations）

<a id="r_gafccaaeb8f4d4f3e3834f358ccfdfb86b"></a>

```c
enum { BT_RFCOMM_CHAN_HFP_HF = 1 , BT_RFCOMM_CHAN_HFP_AG , BT_RFCOMM_CHAN_HSP_AG , BT_RFCOMM_CHAN_HSP_HS , BT_RFCOMM_CHAN_SPP , BT_RFCOMM_CHAN_DYNAMIC_START }
```

相关声明：[BT_RFCOMM_CHAN_HFP_HF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4)、[BT_RFCOMM_CHAN_HFP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd)、[BT_RFCOMM_CHAN_HSP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b)、[BT_RFCOMM_CHAN_HSP_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25)、[BT_RFCOMM_CHAN_SPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)、[BT_RFCOMM_CHAN_DYNAMIC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)。

<a id="r_gaa70d7971435dc7e6421372d7385811b2"></a>

```c
enum bt_rfcomm_role { BT_RFCOMM_ROLE_ACCEPTOR , BT_RFCOMM_ROLE_INITIATOR }
```

相关声明：[bt_rfcomm_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaa70d7971435dc7e6421372d7385811b2)、[BT_RFCOMM_ROLE_ACCEPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)、[BT_RFCOMM_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)。

RFCOMM 会话与数据链路连接（DLC）的角色（Role）。

<a id="r_ga61637d261987529c219dcd1179ed1711"></a>

```c
enum { BT_RFCOMM_RPN_BAUD_RATE_2400 = 0x0 , BT_RFCOMM_RPN_BAUD_RATE_4800 = 0x1 , BT_RFCOMM_RPN_BAUD_RATE_7200 = 0x2 , BT_RFCOMM_RPN_BAUD_RATE_9600 = 0x3 , BT_RFCOMM_RPN_BAUD_RATE_19200 = 0x4 , BT_RFCOMM_RPN_BAUD_RATE_38400 = 0x5 , BT_RFCOMM_RPN_BAUD_RATE_57600 = 0x6 , BT_RFCOMM_RPN_BAUD_RATE_115200 = 0x7 , BT_RFCOMM_RPN_BAUD_RATE_230400 = 0x8 }
```

相关声明：[BT_RFCOMM_RPN_BAUD_RATE_2400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3)、[BT_RFCOMM_RPN_BAUD_RATE_4800](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60)、[BT_RFCOMM_RPN_BAUD_RATE_7200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593)、[BT_RFCOMM_RPN_BAUD_RATE_9600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9)、[BT_RFCOMM_RPN_BAUD_RATE_19200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c)、[BT_RFCOMM_RPN_BAUD_RATE_38400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5)、[BT_RFCOMM_RPN_BAUD_RATE_57600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048)、[BT_RFCOMM_RPN_BAUD_RATE_115200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33)、[BT_RFCOMM_RPN_BAUD_RATE_230400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760)。

RFCOMM 远端端口协商（RPN）的波特率值（Baud Rate Values）。

<a id="r_ga15600feb01d876e319e1d5f93991592b"></a>

```c
enum { BT_RFCOMM_RPN_DATA_BITS_5 = 0x0 , BT_RFCOMM_RPN_DATA_BITS_6 = 0x1 , BT_RFCOMM_RPN_DATA_BITS_7 = 0x2 , BT_RFCOMM_RPN_DATA_BITS_8 = 0x3 }
```

相关声明：[BT_RFCOMM_RPN_DATA_BITS_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1)、[BT_RFCOMM_RPN_DATA_BITS_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc)、[BT_RFCOMM_RPN_DATA_BITS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867)、[BT_RFCOMM_RPN_DATA_BITS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83)。

RFCOMM 远端端口协商（RPN）的数据位值（Data Bit Values）。

<a id="r_gabe97ddd372c3b0b44a9b78539ddf9ffc"></a>

```c
enum { BT_RFCOMM_RPN_STOP_BITS_1 = 0 , BT_RFCOMM_RPN_STOP_BITS_1_5 = 1 }
```

相关声明：[BT_RFCOMM_RPN_STOP_BITS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339)、[BT_RFCOMM_RPN_STOP_BITS_1_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6)。

RFCOMM 远端端口协商（RPN）的停止位值（Stop Bit Values）。

<a id="r_gad1794db284f7b39f4816f04f21ed3f4b"></a>

```c
enum { BT_RFCOMM_RPN_PARITY_NONE = 0x0 , BT_RFCOMM_RPN_PARITY_ODD = 0x1 , BT_RFCOMM_RPN_PARITY_EVEN = 0x3 , BT_RFCOMM_RPN_PARITY_MARK = 0x5 , BT_RFCOMM_RPN_PARITY_SPACE = 0x7 }
```

相关声明：[BT_RFCOMM_RPN_PARITY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b)、[BT_RFCOMM_RPN_PARITY_ODD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169)、[BT_RFCOMM_RPN_PARITY_EVEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18)、[BT_RFCOMM_RPN_PARITY_MARK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9)、[BT_RFCOMM_RPN_PARITY_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1)。

RFCOMM 远端端口协商（RPN）的奇偶校验位值（Parity Bit Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.5\_函数（Functions）

<a id="r_gafd0ffcff41e233f74dc2726e889f5401"></a>

```c
int bt_rfcomm_server_register (struct bt_rfcomm_server *server)
```

相关声明：[bt_rfcomm_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gafd0ffcff41e233f74dc2726e889f5401)、[bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)。

注册 RFCOMM 服务器（Server）。

<a id="r_gaf6bb5c563ba32fa76fc774271d958fe4"></a>

```c
int bt_rfcomm_server_unregister (struct bt_rfcomm_server *server)
```

相关声明：[bt_rfcomm_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaf6bb5c563ba32fa76fc774271d958fe4)、[bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)。

注销 RFCOMM 服务器（Server）。

<a id="r_ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7"></a>

```c
int bt_rfcomm_dlc_connect (struct bt_conn *conn, struct bt_rfcomm_dlc *dlc, uint8_t channel)
```

相关声明：[bt_rfcomm_dlc_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

连接 RFCOMM 通道（Channel）。

<a id="r_ga593841aef52027598977b7b2bbd0237d"></a>

```c
int bt_rfcomm_dlc_send (struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

相关声明：[bt_rfcomm_dlc_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga593841aef52027598977b7b2bbd0237d)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向 RFCOMM 发送数据。

<a id="r_ga998328b021ec53f7e291ab76856ffa18"></a>

```c
int bt_rfcomm_dlc_disconnect (struct bt_rfcomm_dlc *dlc)
```

相关声明：[bt_rfcomm_dlc_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga998328b021ec53f7e291ab76856ffa18)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)。

断开 RFCOMM 数据链路连接（DLC）。

<a id="r_ga2ce765351798976136c3096a9a7f9465"></a>

```c
int bt_rfcomm_dlc_recv_complete (struct bt_rfcomm_dlc *dlc, struct net_buf *buf)
```

相关声明：[bt_rfcomm_dlc_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2ce765351798976136c3096a9a7f9465)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

完成 RFCOMM 通道数据的接收。

<a id="r_gaed05e67dc975d94e1209372d5817077a"></a>

```c
struct net_buf * bt_rfcomm_create_pdu (struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_rfcomm_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaed05e67dc975d94e1209372d5817077a)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

为 RFCOMM、L2CAP 和 ACL 头部预留头部空间（Headroom）后，从池中分配缓冲区。

<a id="r_gab38378db71d7f4631e47742ce4a5c59d"></a>

```c
int bt_rfcomm_send_rpn_cmd (struct bt_rfcomm_dlc *dlc, struct bt_rfcomm_rpn *rpn)
```

相关声明：[bt_rfcomm_send_rpn_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gab38378db71d7f4631e47742ce4a5c59d)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)。

发送远端端口协商命令（Remote Port Negotiation Command）。

<a id="r_ga1a46f58b41dab9a81b8d2b88f0f22547"></a>

```c
int bt_rfcomm_send_rls_cmd (struct bt_rfcomm_dlc *dlc, uint8_t line_status)
```

相关声明：[bt_rfcomm_send_rls_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga1a46f58b41dab9a81b8d2b88f0f22547)、[bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送远端线路状态命令（Remote Line Status Command）。


## 24.6\_原页交叉引用（Cross References）

- [zephyr/bluetooth/buf.h](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/bluetooth/l2cap.h](../api_source_system_reference/P016_l2cap.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P053_rfcomm.h_源码浏览.md)
- [bt_rfcomm_dlc_ops](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md)
- [bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)
- [bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)
- [bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)
- [BT_RFCOMM_HDR_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga8d7b15c80fc69a25b105aadf6f3a6a6d)
- [BT_RFCOMM_FCS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaea26fe8eac8c5792a4cb78404dc4f7c1)
- [BT_RFCOMM_CREDITS_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga90af70151ba4581d74422c9c79bee320)
- [BT_RFCOMM_OVERHEAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga99d36ccceccf03b011fbee0690d6565c)
- [BT_RFCOMM_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gabb568d7f32dbd0720f203538e3aa345c)
- [BT_RFCOMM_SET_LINE_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gacbb625b129afb33fceafe5ddf61c839a)
- [BT_RFCOMM_RPN_FLOW_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaef902e774d1a6279a117968a32cc5878)
- [BT_RFCOMM_RPN_XON_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga90ab80687e32da0f8164292cd63b0623)
- [BT_RFCOMM_RPN_XOFF_CHAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gacdca9e597689b3de20b1df3616ad523c)
- [BT_RFCOMM_RPN_PARAM_MASK_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga71099379ed90d3d6ce9d4c1eed3be827)
- [BT_RFCOMM_RLS_NO_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gad98eed7203cbf79f2b97ba695af1ae06)
- [BT_RFCOMM_RLS_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga4e3f4fdb6841de8796f7598055cca1ae)
- [BT_RFCOMM_RLS_ERR_OVERRUN_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga14064eb94c14aa984eb36cf8a9656ba9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_RFCOMM_RLS_ERR_PARITY_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga551b453e00b81289f239335d07bc62f2)
- [BT_RFCOMM_RLS_ERR_FRAMING_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gad4b245fdc58379a9617200921f29dd77)
- [bt_rfcomm_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaa70d7971435dc7e6421372d7385811b2)
- [bt_rfcomm_role_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga11f290d34ad631afaa10caf2cefd72b9)
- [BT_RFCOMM_CHAN_HFP_HF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4)
- [BT_RFCOMM_CHAN_HFP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd)
- [BT_RFCOMM_CHAN_HSP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b)
- [BT_RFCOMM_CHAN_HSP_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25)
- [BT_RFCOMM_CHAN_SPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)
- [BT_RFCOMM_CHAN_DYNAMIC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)
- [BT_RFCOMM_ROLE_ACCEPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)
- [BT_RFCOMM_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)
- [BT_RFCOMM_RPN_BAUD_RATE_2400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3)
- [BT_RFCOMM_RPN_BAUD_RATE_4800](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60)
- [BT_RFCOMM_RPN_BAUD_RATE_7200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593)
- [BT_RFCOMM_RPN_BAUD_RATE_9600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9)
- [BT_RFCOMM_RPN_BAUD_RATE_19200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c)
- [BT_RFCOMM_RPN_BAUD_RATE_38400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5)
- [BT_RFCOMM_RPN_BAUD_RATE_57600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048)
- [BT_RFCOMM_RPN_BAUD_RATE_115200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33)
- [BT_RFCOMM_RPN_BAUD_RATE_230400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760)
- [BT_RFCOMM_RPN_DATA_BITS_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1)
- [BT_RFCOMM_RPN_DATA_BITS_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc)
- [BT_RFCOMM_RPN_DATA_BITS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867)
- [BT_RFCOMM_RPN_DATA_BITS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83)
- [BT_RFCOMM_RPN_STOP_BITS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339)
- [BT_RFCOMM_RPN_STOP_BITS_1_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6)
- [BT_RFCOMM_RPN_PARITY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b)
- [BT_RFCOMM_RPN_PARITY_ODD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169)
- [BT_RFCOMM_RPN_PARITY_EVEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18)
- [BT_RFCOMM_RPN_PARITY_MARK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9)
- [BT_RFCOMM_RPN_PARITY_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1)
- [bt_rfcomm_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gafd0ffcff41e233f74dc2726e889f5401)
- [bt_rfcomm_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaf6bb5c563ba32fa76fc774271d958fe4)
- [bt_rfcomm_dlc_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_rfcomm_dlc_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga593841aef52027598977b7b2bbd0237d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_rfcomm_dlc_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga998328b021ec53f7e291ab76856ffa18)
- [bt_rfcomm_dlc_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2ce765351798976136c3096a9a7f9465)
- [bt_rfcomm_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaed05e67dc975d94e1209372d5817077a)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_rfcomm_send_rpn_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gab38378db71d7f4631e47742ce4a5c59d)
- [bt_rfcomm_send_rls_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga1a46f58b41dab9a81b8d2b88f0f22547)

<a id="header-details"></a>

---

[上一章](P023_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rx-pfs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__bluetooth__sbc.h_文件参考.md)
