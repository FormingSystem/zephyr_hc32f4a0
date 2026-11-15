---
id: learning.zephyr-docs.platform-security-model-reference.page-3
title: edac_nxp_callback_data_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structedac__nxp__callback__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_edac\_nxp\_callback\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structedac__nxp__callback__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供给通过edac_notify_callback_set设置的函数的回调数据（Callback Data）。

```c
#include <zephyr/drivers/edac/edac_mcux_erm.h>
```

<a id="details"></a>

提供给通过edac_notify_callback_set设置的函数的回调数据（Callback Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_ac6c51cd937e68365c03bf9adc0d812d9"></a>

```c
uint8_t corr_err_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[corr_err_count](#ac6c51cd937e68365c03bf9adc0d812d9)。

已纠正错误的数量。

<a id="r_a50766299a1d828d69c185ebe713b7167"></a>

```c
uint8_t err_syndrome
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[err_syndrome](#a50766299a1d828d69c185ebe713b7167)。

最近一次单比特纠错码（ECC）事件的校验子（syndrome）ECC 位。

<a id="r_a505938240dd1ade2aa7d7a62176c6ab2"></a>

```c
uint32_t err_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[err_addr](#a505938240dd1ade2aa7d7a62176c6ab2)。

最近一次 ECC 事件的地址。

<a id="r_a86b3ffc195ea995856b9ab1369696084"></a>

```c
uint32_t err_status
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[err_status](#a86b3ffc195ea995856b9ab1369696084)。

最近一次 ECC 事件的类型。

## 3.2\_详细说明（Detailed Documentation）

<a id="ac6c51cd937e68365c03bf9adc0d812d9"></a>

### `corr_err_count`

```c
uint8_t edac_nxp_callback_data::corr_err_count
```

已纠正错误的数量。

<a id="a505938240dd1ade2aa7d7a62176c6ab2"></a>

### `err_addr`

```c
uint32_t edac_nxp_callback_data::err_addr
```

最近一次 ECC 事件的地址。

<a id="a86b3ffc195ea995856b9ab1369696084"></a>

### `err_status`

```c
uint32_t edac_nxp_callback_data::err_status
```

最近一次 ECC 事件的类型。

<a id="a50766299a1d828d69c185ebe713b7167"></a>

### `err_syndrome`

```c
uint8_t edac_nxp_callback_data::err_syndrome
```

最近一次单比特纠错码（ECC）事件的校验子（syndrome）ECC 位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/edac/edac_mcux_erm.h`

## 3.3\_原页交叉引用（Cross References）

- [edac_notify_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2def500f72a06271d9a10243bfdf6527)
- [zephyr/drivers/edac/edac_mcux_erm.h](https://docs.zephyrproject.org/latest/doxygen/html/edac__mcux__erm_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_dw_ace_v1_ictl_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_edac_synopsys_callback_data_结构体.md)
