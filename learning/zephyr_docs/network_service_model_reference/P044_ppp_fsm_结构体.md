---
id: learning.zephyr-docs.network-service-model-reference.page-44
title: ppp_fsm_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structppp__fsm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_ppp\_fsm\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structppp__fsm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用PPP有限状态机（Finite State Machine）。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

通用PPP有限状态机（Finite State Machine）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_ae033ee41d66ec568dc4244115730114a"></a>

```c
struct k_work_delayable timer
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[timer](#ae033ee41d66ec568dc4244115730114a)。

超时定时器（Timeout Timer）。

```c
struct {
```

<a id="r_a57bf8e8f6f47b249f8b3f8f920b98f1b"></a>

```c
int(* config_info_ack )(struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length)
```

相关声明：[config_info_ack](#a42bb4a40d88893d461d93202c4ad8e2a)、[ppp_fsm](P044_ppp_fsm_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

确认配置信息（Acknowledge Configuration Information）。

<a id="r_a979e7d2f5b97782daa448874111669e9"></a>

```c
struct net_pkt *(* config_info_add )(struct ppp_fsm *fsm)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[config_info_add](#a5a3c96319ec906968701c3eb72ce3d24)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

添加配置信息（Add Configuration Information）。

<a id="r_a9712a013b70e515bbc2573b534351197"></a>

```c
int(* config_info_len )(struct ppp_fsm *fsm)
```

相关声明：[config_info_len](#a099cc834fc5e2d062ee4410a1de729c2)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

配置信息长度（Length of Configuration Information）。

<a id="r_a7f6f39b8583330271a2005f3341838ff"></a>

```c
int(* config_info_nack )(struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length, bool rejected)
```

相关声明：[config_info_nack](#ad0967edee7fee72368732876ca6bc5e7)、[ppp_fsm](P044_ppp_fsm_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

否定确认配置信息（Negative Acknowledge Configuration Information）。

<a id="r_a827c723aa4b4bd35f0c067fb39f73167"></a>

```c
int(* config_info_req )(struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length, struct net_pkt *ret_pkt)
```

相关声明：[config_info_req](#ab430e0240f35718f6eaf8f9052a4edde)、[ppp_fsm](P044_ppp_fsm_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

请求对端配置信息（Request peer's Configuration Information）。

<a id="r_ab71eadb4f476c38e18de895da1a9168a"></a>

```c
int(* config_info_rej )(struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length)
```

相关声明：[config_info_rej](#a90dad2f780b4573559c76e6a67e44f4c)、[ppp_fsm](P044_ppp_fsm_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

拒绝配置信息（Reject Configuration Information）。

<a id="r_a8af45cd04e931c8b0cf3f55d9174c7b9"></a>

```c
void(* config_info_reset )(struct ppp_fsm *fsm)
```

相关声明：[config_info_reset](#afb0296b0d8e9b60594781cfd5f8acee3)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

重置配置信息（Reset Configuration Information）。

<a id="r_a73de021c8d134cedbbdc205d4fe36fc5"></a>

```c
void(* up )(struct ppp_fsm *fsm)
```

相关声明：[up](#aa1ca37605ab7934c16a5260d531efa00)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

有限状态机（FSM）进入 `OPENED` 状态。

<a id="r_a534695f366ccfc3bfec2bf511dff6974"></a>

```c
void(* down )(struct ppp_fsm *fsm)
```

相关声明：[down](#a2ba52396156dd1ec63d67dc6ae0a2d5a)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

有限状态机（FSM）离开 `OPENED` 状态。

<a id="r_a4f3d2c7a116d37bdbf06fe55e56a772f"></a>

```c
void(* starting )(struct ppp_fsm *fsm)
```

相关声明：[starting](#ad7f2d5d09acb298d29ebc60b4f748478)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

启动此协议。

<a id="r_ad540a5d2bb1ea5d5ed72134ff4c6dc3b"></a>

```c
void(* finished )(struct ppp_fsm *fsm)
```

相关声明：[finished](#aecdcdfa2f7264c7b1b2202a23327fa3b)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

退出此协议。

<a id="r_a06f90c4da059fcfc42ddfd3177d67d0c"></a>

```c
void(* proto_reject )(struct ppp_fsm *fsm)
```

相关声明：[proto_reject](#ae4f68c11709ab03445b853c12c11c787)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

已收到协议拒绝（Protocol-Reject）消息。

<a id="r_a22b0cb2233fb18fa66c2d9edcefd457f"></a>

```c
void(* retransmit )(struct ppp_fsm *fsm)
```

相关声明：[retransmit](#ae0c0b33d5e51a01a63b5afbf5012c0f5)、[ppp_fsm](P044_ppp_fsm_结构体.md)。

重传（Retransmit）。

<a id="r_af42387b021c5a3f2ac998d8a2a2ef85a"></a>

```c
enum net_verdict(* proto_extension )(struct ppp_fsm *fsm, enum ppp_packet_type code, uint8_t id, struct net_pkt *pkt)
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[proto_extension](#aa302cfe79c73fe081d2642cf54d1d3cf)、[ppp_fsm](P044_ppp_fsm_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a844c8747b299d3614e5ccff892b45d5c)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

PPP 无法识别的任何代码，都会传给此有限状态机作进一步处理。

<a id="r_a0e3cd20db2e06d6d0e85478c013e36db"></a>

```c
} cb
```

相关声明：[cb](#a0e3cd20db2e06d6d0e85478c013e36db)。

有限状态机（FSM）回调。

```c
struct {
```

<a id="r_a33a6831e4040f132374611abbd2b783b"></a>

```c
const struct ppp_my_option_info * info
```

相关声明：[info](#a117a5df8fed62b57a59580a2513fc1c3)。

选项信息。

<a id="r_a9652d4802b764938429629e0367ce9c2"></a>

```c
struct ppp_my_option_data * data
```

相关声明：[data](#a64330e89597eac2b8b841d0f95389473)。

选项协商（negotiation）数据。

<a id="r_afd3a4a9ce1535496cd928f0ddabd65af"></a>

```c
size_t count
```

相关声明：[count](#a7e125f9011a9377d18dc523b1f84964f)。

已协商选项的数量。

<a id="r_a39a7d8b02a0c905ea27565445295c4f2"></a>

```c
} my_options
```

相关声明：[my_options](#a39a7d8b02a0c905ea27565445295c4f2)。

本端选项。

<a id="r_a489c2d992e03e126ba2d1bbfe7a71b85"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a489c2d992e03e126ba2d1bbfe7a71b85)。

选项位（Option bits）。

<a id="r_a31d84f3fa6246bd70d664dbae6845c4b"></a>

```c
uint32_t retransmits
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[retransmits](#a31d84f3fa6246bd70d664dbae6845c4b)。

剩余重传次数。

<a id="r_a0a0523fe16fe45a756615b62e8673828"></a>

```c
uint32_t nack_loops
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[nack_loops](#a0a0523fe16fe45a756615b62e8673828)。

自上次确认（ACK）以来的否定确认（NACK）循环次数。

<a id="r_a55c0fe60eb84f33386ec90691ee0f707"></a>

```c
uint32_t recv_nack_loops
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_nack_loops](#a55c0fe60eb84f33386ec90691ee0f707)。

已收到的 NACK 数量。

<a id="r_a054fd1e61e667072a552eadf54634ffc"></a>

```c
char terminate_reason [32]
```

相关声明：[terminate_reason](#a054fd1e61e667072a552eadf54634ffc)。

关闭协议的原因。

<a id="r_a2032a922d2e356155c5a4c86cf48ff3d"></a>

```c
uint16_t protocol
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[protocol](#a2032a922d2e356155c5a4c86cf48ff3d)。

此有限状态机对应的 PPP 协议编号。

<a id="r_ab955d11b75231e94ec1613d5c8c027e1"></a>

```c
enum ppp_state state
```

相关声明：[state](#ab955d11b75231e94ec1613d5c8c027e1)。

PPP 链路的当前状态。

<a id="r_a9192c71ef82436c519ac3b8ccd38a089"></a>

```c
const char * name
```

相关声明：[name](#a9192c71ef82436c519ac3b8ccd38a089)。

此有限状态机对应的协议或协议层名称，用于调试。

<a id="r_a844c8747b299d3614e5ccff892b45d5c"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a844c8747b299d3614e5ccff892b45d5c)。

当前 ID。

<a id="r_a8fe52ffe2a17c03ff0432e36c9d43578"></a>

```c
uint8_t req_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[req_id](#a8fe52ffe2a17c03ff0432e36c9d43578)。

当前请求 ID。

<a id="r_a42777bc7c5f904cbac6bb0b16615fb02"></a>

```c
uint8_t ack_received: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ack_received](#a42777bc7c5f904cbac6bb0b16615fb02)。

已收到针对请求的有效 Ack、Nack 或 Reject 响应。

## 44.2\_详细说明（Detailed Documentation）

<a id="a42777bc7c5f904cbac6bb0b16615fb02"></a>

### `ack_received`

```c
uint8_t ppp_fsm::ack_received
```

已收到针对请求的有效 Ack、Nack 或 Reject 响应。

<a id="a0e3cd20db2e06d6d0e85478c013e36db"></a>

### `[struct]`

```c
struct { ... } ppp_fsm::cb
```

有限状态机（FSM）回调。

<a id="a42bb4a40d88893d461d93202c4ad8e2a"></a>

### `config_info_ack`

```c
int(* ppp_fsm::config_info_ack) (struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length)
```

确认配置信息（Acknowledge Configuration Information）。

<a id="a5a3c96319ec906968701c3eb72ce3d24"></a>

### `config_info_add`

```c
struct net_pkt *(* ppp_fsm::config_info_add) (struct ppp_fsm *fsm)
```

添加配置信息（Add Configuration Information）。

<a id="a099cc834fc5e2d062ee4410a1de729c2"></a>

### `config_info_len`

```c
int(* ppp_fsm::config_info_len) (struct ppp_fsm *fsm)
```

配置信息长度（Length of Configuration Information）。

<a id="ad0967edee7fee72368732876ca6bc5e7"></a>

### `config_info_nack`

```c
int(* ppp_fsm::config_info_nack) (struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length, bool rejected)
```

否定确认配置信息（Negative Acknowledge Configuration Information）。

<a id="a90dad2f780b4573559c76e6a67e44f4c"></a>

### `config_info_rej`

```c
int(* ppp_fsm::config_info_rej) (struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length)
```

拒绝配置信息（Reject Configuration Information）。

<a id="ab430e0240f35718f6eaf8f9052a4edde"></a>

### `config_info_req`

```c
int(* ppp_fsm::config_info_req) (struct ppp_fsm *fsm, struct net_pkt *pkt, uint16_t length, struct net_pkt *ret_pkt)
```

请求对端配置信息（Request peer's Configuration Information）。

<a id="afb0296b0d8e9b60594781cfd5f8acee3"></a>

### `config_info_reset`

```c
void(* ppp_fsm::config_info_reset) (struct ppp_fsm *fsm)
```

重置配置信息（Reset Configuration Information）。

<a id="a7e125f9011a9377d18dc523b1f84964f"></a>

### `count`

```c
size_t ppp_fsm::count
```

已协商选项的数量。

<a id="a64330e89597eac2b8b841d0f95389473"></a>

### `data`

```c
struct ppp_my_option_data* ppp_fsm::data
```

选项协商（negotiation）数据。

<a id="a2ba52396156dd1ec63d67dc6ae0a2d5a"></a>

### `down`

```c
void(* ppp_fsm::down) (struct ppp_fsm *fsm)
```

有限状态机（FSM）离开 `OPENED` 状态。

<a id="aecdcdfa2f7264c7b1b2202a23327fa3b"></a>

### `finished`

```c
void(* ppp_fsm::finished) (struct ppp_fsm *fsm)
```

退出此协议。

<a id="a489c2d992e03e126ba2d1bbfe7a71b85"></a>

### `flags`

```c
uint32_t ppp_fsm::flags
```

选项位（Option bits）。

<a id="a844c8747b299d3614e5ccff892b45d5c"></a>

### `id`

```c
uint8_t ppp_fsm::id
```

当前 ID。

<a id="a117a5df8fed62b57a59580a2513fc1c3"></a>

### `info`

```c
const struct ppp_my_option_info* ppp_fsm::info
```

选项信息。

<a id="a39a7d8b02a0c905ea27565445295c4f2"></a>

### `[struct]`

```c
struct { ... } ppp_fsm::my_options
```

本端选项。

<a id="a0a0523fe16fe45a756615b62e8673828"></a>

### `nack_loops`

```c
uint32_t ppp_fsm::nack_loops
```

自上次确认（ACK）以来的否定确认（NACK）循环次数。

<a id="a9192c71ef82436c519ac3b8ccd38a089"></a>

### `name`

```c
const char* ppp_fsm::name
```

此有限状态机对应的协议或协议层名称，用于调试。

<a id="aa302cfe79c73fe081d2642cf54d1d3cf"></a>

### `proto_extension`

```c
enum net_verdict(* ppp_fsm::proto_extension) (struct ppp_fsm *fsm, enum ppp_packet_type code, uint8_t id, struct net_pkt *pkt)
```

PPP 无法识别的任何代码，都会传给此有限状态机作进一步处理。

<a id="ae4f68c11709ab03445b853c12c11c787"></a>

### `proto_reject`

```c
void(* ppp_fsm::proto_reject) (struct ppp_fsm *fsm)
```

已收到协议拒绝（Protocol-Reject）消息。

<a id="a2032a922d2e356155c5a4c86cf48ff3d"></a>

### `protocol`

```c
uint16_t ppp_fsm::protocol
```

此有限状态机对应的 PPP 协议编号。

<a id="a55c0fe60eb84f33386ec90691ee0f707"></a>

### `recv_nack_loops`

```c
uint32_t ppp_fsm::recv_nack_loops
```

已收到的 NACK 数量。

<a id="a8fe52ffe2a17c03ff0432e36c9d43578"></a>

### `req_id`

```c
uint8_t ppp_fsm::req_id
```

当前请求 ID。

<a id="ae0c0b33d5e51a01a63b5afbf5012c0f5"></a>

### `retransmit`

```c
void(* ppp_fsm::retransmit) (struct ppp_fsm *fsm)
```

重传（Retransmit）。

<a id="a31d84f3fa6246bd70d664dbae6845c4b"></a>

### `retransmits`

```c
uint32_t ppp_fsm::retransmits
```

剩余重传次数。

<a id="ad7f2d5d09acb298d29ebc60b4f748478"></a>

### `starting`

```c
void(* ppp_fsm::starting) (struct ppp_fsm *fsm)
```

启动此协议。

<a id="ab955d11b75231e94ec1613d5c8c027e1"></a>

### `state`

```c
enum ppp_state ppp_fsm::state
```

PPP 链路的当前状态。

<a id="a054fd1e61e667072a552eadf54634ffc"></a>

### `terminate_reason`

```c
char ppp_fsm::terminate_reason[32]
```

关闭协议的原因。

<a id="ae033ee41d66ec568dc4244115730114a"></a>

### `timer`

```c
struct k_work_delayable ppp_fsm::timer
```

超时定时器（Timeout Timer）。

<a id="aa1ca37605ab7934c16a5260d531efa00"></a>

### `up`

```c
void(* ppp_fsm::up) (struct ppp_fsm *fsm)
```

有限状态机（FSM）进入 `OPENED` 状态。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [ppp_fsm](P044_ppp_fsm_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_ppp_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_prometheus_collector_结构体.md)
