---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-4
title: 远程配网客户端模型（Remote Provisioning Client model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_远程配网客户端模型（Remote Provisioning Client model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_rpr_5Fcli_2Eh"></a>

```c
file rpr_cli.h
```

相关声明：[rpr_cli.h](../api_file_network_device_reference/P031_zephyr__bluetooth__mesh__rpr_cli.h_文件参考.md)。

蓝牙Mesh远程配网客户端（Remote Provisioning Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Frpr_5Fscan_5Fstatus"></a>

```c
struct bt_mesh_rpr_scan_status
```

相关声明：[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

扫描状态（Scan Status）的响应。

<a id="r_bt_5Fmesh_5Frpr_5Fcaps"></a>

```c
struct bt_mesh_rpr_caps
```

相关声明：[bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)。

远程配网服务器（Remote Provisioning Server）的扫描能力。

<a id="r_bt_5Fmesh_5Frpr_5Fcli"></a>

```c
struct bt_mesh_rpr_cli
```

相关声明：[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)。

远程配网客户端（Remote Provisioning Client）的模型实例。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.3\_宏定义（Macros）

<a id="r_gafa00eb1bff764a4ab723bb978b459297"></a>

```c
#define BT_MESH_RPR_SCAN_MAX_DEVS_ANY 0
```

相关声明：[BT_MESH_RPR_SCAN_MAX_DEVS_ANY](#gafa00eb1bff764a4ab723bb978b459297)。

`bt_mesh_rpr_scan_start` 的 `max_devs` 参数使用的特殊值。

<a id="r_ga83d18bb8d1108db9f7e54cd2cad32a99"></a>

```c
#define BT_MESH_MODEL_RPR_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_RPR_CLI](#ga83d18bb8d1108db9f7e54cd2cad32a99)。

远程配网客户端模型（Remote Provisioning Client Model）的组合数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga1cfef51b2d6389fb4b125cba4d21d739"></a>

```c
int bt_mesh_rpr_scan_caps_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_caps *caps)
```

相关声明：[bt_mesh_rpr_scan_caps_get](#ga1cfef51b2d6389fb4b125cba4d21d739)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的扫描能力。

<a id="r_ga03602b651a5bf1c88dac810e272ea142"></a>

```c
int bt_mesh_rpr_scan_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_get](#ga03602b651a5bf1c88dac810e272ea142)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的当前扫描状态。

<a id="r_gaf404922f2340442490f1ab29191f43e3"></a>

```c
int bt_mesh_rpr_scan_start (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint8_t timeout, uint8_t max_devs, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_start](#gaf404922f2340442490f1ab29191f43e3)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

开始扫描未配网设备（Unprovisioned Devices）。

<a id="r_ga934104e6ee33ba8c228fde4c68e752e1"></a>

```c
int bt_mesh_rpr_scan_start_ext (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint8_t timeout, const uint8_t *ad_types, size_t ad_count)
```

相关声明：[bt_mesh_rpr_scan_start_ext](#ga934104e6ee33ba8c228fde4c68e752e1)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

开始对未配网设备执行扩展扫描（Extended Scanning）。

<a id="r_ga007aa9b409d1370ed04c45efccdf0408"></a>

```c
int bt_mesh_rpr_scan_stop (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_stop](#ga007aa9b409d1370ed04c45efccdf0408)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

停止远程配网服务器（Remote Provisioning Server）上正在进行的所有扫描。

<a id="r_ga36de5bfca8ba9b03a99625fbc1734839"></a>

```c
int bt_mesh_rpr_link_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_link *rsp)
```

相关声明：[bt_mesh_rpr_link_get](#ga36de5bfca8ba9b03a99625fbc1734839)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的当前链路状态。

<a id="r_gaa240b465a1ed5796b190d241e484d467"></a>

```c
int bt_mesh_rpr_link_close (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_link *rsp)
```

相关声明：[bt_mesh_rpr_link_close](#gaa240b465a1ed5796b190d241e484d467)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)。

关闭远程配网服务器（Remote Provisioning Server）上任何已打开的链路。

<a id="r_ga93aca19586795801eefa04ffc4635533"></a>

```c
int32_t bt_mesh_rpr_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_rpr_cli_timeout_get](#ga93aca19586795801eefa04ffc4635533)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga5ad2a2f6f0b9a3f27ef8174cd15b8818"></a>

```c
void bt_mesh_rpr_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_rpr_cli_timeout_set](#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga83d18bb8d1108db9f7e54cd2cad32a99"></a>

### `BT_MESH_MODEL_RPR_CLI`

```c
#define BT_MESH_MODEL_RPR_CLI ( _cli)
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_REMOTE_PROV_CLI,                     \
                 _bt_mesh_rpr_cli_op, NULL, _cli, &_bt_mesh_rpr_cli_cb)
```

远程配网客户端模型（Remote Provisioning Client Model）的组合数据（Composition Data）条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_cli` | 指向远程配网客户端模型实例（Remote Provisioning Client Model Instance）的指针。 |

<a id="gafa00eb1bff764a4ab723bb978b459297"></a>

### `BT_MESH_RPR_SCAN_MAX_DEVS_ANY`

```c
#define BT_MESH_RPR_SCAN_MAX_DEVS_ANY 0
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

`bt_mesh_rpr_scan_start` 的 `max_devs` 参数使用的特殊值。

通知远程配网服务器（Remote Provisioning Server），不要限制向客户端报告的设备最大数量。

<a id="ga93aca19586795801eefa04ffc4635533"></a>

### `bt_mesh_rpr_cli_timeout_get()`

```c
int32_t bt_mesh_rpr_cli_timeout_get ( void )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

获取当前传输超时值（transmission timeout）。

**返回（Returns）**：返回值：配置的传输超时（transmission timeout），单位为毫秒。

<a id="ga5ad2a2f6f0b9a3f27ef8174cd15b8818"></a>

### `bt_mesh_rpr_cli_timeout_set()`

```c
void bt_mesh_rpr_cli_timeout_set ( int32_t timeout)
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

设置传输超时值（Transmission Timeout Value）。

传输超时（Transmission Timeout）控制远程配网客户端模型等待服务器响应的时长。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 新的传输超时。 |

<a id="gaa240b465a1ed5796b190d241e484d467"></a>

### `bt_mesh_rpr_link_close()`

```c
int bt_mesh_rpr_link_close ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, struct bt_mesh_rpr_link * rsp )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

关闭远程配网服务器（Remote Provisioning Server）上任何已打开的链路。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `rsp` | 链路状态响应缓冲区（Link Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga36de5bfca8ba9b03a99625fbc1734839"></a>

### `bt_mesh_rpr_link_get()`

```c
int bt_mesh_rpr_link_get ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, struct bt_mesh_rpr_link * rsp )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

获取远程配网服务器（Remote Provisioning Server）的当前链路状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `rsp` | 链路状态响应缓冲区（Link Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga1cfef51b2d6389fb4b125cba4d21d739"></a>

### `bt_mesh_rpr_scan_caps_get()`

```c
int bt_mesh_rpr_scan_caps_get ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, struct bt_mesh_rpr_caps * caps )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

获取远程配网服务器（Remote Provisioning Server）的扫描能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `caps` | 能力响应缓冲区（Capabilities Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga03602b651a5bf1c88dac810e272ea142"></a>

### `bt_mesh_rpr_scan_get()`

```c
int bt_mesh_rpr_scan_get ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, struct bt_mesh_rpr_scan_status * status )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

获取远程配网服务器（Remote Provisioning Server）的当前扫描状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `status` | 扫描状态响应缓冲区（Scan Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gaf404922f2340442490f1ab29191f43e3"></a>

### `bt_mesh_rpr_scan_start()`

```c
int bt_mesh_rpr_scan_start ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, const uint8_t uuid[16], uint8_t timeout, uint8_t max_devs, struct bt_mesh_rpr_scan_status * status )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

开始扫描未配网设备（Unprovisioned Devices）。

通知远程配网服务器（Remote Provisioning Server）开始扫描未配网设备（Unprovisioned Devices）。服务器通过 `bt_mesh_rpr_cli::scan_report` 回调报告结果。

使用 `uuid` 参数扫描特定设备；传入 `NULL` 则报告所有未配网设备（Unprovisioned Devices）。

服务器忽略重复设备，最多报告 `max_devs` 个设备。请求的 `max_devs` 超过服务器能力（Capability）时会出错。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `uuid` | 要扫描的设备 UUID；为 `NULL` 时报告全部设备。 |
| `timeout` | 扫描超时（Scan Timeout），单位为秒，至少为 1 秒。 |
| `max_devs` | 要报告的设备最大数量；为 0 时尽可能多地报告。 |
| `status` | 扫描状态响应缓冲区（Scan Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga934104e6ee33ba8c228fde4c68e752e1"></a>

### `bt_mesh_rpr_scan_start_ext()`

```c
int bt_mesh_rpr_scan_start_ext ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, const uint8_t uuid[16], uint8_t timeout, const uint8_t * ad_types, size_t ad_count )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

开始对未配网设备执行扩展扫描（Extended Scanning）。

扩展扫描（Extended Scanning）补充常规未配网扫描，允许服务器报告特定设备的更多数据。若支持，远程配网服务器会使用主动扫描（Active Scanning）向未配网设备请求扫描响应。若未提供 UUID，服务器会报告其自身带外信息（OOB Information）和广播数据的扫描结果。

使用 `ad_types` 数组指定扫描报告中要包含的广播数据类型（AD Types）。某些 AD 类型会触发特殊行为：

- `BT_DATA_NAME_COMPLETE`：会同时报告完整名称和缩短名称（Complete and Shortened Name）。
- `BT_DATA_URI`：若未配网信标（Unprovisioned Beacon）包含 URI 哈希，服务器会将扫描扩展到扫描响应以外的数据包，查找与该哈希匹配的统一资源标识符（URIs）。仅报告匹配的 URI。

不应使用以下广播数据类型（AD Types）：

- `BT_DATA_NAME_SHORTENED`：缩短名称（Shortened Name）。
- `BT_DATA_UUID16_SOME`：部分 16 位 UUID（Some 16-bit UUIDs）。
- `BT_DATA_UUID32_SOME`：部分 32 位 UUID（Some 32-bit UUIDs）。
- `BT_DATA_UUID128_SOME`：部分 128 位 UUID（Some 128-bit UUIDs）。

此外，每种广播数据类型（AD Type）只能出现一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `uuid` | 要开始扩展扫描的设备 UUID；为 `NULL` 时扫描远端服务器。 |
| `timeout` | 扫描超时（Scan Timeout），单位为秒。有效值范围为 `BT_MESH_RPR_EXT_SCAN_TIME_MIN` 至 `BT_MESH_RPR_EXT_SCAN_TIME_MAX`。UUID 为 `NULL` 时忽略。 |
| `ad_types` | 扫描报告中要包含的广播数据类型（AD Types）列表，必须包含 1 至 `CONFIG_BT_MESH_RPR_AD_TYPES_MAX` 个条目。 |
| `ad_count` | `ad_types` 中的广播数据类型数量。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga007aa9b409d1370ed04c45efccdf0408"></a>

### `bt_mesh_rpr_scan_stop()`

```c
int bt_mesh_rpr_scan_stop ( struct bt_mesh_rpr_cli * cli, const struct bt_mesh_rpr_node * srv, struct bt_mesh_rpr_scan_status * status )
```

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

停止远程配网服务器（Remote Provisioning Server）上正在进行的所有扫描。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli` | 远程配网客户端（Remote Provisioning Client）。 |
| `srv` | 远程配网服务器（Remote Provisioning Server）。 |
| `status` | 扫描状态响应缓冲区（Scan Status Response Buffer）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。


## 4.6\_原页交叉引用（Cross References）

- [rpr_cli.h](../api_file_network_device_reference/P031_zephyr__bluetooth__mesh__rpr_cli.h_文件参考.md)
- [bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)
- [bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_REMOTE_PROV_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#gaf373eb4d8af5d6bee76a821bd4d5e48c)
- [远程配网客户端模型（Remote Provisioning Client model）](P004_远程配网客户端模型（Remote Provisioning Client model）.md)
- [bt_mesh_rpr_cli::scan_report](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a32b3c63218b506d1bc5759640cb3fb81)
- [BT_DATA_NAME_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab94a7c5689d296acf47f976538056ab5)
- [BT_DATA_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3c6a5903cc4a46aaf0b30a0de0179403)
- [`BT_DATA_NAME_SHORTENED`：缩短名称（Shortened Name）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc509b33a8d2dd9124f6893eadbe1662)
- [`BT_DATA_UUID16_SOME`：部分 16 位 UUID（Some 16-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6c725bd3d31c159a4d046561dbca38ba)
- [`BT_DATA_UUID32_SOME`：部分 32 位 UUID（Some 32-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2486a6748490ba57e442ca15223482ef)
- [`BT_DATA_UUID128_SOME`：部分 128 位 UUID（Some 128-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5c4f7fc1b93c611e95f735330fba243b)
- [BT_MESH_RPR_EXT_SCAN_TIME_MIN](../api_protocol_topic_reference/P007_远程配网模型（Remote Provisioning models）.md#ga2b7e2636da150f5c5cb4e3bdee13c745)
- [BT_MESH_RPR_EXT_SCAN_TIME_MAX](../api_protocol_topic_reference/P007_远程配网模型（Remote Provisioning models）.md#ga2a5241b2e87fec227740dd4f2de3a68a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_gaf373eb4d8af5d6bee76a821bd4d5e48c"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_消息服务器设备（Messaging Server Equipment，MSE）的 OBEX 客户端.md) · [返回大纲](大纲.md) · [下一章](P005_已发布音频能力服务（Published Audio Capabilities Service，PACS）.md)
