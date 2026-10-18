---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-319
title: bt_hci_le_cs_step_data_mode_2_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第319章\_bt\_hci\_le\_cs\_step\_data\_mode\_2\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__cs__step__data__mode__2.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

子事件结果步骤数据格式：模式 2。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

子事件结果步骤数据格式：模式 2。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 319.1\_数据成员（Data Fields）

<a id="r_a9feb2b07f8862aa24772a733f451f7a8"></a>

```c
uint8_t antenna_permutation_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[antenna_permutation_index](#a9feb2b07f8862aa24772a733f451f7a8)。

<a id="r_aef5699cb9bfc522a12be9a284392fd0e"></a>

```c
struct bt_hci_le_cs_step_data_tone_info tone_info []
```

相关声明：[bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)、[tone_info](#aef5699cb9bfc522a12be9a284392fd0e)。

## 319.2\_详细说明（Detailed Documentation）

<a id="a9feb2b07f8862aa24772a733f451f7a8"></a>

### `antenna_permutation_index`

```c
uint8_t bt_hci_le_cs_step_data_mode_2::antenna_permutation_index
```

<a id="aef5699cb9bfc522a12be9a284392fd0e"></a>

### `tone_info`

```c
struct bt_hci_le_cs_step_data_tone_info bt_hci_le_cs_step_data_mode_2::tone_info[]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 319.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_le_cs_step_data_tone_info](P322_bt_hci_le_cs_step_data_tone_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md) · [返回大纲](大纲.md) · [下一章](P320_bt_hci_le_cs_step_data_mode_3_结构体.md)
