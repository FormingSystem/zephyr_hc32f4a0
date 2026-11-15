---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-18
title: Wi-Fi 网络管理器 API（Network Manager API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_Wi-Fi 网络管理器 API（Network Manager API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__nm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi网络管理器（Network Manager）的API。

<a id="details"></a>

Wi-Fi 网络管理器 API（Network Manager API）。**引入版本（Since）：**3.5。**版本（Version）：**0.8.0。

<a id="header-files"></a>
<a id="files"></a>

## 18.1\_文件（Files）

<a id="r_wifi_5Fnm_2Eh"></a>

```c
file wifi_nm.h
```

相关声明：[wifi_nm.h](../api_file_network_device_reference/P044_zephyr__net__wifi_nm.h_文件参考.md)。

Wi-Fi网络管理器（Network Manager）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.2\_数据结构（Data Structures）

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

## 18.3\_枚举（Enumerations）

<a id="r_gadba91c7f3ef5027f7d2a01229372a1a1"></a>

```c
enum wifi_nm_iface_type { WIFI_TYPE_STA = 0 , WIFI_TYPE_SAP , WIFI_TYPE_MAX }
```

相关声明：[wifi_nm_iface_type](#gadba91c7f3ef5027f7d2a01229372a1a1)、[WIFI_TYPE_STA](#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468)、[WIFI_TYPE_SAP](#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345)、[WIFI_TYPE_MAX](#ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa)。

Wi-Fi 接口类型（Interface Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_ga781238fda024558c8ccb4cd8877467ed"></a>

```c
struct wifi_nm_instance * wifi_nm_get_instance (const char *name)
```

相关声明：[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_get_instance](#ga781238fda024558c8ccb4cd8877467ed)。

根据指定名称获取网络管理器（Network Manager）实例。

<a id="r_ga813b6b6cc227115e83b8e632dd39e6f3"></a>

```c
struct wifi_nm_instance * wifi_nm_get_instance_iface (struct net_if *iface)
```

相关声明：[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_get_instance_iface](#ga813b6b6cc227115e83b8e632dd39e6f3)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

根据指定接口获取网络管理器（Network Manager）实例。

<a id="r_ga6a598af94e36a1f4ade05d7a18c019f5"></a>

```c
unsigned char wifi_nm_get_type_iface (struct net_if *iface)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[wifi_nm_get_type_iface](#ga6a598af94e36a1f4ade05d7a18c019f5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取指定接口的 Wi-Fi 类型（Type）。

<a id="r_gaa89e5acfa5eebc9267aa7ed2ce3adc39"></a>

```c
bool wifi_nm_iface_is_sta (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_nm_iface_is_sta](#gaa89e5acfa5eebc9267aa7ed2ce3adc39)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否为 Wi-Fi 站点接口（Station Interface）。

<a id="r_ga963f646981e9a64c9e61659e40c9880e"></a>

```c
bool wifi_nm_iface_is_sap (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[wifi_nm_iface_is_sap](#ga963f646981e9a64c9e61659e40c9880e)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查接口是否为 Wi-Fi 软件接入点接口（Soft AP Interface）。

<a id="r_ga26edd4cbb045a87613b79f8edd8e9dbb"></a>

```c
int wifi_nm_register_mgd_iface (struct wifi_nm_instance *nm, struct net_if *iface)
```

相关声明：[wifi_nm_register_mgd_iface](#ga26edd4cbb045a87613b79f8edd8e9dbb)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注册受管理的接口（Managed Interface）。

<a id="r_gafea087a6c50d6ad05933ef62546868d6"></a>

```c
int wifi_nm_register_mgd_type_iface (struct wifi_nm_instance *nm, enum wifi_nm_iface_type type, struct net_if *iface)
```

相关声明：[wifi_nm_register_mgd_type_iface](#gafea087a6c50d6ad05933ef62546868d6)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[wifi_nm_iface_type](#gadba91c7f3ef5027f7d2a01229372a1a1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注册受管理的接口（Managed Interface）。

<a id="r_ga467b630fa57bb5587c0237b9cdf403ff"></a>

```c
int wifi_nm_unregister_mgd_iface (struct wifi_nm_instance *nm, struct net_if *iface)
```

相关声明：[wifi_nm_unregister_mgd_iface](#ga467b630fa57bb5587c0237b9cdf403ff)、[wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

注销受管理的接口（Managed Interface）。

## 18.5\_详细说明（Detailed Documentation）

<a id="gadba91c7f3ef5027f7d2a01229372a1a1"></a>

### `wifi_nm_iface_type`

```c
enum wifi_nm_iface_type
```

```c
#include <zephyr/net/wifi_nm.h>
```

Wi-Fi 接口类型（Interface Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WIFI_TYPE_STA` | IEEE 802.11 Wi-Fi 站点（Station）。 |
| `WIFI_TYPE_SAP` | IEEE 802.11 Wi-Fi 软件接入点（Soft AP）。 |
| `WIFI_TYPE_MAX` | Wi-Fi 接口类型（Interface Type）的最大值。 |

<a id="ga781238fda024558c8ccb4cd8877467ed"></a>

### `wifi_nm_get_instance()`

```c
struct wifi_nm_instance * wifi_nm_get_instance ( const char * name)
```

```c
#include <zephyr/net/wifi_nm.h>
```

根据指定名称获取网络管理器（Network Manager）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 网络管理器实例名称（Network manager instance name）。 |

<a id="ga813b6b6cc227115e83b8e632dd39e6f3"></a>

### `wifi_nm_get_instance_iface()`

```c
struct wifi_nm_instance * wifi_nm_get_instance_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/wifi_nm.h>
```

根据指定接口获取网络管理器（Network Manager）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接口（Interface）。 |

<a id="ga6a598af94e36a1f4ade05d7a18c019f5"></a>

### `wifi_nm_get_type_iface()`

```c
unsigned char wifi_nm_get_type_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/wifi_nm.h>
```

获取指定接口的 Wi-Fi 类型（Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接口（Interface）。 |

<a id="ga963f646981e9a64c9e61659e40c9880e"></a>

### `wifi_nm_iface_is_sap()`

```c
bool wifi_nm_iface_is_sap ( struct net_if * iface)
```

```c
#include <zephyr/net/wifi_nm.h>
```

检查接口是否为 Wi-Fi 软件接入点接口（Soft AP Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接口（Interface）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 接口为 Wi-Fi 软件接入点接口（Soft AP Interface）时。 |

<a id="gaa89e5acfa5eebc9267aa7ed2ce3adc39"></a>

### `wifi_nm_iface_is_sta()`

```c
bool wifi_nm_iface_is_sta ( struct net_if * iface)
```

```c
#include <zephyr/net/wifi_nm.h>
```

检查接口是否为 Wi-Fi 站点接口（Station Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接口（Interface）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 接口为 Wi-Fi 站点接口（Station Interface）时。 |

<a id="ga26edd4cbb045a87613b79f8edd8e9dbb"></a>

### `wifi_nm_register_mgd_iface()`

```c
int wifi_nm_register_mgd_iface ( struct wifi_nm_instance * nm, struct net_if * iface )
```

```c
#include <zephyr/net/wifi_nm.h>
```

注册受管理的接口（Managed Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nm` | 指向网络管理器（Network Manager）实例的指针。 |
| `iface` | 受管理的接口（Managed Interface）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 传入无效参数时。 |
| `-ENOTSUP` | 接口不是 Wi-Fi 接口时。 |
| `-ENOMEM` | 达到受管理接口（Managed Interfaces）数量上限时。 |

<a id="gafea087a6c50d6ad05933ef62546868d6"></a>

### `wifi_nm_register_mgd_type_iface()`

```c
int wifi_nm_register_mgd_type_iface ( struct wifi_nm_instance * nm, enum wifi_nm_iface_type type, struct net_if * iface )
```

```c
#include <zephyr/net/wifi_nm.h>
```

注册受管理的接口（Managed Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nm` | 指向网络管理器（Network Manager）实例的指针。 |
| `type` | Wi-Fi 类型（Type）。 |
| `iface` | 受管理的接口（Managed Interface）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EINVAL` | 传入无效参数时。 |
| `-ENOTSUP` | 接口不是 Wi-Fi 接口时。 |
| `-ENOMEM` | 达到受管理接口（Managed Interfaces）数量上限时。 |

<a id="ga467b630fa57bb5587c0237b9cdf403ff"></a>

### `wifi_nm_unregister_mgd_iface()`

```c
int wifi_nm_unregister_mgd_iface ( struct wifi_nm_instance * nm, struct net_if * iface )
```

```c
#include <zephyr/net/wifi_nm.h>
```

注销受管理的接口（Managed Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nm` | 指向网络管理器（Network Manager）实例的指针。 |
| `iface` | 接口（Interface）。 |

**返回（Returns）**：**返回值（Returns）：**返回 `int`；成功为 0，参数无效为 `-EINVAL`，接口未向网络管理器注册为 `-ENOENT`。


## 18.6\_原页交叉引用（Cross References）

- [wifi_nm.h](../api_file_network_device_reference/P044_zephyr__net__wifi_nm.h_文件参考.md)
- [wifi_nm_mgd_iface](../network_core_model_reference/P179_wifi_nm_mgd_iface_结构体.md)
- [wifi_nm_instance](../network_core_model_reference/P178_wifi_nm_instance_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468"></a>
<a id="ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345"></a>
<a id="ggadba91c7f3ef5027f7d2a01229372a1a1a43ada3c4512ea29c8a40ec9780d47afa"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_虚拟局域网（Virtual LAN）定义与辅助工具。.md) · [返回大纲](大纲.md) · [下一章](P019_Xen 扩展区域（Extended regions）.md)
