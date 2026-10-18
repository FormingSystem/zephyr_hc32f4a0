---
id: learning.zephyr-docs.shell-management-reference.page-1
title: 蓝牙Mesh_Shell头文件参考
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2shell_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_蓝牙Mesh\_Shell头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2shell_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

蓝牙Mesh Shell命令（Bluetooth Mesh Shell Commands）的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh Shell命令（Bluetooth Mesh Shell Commands）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fshell_5Ftarget"></a>

```c
struct bt_mesh_shell_target
```

相关声明：[bt_mesh_shell_target](P003_蓝牙Mesh_Shell目标结构.md)。

Mesh Shell的目标上下文（Target Context）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_aac63a324676ab3297e509fc5d1afe951"></a>

```c
#define BT_MESH_SHELL_CUR_FAULTS_MAX 4
```

相关声明：[BT_MESH_SHELL_CUR_FAULTS_MAX](#aac63a324676ab3297e509fc5d1afe951)。

健康服务器（Health Server）可具有的最大故障数量（Fault Count）。

<a id="r_a8cd77ce286185c704e64c891d315a1d0"></a>

```c
#define BT_MESH_SHELL_HEALTH_PUB_DEFINE(_name)
```

相关声明：[BT_MESH_SHELL_HEALTH_PUB_DEFINE](#a8cd77ce286185c704e64c891d315a1d0)。

为Shell定义健康模型发布上下文（Health Publication Context）的辅助宏，使用Shell所允许的元素最大故障数量。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 1.3\_变量（Variables）

<a id="r_a313cd00833d5b522a73a3ac5e4eb9596"></a>

```c
struct bt_mesh_health_srv bt_mesh_shell_health_srv
```

相关声明：[bt_mesh_health_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)、[bt_mesh_shell_health_srv](#a313cd00833d5b522a73a3ac5e4eb9596)。

健康服务器（Health Server）的外部引用（External Reference）。

<a id="r_a5ccd2d0b4a3ff642a89fcd77dd0e935f"></a>

```c
const struct bt_mesh_models_metadata_entry health_srv_meta []
```

相关声明：[bt_mesh_models_metadata_entry](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)、[health_srv_meta](#a5ccd2d0b4a3ff642a89fcd77dd0e935f)。

健康服务器元数据（Health Server Metadata）的外部引用。

<a id="r_a4c7a470a6d7cc91ea1b240756053d017"></a>

```c
struct bt_mesh_health_cli bt_mesh_shell_health_cli
```

相关声明：[bt_mesh_health_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html)、[bt_mesh_shell_health_cli](#a4c7a470a6d7cc91ea1b240756053d017)。

健康客户端（Health Client）的外部引用。

<a id="r_a0bac1827aa84e4801252c9b955373067"></a>

```c
struct bt_mesh_dfu_srv bt_mesh_shell_dfu_srv
```

相关声明：[bt_mesh_dfu_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html)、[bt_mesh_shell_dfu_srv](#a0bac1827aa84e4801252c9b955373067)。

固件更新服务器（Firmware Update Server）的外部引用。

<a id="r_a9bc67c98117f6a8741bbd3e40f718b3b"></a>

```c
struct bt_mesh_dfu_cli bt_mesh_shell_dfu_cli
```

相关声明：[bt_mesh_dfu_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html)、[bt_mesh_shell_dfu_cli](#a9bc67c98117f6a8741bbd3e40f718b3b)。

固件更新客户端（Firmware Update Client）的外部引用。

<a id="r_a4c4b37f663428cedfb466832963b9c1b"></a>

```c
struct bt_mesh_blob_srv bt_mesh_shell_blob_srv
```

相关声明：[bt_mesh_blob_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html)、[bt_mesh_shell_blob_srv](#a4c4b37f663428cedfb466832963b9c1b)。

二进制大对象传输服务器（BLOB Transfer Server）的外部引用。

<a id="r_accbfc012251815338ace23f8cb49fff6"></a>

```c
struct bt_mesh_blob_cli bt_mesh_shell_blob_cli
```

相关声明：[bt_mesh_blob_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html)、[bt_mesh_shell_blob_cli](#accbfc012251815338ace23f8cb49fff6)。

二进制大对象传输客户端（BLOB Transfer Client）的外部引用。

<a id="r_a231f1c8492097ae23edb2aeb82139752"></a>

```c
struct bt_mesh_rpr_cli bt_mesh_shell_rpr_cli
```

相关声明：[bt_mesh_rpr_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html)、[bt_mesh_shell_rpr_cli](#a231f1c8492097ae23edb2aeb82139752)。

远程配网客户端（Remote Provisioning Client）的外部引用。

<a id="r_a1e999cded973436a218782acac1ab15b"></a>

```c
struct bt_mesh_prov bt_mesh_shell_prov
```

相关声明：[bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)、[bt_mesh_shell_prov](#a1e999cded973436a218782acac1ab15b)。

配网处理对象（Provisioning Handler）的外部引用。

<a id="r_ab76d90bc284131a56904a2c1b9c19ae2"></a>

```c
struct bt_mesh_shell_target bt_mesh_shell_target_ctx
```

相关声明：[bt_mesh_shell_target](P003_蓝牙Mesh_Shell目标结构.md)、[bt_mesh_shell_target_ctx](#ab76d90bc284131a56904a2c1b9c19ae2)。

Shell目标上下文（Target Context）的外部引用。

## 1.4\_详细说明（Detailed Documentation）

<a id="aac63a324676ab3297e509fc5d1afe951"></a>

### `BT_MESH_SHELL_CUR_FAULTS_MAX`

```c
#define BT_MESH_SHELL_CUR_FAULTS_MAX 4
```

健康服务器（Health Server）可具有的最大故障数量（Fault Count）。

<a id="a8cd77ce286185c704e64c891d315a1d0"></a>

### `BT_MESH_SHELL_HEALTH_PUB_DEFINE`

```c
#define BT_MESH_SHELL_HEALTH_PUB_DEFINE ( _name)
```

展开值（Value）：

```c
BT_MESH_HEALTH_PUB_DEFINE(_name,                               \
                          BT_MESH_SHELL_CUR_FAULTS_MAX);
```

为Shell定义健康模型发布上下文（Health Publication Context）的辅助宏，使用Shell所允许的元素最大故障数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 发布上下文变量（Publication Context Variable）的名称。 |

<a id="accbfc012251815338ace23f8cb49fff6"></a>

### `bt_mesh_shell_blob_cli`

```c
struct bt_mesh_blob_cli bt_mesh_shell_blob_cli
```

声明属性：`extern`。

二进制大对象传输客户端（BLOB Transfer Client）的外部引用。

<a id="a4c4b37f663428cedfb466832963b9c1b"></a>

### `bt_mesh_shell_blob_srv`

```c
struct bt_mesh_blob_srv bt_mesh_shell_blob_srv
```

声明属性：`extern`。

二进制大对象传输服务器（BLOB Transfer Server）的外部引用。

<a id="a9bc67c98117f6a8741bbd3e40f718b3b"></a>

### `bt_mesh_shell_dfu_cli`

```c
struct bt_mesh_dfu_cli bt_mesh_shell_dfu_cli
```

声明属性：`extern`。

固件更新客户端（Firmware Update Client）的外部引用。

<a id="a0bac1827aa84e4801252c9b955373067"></a>

### `bt_mesh_shell_dfu_srv`

```c
struct bt_mesh_dfu_srv bt_mesh_shell_dfu_srv
```

声明属性：`extern`。

固件更新服务器（Firmware Update Server）的外部引用。

<a id="a4c7a470a6d7cc91ea1b240756053d017"></a>

### `bt_mesh_shell_health_cli`

```c
struct bt_mesh_health_cli bt_mesh_shell_health_cli
```

声明属性：`extern`。

健康客户端（Health Client）的外部引用。

<a id="a313cd00833d5b522a73a3ac5e4eb9596"></a>

### `bt_mesh_shell_health_srv`

```c
struct bt_mesh_health_srv bt_mesh_shell_health_srv
```

声明属性：`extern`。

健康服务器（Health Server）的外部引用（External Reference）。

<a id="a1e999cded973436a218782acac1ab15b"></a>

### `bt_mesh_shell_prov`

```c
struct bt_mesh_prov bt_mesh_shell_prov
```

声明属性：`extern`。

配网处理对象（Provisioning Handler）的外部引用。

<a id="a231f1c8492097ae23edb2aeb82139752"></a>

### `bt_mesh_shell_rpr_cli`

```c
struct bt_mesh_rpr_cli bt_mesh_shell_rpr_cli
```

声明属性：`extern`。

远程配网客户端（Remote Provisioning Client）的外部引用。

<a id="ab76d90bc284131a56904a2c1b9c19ae2"></a>

### `bt_mesh_shell_target_ctx`

```c
struct bt_mesh_shell_target bt_mesh_shell_target_ctx
```

声明属性：`extern`。

Shell目标上下文（Target Context）的外部引用。

<a id="a5ccd2d0b4a3ff642a89fcd77dd0e935f"></a>

### `health_srv_meta`

```c
const struct bt_mesh_models_metadata_entry health_srv_meta[]
```

声明属性：`extern`。

健康服务器元数据（Health Server Metadata）的外部引用。

## 1.5\_源码定位与版本边界

源码定位：[include/zephyr/bluetooth/mesh/shell.h](../../../include/zephyr/bluetooth/mesh/shell.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：该头文件集中声明Mesh Shell所用模型对象和当前目标上下文；extern是对其他文件所定义对象的引用，并不在此创建新的模型实例。

> 译注——源码核对：健康发布宏把最大故障数量常量4传给BT_MESH_HEALTH_PUB_DEFINE。目标结构的dst、net_idx和app_idx分别保存当前目标地址、网络索引和应用索引；字段解释来自本册源码页中保留的普通注释。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h_source.html)
- [查看此文件的源码](P002_蓝牙Mesh_Shell头文件源码.md)
- [bt_mesh_shell_target](P003_蓝牙Mesh_Shell目标结构.md)
- [bt_mesh_health_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)
- [bt_mesh_models_metadata_entry](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)
- [bt_mesh_health_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html)
- [bt_mesh_dfu_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html)
- [bt_mesh_dfu_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html)
- [bt_mesh_blob_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html)
- [bt_mesh_blob_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html)
- [bt_mesh_rpr_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html)
- [bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)
- [BT_MESH_HEALTH_PUB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__srv.html#ga35c500e915092ec365862b11e76f92ad)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="abluetooth_2mesh_2shell_8h_html_aac63a324676ab3297e509fc5d1afe951"></a>
<a id="agroup__bt__mesh__health__srv_html_ga35c500e915092ec365862b11e76f92ad"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙Mesh_Shell头文件源码.md)
