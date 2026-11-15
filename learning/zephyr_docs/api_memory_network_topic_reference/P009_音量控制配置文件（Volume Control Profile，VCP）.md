---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-9
title: 音量控制配置文件（Volume Control Profile，VCP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_音量控制配置文件（Volume Control Profile，VCP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音量控制配置文件（Volume Control Profile，VCP）

<a id="details"></a>

音量控制规范（Volume Control Profile，VCP）。引入版本（Since）：2.7；API 版本（Version）：0.8.0。VCP 提供控制音频设备音量等级（Volume Level）与静音状态（Mute State）的过程。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_bt_5Fvcp_5Fvol_5Frend_5Fregister_5Fparam"></a>

```c
struct bt_vcp_vol_rend_register_param
```

相关声明：[bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)。

音量控制服务（Volume Control Service）的注册结构。

<a id="r_bt_5Fvcp_5Fincluded"></a>

```c
struct bt_vcp_included
```

相关声明：[bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)。

音量控制服务（Volume Control Service）包含的服务。

<a id="r_bt_5Fvcp_5Fvol_5Frend_5Fcb"></a>

```c
struct bt_vcp_vol_rend_cb
```

相关声明：[bt_vcp_vol_rend_cb](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md)。

保存音量呈现器（Volume Renderer）回调的结构。

<a id="r_bt_5Fvcp_5Fvol_5Fctlr_5Fcb"></a>

```c
struct bt_vcp_vol_ctlr_cb
```

相关声明：[bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)。

保存音量控制器（Volume Controller）回调的结构。

<a id="r_bt_5Fvcp_5Fvol_5Fctlr"></a>

```c
struct bt_vcp_vol_ctlr
```

相关声明：[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

不透明的音量控制服务（Volume Control Service）实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gae7195f4556ad2442bc45d8d43cdeedd0"></a>

```c
#define BT_VCP_VOL_REND_VOCS_CNT 0U
```

相关声明：[BT_VCP_VOL_REND_VOCS_CNT](#gae7195f4556ad2442bc45d8d43cdeedd0)。

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音量偏移控制服务实例最大数量。

<a id="r_ga571d7ff5a6a507fcd7cbdfa32a04643b"></a>

```c
#define BT_VCP_VOL_REND_AICS_CNT 0U
```

相关声明：[BT_VCP_VOL_REND_AICS_CNT](#ga571d7ff5a6a507fcd7cbdfa32a04643b)。

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音频输入控制服务实例最大数量。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga1761d6618c48983e034cee5574c9c34f"></a>

```c
int bt_vcp_vol_rend_included_get (struct bt_vcp_included *included)
```

相关声明：[bt_vcp_vol_rend_included_get](#ga1761d6618c48983e034cee5574c9c34f)、[bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)。

获取音量控制服务（Volume Control Service）包含的服务。

<a id="r_ga752d8ff54a4b8c8c854a9c693617e64d"></a>

```c
int bt_vcp_vol_rend_register (struct bt_vcp_vol_rend_register_param *param)
```

相关声明：[bt_vcp_vol_rend_register](#ga752d8ff54a4b8c8c854a9c693617e64d)、[bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)。

注册音量控制服务（Volume Control Service）。

<a id="r_ga56e0f99d2688fb6f9e0e4d9103de706c"></a>

```c
int bt_vcp_vol_rend_set_step (uint8_t volume_step)
```

相关声明：[bt_vcp_vol_rend_set_step](#ga56e0f99d2688fb6f9e0e4d9103de706c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置音量控制服务（Volume Control Service）的音量步长。

<a id="r_ga9d1ac028abc88549ea18b6a0c585c781"></a>

```c
int bt_vcp_vol_rend_get_state (void)
```

相关声明：[bt_vcp_vol_rend_get_state](#ga9d1ac028abc88549ea18b6a0c585c781)。

获取音量控制服务（Volume Control Service）的音量状态。

<a id="r_ga1e6c9cfa0d012a4b701c99d8e6b5985d"></a>

```c
int bt_vcp_vol_rend_get_flags (void)
```

相关声明：[bt_vcp_vol_rend_get_flags](#ga1e6c9cfa0d012a4b701c99d8e6b5985d)。

获取音量控制服务（Volume Control Service）的标志。

<a id="r_gaf3c622f151a21d1dd617e97917c5ff5e"></a>

```c
int bt_vcp_vol_rend_vol_down (void)
```

相关声明：[bt_vcp_vol_rend_vol_down](#gaf3c622f151a21d1dd617e97917c5ff5e)。

将服务器的音量降低一步（One Step）。

<a id="r_ga6c10dd5a029b524994739f0b37a82c84"></a>

```c
int bt_vcp_vol_rend_vol_up (void)
```

相关声明：[bt_vcp_vol_rend_vol_up](#ga6c10dd5a029b524994739f0b37a82c84)。

将服务器的音量提高一步（One Step）。

<a id="r_ga3e6236a8679f95ba512181284a05923d"></a>

```c
int bt_vcp_vol_rend_unmute_vol_down (void)
```

相关声明：[bt_vcp_vol_rend_unmute_vol_down](#ga3e6236a8679f95ba512181284a05923d)。

降低服务器音量并取消静音（Unmute）。

<a id="r_gadf77729fee34f6605101c278fd2b7c46"></a>

```c
int bt_vcp_vol_rend_unmute_vol_up (void)
```

相关声明：[bt_vcp_vol_rend_unmute_vol_up](#gadf77729fee34f6605101c278fd2b7c46)。

提高服务器音量并取消静音（Unmute）。

<a id="r_ga61279baeba11152625cd3a87c5d973c9"></a>

```c
int bt_vcp_vol_rend_set_vol (uint8_t volume)
```

相关声明：[bt_vcp_vol_rend_set_vol](#ga61279baeba11152625cd3a87c5d973c9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置服务器上的音量（Volume）。

<a id="r_ga303d4b6b77987ab41cb1753ef861dd6c"></a>

```c
int bt_vcp_vol_rend_unmute (void)
```

相关声明：[bt_vcp_vol_rend_unmute](#ga303d4b6b77987ab41cb1753ef861dd6c)。

取消服务器静音（Unmute）。

<a id="r_ga0c6d0b6b015f069a9adc1332a32c79f9"></a>

```c
int bt_vcp_vol_rend_mute (void)
```

相关声明：[bt_vcp_vol_rend_mute](#ga0c6d0b6b015f069a9adc1332a32c79f9)。

使服务器静音（Mute）。

<a id="r_ga7861d0c3426870c015106e8e170004a3"></a>

```c
int bt_vcp_vol_ctlr_cb_register (struct bt_vcp_vol_ctlr_cb *cb)
```

相关声明：[bt_vcp_vol_ctlr_cb_register](#ga7861d0c3426870c015106e8e170004a3)、[bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)。

注册音量控制器（Volume Controller）使用的回调。

<a id="r_gae69e4730df4341bbb9bbbba1bea14005"></a>

```c
int bt_vcp_vol_ctlr_cb_unregister (struct bt_vcp_vol_ctlr_cb *cb)
```

相关声明：[bt_vcp_vol_ctlr_cb_unregister](#gae69e4730df4341bbb9bbbba1bea14005)、[bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)。

注销音量控制器（Volume Controller）使用的回调。

<a id="r_gac18d43a0785155c1131249f95554f2de"></a>

```c
int bt_vcp_vol_ctlr_discover (struct bt_conn *conn, struct bt_vcp_vol_ctlr **vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_discover](#gac18d43a0785155c1131249f95554f2de)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

发现音量控制服务（Volume Control Service）及其包含的服务。

<a id="r_ga0c8faa95cc36950c70ff572c931eedee"></a>

```c
struct bt_vcp_vol_ctlr * bt_vcp_vol_ctlr_get_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_vcp_vol_ctlr_get_by_conn](#ga0c8faa95cc36950c70ff572c931eedee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

根据连接指针获取音量控制器（Volume Controller）。

<a id="r_gab287197243191e3dbf162c6d16b6d726"></a>

```c
int bt_vcp_vol_ctlr_conn_get (const struct bt_vcp_vol_ctlr *vol_ctlr, struct bt_conn **conn)
```

相关声明：[bt_vcp_vol_ctlr_conn_get](#gab287197243191e3dbf162c6d16b6d726)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_gaaa748c49e103ff161f67df9663ea6330"></a>

```c
int bt_vcp_vol_ctlr_included_get (struct bt_vcp_vol_ctlr *vol_ctlr, struct bt_vcp_included *included)
```

相关声明：[bt_vcp_vol_ctlr_included_get](#gaaa748c49e103ff161f67df9663ea6330)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)。

获取音量控制服务（Volume Control Service）包含的服务。

<a id="r_ga68cab2f59c63542b6a7da33d555da0ab"></a>

```c
int bt_vcp_vol_ctlr_read_state (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_read_state](#ga68cab2f59c63542b6a7da33d555da0ab)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

读取远端音量渲染器（Volume Renderer）的音量状态。

<a id="r_gaefc226a5abb6bb1540d4b44ac4ddc236"></a>

```c
int bt_vcp_vol_ctlr_read_flags (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_read_flags](#gaefc226a5abb6bb1540d4b44ac4ddc236)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

读取远端音量渲染器（Volume Renderer）的音量标志。

<a id="r_ga03e073e29920f4a530d2f8851b4b8df4"></a>

```c
int bt_vcp_vol_ctlr_vol_down (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_vol_down](#ga03e073e29920f4a530d2f8851b4b8df4)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量降低一步。

<a id="r_ga908eb20727e1d68ed569badfd13ff896"></a>

```c
int bt_vcp_vol_ctlr_vol_up (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_vol_up](#ga908eb20727e1d68ed569badfd13ff896)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量提高一步。

<a id="r_ga20348b220988c700cabf356f7165d4d6"></a>

```c
int bt_vcp_vol_ctlr_unmute_vol_down (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute_vol_down](#ga20348b220988c700cabf356f7165d4d6)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量降低一步并取消静音。

<a id="r_ga2defdeee7486eee22a3416db8aa7c251"></a>

```c
int bt_vcp_vol_ctlr_unmute_vol_up (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute_vol_up](#ga2defdeee7486eee22a3416db8aa7c251)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量提高一步并取消静音。

<a id="r_gaaa5b5cd9a11c0e1fcdabce690ba20616"></a>

```c
int bt_vcp_vol_ctlr_set_vol (struct bt_vcp_vol_ctlr *vol_ctlr, uint8_t volume)
```

相关声明：[bt_vcp_vol_ctlr_set_vol](#gaaa5b5cd9a11c0e1fcdabce690ba20616)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置远端音量渲染器（Volume Renderer）的绝对音量（Absolute Volume）。

<a id="r_ga4e95c3fb071cb94fbe75f88e96d34b36"></a>

```c
int bt_vcp_vol_ctlr_unmute (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute](#ga4e95c3fb071cb94fbe75f88e96d34b36)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

取消远端音量渲染器（Volume Renderer）的静音。

<a id="r_ga106b7f826adec665b4f0ac3d5e82b867"></a>

```c
int bt_vcp_vol_ctlr_mute (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_mute](#ga106b7f826adec665b4f0ac3d5e82b867)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

使远端音量渲染器（Volume Renderer）静音。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.4\_音量控制服务错误码（Volume Control Service Error Codes）

<a id="r_gabb8bdfde60f1cbb31bab41fd61b3384b"></a>

```c
#define BT_VCP_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_VCP_ERR_INVALID_COUNTER](#gabb8bdfde60f1cbb31bab41fd61b3384b)。

Change_Counter 操作数值与音量状态特征（Volume State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_gad979c43e4d84f52009d9931fb74628e6"></a>

```c
#define BT_VCP_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_VCP_ERR_OP_NOT_SUPPORTED](#gad979c43e4d84f52009d9931fb74628e6)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

## 9.5\_音量控制服务静音值（Volume Control Service Mute Values）

<a id="r_ga4660f938a16113f715dd8aec3ed3baf6"></a>

```c
#define BT_VCP_STATE_UNMUTED 0x00U
```

相关声明：[BT_VCP_STATE_UNMUTED](#ga4660f938a16113f715dd8aec3ed3baf6)。

音量处于取消静音状态（Unmuted）。

<a id="r_ga3d6ffdfb9e0d8d58073f4a130a8020b0"></a>

```c
#define BT_VCP_STATE_MUTED 0x01U
```

相关声明：[BT_VCP_STATE_MUTED](#ga3d6ffdfb9e0d8d58073f4a130a8020b0)。

音量处于静音状态（Muted）。

## 9.6\_详细说明（Detailed Documentation）

<a id="gabb8bdfde60f1cbb31bab41fd61b3384b"></a>

### `BT_VCP_ERR_INVALID_COUNTER`

```c
#define BT_VCP_ERR_INVALID_COUNTER 0x80U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

Change_Counter 操作数值与音量状态特征（Volume State Characteristic）的 Change_Counter 字段值不匹配。

<a id="gad979c43e4d84f52009d9931fb74628e6"></a>

### `BT_VCP_ERR_OP_NOT_SUPPORTED`

```c
#define BT_VCP_ERR_OP_NOT_SUPPORTED 0x81U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="ga3d6ffdfb9e0d8d58073f4a130a8020b0"></a>

### `BT_VCP_STATE_MUTED`

```c
#define BT_VCP_STATE_MUTED 0x01U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

音量处于静音状态（Muted）。

<a id="ga4660f938a16113f715dd8aec3ed3baf6"></a>

### `BT_VCP_STATE_UNMUTED`

```c
#define BT_VCP_STATE_UNMUTED 0x00U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

音量处于取消静音状态（Unmuted）。

<a id="ga571d7ff5a6a507fcd7cbdfa32a04643b"></a>

### `BT_VCP_VOL_REND_AICS_CNT`

```c
#define BT_VCP_VOL_REND_AICS_CNT 0U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音频输入控制服务实例最大数量。

<a id="gae7195f4556ad2442bc45d8d43cdeedd0"></a>

### `BT_VCP_VOL_REND_VOCS_CNT`

```c
#define BT_VCP_VOL_REND_VOCS_CNT 0U
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音量偏移控制服务实例最大数量。

<a id="ga7861d0c3426870c015106e8e170004a3"></a>

### `bt_vcp_vol_ctlr_cb_register()`

```c
int bt_vcp_vol_ctlr_cb_register ( struct bt_vcp_vol_ctlr_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

注册音量控制器（Volume Controller）使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | `cb` 已注册（Registered）时。 |

<a id="gae69e4730df4341bbb9bbbba1bea14005"></a>

### `bt_vcp_vol_ctlr_cb_unregister()`

```c
int bt_vcp_vol_ctlr_cb_unregister ( struct bt_vcp_vol_ctlr_cb * cb)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

注销音量控制器（Volume Controller）使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（callback structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-EALREADY` | `cb` 未注册（Registered）时。 |

<a id="gab287197243191e3dbf162c6d16b6d726"></a>

### `bt_vcp_vol_ctlr_conn_get()`

```c
int bt_vcp_vol_ctlr_conn_get ( const struct bt_vcp_vol_ctlr * vol_ctlr, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

获取客户端实例的连接指针（Connection Pointer）。

获取音量控制服务（Volume Control Service）客户端实例的蓝牙连接指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `[out] conn` | 连接指针（Connection Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gac18d43a0785155c1131249f95554f2de"></a>

### `bt_vcp_vol_ctlr_discover()`

```c
int bt_vcp_vol_ctlr_discover ( struct bt_conn * conn, struct bt_vcp_vol_ctlr ** vol_ctlr )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

发现音量控制服务（Volume Control Service）及其包含的服务。

启动 GATT 发现（Discovery），设置句柄与订阅。对端设备执行其他操作之前必须先调用一次；bt_vcp_vol_ctlr_cb::discover 回调会通知何时可以开始远端操作。

仅能以客户端（Client）身份执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` conn` | 要在其上发现音量控制服务（Volume Control Service）的连接。 |
| `[out] vol_ctlr` | 成功时的有效远端实例对象（Remote Instance Object）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga0c8faa95cc36950c70ff572c931eedee"></a>

### `bt_vcp_vol_ctlr_get_by_conn()`

```c
struct bt_vcp_vol_ctlr * bt_vcp_vol_ctlr_get_by_conn ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

根据连接指针获取音量控制器（Volume Controller）。

根据连接指针获取 VCP 音量控制器（Volume Controller）指针。仅能获取通过 bt_vcp_vol_ctlr_discover() 初始化的音量控制器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接指针（Connection Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Pointer` | 指向 VCP 音量控制器（Volume Controller）实例。 |
| `NULL` | `conn` 为 `NULL`，或者连接尚未完成发现（Discovery）时。 |

<a id="gaaa748c49e103ff161f67df9663ea6330"></a>

### `bt_vcp_vol_ctlr_included_get()`

```c
int bt_vcp_vol_ctlr_included_get ( struct bt_vcp_vol_ctlr * vol_ctlr, struct bt_vcp_included * included )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

获取音量控制服务（Volume Control Service）包含的服务。

返回一个结构体指针，其中包含音量控制服务的内含服务实例信息，例如音量偏移控制服务（Volume Offset Control Service）或音频输入控制服务（Audio Input Control Service，AICS）实例指针。

要求启用 CONFIG_BT_VCP_VOL_CTLR_VOCS 或 CONFIG_BT_VCP_VOL_CTLR_AICS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `[out] included` | 用于保存结果的指针（Result Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga106b7f826adec665b4f0ac3d5e82b867"></a>

### `bt_vcp_vol_ctlr_mute()`

```c
int bt_vcp_vol_ctlr_mute ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

使远端音量渲染器（Volume Renderer）静音。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaefc226a5abb6bb1540d4b44ac4ddc236"></a>

### `bt_vcp_vol_ctlr_read_flags()`

```c
int bt_vcp_vol_ctlr_read_flags ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

读取远端音量渲染器（Volume Renderer）的音量标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga68cab2f59c63542b6a7da33d555da0ab"></a>

### `bt_vcp_vol_ctlr_read_state()`

```c
int bt_vcp_vol_ctlr_read_state ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

读取远端音量渲染器（Volume Renderer）的音量状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaaa5b5cd9a11c0e1fcdabce690ba20616"></a>

### `bt_vcp_vol_ctlr_set_vol()`

```c
int bt_vcp_vol_ctlr_set_vol ( struct bt_vcp_vol_ctlr * vol_ctlr, uint8_t volume )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

设置远端音量渲染器（Volume Renderer）的绝对音量（Absolute Volume）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |
| `volume` | 要设置的绝对音量（Absolute volume）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga4e95c3fb071cb94fbe75f88e96d34b36"></a>

### `bt_vcp_vol_ctlr_unmute()`

```c
int bt_vcp_vol_ctlr_unmute ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

取消远端音量渲染器（Volume Renderer）的静音。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga20348b220988c700cabf356f7165d4d6"></a>

### `bt_vcp_vol_ctlr_unmute_vol_down()`

```c
int bt_vcp_vol_ctlr_unmute_vol_down ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将远端音量渲染器（Volume Renderer）的音量降低一步并取消静音。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga2defdeee7486eee22a3416db8aa7c251"></a>

### `bt_vcp_vol_ctlr_unmute_vol_up()`

```c
int bt_vcp_vol_ctlr_unmute_vol_up ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将远端音量渲染器（Volume Renderer）的音量提高一步并取消静音。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga03e073e29920f4a530d2f8851b4b8df4"></a>

### `bt_vcp_vol_ctlr_vol_down()`

```c
int bt_vcp_vol_ctlr_vol_down ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将远端音量渲染器（Volume Renderer）的音量降低一步。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga908eb20727e1d68ed569badfd13ff896"></a>

### `bt_vcp_vol_ctlr_vol_up()`

```c
int bt_vcp_vol_ctlr_vol_up ( struct bt_vcp_vol_ctlr * vol_ctlr)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将远端音量渲染器（Volume Renderer）的音量提高一步。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vol_ctlr` | 音量控制器（Volume Controller）实例指针。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga1e6c9cfa0d012a4b701c99d8e6b5985d"></a>

### `bt_vcp_vol_rend_get_flags()`

```c
int bt_vcp_vol_rend_get_flags ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

获取音量控制服务（Volume Control Service）的标志。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga9d1ac028abc88549ea18b6a0c585c781"></a>

### `bt_vcp_vol_rend_get_state()`

```c
int bt_vcp_vol_rend_get_state ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

获取音量控制服务（Volume Control Service）的音量状态。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga1761d6618c48983e034cee5574c9c34f"></a>

### `bt_vcp_vol_rend_included_get()`

```c
int bt_vcp_vol_rend_included_get ( struct bt_vcp_included * included)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

获取音量控制服务（Volume Control Service）包含的服务。

返回一个结构体指针，其中包含音量控制服务的内含服务实例信息，例如音量偏移控制服务（Volume Offset Control Service）或音频输入控制服务（Audio Input Control Service，AICS）实例指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] included` | 用于保存结果的指针（Result Pointer）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga0c6d0b6b015f069a9adc1332a32c79f9"></a>

### `bt_vcp_vol_rend_mute()`

```c
int bt_vcp_vol_rend_mute ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

使服务器静音（Mute）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga752d8ff54a4b8c8c854a9c693617e64d"></a>

### `bt_vcp_vol_rend_register()`

```c
int bt_vcp_vol_rend_register ( struct bt_vcp_vol_rend_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

注册音量控制服务（Volume Control Service）。

注册并启用服务，使客户端可以发现它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 音量控制服务（Volume Control Service）注册参数。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga56e0f99d2688fb6f9e0e4d9103de706c"></a>

### `bt_vcp_vol_rend_set_step()`

```c
int bt_vcp_vol_rend_set_step ( uint8_t volume_step)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

设置音量控制服务（Volume Control Service）的音量步长。

设置通过 bt_vcp_vol_rend_vol_down、bt_vcp_vol_rend_vol_up 等进行相对音量调整时的变化量。

仅能以服务器（Server）身份执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `volume_step` | 音量步长（Volume Step Size），范围为 1～255。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga61279baeba11152625cd3a87c5d973c9"></a>

### `bt_vcp_vol_rend_set_vol()`

```c
int bt_vcp_vol_rend_set_vol ( uint8_t volume)
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

设置服务器上的音量（Volume）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `volume` | 要设置的绝对音量（Absolute volume）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga303d4b6b77987ab41cb1753ef861dd6c"></a>

### `bt_vcp_vol_rend_unmute()`

```c
int bt_vcp_vol_rend_unmute ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

取消服务器静音（Unmute）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga3e6236a8679f95ba512181284a05923d"></a>

### `bt_vcp_vol_rend_unmute_vol_down()`

```c
int bt_vcp_vol_rend_unmute_vol_down ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

降低服务器音量并取消静音（Unmute）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gadf77729fee34f6605101c278fd2b7c46"></a>

### `bt_vcp_vol_rend_unmute_vol_up()`

```c
int bt_vcp_vol_rend_unmute_vol_up ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

提高服务器音量并取消静音（Unmute）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="gaf3c622f151a21d1dd617e97917c5ff5e"></a>

### `bt_vcp_vol_rend_vol_down()`

```c
int bt_vcp_vol_rend_vol_down ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将服务器的音量降低一步（One Step）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。

<a id="ga6c10dd5a029b524994739f0b37a82c84"></a>

### `bt_vcp_vol_rend_vol_up()`

```c
int bt_vcp_vol_rend_vol_up ( void )
```

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

将服务器的音量提高一步（One Step）。

**返回（Returns）**：返回值：成功返回 0，失败返回 errno 错误码。


## 9.7\_原页交叉引用（Cross References）

- [bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)
- [bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)
- [bt_vcp_vol_rend_cb](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md)
- [bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)
- [bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/vcp.h](../api_file_clock_network_reference/P028_zephyr__bluetooth__audio__vcp.h_文件参考.md)
- [bt_vcp_vol_ctlr_cb::discover](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md#ada8fe8d838d6d2c983d746e7e7ed1171)
- [CONFIG_BT_VCP_VOL_CTLR_VOCS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VCP_VOL_CTLR_VOCS)
- [CONFIG_BT_VCP_VOL_CTLR_AICS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_VCP_VOL_CTLR_AICS)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_RFCOMM API主题.md) · [返回大纲](大纲.md) · [下一章](P010_Realtek Bee DMA 宏（Macros）.md)
