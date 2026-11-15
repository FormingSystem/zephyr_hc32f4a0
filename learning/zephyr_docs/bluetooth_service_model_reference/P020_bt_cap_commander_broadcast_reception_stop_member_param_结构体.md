---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-20
title: bt_cap_commander_broadcast_reception_stop_member_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__stop__member__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__commander__broadcast__reception__stop__member__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

停止广播接收的成员参数（Member Parameters）。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

停止广播接收的成员参数（Member Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_aa934af2e197c129b1fcb1eea9359ea6d"></a>

```c
union bt_cap_set_member member
```

相关声明：[bt_cap_set_member](P188_bt_cap_set_member_联合体.md)、[member](#aa934af2e197c129b1fcb1eea9359ea6d)。

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="r_a72d606f6a83b1c84aa41d9db22cb955a"></a>

```c
uint8_t src_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[src_id](#a72d606f6a83b1c84aa41d9db22cb955a)。

接收状态的音频源 ID（Source ID）。

<a id="r_aeeab53e8bd7ae4f36433c0d4b60c313b"></a>

```c
size_t num_subgroups
```

相关声明：[num_subgroups](#aeeab53e8bd7ae4f36433c0d4b60c313b)。

子组数量。

## 20.2\_详细说明（Detailed Documentation）

<a id="aa934af2e197c129b1fcb1eea9359ea6d"></a>

### `member`

```c
union bt_cap_set_member bt_cap_commander_broadcast_reception_stop_member_param::member
```

协调集合或临时集合成员（Coordinated or ad-hoc set member）。

<a id="aeeab53e8bd7ae4f36433c0d4b60c313b"></a>

### `num_subgroups`

```c
size_t bt_cap_commander_broadcast_reception_stop_member_param::num_subgroups
```

子组数量。

<a id="a72d606f6a83b1c84aa41d9db22cb955a"></a>

### `src_id`

```c
uint8_t bt_cap_commander_broadcast_reception_stop_member_param::src_id
```

接收状态的音频源 ID（Source ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_set_member](P188_bt_cap_set_member_联合体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_bt_cap_commander_broadcast_reception_start_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_bt_cap_commander_broadcast_reception_stop_param_结构体.md)
