---
id: learning.zephyr-docs.api-file-storage-event-reference.page-14
title: zephyr__net__mdns_responder.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_net\_\_mdns\_responder.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mdns__responder_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组播DNS（mDNS）响应器的API。

<a id="details"></a>

```c
#include <stddef.h>
#include <errno.h>
#include <zephyr/net/dns_sd.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

多播 DNS（mDNS）响应器（Responder）API。本文件包含用于注册 mDNS 记录（Records）的响应器 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.1\_函数（Functions）

<a id="r_a4682ee30bf3e739790dbcaede5485777"></a>

```c
int mdns_responder_set_ext_records (const struct dns_sd_rec *records, size_t count)
```

相关声明：[mdns_responder_set_ext_records](#a4682ee30bf3e739790dbcaede5485777)、[dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)。

注册连续内存中的 `dns_sd_rec` 记录（Records）。

<a id="r_ae8b53e59ec3e159e34ffda276a2f72dc"></a>

```c
int mdns_responder_enable_iface (struct net_if *iface)
```

相关声明：[mdns_responder_enable_iface](#ae8b53e59ec3e159e34ffda276a2f72dc)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在运行时（Runtime）为指定网络接口启用 mDNS 响应器（Responder）。

<a id="r_a085957294062f9948c213070dc912a34"></a>

```c
int mdns_responder_disable_iface (struct net_if *iface)
```

相关声明：[mdns_responder_disable_iface](#a085957294062f9948c213070dc912a34)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

在运行时（Runtime）为指定网络接口禁用 mDNS 响应器（Responder）。

## 14.2\_详细说明（Detailed Documentation）

<a id="a085957294062f9948c213070dc912a34"></a>

### `mdns_responder_disable_iface()`

```c
int mdns_responder_disable_iface ( struct net_if * iface)
```

在运行时（Runtime）为指定网络接口禁用 mDNS 响应器（Responder）。

运行时设置覆盖给定接口的构建时接口策略（Build-time Interface Policy）。绑定到该接口的监听套接字会被关闭，并退出其 mDNS 多播组（Multicast Groups），因此不再回答该接口上的查询。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要禁用响应器（Responder）的网络接口。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 Kconfig 选项 `CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL` 时可用。

**返回（Returns）**：**返回值（Returns）：**成功为 `0`；`iface` 为 `NULL` 时为 `-EINVAL`；接口索引超出范围时为 `-ERANGE`；未启用运行时控制时为 `-ENOTSUP`。

<a id="ae8b53e59ec3e159e34ffda276a2f72dc"></a>

### `mdns_responder_enable_iface()`

```c
int mdns_responder_enable_iface ( struct net_if * iface)
```

在运行时（Runtime）为指定网络接口启用 mDNS 响应器（Responder）。

运行时设置覆盖给定接口的构建时接口策略（Build-time Interface Policy），即 `CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALL` 等选项。响应器监听套接字及多播组成员关系（Multicast Group Memberships）会重新配置，使到达该接口的查询得到回答。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要启用响应器（Responder）的网络接口。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 Kconfig 选项 `CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL` 时可用。

**返回（Returns）**：**返回值（Returns）：**成功为 `0`；`iface` 为 `NULL` 时为 `-EINVAL`；接口索引超出范围时为 `-ERANGE`；未启用运行时控制时为 `-ENOTSUP`。

<a id="a4682ee30bf3e739790dbcaede5485777"></a>

### `mdns_responder_set_ext_records()`

```c
int mdns_responder_set_ext_records ( const struct dns_sd_rec * records, size_t count )
```

注册连续内存中的 `dns_sd_rec` 记录（Records）。

mDNS 响应器先遍历使用 `DNS_SD_REGISTER_SERVICE` 注册的记录（如果存在），再遍历外部记录（External Records）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `records` | 指向 mDNS 记录数组（Records Array）的指针。内部只存储该指针，不复制内容，因此其指向的数据必须保持有效。要注销记录，可传入 `NULL` 并将数量设为 `0`，例如在释放内存块之前这样做。本调用会等待正在进行的响应停止使用这些记录。 |
| `count` | 元素数量（Number of Elements）；仅当 `records` 为 `NULL` 时可为 `0`。 |

**返回（Returns）**：**返回值（Returns）：**成功为 `0`；`records` 为 `NULL` 而 `count` 非零，或 `records` 非 `NULL` 而 `count` 为零时，返回 `-EINVAL`。


## 14.3\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/net/dns_sd.h](../api_source_reference/P144_dns_sd.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P109_mdns_responder.h_源码浏览.md)
- [dns_sd_rec](../network_application_model_reference/P025_dns_sd_rec_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL)
- [CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALL)
- [DNS_SD_REGISTER_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html#ga0c0060a680d5c4fe56f2815c920c3627)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_zephyr__dt-bindings__sensor__lps2xdf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__net__net_mgmt.h_文件参考.md)
