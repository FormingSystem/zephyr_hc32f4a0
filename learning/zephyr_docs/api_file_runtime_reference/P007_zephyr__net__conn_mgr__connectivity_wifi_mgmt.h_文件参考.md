---
id: learning.zephyr-docs.api-file-runtime-reference.page-7
title: zephyr__net__conn_mgr__connectivity_wifi_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_net\_\_conn\_mgr\_\_connectivity\_wifi\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/connectivity__wifi__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

为提供wifi_mgmt API的驱动实现连接功能（Connectivity Implementation）。

<a id="details"></a>

```c
#include <zephyr/net/conn_mgr_connectivity_impl.h>
```

查看此文件的源码。

为提供wifi_mgmt API的驱动实现连接功能（Connectivity Implementation）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_aa8d1b34502bfcc5c482265148a3bb67a"></a>

```c
#define CONNECTIVITY_WIFI_MGMT_CTX_TYPE void *
```

相关声明：[CONNECTIVITY_WIFI_MGMT_CTX_TYPE](#aa8d1b34502bfcc5c482265148a3bb67a)。

通用 `WIFI_MGMT` 连接后端（Connectivity Backend）的上下文类型（Context Type）。

<a id="r_a0c5f4f4ce3091c0a6e43292b095f7be3"></a>

```c
#define CONNECTIVITY_WIFI_MGMT_BIND(dev_id)
```

相关声明：[CONNECTIVITY_WIFI_MGMT_BIND](#a0c5f4f4ce3091c0a6e43292b095f7be3)。

将通用 `WIFI_MGMT` 实现与网络设备（Network Device）关联。

## 7.2\_详细说明（Detailed Documentation）

<a id="a0c5f4f4ce3091c0a6e43292b095f7be3"></a>

### `CONNECTIVITY_WIFI_MGMT_BIND`

```c
#define CONNECTIVITY_WIFI_MGMT_BIND ( dev_id)
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_NET_CONNECTION_MANAGER_CONNECTIVITY_WIFI_MGMT,  \
           (CONN_MGR_CONN_DECLARE_PUBLIC(CONNECTIVITY_WIFI_MGMT); \
            CONN_MGR_BIND_CONN(dev_id, CONNECTIVITY_WIFI_MGMT)))
```

将通用 `WIFI_MGMT` 实现与网络设备（Network Device）关联。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_id` | 网络设备标识（Network Device ID）。 |

<a id="aa8d1b34502bfcc5c482265148a3bb67a"></a>

### `CONNECTIVITY_WIFI_MGMT_CTX_TYPE`

```c
#define CONNECTIVITY_WIFI_MGMT_CTX_TYPE void *
```

通用 `WIFI_MGMT` 连接后端（Connectivity Backend）的上下文类型（Context Type）。


## 7.3\_原页交叉引用（Cross References）

- [zephyr/net/conn_mgr_connectivity_impl.h](../api_source_runtime_reference/P011_conn_mgr_connectivity_impl.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P114_connectivity_wifi_mgmt.h_源码浏览.md)
- [IF_ENABLED](../util_reference/P001_通用工具公共接口.md#gae67ffe50e848951dbde309ed569ea925)
- [CONN_MGR_CONN_DECLARE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__impl.html#ga519cfa66e1a1f0b769ce2bf61a61887f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__conn__mgr__connectivity__impl_html_ga519cfa66e1a1f0b769ce2bf61a61887f"></a>
<a id="agroup__sys-util_html_gae67ffe50e848951dbde309ed569ea925"></a>

---

[上一章](P006_zephyr__drivers__clock_control__clock_control_numicro.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__bluetooth__mesh__dfd.h_文件参考.md)
