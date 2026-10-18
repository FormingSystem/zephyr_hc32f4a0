---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-4
title: 蓝牙HCI数据包辅助接口（Packet Helpers）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙HCI数据包辅助接口（Packet Helpers）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙HCI数据包辅助接口（Packet Helpers）。

<a id="details"></a>

蓝牙 HCI 数据包辅助接口（Bluetooth HCI Packet Helpers）。引入版本（Since）：4.5；API 版本（Version）：0.1.0。用于构造 HCI 命令包，以及解析承载命令响应的 HCI 事件的无状态辅助接口，操作对象为 net_buf_simple 缓冲区和数据包字节。它们既不依赖蓝牙主机（Bluetooth Host），也不依赖 HCI 驱动接口，可用于任何构建类型：主机、HCI 驱动（例如通过驱动自己的传输通道执行厂商专有控制器初始化，参见 hci_lockstep.h），以及仅包含控制器的应用。注意（Note）：虽然头文件位于应用可见的 include 目录中，这些接口并非通用应用 API；预期使用者是 HCI 驱动及蓝牙协议栈内部代码。需要在主机运行期间发送 HCI 命令的应用，应使用 hci.h 中更高层的 bt_hci_cmd_alloc()、bt_hci_cmd_send() 和 bt_hci_cmd_send_sync()，它们与主机的命令流量控制协同工作。数据包沿用 Zephyr 的通用形式：首字节为 HCI 数据包指示符（Packet Indicator，如 BT_HCI_H4_CMD、BT_HCI_H4_EVT 等），随后是包头和参数。调用方通过紧凑布局的 bt_hci_cp_*、bt_hci_rp_* 结构体与 net_buf_simple API 编解码参数，与蓝牙主机中的做法相同。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Fpkt_5Fcmd_5Frsp"></a>

```c
struct bt_hci_pkt_cmd_rsp
```

相关声明：[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

已解码的 HCI 命令响应（Decoded HCI Command Response）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga97349aa18498cfd9a61817f1d149aa29"></a>

```c
#define BT_HCI_PKT_CMD_HDR_SIZE (sizeof(uint8_t) + BT_HCI_CMD_HDR_SIZE)
```

相关声明：[BT_HCI_PKT_CMD_HDR_SIZE](#ga97349aa18498cfd9a61817f1d149aa29)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_HCI_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acdf2b6de1459a7492415a8987ad9a896)。

HCI 命令数据包前缀（Prefix）的大小。

<a id="r_ga08079006c088d639abc45077c7a09532"></a>

```c
#define BT_HCI_PKT_CMD_SIZE(param_len)
```

相关声明：[BT_HCI_PKT_CMD_SIZE](#ga08079006c088d639abc45077c7a09532)。

带有 `param_len` 字节参数的 HCI 命令数据包大小。

<a id="r_ga5c26db578cf6b427e7009fbbd692253e"></a>

```c
#define BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len)
```

相关声明：[BT_HCI_PKT_CMD_DEFINE](#ga5c26db578cf6b427e7009fbbd692253e)。

定义用于 HCI 命令数据包的缓冲区（Buffer）。

<a id="r_ga0cc8ce4451e316f72cceda47c3a68b10"></a>

```c
#define BT_HCI_PKT_CMD_DEFINE_STATIC(_name, _max_param_len)
```

相关声明：[BT_HCI_PKT_CMD_DEFINE_STATIC](#ga0cc8ce4451e316f72cceda47c3a68b10)。

定义用于 HCI 命令数据包的静态缓冲区（Static Buffer）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga7f6c2d3674275bb9ce6752cf3f7e3228"></a>

```c
void bt_hci_pkt_reset_cmd (struct net_buf_simple *buf)
```

相关声明：[bt_hci_pkt_reset_cmd](#ga7f6c2d3674275bb9ce6752cf3f7e3228)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为新的 HCI 命令数据包重置缓冲区（Reset Buffer）。

<a id="r_gac9d4ade374ccf35895cf601cdd6b3f79"></a>

```c
int bt_hci_pkt_push_cmd_hdr (struct net_buf_simple *buf, uint16_t opcode)
```

相关声明：[bt_hci_pkt_push_cmd_hdr](#gac9d4ade374ccf35895cf601cdd6b3f79)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

压入 HCI 命令数据包的包指示符（Packet Indicator）和命令头（Command Header）。

<a id="r_ga5494d5cdc68840408f6b4b254dd474c9"></a>

```c
int bt_hci_pkt_pull_cmd_complete (struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_pull_cmd_complete](#ga5494d5cdc68840408f6b4b254dd474c9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

取出 `HCI_Command_Complete` 事件。

<a id="r_ga591c10d3d94a29be93ff5c4eb690201f"></a>

```c
int bt_hci_pkt_pull_cmd_status (struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_pull_cmd_status](#ga591c10d3d94a29be93ff5c4eb690201f)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

取出 `HCI_Command_Status` 事件。

<a id="r_ga588ed90a133f526c4abfa3fcd87ad8e5"></a>

```c
int bt_hci_pkt_parse_cmd_rsp (const uint8_t *pkt, size_t len, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_parse_cmd_rsp](#ga588ed90a133f526c4abfa3fcd87ad8e5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

从完整 HCI 数据包中解析 HCI 命令响应（Command Response）。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga5c26db578cf6b427e7009fbbd692253e"></a>

### `BT_HCI_PKT_CMD_DEFINE`

```c
#define BT_HCI_PKT_CMD_DEFINE ( _name, _max_param_len )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

展开值（Value）：

```c
Z_BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len,)
```

定义用于 HCI 命令数据包的缓冲区（Buffer）。

定义并初始化一个 net_buf_simple，为最多携带 _max_param_len 字节参数的 HCI 命令包提供存储空间。缓冲区初始为空，并为 bt_hci_pkt_push_cmd_hdr() 预留头部空间（Headroom）：先使用 net_buf_simple API 添加参数，再将包头压入参数前方。

若要将缓冲区复用于另一条命令，或在其他存储空间上准备缓冲区，请使用 bt_hci_pkt_reset_cmd()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | net_buf_simple 对象名称。 |
| `_max_param_len` | 该缓冲区容纳的最大参数字节数。 |

<a id="ga0cc8ce4451e316f72cceda47c3a68b10"></a>

### `BT_HCI_PKT_CMD_DEFINE_STATIC`

```c
#define BT_HCI_PKT_CMD_DEFINE_STATIC ( _name, _max_param_len )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

展开值（Value）：

```c
Z_BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len, static)
```

定义用于 HCI 命令数据包的静态缓冲区（Static Buffer）。

与 BT_HCI_PKT_CMD_DEFINE() 相同，但具有静态存储期（Static Storage Duration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | net_buf_simple 对象名称。 |
| `_max_param_len` | 该缓冲区容纳的最大参数字节数。 |

<a id="ga97349aa18498cfd9a61817f1d149aa29"></a>

### `BT_HCI_PKT_CMD_HDR_SIZE`

```c
#define BT_HCI_PKT_CMD_HDR_SIZE (sizeof(uint8_t) + BT_HCI_CMD_HDR_SIZE)
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

HCI 命令数据包前缀（Prefix）的大小。

数据包指示符后接 HCI 命令头，两者位于命令参数之前。大小等于蓝牙主机命令缓冲区使用的预留空间（参见 BT_BUF_CMD_SIZE）；单独定义此值，使本头文件不依赖主机的缓冲区 API。

<a id="ga08079006c088d639abc45077c7a09532"></a>

### `BT_HCI_PKT_CMD_SIZE`

```c
#define BT_HCI_PKT_CMD_SIZE ( param_len)
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

展开值（Value）：

```c
(BT_HCI_PKT_CMD_HDR_SIZE + (param_len))
```

带有 `param_len` 字节参数的 HCI 命令数据包大小。

<a id="ga588ed90a133f526c4abfa3fcd87ad8e5"></a>

### `bt_hci_pkt_parse_cmd_rsp()`

```c
int bt_hci_pkt_parse_cmd_rsp ( const uint8_t * pkt, size_t len, struct bt_hci_pkt_cmd_rsp * rsp )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

从完整 HCI 数据包中解析 HCI 命令响应（Command Response）。

检查从数据包指示符开始的完整 HCI 数据包；若其为 HCI_Command_Complete 或 HCI_Command_Status 事件，则解码并将命令的返回参数留在 bt_hci_pkt_cmd_rsp::rp 中。忽略事件头指定长度以外的字节，且不修改数据包，因此任何接收包均可原位检查。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 完整的 HCI 数据包。 |
| `len` | pkt 的长度，单位为字节。 |
| `rsp` | 解码后的响应（Decoded Response）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 该数据包是命令响应（Command Response）。 |
| `-ENODATA` | 该数据包是某条命令的 HCI_Command_Complete 事件，但未携带任何返回参数，甚至没有状态；将 rsp 中的状态填为 BT_HCI_ERR_UNSPECIFIED。 |
| `-ENOMSG` | 该数据包不是命令响应；rsp 保持不变。 |
| `-EINVAL` | 该数据包是格式错误的 HCI 事件；rsp 保持不变。 |

<a id="ga5494d5cdc68840408f6b4b254dd474c9"></a>

### `bt_hci_pkt_pull_cmd_complete()`

```c
int bt_hci_pkt_pull_cmd_complete ( struct net_buf_simple * buf, struct bt_hci_pkt_cmd_rsp * rsp )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

取出 `HCI_Command_Complete` 事件。

从 buf 解码 HCI_Command_Complete 事件的事件参数；buf 必须指向事件参数起始处，即 HCI 事件头之后。成功时移除返回参数之前的事件参数，使 buf 指向命令的返回参数；返回参数以状态开头，与 bt_hci_rp_* 结构体相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向事件参数位置的缓冲区。 |
| `rsp` | 解码后的响应（Decoded Response）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功；buf 指向返回参数。 |
| `-ENODATA` | 该事件响应了一条命令，但未携带任何返回参数，甚至没有状态；将 rsp 中的状态填为 BT_HCI_ERR_UNSPECIFIED，并将 buf 移至与成功时相同的位置。 |
| `-EINVAL` | 事件格式错误；buf 和 rsp 均保持不变。 |

<a id="ga591c10d3d94a29be93ff5c4eb690201f"></a>

### `bt_hci_pkt_pull_cmd_status()`

```c
int bt_hci_pkt_pull_cmd_status ( struct net_buf_simple * buf, struct bt_hci_pkt_cmd_rsp * rsp )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

取出 `HCI_Command_Status` 事件。

从 buf 解码 HCI_Command_Status 事件的事件参数；buf 必须指向事件参数起始处，即 HCI 事件头之后。成功时从缓冲区移除事件参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向事件参数位置的缓冲区。 |
| `rsp` | 解码后的响应（Decoded Response）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功；已从 buf 移除事件参数。 |
| `-EINVAL` | 事件格式错误；buf 和 rsp 均保持不变。 |

<a id="gac9d4ade374ccf35895cf601cdd6b3f79"></a>

### `bt_hci_pkt_push_cmd_hdr()`

```c
int bt_hci_pkt_push_cmd_hdr ( struct net_buf_simple * buf, uint16_t opcode )
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

压入 HCI 命令数据包的包指示符（Packet Indicator）和命令头（Command Header）。

在 buf 内容前添加 BT_HCI_H4_CMD 和操作码为 opcode 的 HCI 命令头。buf 必须存放命令参数（如有）；头部中的参数长度根据 buf 长度计算，随后缓冲区中即为完整的命令包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 存放命令参数的缓冲区，须至少具有 BT_HCI_PKT_CMD_HDR_SIZE 字节的头部空间（Headroom），如 BT_HCI_PKT_CMD_DEFINE() 或 bt_hci_pkt_reset_cmd() 所设置。 |
| `opcode` | HCI 命令操作码（Opcode）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功；buf 存放完整的命令包。 |
| `-EINVAL` | buf 的头部空间（Headroom）不足以容纳前缀。 |
| `-EMSGSIZE` | buf 中的参数字节数超过 HCI 命令可携带的上限。 |

<a id="ga7f6c2d3674275bb9ce6752cf3f7e3228"></a>

### `bt_hci_pkt_reset_cmd()`

```c
void bt_hci_pkt_reset_cmd ( struct net_buf_simple * buf)
```

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

为新的 HCI 命令数据包重置缓冲区（Reset Buffer）。

清空 buf，并为 bt_hci_pkt_push_cmd_hdr() 预留头部空间（Headroom），以便使用 net_buf_simple API 添加命令参数。可用此函数复用 BT_HCI_PKT_CMD_DEFINE() 定义的缓冲区，或准备在调用方提供的存储空间上初始化的 net_buf_simple（例如通过 net_buf_simple_init_with_data()）。存储空间至少须容纳 BT_HCI_PKT_CMD_HDR_SIZE 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 待重置的缓冲区。 |


## 4.5\_原页交叉引用（Cross References）

- [bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_HCI_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acdf2b6de1459a7492415a8987ad9a896)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [hci_lockstep.h](../api_file_interface_reference/P019_zephyr__drivers__bluetooth__hci_lockstep.h_文件参考.md)
- [bt_hci_cmd_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)
- [bt_hci_cmd_send()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#af2eed9d93da45185aad9c2edc0001a54)
- [bt_hci_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8d306b5b56afdece1cadbbf0eecfe5a7)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/bluetooth/hci_pkt.h](../api_file_network_device_reference/P014_zephyr__bluetooth__hci_pkt.h_文件参考.md)
- [BT_BUF_CMD_SIZE](P002_数据缓冲区（Data buffers）.md#ga9dc9de00be5e8bf673ec60921ea6681b)
- [bt_hci_pkt_cmd_rsp::rp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a16a24c4f86c12dcb5fba854609b9bb96)
- [net_buf_simple_init_with_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7fac47a2a25eaca39c5d14f1f55b485d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__hci__pkt_html_ga97349aa18498cfd9a61817f1d149aa29"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_密码学（Cryptography）.md) · [返回大纲](大纲.md) · [下一章](P005_动态主机配置协议第 4 版（DHCPv4）.md)
