---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-4
title: 连接管理器连接性 API（Connectivity API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_连接管理器连接性 API（Connectivity API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__conn__mgr__connectivity.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理器连接性 API（Connectivity API）

<a id="details"></a>

连接管理器连接能力 API（Connection Manager Connectivity API）。起始版本（Since）：3.4。接口版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 4.1\_主题（Topics）

<a id="r_conn_5Fmgr_5Fconnectivity_5Fbulk"></a>

相关声明：[连接管理器连接性批量 API（Connectivity Bulk API）](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md)。

连接管理器批量 API（Bulk API）

<a id="r_conn_5Fmgr_5Fconnectivity_5Fimpl"></a>

相关声明：[连接管理器连接性实现 API（Connectivity Implementation API）](../api_input_runtime_topic_reference/P004_连接管理器连接性实现 API（Connectivity Implementation API）.md)。

连接管理器连接性实现 API（Connectivity Implementation API）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga5ea6e37ca9eda2b6fd8b165b8182dd38"></a>

```c
#define NET_EVENT_CONN_IF_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_TIMEOUT)
```

相关声明：[NET_EVENT_CONN_IF_TIMEOUT](#ga5ea6e37ca9eda2b6fd8b165b8182dd38)。

连接尝试超时（Connection Attempt Timeout）时产生的 `net_mgmt` 网络管理事件。

<a id="r_gae8f207559a7123bd2eca5ef08086d377"></a>

```c
#define NET_EVENT_CONN_IF_FATAL_ERROR (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_FATAL_ERROR)
```

相关声明：[NET_EVENT_CONN_IF_FATAL_ERROR](#gae8f207559a7123bd2eca5ef08086d377)。

接口发生不可恢复的连接错误（Non-recoverable Connectivity Error）时产生的 `net_mgmt` 事件。

<a id="r_gaaab7f33dcc175b4c9117d6c69a0c84c8"></a>

```c
#define NET_EVENT_CONN_IF_IDLE_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT)
```

相关声明：[NET_EVENT_CONN_IF_IDLE_TIMEOUT](#gaaab7f33dcc175b4c9117d6c69a0c84c8)。

接口因不活动（Inactivity）而超时时产生的 `net_mgmt` 事件。

<a id="r_gaa4b57ac324a2ac090751919c89c3f0cd"></a>

```c
#define NET_EVENT_CONN_IF_NO_CONFIGURATION (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION)
```

相关声明：[NET_EVENT_CONN_IF_NO_CONFIGURATION](#gaa4b57ac324a2ac090751919c89c3f0cd)。

接口因缺少配置而无法连接时产生的 `net_mgmt` 事件。

<a id="r_ga605eee24f4419b5cd6a50a0272979da7"></a>

```c
#define CONN_MGR_IF_NO_TIMEOUT 0
```

相关声明：[CONN_MGR_IF_NO_TIMEOUT](#ga605eee24f4419b5cd6a50a0272979da7)。

用于 `conn_mgr_if_set_timeout` 和 `conn_mgr_conn_binding::timeout` 的值，表示不设超时（No Timeout）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gaf10fb532a3dd07ec8c692a72643d0e3f"></a>

```c
enum conn_mgr_if_flag { CONN_MGR_IF_PERSISTENT , CONN_MGR_IF_NO_AUTO_CONNECT , CONN_MGR_IF_NO_AUTO_DOWN }
```

相关声明：[conn_mgr_if_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f)、[CONN_MGR_IF_PERSISTENT](#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f)、[CONN_MGR_IF_NO_AUTO_CONNECT](#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd)、[CONN_MGR_IF_NO_AUTO_DOWN](#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d)。

各接口的连接标志（Per-interface Connectivity Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga575d367c95592fd9f4ead694ff94543f"></a>

```c
int conn_mgr_if_connect (struct net_if *iface)
```

相关声明：[conn_mgr_if_connect](#ga575d367c95592fd9f4ead694ff94543f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

连接接口（Connect Interface）。

<a id="r_gada2b5271b3e5dbcab629e1538b3d8eb4"></a>

```c
int conn_mgr_if_disconnect (struct net_if *iface)
```

相关声明：[conn_mgr_if_disconnect](#gada2b5271b3e5dbcab629e1538b3d8eb4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

断开接口连接（Disconnect Interface）。

<a id="r_ga09a1169a89eac1a3291185281952ce05"></a>

```c
bool conn_mgr_if_is_bound (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_if_is_bound](#ga09a1169a89eac1a3291185281952ce05)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查所给网络接口（Network Interface）是否支持连接管理，即是否已绑定到某个连接实现（Connectivity Implementation）。

<a id="r_ga2a2e6d7fbb7b1ed0327706a8c253d3e4"></a>

```c
int conn_mgr_if_set_opt (struct net_if *iface, int optname, const void *optval, size_t optlen)
```

相关声明：[conn_mgr_if_set_opt](#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

<a id="r_gaa79794ce9c773c0c3932121c931ac2d6"></a>

```c
int conn_mgr_if_get_opt (struct net_if *iface, int optname, void *optval, size_t *optlen)
```

相关声明：[conn_mgr_if_get_opt](#gaa79794ce9c773c0c3932121c931ac2d6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

<a id="r_ga465c9491106cba3c9cb1cf296090612b"></a>

```c
bool conn_mgr_if_get_flag (struct net_if *iface, enum conn_mgr_if_flag flag)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[conn_mgr_if_get_flag](#ga465c9491106cba3c9cb1cf296090612b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[conn_mgr_if_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f)。

检查连接标志（Connectivity Flags）的值。

<a id="r_gae86d1c808f31b8ca5e67bacbc844ef47"></a>

```c
int conn_mgr_if_set_flag (struct net_if *iface, enum conn_mgr_if_flag flag, bool value)
```

相关声明：[conn_mgr_if_set_flag](#gae86d1c808f31b8ca5e67bacbc844ef47)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[conn_mgr_if_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置连接标志（Connectivity Flag）的值。

<a id="r_gada9c37847acc604d82604351cbbb5e64"></a>

```c
int conn_mgr_if_get_timeout (struct net_if *iface)
```

相关声明：[conn_mgr_if_get_timeout](#gada9c37847acc604d82604351cbbb5e64)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的连接超时（Connectivity Timeout）。

<a id="r_ga467ecbb330d21b8dfea3e0ce08448400"></a>

```c
int conn_mgr_if_set_timeout (struct net_if *iface, int timeout)
```

相关声明：[conn_mgr_if_set_timeout](#ga467ecbb330d21b8dfea3e0ce08448400)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置接口的连接超时（Connectivity Timeout）。

<a id="r_ga5d22b2a44c3595a5b7b240c8fe7d0db1"></a>

```c
int conn_mgr_if_get_idle_timeout (struct net_if *iface)
```

相关声明：[conn_mgr_if_get_idle_timeout](#ga5d22b2a44c3595a5b7b240c8fe7d0db1)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取接口的空闲超时（Idle Timeout）。

<a id="r_ga93f333199c87b2d7668e94c92efd31ce"></a>

```c
int conn_mgr_if_set_idle_timeout (struct net_if *iface, int timeout)
```

相关声明：[conn_mgr_if_set_idle_timeout](#ga93f333199c87b2d7668e94c92efd31ce)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

设置接口的空闲超时（Idle Timeout）。

<a id="r_ga4079113088236aede697538d79e5272f"></a>

```c
void conn_mgr_if_used (struct net_if *iface)
```

相关声明：[conn_mgr_if_used](#ga4079113088236aede697538d79e5272f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

通知连接管理器（Connection Manager）：该接口刚刚被使用。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga605eee24f4419b5cd6a50a0272979da7"></a>

### `CONN_MGR_IF_NO_TIMEOUT`

```c
#define CONN_MGR_IF_NO_TIMEOUT 0
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

用于 `conn_mgr_if_set_timeout` 和 `conn_mgr_conn_binding::timeout` 的值，表示不设超时（No Timeout）。

<a id="gae8f207559a7123bd2eca5ef08086d377"></a>

### `NET_EVENT_CONN_IF_FATAL_ERROR`

```c
#define NET_EVENT_CONN_IF_FATAL_ERROR (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_FATAL_ERROR)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

接口发生不可恢复的连接错误（Non-recoverable Connectivity Error）时产生的 `net_mgmt` 事件。

<a id="gaaab7f33dcc175b4c9117d6c69a0c84c8"></a>

### `NET_EVENT_CONN_IF_IDLE_TIMEOUT`

```c
#define NET_EVENT_CONN_IF_IDLE_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_IDLE_TIMEOUT)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

接口因不活动（Inactivity）而超时时产生的 `net_mgmt` 事件。

<a id="gaa4b57ac324a2ac090751919c89c3f0cd"></a>

### `NET_EVENT_CONN_IF_NO_CONFIGURATION`

```c
#define NET_EVENT_CONN_IF_NO_CONFIGURATION (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_NO_CONFIGURATION)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

接口因缺少配置而无法连接时产生的 `net_mgmt` 事件。

<a id="ga5ea6e37ca9eda2b6fd8b165b8182dd38"></a>

### `NET_EVENT_CONN_IF_TIMEOUT`

```c
#define NET_EVENT_CONN_IF_TIMEOUT (NET_MGMT_CONN_IF_EVENT | NET_EVENT_CONN_CMD_IF_TIMEOUT)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

连接尝试超时（Connection Attempt Timeout）时产生的 `net_mgmt` 网络管理事件。

<a id="gaf10fb532a3dd07ec8c692a72643d0e3f"></a>

### `conn_mgr_if_flag`

```c
enum conn_mgr_if_flag
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

各接口的连接标志（Per-interface Connectivity Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CONN_MGR_IF_PERSISTENT` | 保持连接（Persistent）。设置后，表示绑定到此 `iface` 的连接实现（Connectivity Implementation）应在连接丢失后自动重新连接，以尽量保持连接。 |
| `CONN_MGR_IF_NO_AUTO_CONNECT` | 禁止自动连接（No Auto-connect）。设置后，`iface` 达到管理启用状态（Admin-up）时，`conn_mgr` 不会自动尝试连接该接口。 |
| `CONN_MGR_IF_NO_AUTO_DOWN` | 禁止自动关闭接口（No Auto-down）。设置后，`conn_mgr` 停止尝试连接时，不会自动将 `iface` 置为管理关闭状态（Admin-down），即使启用了 `CONFIG_NET_CONNECTION_MANAGER_AUTO_IF_DOWN`。 |

<a id="ga575d367c95592fd9f4ead694ff94543f"></a>

### `conn_mgr_if_connect()`

```c
int conn_mgr_if_connect ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

连接接口（Connect Interface）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则发起网络连接／关联（Connect/Association）。

如果 `iface` 尚未处于管理启用状态（Admin-up），则通过调用 `net_if_up` 自动将其置为该状态。

非阻塞（Non-blocking）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ESHUTDOWN` | `iface` 未处于管理启用状态（Admin-up）时。 |
| `-ENOTSUP` | `iface` 没有连接实现（Connectivity Implementation）时。 |
| `-EAGAIN` | `iface` 没有建立连接所需的配置信息（Configuration Information）时。 |

**返回（Returns）**：返回值（Returns）：其他情况下返回实现特定状态码（Implementation-specific Status Code）。

<a id="gada2b5271b3e5dbcab629e1538b3d8eb4"></a>

### `conn_mgr_if_disconnect()`

```c
int conn_mgr_if_disconnect ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

断开接口连接（Disconnect Interface）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则使其断开网络连接／解除关联（Disconnect/Disassociate），并取消所有待处理的连接／关联尝试。

如果 `iface` 当前处于管理关闭状态（Admin-down），则不执行任何操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | `iface` 没有连接实现（Connectivity Implementation）时。 |

**返回（Returns）**：返回值（Returns）：其他情况下返回实现特定状态码（Implementation-specific Status Code）。

<a id="ga465c9491106cba3c9cb1cf296090612b"></a>

### `conn_mgr_if_get_flag()`

```c
bool conn_mgr_if_get_flag ( struct net_if * iface, enum conn_mgr_if_flag flag )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

检查连接标志（Connectivity Flags）的值。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则获取与该接口关联的指定连接标志（Connectivity Flag）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待检查网络接口（Network Interface）的指针。 |
| `flag` | 要检查的标志（Flag）。 |

**返回（Returns）**：返回值（Returns）：标志已设置时为 `True`，否则为 `False`。如果提供的 `iface` 未绑定连接实现（Connectivity Implementation），或请求的标志不存在，也返回 `False`。

<a id="ga5d22b2a44c3595a5b7b240c8fe7d0db1"></a>

### `conn_mgr_if_get_idle_timeout()`

```c
int conn_mgr_if_get_idle_timeout ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

获取接口的空闲超时（Idle Timeout）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则获取其空闲超时设置（Idle Timeout），以秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待检查 `iface` 的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，成功获取时为连接超时值（Connectivity Timeout），以秒为单位；否则为 `CONN_MGR_IF_NO_TIMEOUT`。

<a id="gaa79794ce9c773c0c3932121c931ac2d6"></a>

### `conn_mgr_if_get_opt()`

```c
int conn_mgr_if_get_opt ( struct net_if * iface, int optname, void * optval, size_t * optlen )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

获取由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

如果提供的 `iface` 已绑定支持此操作的连接实现（Connectivity Implementation），则获取与该接口相关的实现特定连接选项（Connectivity Options）。

无论是否返回错误，`optlen` 都会被设为实际写入的总字节数，即使未写入任何字节也如此。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `optname` | 表示要设置选项的整数值。各值的含义由 `conn_mgr_conn_api` 实现决定。某些设置可能由多个网络接口（Iface）共享。 |
| `optval` | 指向获取值的存储位置的指针。 |
| `optlen` | 指向目标缓冲区可用长度的指针，以字节为单位，该缓冲区用于存储获取的值。可用空间小于所需空间时返回 `-ENOBUFS`；可用空间无效时返回 `-EINVAL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | 网络接口（Iface）未实现 `conn_mgr_if_get_opt` 时。 |
| `-ENOBUFS` | 获取结果缓冲区（Retrieval Buffer）过小时。 |
| `-EINVAL` | 提供的获取结果缓冲区长度（Retrieval Buffer Length）无效，或 `optval`／`optlen` 指针为 `NULL` 时。 |
| `-ENOPROTOOPT` | 无法识别 `optname` 时。 |

**返回（Returns）**：返回值（Returns）：其他情况下返回实现特定错误码（Implementation-specific Error Code）。

<a id="gada9c37847acc604d82604351cbbb5e64"></a>

### `conn_mgr_if_get_timeout()`

```c
int conn_mgr_if_get_timeout ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

获取接口的连接超时（Connectivity Timeout）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则获取其超时设置（Timeout），以秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待检查 `iface` 的指针。 |

**返回（Returns）**：返回值（Returns）：`int`，成功获取时为连接超时值（Connectivity Timeout），以秒为单位；否则为 `CONN_MGR_IF_NO_TIMEOUT`。

<a id="ga09a1169a89eac1a3291185281952ce05"></a>

### `conn_mgr_if_is_bound()`

```c
bool conn_mgr_if_is_bound ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

检查所给网络接口（Network Interface）是否支持连接管理，即是否已绑定到某个连接实现（Connectivity Implementation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待检查 `iface` 的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 支持连接能力（Connectivity），即已绑定连接实现时。 |
| `false` | 其他情况。 |

<a id="gae86d1c808f31b8ca5e67bacbc844ef47"></a>

### `conn_mgr_if_set_flag()`

```c
int conn_mgr_if_set_flag ( struct net_if * iface, enum conn_mgr_if_flag flag, bool value )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

设置连接标志（Connectivity Flag）的值。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则设置与该接口关联的指定连接标志（Connectivity Flag）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待修改网络接口（Network Interface）的指针。 |
| `flag` | 要设置的标志（Flag）。 |
| `value` | 应启用还是禁用该标志（Flag）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 标志（Flag）不存在时。 |
| `-ENOTSUP` | 提供的 `iface` 未绑定连接实现（Connectivity Implementation）时。 |

<a id="ga93f333199c87b2d7668e94c92efd31ce"></a>

### `conn_mgr_if_set_idle_timeout()`

```c
int conn_mgr_if_set_idle_timeout ( struct net_if * iface, int timeout )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

设置接口的空闲超时（Idle Timeout）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则设置其空闲超时（Idle Timeout），以秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待修改网络接口（Network Interface）的指针。 |
| `timeout` | 要设置的超时值（Timeout Value），以秒为单位。传入 `CONN_MGR_IF_NO_TIMEOUT` 可禁用超时。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | 提供的 `iface` 未绑定连接实现（Connectivity Implementation）时。 |

<a id="ga2a2e6d7fbb7b1ed0327706a8c253d3e4"></a>

### `conn_mgr_if_set_opt()`

```c
int conn_mgr_if_set_opt ( struct net_if * iface, int optname, const void * optval, size_t optlen )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

设置由具体实现定义的连接选项（Implementation-specific Connectivity Options）。

如果提供的 `iface` 已绑定支持此操作的连接实现（Connectivity Implementation），则处理与该接口相关的实现特定连接选项（Connectivity Options）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（Network Interface）的指针。 |
| `optname` | 表示要设置选项的整数值。各值的含义由 `conn_mgr_conn_api` 实现决定。某些设置可能影响多个网络接口（Iface）。 |
| `optval` | 指向要赋给选项（Option）的值的指针。 |
| `optlen` | 要赋给选项（Option）的值的长度，以字节为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | 网络接口（Iface）未实现 `conn_mgr_if_set_opt` 时。 |
| `-ENOBUFS` | `optlen` 过长时。 |
| `-EINVAL` | 提供的 `optval` 指针为 `NULL` 时。 |
| `-ENOPROTOOPT` | 无法识别 `optname` 时。 |

**返回（Returns）**：返回值（Returns）：其他情况下返回实现特定错误码（Implementation-specific Error Code）。

<a id="ga467ecbb330d21b8dfea3e0ce08448400"></a>

### `conn_mgr_if_set_timeout()`

```c
int conn_mgr_if_set_timeout ( struct net_if * iface, int timeout )
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

设置接口的连接超时（Connectivity Timeout）。

如果提供的 `iface` 已绑定连接实现（Connectivity Implementation），则设置其超时（Timeout），以秒为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向待修改网络接口（Network Interface）的指针。 |
| `timeout` | 要设置的超时值（Timeout Value），以秒为单位。传入 `CONN_MGR_IF_NO_TIMEOUT` 可禁用超时。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTSUP` | 提供的 `iface` 未绑定连接实现（Connectivity Implementation）时。 |

<a id="ga4079113088236aede697538d79e5272f"></a>

### `conn_mgr_if_used()`

```c
void conn_mgr_if_used ( struct net_if * iface)
```

```c
#include <zephyr/net/conn_mgr_connectivity.h>
```

通知连接管理器（Connection Manager）：该接口刚刚被使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 刚刚使用过的网络接口（Iface）。 |

**说明（Note）**：注意（Note）：通常由网络驱动（Network Driver）调用，而非应用软件。


## 4.6\_原页交叉引用（Cross References）

- [连接管理器连接性批量 API（Connectivity Bulk API）](../api_update_memory_topic_reference/P004_连接管理器连接性批量 API（Connectivity Bulk API）.md)
- [连接管理器连接性实现 API（Connectivity Implementation API）](../api_input_runtime_topic_reference/P004_连接管理器连接性实现 API（Connectivity Implementation API）.md)
- [conn_mgr_conn_binding::timeout](../modem_wireless_model_reference/P010_conn_mgr_conn_binding_结构体.md#a8474461cf7b00132441227aae07511ab)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/conn_mgr_connectivity.h](../api_file_mesh_interrupt_reference/P003_zephyr__net__conn_mgr_connectivity.h_文件参考.md)
- [net_if_up](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga02644cc623fc7a8878c17d54984e4210)
- [conn_mgr_conn_api](../modem_wireless_model_reference/P009_conn_mgr_conn_api_结构体.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f"></a>
<a id="ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd"></a>
<a id="ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_nPM10xx 充电器接口（Charger interface）.md) · [返回大纲](大纲.md) · [下一章](P005_闪存区域接口（flash area Interface）.md)
