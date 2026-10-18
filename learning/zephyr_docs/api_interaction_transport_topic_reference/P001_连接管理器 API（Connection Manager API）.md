---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-1
title: 连接管理器 API（Connection Manager API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_连接管理器 API（Connection Manager API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器 API（Connection Manager API）

<a id="details"></a>

连接管理器 API（Connection Manager API）。**引入版本（Since）：**2.0。**版本（Version）：**0.1.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_gacdde95f41f32e7a829d8cd3a6d0e2277"></a>

```c
void conn_mgr_mon_resend_status (void)
```

相关声明：[conn_mgr_mon_resend_status](#gacdde95f41f32e7a829d8cd3a6d0e2277)。

根据当前是否具备网络连通性（connectivity），重新发送 `NET_L4_CONNECTED` 或 `NET_L4_DISCONNECTED`。

<a id="r_ga7bad393c43a24df7a03176830b05b288"></a>

```c
void conn_mgr_ignore_iface (struct net_if *iface)
```

相关声明：[conn_mgr_ignore_iface](#ga7bad393c43a24df7a03176830b05b288)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

将网络接口（iface）标记为由 `conn_mgr` 忽略。

<a id="r_gacc8735b835dea9b31531fcca9fe8a979"></a>

```c
void conn_mgr_watch_iface (struct net_if *iface)
```

相关声明：[conn_mgr_watch_iface](#gacc8735b835dea9b31531fcca9fe8a979)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

监视网络接口，即停止忽略该接口。

<a id="r_gada16a88ec2c1db71fc39782b0696dac2"></a>

```c
bool conn_mgr_is_iface_ignored (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_is_iface_ignored](#gada16a88ec2c1db71fc39782b0696dac2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查所提供网络接口当前是否被忽略。

<a id="r_ga6bd1ee46dc2e3dae554fce49e82c6187"></a>

```c
void conn_mgr_ignore_l2 (const struct net_l2 *l2)
```

相关声明：[conn_mgr_ignore_l2](#ga6bd1ee46dc2e3dae554fce49e82c6187)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

将第二层（L2）标记为由 `conn_mgr` 忽略。

<a id="r_gad96056478dcbcb568dd2ef8d5d2ad50b"></a>

```c
void conn_mgr_watch_l2 (const struct net_l2 *l2)
```

相关声明：[conn_mgr_watch_l2](#gad96056478dcbcb568dd2ef8d5d2ad50b)、[net_l2](../network_core_model_reference/P103_net_l2_结构体.md)。

监视 L2，即停止忽略该 L2。

## 1.2\_详细说明（Detailed Documentation）

<a id="ga7bad393c43a24df7a03176830b05b288"></a>

### `conn_mgr_ignore_iface()`

```c
void conn_mgr_ignore_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

将网络接口（iface）标记为由 `conn_mgr` 忽略。

忽略接口（Ignore an Interface）会强制 `conn_mgr` 将其视为未就绪／未连接。

因此不再发出该接口连接／断开相关事件；若接口在被忽略之前已连接，则此时会发出事件，如同它刚刚断开。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要忽略的接口（Interface）。 |

<a id="ga6bd1ee46dc2e3dae554fce49e82c6187"></a>

### `conn_mgr_ignore_l2()`

```c
void conn_mgr_ignore_l2 ( const struct net_l2 * l2)
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

将第二层（L2）标记为由 `conn_mgr` 忽略。

这是 `conn_mgr_ignore_iface` 的包装器，用于忽略所有使用指定二层（L2）的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `l2` | 要忽略的二层（L2）。 |

<a id="gada16a88ec2c1db71fc39782b0696dac2"></a>

### `conn_mgr_is_iface_ignored()`

```c
bool conn_mgr_is_iface_ignored ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

检查所提供网络接口当前是否被忽略。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 要检查的接口（Interface）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 接口正被 `conn_mgr` 忽略时。 |
| `false` | 接口正由 `conn_mgr` 监视（Watched）时。 |

<a id="gacdde95f41f32e7a829d8cd3a6d0e2277"></a>

### `conn_mgr_mon_resend_status()`

```c
void conn_mgr_mon_resend_status ( void )
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

根据当前是否具备网络连通性（connectivity），重新发送 `NET_L4_CONNECTED` 或 `NET_L4_DISCONNECTED`。

<a id="gacc8735b835dea9b31531fcca9fe8a979"></a>

### `conn_mgr_watch_iface()`

```c
void conn_mgr_watch_iface ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

监视网络接口，即停止忽略该接口。

不再强制 `conn_mgr` 将该接口视为未就绪／未连接。

不再阻止该接口连接／断开相关事件；若接口在开始监视之前已连接，则此时会发出事件，如同它刚刚连接。

启动时默认监视（Watch）所有接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 不再忽略的接口（Interface）。 |

<a id="gad96056478dcbcb568dd2ef8d5d2ad50b"></a>

### `conn_mgr_watch_l2()`

```c
void conn_mgr_watch_l2 ( const struct net_l2 * l2)
```

```c
#include <zephyr/net/conn_mgr_monitor.h>
```

监视 L2，即停止忽略该 L2。

这是 `conn_mgr_watch_iface` 的包装器，用于监视所有使用指定二层（L2）的接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `l2` | 要监视的二层（L2）。 |


## 1.3\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_l2](../network_core_model_reference/P103_net_l2_结构体.md)
- [zephyr/net/conn_mgr_monitor.h](../api_file_management_reference/P006_zephyr__net__conn_mgr_monitor.h_文件参考.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_FT9001 IOCTRL 寄存器偏移量（Register offsets）.md)
