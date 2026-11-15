---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-3
title: 固件分发模型（Firmware Distribution models）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_固件分发模型（Firmware Distribution models）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_bt_5Fmesh_5Fdfd_5Fsrv"></a>

相关声明：[固件分发服务器模型（Firmware Distribution Server model）](../api_extension_topic_reference/P004_固件分发服务器模型（Firmware Distribution Server model）.md)。

固件分发服务器模型的 API。

<a id="header-files"></a>
<a id="files"></a>

## 3.2\_文件（Files）

<a id="r_dfd_2Eh"></a>

```c
file dfd.h
```

相关声明：[dfd.h](../api_file_runtime_reference/P008_zephyr__bluetooth__mesh__dfd.h_文件参考.md)。

蓝牙Mesh固件分发模型（Firmware Distribution Models）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_gaedd84b3b4bdde360c860d3cb04b301d5"></a>

```c
enum bt_mesh_dfd_status { BT_MESH_DFD_SUCCESS , BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES , BT_MESH_DFD_ERR_WRONG_PHASE , BT_MESH_DFD_ERR_INTERNAL , BT_MESH_DFD_ERR_FW_NOT_FOUND , BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX , BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY , BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION , BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD , BT_MESH_DFD_ERR_URI_NOT_SUPPORTED , BT_MESH_DFD_ERR_URI_MALFORMED , BT_MESH_DFD_ERR_URI_UNREACHABLE , BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE , BT_MESH_DFD_ERR_SUSPEND_FAILED }
```

相关声明：[bt_mesh_dfd_status](#gaedd84b3b4bdde360c860d3cb04b301d5)、[BT_MESH_DFD_SUCCESS](#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f)、[BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES](#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da)、[BT_MESH_DFD_ERR_WRONG_PHASE](#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f)、[BT_MESH_DFD_ERR_INTERNAL](#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced)、[BT_MESH_DFD_ERR_FW_NOT_FOUND](#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e)、[BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX](#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65)、[BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY](#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b)、[BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION](#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a)、[BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD](#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280)、[BT_MESH_DFD_ERR_URI_NOT_SUPPORTED](#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c)、[BT_MESH_DFD_ERR_URI_MALFORMED](#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523)、[BT_MESH_DFD_ERR_URI_UNREACHABLE](#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256)、[BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE](#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7)、[BT_MESH_DFD_ERR_SUSPEND_FAILED](#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)。

固件分发状态（Firmware Distribution Status）。

<a id="r_gab6562d62668ebcdb146be35b909c30c2"></a>

```c
enum bt_mesh_dfd_phase { BT_MESH_DFD_PHASE_IDLE , BT_MESH_DFD_PHASE_TRANSFER_ACTIVE , BT_MESH_DFD_PHASE_TRANSFER_SUCCESS , BT_MESH_DFD_PHASE_APPLYING_UPDATE , BT_MESH_DFD_PHASE_COMPLETED , BT_MESH_DFD_PHASE_FAILED , BT_MESH_DFD_PHASE_CANCELING_UPDATE , BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED }
```

相关声明：[bt_mesh_dfd_phase](#gab6562d62668ebcdb146be35b909c30c2)、[BT_MESH_DFD_PHASE_IDLE](#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93)、[BT_MESH_DFD_PHASE_TRANSFER_ACTIVE](#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497)、[BT_MESH_DFD_PHASE_TRANSFER_SUCCESS](#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c)、[BT_MESH_DFD_PHASE_APPLYING_UPDATE](#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf)、[BT_MESH_DFD_PHASE_COMPLETED](#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817)、[BT_MESH_DFD_PHASE_FAILED](#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab)、[BT_MESH_DFD_PHASE_CANCELING_UPDATE](#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886)、[BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED](#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)。

固件分发阶段（Firmware Distribution Phases）。

<a id="r_ga1cce8331a0876c056b25175df32188fb"></a>

```c
enum bt_mesh_dfd_upload_phase { BT_MESH_DFD_UPLOAD_PHASE_IDLE , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR , BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS }
```

相关声明：[bt_mesh_dfd_upload_phase](#ga1cce8331a0876c056b25175df32188fb)、[BT_MESH_DFD_UPLOAD_PHASE_IDLE](#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE](#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR](#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14)、[BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS](#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0)。

固件上传阶段（Firmware Upload Phases）。

## 3.4\_详细说明（Detailed Documentation）

<a id="gab6562d62668ebcdb146be35b909c30c2"></a>

### `bt_mesh_dfd_phase`

```c
enum bt_mesh_dfd_phase
```

```c
#include <zephyr/bluetooth/mesh/dfd.h>
```

固件分发阶段（Firmware Distribution Phases）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFD_PHASE_IDLE` | 当前没有进行中的固件分发（Firmware Distribution）。 |
| `BT_MESH_DFD_PHASE_TRANSFER_ACTIVE` | 固件分发（Firmware Distribution）正在进行。 |
| `BT_MESH_DFD_PHASE_TRANSFER_SUCCESS` | 传输二进制大对象流程（Transfer BLOB Procedure）已成功完成。 |
| `BT_MESH_DFD_PHASE_APPLYING_UPDATE` | 正在执行在目标节点应用固件流程（Apply Firmware on Target Nodes Procedure）。 |
| `BT_MESH_DFD_PHASE_COMPLETED` | 分发固件流程（Distribute Firmware Procedure）已成功完成。 |
| `BT_MESH_DFD_PHASE_FAILED` | 分发固件流程（Distribute Firmware Procedure）失败。 |
| `BT_MESH_DFD_PHASE_CANCELING_UPDATE` | 正在执行取消固件更新流程（Cancel Firmware Update Procedure）。 |
| `BT_MESH_DFD_PHASE_TRANSFER_SUSPENDED` | 传输二进制大对象流程（Transfer BLOB Procedure）已挂起。 |

<a id="gaedd84b3b4bdde360c860d3cb04b301d5"></a>

### `bt_mesh_dfd_status`

```c
enum bt_mesh_dfd_status
```

```c
#include <zephyr/bluetooth/mesh/dfd.h>
```

固件分发状态（Firmware Distribution Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFD_SUCCESS` | 消息已成功处理（Processed Successfully）。 |
| `BT_MESH_DFD_ERR_INSUFFICIENT_RESOURCES` | 节点上的资源不足（Insufficient Resources）。 |
| `BT_MESH_DFD_ERR_WRONG_PHASE` | 服务器处于当前阶段（Phase）时，无法执行该操作。 |
| `BT_MESH_DFD_ERR_INTERNAL` | 节点发生内部错误（Internal Error）。 |
| `BT_MESH_DFD_ERR_FW_NOT_FOUND` | 请求的固件镜像（Firmware Image）未存储在分发器（Distributor）上。 |
| `BT_MESH_DFD_ERR_INVALID_APPKEY_INDEX` | 节点不知道应用密钥索引（AppKey Index）所标识的应用密钥（AppKey）。 |
| `BT_MESH_DFD_ERR_RECEIVERS_LIST_EMPTY` | 分发接收端列表状态（Distribution Receivers List State）中没有目标节点。 |
| `BT_MESH_DFD_ERR_BUSY_WITH_DISTRIBUTION` | 另一个固件镜像分发（Firmware Image Distribution）正在进行。 |
| `BT_MESH_DFD_ERR_BUSY_WITH_UPLOAD` | 另一次上传（Upload）正在进行。 |
| `BT_MESH_DFD_ERR_URI_NOT_SUPPORTED` | 不支持更新统一资源标识符（Update URI）指示的 URI 方案名称（Scheme Name）。 |
| `BT_MESH_DFD_ERR_URI_MALFORMED` | 更新统一资源标识符（Update URI）的格式无效。 |
| `BT_MESH_DFD_ERR_URI_UNREACHABLE` | 该统一资源标识符（URI）当前不可访问。 |
| `BT_MESH_DFD_ERR_NEW_FW_NOT_AVAILABLE` | 带外检查固件流程（Check Firmware OOB Procedure）未找到任何新固件。 |
| `BT_MESH_DFD_ERR_SUSPEND_FAILED` | 挂起分发固件流程（Distribute Firmware Procedure）失败。 |

<a id="ga1cce8331a0876c056b25175df32188fb"></a>

### `bt_mesh_dfd_upload_phase`

```c
enum bt_mesh_dfd_upload_phase
```

```c
#include <zephyr/bluetooth/mesh/dfd.h>
```

固件上传阶段（Firmware Upload Phases）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFD_UPLOAD_PHASE_IDLE` | 当前没有进行中的固件上传（Firmware Upload）。 |
| `BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ACTIVE` | 正在执行存储固件流程（Store Firmware Procedure）。 |
| `BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_ERROR` | 存储固件流程（Store Firmware Procedure）或带外存储固件流程（Store Firmware OOB Procedure）失败。 |
| `BT_MESH_DFD_UPLOAD_PHASE_TRANSFER_SUCCESS` | 存储固件流程（Store Firmware Procedure）或带外存储固件流程（Store Firmware OOB Procedure）已成功完成。 |


## 3.5\_原页交叉引用（Cross References）

- [固件分发服务器模型（Firmware Distribution Server model）](../api_extension_topic_reference/P004_固件分发服务器模型（Firmware Distribution Server model）.md)
- [dfd.h](../api_file_runtime_reference/P008_zephyr__bluetooth__mesh__dfd.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886"></a>
<a id="ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7"></a>
<a id="ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e"></a>
<a id="gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e"></a>
<a id="gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65"></a>
<a id="gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14"></a>
<a id="gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0"></a>

---

[上一章](P002_蓝牙 HID 设备（Device）.md) · [返回大纲](大纲.md) · [下一章](P004_麦克风控制配置文件（Microphone Control Profile，MICP）.md)
