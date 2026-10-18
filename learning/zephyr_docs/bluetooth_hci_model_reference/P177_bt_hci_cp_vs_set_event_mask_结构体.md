---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-177
title: bt_hci_cp_vs_set_event_mask_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__set__event__mask.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_bt\_hci\_cp\_vs\_set\_event\_mask\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__vs__set__event__mask.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 177.1\_数据成员（Data Fields）

<a id="r_ad5883adb065f04e923ff64093c78949a"></a>

```c
uint8_t event_mask [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[event_mask](#ad5883adb065f04e923ff64093c78949a)。

## 177.2\_详细说明（Detailed Documentation）

<a id="ad5883adb065f04e923ff64093c78949a"></a>

### `event_mask`

```c
uint8_t bt_hci_cp_vs_set_event_mask::event_mask[8]
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 177.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P176_bt_hci_cp_vs_reset_结构体.md) · [返回大纲](大纲.md) · [下一章](P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md)
