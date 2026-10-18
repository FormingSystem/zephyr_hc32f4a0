---
id: learning.zephyr-docs.api-file-clock-network-reference.page-28
title: zephyr__bluetooth__audio__vcp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_bluetooth\_\_audio\_\_vcp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音量控制配置文件（Volume Control Profile，VCP）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/bluetooth/audio/aics.h>
#include <zephyr/bluetooth/audio/vocs.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙音量控制配置文件（Volume Control Profile，VCP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.2\_宏定义（Macros）

<a id="r_gae7195f4556ad2442bc45d8d43cdeedd0"></a>

```c
#define BT_VCP_VOL_REND_VOCS_CNT 0U
```

相关声明：[BT_VCP_VOL_REND_VOCS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae7195f4556ad2442bc45d8d43cdeedd0)。

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音量偏移控制服务实例最大数量。

<a id="r_ga571d7ff5a6a507fcd7cbdfa32a04643b"></a>

```c
#define BT_VCP_VOL_REND_AICS_CNT 0U
```

相关声明：[BT_VCP_VOL_REND_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga571d7ff5a6a507fcd7cbdfa32a04643b)。

定义音量控制规范（Volume Control Profile）音量渲染器（Volume Renderer）支持的音频输入控制服务实例最大数量。

<a id="define-members-0"></a>

### 音量控制服务错误码（Volume Control Service Error Codes）

<a id="r_gabb8bdfde60f1cbb31bab41fd61b3384b"></a>

```c
#define BT_VCP_ERR_INVALID_COUNTER 0x80U
```

相关声明：[BT_VCP_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gabb8bdfde60f1cbb31bab41fd61b3384b)。

Change_Counter 操作数值与音量状态特征（Volume State Characteristic）的 Change_Counter 字段值不匹配。

<a id="r_gad979c43e4d84f52009d9931fb74628e6"></a>

```c
#define BT_VCP_ERR_OP_NOT_SUPPORTED 0x81U
```

相关声明：[BT_VCP_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gad979c43e4d84f52009d9931fb74628e6)。

控制点过程（Control Point Procedure）使用了无效操作码（Opcode）。

<a id="define-members-1"></a>

### 音量控制服务静音值（Volume Control Service Mute Values）

<a id="r_ga4660f938a16113f715dd8aec3ed3baf6"></a>

```c
#define BT_VCP_STATE_UNMUTED 0x00U
```

相关声明：[BT_VCP_STATE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4660f938a16113f715dd8aec3ed3baf6)。

音量处于取消静音状态（Unmuted）。

<a id="r_ga3d6ffdfb9e0d8d58073f4a130a8020b0"></a>

```c
#define BT_VCP_STATE_MUTED 0x01U
```

相关声明：[BT_VCP_STATE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga3d6ffdfb9e0d8d58073f4a130a8020b0)。

音量处于静音状态（Muted）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga1761d6618c48983e034cee5574c9c34f"></a>

```c
int bt_vcp_vol_rend_included_get (struct bt_vcp_included *included)
```

相关声明：[bt_vcp_vol_rend_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1761d6618c48983e034cee5574c9c34f)、[bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)。

获取音量控制服务（Volume Control Service）包含的服务。

<a id="r_ga752d8ff54a4b8c8c854a9c693617e64d"></a>

```c
int bt_vcp_vol_rend_register (struct bt_vcp_vol_rend_register_param *param)
```

相关声明：[bt_vcp_vol_rend_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga752d8ff54a4b8c8c854a9c693617e64d)、[bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)。

注册音量控制服务（Volume Control Service）。

<a id="r_ga56e0f99d2688fb6f9e0e4d9103de706c"></a>

```c
int bt_vcp_vol_rend_set_step (uint8_t volume_step)
```

相关声明：[bt_vcp_vol_rend_set_step](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga56e0f99d2688fb6f9e0e4d9103de706c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置音量控制服务（Volume Control Service）的音量步长。

<a id="r_ga9d1ac028abc88549ea18b6a0c585c781"></a>

```c
int bt_vcp_vol_rend_get_state (void)
```

相关声明：[bt_vcp_vol_rend_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga9d1ac028abc88549ea18b6a0c585c781)。

获取音量控制服务（Volume Control Service）的音量状态。

<a id="r_ga1e6c9cfa0d012a4b701c99d8e6b5985d"></a>

```c
int bt_vcp_vol_rend_get_flags (void)
```

相关声明：[bt_vcp_vol_rend_get_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1e6c9cfa0d012a4b701c99d8e6b5985d)。

获取音量控制服务（Volume Control Service）的标志。

<a id="r_gaf3c622f151a21d1dd617e97917c5ff5e"></a>

```c
int bt_vcp_vol_rend_vol_down (void)
```

相关声明：[bt_vcp_vol_rend_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaf3c622f151a21d1dd617e97917c5ff5e)。

将服务器的音量降低一步（One Step）。

<a id="r_ga6c10dd5a029b524994739f0b37a82c84"></a>

```c
int bt_vcp_vol_rend_vol_up (void)
```

相关声明：[bt_vcp_vol_rend_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga6c10dd5a029b524994739f0b37a82c84)。

将服务器的音量提高一步（One Step）。

<a id="r_ga3e6236a8679f95ba512181284a05923d"></a>

```c
int bt_vcp_vol_rend_unmute_vol_down (void)
```

相关声明：[bt_vcp_vol_rend_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga3e6236a8679f95ba512181284a05923d)。

降低服务器音量并取消静音（Unmute）。

<a id="r_gadf77729fee34f6605101c278fd2b7c46"></a>

```c
int bt_vcp_vol_rend_unmute_vol_up (void)
```

相关声明：[bt_vcp_vol_rend_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gadf77729fee34f6605101c278fd2b7c46)。

提高服务器音量并取消静音（Unmute）。

<a id="r_ga61279baeba11152625cd3a87c5d973c9"></a>

```c
int bt_vcp_vol_rend_set_vol (uint8_t volume)
```

相关声明：[bt_vcp_vol_rend_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga61279baeba11152625cd3a87c5d973c9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置服务器上的音量（Volume）。

<a id="r_ga303d4b6b77987ab41cb1753ef861dd6c"></a>

```c
int bt_vcp_vol_rend_unmute (void)
```

相关声明：[bt_vcp_vol_rend_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga303d4b6b77987ab41cb1753ef861dd6c)。

取消服务器静音（Unmute）。

<a id="r_ga0c6d0b6b015f069a9adc1332a32c79f9"></a>

```c
int bt_vcp_vol_rend_mute (void)
```

相关声明：[bt_vcp_vol_rend_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c6d0b6b015f069a9adc1332a32c79f9)。

使服务器静音（Mute）。

<a id="r_ga7861d0c3426870c015106e8e170004a3"></a>

```c
int bt_vcp_vol_ctlr_cb_register (struct bt_vcp_vol_ctlr_cb *cb)
```

相关声明：[bt_vcp_vol_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga7861d0c3426870c015106e8e170004a3)、[bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)。

注册音量控制器（Volume Controller）使用的回调。

<a id="r_gae69e4730df4341bbb9bbbba1bea14005"></a>

```c
int bt_vcp_vol_ctlr_cb_unregister (struct bt_vcp_vol_ctlr_cb *cb)
```

相关声明：[bt_vcp_vol_ctlr_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae69e4730df4341bbb9bbbba1bea14005)、[bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)。

注销音量控制器（Volume Controller）使用的回调。

<a id="r_gac18d43a0785155c1131249f95554f2de"></a>

```c
int bt_vcp_vol_ctlr_discover (struct bt_conn *conn, struct bt_vcp_vol_ctlr **vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gac18d43a0785155c1131249f95554f2de)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

发现音量控制服务（Volume Control Service）及其包含的服务。

<a id="r_ga0c8faa95cc36950c70ff572c931eedee"></a>

```c
struct bt_vcp_vol_ctlr * bt_vcp_vol_ctlr_get_by_conn (const struct bt_conn *conn)
```

相关声明：[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_vcp_vol_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c8faa95cc36950c70ff572c931eedee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

根据连接指针获取音量控制器（Volume Controller）。

<a id="r_gab287197243191e3dbf162c6d16b6d726"></a>

```c
int bt_vcp_vol_ctlr_conn_get (const struct bt_vcp_vol_ctlr *vol_ctlr, struct bt_conn **conn)
```

相关声明：[bt_vcp_vol_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gab287197243191e3dbf162c6d16b6d726)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取客户端实例的连接指针（Connection Pointer）。

<a id="r_gaaa748c49e103ff161f67df9663ea6330"></a>

```c
int bt_vcp_vol_ctlr_included_get (struct bt_vcp_vol_ctlr *vol_ctlr, struct bt_vcp_included *included)
```

相关声明：[bt_vcp_vol_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa748c49e103ff161f67df9663ea6330)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)。

获取音量控制服务（Volume Control Service）包含的服务。

<a id="r_ga68cab2f59c63542b6a7da33d555da0ab"></a>

```c
int bt_vcp_vol_ctlr_read_state (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_read_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga68cab2f59c63542b6a7da33d555da0ab)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

读取远端音量渲染器（Volume Renderer）的音量状态。

<a id="r_gaefc226a5abb6bb1540d4b44ac4ddc236"></a>

```c
int bt_vcp_vol_ctlr_read_flags (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_read_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaefc226a5abb6bb1540d4b44ac4ddc236)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

读取远端音量渲染器（Volume Renderer）的音量标志。

<a id="r_ga03e073e29920f4a530d2f8851b4b8df4"></a>

```c
int bt_vcp_vol_ctlr_vol_down (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga03e073e29920f4a530d2f8851b4b8df4)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量降低一步。

<a id="r_ga908eb20727e1d68ed569badfd13ff896"></a>

```c
int bt_vcp_vol_ctlr_vol_up (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga908eb20727e1d68ed569badfd13ff896)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量提高一步。

<a id="r_ga20348b220988c700cabf356f7165d4d6"></a>

```c
int bt_vcp_vol_ctlr_unmute_vol_down (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga20348b220988c700cabf356f7165d4d6)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量降低一步并取消静音。

<a id="r_ga2defdeee7486eee22a3416db8aa7c251"></a>

```c
int bt_vcp_vol_ctlr_unmute_vol_up (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga2defdeee7486eee22a3416db8aa7c251)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

将远端音量渲染器（Volume Renderer）的音量提高一步并取消静音。

<a id="r_gaaa5b5cd9a11c0e1fcdabce690ba20616"></a>

```c
int bt_vcp_vol_ctlr_set_vol (struct bt_vcp_vol_ctlr *vol_ctlr, uint8_t volume)
```

相关声明：[bt_vcp_vol_ctlr_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa5b5cd9a11c0e1fcdabce690ba20616)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置远端音量渲染器（Volume Renderer）的绝对音量（Absolute Volume）。

<a id="r_ga4e95c3fb071cb94fbe75f88e96d34b36"></a>

```c
int bt_vcp_vol_ctlr_unmute (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4e95c3fb071cb94fbe75f88e96d34b36)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

取消远端音量渲染器（Volume Renderer）的静音。

<a id="r_ga106b7f826adec665b4f0ac3d5e82b867"></a>

```c
int bt_vcp_vol_ctlr_mute (struct bt_vcp_vol_ctlr *vol_ctlr)
```

相关声明：[bt_vcp_vol_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga106b7f826adec665b4f0ac3d5e82b867)、[bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)。

使远端音量渲染器（Volume Renderer）静音。


## 28.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/audio/aics.h](../api_source_reference/P018_aics.h_源码浏览.md)
- [zephyr/bluetooth/audio/vocs.h](../api_source_reference/P914_vocs.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P902_vcp.h_源码浏览.md)
- [bt_vcp_vol_rend_register_param](../bluetooth_service_model_reference/P183_bt_vcp_vol_rend_register_param_结构体.md)
- [bt_vcp_included](../bluetooth_service_model_reference/P179_bt_vcp_included_结构体.md)
- [bt_vcp_vol_rend_cb](../bluetooth_service_model_reference/P182_bt_vcp_vol_rend_cb_结构体.md)
- [bt_vcp_vol_ctlr_cb](../bluetooth_service_model_reference/P181_bt_vcp_vol_ctlr_cb_结构体.md)
- [BT_VCP_VOL_REND_VOCS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae7195f4556ad2442bc45d8d43cdeedd0)
- [BT_VCP_VOL_REND_AICS_CNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga571d7ff5a6a507fcd7cbdfa32a04643b)
- [BT_VCP_ERR_INVALID_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gabb8bdfde60f1cbb31bab41fd61b3384b)
- [BT_VCP_ERR_OP_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gad979c43e4d84f52009d9931fb74628e6)
- [BT_VCP_STATE_UNMUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4660f938a16113f715dd8aec3ed3baf6)
- [BT_VCP_STATE_MUTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga3d6ffdfb9e0d8d58073f4a130a8020b0)
- [bt_vcp_vol_rend_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1761d6618c48983e034cee5574c9c34f)
- [bt_vcp_vol_rend_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga752d8ff54a4b8c8c854a9c693617e64d)
- [bt_vcp_vol_rend_set_step](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga56e0f99d2688fb6f9e0e4d9103de706c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_vcp_vol_rend_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga9d1ac028abc88549ea18b6a0c585c781)
- [bt_vcp_vol_rend_get_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga1e6c9cfa0d012a4b701c99d8e6b5985d)
- [bt_vcp_vol_rend_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaf3c622f151a21d1dd617e97917c5ff5e)
- [bt_vcp_vol_rend_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga6c10dd5a029b524994739f0b37a82c84)
- [bt_vcp_vol_rend_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga3e6236a8679f95ba512181284a05923d)
- [bt_vcp_vol_rend_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gadf77729fee34f6605101c278fd2b7c46)
- [bt_vcp_vol_rend_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga61279baeba11152625cd3a87c5d973c9)
- [bt_vcp_vol_rend_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga303d4b6b77987ab41cb1753ef861dd6c)
- [bt_vcp_vol_rend_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c6d0b6b015f069a9adc1332a32c79f9)
- [bt_vcp_vol_ctlr_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga7861d0c3426870c015106e8e170004a3)
- [bt_vcp_vol_ctlr_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gae69e4730df4341bbb9bbbba1bea14005)
- [bt_vcp_vol_ctlr_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gac18d43a0785155c1131249f95554f2de)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_vcp_vol_ctlr](../bluetooth_service_model_reference/P180_bt_vcp_vol_ctlr_结构体.md)
- [bt_vcp_vol_ctlr_get_by_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga0c8faa95cc36950c70ff572c931eedee)
- [bt_vcp_vol_ctlr_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gab287197243191e3dbf162c6d16b6d726)
- [bt_vcp_vol_ctlr_included_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa748c49e103ff161f67df9663ea6330)
- [bt_vcp_vol_ctlr_read_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga68cab2f59c63542b6a7da33d555da0ab)
- [bt_vcp_vol_ctlr_read_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaefc226a5abb6bb1540d4b44ac4ddc236)
- [bt_vcp_vol_ctlr_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga03e073e29920f4a530d2f8851b4b8df4)
- [bt_vcp_vol_ctlr_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga908eb20727e1d68ed569badfd13ff896)
- [bt_vcp_vol_ctlr_unmute_vol_down](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga20348b220988c700cabf356f7165d4d6)
- [bt_vcp_vol_ctlr_unmute_vol_up](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga2defdeee7486eee22a3416db8aa7c251)
- [bt_vcp_vol_ctlr_set_vol](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#gaaa5b5cd9a11c0e1fcdabce690ba20616)
- [bt_vcp_vol_ctlr_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga4e95c3fb071cb94fbe75f88e96d34b36)
- [bt_vcp_vol_ctlr_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html#ga106b7f826adec665b4f0ac3d5e82b867)

<a id="header-details"></a>

---

[上一章](P027_zephyr__usb_c__usbc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__drivers__sensor__veml7700.h_文件参考.md)
