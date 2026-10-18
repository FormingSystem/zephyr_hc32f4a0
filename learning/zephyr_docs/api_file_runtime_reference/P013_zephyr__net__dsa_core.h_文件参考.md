---
id: learning.zephyr-docs.api-file-runtime-reference.page-13
title: zephyr__net__dsa_core.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_net\_\_dsa\_core.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（Distributed Switch Architecture，DSA）。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/phy.h>
#include <zephyr/net/ethernet.h>
```

查看此文件的源码。

分布式交换架构（Distributed Switch Architecture，DSA）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_dsa_5Fswitch_5Fcontext"></a>

```c
struct dsa_switch_context
```

相关声明：[dsa_switch_context](../network_service_model_reference/P004_dsa_switch_context_结构体.md)。

分布式交换架构（DSA）交换机的上下文数据。

<a id="r_dsa_5Fapi"></a>

```c
struct dsa_api
```

相关声明：[dsa_api](../network_service_model_reference/P002_dsa_api_结构体.md)。

提供分布式交换架构（DSA）交换机API回调的结构；它扩展了struct ethernet_api。

<a id="r_dsa_5Fport_5Fconfig"></a>

```c
struct dsa_port_config
```

相关声明：[dsa_port_config](../network_service_model_reference/P003_dsa_port_config_结构体.md)。

分布式交换架构（DSA）的端口配置结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_ga012eeda4facb67b5c387b74878b53188"></a>

```c
#define DSA_PORT_INST_INIT(port, n, cfg)
```

相关声明：[DSA_PORT_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#ga012eeda4facb67b5c387b74878b53188)。

用于分布式交换架构端口实例初始化（DSA Port Instance Initialization）的宏（Macro）。

<a id="r_gaa7665e4b96cbc40cbae6de621f773aa4"></a>

```c
#define DSA_SWITCH_INST_INIT(n, _dapi, data, fn)
```

相关声明：[DSA_SWITCH_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#gaa7665e4b96cbc40cbae6de621f773aa4)。

用于分布式交换架构交换机实例初始化（DSA Switch Instance Initialization）的宏（Macro）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.3\_函数（Functions）

<a id="r_ga16d03129d1e4c39f8662dae4b35598d9"></a>

```c
struct net_if * dsa_user_get_iface (struct net_if *iface, int port_idx)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[dsa_user_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#ga16d03129d1e4c39f8662dae4b35598d9)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取用户端口（User Port）的网络接口（Network Interface）。


## 13.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/phy.h](../api_source_supplement_reference/P142_phy.h_源码浏览.md)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html)
- [dsa_switch_context](../network_service_model_reference/P004_dsa_switch_context_结构体.md)
- [dsa_api](../network_service_model_reference/P002_dsa_api_结构体.md)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [dsa_port_config](../network_service_model_reference/P003_dsa_port_config_结构体.md)
- [DSA_PORT_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#ga012eeda4facb67b5c387b74878b53188)
- [DSA_SWITCH_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#gaa7665e4b96cbc40cbae6de621f773aa4)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [dsa_user_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#ga16d03129d1e4c39f8662dae4b35598d9)

<a id="header-details"></a>

---

[上一章](P012_zephyr__drivers__sensor__icm4268x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__mgmt__hawkbit__event.h_文件参考.md)
