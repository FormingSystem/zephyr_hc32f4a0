---
id: learning.zephyr-docs.platform-security-model-reference.page-4
title: edac_synopsys_callback_data_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structedac__synopsys__callback__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_edac\_synopsys\_callback\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structedac__synopsys__callback__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供给通过edac_notify_callback_set设置的函数的回调数据（Callback Data）。

```c
#include <zephyr/drivers/edac/edac_synopsys.h>
```

<a id="details"></a>

提供给通过edac_notify_callback_set设置的函数的回调数据（Callback Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a71c5e4b31f16927b483e7bd3bf8b6f32"></a>

```c
uint16_t corr_err_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[corr_err_count](#a71c5e4b31f16927b483e7bd3bf8b6f32)。

自上次回调以来已纠正错误的数量。

<a id="r_aece294a29dbd98a3e75f4cfb6c9c79c3"></a>

```c
uint8_t corr_err_rank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_rank](#aece294a29dbd98a3e75f4cfb6c9c79c3)。

最近一次已纠正 ECC 错误的内存排（rank）编号。

<a id="r_ae6a6c090671e5bfda93b904ee9e95a2b"></a>

```c
uint8_t corr_err_bg
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_bg](#ae6a6c090671e5bfda93b904ee9e95a2b)。

最近一次已纠正 ECC 错误的存储体组（bank group）编号。

<a id="r_a749fb5929f89a63cb62fd76f4c143dba"></a>

```c
uint8_t corr_err_bank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_bank](#a749fb5929f89a63cb62fd76f4c143dba)。

最近一次已纠正 ECC 错误的存储体（bank）编号。

<a id="r_aa549050b7305f4e8bb15f5b849bec165"></a>

```c
uint32_t corr_err_row
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[corr_err_row](#aa549050b7305f4e8bb15f5b849bec165)。

最近一次已纠正 ECC 错误的行号。

<a id="r_af23d5d538b8ebe722838a186c6b30909"></a>

```c
uint8_t corr_err_col
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_col](#af23d5d538b8ebe722838a186c6b30909)。

最近一次已纠正 ECC 错误的列号。

<a id="r_aca79f779ac263e5344dad5e12ee6d3da"></a>

```c
uint64_t corr_err_syndrome
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[corr_err_syndrome](#aca79f779ac263e5344dad5e12ee6d3da)。

最近一次已纠正 ECC 错误的校验子（syndrome），即数据模式。

<a id="r_a73567e401a706bbf392db489afd72012"></a>

```c
uint8_t corr_err_syndrome_ecc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_syndrome_ecc](#a73567e401a706bbf392db489afd72012)。

最近一次已纠正 ECC 错误的校验子 ECC 位。

<a id="r_a10387f0ff6db7c6a116a8ccb2ba3e7c0"></a>

```c
uint64_t corr_err_bitmask
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[corr_err_bitmask](#a10387f0ff6db7c6a116a8ccb2ba3e7c0)。

数据字中已纠正错误位的位掩码。

<a id="r_a659a7a12f24337cc57ea121e06cbd20c"></a>

```c
uint8_t corr_err_bitmask_ecc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_bitmask_ecc](#a659a7a12f24337cc57ea121e06cbd20c)。

ECC 字中已纠正错误位的位掩码。

<a id="r_aa34f78372e80c57772ea864827a5abe1"></a>

```c
uint16_t uncorr_err_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uncorr_err_count](#aa34f78372e80c57772ea864827a5abe1)。

自上次回调以来未纠正错误的数量。

<a id="r_a07c6bd60a094e5b807df0bf823959a3e"></a>

```c
uint8_t uncorr_err_rank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uncorr_err_rank](#a07c6bd60a094e5b807df0bf823959a3e)。

最近一次未纠正 ECC 错误的内存排（rank）编号。

<a id="r_af148757e829b0e0bfbf575521131f54b"></a>

```c
uint8_t uncorr_err_bg
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uncorr_err_bg](#af148757e829b0e0bfbf575521131f54b)。

最近一次未纠正 ECC 错误的存储体组（bank group）编号。

<a id="r_a8df3545fd3f7dfa8a99dcac90e708ec2"></a>

```c
uint8_t uncorr_err_bank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uncorr_err_bank](#a8df3545fd3f7dfa8a99dcac90e708ec2)。

最近一次未纠正 ECC 错误的存储体（bank）编号。

<a id="r_a99670584c0c09eaf2e14e6e797ec834d"></a>

```c
uint32_t uncorr_err_row
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uncorr_err_row](#a99670584c0c09eaf2e14e6e797ec834d)。

最近一次未纠正 ECC 错误的行号。

<a id="r_a17fee6074688540133b07fb0d567857a"></a>

```c
uint8_t uncorr_err_col
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uncorr_err_col](#a17fee6074688540133b07fb0d567857a)。

最近一次未纠正 ECC 错误的列号。

<a id="r_a3c05b263247c78ac195760f6a73a30b8"></a>

```c
uint64_t uncorr_err_syndrome
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[uncorr_err_syndrome](#a3c05b263247c78ac195760f6a73a30b8)。

最近一次未纠正 ECC 错误的校验子（syndrome），即数据模式。

<a id="r_a36d022f0de8a63581a4a2a95d923e041"></a>

```c
uint8_t uncorr_err_syndrome_ecc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uncorr_err_syndrome_ecc](#a36d022f0de8a63581a4a2a95d923e041)。

最近一次未纠正 ECC 错误的校验子 ECC 位。

## 4.2\_详细说明（Detailed Documentation）

<a id="a749fb5929f89a63cb62fd76f4c143dba"></a>

### `corr_err_bank`

```c
uint8_t edac_synopsys_callback_data::corr_err_bank
```

最近一次已纠正 ECC 错误的存储体（bank）编号。

<a id="ae6a6c090671e5bfda93b904ee9e95a2b"></a>

### `corr_err_bg`

```c
uint8_t edac_synopsys_callback_data::corr_err_bg
```

最近一次已纠正 ECC 错误的存储体组（bank group）编号。

<a id="a10387f0ff6db7c6a116a8ccb2ba3e7c0"></a>

### `corr_err_bitmask`

```c
uint64_t edac_synopsys_callback_data::corr_err_bitmask
```

数据字中已纠正错误位的位掩码。

<a id="a659a7a12f24337cc57ea121e06cbd20c"></a>

### `corr_err_bitmask_ecc`

```c
uint8_t edac_synopsys_callback_data::corr_err_bitmask_ecc
```

ECC 字中已纠正错误位的位掩码。

<a id="af23d5d538b8ebe722838a186c6b30909"></a>

### `corr_err_col`

```c
uint8_t edac_synopsys_callback_data::corr_err_col
```

最近一次已纠正 ECC 错误的列号。

<a id="a71c5e4b31f16927b483e7bd3bf8b6f32"></a>

### `corr_err_count`

```c
uint16_t edac_synopsys_callback_data::corr_err_count
```

自上次回调以来已纠正错误的数量。

<a id="aece294a29dbd98a3e75f4cfb6c9c79c3"></a>

### `corr_err_rank`

```c
uint8_t edac_synopsys_callback_data::corr_err_rank
```

最近一次已纠正 ECC 错误的内存排（rank）编号。

<a id="aa549050b7305f4e8bb15f5b849bec165"></a>

### `corr_err_row`

```c
uint32_t edac_synopsys_callback_data::corr_err_row
```

最近一次已纠正 ECC 错误的行号。

<a id="aca79f779ac263e5344dad5e12ee6d3da"></a>

### `corr_err_syndrome`

```c
uint64_t edac_synopsys_callback_data::corr_err_syndrome
```

最近一次已纠正 ECC 错误的校验子（syndrome），即数据模式。

<a id="a73567e401a706bbf392db489afd72012"></a>

### `corr_err_syndrome_ecc`

```c
uint8_t edac_synopsys_callback_data::corr_err_syndrome_ecc
```

最近一次已纠正 ECC 错误的校验子 ECC 位。

<a id="a8df3545fd3f7dfa8a99dcac90e708ec2"></a>

### `uncorr_err_bank`

```c
uint8_t edac_synopsys_callback_data::uncorr_err_bank
```

最近一次未纠正 ECC 错误的存储体（bank）编号。

<a id="af148757e829b0e0bfbf575521131f54b"></a>

### `uncorr_err_bg`

```c
uint8_t edac_synopsys_callback_data::uncorr_err_bg
```

最近一次未纠正 ECC 错误的存储体组（bank group）编号。

<a id="a17fee6074688540133b07fb0d567857a"></a>

### `uncorr_err_col`

```c
uint8_t edac_synopsys_callback_data::uncorr_err_col
```

最近一次未纠正 ECC 错误的列号。

<a id="aa34f78372e80c57772ea864827a5abe1"></a>

### `uncorr_err_count`

```c
uint16_t edac_synopsys_callback_data::uncorr_err_count
```

自上次回调以来未纠正错误的数量。

<a id="a07c6bd60a094e5b807df0bf823959a3e"></a>

### `uncorr_err_rank`

```c
uint8_t edac_synopsys_callback_data::uncorr_err_rank
```

最近一次未纠正 ECC 错误的内存排（rank）编号。

<a id="a99670584c0c09eaf2e14e6e797ec834d"></a>

### `uncorr_err_row`

```c
uint32_t edac_synopsys_callback_data::uncorr_err_row
```

最近一次未纠正 ECC 错误的行号。

<a id="a3c05b263247c78ac195760f6a73a30b8"></a>

### `uncorr_err_syndrome`

```c
uint64_t edac_synopsys_callback_data::uncorr_err_syndrome
```

最近一次未纠正 ECC 错误的校验子（syndrome），即数据模式。

<a id="a36d022f0de8a63581a4a2a95d923e041"></a>

### `uncorr_err_syndrome_ecc`

```c
uint8_t edac_synopsys_callback_data::uncorr_err_syndrome_ecc
```

最近一次未纠正 ECC 错误的校验子 ECC 位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/edac/edac_synopsys.h`

## 4.3\_原页交叉引用（Cross References）

- [edac_notify_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2def500f72a06271d9a10243bfdf6527)
- [zephyr/drivers/edac/edac_synopsys.h](https://docs.zephyrproject.org/latest/doxygen/html/edac__synopsys_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_edac_nxp_callback_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_eic_config_params_结构体.md)
