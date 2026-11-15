---
id: learning.zephyr-docs.api-file-network-device-reference.page-31
title: zephyr__bluetooth__mesh__rpr_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_bluetooth\_\_mesh\_\_rpr\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh远程配网客户端（Remote Provisioning Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/rpr.h>
```

查看此文件的源码。

蓝牙Mesh远程配网客户端（Remote Provisioning Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 31.1\_数据结构（Data Structures）

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

## 31.2\_宏定义（Macros）

<a id="r_gafa00eb1bff764a4ab723bb978b459297"></a>

```c
#define BT_MESH_RPR_SCAN_MAX_DEVS_ANY 0
```

相关声明：[BT_MESH_RPR_SCAN_MAX_DEVS_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gafa00eb1bff764a4ab723bb978b459297)。

`bt_mesh_rpr_scan_start` 的 `max_devs` 参数使用的特殊值。

<a id="r_ga83d18bb8d1108db9f7e54cd2cad32a99"></a>

```c
#define BT_MESH_MODEL_RPR_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_RPR_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga83d18bb8d1108db9f7e54cd2cad32a99)。

远程配网客户端模型（Remote Provisioning Client Model）的组合数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 31.3\_函数（Functions）

<a id="r_ga1cfef51b2d6389fb4b125cba4d21d739"></a>

```c
int bt_mesh_rpr_scan_caps_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_caps *caps)
```

相关声明：[bt_mesh_rpr_scan_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga1cfef51b2d6389fb4b125cba4d21d739)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的扫描能力。

<a id="r_ga03602b651a5bf1c88dac810e272ea142"></a>

```c
int bt_mesh_rpr_scan_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga03602b651a5bf1c88dac810e272ea142)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的当前扫描状态。

<a id="r_gaf404922f2340442490f1ab29191f43e3"></a>

```c
int bt_mesh_rpr_scan_start (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint8_t timeout, uint8_t max_devs, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaf404922f2340442490f1ab29191f43e3)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

开始扫描未配网设备（Unprovisioned Devices）。

<a id="r_ga934104e6ee33ba8c228fde4c68e752e1"></a>

```c
int bt_mesh_rpr_scan_start_ext (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, const uint8_t uuid[16], uint8_t timeout, const uint8_t *ad_types, size_t ad_count)
```

相关声明：[bt_mesh_rpr_scan_start_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga934104e6ee33ba8c228fde4c68e752e1)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

开始对未配网设备执行扩展扫描（Extended Scanning）。

<a id="r_ga007aa9b409d1370ed04c45efccdf0408"></a>

```c
int bt_mesh_rpr_scan_stop (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_scan_status *status)
```

相关声明：[bt_mesh_rpr_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga007aa9b409d1370ed04c45efccdf0408)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)。

停止远程配网服务器（Remote Provisioning Server）上正在进行的所有扫描。

<a id="r_ga36de5bfca8ba9b03a99625fbc1734839"></a>

```c
int bt_mesh_rpr_link_get (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_link *rsp)
```

相关声明：[bt_mesh_rpr_link_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga36de5bfca8ba9b03a99625fbc1734839)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)。

获取远程配网服务器（Remote Provisioning Server）的当前链路状态。

<a id="r_gaa240b465a1ed5796b190d241e484d467"></a>

```c
int bt_mesh_rpr_link_close (struct bt_mesh_rpr_cli *cli, const struct bt_mesh_rpr_node *srv, struct bt_mesh_rpr_link *rsp)
```

相关声明：[bt_mesh_rpr_link_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaa240b465a1ed5796b190d241e484d467)、[bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)、[bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)、[bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)。

关闭远程配网服务器（Remote Provisioning Server）上任何已打开的链路。

<a id="r_ga93aca19586795801eefa04ffc4635533"></a>

```c
int32_t bt_mesh_rpr_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_rpr_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga93aca19586795801eefa04ffc4635533)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga5ad2a2f6f0b9a3f27ef8174cd15b8818"></a>

```c
void bt_mesh_rpr_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_rpr_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 31.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/bluetooth/mesh/access.h](../api_source_compiler_device_reference/P001_access.h_源码浏览.md)
- [zephyr/bluetooth/mesh/rpr.h](../api_source_reference/P731_rpr.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P169_rpr_cli.h_源码浏览.md)
- [bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)
- [bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [BT_MESH_RPR_SCAN_MAX_DEVS_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gafa00eb1bff764a4ab723bb978b459297)
- [bt_mesh_rpr_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaf404922f2340442490f1ab29191f43e3)
- [BT_MESH_MODEL_RPR_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga83d18bb8d1108db9f7e54cd2cad32a99)
- [bt_mesh_rpr_scan_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga1cfef51b2d6389fb4b125cba4d21d739)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [bt_mesh_rpr_scan_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga03602b651a5bf1c88dac810e272ea142)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_rpr_scan_start_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga934104e6ee33ba8c228fde4c68e752e1)
- [bt_mesh_rpr_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga007aa9b409d1370ed04c45efccdf0408)
- [bt_mesh_rpr_link_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga36de5bfca8ba9b03a99625fbc1734839)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [bt_mesh_rpr_link_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaa240b465a1ed5796b190d241e484d467)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_rpr_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga93aca19586795801eefa04ffc4635533)
- [bt_mesh_rpr_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)

<a id="header-details"></a>

---

[上一章](P030_zephyr__dt-bindings__power__rpi_bcm283x_power.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__dt-bindings__interrupt-controller__rts5817_intc.h_文件参考.md)
