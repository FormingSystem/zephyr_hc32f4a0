---
id: learning.zephyr-docs.api-file-service-interface-reference.page-14
title: zephyr__bluetooth__mesh__dfu_srv.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_bluetooth\_\_mesh\_\_dfu\_srv.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfu__srv_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/dfu.h>
#include <zephyr/bluetooth/mesh/blob_srv.h>
#include <zephyr/bluetooth/mesh/access.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfu_5Fsrv_5Fcb"></a>

```c
struct bt_mesh_dfu_srv_cb
```

相关声明：[bt_mesh_dfu_srv_cb](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md)。

固件更新服务器（Firmware Update Server）的事件回调。

<a id="r_bt_5Fmesh_5Fdfu_5Fsrv"></a>

```c
struct bt_mesh_dfu_srv
```

相关声明：[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

固件更新服务器（Firmware Update Server）的实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga8467cd5241dfdcd7add718bbaae6fa60"></a>

```c
#define BT_MESH_DFU_SRV_INIT(_handlers, _imgs, _img_count)
```

相关声明：[BT_MESH_DFU_SRV_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga8467cd5241dfdcd7add718bbaae6fa60)。

固件更新服务器模型（Firmware Update Server Model）的初始化参数。

<a id="r_gafdf78cc0f99668d38df4f29138392632"></a>

```c
#define BT_MESH_MODEL_DFU_SRV(_srv)
```

相关声明：[BT_MESH_MODEL_DFU_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#gafdf78cc0f99668d38df4f29138392632)。

固件更新服务器模型（Firmware Update Server Model）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_ga64eeb5bfe9bac8c1120c5e0aa9ce02ac"></a>

```c
void bt_mesh_dfu_srv_verified (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_verified](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

接受已接收的设备固件更新（DFU）传输。

<a id="r_ga77142a1f3cfe2ff1d53332114f977b38"></a>

```c
void bt_mesh_dfu_srv_rejected (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_rejected](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga77142a1f3cfe2ff1d53332114f977b38)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

拒绝已接收的设备固件更新（DFU）传输。

<a id="r_gaf5a00dd89faf52cd7797c54c572e1211"></a>

```c
void bt_mesh_dfu_srv_cancel (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#gaf5a00dd89faf52cd7797c54c572e1211)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

取消正在进行的设备固件更新（DFU）传输。

<a id="r_ga45aef92fe1de4c45ccb5369c1f5222ee"></a>

```c
void bt_mesh_dfu_srv_applied (struct bt_mesh_dfu_srv *srv)
```

相关声明：[bt_mesh_dfu_srv_applied](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga45aef92fe1de4c45ccb5369c1f5222ee)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

确认已应用收到的设备固件更新（DFU）传输内容。

<a id="r_ga94107fb1ca9207fc6918eae1fb1b3755"></a>

```c
bool bt_mesh_dfu_srv_is_busy (const struct bt_mesh_dfu_srv *srv)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_mesh_dfu_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga94107fb1ca9207fc6918eae1fb1b3755)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

检查固件更新服务器（Firmware Update Server）是否正忙于处理传输。

<a id="r_ga9f125ace97a40f060e0d8c59fd49f514"></a>

```c
uint8_t bt_mesh_dfu_srv_progress (const struct bt_mesh_dfu_srv *srv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_dfu_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga9f125ace97a40f060e0d8c59fd49f514)、[bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)。

获取当前设备固件更新（DFU）过程的进度，单位为百分比。


## 14.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu.h](../api_source_reference/P126_dfu.h_源码浏览.md)
- [zephyr/bluetooth/mesh/blob_srv.h](../api_source_runtime_reference/P002_blob_srv.h_源码浏览.md)
- [zephyr/bluetooth/mesh/access.h](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P016_dfu_srv.h_源码浏览.md)
- [bt_mesh_dfu_srv_cb](../bluetooth_mesh_model_reference/P056_bt_mesh_dfu_srv_cb_结构体.md)
- [bt_mesh_dfu_srv](../bluetooth_mesh_model_reference/P055_bt_mesh_dfu_srv_结构体.md)
- [BT_MESH_DFU_SRV_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga8467cd5241dfdcd7add718bbaae6fa60)
- [固件更新服务器模型（Firmware Update Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html)
- [BT_MESH_MODEL_DFU_SRV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#gafdf78cc0f99668d38df4f29138392632)
- [bt_mesh_dfu_srv_verified](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga64eeb5bfe9bac8c1120c5e0aa9ce02ac)
- [bt_mesh_dfu_srv_rejected](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga77142a1f3cfe2ff1d53332114f977b38)
- [bt_mesh_dfu_srv_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#gaf5a00dd89faf52cd7797c54c572e1211)
- [bt_mesh_dfu_srv_applied](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga45aef92fe1de4c45ccb5369c1f5222ee)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_dfu_srv_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga94107fb1ca9207fc6918eae1fb1b3755)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_dfu_srv_progress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__srv.html#ga9f125ace97a40f060e0d8c59fd49f514)

---

[上一章](P013_zephyr__modem__cmux.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__net__dhcpv4_server.h_文件参考.md)
