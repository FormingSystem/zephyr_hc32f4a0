---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-448
title: bt_hci_vs_fatal_error_stack_frame_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__fatal__error__stack__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第448章\_bt\_hci\_vs\_fatal\_error\_stack\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__vs__fatal__error__stack__frame.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 448.1\_数据成员（Data Fields）

<a id="r_ac2f93a05158d4c170848ee4afdfe1bd1"></a>

```c
uint32_t reason
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reason](#ac2f93a05158d4c170848ee4afdfe1bd1)。

<a id="r_a1530d501d5fd5dade63219e16ddd5d85"></a>

```c
uint8_t cpu_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cpu_type](#a1530d501d5fd5dade63219e16ddd5d85)。

<a id="r_a89e4ede59af9b37fcaeee00ea028f930"></a>

```c
uint8_t cpu_data [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cpu_data](#a89e4ede59af9b37fcaeee00ea028f930)。

## 448.2\_详细说明（Detailed Documentation）

<a id="a89e4ede59af9b37fcaeee00ea028f930"></a>

### `cpu_data`

```c
uint8_t bt_hci_vs_fatal_error_stack_frame::cpu_data[0]
```

<a id="a1530d501d5fd5dade63219e16ddd5d85"></a>

### `cpu_type`

```c
uint8_t bt_hci_vs_fatal_error_stack_frame::cpu_type
```

<a id="ac2f93a05158d4c170848ee4afdfe1bd1"></a>

### `reason`

```c
uint32_t bt_hci_vs_fatal_error_stack_frame::reason
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 448.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md) · [返回大纲](大纲.md) · [下一章](P449_bt_hci_vs_static_addr_结构体.md)
