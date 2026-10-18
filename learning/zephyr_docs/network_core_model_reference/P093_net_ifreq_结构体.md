---
id: learning.zephyr-docs.network-core-model-reference.page-93
title: net_ifreq_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__ifreq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_net\_ifreq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__ifreq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接口描述（Interface Description）结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

接口描述（Interface Description）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_ad3147844bf168ff8f19893e89e3d04dd"></a>

```c
char ifr_name [NET_IFNAMSIZ]
```

相关声明：[ifr_name](#ad3147844bf168ff8f19893e89e3d04dd)。

网络接口名称（Network interface name）。

## 93.2\_详细说明（Detailed Documentation）

<a id="ad3147844bf168ff8f19893e89e3d04dd"></a>

### `ifr_name`

```c
char net_ifreq::ifr_name[NET_IFNAMSIZ]
```

网络接口名称（Network interface name）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_net_if_timestamp_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_net_in6_addr_结构体.md)
