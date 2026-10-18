---
id: learning.zephyr-docs.api-file-network-device-reference.page-44
title: zephyr__net__wifi_nm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_net\_\_wifi\_nm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi__nm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi网络管理器（Network Manager）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/wifi_mgmt.h>
```

查看此文件的源码。

Wi-Fi 网络管理器 API（Network Manager API）。本文件包含这些 API，网络管理应用程序可用它们注册为 Wi-Fi 网络管理器。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 44.1\_数据结构（Data Structures）

<a id="r_wifi_5Fnm_5Fmgd_5Fiface"></a>

```c
struct wifi_nm_mgd_iface
```

相关声明：[wifi_nm_mgd_iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md)。

Wi-Fi网络管理的接口（Network Managed Interfaces）。

<a id="r_wifi_5Fnm_5Finstance"></a>

```c
struct wifi_nm_instance
```

相关声明：[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)。

Wi-Fi网络管理器（Network Manager）的实例。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 44.2\_枚举（Enumerations）

<a id="r_gadba91c7f3ef5027f7d2a01229372a1a1"></a>

```c
enum wifi_nm_iface_type { WIFI_TYPE_STA = 0 , WIFI_TYPE_SAP , WIFI_TYPE_MAX }
```

相关声明：[wifi_nm_iface_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gadba91c7f3ef5027f7d2a01229372a1a1)、[WIFI_TYPE_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468)、[WIFI_TYPE_SAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345)、[WIFI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa)。

Wi-Fi 接口类型（Interface Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 44.3\_函数（Functions）

<a id="r_ga781238fda024558c8ccb4cd8877467ed"></a>

```c
struct wifi_nm_instance * wifi_nm_get_instance (const char *name)
```

相关声明：[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_get_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga781238fda024558c8ccb4cd8877467ed)。

根据指定名称获取网络管理器（Network Manager）实例。

<a id="r_ga813b6b6cc227115e83b8e632dd39e6f3"></a>

```c
struct wifi_nm_instance * wifi_nm_get_instance_iface (struct net_if *iface)
```

相关声明：[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_get_instance_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga813b6b6cc227115e83b8e632dd39e6f3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指定接口获取网络管理器（Network Manager）实例。

<a id="r_ga6a598af94e36a1f4ade05d7a18c019f5"></a>

```c
unsigned char wifi_nm_get_type_iface (struct net_if *iface)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[wifi_nm_get_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga6a598af94e36a1f4ade05d7a18c019f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指定接口的 Wi-Fi 类型（Type）。

<a id="r_gaa89e5acfa5eebc9267aa7ed2ce3adc39"></a>

```c
bool wifi_nm_iface_is_sta (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_nm_iface_is_sta](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gaa89e5acfa5eebc9267aa7ed2ce3adc39)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否为 Wi-Fi 站点接口（Station Interface）。

<a id="r_ga963f646981e9a64c9e61659e40c9880e"></a>

```c
bool wifi_nm_iface_is_sap (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_nm_iface_is_sap](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga963f646981e9a64c9e61659e40c9880e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否为 Wi-Fi 软件接入点接口（Soft AP Interface）。

<a id="r_ga26edd4cbb045a87613b79f8edd8e9dbb"></a>

```c
int wifi_nm_register_mgd_iface (struct wifi_nm_instance *nm, struct net_if *iface)
```

相关声明：[wifi_nm_register_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga26edd4cbb045a87613b79f8edd8e9dbb)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注册受管理的接口（Managed Interface）。

<a id="r_gafea087a6c50d6ad05933ef62546868d6"></a>

```c
int wifi_nm_register_mgd_type_iface (struct wifi_nm_instance *nm, enum wifi_nm_iface_type type, struct net_if *iface)
```

相关声明：[wifi_nm_register_mgd_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gafea087a6c50d6ad05933ef62546868d6)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_iface_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gadba91c7f3ef5027f7d2a01229372a1a1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注册受管理的接口（Managed Interface）。

<a id="r_ga467b630fa57bb5587c0237b9cdf403ff"></a>

```c
int wifi_nm_unregister_mgd_iface (struct wifi_nm_instance *nm, struct net_if *iface)
```

相关声明：[wifi_nm_unregister_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga467b630fa57bb5587c0237b9cdf403ff)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注销受管理的接口（Managed Interface）。


## 44.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/wifi_mgmt.h](../api_source_http_wifi_reference/P009_wifi_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P919_wifi_nm.h_源码浏览.md)
- [wifi_nm_mgd_iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md)
- [wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)
- [wifi_nm_iface_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gadba91c7f3ef5027f7d2a01229372a1a1)
- [WIFI_TYPE_STA](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468)
- [WIFI_TYPE_SAP](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345)
- [WIFI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa)
- [wifi_nm_get_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga781238fda024558c8ccb4cd8877467ed)
- [wifi_nm_get_instance_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga813b6b6cc227115e83b8e632dd39e6f3)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [wifi_nm_get_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga6a598af94e36a1f4ade05d7a18c019f5)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [wifi_nm_iface_is_sta](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gaa89e5acfa5eebc9267aa7ed2ce3adc39)
- [wifi_nm_iface_is_sap](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga963f646981e9a64c9e61659e40c9880e)
- [wifi_nm_register_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga26edd4cbb045a87613b79f8edd8e9dbb)
- [wifi_nm_register_mgd_type_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#gafea087a6c50d6ad05933ef62546868d6)
- [wifi_nm_unregister_mgd_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html#ga467b630fa57bb5587c0237b9cdf403ff)

<a id="header-details"></a>

---

[上一章](P043_zephyr__net__wifi_certs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_mock.h_文件参考.md)
