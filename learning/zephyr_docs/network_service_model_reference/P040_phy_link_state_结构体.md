---
id: learning.zephyr-docs.network-service-model-reference.page-40
title: phy_link_state_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structphy__link__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_phy\_link\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structphy__link__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

链路状态（Link State）。

```c
#include <zephyr/net/phy.h>
```

<a id="details"></a>

链路状态（Link State）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_ab47802265dcf47b0aa815f4579467b6f"></a>

```c
enum phy_link_speed speed
```

相关声明：[phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)、[speed](#ab47802265dcf47b0aa815f4579467b6f)。

链路速率（Link speed）。

<a id="r_aaced7164c07c5f964c952c2b04d68395"></a>

```c
bool is_up
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_up](#aaced7164c07c5f964c952c2b04d68395)。

为 `true` 表示链路活动且已连接。

## 40.2\_详细说明（Detailed Documentation）

<a id="aaced7164c07c5f964c952c2b04d68395"></a>

### `is_up`

```c
bool phy_link_state::is_up
```

为 `true` 表示链路活动且已连接。

<a id="ab47802265dcf47b0aa815f4579467b6f"></a>

### `speed`

```c
enum phy_link_speed phy_link_state::speed
```

链路速率（Link speed）。

本数据类型文档由以下文件生成：

- `zephyr/net/phy.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/net/phy.h](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h_source.html)
- [phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_openthread_state_changed_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_phy_plca_cfg_结构体.md)
