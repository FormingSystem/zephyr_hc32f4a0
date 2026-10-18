---
id: learning.zephyr-docs.api-file-modem-network-reference.page-7
title: zephyr__drivers__firmware__tisci__tisci.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_firmware\_\_tisci\_\_tisci.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI系统控制接口（TISCI）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

TI系统控制接口（TISCI）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_tisci_5Fversion_5Finfo"></a>

```c
struct tisci_version_info
```

相关声明：[tisci_version_info](../platform_security_model_reference/P072_tisci_version_info_结构体.md)。

版本信息（Version Information）结构。

<a id="r_tisci_5Fmsg_5Ffwl_5Fregion"></a>

```c
struct tisci_msg_fwl_region
```

相关声明：[tisci_msg_fwl_region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md)。

<a id="r_tisci_5Fmsg_5Ffwl_5Fowner"></a>

```c
struct tisci_msg_fwl_owner
```

相关声明：[tisci_msg_fwl_owner](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md)。

防火墙所有者变更（Firewall Owner Change）的请求和响应。

<a id="r_tisci_5Fmsg_5Frm_5Fudmap_5Ftx_5Fch_5Fcfg"></a>

```c
struct tisci_msg_rm_udmap_tx_ch_cfg
```

相关声明：[tisci_msg_rm_udmap_tx_ch_cfg](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md)。

配置Navigator子系统的统一DMA（UDMAP）发送通道。

<a id="r_tisci_5Fmsg_5Frm_5Fudmap_5Frx_5Fch_5Fcfg"></a>

```c
struct tisci_msg_rm_udmap_rx_ch_cfg
```

相关声明：[tisci_msg_rm_udmap_rx_ch_cfg](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md)。

配置Navigator子系统的统一DMA（UDMAP）接收通道。

<a id="r_tisci_5Firq_5Fset_5Freq"></a>

```c
struct tisci_irq_set_req
```

相关声明：[tisci_irq_set_req](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md)。

设置中断路由（Interrupt Route）的请求。

<a id="r_tisci_5Firq_5Frelease_5Freq"></a>

```c
struct tisci_irq_release_req
```

相关声明：[tisci_irq_release_req](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md)。

释放中断外设资源（Interrupt Peripheral Resources）的请求。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_a396f8869a1aee7aa1b88a039a17746bf"></a>

```c
#define MAILBOX_MBOX_SIZE 60
```

相关声明：[MAILBOX_MBOX_SIZE](#a396f8869a1aee7aa1b88a039a17746bf)。

<a id="r_a736e0c626ee9d1df858ce5936bf4029e"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_EINFO_VALID BIT(9)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_EINFO_VALID](#a736e0c626ee9d1df858ce5936bf4029e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6db1d6169cc2def41e73ce4c22fa118e"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_PSWORDS_VALID BIT(10)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_PSWORDS_VALID](#a6db1d6169cc2def41e73ce4c22fa118e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a64195889325d54d493923b95620b1550"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_SUPR_TDPKT_VALID BIT(11)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_SUPR_TDPKT_VALID](#a64195889325d54d493923b95620b1550)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1110504d079ae51a526ed80144560b27"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_CREDIT_COUNT_VALID BIT(12)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_CREDIT_COUNT_VALID](#a1110504d079ae51a526ed80144560b27)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af8dbd5c7af94ec3690012458d35f2456"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FDEPTH_VALID BIT(13)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FDEPTH_VALID](#af8dbd5c7af94ec3690012458d35f2456)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4de2b535f4d2548218dde6c2dddc9448"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_TDTYPE_VALID BIT(15)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_TX_TDTYPE_VALID](#a4de2b535f4d2548218dde6c2dddc9448)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abb692a88d05498a4c0dd5e69857cda92"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_EXTENDED_CH_TYPE_VALID BIT(16)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_EXTENDED_CH_TYPE_VALID](#abb692a88d05498a4c0dd5e69857cda92)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae0c03a2c76f884f37f472b081d0dd028"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_START_VALID BIT(9)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_START_VALID](#ae0c03a2c76f884f37f472b081d0dd028)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a04febde272953c690f94d44db18663f7"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_CNT_VALID BIT(10)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_CNT_VALID](#a04febde272953c690f94d44db18663f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a512091ff6dff198c2801a8f51fe18755"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_SHORT_VALID BIT(11)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_SHORT_VALID](#a512091ff6dff198c2801a8f51fe18755)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a818ed2617f42b219d3e3aed2a46ed7d8"></a>

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_LONG_VALID BIT(12)
```

相关声明：[TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_LONG_VALID](#a818ed2617f42b219d3e3aed2a46ed7d8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae309074218959da90a5978304c34e916"></a>

```c
#define TISCI_MSG_VALUE_RM_DST_ID_VALID (1u << 0u)
```

相关声明：[TISCI_MSG_VALUE_RM_DST_ID_VALID](#ae309074218959da90a5978304c34e916)。

<a id="r_a69aa4a4b3a5e99a86adbc6a0ccf74560"></a>

```c
#define TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID (1u << 1u)
```

相关声明：[TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID](#a69aa4a4b3a5e99a86adbc6a0ccf74560)。

<a id="r_abf34b43187cdc7ea4b68ee151816d97a"></a>

```c
#define TISCI_MSG_VALUE_RM_IA_ID_VALID (1u << 2u)
```

相关声明：[TISCI_MSG_VALUE_RM_IA_ID_VALID](#abf34b43187cdc7ea4b68ee151816d97a)。

<a id="r_a334a7f7a6fd37286c5635f1cfe2d061f"></a>

```c
#define TISCI_MSG_VALUE_RM_VINT_VALID (1u << 3u)
```

相关声明：[TISCI_MSG_VALUE_RM_VINT_VALID](#a334a7f7a6fd37286c5635f1cfe2d061f)。

<a id="r_aad5b430c5924f794b35cfb7c9830b48b"></a>

```c
#define TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID (1u << 4u)
```

相关声明：[TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID](#aad5b430c5924f794b35cfb7c9830b48b)。

<a id="r_ae2c0b651fc864d6904bfef4fdacb2aea"></a>

```c
#define TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID (1u << 5u)
```

相关声明：[TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID](#ae2c0b651fc864d6904bfef4fdacb2aea)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_aea0b9addbd3cfcb2be691f0801128fe1"></a>

```c
int tisci_cmd_get_revision (const struct device *dev, struct tisci_version_info *ver)
```

相关声明：[tisci_cmd_get_revision](#aea0b9addbd3cfcb2be691f0801128fe1)、[device](../device_reference/P002_设备对象结构.md)、[tisci_version_info](../platform_security_model_reference/P072_tisci_version_info_结构体.md)。

获取 TI 系统控制接口（SCI）固件的修订版本信息（Revision Information）。

<a id="r_a3f8128fa6c8c6f10bb7e302e6e9cfeaf"></a>

```c
int tisci_cmd_get_clock_state (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint8_t *programmed_state, uint8_t *current_state)
```

相关声明：[tisci_cmd_get_clock_state](#a3f8128fa6c8c6f10bb7e302e6e9cfeaf)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取时钟状态（Clock State）。

<a id="r_a086d96bed3d789bf303f56405a791aa6"></a>

```c
int tisci_set_clock_state (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint32_t flags, uint8_t state)
```

相关声明：[tisci_set_clock_state](#a086d96bed3d789bf303f56405a791aa6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置时钟状态（Clock State）。

<a id="r_a7f0bafa6005d46d2786db590a27add25"></a>

```c
int tisci_cmd_clk_is_on (const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool *req_state, bool *curr_state)
```

相关声明：[tisci_cmd_clk_is_on](#a7f0bafa6005d46d2786db590a27add25)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查时钟是否开启（ON）。

<a id="r_a20276a83e2037db6895085770353a194"></a>

```c
int tisci_cmd_clk_is_off (const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool *req_state, bool *curr_state)
```

相关声明：[tisci_cmd_clk_is_off](#a20276a83e2037db6895085770353a194)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查时钟是否关闭（OFF）。

<a id="r_aaebb0012c291ded1b9303d634b1bb245"></a>

```c
int tisci_cmd_clk_is_auto (const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool *req_state)
```

相关声明：[tisci_cmd_clk_is_auto](#aaebb0012c291ded1b9303d634b1bb245)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查时钟是否由系统自动管理（Auto-managed）。

<a id="r_a5c69f5f12b79a0b37a1f704624106960"></a>

```c
int tisci_cmd_clk_get_freq (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint64_t *freq)
```

相关声明：[tisci_cmd_clk_get_freq](#a5c69f5f12b79a0b37a1f704624106960)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取时钟的当前频率（Current Frequency）。

<a id="r_ad3563b7ec2fa13eb4b1faa564062ae12"></a>

```c
int tisci_cmd_clk_set_freq (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint64_t min_freq, uint64_t target_freq, uint64_t max_freq)
```

相关声明：[tisci_cmd_clk_set_freq](#ad3563b7ec2fa13eb4b1faa564062ae12)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

为时钟设置频率（Frequency）。

<a id="r_a9801b388e5dc60f10aa624040cb8bfe2"></a>

```c
int tisci_cmd_clk_get_match_freq (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint64_t min_freq, uint64_t target_freq, uint64_t max_freq, uint64_t *match_freq)
```

相关声明：[tisci_cmd_clk_get_match_freq](#a9801b388e5dc60f10aa624040cb8bfe2)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取符合要求的时钟频率（Matching Frequency）。

<a id="r_a6ad9804cf3e23246955bcab1e98aecdb"></a>

```c
int tisci_cmd_clk_set_parent (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint8_t parent_id)
```

相关声明：[tisci_cmd_clk_set_parent](#a6ad9804cf3e23246955bcab1e98aecdb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为时钟设置父时钟（Parent Clock）。

<a id="r_a86e0ed2c8711363dc5ea710b12a303af"></a>

```c
int tisci_cmd_clk_get_parent (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint8_t *parent_id)
```

相关声明：[tisci_cmd_clk_get_parent](#a86e0ed2c8711363dc5ea710b12a303af)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取时钟的父时钟（Parent Clock）。

<a id="r_ae93fb7c70a4f2299415a51b993d36741"></a>

```c
int tisci_cmd_clk_get_num_parents (const struct device *dev, uint32_t dev_id, uint8_t clk_id, uint8_t *num_parents)
```

相关声明：[tisci_cmd_clk_get_num_parents](#ae93fb7c70a4f2299415a51b993d36741)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取时钟的父时钟数量（Number of Parent Clocks）。

<a id="r_ab63106de04e579ba18f34763b3efa8b3"></a>

```c
int tisci_cmd_get_clock (const struct device *dev, uint32_t dev_id, uint8_t clk_id, bool needs_ssc, bool can_change_freq, bool enable_input_term)
```

相关声明：[tisci_cmd_get_clock](#ab63106de04e579ba18f34763b3efa8b3)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

从 TI SCI 获取时钟的控制权（Clock Control）。

<a id="r_a3d39780a18358066ec8f187474c18f71"></a>

```c
int tisci_cmd_idle_clock (const struct device *dev, uint32_t dev_id, uint8_t clk_id)
```

相关声明：[tisci_cmd_idle_clock](#a3d39780a18358066ec8f187474c18f71)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使由 TI SCI 控制的时钟进入空闲状态（Idle）。

<a id="r_ae48c6c78db3f4bee6520c0af66e37e7d"></a>

```c
int tisci_cmd_put_clock (const struct device *dev, uint32_t dev_id, uint8_t clk_id)
```

相关声明：[tisci_cmd_put_clock](#ae48c6c78db3f4bee6520c0af66e37e7d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

释放时钟控制权（Clock Control），将其交回 TI SCI。

<a id="r_a8b6d6f99df32eeba9131ce130ee4f12d"></a>

```c
int tisci_set_device_state (const struct device *dev, uint32_t dev_id, uint32_t flags, uint8_t state)
```

相关声明：[tisci_set_device_state](#a8b6d6f99df32eeba9131ce130ee4f12d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置设备状态（Device State）。

<a id="r_a05f871388f68d9c71620ea43bde1e3ab"></a>

```c
int tisci_set_device_state_no_wait (const struct device *dev, uint32_t dev_id, uint32_t flags, uint8_t state)
```

相关声明：[tisci_set_device_state_no_wait](#a05f871388f68d9c71620ea43bde1e3ab)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置设备状态（Device State），不等待响应（Response）。

<a id="r_ada78c57b3cb24e57a3f6cc155e3a3d09"></a>

```c
int tisci_get_device_state (const struct device *dev, uint32_t dev_id, uint32_t *clcnt, uint32_t *resets, uint8_t *p_state, uint8_t *c_state)
```

相关声明：[tisci_get_device_state](#ada78c57b3cb24e57a3f6cc155e3a3d09)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取设备状态（Device State）。

<a id="r_a4011bbe29370fb581ab2dd0fcaa151db"></a>

```c
int tisci_cmd_get_device (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_get_device](#a4011bbe29370fb581ab2dd0fcaa151db)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

请求对 TISCI 管理的设备进行独占访问（Exclusive Access）。

<a id="r_adc16227f1ec150d0c6cf32442fa3e915"></a>

```c
int tisci_cmd_get_device_exclusive (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_get_device_exclusive](#adc16227f1ec150d0c6cf32442fa3e915)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ab8203c5d0b699ec726a889e7027ae034"></a>

```c
int tisci_cmd_idle_device (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_idle_device](#ab8203c5d0b699ec726a889e7027ae034)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使 TISCI 管理的设备进入空闲状态（Idle）的命令。

<a id="r_aab1720913f75a771e041e2195b9deede"></a>

```c
int tisci_cmd_idle_device_exclusive (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_idle_device_exclusive](#aab1720913f75a771e041e2195b9deede)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a5a7c9ff34ad1ffa87c62fef6b2ac8719"></a>

```c
int tisci_cmd_put_device (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_put_device](#a5a7c9ff34ad1ffa87c62fef6b2ac8719)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

释放 TISCI 管理的设备（Device）的命令。

<a id="r_a4f4072f951c0ebbeb75e8cd2f06b6e8f"></a>

```c
int tisci_cmd_dev_is_valid (const struct device *dev, uint32_t dev_id)
```

相关声明：[tisci_cmd_dev_is_valid](#a4f4072f951c0ebbeb75e8cd2f06b6e8f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查设备标识符（Device ID）是否有效。

<a id="r_a01393f21cb5a88388ce51e36ba1843fc"></a>

```c
int tisci_cmd_dev_get_clcnt (const struct device *dev, uint32_t dev_id, uint32_t *count)
```

相关声明：[tisci_cmd_dev_get_clcnt](#a01393f21cb5a88388ce51e36ba1843fc)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取设备的上下文丢失计数器（Context Loss Counter）。

<a id="r_af9ff6eee5bca675c50c28fbc4af3048c"></a>

```c
int tisci_cmd_dev_is_idle (const struct device *dev, uint32_t dev_id, bool *r_state)
```

相关声明：[tisci_cmd_dev_is_idle](#af9ff6eee5bca675c50c28fbc4af3048c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查设备是否被请求进入空闲状态（Idle）。

<a id="r_a1a441bdad9bfef9a0136f0b737c9c7aa"></a>

```c
int tisci_cmd_dev_is_stop (const struct device *dev, uint32_t dev_id, bool *r_state, bool *curr_state)
```

相关声明：[tisci_cmd_dev_is_stop](#a1a441bdad9bfef9a0136f0b737c9c7aa)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查设备是否被请求停止（Stopped）。

<a id="r_aa7bb463be840666d87a68c1e65496b19"></a>

```c
int tisci_cmd_dev_is_on (const struct device *dev, uint32_t dev_id, bool *r_state, bool *curr_state)
```

相关声明：[tisci_cmd_dev_is_on](#aa7bb463be840666d87a68c1e65496b19)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查设备是否被请求开启（ON）。

<a id="r_a4a3b7acb3098f71b2a9f85fbb318d595"></a>

```c
int tisci_cmd_dev_is_trans (const struct device *dev, uint32_t dev_id, bool *curr_state)
```

相关声明：[tisci_cmd_dev_is_trans](#a4a3b7acb3098f71b2a9f85fbb318d595)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查设备当前是否处于状态转换过程中（Transitioning）。

<a id="r_a94f43ead8c81320f651fa9c0450a2493"></a>

```c
int tisci_cmd_set_device_resets (const struct device *dev, uint32_t dev_id, uint32_t reset_state)
```

相关声明：[tisci_cmd_set_device_resets](#a94f43ead8c81320f651fa9c0450a2493)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

为 TISCI 管理的设备设置复位（Resets）。

<a id="r_a90613df222309651abc1adb2f4d82272"></a>

```c
int tisci_cmd_get_device_resets (const struct device *dev, uint32_t dev_id, uint32_t *reset_state)
```

相关声明：[tisci_cmd_get_device_resets](#a90613df222309651abc1adb2f4d82272)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 TISCI 管理的设备的复位状态（Reset State）。

<a id="r_a8ced32499c14aae81994368d4450422d"></a>

```c
int tisci_get_resource_range (const struct device *dev, uint32_t dev_id, uint8_t subtype, uint8_t s_host, uint16_t *range_start, uint16_t *range_num)
```

相关声明：[tisci_get_resource_range](#a8ced32499c14aae81994368d4450422d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取分配给某个主机（Host）的资源范围（Resource Range）。

<a id="r_ae249d114c60b6b1a76f7de8dab5c3ce1"></a>

```c
int tisci_cmd_get_resource_range (const struct device *dev, uint32_t dev_id, uint8_t subtype, uint16_t *range_start, uint16_t *range_num)
```

相关声明：[tisci_cmd_get_resource_range](#ae249d114c60b6b1a76f7de8dab5c3ce1)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取分配给该主机（Host）的资源范围（Resource Range）。

<a id="r_aa261b08c9141360c5f4f9e50ab151ed5"></a>

```c
int tisci_cmd_get_resource_range_from_shost (const struct device *dev, uint32_t dev_id, uint8_t subtype, uint8_t s_host, uint16_t *range_start, uint16_t *range_num)
```

相关声明：[tisci_cmd_get_resource_range_from_shost](#aa261b08c9141360c5f4f9e50ab151ed5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取分配给指定主机（Host）的资源范围（Resource Range）。

<a id="r_a3181b68860761b0060048a01d71888a8"></a>

```c
int tisci_cmd_proc_request (const struct device *dev, uint8_t proc_id)
```

相关声明：[tisci_cmd_proc_request](#a3181b68860761b0060048a01d71888a8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求物理处理器控制权（Physical Processor Control）的命令。

<a id="r_a2e0e3e88c635a4e6399941696056b8a9"></a>

```c
int tisci_cmd_proc_release (const struct device *dev, uint8_t proc_id)
```

相关声明：[tisci_cmd_proc_release](#a2e0e3e88c635a4e6399941696056b8a9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

释放物理处理器控制权（Physical Processor Control）的命令。

<a id="r_a1acfab0f8fd3b1db050f97aa21d26ce3"></a>

```c
int tisci_cmd_proc_handover (const struct device *dev, uint8_t proc_id, uint8_t host_id)
```

相关声明：[tisci_cmd_proc_handover](#a1acfab0f8fd3b1db050f97aa21d26ce3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将物理处理器控制权（Physical Processor Control）移交给该处理器访问控制列表（Access Control List）中的某个主机（Host）的命令。

<a id="r_a3551276e98c3f03ea4beb9086c3b89c3"></a>

```c
int tisci_cmd_set_proc_boot_cfg (const struct device *dev, uint8_t proc_id, uint64_t bootvector, uint32_t config_flags_set, uint32_t config_flags_clear)
```

相关声明：[tisci_cmd_set_proc_boot_cfg](#a3551276e98c3f03ea4beb9086c3b89c3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置处理器启动配置标志（Processor Boot Configuration Flags）的命令。

<a id="r_aee60c2eb75e6786b91d9dc73c7a7e2c6"></a>

```c
int tisci_cmd_set_proc_boot_ctrl (const struct device *dev, uint8_t proc_id, uint32_t control_flags_set, uint32_t control_flags_clear)
```

相关声明：[tisci_cmd_set_proc_boot_ctrl](#aee60c2eb75e6786b91d9dc73c7a7e2c6)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置处理器启动控制标志（Processor Boot Control Flags）的命令。

<a id="r_aaa3b1c5f5072b40e2eb1c626cb6f6f29"></a>

```c
int tisci_cmd_proc_auth_boot_image (const struct device *dev, uint64_t *image_addr, uint32_t *image_size)
```

相关声明：[tisci_cmd_proc_auth_boot_image](#aaa3b1c5f5072b40e2eb1c626cb6f6f29)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对镜像（Image）进行认证并加载，随后设置处理器配置标志（Processor Configuration Flags）的命令。

<a id="r_a9e057dd13353ccdd7df3b2263ef22940"></a>

```c
int tisci_cmd_get_proc_boot_status (const struct device *dev, uint8_t proc_id, uint64_t *bv, uint32_t *cfg_flags, uint32_t *ctrl_flags, uint32_t *sts_flags)
```

相关声明：[tisci_cmd_get_proc_boot_status](#a9e057dd13353ccdd7df3b2263ef22940)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取处理器启动状态（Processor Boot Status）的命令。

<a id="r_a8a29455ba732efa082c1a72922f46f9e"></a>

```c
int tisci_proc_wait_boot_status_no_wait (const struct device *dev, uint8_t proc_id, uint8_t num_wait_iterations, uint8_t num_match_iterations, uint8_t delay_per_iteration_us, uint8_t delay_before_iterations_us, uint32_t status_flags_1_set_all_wait, uint32_t status_flags_1_set_any_wait, uint32_t status_flags_1_clr_all_wait, uint32_t status_flags_1_clr_any_wait)
```

相关声明：[tisci_proc_wait_boot_status_no_wait](#a8a29455ba732efa082c1a72922f46f9e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

等待处理器启动状态（Processor Boot Status）的辅助函数，不请求也不等待响应（Response）。

<a id="r_a9a80ade10fb08159e3fdfbd85ac8dfbf"></a>

```c
int tisci_cmd_proc_shutdown_no_wait (const struct device *dev, uint8_t proc_id)
```

相关声明：[tisci_cmd_proc_shutdown_no_wait](#a9a80ade10fb08159e3fdfbd85ac8dfbf)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

关闭内核（Core）的命令，不请求也不等待响应（Response）。

<a id="r_ac83cc7874ddc4c42c35e6a9f41e64ee7"></a>

```c
int cmd_set_board_config_using_msg (const struct device *dev, uint16_t msg_type, uint64_t addr, uint32_t size)
```

相关声明：[cmd_set_board_config_using_msg](#ac83cc7874ddc4c42c35e6a9f41e64ee7)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用指定消息类型（Message Type）设置开发板配置（Board Configuration）。

<a id="r_a9110e6b0fd37057ea72c64c8c2067a21"></a>

```c
int tisci_cmd_ring_config (const struct device *dev, uint32_t valid_params, uint16_t nav_id, uint16_t index, uint32_t addr_lo, uint32_t addr_hi, uint32_t count, uint8_t mode, uint8_t size, uint8_t order_id)
```

相关声明：[tisci_cmd_ring_config](#a9110e6b0fd37057ea72c64c8c2067a21)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置环形加速器（RA）的环（Ring）。

<a id="r_aa7b6bef27ce24be4762d28499197a8bd"></a>

```c
int tisci_cmd_sys_reset (const struct device *dev)
```

相关声明：[tisci_cmd_sys_reset](#aa7b6bef27ce24be4762d28499197a8bd)、[device](../device_reference/P002_设备对象结构.md)。

请求系统复位（System Reset）。

<a id="r_a01625817d1a222c2979443413c7d712c"></a>

```c
int tisci_cmd_query_msmc (const struct device *dev, uint64_t *msmc_start, uint64_t *msmc_end)
```

相关声明：[tisci_cmd_query_msmc](#a01625817d1a222c2979443413c7d712c)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

查询可用的 MSMC 内存范围（Memory Range）。

<a id="r_a2a1873dd1b47f7437cfd8adbea2decab"></a>

```c
int tisci_cmd_set_fwl_region (const struct device *dev, const struct tisci_msg_fwl_region *region)
```

相关声明：[tisci_cmd_set_fwl_region](#a2a1873dd1b47f7437cfd8adbea2decab)、[device](../device_reference/P002_设备对象结构.md)、[tisci_msg_fwl_region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md)。

配置防火墙区域（Firewall Region）。

<a id="r_aafb0c859914130228e6c229725f87eca"></a>

```c
int tisci_cmd_get_fwl_region (const struct device *dev, struct tisci_msg_fwl_region *region)
```

相关声明：[tisci_cmd_get_fwl_region](#aafb0c859914130228e6c229725f87eca)、[device](../device_reference/P002_设备对象结构.md)、[tisci_msg_fwl_region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md)。

获取防火墙区域配置（Firewall Region Configuration）。

<a id="r_afe30856eaa98b6f30b11ab99daf1dc91"></a>

```c
int tisci_cmd_change_fwl_owner (const struct device *dev, struct tisci_msg_fwl_owner *owner)
```

相关声明：[tisci_cmd_change_fwl_owner](#afe30856eaa98b6f30b11ab99daf1dc91)、[device](../device_reference/P002_设备对象结构.md)、[tisci_msg_fwl_owner](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md)。

更改防火墙区域所有者（Firewall Region Owner）。

<a id="r_a98a90edf1033e5146c51da785ee29581"></a>

```c
int tisci_cmd_rm_udmap_tx_ch_cfg (const struct device *dev, const struct tisci_msg_rm_udmap_tx_ch_cfg *params)
```

相关声明：[tisci_cmd_rm_udmap_tx_ch_cfg](#a98a90edf1033e5146c51da785ee29581)、[device](../device_reference/P002_设备对象结构.md)、[tisci_msg_rm_udmap_tx_ch_cfg](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md)。

配置 UDMAP 发送通道（Transmit Channel）。

<a id="r_a5217423ca42a90a472777a907864128e"></a>

```c
int tisci_cmd_rm_udmap_rx_ch_cfg (const struct device *dev, const struct tisci_msg_rm_udmap_rx_ch_cfg *params)
```

相关声明：[tisci_cmd_rm_udmap_rx_ch_cfg](#a5217423ca42a90a472777a907864128e)、[device](../device_reference/P002_设备对象结构.md)、[tisci_msg_rm_udmap_rx_ch_cfg](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md)。

配置 UDMAP 接收通道（Receive Channel）。

<a id="r_a64b6aa840b820beed84fc9a21ffde350"></a>

```c
int tisci_cmd_rm_psil_pair (const struct device *dev, uint32_t nav_id, uint32_t src_thread, uint32_t dst_thread)
```

相关声明：[tisci_cmd_rm_psil_pair](#a64b6aa840b820beed84fc9a21ffde350)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）配对。

<a id="r_a61d3ce5732bbd5a25d5d63af5a059666"></a>

```c
int tisci_cmd_rm_psil_unpair (const struct device *dev, uint32_t nav_id, uint32_t src_thread, uint32_t dst_thread)
```

相关声明：[tisci_cmd_rm_psil_unpair](#a61d3ce5732bbd5a25d5d63af5a059666)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

解除 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）的配对。

<a id="r_a0d5c1b5afc2842e38de56c64c62f17fd"></a>

```c
int tisci_cmd_rm_irq_set (const struct device *dev, struct tisci_irq_set_req *req)
```

相关声明：[tisci_cmd_rm_irq_set](#a0d5c1b5afc2842e38de56c64c62f17fd)、[device](../device_reference/P002_设备对象结构.md)、[tisci_irq_set_req](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md)。

设置 Navigator 子系统（Navigator Subsystem）的中断请求（IRQ）。

<a id="r_ac30ac2d3539999418f8b200e7b78d259"></a>

```c
int tisci_cmd_rm_irq_release (const struct device *dev, struct tisci_irq_release_req *req)
```

相关声明：[tisci_cmd_rm_irq_release](#ac30ac2d3539999418f8b200e7b78d259)、[device](../device_reference/P002_设备对象结构.md)、[tisci_irq_release_req](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md)。

释放 Navigator 子系统（Navigator Subsystem）的中断请求（IRQ）。

## 7.4\_详细说明（Detailed Documentation）

<a id="a396f8869a1aee7aa1b88a039a17746bf"></a>

### `MAILBOX_MBOX_SIZE`

```c
#define MAILBOX_MBOX_SIZE 60
```

<a id="a69aa4a4b3a5e99a86adbc6a0ccf74560"></a>

### `TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID`

```c
#define TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID (1u << 1u)
```

<a id="ae309074218959da90a5978304c34e916"></a>

### `TISCI_MSG_VALUE_RM_DST_ID_VALID`

```c
#define TISCI_MSG_VALUE_RM_DST_ID_VALID (1u << 0u)
```

<a id="aad5b430c5924f794b35cfb7c9830b48b"></a>

### `TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID`

```c
#define TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID (1u << 4u)
```

<a id="abf34b43187cdc7ea4b68ee151816d97a"></a>

### `TISCI_MSG_VALUE_RM_IA_ID_VALID`

```c
#define TISCI_MSG_VALUE_RM_IA_ID_VALID (1u << 2u)
```

<a id="abb692a88d05498a4c0dd5e69857cda92"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_EXTENDED_CH_TYPE_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_EXTENDED_CH_TYPE_VALID BIT(16)
```

<a id="a04febde272953c690f94d44db18663f7"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_CNT_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_CNT_VALID BIT(10)
```

<a id="ae0c03a2c76f884f37f472b081d0dd028"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_START_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_FLOWID_START_VALID BIT(9)
```

<a id="a818ed2617f42b219d3e3aed2a46ed7d8"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_LONG_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_LONG_VALID BIT(12)
```

<a id="a512091ff6dff198c2801a8f51fe18755"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_SHORT_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_RX_IGNORE_SHORT_VALID BIT(11)
```

<a id="a1110504d079ae51a526ed80144560b27"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_CREDIT_COUNT_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_CREDIT_COUNT_VALID BIT(12)
```

<a id="af8dbd5c7af94ec3690012458d35f2456"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FDEPTH_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FDEPTH_VALID BIT(13)
```

<a id="a736e0c626ee9d1df858ce5936bf4029e"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_EINFO_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_EINFO_VALID BIT(9)
```

<a id="a6db1d6169cc2def41e73ce4c22fa118e"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_PSWORDS_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_FILT_PSWORDS_VALID BIT(10)
```

<a id="a64195889325d54d493923b95620b1550"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_SUPR_TDPKT_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_SUPR_TDPKT_VALID BIT(11)
```

<a id="a4de2b535f4d2548218dde6c2dddc9448"></a>

### `TISCI_MSG_VALUE_RM_UDMAP_CH_TX_TDTYPE_VALID`

```c
#define TISCI_MSG_VALUE_RM_UDMAP_CH_TX_TDTYPE_VALID BIT(15)
```

<a id="ae2c0b651fc864d6904bfef4fdacb2aea"></a>

### `TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID`

```c
#define TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID (1u << 5u)
```

<a id="a334a7f7a6fd37286c5635f1cfe2d061f"></a>

### `TISCI_MSG_VALUE_RM_VINT_VALID`

```c
#define TISCI_MSG_VALUE_RM_VINT_VALID (1u << 3u)
```

<a id="ac83cc7874ddc4c42c35e6a9f41e64ee7"></a>

### `cmd_set_board_config_using_msg()`

```c
int cmd_set_board_config_using_msg ( const struct device * dev, uint16_t msg_type, uint64_t addr, uint32_t size )
```

使用指定消息类型（Message Type）设置开发板配置（Board Configuration）。

使用指定内存位置（Memory Location）的配置数据，向 TI SCI 固件发送开发板配置消息（Board Configuration Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `msg_type` | 开发板配置（Board Configuration）所用的 TISCI 消息类型（Message Type）。 |
| `addr` | 开发板配置数据（Board Configuration Data）的物理地址（Physical Address）。 |
| `size` | 开发板配置数据（Board Configuration Data）的大小，单位为字节。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="afe30856eaa98b6f30b11ab99daf1dc91"></a>

### `tisci_cmd_change_fwl_owner()`

```c
int tisci_cmd_change_fwl_owner ( const struct device * dev, struct tisci_msg_fwl_owner * owner )
```

更改防火墙区域所有者（Firewall Region Owner）。

更改防火墙区域（Firewall Region）的所有权（Ownership），并获取更新后的所有权信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `owner` | 指向防火墙所有者配置（Firewall Owner Configuration）的指针。输入时包含 `fwl_id`、`region` 和 `owner_index`；输出时包含更新后的所有权信息（Ownership Information）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a5c69f5f12b79a0b37a1f704624106960"></a>

### `tisci_cmd_clk_get_freq()`

```c
int tisci_cmd_clk_get_freq ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint64_t * freq )
```

获取时钟的当前频率（Current Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `freq` | 用于保存当前频率（Current Frequency）的指针，单位为 Hz。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a9801b388e5dc60f10aa624040cb8bfe2"></a>

### `tisci_cmd_clk_get_match_freq()`

```c
int tisci_cmd_clk_get_match_freq ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint64_t min_freq, uint64_t target_freq, uint64_t max_freq, uint64_t * match_freq )
```

获取符合要求的时钟频率（Matching Frequency）。

查找符合请求范围（Requested Range）的时钟频率（Clock Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `min_freq` | 允许的最低频率（Minimum Allowable Frequency），单位为 Hz。 |
| `target_freq` | 目标时钟频率（Target Clock Frequency），单位为 Hz。 |
| `max_freq` | 允许的最高频率（Maximum Allowable Frequency），单位为 Hz。 |
| `match_freq` | 用于保存匹配频率（Matched Frequency）的指针，单位为 Hz。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ae93fb7c70a4f2299415a51b993d36741"></a>

### `tisci_cmd_clk_get_num_parents()`

```c
int tisci_cmd_clk_get_num_parents ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint8_t * num_parents )
```

获取时钟的父时钟数量（Number of Parent Clocks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `num_parents` | 用于保存父时钟数量（Number of Parent Clocks）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a86e0ed2c8711363dc5ea710b12a303af"></a>

### `tisci_cmd_clk_get_parent()`

```c
int tisci_cmd_clk_get_parent ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint8_t * parent_id )
```

获取时钟的父时钟（Parent Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `parent_id` | 用于保存父时钟标识符（Parent Clock Identifier）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aaebb0012c291ded1b9303d634b1bb245"></a>

### `tisci_cmd_clk_is_auto()`

```c
int tisci_cmd_clk_is_auto ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, bool * req_state )
```

检查时钟是否由系统自动管理（Auto-managed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `req_state` | 用于保存时钟是否自动管理（Auto-managed）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a20276a83e2037db6895085770353a194"></a>

### `tisci_cmd_clk_is_off()`

```c
int tisci_cmd_clk_is_off ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, bool * req_state, bool * curr_state )
```

检查时钟是否关闭（OFF）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `req_state` | 用于保存时钟是否受管理且已禁用（Managed and Disabled）的指针。 |
| `curr_state` | 用于保存时钟是否尚未就绪、无法运行（Not Ready for Operation）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a7f0bafa6005d46d2786db590a27add25"></a>

### `tisci_cmd_clk_is_on()`

```c
int tisci_cmd_clk_is_on ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, bool * req_state, bool * curr_state )
```

检查时钟是否开启（ON）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `req_state` | 用于保存时钟是否受管理且已启用（Managed and Enabled）的指针。 |
| `curr_state` | 用于保存时钟是否已就绪、可以运行（Ready for Operation）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ad3563b7ec2fa13eb4b1faa564062ae12"></a>

### `tisci_cmd_clk_set_freq()`

```c
int tisci_cmd_clk_set_freq ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint64_t min_freq, uint64_t target_freq, uint64_t max_freq )
```

为时钟设置频率（Frequency）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `min_freq` | 允许的最低频率（Minimum Allowable Frequency），单位为 Hz。 |
| `target_freq` | 目标时钟频率（Target Clock Frequency），单位为 Hz。 |
| `max_freq` | 允许的最高频率（Maximum Allowable Frequency），单位为 Hz。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a6ad9804cf3e23246955bcab1e98aecdb"></a>

### `tisci_cmd_clk_set_parent()`

```c
int tisci_cmd_clk_set_parent ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint8_t parent_id )
```

为时钟设置父时钟（Parent Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `parent_id` | 要设置的父时钟标识符（Parent Clock Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a01393f21cb5a88388ce51e36ba1843fc"></a>

### `tisci_cmd_dev_get_clcnt()`

```c
int tisci_cmd_dev_get_clcnt ( const struct device * dev, uint32_t dev_id, uint32_t * count )
```

获取设备的上下文丢失计数器（Context Loss Counter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `count` | 用于保存上下文丢失计数器（Context Loss Counter）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="af9ff6eee5bca675c50c28fbc4af3048c"></a>

### `tisci_cmd_dev_is_idle()`

```c
int tisci_cmd_dev_is_idle ( const struct device * dev, uint32_t dev_id, bool * r_state )
```

检查设备是否被请求进入空闲状态（Idle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `r_state` | 用于保存结果（Result）的指针；已请求进入空闲状态（Idle）时为 `true`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aa7bb463be840666d87a68c1e65496b19"></a>

### `tisci_cmd_dev_is_on()`

```c
int tisci_cmd_dev_is_on ( const struct device * dev, uint32_t dev_id, bool * r_state, bool * curr_state )
```

检查设备是否被请求开启（ON）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `r_state` | 用于保存结果（Result）的指针；已请求开启（ON）时为 `true`。 |
| `curr_state` | 用于保存结果（Result）的指针；当前已开启且活动（ON and Active）时为 `true`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a1a441bdad9bfef9a0136f0b737c9c7aa"></a>

### `tisci_cmd_dev_is_stop()`

```c
int tisci_cmd_dev_is_stop ( const struct device * dev, uint32_t dev_id, bool * r_state, bool * curr_state )
```

检查设备是否被请求停止（Stopped）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `r_state` | 用于保存结果（Result）的指针；已请求停止（Stopped）时为 `true`。 |
| `curr_state` | 用于保存结果（Result）的指针；当前已停止（Stopped）时为 `true`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a4a3b7acb3098f71b2a9f85fbb318d595"></a>

### `tisci_cmd_dev_is_trans()`

```c
int tisci_cmd_dev_is_trans ( const struct device * dev, uint32_t dev_id, bool * curr_state )
```

检查设备当前是否处于状态转换过程中（Transitioning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `curr_state` | 用于保存结果（Result）的指针；当前正在进行状态转换（Transitioning）时为 `true`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a4f4072f951c0ebbeb75e8cd2f06b6e8f"></a>

### `tisci_cmd_dev_is_valid()`

```c
int tisci_cmd_dev_is_valid ( const struct device * dev, uint32_t dev_id )
```

检查设备标识符（Device ID）是否有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |

**返回（Returns）**：返回值（Returns）：设备标识符（Device ID）有效时为 `0`，否则为错误码（Error Code）。

<a id="ab63106de04e579ba18f34763b3efa8b3"></a>

### `tisci_cmd_get_clock()`

```c
int tisci_cmd_get_clock ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, bool needs_ssc, bool can_change_freq, bool enable_input_term )
```

从 TI SCI 获取时钟的控制权（Clock Control）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `needs_ssc` | 需要扩频时钟（Spread Spectrum Clock）时为 `true`，否则为 `false`。 |
| `can_change_freq` | 需要改变频率（Frequency Change）时为 `true`，否则为 `false`。 |
| `enable_input_term` | 需要输入端接（Input Termination）时为 `true`，否则为 `false`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a3f8128fa6c8c6f10bb7e302e6e9cfeaf"></a>

### `tisci_cmd_get_clock_state()`

```c
int tisci_cmd_get_clock_state ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint8_t * programmed_state, uint8_t * current_state )
```

获取时钟状态（Clock State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `programmed_state` | 用于保存请求的时钟状态（Requested Clock State）的指针。 |
| `current_state` | 用于保存当前时钟状态（Current Clock State）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a4011bbe29370fb581ab2dd0fcaa151db"></a>

### `tisci_cmd_get_device()`

```c
int tisci_cmd_get_device ( const struct device * dev, uint32_t dev_id )
```

请求对 TISCI 管理的设备进行独占访问（Exclusive Access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="adc16227f1ec150d0c6cf32442fa3e915"></a>

### `tisci_cmd_get_device_exclusive()`

```c
int tisci_cmd_get_device_exclusive ( const struct device * dev, uint32_t dev_id )
```

<a id="a90613df222309651abc1adb2f4d82272"></a>

### `tisci_cmd_get_device_resets()`

```c
int tisci_cmd_get_device_resets ( const struct device * dev, uint32_t dev_id, uint32_t * reset_state )
```

获取 TISCI 管理的设备的复位状态（Reset State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `reset_state` | 用于保存复位状态（Reset State）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aafb0c859914130228e6c229725f87eca"></a>

### `tisci_cmd_get_fwl_region()`

```c
int tisci_cmd_get_fwl_region ( const struct device * dev, struct tisci_msg_fwl_region * region )
```

获取防火墙区域配置（Firewall Region Configuration）。

获取防火墙区域配置（Firewall Region Configuration），包括权限（Permissions）、地址（Addresses）和控制设置（Control Settings）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `region` | 用于保存防火墙区域配置（Firewall Region Configuration）的指针。调用此函数之前，必须设置 `fwl_id`、`region` 和 `n_permission_regs` 字段。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a9e057dd13353ccdd7df3b2263ef22940"></a>

### `tisci_cmd_get_proc_boot_status()`

```c
int tisci_cmd_get_proc_boot_status ( const struct device * dev, uint8_t proc_id, uint64_t * bv, uint32_t * cfg_flags, uint32_t * ctrl_flags, uint32_t * sts_flags )
```

获取处理器启动状态（Processor Boot Status）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |
| `bv` | 用于保存启动向量（Boot Vector）的指针。 |
| `cfg_flags` | 用于保存配置标志（Configuration Flags）的指针。 |
| `ctrl_flags` | 用于保存控制标志（Control Flags）的指针。 |
| `sts_flags` | 用于保存状态标志（Status Flags）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ae249d114c60b6b1a76f7de8dab5c3ce1"></a>

### `tisci_cmd_get_resource_range()`

```c
int tisci_cmd_get_resource_range ( const struct device * dev, uint32_t dev_id, uint8_t subtype, uint16_t * range_start, uint16_t * range_num )
```

获取分配给该主机（Host）的资源范围（Resource Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | TISCI 设备标识符（Device ID）。 |
| `subtype` | 所请求的资源分配子类型（Resource Assignment Subtype）。 |
| `range_start` | 用于保存资源范围起始索引（Start Index of the Resource Range）的指针。 |
| `range_num` | 用于保存范围内资源数量（Number of Resources）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aa261b08c9141360c5f4f9e50ab151ed5"></a>

### `tisci_cmd_get_resource_range_from_shost()`

```c
int tisci_cmd_get_resource_range_from_shost ( const struct device * dev, uint32_t dev_id, uint8_t subtype, uint8_t s_host, uint16_t * range_start, uint16_t * range_num )
```

获取分配给指定主机（Host）的资源范围（Resource Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | TISCI 设备标识符（Device ID）。 |
| `subtype` | 所请求的资源分配子类型（Resource Assignment Subtype）。 |
| `s_host` | 资源所分配给的主机处理器标识符（Host Processor ID）。 |
| `range_start` | 用于保存资源范围起始索引（Start Index of the Resource Range）的指针。 |
| `range_num` | 用于保存范围内资源数量（Number of Resources）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aea0b9addbd3cfcb2be691f0801128fe1"></a>

### `tisci_cmd_get_revision()`

```c
int tisci_cmd_get_revision ( const struct device * dev, struct tisci_version_info * ver )
```

获取 TI 系统控制接口（SCI）固件的修订版本信息（Revision Information）。

查询 TI SCI 固件的版本和修订版本信息（Version and Revision Information）。获取的信息存储在提供的 `ver` 结构体中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `ver` | 指向用于保存固件版本信息（Firmware Version Information）的结构体的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，失败时为负错误码（Negative Error Code）。

<a id="a3d39780a18358066ec8f187474c18f71"></a>

### `tisci_cmd_idle_clock()`

```c
int tisci_cmd_idle_clock ( const struct device * dev, uint32_t dev_id, uint8_t clk_id )
```

使由 TI SCI 控制的时钟进入空闲状态（Idle）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ab8203c5d0b699ec726a889e7027ae034"></a>

### `tisci_cmd_idle_device()`

```c
int tisci_cmd_idle_device ( const struct device * dev, uint32_t dev_id )
```

使 TISCI 管理的设备进入空闲状态（Idle）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aab1720913f75a771e041e2195b9deede"></a>

### `tisci_cmd_idle_device_exclusive()`

```c
int tisci_cmd_idle_device_exclusive ( const struct device * dev, uint32_t dev_id )
```

<a id="aaa3b1c5f5072b40e2eb1c626cb6f6f29"></a>

### `tisci_cmd_proc_auth_boot_image()`

```c
int tisci_cmd_proc_auth_boot_image ( const struct device * dev, uint64_t * image_addr, uint32_t * image_size )
```

对镜像（Image）进行认证并加载，随后设置处理器配置标志（Processor Configuration Flags）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `image_addr` | 指向载荷镜像（Payload Image）和证书（Certificate）的内存地址的指针。 |
| `image_size` | 用于保存认证后镜像大小（Image Size after Authentication）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a1acfab0f8fd3b1db050f97aa21d26ce3"></a>

### `tisci_cmd_proc_handover()`

```c
int tisci_cmd_proc_handover ( const struct device * dev, uint8_t proc_id, uint8_t host_id )
```

将物理处理器控制权（Physical Processor Control）移交给该处理器访问控制列表（Access Control List）中的某个主机（Host）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |
| `host_id` | 要取得处理器控制权（Processor Control）的主机标识符（Host ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a2e0e3e88c635a4e6399941696056b8a9"></a>

### `tisci_cmd_proc_release()`

```c
int tisci_cmd_proc_release ( const struct device * dev, uint8_t proc_id )
```

释放物理处理器控制权（Physical Processor Control）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a3181b68860761b0060048a01d71888a8"></a>

### `tisci_cmd_proc_request()`

```c
int tisci_cmd_proc_request ( const struct device * dev, uint8_t proc_id )
```

请求物理处理器控制权（Physical Processor Control）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a9a80ade10fb08159e3fdfbd85ac8dfbf"></a>

### `tisci_cmd_proc_shutdown_no_wait()`

```c
int tisci_cmd_proc_shutdown_no_wait ( const struct device * dev, uint8_t proc_id )
```

关闭内核（Core）的命令，不请求也不等待响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ae48c6c78db3f4bee6520c0af66e37e7d"></a>

### `tisci_cmd_put_clock()`

```c
int tisci_cmd_put_clock ( const struct device * dev, uint32_t dev_id, uint8_t clk_id )
```

释放时钟控制权（Clock Control），将其交回 TI SCI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a5a7c9ff34ad1ffa87c62fef6b2ac8719"></a>

### `tisci_cmd_put_device()`

```c
int tisci_cmd_put_device ( const struct device * dev, uint32_t dev_id )
```

释放 TISCI 管理的设备（Device）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a01625817d1a222c2979443413c7d712c"></a>

### `tisci_cmd_query_msmc()`

```c
int tisci_cmd_query_msmc ( const struct device * dev, uint64_t * msmc_start, uint64_t * msmc_end )
```

查询可用的 MSMC 内存范围（Memory Range）。

向 TI SCI 固件查询当前可用的多标准共享内存控制器（Multi-Standard Shared Memory Controller，MSMC）的内存范围（Memory Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `msmc_start` | 用于保存 MSMC 起始地址（Start Address）的指针。 |
| `msmc_end` | 用于保存 MSMC 结束地址（End Address）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a9110e6b0fd37057ea72c64c8c2067a21"></a>

### `tisci_cmd_ring_config()`

```c
int tisci_cmd_ring_config ( const struct device * dev, uint32_t valid_params, uint16_t nav_id, uint16_t index, uint32_t addr_lo, uint32_t addr_hi, uint32_t count, uint8_t mode, uint8_t size, uint8_t order_id )
```

配置环形加速器（RA）的环（Ring）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `valid_params` | 定义环配置参数有效性（Validity of Ring Configuration Parameters）的位字段（Bitfield）。 |
| `nav_id` | 分配该环（Ring）的 Navigator 子系统设备标识符（Device ID）。 |
| `index` | 环索引（Ring Index）。 |
| `addr_lo` | 环基地址（Ring Base Address）的低 32 位。 |
| `addr_hi` | 环基地址（Ring Base Address）的高 32 位。 |
| `count` | 环元素（Ring Elements）的数量。 |
| `mode` | 环模式（Ring Mode）。 |
| `size` | 环元素大小（Ring Element Size）。 |
| `order_id` | 指定环的总线顺序标识符（Bus Order ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ac30ac2d3539999418f8b200e7b78d259"></a>

### `tisci_cmd_rm_irq_release()`

```c
int tisci_cmd_rm_irq_release ( const struct device * dev, struct tisci_irq_release_req * req )
```

释放 Navigator 子系统（Navigator Subsystem）的中断请求（IRQ）。

使用提供的请求结构体（Request Structure），释放 Navigator 子系统中的中断路由（Interrupt Route）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `req` | 指向中断请求释放请求结构体（IRQ Release Request Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a0d5c1b5afc2842e38de56c64c62f17fd"></a>

### `tisci_cmd_rm_irq_set()`

```c
int tisci_cmd_rm_irq_set ( const struct device * dev, struct tisci_irq_set_req * req )
```

设置 Navigator 子系统（Navigator Subsystem）的中断请求（IRQ）。

使用提供的请求结构体（Request Structure），建立 Navigator 子系统中的中断路由（Interrupt Route）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `req` | 指向中断请求设置请求结构体（IRQ Set Request Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a64b6aa840b820beed84fc9a21ffde350"></a>

### `tisci_cmd_rm_psil_pair()`

```c
int tisci_cmd_rm_psil_pair ( const struct device * dev, uint32_t nav_id, uint32_t src_thread, uint32_t dst_thread )
```

将 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）配对。

在 Navigator 子系统中，将 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）配对。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `nav_id` | Navigator 子系统设备标识符（Device ID）。 |
| `src_thread` | 源线程标识符（Source Thread ID）。 |
| `dst_thread` | 目标线程标识符（Destination Thread ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a61d3ce5732bbd5a25d5d63af5a059666"></a>

### `tisci_cmd_rm_psil_unpair()`

```c
int tisci_cmd_rm_psil_unpair ( const struct device * dev, uint32_t nav_id, uint32_t src_thread, uint32_t dst_thread )
```

解除 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）的配对。

在 Navigator 子系统中，解除 PSI-L 源线程（Source Thread）与目标线程（Destination Thread）的配对。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `nav_id` | Navigator 子系统设备标识符（Device ID）。 |
| `src_thread` | 源线程标识符（Source Thread ID）。 |
| `dst_thread` | 目标线程标识符（Destination Thread ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a5217423ca42a90a472777a907864128e"></a>

### `tisci_cmd_rm_udmap_rx_ch_cfg()`

```c
int tisci_cmd_rm_udmap_rx_ch_cfg ( const struct device * dev, const struct tisci_msg_rm_udmap_rx_ch_cfg * params )
```

配置 UDMAP 接收通道（Receive Channel）。

配置 Navigator 子系统 UDMAP 接收通道（Receive Channel）的非实时寄存器（Non-real-time Registers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `params` | 指向接收通道配置参数（Receive Channel Configuration Parameters）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a98a90edf1033e5146c51da785ee29581"></a>

### `tisci_cmd_rm_udmap_tx_ch_cfg()`

```c
int tisci_cmd_rm_udmap_tx_ch_cfg ( const struct device * dev, const struct tisci_msg_rm_udmap_tx_ch_cfg * params )
```

配置 UDMAP 发送通道（Transmit Channel）。

配置 Navigator 子系统 UDMAP 发送通道（Transmit Channel）的非实时寄存器（Non-real-time Registers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `params` | 指向发送通道配置参数（Transmit Channel Configuration Parameters）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a94f43ead8c81320f651fa9c0450a2493"></a>

### `tisci_cmd_set_device_resets()`

```c
int tisci_cmd_set_device_resets ( const struct device * dev, uint32_t dev_id, uint32_t reset_state )
```

为 TISCI 管理的设备设置复位（Resets）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `reset_state` | 设备专用复位位字段（Device-specific Reset Bit Field）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a2a1873dd1b47f7437cfd8adbea2decab"></a>

### `tisci_cmd_set_fwl_region()`

```c
int tisci_cmd_set_fwl_region ( const struct device * dev, const struct tisci_msg_fwl_region * region )
```

配置防火墙区域（Firewall Region）。

使用指定配置参数（Configuration Parameters）建立防火墙区域（Firewall Region），包括权限、地址和控制设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `region` | 指向防火墙区域配置参数（Firewall Region Configuration Parameters）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a3551276e98c3f03ea4beb9086c3b89c3"></a>

### `tisci_cmd_set_proc_boot_cfg()`

```c
int tisci_cmd_set_proc_boot_cfg ( const struct device * dev, uint8_t proc_id, uint64_t bootvector, uint32_t config_flags_set, uint32_t config_flags_clear )
```

设置处理器启动配置标志（Processor Boot Configuration Flags）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |
| `bootvector` | 启动向量地址（Boot Vector Address）。 |
| `config_flags_set` | 要设置的配置标志（Configuration Flags）。 |
| `config_flags_clear` | 要清除的配置标志（Configuration Flags）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aee60c2eb75e6786b91d9dc73c7a7e2c6"></a>

### `tisci_cmd_set_proc_boot_ctrl()`

```c
int tisci_cmd_set_proc_boot_ctrl ( const struct device * dev, uint8_t proc_id, uint32_t control_flags_set, uint32_t control_flags_clear )
```

设置处理器启动控制标志（Processor Boot Control Flags）的命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |
| `control_flags_set` | 要设置的控制标志（Control Flags）。 |
| `control_flags_clear` | 要清除的控制标志（Control Flags）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="aa7b6bef27ce24be4762d28499197a8bd"></a>

### `tisci_cmd_sys_reset()`

```c
int tisci_cmd_sys_reset ( const struct device * dev)
```

请求系统复位（System Reset）。

命令 TI SCI 固件执行系统复位（System Reset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="ada78c57b3cb24e57a3f6cc155e3a3d09"></a>

### `tisci_get_device_state()`

```c
int tisci_get_device_state ( const struct device * dev, uint32_t dev_id, uint32_t * clcnt, uint32_t * resets, uint8_t * p_state, uint8_t * c_state )
```

获取设备状态（Device State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clcnt` | 用于保存上下文丢失计数（Context Loss Count）的指针。 |
| `resets` | 用于保存复位计数（Reset Count）的指针。 |
| `p_state` | 用于保存已编程状态（Programmed State）的指针。 |
| `c_state` | 用于保存当前状态（Current State）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a8ced32499c14aae81994368d4450422d"></a>

### `tisci_get_resource_range()`

```c
int tisci_get_resource_range ( const struct device * dev, uint32_t dev_id, uint8_t subtype, uint8_t s_host, uint16_t * range_start, uint16_t * range_num )
```

获取分配给某个主机（Host）的资源范围（Resource Range）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | TISCI 设备标识符（Device ID）。 |
| `subtype` | 所请求的资源分配子类型（Resource Assignment Subtype）。 |
| `s_host` | 资源所分配给的主机处理器标识符（Host Processor ID）。 |
| `range_start` | 用于保存资源范围起始索引（Start Index of the Resource Range）的指针。 |
| `range_num` | 用于保存范围内资源数量（Number of Resources）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a8a29455ba732efa082c1a72922f46f9e"></a>

### `tisci_proc_wait_boot_status_no_wait()`

```c
int tisci_proc_wait_boot_status_no_wait ( const struct device * dev, uint8_t proc_id, uint8_t num_wait_iterations, uint8_t num_match_iterations, uint8_t delay_per_iteration_us, uint8_t delay_before_iterations_us, uint32_t status_flags_1_set_all_wait, uint32_t status_flags_1_set_any_wait, uint32_t status_flags_1_clr_all_wait, uint32_t status_flags_1_clr_any_wait )
```

等待处理器启动状态（Processor Boot Status）的辅助函数，不请求也不等待响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `proc_id` | 此请求所针对的处理器标识符（Processor ID）。 |
| `num_wait_iterations` | 超时前执行检查的总迭代次数（Total Number of Iterations）。 |
| `num_match_iterations` | 确认状态所需的连续匹配次数（Number of Consecutive Matches）。 |
| `delay_per_iteration_us` | 每次状态检查（Status Check）之间的延迟，单位为微秒。 |
| `delay_before_iterations_us` | 第一次状态检查（Status Check）之前的延迟，单位为微秒。 |
| `status_flags_1_set_all_wait` | 必须全部置为 `1` 的标志（Flags）。 |
| `status_flags_1_set_any_wait` | 至少一个必须置为 `1` 的标志（Flags）。 |
| `status_flags_1_clr_all_wait` | 必须全部清为 `0` 的标志（Flags）。 |
| `status_flags_1_clr_any_wait` | 至少一个必须清为 `0` 的标志（Flags）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a086d96bed3d789bf303f56405a791aa6"></a>

### `tisci_set_clock_state()`

```c
int tisci_set_clock_state ( const struct device * dev, uint32_t dev_id, uint8_t clk_id, uint32_t flags, uint8_t state )
```

设置时钟状态（Clock State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `clk_id` | 此请求所针对设备的时钟标识符（Clock Identifier）。 |
| `flags` | 按需设置的头部标志（Header Flags）。 |
| `state` | 要为时钟请求的状态（State）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a8b6d6f99df32eeba9131ce130ee4f12d"></a>

### `tisci_set_device_state()`

```c
int tisci_set_device_state ( const struct device * dev, uint32_t dev_id, uint32_t flags, uint8_t state )
```

设置设备状态（Device State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `flags` | 要为设备设置的标志（Flags）。 |
| `state` | 设备要进入的状态（State）：`0` 为关闭（Off），`1` 为开启（On），`2` 为保持（Retention），`3` 为复位（Reset）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。

<a id="a05f871388f68d9c71620ea43bde1e3ab"></a>

### `tisci_set_device_state_no_wait()`

```c
int tisci_set_device_state_no_wait ( const struct device * dev, uint32_t dev_id, uint32_t flags, uint8_t state )
```

设置设备状态（Device State），不等待响应（Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TI SCI 设备（Device）的指针。 |
| `dev_id` | 此请求所针对的设备标识符（Device Identifier）。 |
| `flags` | 要为设备设置的标志（Flags）。 |
| `state` | 设备要进入的状态（State）：`0` 为关闭（Off），`1` 为开启（On），`2` 为保持（Retention），`3` 为复位（Reset）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为错误码（Error Code）。


## 7.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P015_tisci.h_源码浏览.md)
- [tisci_version_info](../platform_security_model_reference/P072_tisci_version_info_结构体.md)
- [tisci_msg_fwl_region](../platform_security_model_reference/P068_tisci_msg_fwl_region_结构体.md)
- [tisci_msg_fwl_owner](../platform_security_model_reference/P067_tisci_msg_fwl_owner_结构体.md)
- [tisci_msg_rm_udmap_tx_ch_cfg](../platform_security_model_reference/P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md)
- [tisci_msg_rm_udmap_rx_ch_cfg](../platform_security_model_reference/P070_tisci_msg_rm_udmap_rx_ch_cfg_结构体.md)
- [tisci_irq_set_req](../platform_security_model_reference/P066_tisci_irq_set_req_结构体.md)
- [tisci_irq_release_req](../platform_security_model_reference/P065_tisci_irq_release_req_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_zephyr__dt-bindings__pinctrl__rtl87x2g-pinctrl.h_文件参考.md) · [返回大纲](大纲.md)
