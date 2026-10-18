---
id: learning.zephyr-docs.network-core-model-reference.page-52
title: net_cmsghdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__cmsghdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_net\_cmsghdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__cmsghdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

控制消息辅助数据（Control Message Ancillary Data）。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

控制消息辅助数据（Control Message Ancillary Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a306a55e0b7ab30d6258c71e92566f727"></a>

```c
net_socklen_t cmsg_len
```

相关声明：[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[cmsg_len](#a306a55e0b7ab30d6258c71e92566f727)。

包含头部（Header）在内的字节数。

<a id="r_a3f8abb9fbf85597c885ac045df9492b5"></a>

```c
int cmsg_level
```

相关声明：[cmsg_level](#a3f8abb9fbf85597c885ac045df9492b5)。

来源协议（Originating Protocol）。

<a id="r_aa44e7136defe85d81bec20aa00cc6668"></a>

```c
int cmsg_type
```

相关声明：[cmsg_type](#aa44e7136defe85d81bec20aa00cc6668)。

协议专用类型（Protocol-Specific Type）。

<a id="r_aee333d1c9f262de2135a9bed3bca1d98"></a>

```c
z_max_align_t cmsg_data []
```

相关声明：[cmsg_data](#aee333d1c9f262de2135a9bed3bca1d98)。

用于强制net_cmsghdr对齐的柔性数组成员（Flexible Array Member）。

## 52.2\_详细说明（Detailed Documentation）

<a id="aee333d1c9f262de2135a9bed3bca1d98"></a>

### `cmsg_data`

```c
z_max_align_t net_cmsghdr::cmsg_data[]
```

用于强制net_cmsghdr对齐的柔性数组成员（Flexible Array Member）。

<a id="a306a55e0b7ab30d6258c71e92566f727"></a>

### `cmsg_len`

```c
net_socklen_t net_cmsghdr::cmsg_len
```

包含头部（Header）在内的字节数。

<a id="a3f8abb9fbf85597c885ac045df9492b5"></a>

### `cmsg_level`

```c
int net_cmsghdr::cmsg_level
```

来源协议（Originating Protocol）。

<a id="aa44e7136defe85d81bec20aa00cc6668"></a>

### `cmsg_type`

```c
int net_cmsghdr::cmsg_type
```

协议专用类型（Protocol-Specific Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [net_cmsghdr](P052_net_cmsghdr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_net_capture_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_net_config_ssh_key_结构体.md)
