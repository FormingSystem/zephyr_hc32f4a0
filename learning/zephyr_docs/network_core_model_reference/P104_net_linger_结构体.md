---
id: learning.zephyr-docs.network-core-model-reference.page-104
title: net_linger_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__linger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_net\_linger\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__linger.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

套接字选项SO_LINGER使用的延迟关闭选项（Linger Option）结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

套接字选项SO_LINGER使用的延迟关闭选项（Linger Option）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 104.1\_数据成员（Data Fields）

<a id="r_a8e93ff6b67e724cb24de03c21c5f99af"></a>

```c
int l_onoff
```

相关声明：[l_onoff](#a8e93ff6b67e724cb24de03c21c5f99af)。

是否启用延迟关闭行为（Linger behaviour）。

<a id="r_a9dab7be2bea49133c219cdfb154e9fdf"></a>

```c
int l_linger
```

相关声明：[l_linger](#a9dab7be2bea49133c219cdfb154e9fdf)。

延迟关闭时间（Linger time），单位为秒。

## 104.2\_详细说明（Detailed Documentation）

<a id="a9dab7be2bea49133c219cdfb154e9fdf"></a>

### `l_linger`

```c
int net_linger::l_linger
```

延迟关闭时间（Linger time），单位为秒。

<a id="a8e93ff6b67e724cb24de03c21c5f99af"></a>

### `l_onoff`

```c
int net_linger::l_onoff
```

是否启用延迟关闭行为（Linger behaviour）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 104.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P103_net_l2_结构体.md) · [返回大纲](大纲.md) · [下一章](P105_net_linkaddr_结构体.md)
