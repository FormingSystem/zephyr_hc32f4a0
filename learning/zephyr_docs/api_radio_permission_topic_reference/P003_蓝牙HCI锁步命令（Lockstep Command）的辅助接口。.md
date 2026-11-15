---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-3
title: 蓝牙HCI锁步命令（Lockstep Command）的辅助接口。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙HCI锁步命令（Lockstep Command）的辅助接口。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙HCI锁步命令（Lockstep Command）的辅助接口。

<a id="details"></a>

蓝牙 HCI 锁步命令辅助接口（Bluetooth HCI Lockstep Command Helper）。引入版本（Since）：4.5；API 版本（Version）：0.1.0。帮助 HCI 驱动逐条发送 HCI 命令并等待响应。这些驱动通过自己的传输通道与控制器交换 HCI 命令，通常用于厂商专有控制器初始化，不使用蓝牙主机（Bluetooth Host）的命令机制，也不依赖构建中是否包含主机。辅助接口要求 HCI 流量以锁步方式运行：一条命令未完成时不发送其他命令，因此收到的下一个命令响应必然属于该命令。控制器初始化期间、HCI 传输通道交给使用者之前满足这一条件，因而无需操作码关联状态机。仍需遵守命令流量控制（Command Flow Control）：只有控制器允许时才发送一条命令。控制器在初始时允许一条，并通过每个命令响应中的 Num_HCI_Command_Packets 字段继续授权，包括控制器主动发送、用于允许后续命令的 NOP 操作码 HCI_Command_Complete 事件。驱动提供传输发送函数，并将收到的控制器数据包交给 bt_hci_lockstep_feed()；该函数消费正在等待的响应，将其他数据包留给驱动处理。命令使用 hci_pkt.h 中的辅助接口构建，本头文件已包含该文件。辅助接口仅初始化一次，控制器命令额度（Command Allowance）的记录跨越传输通道的多次打开而保留。若驱动通过 HCI 命令之外的方式复位控制器，例如打开时使用复位线，则应在复位后、第一条命令之前调用 bt_hci_lockstep_reset()。所有启用 CONFIG_BT 的构建都包含此辅助接口。注意（Note）：这不是应用 API，预期使用者是 HCI 驱动。需要在主机运行期间发送 HCI 命令的应用，应使用 hci.h 中更高层的 bt_hci_cmd_alloc()、bt_hci_cmd_send() 和 bt_hci_cmd_send_sync()，它们与主机的命令流量控制协同工作。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Flockstep"></a>

```c
struct bt_hci_lockstep
```

相关声明：[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

锁步辅助对象（Lockstep Helper）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_ga3eeed334ea5d5f212e3b560bd5cd4def"></a>

```c
typedef int(* bt_hci_lockstep_send_t) (const struct device *dev, const uint8_t *pkt, size_t len)
```

相关声明：[bt_hci_lockstep_send_t](#ga3eeed334ea5d5f212e3b560bd5cd4def)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

锁步辅助器（lockstep helper）的传输发送函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga02ea7a0ad2bbb7d8ee9845122e34f8ab"></a>

```c
void bt_hci_lockstep_init (struct bt_hci_lockstep *ls, const struct device *dev, bt_hci_lockstep_send_t send)
```

相关声明：[bt_hci_lockstep_init](#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[device](../device_reference/P002_设备对象结构.md)、[bt_hci_lockstep_send_t](#ga3eeed334ea5d5f212e3b560bd5cd4def)、[send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)。

初始化锁步辅助器。

<a id="r_ga1d2d42b2db398cf4449b337588897f56"></a>

```c
void bt_hci_lockstep_reset (struct bt_hci_lockstep *ls)
```

相关声明：[bt_hci_lockstep_reset](#ga1d2d42b2db398cf4449b337588897f56)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)。

恢复锁步辅助器的初始状态。

<a id="r_gacb84fdafc6376483e12a8b7ec391fa7c"></a>

```c
bool bt_hci_lockstep_feed (struct bt_hci_lockstep *ls, const uint8_t *pkt, size_t len)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_hci_lockstep_feed](#gacb84fdafc6376483e12a8b7ec391fa7c)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将收到的主机控制器接口（HCI）数据包交给锁步辅助器。

<a id="r_gaa53d7b9aa5a7d6c5f11ea442c37f75d8"></a>

```c
int bt_hci_lockstep_cmd_send_sync (struct bt_hci_lockstep *ls, uint16_t opcode, struct net_buf_simple *cmd, struct net_buf_simple *rsp)
```

相关声明：[bt_hci_lockstep_cmd_send_sync](#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)、[bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

发送 HCI 命令并等待其响应。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga3eeed334ea5d5f212e3b560bd5cd4def"></a>

### `bt_hci_lockstep_send_t`

```c
typedef int(* bt_hci_lockstep_send_t) (const struct device *dev, const uint8_t *pkt, size_t len)
```

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

锁步辅助器（lockstep helper）的传输发送函数。

向控制器传输完整的 HCI 数据包（HCI Packet）。

负返回值表示命令未提交到控制器：辅助接口保留原本会消耗的命令额度（Command Allowance）。若传输层无法判断失败前命令是否已经到达控制器，则应返回 0，由响应等待结果决定最终结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 传给 bt_hci_lockstep_init() 的 HCI 设备。 |
| `pkt` | 要发送的数据包，从其数据包指示符（Packet Indicator）开始。 |
| `len` | pkt 的长度，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已将数据包提交到控制器。 |

**返回（Returns）**：返回值（Returns）：失败时返回负 errno，表示数据包未提交；该值传递给 bt_hci_lockstep_cmd_send_sync() 的调用方。

<a id="gaa53d7b9aa5a7d6c5f11ea442c37f75d8"></a>

### `bt_hci_lockstep_cmd_send_sync()`

```c
int bt_hci_lockstep_cmd_send_sync ( struct bt_hci_lockstep * ls, uint16_t opcode, struct net_buf_simple * cmd, struct net_buf_simple * rsp )
```

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

发送 HCI 命令并等待其响应。

使用 bt_hci_pkt_push_cmd_hdr() 将 cmd 中的命令参数封装成完整 HCI 命令包，等待控制器允许一条命令，通过传输发送函数发送数据包，然后等待控制器的 HCI_Command_Complete 或 HCI_Command_Status 响应经 bt_hci_lockstep_feed() 到达。等待命令许可和命令响应的总时长最多为 bt_hci_lockstep::timeout。

响应存放到 rsp 中，存放前先清空：首先是状态，其后是 HCI_Command_Complete 的返回参数，与 hci_types.h 中 bt_hci_rp_* 结构体的布局一致。超出 rsp 容量的字节会丢弃，因此应按预期返回参数设置容量。HCI_Command_Status 响应不携带返回参数，所以 rsp 仅存放状态；这只表示控制器已接受命令，完成情况稍后通过该命令自己的事件报告。

必须在线程上下文（Thread Context）调用，且一次只允许一个调用，由驱动串行化调用方。返回 -EINVAL 或 -EMSGSIZE 时 cmd 不变；其他任何返回时，cmd 都存放完整命令包，因此复用前须调用 bt_hci_pkt_reset_cmd()。每次失败都会与操作码一起记入日志，调用方无需重复记录。若响应已到达之后才报告传输发送失败，则只记录日志：命令已到达控制器，其响应仍然有效。

-EAGAIN 表示控制器无响应，应按无响应处理，而不是重试：可能是在超时内不允许发送命令，也可能是没有响应已发送命令。后一种情况下不再允许后续命令，否则无法区分迟到响应与后续同操作码命令的响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ls` | 锁步辅助对象（Lockstep Helper）。 |
| `opcode` | HCI 命令操作码（Opcode）。 |
| `cmd` | 存放命令参数的缓冲区，通过 BT_HCI_PKT_CMD_DEFINE() 或 bt_hci_pkt_reset_cmd() 设置；无参数命令可传 NULL。 |
| `rsp` | 用于返回参数的缓冲区；传 NULL 表示丢弃返回参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 命令成功完成。 |
| `-EIO` | 控制器响应了错误状态，该状态已记入日志并存入 rsp。 |
| `-EAGAIN` | 控制器在 bt_hci_lockstep::timeout 内未允许命令，或未作响应。 |
| `-EINVAL` | cmd 的头部空间（Headroom）不足以容纳数据包前缀。 |
| `-EMSGSIZE` | cmd 中的参数字节数超过 HCI 命令可携带的上限。 |

**返回（Returns）**：返回值（Returns）：传输发送失败时返回发送函数给出的负 errno；命令未提交。

<a id="gacb84fdafc6376483e12a8b7ec391fa7c"></a>

### `bt_hci_lockstep_feed()`

```c
bool bt_hci_lockstep_feed ( struct bt_hci_lockstep * ls, const uint8_t * pkt, size_t len )
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

将收到的主机控制器接口（HCI）数据包交给锁步辅助器。

使用辅助接口期间，驱动应对收到的每个控制器数据包调用此函数。若数据包是 bt_hci_lockstep_cmd_send_sync() 正在等待的命令响应，则消费该响应并唤醒等待者；其他包留给驱动按常规方式处理。不修改数据包。

传入的每个命令响应，无论是否被消费，都会更新控制器允许的命令数量，供 bt_hci_lockstep_cmd_send_sync() 等待；NOP 操作码的 HCI_Command_Complete 事件仅用于此目的。

可从任何上下文调用，包括中断服务例程（ISRs）。调用由驱动的单一接收路径串行化，并保持数据包的接收顺序。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ls` | 锁步辅助对象（Lockstep Helper）。 |
| `pkt` | 接收到的数据包，从其数据包指示符（Packet Indicator）开始。 |
| `len` | pkt 的长度，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 该数据包是所等待的响应，且已被消费。 |
| `false` | 该数据包不是所等待的响应。 |

<a id="ga02ea7a0ad2bbb7d8ee9845122e34f8ab"></a>

### `bt_hci_lockstep_init()`

```c
void bt_hci_lockstep_init ( struct bt_hci_lockstep * ls, const struct device * dev, bt_hci_lockstep_send_t send )
```

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

初始化锁步辅助器。

仅调用一次，通常在驱动的设备初始化函数中调用；之后每次打开传输通道都可使用辅助接口，无需重新初始化信号量（Semaphore）。若通过 HCI 命令之外的方式复位控制器，随后应调用 bt_hci_lockstep_reset()，而非再次调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ls` | 锁步辅助对象（Lockstep Helper）。 |
| `dev` | 传给 send 的 HCI 设备。 |
| `send` | 传输发送函数（Transport Send Function）。 |

<a id="ga1d2d42b2db398cf4449b337588897f56"></a>

### `bt_hci_lockstep_reset()`

```c
void bt_hci_lockstep_reset ( struct bt_hci_lockstep * ls)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/drivers/bluetooth/hci_lockstep.h>
```

恢复锁步辅助器的初始状态。

对于通过 HCI 命令之外的方式复位的控制器，恢复初始的一条命令额度（Command Allowance），使辅助接口不再等待复位后的控制器不会主动通告的额度。传输发送函数与 bt_hci_lockstep::timeout 保持不变。

可从任何上下文调用，包括中断服务例程（ISRs），也可与 bt_hci_lockstep_feed() 同时调用，因此通过无法停止的回调接收数据的驱动也能使用。如果 bt_hci_lockstep_cmd_send_sync() 正等待控制器允许命令，它将继续执行并发送命令；例如恢复路径复位了一个停止响应的控制器时即如此。

已经取得额度、但尚未收到响应的未完成命令（Outstanding Command）则不同：无法判断它在复位之前还是之后到达控制器，因此驱动不应在此时复位控制器。若仍然复位，该命令将被放弃，响应不再被消费，发送方失败：若命令无法提交，则返回传输错误；否则仅在超时到期后返回 -EAGAIN，不会提前返回，以免仍然到达的响应被误认为后续同操作码命令的响应。

控制器在复位前发送的数据包不得在复位后传入。辅助接口无法区分旧包与后续命令响应，因此相同操作码的旧响应会被当作新响应，而不允许任何命令的旧响应会撤销已恢复的命令额度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ls` | 锁步辅助对象（Lockstep Helper）。 |


## 3.5\_原页交叉引用（Cross References）

- [bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [hci_pkt.h](../api_file_network_device_reference/P014_zephyr__bluetooth__hci_pkt.h_文件参考.md)
- [CONFIG_BT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT)
- [bt_hci_cmd_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a974e6e9262601e73537cbdcba7a7c93c)
- [bt_hci_cmd_send()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#af2eed9d93da45185aad9c2edc0001a54)
- [bt_hci_cmd_send_sync()](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html#a8d306b5b56afdece1cadbbf0eecfe5a7)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/drivers/bluetooth/hci_lockstep.h](../api_file_interface_reference/P019_zephyr__drivers__bluetooth__hci_lockstep.h_文件参考.md)
- [bt_hci_pkt_push_cmd_hdr()](../api_buffer_paging_topic_reference/P004_蓝牙HCI数据包辅助接口（Packet Helpers）。.md#gac9d4ade374ccf35895cf601cdd6b3f79)
- [bt_hci_lockstep::timeout](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md#a6af9d44ebb27dab6971b99c39ba9b747)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [bt_hci_pkt_reset_cmd()](../api_buffer_paging_topic_reference/P004_蓝牙HCI数据包辅助接口（Packet Helpers）。.md#ga7f6c2d3674275bb9ce6752cf3f7e3228)
- [BT_HCI_PKT_CMD_DEFINE()](../api_buffer_paging_topic_reference/P004_蓝牙HCI数据包辅助接口（Packet Helpers）。.md#ga5c26db578cf6b427e7009fbbd692253e)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_CCP 呼叫控制客户端 API.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙 HID 主机（Host）.md)
