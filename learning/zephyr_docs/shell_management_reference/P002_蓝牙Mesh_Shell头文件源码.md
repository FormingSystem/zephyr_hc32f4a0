---
id: learning.zephyr-docs.shell-management-reference.page-2
title: 蓝牙Mesh_Shell头文件源码
kind: reference
status: maintained
domains: [zephyr, shell, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2shell_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_蓝牙Mesh\_Shell头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2shell_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P001_蓝牙Mesh_Shell头文件参考.md)和[公共接口](P001_蓝牙Mesh_Shell头文件参考.md)；访问语义和生命周期见本页译注。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00031"></a>
<a id="foldopen00036"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a0bac1827aa84e4801252c9b955373067"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a1e999cded973436a218782acac1ab15b"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a231f1c8492097ae23edb2aeb82139752"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a313cd00833d5b522a73a3ac5e4eb9596"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a4c4b37f663428cedfb466832963b9c1b"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a4c7a470a6d7cc91ea1b240756053d017"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a5ccd2d0b4a3ff642a89fcd77dd0e935f"></a>
<a id="abluetooth_2mesh_2shell_8h_html_a9bc67c98117f6a8741bbd3e40f718b3b"></a>
<a id="abluetooth_2mesh_2shell_8h_html_ab76d90bc284131a56904a2c1b9c19ae2"></a>
<a id="abluetooth_2mesh_2shell_8h_html_accbfc012251815338ace23f8cb49fff6"></a>
<a id="amesh_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__cli_html"></a>
<a id="astructbt__mesh__blob__srv_html"></a>
<a id="astructbt__mesh__dfu__cli_html"></a>
<a id="astructbt__mesh__dfu__srv_html"></a>
<a id="astructbt__mesh__health__cli_html"></a>
<a id="astructbt__mesh__health__srv_html"></a>
<a id="astructbt__mesh__models__metadata__entry_html"></a>
<a id="astructbt__mesh__prov_html"></a>
<a id="astructbt__mesh__rpr__cli_html"></a>
<a id="astructbt__mesh__shell__target_html"></a>
<a id="astructbt__mesh__shell__target_html_a2cb816bbfd493656d327cd604254fdbd"></a>
<a id="astructbt__mesh__shell__target_html_a48a9039d99fefb8a536c427161359485"></a>
<a id="astructbt__mesh__shell__target_html_a52c511cf9843512ec6d8db7cec6f6fa1"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2021 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_SHELL_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_SHELL_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/bluetooth/mesh.h&gt;
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00023"></a>#define BT_MESH_SHELL_CUR_FAULTS_MAX 4
<a id="l00024"></a>
<a id="l00031"></a>#define BT_MESH_SHELL_HEALTH_PUB_DEFINE(_name)                                 \
<a id="l00032"></a>                BT_MESH_HEALTH_PUB_DEFINE(_name,                               \
<a id="l00033"></a>                                          BT_MESH_SHELL_CUR_FAULTS_MAX);
<a id="l00034"></a>
<a id="l00036"></a>struct bt_mesh_shell_target {
<a id="l00037"></a>        /* Current destination address */
<a id="l00038"></a>        uint16_t dst;
<a id="l00039"></a>        /* Current net index */
<a id="l00040"></a>        uint16_t net_idx;
<a id="l00041"></a>        /* Current app index */
<a id="l00042"></a>        uint16_t app_idx;
<a id="l00043"></a>};
<a id="l00044"></a>
<a id="l00046"></a>extern struct bt_mesh_health_srv bt_mesh_shell_health_srv;
<a id="l00047"></a>
<a id="l00049"></a>extern const struct bt_mesh_models_metadata_entry health_srv_meta[];
<a id="l00050"></a>
<a id="l00052"></a>extern struct bt_mesh_health_cli bt_mesh_shell_health_cli;
<a id="l00053"></a>
<a id="l00055"></a>extern struct bt_mesh_dfu_srv bt_mesh_shell_dfu_srv;
<a id="l00056"></a>
<a id="l00058"></a>extern struct bt_mesh_dfu_cli bt_mesh_shell_dfu_cli;
<a id="l00059"></a>
<a id="l00061"></a>extern struct bt_mesh_blob_srv bt_mesh_shell_blob_srv;
<a id="l00062"></a>
<a id="l00064"></a>extern struct bt_mesh_blob_cli bt_mesh_shell_blob_cli;
<a id="l00065"></a>
<a id="l00067"></a>extern struct bt_mesh_rpr_cli bt_mesh_shell_rpr_cli;
<a id="l00068"></a>
<a id="l00070"></a>extern struct bt_mesh_prov bt_mesh_shell_prov;
<a id="l00071"></a>
<a id="l00073"></a>extern struct bt_mesh_shell_target bt_mesh_shell_target_ctx;
<a id="l00074"></a>
<a id="l00075"></a>#ifdef __cplusplus
<a id="l00076"></a>}
<a id="l00077"></a>#endif
<a id="l00078"></a>
<a id="l00079"></a>#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_SHELL_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2021 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 当前目标地址（Destination Address）。

3. 当前网络索引（Network Index）。

4. 当前应用索引（Application Index）。

5. ZEPHYR_INCLUDE_BLUETOOTH_MESH_SHELL_H_头文件包含保护结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `bt_mesh_shell_dfu_srv`

```c
struct bt_mesh_dfu_srv bt_mesh_shell_dfu_srv
```

固件更新服务器（Firmware Update Server）的外部引用。

符号定位：[bt_mesh_shell_dfu_srv](P001_蓝牙Mesh_Shell头文件参考.md#a0bac1827aa84e4801252c9b955373067)。

### `bt_mesh_shell_prov`

```c
struct bt_mesh_prov bt_mesh_shell_prov
```

配网处理对象（Provisioning Handler）的外部引用。

符号定位：[bt_mesh_shell_prov](P001_蓝牙Mesh_Shell头文件参考.md#a1e999cded973436a218782acac1ab15b)。

### `bt_mesh_shell_rpr_cli`

```c
struct bt_mesh_rpr_cli bt_mesh_shell_rpr_cli
```

远程配网客户端（Remote Provisioning Client）的外部引用。

符号定位：[bt_mesh_shell_rpr_cli](P001_蓝牙Mesh_Shell头文件参考.md#a231f1c8492097ae23edb2aeb82139752)。

### `bt_mesh_shell_health_srv`

```c
struct bt_mesh_health_srv bt_mesh_shell_health_srv
```

健康服务器（Health Server）的外部引用（External Reference）。

符号定位：[bt_mesh_shell_health_srv](P001_蓝牙Mesh_Shell头文件参考.md#a313cd00833d5b522a73a3ac5e4eb9596)。

### `bt_mesh_shell_blob_srv`

```c
struct bt_mesh_blob_srv bt_mesh_shell_blob_srv
```

二进制大对象传输服务器（BLOB Transfer Server）的外部引用。

符号定位：[bt_mesh_shell_blob_srv](P001_蓝牙Mesh_Shell头文件参考.md#a4c4b37f663428cedfb466832963b9c1b)。

### `bt_mesh_shell_health_cli`

```c
struct bt_mesh_health_cli bt_mesh_shell_health_cli
```

健康客户端（Health Client）的外部引用。

符号定位：[bt_mesh_shell_health_cli](P001_蓝牙Mesh_Shell头文件参考.md#a4c7a470a6d7cc91ea1b240756053d017)。

### `health_srv_meta`

```c
const struct bt_mesh_models_metadata_entry health_srv_meta[]
```

健康服务器元数据（Health Server Metadata）的外部引用。

符号定位：[health_srv_meta](P001_蓝牙Mesh_Shell头文件参考.md#a5ccd2d0b4a3ff642a89fcd77dd0e935f)。

### `bt_mesh_shell_dfu_cli`

```c
struct bt_mesh_dfu_cli bt_mesh_shell_dfu_cli
```

固件更新客户端（Firmware Update Client）的外部引用。

符号定位：[bt_mesh_shell_dfu_cli](P001_蓝牙Mesh_Shell头文件参考.md#a9bc67c98117f6a8741bbd3e40f718b3b)。

### `bt_mesh_shell_target_ctx`

```c
struct bt_mesh_shell_target bt_mesh_shell_target_ctx
```

Shell目标上下文（Target Context）的外部引用。

符号定位：[bt_mesh_shell_target_ctx](P001_蓝牙Mesh_Shell头文件参考.md#ab76d90bc284131a56904a2c1b9c19ae2)。

### `bt_mesh_shell_blob_cli`

```c
struct bt_mesh_blob_cli bt_mesh_shell_blob_cli
```

二进制大对象传输客户端（BLOB Transfer Client）的外部引用。

符号定位：[bt_mesh_shell_blob_cli](P001_蓝牙Mesh_Shell头文件参考.md#accbfc012251815338ace23f8cb49fff6)。

### `mesh.h`

蓝牙Mesh规范（Bluetooth Mesh Profile）API。

符号定位：[mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `bt_mesh_blob_cli`

BLOB传输客户端模型实例（BLOB Transfer Client Model Instance）。

定义位置（Definition）：blob_cli.h:299。

符号定位：[bt_mesh_blob_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html)。

### `bt_mesh_blob_srv`

BLOB传输服务器模型实例（BLOB Transfer Server Model Instance）。

定义位置（Definition）：blob_srv.h:137。

符号定位：[bt_mesh_blob_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html)。

### `bt_mesh_dfu_cli`

固件更新客户端模型实例（Firmware Update Client Model Instance）。

定义位置（Definition）：dfu_cli.h:184。

符号定位：[bt_mesh_dfu_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html)。

### `bt_mesh_dfu_srv`

固件更新服务器实例（Firmware Update Server Instance）。

定义位置（Definition）：dfu_srv.h:176。

符号定位：[bt_mesh_dfu_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html)。

### `bt_mesh_health_cli`

健康客户端模型上下文（Health Client Model Context）。

定义位置（Definition）：health_cli.h:27。

符号定位：[bt_mesh_health_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html)。

### `bt_mesh_health_srv`

Mesh健康服务器模型上下文（Health Server Model Context）。

定义位置（Definition）：health_srv.h:150。

符号定位：[bt_mesh_health_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)。

### `bt_mesh_models_metadata_entry`

模型元数据条目结构（Models Metadata Entry）。

定义位置（Definition）：access.h:604。

符号定位：[bt_mesh_models_metadata_entry](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)。

### `bt_mesh_prov`

配网属性与能力（Provisioning Properties and Capabilities）。

定义位置（Definition）：main.h:115。

符号定位：[bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)。

### `bt_mesh_rpr_cli`

远程配网客户端模型实例（Remote Provisioning Client Model Instance）。

定义位置（Definition）：rpr_cli.h:70。

符号定位：[bt_mesh_rpr_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html)。

### `bt_mesh_shell_target`

Mesh Shell的目标上下文（Target Context）。

定义位置（Definition）：shell.h:36。

符号定位：[bt_mesh_shell_target](P003_蓝牙Mesh_Shell目标结构.md)。

### `bt_mesh_shell_target::net_idx`

```c
uint16_t net_idx
```

定义位置（Definition）：shell.h:40。

符号定位：[bt_mesh_shell_target::net_idx](P003_蓝牙Mesh_Shell目标结构.md#a2cb816bbfd493656d327cd604254fdbd)。

### `bt_mesh_shell_target::dst`

```c
uint16_t dst
```

定义位置（Definition）：shell.h:38。

符号定位：[bt_mesh_shell_target::dst](P003_蓝牙Mesh_Shell目标结构.md#a48a9039d99fefb8a536c427161359485)。

### `bt_mesh_shell_target::app_idx`

```c
uint16_t app_idx
```

定义位置（Definition）：shell.h:42。

符号定位：[bt_mesh_shell_target::app_idx](P003_蓝牙Mesh_Shell目标结构.md#a52c511cf9843512ec6d8db7cec6f6fa1)。

## 2.4\_源码跟踪译注

> 译注——该头文件集中声明Mesh Shell所用模型对象和当前目标上下文；extern是对其他文件所定义对象的引用，并不在此创建新的模型实例。

> 译注——健康发布宏把最大故障数量常量4传给BT_MESH_HEALTH_PUB_DEFINE。目标结构的dst、net_idx和app_idx分别保存当前目标地址、网络索引和应用索引；字段解释来自本册源码页中保留的普通注释。

头文件定位：[include/zephyr/bluetooth/mesh/shell.h](../../../include/zephyr/bluetooth/mesh/shell.h)，关联实现／接口：[subsys/bluetooth/mesh/shell/health.c](../../../subsys/bluetooth/mesh/shell/health.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/mesh/shell.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/mesh/shell/health.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_蓝牙Mesh_Shell头文件参考.md)
- [zephyr/bluetooth/mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/mesh_8h.html)
- [bt_mesh_shell_target](P003_蓝牙Mesh_Shell目标结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [dst](P003_蓝牙Mesh_Shell目标结构.md#a48a9039d99fefb8a536c427161359485)
- [net_idx](P003_蓝牙Mesh_Shell目标结构.md#a2cb816bbfd493656d327cd604254fdbd)
- [app_idx](P003_蓝牙Mesh_Shell目标结构.md#a52c511cf9843512ec6d8db7cec6f6fa1)
- [bt_mesh_health_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__srv.html)
- [bt_mesh_shell_health_srv](P001_蓝牙Mesh_Shell头文件参考.md#a313cd00833d5b522a73a3ac5e4eb9596)
- [bt_mesh_models_metadata_entry](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__models__metadata__entry.html)
- [health_srv_meta](P001_蓝牙Mesh_Shell头文件参考.md#a5ccd2d0b4a3ff642a89fcd77dd0e935f)
- [bt_mesh_health_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__health__cli.html)
- [bt_mesh_shell_health_cli](P001_蓝牙Mesh_Shell头文件参考.md#a4c7a470a6d7cc91ea1b240756053d017)
- [bt_mesh_dfu_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__srv.html)
- [bt_mesh_shell_dfu_srv](P001_蓝牙Mesh_Shell头文件参考.md#a0bac1827aa84e4801252c9b955373067)
- [bt_mesh_dfu_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html)
- [bt_mesh_shell_dfu_cli](P001_蓝牙Mesh_Shell头文件参考.md#a9bc67c98117f6a8741bbd3e40f718b3b)
- [bt_mesh_blob_srv](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html)
- [bt_mesh_shell_blob_srv](P001_蓝牙Mesh_Shell头文件参考.md#a4c4b37f663428cedfb466832963b9c1b)
- [bt_mesh_blob_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html)
- [bt_mesh_shell_blob_cli](P001_蓝牙Mesh_Shell头文件参考.md#accbfc012251815338ace23f8cb49fff6)
- [bt_mesh_rpr_cli](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html)
- [bt_mesh_shell_rpr_cli](P001_蓝牙Mesh_Shell头文件参考.md#a231f1c8492097ae23edb2aeb82139752)
- [bt_mesh_prov](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html)
- [bt_mesh_shell_prov](P001_蓝牙Mesh_Shell头文件参考.md#a1e999cded973436a218782acac1ab15b)
- [bt_mesh_shell_target_ctx](P001_蓝牙Mesh_Shell头文件参考.md#ab76d90bc284131a56904a2c1b9c19ae2)

---

[上一章](P001_蓝牙Mesh_Shell头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_蓝牙Mesh_Shell目标结构.md)
