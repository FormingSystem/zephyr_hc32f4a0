---
id: learning.zephyr-docs.platform-security-model-reference.page-70
title: tisci_msg_rm_udmap_rx_ch_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__rm__udmap__rx__ch__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_tisci\_msg\_rm\_udmap\_rx\_ch\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__rm__udmap__rx__ch__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置Navigator子系统的统一DMA（UDMAP）接收通道。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

配置 Navigator 子系统的统一 DMA（UDMAP）接收通道。配置 Navigator 子系统 UDMAP 接收通道寄存器。参见 `tisci_msg_rm_udmap_rx_ch_cfg_req`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a88fa4f4bf94a290a035419a65054b544"></a>

```c
uint32_t valid_params
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_params](#a88fa4f4bf94a290a035419a65054b544)。

<a id="r_a691a478fa65af24279638789433dca6f"></a>

```c
uint16_t nav_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nav_id](#a691a478fa65af24279638789433dca6f)。

<a id="r_a459ca9cb93410be5747595a57d88c7ed"></a>

```c
uint16_t index
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[index](#a459ca9cb93410be5747595a57d88c7ed)。

<a id="r_ad57a6d0dca932c95cff2a4675dc72990"></a>

```c
uint16_t rx_fetch_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_fetch_size](#ad57a6d0dca932c95cff2a4675dc72990)。

<a id="r_a554db2ab8742b2f15a6c7531638a6d74"></a>

```c
uint16_t rxcq_qnum
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rxcq_qnum](#a554db2ab8742b2f15a6c7531638a6d74)。

<a id="r_a03ec736938d7b3eb05fcd56c62fd736a"></a>

```c
uint8_t rx_priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_priority](#a03ec736938d7b3eb05fcd56c62fd736a)。

<a id="r_a54f4136011d83df5441004dde0d5e696"></a>

```c
uint8_t rx_qos
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_qos](#a54f4136011d83df5441004dde0d5e696)。

<a id="r_a9782a0a412413087ecf669beed77ff77"></a>

```c
uint8_t rx_orderid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_orderid](#a9782a0a412413087ecf669beed77ff77)。

<a id="r_a4e9720567203889d41fdccb769d56025"></a>

```c
uint8_t rx_sched_priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_sched_priority](#a4e9720567203889d41fdccb769d56025)。

<a id="r_abde08f01f02f26e1538cd82d9e87b19a"></a>

```c
uint16_t flowid_start
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flowid_start](#abde08f01f02f26e1538cd82d9e87b19a)。

<a id="r_ac10643f49f4d685af2bf14bb7b9b90f0"></a>

```c
uint16_t flowid_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flowid_cnt](#ac10643f49f4d685af2bf14bb7b9b90f0)。

<a id="r_ad008f77af3d4edbfeedb863ee2f8dcd0"></a>

```c
uint8_t rx_pause_on_err
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_pause_on_err](#ad008f77af3d4edbfeedb863ee2f8dcd0)。

<a id="r_a7a36a9e37b22229c6ec90528aa7f9a9c"></a>

```c
uint8_t rx_atype
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_atype](#a7a36a9e37b22229c6ec90528aa7f9a9c)。

<a id="r_aecf4e3eaaa8b8c604504eb525d3e1a5f"></a>

```c
uint8_t rx_chan_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_chan_type](#aecf4e3eaaa8b8c604504eb525d3e1a5f)。

<a id="r_ab1245dc9783e74cd3cb1fcb648714e76"></a>

```c
uint8_t rx_ignore_short
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_ignore_short](#ab1245dc9783e74cd3cb1fcb648714e76)。

<a id="r_a8e9b939089204b70469afedcb6c5ad8c"></a>

```c
uint8_t rx_ignore_long
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_ignore_long](#a8e9b939089204b70469afedcb6c5ad8c)。

<a id="r_a57c0675af1fdefd1c270d11183fa77d6"></a>

```c
uint8_t rx_burst_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_burst_size](#a57c0675af1fdefd1c270d11183fa77d6)。

## 70.2\_详细说明（Detailed Documentation）

<a id="ac10643f49f4d685af2bf14bb7b9b90f0"></a>

### `flowid_cnt`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::flowid_cnt
```

<a id="abde08f01f02f26e1538cd82d9e87b19a"></a>

### `flowid_start`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::flowid_start
```

<a id="a459ca9cb93410be5747595a57d88c7ed"></a>

### `index`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::index
```

<a id="a691a478fa65af24279638789433dca6f"></a>

### `nav_id`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::nav_id
```

<a id="a7a36a9e37b22229c6ec90528aa7f9a9c"></a>

### `rx_atype`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_atype
```

<a id="a57c0675af1fdefd1c270d11183fa77d6"></a>

### `rx_burst_size`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_burst_size
```

<a id="aecf4e3eaaa8b8c604504eb525d3e1a5f"></a>

### `rx_chan_type`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_chan_type
```

<a id="ad57a6d0dca932c95cff2a4675dc72990"></a>

### `rx_fetch_size`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::rx_fetch_size
```

<a id="a8e9b939089204b70469afedcb6c5ad8c"></a>

### `rx_ignore_long`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_ignore_long
```

<a id="ab1245dc9783e74cd3cb1fcb648714e76"></a>

### `rx_ignore_short`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_ignore_short
```

<a id="a9782a0a412413087ecf669beed77ff77"></a>

### `rx_orderid`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_orderid
```

<a id="ad008f77af3d4edbfeedb863ee2f8dcd0"></a>

### `rx_pause_on_err`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_pause_on_err
```

<a id="a03ec736938d7b3eb05fcd56c62fd736a"></a>

### `rx_priority`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_priority
```

<a id="a54f4136011d83df5441004dde0d5e696"></a>

### `rx_qos`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_qos
```

<a id="a4e9720567203889d41fdccb769d56025"></a>

### `rx_sched_priority`

```c
uint8_t tisci_msg_rm_udmap_rx_ch_cfg::rx_sched_priority
```

<a id="a554db2ab8742b2f15a6c7531638a6d74"></a>

### `rxcq_qnum`

```c
uint16_t tisci_msg_rm_udmap_rx_ch_cfg::rxcq_qnum
```

<a id="a88fa4f4bf94a290a035419a65054b544"></a>

### `valid_params`

```c
uint32_t tisci_msg_rm_udmap_rx_ch_cfg::valid_params
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_tisci_msg_fwl_region_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md)
