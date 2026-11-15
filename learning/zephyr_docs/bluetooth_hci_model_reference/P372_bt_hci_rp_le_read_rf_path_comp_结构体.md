---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-372
title: bt_hci_rp_le_read_rf_path_comp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__rf__path__comp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第372章\_bt\_hci\_rp\_le\_read\_rf\_path\_comp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__le__read__rf__path__comp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 372.1\_数据成员（Data Fields）

<a id="r_a84a04bcc64ea6d50fe41e9b416a5ada1"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a84a04bcc64ea6d50fe41e9b416a5ada1)。

<a id="r_a827fa954277823efdc5838c317a1460a"></a>

```c
int16_t tx_path_comp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[tx_path_comp](#a827fa954277823efdc5838c317a1460a)。

<a id="r_a0f46a99c74006dc0a4dfd1a49c72e077"></a>

```c
int16_t rx_path_comp
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[rx_path_comp](#a0f46a99c74006dc0a4dfd1a49c72e077)。

## 372.2\_详细说明（Detailed Documentation）

<a id="a0f46a99c74006dc0a4dfd1a49c72e077"></a>

### `rx_path_comp`

```c
int16_t bt_hci_rp_le_read_rf_path_comp::rx_path_comp
```

<a id="a84a04bcc64ea6d50fe41e9b416a5ada1"></a>

### `status`

```c
uint8_t bt_hci_rp_le_read_rf_path_comp::status
```

<a id="a827fa954277823efdc5838c317a1460a"></a>

### `tx_path_comp`

```c
int16_t bt_hci_rp_le_read_rf_path_comp::tx_path_comp
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 372.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P371_bt_hci_rp_le_read_phy_结构体.md) · [返回大纲](大纲.md) · [下一章](P373_bt_hci_rp_le_read_rl_size_结构体.md)
