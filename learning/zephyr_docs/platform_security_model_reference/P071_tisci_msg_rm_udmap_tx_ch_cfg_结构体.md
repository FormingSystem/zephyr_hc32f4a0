---
id: learning.zephyr-docs.platform-security-model-reference.page-71
title: tisci_msg_rm_udmap_tx_ch_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__rm__udmap__tx__ch__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_tisci\_msg\_rm\_udmap\_tx\_ch\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__rm__udmap__tx__ch__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

配置Navigator子系统的统一DMA（UDMAP）发送通道。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

配置 Navigator 子系统的统一 DMA（UDMAP）发送通道。配置 Navigator 子系统 UDMAP 发送通道寄存器。参见 `tisci_msg_rm_udmap_tx_ch_cfg_req`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_acb243dd0b94ab38fa50ddd14a758b33a"></a>

```c
uint32_t valid_params
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_params](#acb243dd0b94ab38fa50ddd14a758b33a)。

<a id="r_a646845b965fee520329a118ade711f02"></a>

```c
uint16_t nav_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nav_id](#a646845b965fee520329a118ade711f02)。

<a id="r_ab8327c9b3896c8294f47349572546e70"></a>

```c
uint16_t index
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[index](#ab8327c9b3896c8294f47349572546e70)。

<a id="r_ad255f2c020bfc237f5f22a747e68c1b8"></a>

```c
uint8_t tx_pause_on_err
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_pause_on_err](#ad255f2c020bfc237f5f22a747e68c1b8)。

<a id="r_a9d298e2ae456dcad3cbfdce595f0655c"></a>

```c
uint8_t tx_filt_einfo
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_filt_einfo](#a9d298e2ae456dcad3cbfdce595f0655c)。

<a id="r_ab9a869848d253d09f9fafc91dc8958cc"></a>

```c
uint8_t tx_filt_pswords
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_filt_pswords](#ab9a869848d253d09f9fafc91dc8958cc)。

<a id="r_a75147fe8091db6c41050ded22c9eefa3"></a>

```c
uint8_t tx_atype
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_atype](#a75147fe8091db6c41050ded22c9eefa3)。

<a id="r_a14b9ea920df0ff044bd9cf45c2084f3a"></a>

```c
uint8_t tx_chan_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_chan_type](#a14b9ea920df0ff044bd9cf45c2084f3a)。

<a id="r_aaa18a6837a0271781164a353ce729623"></a>

```c
uint8_t tx_supr_tdpkt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_supr_tdpkt](#aaa18a6837a0271781164a353ce729623)。

<a id="r_afd02dd108fd620f1bc9d66fac5a3e775"></a>

```c
uint16_t tx_fetch_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_fetch_size](#afd02dd108fd620f1bc9d66fac5a3e775)。

<a id="r_a90a701c601691c79cd37192fac02d052"></a>

```c
uint8_t tx_credit_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_credit_count](#a90a701c601691c79cd37192fac02d052)。

<a id="r_a89f3ac8683240274b5bbc635e08b659f"></a>

```c
uint16_t txcq_qnum
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[txcq_qnum](#a89f3ac8683240274b5bbc635e08b659f)。

<a id="r_aeaf51ae045dbc4079c02d61f13e487ed"></a>

```c
uint8_t tx_priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_priority](#aeaf51ae045dbc4079c02d61f13e487ed)。

<a id="r_af377d65e1fb43ed7fceda8a0665605d0"></a>

```c
uint8_t tx_qos
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_qos](#af377d65e1fb43ed7fceda8a0665605d0)。

<a id="r_ada34a3a63d1ed339a86804f906d4dbc5"></a>

```c
uint8_t tx_orderid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_orderid](#ada34a3a63d1ed339a86804f906d4dbc5)。

<a id="r_ad8aec84ccd12e9f02c4cafac7eadb4a4"></a>

```c
uint16_t fdepth
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fdepth](#ad8aec84ccd12e9f02c4cafac7eadb4a4)。

<a id="r_a01334fae8a1e94ffbbba28d9c59ed0b1"></a>

```c
uint8_t tx_sched_priority
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_sched_priority](#a01334fae8a1e94ffbbba28d9c59ed0b1)。

<a id="r_a7e0bfdb950b1b285ddc0e58282bc224b"></a>

```c
uint8_t tx_burst_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_burst_size](#a7e0bfdb950b1b285ddc0e58282bc224b)。

<a id="r_ab36b40f8989fa7cdc5419bc0e9dd5a68"></a>

```c
uint8_t tx_tdtype
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_tdtype](#ab36b40f8989fa7cdc5419bc0e9dd5a68)。

<a id="r_a37b6f2565ccdf51fcc09801a72fde7e4"></a>

```c
uint8_t extended_ch_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[extended_ch_type](#a37b6f2565ccdf51fcc09801a72fde7e4)。

## 71.2\_详细说明（Detailed Documentation）

<a id="a37b6f2565ccdf51fcc09801a72fde7e4"></a>

### `extended_ch_type`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::extended_ch_type
```

<a id="ad8aec84ccd12e9f02c4cafac7eadb4a4"></a>

### `fdepth`

```c
uint16_t tisci_msg_rm_udmap_tx_ch_cfg::fdepth
```

<a id="ab8327c9b3896c8294f47349572546e70"></a>

### `index`

```c
uint16_t tisci_msg_rm_udmap_tx_ch_cfg::index
```

<a id="a646845b965fee520329a118ade711f02"></a>

### `nav_id`

```c
uint16_t tisci_msg_rm_udmap_tx_ch_cfg::nav_id
```

<a id="a75147fe8091db6c41050ded22c9eefa3"></a>

### `tx_atype`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_atype
```

<a id="a7e0bfdb950b1b285ddc0e58282bc224b"></a>

### `tx_burst_size`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_burst_size
```

<a id="a14b9ea920df0ff044bd9cf45c2084f3a"></a>

### `tx_chan_type`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_chan_type
```

<a id="a90a701c601691c79cd37192fac02d052"></a>

### `tx_credit_count`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_credit_count
```

<a id="afd02dd108fd620f1bc9d66fac5a3e775"></a>

### `tx_fetch_size`

```c
uint16_t tisci_msg_rm_udmap_tx_ch_cfg::tx_fetch_size
```

<a id="a9d298e2ae456dcad3cbfdce595f0655c"></a>

### `tx_filt_einfo`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_filt_einfo
```

<a id="ab9a869848d253d09f9fafc91dc8958cc"></a>

### `tx_filt_pswords`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_filt_pswords
```

<a id="ada34a3a63d1ed339a86804f906d4dbc5"></a>

### `tx_orderid`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_orderid
```

<a id="ad255f2c020bfc237f5f22a747e68c1b8"></a>

### `tx_pause_on_err`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_pause_on_err
```

<a id="aeaf51ae045dbc4079c02d61f13e487ed"></a>

### `tx_priority`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_priority
```

<a id="af377d65e1fb43ed7fceda8a0665605d0"></a>

### `tx_qos`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_qos
```

<a id="a01334fae8a1e94ffbbba28d9c59ed0b1"></a>

### `tx_sched_priority`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_sched_priority
```

<a id="aaa18a6837a0271781164a353ce729623"></a>

### `tx_supr_tdpkt`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_supr_tdpkt
```

<a id="ab36b40f8989fa7cdc5419bc0e9dd5a68"></a>

### `tx_tdtype`

```c
uint8_t tisci_msg_rm_udmap_tx_ch_cfg::tx_tdtype
```

<a id="a89f3ac8683240274b5bbc635e08b659f"></a>

### `txcq_qnum`

```c
uint16_t tisci_msg_rm_udmap_tx_ch_cfg::txcq_qnum
```

<a id="acb243dd0b94ab38fa50ddd14a758b33a"></a>

### `valid_params`

```c
uint32_t tisci_msg_rm_udmap_tx_ch_cfg::valid_params
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_tisci_version_info_结构体.md)
