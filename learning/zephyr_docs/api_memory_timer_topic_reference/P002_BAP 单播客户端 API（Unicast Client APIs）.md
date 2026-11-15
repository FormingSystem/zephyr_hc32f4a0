---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-2
title: BAP 单播客户端 API（Unicast Client APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_BAP 单播客户端 API（Unicast Client APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fstream_5Fparam"></a>

```c
struct bt_bap_unicast_group_stream_param
```

相关声明：[bt_bap_unicast_group_stream_param](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md)。

单播组中每条流的参数结构体。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fstream_5Fpair_5Fparam"></a>

```c
struct bt_bap_unicast_group_stream_pair_param
```

相关声明：[bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)。

单播组函数使用的参数结构体。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Fparam"></a>

```c
struct bt_bap_unicast_group_param
```

相关声明：[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)。

使用 `bt_bap_unicast_group_create()` 创建单播组的参数。

<a id="r_bt_5Fbap_5Funicast_5Fgroup_5Finfo"></a>

```c
struct bt_bap_unicast_group_info
```

相关声明：[bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)。

保存单播组（Unicast Group）信息的结构体。

<a id="r_bt_5Fbap_5Funicast_5Fclient_5Fcb"></a>

```c
struct bt_bap_unicast_client_cb
```

相关声明：[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

单播客户端（Unicast Client）回调结构体。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gaf0e5a38208e90176292e745933b5e29e"></a>

```c
typedef bool(* bt_bap_unicast_group_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_unicast_group_foreach_stream_func_t](#gaf0e5a38208e90176292e745933b5e29e)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)。

bt_bap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gaafd53b5f45d998b44e94a1b58e93ba21"></a>

```c
int bt_bap_unicast_group_create (struct bt_bap_unicast_group_param *param, struct bt_bap_unicast_group **unicast_group)
```

相关声明：[bt_bap_unicast_group_create](#gaafd53b5f45d998b44e94a1b58e93ba21)、[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)。

创建单播组（Unicast Group）。

<a id="r_gacd684504c8127ff4f8d038cc06718e5e"></a>

```c
int bt_bap_unicast_group_reconfig (struct bt_bap_unicast_group *unicast_group, const struct bt_bap_unicast_group_param *param)
```

相关声明：[bt_bap_unicast_group_reconfig](#gacd684504c8127ff4f8d038cc06718e5e)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)。

重新配置单播组（Unicast Group）。

<a id="r_ga9cc792cd1eaaa79d56f3df0e2341cbf6"></a>

```c
int bt_bap_unicast_group_add_streams (struct bt_bap_unicast_group *unicast_group, struct bt_bap_unicast_group_stream_pair_param params[], size_t num_param)
```

相关声明：[bt_bap_unicast_group_add_streams](#ga9cc792cd1eaaa79d56f3df0e2341cbf6)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)。

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

<a id="r_ga34dbdce6133f8366df453ec937fb47d2"></a>

```c
int bt_bap_unicast_group_delete (struct bt_bap_unicast_group *unicast_group)
```

相关声明：[bt_bap_unicast_group_delete](#ga34dbdce6133f8366df453ec937fb47d2)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)。

删除音频单播组（Audio Unicast Group）。

<a id="r_gad608ee07c8a50abf586a3bc31921f032"></a>

```c
int bt_bap_unicast_group_foreach_stream (struct bt_bap_unicast_group *unicast_group, bt_bap_unicast_group_foreach_stream_func_t func, void *user_data)
```

相关声明：[bt_bap_unicast_group_foreach_stream](#gad608ee07c8a50abf586a3bc31921f032)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_foreach_stream_func_t](#gaf0e5a38208e90176292e745933b5e29e)。

遍历单播组（Unicast Group）中的全部流。

<a id="r_ga4ba0e4c3fa7ec3a36a64a19c80027504"></a>

```c
int bt_bap_unicast_group_get_info (const struct bt_bap_unicast_group *unicast_group, struct bt_bap_unicast_group_info *info)
```

相关声明：[bt_bap_unicast_group_get_info](#ga4ba0e4c3fa7ec3a36a64a19c80027504)、[bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)、[bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)。

返回保存单播组信息（Unicast Group Information）的结构体。

<a id="r_gade70f04ae1a828b43b3b44fa8933f674"></a>

```c
int bt_bap_unicast_client_register_cb (struct bt_bap_unicast_client_cb *cb)
```

相关声明：[bt_bap_unicast_client_register_cb](#gade70f04ae1a828b43b3b44fa8933f674)、[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

注册单播客户端回调（Unicast Client Callbacks）。

<a id="r_gaee092a4e918a67bb5fd94cb78cc21141"></a>

```c
int bt_bap_unicast_client_unregister_cb (struct bt_bap_unicast_client_cb *cb)
```

相关声明：[bt_bap_unicast_client_unregister_cb](#gaee092a4e918a67bb5fd94cb78cc21141)、[bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)。

注销单播客户端回调（Unicast Client Callbacks）。

<a id="r_gacef9c88f66762e8de19303d20dafa0bb"></a>

```c
int bt_bap_unicast_client_discover (struct bt_conn *conn, enum bt_audio_dir dir)
```

相关声明：[bt_bap_unicast_client_discover](#gacef9c88f66762e8de19303d20dafa0bb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

发现远端能力（Remote Capabilities）和端点（Endpoints）。

<a id="r_gad963bdda290df96036a68b00cc940eca"></a>

```c
int bt_bap_unicast_client_qos_from_group (const struct bt_bap_stream *stream, struct bt_bap_qos_cfg *qos)
```

相关声明：[bt_bap_unicast_client_qos_from_group](#gad963bdda290df96036a68b00cc940eca)、[bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)。

获取为该流所属组配置的服务质量（QoS）副本。

<a id="r_gad106ae43201100940d9145d291fe9ca3"></a>

```c
bool bt_bap_qos_cfg_eq (const struct bt_bap_qos_cfg *a, const struct bt_bap_qos_cfg *b)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_bap_qos_cfg_eq](#gad106ae43201100940d9145d291fe9ca3)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)、[bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)。

比较两个 bt_bap_qos_cfg，并返回它们是否相等。

## 2.4\_详细说明（Detailed Documentation）

<a id="gaf0e5a38208e90176292e745933b5e29e"></a>

### `bt_bap_unicast_group_foreach_stream_func_t`

```c
typedef bool(* bt_bap_unicast_group_foreach_stream_func_t) (struct bt_bap_stream *stream, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

bt_bap_unicast_group_foreach_stream() 的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `stream` | 音频流（Audio Stream） |
| `user_data` | 用户数据（User Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 继续遍历（Continue Iterating）。 |
| `false` | 停止遍历（Stop Iterating）。 |

<a id="gad106ae43201100940d9145d291fe9ca3"></a>

### `bt_bap_qos_cfg_eq()`

```c
bool bt_bap_qos_cfg_eq ( const struct bt_bap_qos_cfg * a, const struct bt_bap_qos_cfg * b )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

比较两个 bt_bap_qos_cfg，并返回它们是否相等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 要比较的第一个服务质量配置（QoS Config）。 |
| `b` | 要比较的第二个服务质量配置（QoS Config）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | a 和 b 指向同一内存，包括两者均为 NULL，或者所有字段均相同。 |
| `false` | a 或 b 之一为 NULL，或者存在任一字段不同。 |

<a id="gacef9c88f66762e8de19303d20dafa0bb"></a>

### `bt_bap_unicast_client_discover()`

```c
int bt_bap_unicast_client_discover ( struct bt_conn * conn, enum bt_audio_dir dir )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

发现远端能力（Remote Capabilities）和端点（Endpoints）。

客户端使用此过程发现远端能力（Remote Capabilities）和端点（Endpoints），并通过 params 回调通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | ACL 连接（ACL Connection），必须已满足基本音频配置文件（Basic Audio Profile）的安全要求。 |
| `dir` | 要发现的远端端点和能力的类型（Type）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | conn 为 NULL、不是中心设备连接（Central Connection）或不满足安全要求，或者 dir 无效。 |
| `-EBUSY` | 此 conn 已有另一项操作正在进行。 |
| `-ENOTCONN` | conn 未连接。 |
| `-ENOMEM` | 无法为请求分配内存（Allocate Memory）。 |
| `-ENOEXEC` | 非预期的 GATT 错误（Unexpected GATT Error）。 |

<a id="gad963bdda290df96036a68b00cc940eca"></a>

### `bt_bap_unicast_client_qos_from_group()`

```c
int bt_bap_unicast_client_qos_from_group ( const struct bt_bap_stream * stream, struct bt_bap_qos_cfg * qos )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

获取为该流所属组配置的服务质量（QoS）副本。

如果流尚未进行 QoS 配置，或者组已通过 bt_bap_unicast_group_reconfig() 重新配置，此值可能与 stream->qos 不同。这里返回的 QoS 是为该组调用 bt_bap_stream_qos() 时将应用的配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] stream` | 要从中获取服务质量配置信息（QoS Configuration Information）的流。 |
| `[out] qos` | 服务质量配置数据（QoS Configuration Data）的副本。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | stream 或 qos 为 NULL，或 stream 不属于任何组。 |

<a id="gade70f04ae1a828b43b3b44fa8933f674"></a>

### `bt_bap_unicast_client_register_cb()`

```c
int bt_bap_unicast_client_register_cb ( struct bt_bap_unicast_client_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注册单播客户端回调（Unicast Client Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要注册的单播客户端回调结构体（Unicast Client Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL。 |
| `-EEXIST` | cb 已注册。 |

<a id="gaee092a4e918a67bb5fd94cb78cc21141"></a>

### `bt_bap_unicast_client_unregister_cb()`

```c
int bt_bap_unicast_client_unregister_cb ( struct bt_bap_unicast_client_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

注销单播客户端回调（Unicast Client Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要注销的单播客户端回调结构体（Unicast Client Callback Structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | cb 为 NULL，或 cb 未注册。 |

<a id="ga9cc792cd1eaaa79d56f3df0e2341cbf6"></a>

### `bt_bap_unicast_group_add_streams()`

```c
int bt_bap_unicast_group_add_streams ( struct bt_bap_unicast_group * unicast_group, struct bt_bap_unicast_group_stream_pair_param params[], size_t num_param )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

以单播客户端（Unicast Client）身份向单播组添加流（Streams）。

此函数可向 bt_bap_unicast_group 添加更多流（Streams）。

可以在组中任何流启动之前调用，参见 bt_bap_stream_ops.started()；也可以在流停止之后调用，参见 bt_bap_stream_ops.stopped()。

流加入单播组（Unicast Group）后，就不能单独移除。若要从组中移除流，必须通过 bt_bap_unicast_group_delete() 删除整个组，但这又要求先释放组中的所有流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向单播组（Unicast Group）的指针。 |
| `params` | 流参数数组（Stream Parameters Array），其中的流将被添加到组中。 |
| `num_param` | params 中的参数数量。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaafd53b5f45d998b44e94a1b58e93ba21"></a>

### `bt_bap_unicast_group_create()`

```c
int bt_bap_unicast_group_create ( struct bt_bap_unicast_group_param * param, struct bt_bap_unicast_group ** unicast_group )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

创建单播组（Unicast Group）。

以单播客户端（Unicast Client）身份创建包含一个或多个音频流的新音频单播组（Audio Unicast Group）。所有流必须使用相同的成帧方式（Framing）；同一方向的所有流必须使用相同的间隔（Interval）和延迟（Latency），参见 bt_bap_qos_cfg。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 单播组创建参数（Unicast Group Create Parameters）。 |
| `[out] unicast_group` | 指向已创建单播组（Unicast Group）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga34dbdce6133f8366df453ec937fb47d2"></a>

### `bt_bap_unicast_group_delete()`

```c
int bt_bap_unicast_group_delete ( struct bt_bap_unicast_group * unicast_group)
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

删除音频单播组（Audio Unicast Group）。

以客户端身份删除音频单播组（Audio Unicast Group）。组中的所有流都必须处于空闲状态（Idle）或已配置状态（Configured）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向待删除单播组（Unicast Group）的指针。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gad608ee07c8a50abf586a3bc31921f032"></a>

### `bt_bap_unicast_group_foreach_stream()`

```c
int bt_bap_unicast_group_foreach_stream ( struct bt_bap_unicast_group * unicast_group, bt_bap_unicast_group_foreach_stream_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

遍历单播组（Unicast Group）中的全部流。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 单播组（Unicast Group）。 |
| `func` | 回调函数。 |
| `user_data` | 传给回调函数的用户指定数据（User-specified Data）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功，即使组中没有流也视为成功。 |
| `-ECANCELED` | 遍历尚未完成便被回调函数（Callback Function）停止。 |
| `-EINVAL` | unicast_group 或 func 为 NULL。 |

<a id="ga4ba0e4c3fa7ec3a36a64a19c80027504"></a>

### `bt_bap_unicast_group_get_info()`

```c
int bt_bap_unicast_group_get_info ( const struct bt_bap_unicast_group * unicast_group, struct bt_bap_unicast_group_info * info )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

返回保存单播组信息（Unicast Group Information）的结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 单播组对象（Unicast Group Object）。 |
| `info` | 要用信息填充的结构体对象（Structure Object）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | unicast_group 或 info 为 NULL。 |

<a id="gacd684504c8127ff4f8d038cc06718e5e"></a>

### `bt_bap_unicast_group_reconfig()`

```c
int bt_bap_unicast_group_reconfig ( struct bt_bap_unicast_group * unicast_group, const struct bt_bap_unicast_group_param * param )
```

```c
#include <zephyr/bluetooth/audio/bap.h>
```

重新配置单播组（Unicast Group）。

以单播客户端（Unicast Client）身份重新配置包含一个或多个音频流的单播组（Unicast Group）。所有流必须使用相同的成帧方式（Framing）；同一方向的所有流必须使用相同的间隔（Interval）和延迟（Latency），参见 bt_bap_qos_cfg。param 中的全部流必须已经属于 unicast_group；添加更多流请使用 bt_bap_unicast_group_add_streams()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `unicast_group` | 指向已创建单播组（Unicast Group）的指针。 |
| `param` | 单播组重新配置参数（Unicast Group Reconfigure Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 2.5\_原页交叉引用（Cross References）

- [bt_bap_unicast_group_stream_param](../bluetooth_le_audio_model_reference/P040_bt_bap_unicast_group_stream_param_结构体.md)
- [bt_bap_unicast_group_stream_pair_param](../bluetooth_le_audio_model_reference/P039_bt_bap_unicast_group_stream_pair_param_结构体.md)
- [bt_bap_unicast_group_param](../bluetooth_le_audio_model_reference/P038_bt_bap_unicast_group_param_结构体.md)
- [bt_bap_unicast_group_info](../bluetooth_le_audio_model_reference/P037_bt_bap_unicast_group_info_结构体.md)
- [bt_bap_unicast_client_cb](../bluetooth_le_audio_model_reference/P035_bt_bap_unicast_client_cb_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_bap_stream](../bluetooth_le_audio_model_reference/P033_bt_bap_stream_结构体.md)
- [bt_bap_unicast_group](../bluetooth_le_audio_model_reference/P036_bt_bap_unicast_group_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_bap_qos_cfg](../bluetooth_le_audio_model_reference/P027_bt_bap_qos_cfg_结构体.md)
- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h.html)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [bt_bap_stream_qos()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html#gac878ed89242cac9a8514e8e4f1da4d9d)
- [bt_bap_stream_ops.started()](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#a7f595e37d40b94510bf09c1f82b479f3)
- [bt_bap_stream_ops.stopped()](../bluetooth_le_audio_model_reference/P034_bt_bap_stream_ops_结构体.md#ab50ea295069a2cd1ab6f4353052262f5)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_音频输入控制服务（Audio Input Control Service，AICS）.md) · [返回大纲](大纲.md) · [下一章](P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 服务器.md)
