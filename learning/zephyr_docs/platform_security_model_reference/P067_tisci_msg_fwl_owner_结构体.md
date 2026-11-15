---
id: learning.zephyr-docs.platform-security-model-reference.page-67
title: tisci_msg_fwl_owner_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__owner.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_tisci\_msg\_fwl\_owner\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__owner.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

防火墙所有者变更（Firewall Owner Change）的请求和响应。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

更改防火墙所有者（Firewall owner）的请求和响应。

参数（Parameters）：

- `fwl_id`：目标防火墙的 ID。
- `region`：要设置配置信息的区域号或通道号。简单防火墙不使用此字段，必须将其初始化为零。对于基于区域的防火墙，该字段表示目标区域，索引从 0 开始；对于基于通道的防火墙，该字段表示目标通道，索引从 0 开始。
- `n_permission_regs`：权限寄存器（Permission registers）的数量，必须小于或等于 3。
- `control`：该区域的控制寄存器值。
- `owner_index`：要切换到的新所有者索引。所有者索引在 DMSC 固件启动配置数据中设置。
- `owner_privid`：新所有者的 priv-id，在不知道 `owner_index` 时用于查找所有者索引；否则必须设为零。
- `owner_permission_bits`：新所有者的权限位。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a370a1aff0233b53b035cbcd7b4c264b5"></a>

```c
uint16_t fwl_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fwl_id](#a370a1aff0233b53b035cbcd7b4c264b5)。

<a id="r_a7ccaf9d3c1bd3639e8c170acd5d535a8"></a>

```c
uint16_t region
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[region](#a7ccaf9d3c1bd3639e8c170acd5d535a8)。

<a id="r_a2010d9ee65f9a94e5477a0fc1f21774e"></a>

```c
uint8_t owner_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[owner_index](#a2010d9ee65f9a94e5477a0fc1f21774e)。

<a id="r_a5e5e33a9a2f7c04022ce51fa1dcb8eef"></a>

```c
uint8_t owner_privid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[owner_privid](#a5e5e33a9a2f7c04022ce51fa1dcb8eef)。

<a id="r_a31ec3f0e90fdb8cea887d67004b066a7"></a>

```c
uint16_t owner_permission_bits
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[owner_permission_bits](#a31ec3f0e90fdb8cea887d67004b066a7)。

## 67.2\_详细说明（Detailed Documentation）

<a id="a370a1aff0233b53b035cbcd7b4c264b5"></a>

### `fwl_id`

```c
uint16_t tisci_msg_fwl_owner::fwl_id
```

<a id="a2010d9ee65f9a94e5477a0fc1f21774e"></a>

### `owner_index`

```c
uint8_t tisci_msg_fwl_owner::owner_index
```

<a id="a31ec3f0e90fdb8cea887d67004b066a7"></a>

### `owner_permission_bits`

```c
uint16_t tisci_msg_fwl_owner::owner_permission_bits
```

<a id="a5e5e33a9a2f7c04022ce51fa1dcb8eef"></a>

### `owner_privid`

```c
uint8_t tisci_msg_fwl_owner::owner_privid
```

<a id="a7ccaf9d3c1bd3639e8c170acd5d535a8"></a>

### `region`

```c
uint16_t tisci_msg_fwl_owner::region
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_tisci_irq_set_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_tisci_msg_fwl_region_结构体.md)
