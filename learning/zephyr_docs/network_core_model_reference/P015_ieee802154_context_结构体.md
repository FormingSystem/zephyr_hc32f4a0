---
id: learning.zephyr-docs.network-core-model-reference.page-15
title: ieee802154_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_ieee802154\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4第二层（L2）的上下文。

```c
#include <zephyr/net/ieee802154.h>
```

<a id="details"></a>

IEEE 802.15.4第二层（L2）的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_ae3c9b2de2e55d619f2d8acf5cf8b7491"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#ae3c9b2de2e55d619f2d8acf5cf8b7491)。

个人区域网标识（PAN ID）。

<a id="r_ad02d219198201aee98ab1ab1793cfe6b"></a>

```c
uint16_t channel
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[channel](#ad02d219198201aee98ab1ab1793cfe6b)。

信道号（Channel Number）。

<a id="r_a64e992804fcd463ff437ac88c296dfab"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#a64e992804fcd463ff437ac88c296dfab)。

短地址（Short Address），采用CPU字节序。

<a id="r_a3dbbea6bef660e17b3bbf7c02a4672cc"></a>

```c
uint8_t ext_addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ext_addr](#a3dbbea6bef660e17b3bbf7c02a4672cc)。

扩展地址（Extended Address），采用小端序。

<a id="r_a4d1826923921a7b9a6caf993d50f6056"></a>

```c
struct net_linkaddr linkaddr
```

相关声明：[net_linkaddr](P105_net_linkaddr_结构体.md)、[linkaddr](#a4d1826923921a7b9a6caf993d50f6056)。

链路层地址（Link Layer Address），采用大端序。

<a id="r_a0a4cc252326f86af4d142d32950d2af6"></a>

```c
struct ieee802154_security_ctx sec_ctx
```

相关声明：[ieee802154_security_ctx](P044_ieee802154_security_ctx_结构体.md)、[sec_ctx](#a0a4cc252326f86af4d142d32950d2af6)。

安全上下文（Security Context）。

<a id="r_a06de84ddc495a80777b87f8934da94e5"></a>

```c
struct ieee802154_req_params * scan_ctx
```

相关声明：[ieee802154_req_params](P042_ieee802154_req_params_结构体.md)、[scan_ctx](#a06de84ddc495a80777b87f8934da94e5)。

指向扫描参数与结果（Scanning Parameters and Results）的指针，由scan_ctx_lock保护。

<a id="r_a35bfac224aff80f256853cb0d8ce8466"></a>

```c
struct k_sem scan_ctx_lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[scan_ctx_lock](#a35bfac224aff80f256853cb0d8ce8466)。

用于维护此结构中全部字段的数据完整性，字段级说明另有规定时除外。

<a id="r_a84053e172fbfd9d59c4d8e7a1b98d5b6"></a>

```c
uint8_t coord_ext_addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coord_ext_addr](#a84053e172fbfd9d59c4d8e7a1b98d5b6)。

协调器扩展地址（Coordinator Extended Address）。

<a id="r_abf1cc83c3a4880513137e7e4955174c1"></a>

```c
uint16_t coord_short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[coord_short_addr](#abf1cc83c3a4880513137e7e4955174c1)。

协调器短地址（Coordinator Short Address）。

<a id="r_a800a07927c4faec1dca2910a65c1baae"></a>

```c
int16_t tx_power
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tx_power](#a800a07927c4faec1dca2910a65c1baae)。

发射功率（Transmission Power），单位为dBm。

<a id="r_acf1fcafe106362eba112ea946a575bbd"></a>

```c
enum net_l2_flags flags
```

相关声明：[net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)、[flags](#acf1fcafe106362eba112ea946a575bbd)。

第二层标志（L2 Flags）。

<a id="r_a5618dec853ce41bbfa48e2aaa3f73262"></a>

```c
uint8_t sequence
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sequence](#a5618dec853ce41bbfa48e2aaa3f73262)。

数据序列号（Data Sequence Number）。

<a id="r_a70b2a2936aca60a5bc4fc2b98aa11497"></a>

```c
uint8_t device_role: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[device_role](#a70b2a2936aca60a5bc4fc2b98aa11497)。

设备角色（Device Role）。

<a id="r_a511059cb95c0d52c907464a1891586aa"></a>

```c
uint8_t ack_requested: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ack_requested](#a511059cb95c0d52c907464a1891586aa)。

确认请求标志（ACK Requested Flag），由ack_lock保护。

<a id="r_a0eeefef60bc7c266b2bb26893404ff86"></a>

```c
uint8_t ack_seq
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ack_seq](#a0eeefef60bc7c266b2bb26893404ff86)。

预期确认序列号（ACK Expected Sequence Number），由ack_lock保护。

<a id="r_a641c70a792f47431be8a0ffe2635a11f"></a>

```c
struct k_sem ack_lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[ack_lock](#a641c70a792f47431be8a0ffe2635a11f)。

确认锁（ACK Lock），保护ack_*字段。

<a id="r_a462527426b11b80ee53a3f91aacf1e1e"></a>

```c
struct k_sem ctx_lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[ctx_lock](#a462527426b11b80ee53a3f91aacf1e1e)。

上下文锁（Context Lock）。

## 15.2\_详细说明（Detailed Documentation）

<a id="a641c70a792f47431be8a0ffe2635a11f"></a>

### `ack_lock`

```c
struct k_sem ieee802154_context::ack_lock
```

确认锁（ACK Lock），保护ack_*字段。

<a id="a511059cb95c0d52c907464a1891586aa"></a>

### `ack_requested`

```c
uint8_t ieee802154_context::ack_requested
```

确认请求标志（ACK Requested Flag），由ack_lock保护。

<a id="a0eeefef60bc7c266b2bb26893404ff86"></a>

### `ack_seq`

```c
uint8_t ieee802154_context::ack_seq
```

预期确认序列号（ACK Expected Sequence Number），由ack_lock保护。

<a id="ad02d219198201aee98ab1ab1793cfe6b"></a>

### `channel`

```c
uint16_t ieee802154_context::channel
```

信道号（Channel Number）。

全部发送和接收使用的射频信道（RF Channel），见第11.3节表11-2的phyCurrentChannel。允许值范围取决于物理层（PHY），定义见第10.1.3节。

采用CPU字节序（CPU Byte Order）。

<a id="a84053e172fbfd9d59c4d8e7a1b98d5b6"></a>

### `coord_ext_addr`

```c
uint8_t ieee802154_context::coord_ext_addr[8]
```

协调器扩展地址（Coordinator Extended Address）。

见第8.4.3.1节表8-94的macCoordExtendedAddress，即设备通过其建立关联的协调器的地址。

0表示协调器扩展地址（Coordinator Extended Address）未知，为默认值。

采用小端序（Little Endian）。

<a id="abf1cc83c3a4880513137e7e4955174c1"></a>

### `coord_short_addr`

```c
uint16_t ieee802154_context::coord_short_addr
```

协调器短地址（Coordinator Short Address）。

见第8.4.3.1节表8-94的macCoordShortAddress，即设备通过其建立关联的协调器获分配的短地址。

0xfffe表示协调器仅使用扩展地址（Extended Address）；0xffff表示此值未知。

采用CPU字节序（CPU Byte Order）。

<a id="a462527426b11b80ee53a3f91aacf1e1e"></a>

### `ctx_lock`

```c
struct k_sem ieee802154_context::ctx_lock
```

上下文锁（Context Lock）。

此锁保护全部可变上下文属性（Mutable Context Attributes），属性级说明另有规定时除外。

<a id="a70b2a2936aca60a5bc4fc2b98aa11497"></a>

### `device_role`

```c
uint8_t ieee802154_context::device_role
```

设备角色（Device Role）。

见第6.1节：设备可以作为终端设备（End Device，0）、协调器（Coordinator，1）或PAN协调器（PAN Coordinator，2）运行。未显式配置设备角色时，将按终端设备处理。

值3未定义（Undefined）。

可通过ieee802154_device_role读取或设置。

<a id="a3dbbea6bef660e17b3bbf7c02a4672cc"></a>

### `ext_addr`

```c
uint8_t ieee802154_context::ext_addr[8]
```

扩展地址（Extended Address），采用小端序。

扩展地址（Extended Address）属于设备专用信息，通常永久存储在设备上且不可更改。

见第8.4.3.1节表8-94的macExtendedAddress。

<a id="acf1fcafe106362eba112ea946a575bbd"></a>

### `flags`

```c
enum net_l2_flags ieee802154_context::flags
```

第二层标志（L2 Flags）。

<a id="a4d1826923921a7b9a6caf993d50f6056"></a>

### `linkaddr`

```c
struct net_linkaddr ieee802154_context::linkaddr
```

链路层地址（Link Layer Address），采用大端序。

<a id="ae3c9b2de2e55d619f2d8acf5cf8b7491"></a>

### `pan_id`

```c
uint16_t ieee802154_context::pan_id
```

个人区域网标识（PAN ID）。

设备所在个人区域网（PAN）的标识符。0xffff表示设备尚未关联。见第8.4.3.1节表8-94的macPanId。

采用CPU字节序（CPU Byte Order）。

<a id="a06de84ddc495a80777b87f8934da94e5"></a>

### `scan_ctx`

```c
struct ieee802154_req_params* ieee802154_context::scan_ctx
```

指向扫描参数与结果（Scanning Parameters and Results）的指针，由scan_ctx_lock保护。

<a id="a35bfac224aff80f256853cb0d8ce8466"></a>

### `scan_ctx_lock`

```c
struct k_sem ieee802154_context::scan_ctx_lock
```

用于维护此结构中全部字段的数据完整性，字段级说明另有规定时除外。

<a id="a0a4cc252326f86af4d142d32950d2af6"></a>

### `sec_ctx`

```c
struct ieee802154_security_ctx ieee802154_context::sec_ctx
```

安全上下文（Security Context）。

<a id="a5618dec853ce41bbfa48e2aaa3f73262"></a>

### `sequence`

```c
uint8_t ieee802154_context::sequence
```

数据序列号（Data Sequence Number）。

添加到发送数据帧或MAC命令中的序列号（Sequence Number），见第8.4.3.1节表8-94的macDsn。

<a id="a64e992804fcd463ff437ac88c296dfab"></a>

### `short_addr`

```c
uint16_t ieee802154_context::short_addr
```

短地址（Short Address），采用CPU字节序。

范围（Range）：

- `0x0000`–`0xfffd`：已关联（Associated），并已分配短地址（Short address）。
- `0xfffe`：已关联（Associated），但未分配短地址（Short address）。
- `0xffff`：未关联（Not associated），默认值。

见第6.4.1节表6-4“短地址的使用（Usage of the short address）”，以及第8.4.3.1节表8-94的macShortAddress。原文将short误写为shart。

<a id="a800a07927c4faec1dca2910a65c1baae"></a>

### `tx_power`

```c
int16_t ieee802154_context::tx_power
```

发射功率（Transmission Power），单位为dBm。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_linkaddr](P105_net_linkaddr_结构体.md)
- [ieee802154_security_ctx](P044_ieee802154_security_ctx_结构体.md)
- [ieee802154_req_params](P042_ieee802154_req_params_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [net_l2_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html#gac7db0cc6c56d371a5803873074ec2516)
- [ieee802154_device_role](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__l2.html#ga7a4fb2d89381bba54514bf8396fb6d26)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_ieee802154_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_ieee802154_fcf_seq_结构体.md)
