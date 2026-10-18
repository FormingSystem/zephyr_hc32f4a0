---
id: learning.zephyr-docs.network-service-model-reference.page-18
title: gptp_phase_dis_cb_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__phase__dis__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_gptp\_phase\_dis\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__phase__dis__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

相位不连续（Phase Discontinuity）的回调结构。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

相位不连续（Phase discontinuity）回调结构体，保存相位不连续回调信息。调用方必须确保所指变量在注册的整个有效期内始终有效；通常意味着不能将该变量分配在栈上。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_a9801de29992ae2f23bbe89c417d58fe3"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a9801de29992ae2f23bbe89c417d58fe3)。

单向链表（Slist）的节点信息（Node information）。

<a id="r_a8294a9abac55d1f4406923ea4e8ed144"></a>

```c
gptp_phase_dis_callback_t cb
```

相关声明：[gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)、[cb](#a8294a9abac55d1f4406923ea4e8ed144)。

相位不连续回调。

## 18.2\_详细说明（Detailed Documentation）

<a id="a8294a9abac55d1f4406923ea4e8ed144"></a>

### `cb`

```c
gptp_phase_dis_callback_t gptp_phase_dis_cb::cb
```

相位不连续回调。

<a id="a9801de29992ae2f23bbe89c417d58fe3"></a>

### `node`

```c
sys_snode_t gptp_phase_dis_cb::node
```

单向链表（Slist）的节点信息（Node information）。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_gptp_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_gptp_port_identity_结构体.md)
