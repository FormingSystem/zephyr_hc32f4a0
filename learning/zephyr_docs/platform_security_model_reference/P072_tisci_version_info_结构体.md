---
id: learning.zephyr-docs.platform-security-model-reference.page-72
title: tisci_version_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__version__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_tisci\_version\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__version__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

版本信息（Version Information）结构。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

版本信息结构体（Version information structure）。

参数（Parameters）：

- `abi_major`：应用二进制接口（ABI）的主版本号。此值改变意味着存在破坏向后兼容性的风险。
- `abi_minor`：ABI 的次版本号。此值改变意味着新增功能，或 ABI 发生兼容性变更。
- `firmware_revision`：固件修订版本，通常不使用。
- `firmware_description`：固件描述，通常不使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_a7371d69f5f0993dfd1e582c165d2ddc5"></a>

```c
uint8_t abi_major
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[abi_major](#a7371d69f5f0993dfd1e582c165d2ddc5)。

<a id="r_a8547f04843609b8a324ea4ecb91c17a7"></a>

```c
uint8_t abi_minor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[abi_minor](#a8547f04843609b8a324ea4ecb91c17a7)。

<a id="r_a711c9ca4b063958fcb46ad0e298caa27"></a>

```c
uint16_t firmware_revision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[firmware_revision](#a711c9ca4b063958fcb46ad0e298caa27)。

<a id="r_a62cb5c8e86a94dbf53430d73c9f241a9"></a>

```c
char firmware_description [32]
```

相关声明：[firmware_description](#a62cb5c8e86a94dbf53430d73c9f241a9)。

## 72.2\_详细说明（Detailed Documentation）

<a id="a7371d69f5f0993dfd1e582c165d2ddc5"></a>

### `abi_major`

```c
uint8_t tisci_version_info::abi_major
```

<a id="a8547f04843609b8a324ea4ecb91c17a7"></a>

### `abi_minor`

```c
uint8_t tisci_version_info::abi_minor
```

<a id="a62cb5c8e86a94dbf53430d73c9f241a9"></a>

### `firmware_description`

```c
char tisci_version_info::firmware_description[32]
```

<a id="a711c9ca4b063958fcb46ad0e298caa27"></a>

### `firmware_revision`

```c
uint16_t tisci_version_info::firmware_revision
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_tisci_msg_rm_udmap_tx_ch_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_vector_desc_t_结构体.md)
