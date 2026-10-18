---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-4
title: 连接管理器连接性批量 API（Connectivity Bulk API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_连接管理器连接性批量 API（Connectivity Bulk API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity__bulk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器批量 API（Bulk API）

<a id="details"></a>

连接管理器批量 API（Connection Manager Bulk API）。**引入版本（Since）：**3.4。**版本（Version）：**0.1.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.1\_函数（Functions）

<a id="r_ga9e006b8b5095c223d77055fd619710c3"></a>

```c
int conn_mgr_all_if_up (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_up](#ga9e006b8b5095c223d77055fd619710c3)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理启用（Admin-up）状态的便捷函数。

<a id="r_gabf6f8e5d8ce51b4c1cbf48f18a57efb2"></a>

```c
int conn_mgr_all_if_down (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_down](#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理停用（Admin-down）状态的便捷函数。

<a id="r_ga48e3c1b98f505af9f8ac811a25f94e1b"></a>

```c
int conn_mgr_all_if_connect (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_connect](#ga48e3c1b98f505af9f8ac811a25f94e1b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将所有可用网络接口设为管理启用（Admin-up）状态，并连接其中支持连接功能（Connectivity）的接口的便捷函数。

<a id="r_ga3ce45d9040d3799e1387776257dfa8b7"></a>

```c
int conn_mgr_all_if_disconnect (bool skip_ignored)
```

相关声明：[conn_mgr_all_if_disconnect](#ga3ce45d9040d3799e1387776257dfa8b7)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

断开所有支持连接功能（Connectivity）的可用网络接口的便捷函数；不会将接口置于管理停用（Admin-down）状态，除非该接口启用了自动停用（Auto-down）。

## 4.2\_详细说明（Detailed Documentation）

<a id="ga48e3c1b98f505af9f8ac811a25f94e1b"></a>

### `conn_mgr_all_if_connect()`

```c
int conn_mgr_all_if_connect ( bool skip_ignored)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

将所有可用网络接口设为管理启用（Admin-up）状态，并连接其中支持连接功能（Connectivity）的接口的便捷函数。

本质上是 `net_if_up` 和 `conn_mgr_if_connect` 的包装器（Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `skip_ignored` | 若为 `true`，仅影响未被 `conn_mgr` 忽略的接口；否则影响所有接口。 |

**返回（Returns）**：**返回值（Returns）：**若所有 `net_if_up` 和 `conn_mgr_if_connect` 调用都返回 0，则返回 0；否则返回这两者首次返回的非零值。

<a id="ga3ce45d9040d3799e1387776257dfa8b7"></a>

### `conn_mgr_all_if_disconnect()`

```c
int conn_mgr_all_if_disconnect ( bool skip_ignored)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

断开所有支持连接功能（Connectivity）的可用网络接口的便捷函数；不会将接口置于管理停用（Admin-down）状态，除非该接口启用了自动停用（Auto-down）。

本质上是 `net_if_down` 的包装器（Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `skip_ignored` | 若为 `true`，仅影响未被 `conn_mgr` 忽略的接口；否则影响所有接口。 |

**返回（Returns）**：**返回值（Returns）：**若所有 `net_if_down` 调用都返回 0，则返回 0；否则返回首次出现的非零返回值。

<a id="gabf6f8e5d8ce51b4c1cbf48f18a57efb2"></a>

### `conn_mgr_all_if_down()`

```c
int conn_mgr_all_if_down ( bool skip_ignored)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

将所有可用网络接口设为管理停用（Admin-down）状态的便捷函数。

本质上是 `net_if_down` 的包装器（Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `skip_ignored` | 若为 `true`，仅影响未被 `conn_mgr` 忽略的接口；否则影响所有接口。 |

**返回（Returns）**：**返回值（Returns）：**若所有 `net_if_down` 调用都返回 0，则返回 0；否则返回首次出现的非零返回值。

<a id="ga9e006b8b5095c223d77055fd619710c3"></a>

### `conn_mgr_all_if_up()`

```c
int conn_mgr_all_if_up ( bool skip_ignored)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

将所有可用网络接口设为管理启用（Admin-up）状态的便捷函数。

本质上是 `net_if_up` 的包装器（Wrapper）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `skip_ignored` | 若为 `true`，仅影响未被 `conn_mgr` 忽略的接口；否则影响所有接口。 |

**返回（Returns）**：**返回值（Returns）：**若所有 `net_if_up` 调用都返回 0，则返回 0；否则返回首次出现的非零返回值。


## 4.3\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/conn_mgr_connectivity.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__connectivity_8h.html)
- [net_if_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02644cc623fc7a8878c17d54984e4210)
- [conn_mgr_if_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html#ga575d367c95592fd9f4ead694ff94543f)
- [net_if_down](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga2187650062d6139b9f4b81745a206803)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_瑞萨（Renesas）SmartBond.md) · [返回大纲](大纲.md) · [下一章](P005_Realtek RTS5817中断源（Interrupt Sources）.md)
