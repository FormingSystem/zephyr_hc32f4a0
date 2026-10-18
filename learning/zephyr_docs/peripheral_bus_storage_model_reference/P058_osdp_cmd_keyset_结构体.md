---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-58
title: osdp_cmd_keyset_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__keyset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_osdp\_cmd\_keyset\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__keyset.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

此命令将加密密钥（Encryption Key）从控制面板（CP）传输到外设（PD）。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

此命令将加密密钥（Encryption key）从控制面板（Control Panel，CP）传输给外设（PD）。

参数（Parameters）：

- `type`：密钥类型，`0x01` 表示安全通道基础密钥（Secure Channel Base Key）。
- `length`：密钥数据的字节数，计算方式为 `(密钥位数 + 7) / 8`。
- `data`：密钥数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_add89930f6c3b88355fcd2f95573080e6"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#add89930f6c3b88355fcd2f95573080e6)。

密钥类型（Type of keys）：

<a id="r_a673a4897ae2ff6aa9b88af6440fdc5a6"></a>

```c
uint8_t length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a673a4897ae2ff6aa9b88af6440fdc5a6)。

密钥数据的字节数，计算方式为 `(密钥位数 + 7) / 8`。

<a id="r_af85adb3e9c4f73a91fb7a430ff17f6df"></a>

```c
uint8_t data [32]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#af85adb3e9c4f73a91fb7a430ff17f6df)。

密钥数据。

## 58.2\_详细说明（Detailed Documentation）

<a id="af85adb3e9c4f73a91fb7a430ff17f6df"></a>

### `data`

```c
uint8_t osdp_cmd_keyset::data[32]
```

密钥数据。

<a id="a673a4897ae2ff6aa9b88af6440fdc5a6"></a>

### `length`

```c
uint8_t osdp_cmd_keyset::length
```

密钥数据的字节数，计算方式为 `(密钥位数 + 7) / 8`。

<a id="add89930f6c3b88355fcd2f95573080e6"></a>

### `type`

```c
uint8_t osdp_cmd_keyset::type
```

密钥类型（Type of keys）：

- `0x01`：安全通道基础密钥（Secure Channel Base Key）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_osdp_cmd_comset_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_osdp_cmd_led_结构体.md)
