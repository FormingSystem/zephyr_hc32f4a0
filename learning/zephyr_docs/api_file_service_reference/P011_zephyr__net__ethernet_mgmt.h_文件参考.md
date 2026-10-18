---
id: learning.zephyr-docs.api-file-service-reference.page-11
title: zephyr__net__ethernet_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_net\_\_ethernet\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ethernet__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网管理（Ethernet Management）接口的公共头文件。

<a id="details"></a>

```c
#include <zephyr/net/ethernet.h>
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

以太网管理（Ethernet Management）接口的公共头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_ga07ea7707f01d0c34724e0a71c463f1ad"></a>

```c
void ethernet_mgmt_raise_carrier_on_event (struct net_if *iface)
```

相关声明：[ethernet_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga07ea7707f01d0c34724e0a71c463f1ad)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

以太网（Ethernet）连接时触发 `CARRIER_ON` 事件（Event）。

<a id="r_ga039b86d955331f483386b04ec51c3b4d"></a>

```c
void ethernet_mgmt_raise_carrier_off_event (struct net_if *iface)
```

相关声明：[ethernet_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga039b86d955331f483386b04ec51c3b4d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

以太网（Ethernet）断开连接时触发 `CARRIER_OFF` 事件（Event）。

<a id="r_gaf7fe2fdca74cd547a4d015bfe0dd7536"></a>

```c
void ethernet_mgmt_raise_vlan_enabled_event (struct net_if *iface, uint16_t tag)
```

相关声明：[ethernet_mgmt_raise_vlan_enabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gaf7fe2fdca74cd547a4d015bfe0dd7536)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

启用虚拟局域网（VLAN）时触发 `VLAN_ENABLED` 事件（Event）。

<a id="r_gac02c1f616aee2a7381aa6eebba3f799f"></a>

```c
void ethernet_mgmt_raise_vlan_disabled_event (struct net_if *iface, uint16_t tag)
```

相关声明：[ethernet_mgmt_raise_vlan_disabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gac02c1f616aee2a7381aa6eebba3f799f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

禁用虚拟局域网（VLAN）时触发 `VLAN_DISABLED` 事件（Event）。


## 11.2\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P246_ethernet_mgmt.h_源码浏览.md)
- [ethernet_mgmt_raise_carrier_on_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga07ea7707f01d0c34724e0a71c463f1ad)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [ethernet_mgmt_raise_carrier_off_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#ga039b86d955331f483386b04ec51c3b4d)
- [ethernet_mgmt_raise_vlan_enabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gaf7fe2fdca74cd547a4d015bfe0dd7536)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [ethernet_mgmt_raise_vlan_disabled_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__mgmt.html#gac02c1f616aee2a7381aa6eebba3f799f)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__gpio__ene-kb1200-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__comparator__fake_comp.h_文件参考.md)
