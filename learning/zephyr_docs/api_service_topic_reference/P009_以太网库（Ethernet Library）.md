---
id: learning.zephyr-docs.api-service-topic-reference.page-9
title: 以太网库（Ethernet Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_以太网库（Ethernet Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网库（Ethernet library）

<a id="details"></a>

以太网库（Ethernet Library）。

自 1.12 版提供（Since 1.12）；接口版本（Version）0.8.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_ga07ea7707f01d0c34724e0a71c463f1ad"></a>

```c
void ethernet_mgmt_raise_carrier_on_event (struct net_if *iface)
```

相关声明：[ethernet_mgmt_raise_carrier_on_event](#ga07ea7707f01d0c34724e0a71c463f1ad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

以太网（Ethernet）连接时触发 `CARRIER_ON` 事件（Event）。

<a id="r_ga039b86d955331f483386b04ec51c3b4d"></a>

```c
void ethernet_mgmt_raise_carrier_off_event (struct net_if *iface)
```

相关声明：[ethernet_mgmt_raise_carrier_off_event](#ga039b86d955331f483386b04ec51c3b4d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

以太网（Ethernet）断开连接时触发 `CARRIER_OFF` 事件（Event）。

<a id="r_gaf7fe2fdca74cd547a4d015bfe0dd7536"></a>

```c
void ethernet_mgmt_raise_vlan_enabled_event (struct net_if *iface, uint16_t tag)
```

相关声明：[ethernet_mgmt_raise_vlan_enabled_event](#gaf7fe2fdca74cd547a4d015bfe0dd7536)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

启用虚拟局域网（VLAN）时触发 `VLAN_ENABLED` 事件（Event）。

<a id="r_gac02c1f616aee2a7381aa6eebba3f799f"></a>

```c
void ethernet_mgmt_raise_vlan_disabled_event (struct net_if *iface, uint16_t tag)
```

相关声明：[ethernet_mgmt_raise_vlan_disabled_event](#gac02c1f616aee2a7381aa6eebba3f799f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

禁用虚拟局域网（VLAN）时触发 `VLAN_DISABLED` 事件（Event）。

## 9.2\_详细说明（Detailed Documentation）

<a id="ga039b86d955331f483386b04ec51c3b4d"></a>

### `ethernet_mgmt_raise_carrier_off_event()`

```c
void ethernet_mgmt_raise_carrier_off_event ( struct net_if * iface)
```

```c
#include <zephyr/net/ethernet_mgmt.h>
```

以太网（Ethernet）断开连接时触发 `CARRIER_OFF` 事件（Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 以太网网络接口（Ethernet Network Interface）。 |

<a id="ga07ea7707f01d0c34724e0a71c463f1ad"></a>

### `ethernet_mgmt_raise_carrier_on_event()`

```c
void ethernet_mgmt_raise_carrier_on_event ( struct net_if * iface)
```

```c
#include <zephyr/net/ethernet_mgmt.h>
```

以太网（Ethernet）连接时触发 `CARRIER_ON` 事件（Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 以太网网络接口（Ethernet Network Interface）。 |

<a id="gac02c1f616aee2a7381aa6eebba3f799f"></a>

### `ethernet_mgmt_raise_vlan_disabled_event()`

```c
void ethernet_mgmt_raise_vlan_disabled_event ( struct net_if * iface, uint16_t tag )
```

```c
#include <zephyr/net/ethernet_mgmt.h>
```

禁用虚拟局域网（VLAN）时触发 `VLAN_DISABLED` 事件（Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 以太网网络接口（Ethernet Network Interface）。 |
| `tag` | 被禁用的虚拟局域网标签（VLAN Tag）。 |

<a id="gaf7fe2fdca74cd547a4d015bfe0dd7536"></a>

### `ethernet_mgmt_raise_vlan_enabled_event()`

```c
void ethernet_mgmt_raise_vlan_enabled_event ( struct net_if * iface, uint16_t tag )
```

```c
#include <zephyr/net/ethernet_mgmt.h>
```

启用虚拟局域网（VLAN）时触发 `VLAN_ENABLED` 事件（Event）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 以太网网络接口（Ethernet Network Interface）。 |
| `tag` | 被启用的虚拟局域网标签（VLAN Tag）。 |


## 9.3\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/net/ethernet_mgmt.h](../api_file_service_reference/P011_zephyr__net__ethernet_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_CS35L5X API主题.md) · [返回大纲](大纲.md) · [下一章](P010_FT8xx 内存映射（Memory map）.md)
