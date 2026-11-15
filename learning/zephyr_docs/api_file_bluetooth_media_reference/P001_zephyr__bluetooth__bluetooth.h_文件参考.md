---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-1
title: zephyr__bluetooth__bluetooth.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_bluetooth.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙子系统（Bluetooth Subsystem）的核心API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <string.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/crypto.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/bluetooth/classic/classic.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

蓝牙子系统（Bluetooth Subsystem）的核心API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fle_5Fext_5Fadv_5Fsent_5Finfo"></a>

```c
struct bt_le_ext_adv_sent_info
```

相关声明：[bt_le_ext_adv_sent_info](../bluetooth_connection_model_reference/P107_bt_le_ext_adv_sent_info_结构体.md)。

广播发送事件（Advertising Sent Event）的信息。

<a id="r_bt_5Fle_5Fext_5Fadv_5Fconnected_5Finfo"></a>

```c
struct bt_le_ext_adv_connected_info
```

相关声明：[bt_le_ext_adv_connected_info](../bluetooth_connection_model_reference/P104_bt_le_ext_adv_connected_info_结构体.md)。

广播连接事件（Advertising Connected Event）的信息。

<a id="r_bt_5Fle_5Fext_5Fadv_5Fscanned_5Finfo"></a>

```c
struct bt_le_ext_adv_scanned_info
```

相关声明：[bt_le_ext_adv_scanned_info](../bluetooth_connection_model_reference/P106_bt_le_ext_adv_scanned_info_结构体.md)。

广播被扫描事件（Advertising Scanned Event）的信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fdata_5Frequest"></a>

```c
struct bt_le_per_adv_data_request
```

相关声明：[bt_le_per_adv_data_request](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md)。

带响应的周期广播（PAwR）子事件信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fresponse_5Finfo"></a>

```c
struct bt_le_per_adv_response_info
```

相关声明：[bt_le_per_adv_response_info](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md)。

已接收的带响应周期广播（PAwR）响应的信息。

<a id="r_bt_5Fle_5Fext_5Fadv_5Fcb"></a>

```c
struct bt_le_ext_adv_cb
```

相关声明：[bt_le_ext_adv_cb](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md)。

用于通知广播者（Advertiser）活动的回调结构。

<a id="r_bt_5Fle_5Flocal_5Ffeatures"></a>

```c
struct bt_le_local_features
```

相关声明：[bt_le_local_features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md)。

本地低功耗蓝牙控制器（Bluetooth LE Controller）的特性与能力。

<a id="r_bt_5Fle_5Fadv_5Fparam"></a>

```c
struct bt_le_adv_param
```

相关声明：[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)。

低功耗蓝牙广播（LE Advertising）的参数。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fparam"></a>

```c
struct bt_le_per_adv_param
```

相关声明：[bt_le_per_adv_param](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md)。

配置周期广播（Periodic Advertising）的参数。

<a id="r_bt_5Fle_5Fext_5Fadv_5Fstart_5Fparam"></a>

```c
struct bt_le_ext_adv_start_param
```

相关声明：[bt_le_ext_adv_start_param](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md)。

启动扩展广播会话（Extended Advertising Session）的参数。

<a id="r_bt_5Fle_5Fext_5Fadv_5Finfo"></a>

```c
struct bt_le_ext_adv_info
```

相关声明：[bt_le_ext_adv_info](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md)。

广播集（Advertising Set）的信息结构。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsubevent_5Fdata_5Fparams"></a>

```c
struct bt_le_per_adv_subevent_data_params
```

相关声明：[bt_le_per_adv_subevent_data_params](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md)。

为特定带响应周期广播（PAwR）子事件设置数据的参数。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fsynced_5Finfo"></a>

```c
struct bt_le_per_adv_sync_synced_info
```

相关声明：[bt_le_per_adv_sync_synced_info](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md)。

与周期广播（Periodic Advertising）成功同步的信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fterm_5Finfo"></a>

```c
struct bt_le_per_adv_sync_term_info
```

相关声明：[bt_le_per_adv_sync_term_info](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md)。

周期广播同步（Periodic Advertising Sync）终止的信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Frecv_5Finfo"></a>

```c
struct bt_le_per_adv_sync_recv_info
```

相关声明：[bt_le_per_adv_sync_recv_info](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md)。

已接收的周期广播报告（Periodic Advertising Report）的信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fstate_5Finfo"></a>

```c
struct bt_le_per_adv_sync_state_info
```

相关声明：[bt_le_per_adv_sync_state_info](../bluetooth_connection_model_reference/P122_bt_le_per_adv_sync_state_info_结构体.md)。

周期广播同步（Periodic Advertising Sync）状态的信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fcb"></a>

```c
struct bt_le_per_adv_sync_cb
```

相关声明：[bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)。

周期广播同步（Periodic Advertising Sync）事件的回调结构。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fparam"></a>

```c
struct bt_le_per_adv_sync_param
```

相关声明：[bt_le_per_adv_sync_param](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md)。

创建周期广播同步（Periodic Advertising Sync）对象的参数。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Finfo"></a>

```c
struct bt_le_per_adv_sync_info
```

相关声明：[bt_le_per_adv_sync_info](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md)。

周期广播集（Periodic Advertising Set）的信息结构。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Ftransfer_5Fparam"></a>

```c
struct bt_le_per_adv_sync_transfer_param
```

相关声明：[bt_le_per_adv_sync_transfer_param](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md)。

周期广播同步传递（Periodic Advertising Sync Transfer）的参数。

<a id="r_bt_5Fle_5Fscan_5Fparam"></a>

```c
struct bt_le_scan_param
```

相关声明：[bt_le_scan_param](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md)。

低功耗蓝牙（LE）的扫描参数。

<a id="r_bt_5Fle_5Fscan_5Frecv_5Finfo"></a>

```c
struct bt_le_scan_recv_info
```

相关声明：[bt_le_scan_recv_info](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md)。

低功耗蓝牙（LE）广播包与扫描响应包的信息。

<a id="r_bt_5Fle_5Fscan_5Fcb"></a>

```c
struct bt_le_scan_cb
```

相关声明：[bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)。

低功耗蓝牙（LE）扫描的监听器上下文（Listener Context）。

<a id="r_bt_5Fle_5Foob_5Fsc_5Fdata"></a>

```c
struct bt_le_oob_sc_data
```

相关声明：[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)。

低功耗蓝牙安全连接（LE Secure Connections）配对使用的带外（Out of Band，OOB）数据。

<a id="r_bt_5Fle_5Foob"></a>

```c
struct bt_le_oob
```

相关声明：[bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)。

低功耗蓝牙带外（LE Out of Band，OOB）信息。

<a id="r_bt_5Fbond_5Finfo"></a>

```c
struct bt_bond_info
```

相关声明：[bt_bond_info](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md)。

与远端设备的绑定（Bond）信息。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync_5Fsubevent_5Fparams"></a>

```c
struct bt_le_per_adv_sync_subevent_params
```

相关声明：[bt_le_per_adv_sync_subevent_params](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md)。

与特定周期广播子事件（Periodic Advertising Subevent）同步的参数。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fresponse_5Fparams"></a>

```c
struct bt_le_per_adv_response_params
```

相关声明：[bt_le_per_adv_response_params](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md)。

发送周期广播响应（Periodic Advertising Response）的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gaded4b52c9bb87fd4d19b1eb9361973e5"></a>

```c
#define BT_ID_DEFAULT 0
```

相关声明：[BT_ID_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaded4b52c9bb87fd4d19b1eb9361973e5)。

引用第一个身份地址（Identity Address）的身份句柄（Identity Handle）。

<a id="r_ga17419cd0fcc4660f09ac5dbad3a042f2"></a>

```c
#define BT_IRK_SIZE 16U
```

相关声明：[BT_IRK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga17419cd0fcc4660f09ac5dbad3a042f2)。

身份解析密钥（Identity Resolving Key）的大小，单位为八位字节。

<a id="r_gaa26f90b188caa50ca12247b7911a0a5f"></a>

```c
#define BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE
```

相关声明：[BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa26f90b188caa50ca12247b7911a0a5f)、[BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a81b4b9ce53511c62889790a79b0f6a34)。

本地支持特性（Local Supported Features）的八位字节数。

<a id="r_ga71555b857cf8c2a47c36e4dafa7accf4"></a>

```c
#define BT_LE_ADV_PARAM_INIT(_options, _int_min, _int_max, _peer)
```

相关声明：[BT_LE_ADV_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga71555b857cf8c2a47c36e4dafa7accf4)。

初始化广播参数（Advertising Parameters）。

<a id="r_ga9557269dd36b624b49e76c511c3a0cc1"></a>

```c
#define BT_LE_ADV_PARAM(_options, _int_min, _int_max, _peer)
```

相关声明：[BT_LE_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9557269dd36b624b49e76c511c3a0cc1)。

用于内联声明广播参数（Advertising Parameters）的辅助宏。

<a id="r_ga1f5edc3c4cbead62e32cef8cc7b83725"></a>

```c
#define BT_LE_ADV_CONN_DIR(_peer)
```

相关声明：[BT_LE_ADV_CONN_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1f5edc3c4cbead62e32cef8cc7b83725)。

<a id="r_gaa700527b1caf3bef27d96a3f91a29f69"></a>

```c
#define BT_LE_ADV_CONN_FAST_1
```

相关声明：[BT_LE_ADV_CONN_FAST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa700527b1caf3bef27d96a3f91a29f69)。

通用访问配置文件（GAP）推荐的、由使用者发起的可连接广播参数（Connectable Advertising Parameters）。

<a id="r_ga684a1110a8973bc17211f6f0824beccd"></a>

```c
#define BT_LE_ADV_CONN_FAST_2
```

相关声明：[BT_LE_ADV_CONN_FAST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga684a1110a8973bc17211f6f0824beccd)。

GAP 推荐的可连接广播参数，用于不可连接广播事件（Non-connectable Advertising Events）。（原文同时使用 connectable 与 non-connectable，保留其表述。）

<a id="r_gab89e033ed3fd116c94120d177dfdc839"></a>

```c
#define BT_LE_ADV_CONN_DIR_LOW_DUTY(_peer)
```

相关声明：[BT_LE_ADV_CONN_DIR_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab89e033ed3fd116c94120d177dfdc839)。

<a id="r_ga1610555bf59f1d691d640f245957fdce"></a>

```c
#define BT_LE_ADV_NCONN
```

相关声明：[BT_LE_ADV_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1610555bf59f1d691d640f245957fdce)。

使用私有地址（Private Address）的不可连接广播（Non-connectable Advertising）。

<a id="r_ga6ef9fb7a469b03265c7adc99ea19a11b"></a>

```c
#define BT_LE_ADV_NCONN_IDENTITY
```

相关声明：[BT_LE_ADV_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6ef9fb7a469b03265c7adc99ea19a11b)。

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接广播（Non-connectable Advertising）。

<a id="r_gaeaaef4dede5d45251dfe12f329e070b7"></a>

```c
#define BT_LE_EXT_ADV_CONN
```

相关声明：[BT_LE_EXT_ADV_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaeaaef4dede5d45251dfe12f329e070b7)。

可连接的扩展广播（Connectable Extended Advertising）。

<a id="r_ga5dd57fc7f0e213db08655e631a2f314e"></a>

```c
#define BT_LE_EXT_ADV_SCAN
```

相关声明：[BT_LE_EXT_ADV_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5dd57fc7f0e213db08655e631a2f314e)。

可扫描的扩展广播（Scannable Extended Advertising）。

<a id="r_gaabc0385f6a5307b48ec43af6aae7dea6"></a>

```c
#define BT_LE_EXT_ADV_NCONN
```

相关声明：[BT_LE_EXT_ADV_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaabc0385f6a5307b48ec43af6aae7dea6)。

使用私有地址（Private Address）的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_ga7e46a64af0036c433c2e940ce7db0a05"></a>

```c
#define BT_LE_EXT_ADV_NCONN_IDENTITY
```

相关声明：[BT_LE_EXT_ADV_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7e46a64af0036c433c2e940ce7db0a05)。

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_ga0e911d3aafdd0c926590b3272a3da564"></a>

```c
#define BT_LE_EXT_ADV_CODED_NCONN
```

相关声明：[BT_LE_EXT_ADV_CODED_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0e911d3aafdd0c926590b3272a3da564)。

在编码物理层（Coded PHY）上使用私有地址的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_gac67c52693154ebbeedbb31e100513812"></a>

```c
#define BT_LE_EXT_ADV_CODED_NCONN_IDENTITY
```

相关声明：[BT_LE_EXT_ADV_CODED_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac67c52693154ebbeedbb31e100513812)。

在编码物理层（Coded PHY）上使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_gaf0d4c5b05deb5466a0e29c153263b489"></a>

```c
#define BT_LE_EXT_ADV_START_PARAM_INIT(_timeout, _n_evts)
```

相关声明：[BT_LE_EXT_ADV_START_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0d4c5b05deb5466a0e29c153263b489)。

用于内联初始化扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

<a id="r_ga9b2cefbcb0a85116cadb68f6d80c6429"></a>

```c
#define BT_LE_EXT_ADV_START_PARAM(_timeout, _n_evts)
```

相关声明：[BT_LE_EXT_ADV_START_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9b2cefbcb0a85116cadb68f6d80c6429)。

用于内联声明扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

<a id="r_ga8c83a6f322a479bc24a576a7f091312e"></a>

```c
#define BT_LE_EXT_ADV_START_DEFAULT BT_LE_EXT_ADV_START_PARAM(0, 0)
```

相关声明：[BT_LE_EXT_ADV_START_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8c83a6f322a479bc24a576a7f091312e)、[BT_LE_EXT_ADV_START_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9b2cefbcb0a85116cadb68f6d80c6429)。

<a id="r_ga880567278a81098ae55f52f624c61041"></a>

```c
#define BT_LE_PER_ADV_PARAM_INIT(_int_min, _int_max, _options)
```

相关声明：[BT_LE_PER_ADV_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga880567278a81098ae55f52f624c61041)。

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

<a id="r_gaf46e54f8fcda7b65b659685bb225d243"></a>

```c
#define BT_LE_PER_ADV_PARAM(_int_min, _int_max, _options)
```

相关声明：[BT_LE_PER_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf46e54f8fcda7b65b659685bb225d243)。

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

<a id="r_ga8f6a00faaaab2a91ac943c71ed041ac1"></a>

```c
#define BT_LE_PER_ADV_DEFAULT
```

相关声明：[BT_LE_PER_ADV_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8f6a00faaaab2a91ac943c71ed041ac1)。

<a id="r_gac9f372ca16afb1c2f0e100c5b1b94cd5"></a>

```c
#define BT_LE_SCAN_PARAM_INIT(_type, _options, _interval, _window)
```

相关声明：[BT_LE_SCAN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac9f372ca16afb1c2f0e100c5b1b94cd5)。

初始化扫描参数（Scan Parameters）。

<a id="r_ga57ace75133343ba8de7fa965f452ee3d"></a>

```c
#define BT_LE_SCAN_PARAM(_type, _options, _interval, _window)
```

相关声明：[BT_LE_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga57ace75133343ba8de7fa965f452ee3d)。

用于内联声明扫描参数（Scan Parameters）的辅助宏。

<a id="r_gac137ea4ce32697582a337116ffa41da5"></a>

```c
#define BT_LE_SCAN_ACTIVE
```

相关声明：[BT_LE_SCAN_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac137ea4ce32697582a337116ffa41da5)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

<a id="r_ga9bd9701db0459c066ed7c18343f60911"></a>

```c
#define BT_LE_SCAN_ACTIVE_CONTINUOUS
```

相关声明：[BT_LE_SCAN_ACTIVE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9bd9701db0459c066ed7c18343f60911)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏，其中 window == interval。

<a id="r_ga8ceaef6f0fbf4fe2d76d47e8f59aeb11"></a>

```c
#define BT_LE_SCAN_PASSIVE
```

相关声明：[BT_LE_SCAN_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

<a id="r_ga8d8ccc9ea1db2c96deae1603ec1c78a3"></a>

```c
#define BT_LE_SCAN_PASSIVE_CONTINUOUS
```

相关声明：[BT_LE_SCAN_PASSIVE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8d8ccc9ea1db2c96deae1603ec1c78a3)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏，其中 window == interval。

<a id="r_ga06380c4ae6289c704a143b9d192bc35f"></a>

```c
#define BT_LE_SCAN_CODED_ACTIVE
```

相关声明：[BT_LE_SCAN_CODED_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga06380c4ae6289c704a143b9d192bc35f)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

<a id="r_ga1e5a4589304babc6b0d49019ebcff6b0"></a>

```c
#define BT_LE_SCAN_CODED_PASSIVE
```

相关声明：[BT_LE_SCAN_CODED_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1e5a4589304babc6b0d49019ebcff6b0)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga5398783ab4a5dc854b18e37fb10774eb"></a>

```c
typedef void(* bt_ready_cb_t) (int err)
```

相关声明：[bt_ready_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5398783ab4a5dc854b18e37fb10774eb)。

通知蓝牙（Bluetooth）已启用的回调。

<a id="r_ga1c53d22b6e2dee38c825c58f3eeee9b4"></a>

```c
typedef void bt_le_scan_cb_t(const bt_addr_le_t *addr, int8_t rssi, uint8_t adv_type, struct net_buf_simple *buf)
```

相关声明：[bt_le_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c53d22b6e2dee38c825c58f3eeee9b4)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

报告低功耗蓝牙（LE）扫描结果的回调类型（Callback Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_gafbf81dab68b0e484d4742471c722fc28"></a>

```c
enum bt_le_adv_opt { BT_LE_ADV_OPT_NONE = 0 , BT_LE_ADV_OPT_CONN = (1UL << (0)) | (1UL << (1)) , BT_LE_ADV_OPT_USE_IDENTITY = (1UL << (2)) , BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY = (1UL << (4)) , BT_LE_ADV_OPT_DIR_ADDR_RPA = (1UL << (5)) , BT_LE_ADV_OPT_FILTER_SCAN_REQ = (1UL << (6)) , BT_LE_ADV_OPT_FILTER_CONN = (1UL << (7)) , BT_LE_ADV_OPT_NOTIFY_SCAN_REQ = (1UL << (8)) , BT_LE_ADV_OPT_SCANNABLE = (1UL << (9)) , BT_LE_ADV_OPT_EXT_ADV = (1UL << (10)) , BT_LE_ADV_OPT_NO_2M = (1UL << (11)) , BT_LE_ADV_OPT_CODED = (1UL << (12)) , BT_LE_ADV_OPT_ANONYMOUS = (1UL << (13)) , BT_LE_ADV_OPT_USE_TX_POWER = (1UL << (14)) , BT_LE_ADV_OPT_DISABLE_CHAN_37 = (1UL << (15)) , BT_LE_ADV_OPT_DISABLE_CHAN_38 = (1UL << (16)) , BT_LE_ADV_OPT_DISABLE_CHAN_39 = (1UL << (17)) , BT_LE_ADV_OPT_USE_NRPA = (1UL << (19)) , BT_LE_ADV_OPT_REQUIRE_S2_CODING = (1UL << (20)) , BT_LE_ADV_OPT_REQUIRE_S8_CODING = (1UL << (21)) , BT_LE_ADV_OPT_TX_POWER = (1UL << (22)) }
```

相关声明：[bt_le_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafbf81dab68b0e484d4742471c722fc28)、[BT_LE_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf)、[BT_LE_ADV_OPT_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)、[BT_LE_ADV_OPT_USE_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e)、[BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)、[BT_LE_ADV_OPT_DIR_ADDR_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)、[BT_LE_ADV_OPT_FILTER_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5)、[BT_LE_ADV_OPT_FILTER_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf)、[BT_LE_ADV_OPT_NOTIFY_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b)、[BT_LE_ADV_OPT_SCANNABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9)、[BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)、[BT_LE_ADV_OPT_NO_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b)、[BT_LE_ADV_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1)、[BT_LE_ADV_OPT_ANONYMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab)、[BT_LE_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859)、[BT_LE_ADV_OPT_DISABLE_CHAN_37](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779)、[BT_LE_ADV_OPT_DISABLE_CHAN_38](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275)、[BT_LE_ADV_OPT_DISABLE_CHAN_39](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28)、[BT_LE_ADV_OPT_USE_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e)、[BT_LE_ADV_OPT_REQUIRE_S2_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e)、[BT_LE_ADV_OPT_REQUIRE_S8_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8)、[BT_LE_ADV_OPT_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)。

广播选项（Advertising Options）。

<a id="r_gae60a45dde6b4d9f4c54a2a6070254f11"></a>

```c
enum bt_le_per_adv_opt { BT_LE_PER_ADV_OPT_NONE = 0 , BT_LE_PER_ADV_OPT_USE_TX_POWER = (1UL << (1)) , BT_LE_PER_ADV_OPT_INCLUDE_ADI = (1UL << (2)) }
```

相关声明：[bt_le_per_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae60a45dde6b4d9f4c54a2a6070254f11)、[BT_LE_PER_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)、[BT_LE_PER_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f)、[BT_LE_PER_ADV_OPT_INCLUDE_ADI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403)。

周期性广播选项（Periodic Advertising Options）。

<a id="r_ga544ccde35638d8f580942d830fe9f242"></a>

```c
enum bt_le_ext_adv_state { BT_LE_EXT_ADV_STATE_DISABLED , BT_LE_EXT_ADV_STATE_ENABLED }
```

相关声明：[bt_le_ext_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga544ccde35638d8f580942d830fe9f242)、[BT_LE_EXT_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d)、[BT_LE_EXT_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07)。

广播状态（Advertising States）。

<a id="r_ga6bb77c0808c761753650cde28ddb013e"></a>

```c
enum bt_le_per_adv_state { BT_LE_PER_ADV_STATE_NONE , BT_LE_PER_ADV_STATE_DISABLED , BT_LE_PER_ADV_STATE_ENABLED }
```

相关声明：[bt_le_per_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bb77c0808c761753650cde28ddb013e)、[BT_LE_PER_ADV_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c)、[BT_LE_PER_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b)、[BT_LE_PER_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3)。

周期性广播状态（Periodic Advertising States）。

<a id="r_gac942d7e3cae8fca22080f93bf9528ee9"></a>

```c
enum bt_le_per_adv_sync_opt { BT_LE_PER_ADV_SYNC_OPT_NONE = 0 , BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST = (1UL << (0)) , BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED = (1UL << (1)) , BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE = (1UL << (2)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA = (1UL << (3)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US = (1UL << (4)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US = (1UL << (5)) , BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT = (1UL << (6)) }
```

相关声明：[bt_le_per_adv_sync_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac942d7e3cae8fca22080f93bf9528ee9)、[BT_LE_PER_ADV_SYNC_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c)、[BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)、[BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53)、[BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e)、[BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320)。

周期性广播同步选项（Periodic Advertising Sync Options）。

<a id="r_ga820c5f3721e72662e558cc4576b6111b"></a>

```c
enum bt_le_per_adv_sync_transfer_opt { BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE = 0 , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA = (1UL << (0)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US = (1UL << (1)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US = (1UL << (2)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE = (1UL << (3)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED = (1UL << (4)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES = (1UL << (5)) }
```

相关声明：[bt_le_per_adv_sync_transfer_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga820c5f3721e72662e558cc4576b6111b)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c)。

周期性广播同步传输选项（Periodic Advertising Sync Transfer Options）。

<a id="r_gab4b5773898e2a1eef21557915a21c996"></a>

```c
enum bt_le_scan_opt { BT_LE_SCAN_OPT_NONE = 0 , BT_LE_SCAN_OPT_FILTER_DUPLICATE = (1UL << (0)) , BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST = (1UL << (1)) , BT_LE_SCAN_OPT_CODED = (1UL << (2)) , BT_LE_SCAN_OPT_NO_1M = (1UL << (3)) , BT_LE_SCAN_OPT_EXT_FILTER_POLICY = (1UL << (4)) }
```

相关声明：[bt_le_scan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab4b5773898e2a1eef21557915a21c996)、[BT_LE_SCAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185)、[BT_LE_SCAN_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394)、[BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae)、[BT_LE_SCAN_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb)、[BT_LE_SCAN_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6)、[BT_LE_SCAN_OPT_EXT_FILTER_POLICY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d)。

<a id="r_gaf980473379afa477c09e19912d40d29e"></a>

```c
enum bt_le_scan_type { BT_LE_SCAN_TYPE_PASSIVE = 0x00 , BT_LE_SCAN_TYPE_ACTIVE = 0x01 }
```

相关声明：[bt_le_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf980473379afa477c09e19912d40d29e)、[BT_LE_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)、[BT_LE_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)。

<a id="r_gaad0039d4b524a0eef31158dc9b24a497"></a>

```c
enum bt_le_addr_res_support { BT_LE_ADDR_RES_SUPPORT_UNKNOWN , BT_LE_ADDR_RES_SUPPORT_NO , BT_LE_ADDR_RES_SUPPORT_YES }
```

相关声明：[bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)、[BT_LE_ADDR_RES_SUPPORT_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9)、[BT_LE_ADDR_RES_SUPPORT_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab)、[BT_LE_ADDR_RES_SUPPORT_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c)。

已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_gac45d16bfe21c3c38e834c293e5ebc42b"></a>

```c
int bt_enable (bt_ready_cb_t cb)
```

相关声明：[bt_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)、[bt_ready_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5398783ab4a5dc854b18e37fb10774eb)。

启用蓝牙（Bluetooth）。

<a id="r_ga0a58e5a050170e84a80f8d5bb3516ec7"></a>

```c
int bt_disable (void)
```

相关声明：[bt_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0a58e5a050170e84a80f8d5bb3516ec7)。

禁用蓝牙（Bluetooth）。

<a id="r_gaa8bf6854e7ad1fe7e0805737576e5d1a"></a>

```c
bool bt_is_ready (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa8bf6854e7ad1fe7e0805737576e5d1a)。

检查蓝牙（Bluetooth）是否就绪。

<a id="r_gac8bb3609a3d6da69ff736809e45f5c8a"></a>

```c
int bt_set_name (const char *name)
```

相关声明：[bt_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac8bb3609a3d6da69ff736809e45f5c8a)。

设置蓝牙设备名称（Bluetooth Device Name）。

<a id="r_gad922d894b25e86de3f81ce77200a13fd"></a>

```c
const char * bt_get_name (void)
```

相关声明：[bt_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad922d894b25e86de3f81ce77200a13fd)。

获取蓝牙设备名称（Bluetooth Device Name）。

<a id="r_ga35b76ea7ce79721e47ca4164e08b2dfb"></a>

```c
uint16_t bt_get_appearance (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_get_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga35b76ea7ce79721e47ca4164e08b2dfb)。

获取本地蓝牙外观值（Bluetooth Appearance）。

<a id="r_gaf0729453790aab1bd3d52c623be3b35a"></a>

```c
int bt_set_appearance (uint16_t new_appearance)
```

相关声明：[bt_set_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0729453790aab1bd3d52c623be3b35a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置本地蓝牙外观值（Bluetooth Appearance）。

<a id="r_ga06d0ae35cbf4382679cc3cfe612cee4d"></a>

```c
void bt_id_get (bt_addr_le_t *addrs, size_t *count)
```

相关声明：[bt_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga06d0ae35cbf4382679cc3cfe612cee4d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

获取当前配置的身份地址（Identity Addresses）。

<a id="r_gae11eb8ad254418c38a0e8689df25a159"></a>

```c
int bt_id_create (bt_addr_le_t *addr, uint8_t *irk)
```

相关声明：[bt_id_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae11eb8ad254418c38a0e8689df25a159)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建新的身份地址（Identity Address）。

<a id="r_gabb3353edc8a3a8d29a0370049b20cbe4"></a>

```c
int bt_id_reset (uint8_t id, bt_addr_le_t *addr, uint8_t *irk)
```

相关声明：[bt_id_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabb3353edc8a3a8d29a0370049b20cbe4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

重置／回收身份地址（Identity Address）以供重用。

<a id="r_gaf6cd906690a51ebed04bea4f4ef716ff"></a>

```c
int bt_id_delete (uint8_t id)
```

相关声明：[bt_id_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf6cd906690a51ebed04bea4f4ef716ff)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除身份地址（Identity Address）。

<a id="r_ga7a595421c232b15ad96b52f0300fd960"></a>

```c
int bt_id_reset_irk (uint8_t id, uint8_t *irk)
```

相关声明：[bt_id_reset_irk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a595421c232b15ad96b52f0300fd960)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

重置某个身份的本地身份解析密钥（Identity Resolving Key，IRK）。

<a id="r_ga650faa2a86f54499f4bc5a8657a55a87"></a>

```c
int bt_le_get_local_features (struct bt_le_local_features *local_features)
```

相关声明：[bt_le_get_local_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga650faa2a86f54499f4bc5a8657a55a87)、[bt_le_local_features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md)。

获取本地低功耗蓝牙控制器特性（Bluetooth LE Controller Features）。

<a id="r_ga453074db3964f1b57b92ac7afb0b4fac"></a>

```c
static void bt_le_adv_param_set_tx_power (struct bt_le_adv_param *param, int8_t tx_power)
```

相关声明：[bt_le_adv_param_set_tx_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga453074db3964f1b57b92ac7afb0b4fac)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置广播参数结构体（Advertising Parameter Struct）中的发射功率（TX Power）。

<a id="r_gad2e3caef88d52d720e8e4d21df767b02"></a>

```c
int bt_le_adv_start (const struct bt_le_adv_param *param, const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

启动广播（Advertising）。

<a id="r_ga9a406ebfefac3dd09935a4ae0e317817"></a>

```c
int bt_le_adv_update_data (const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_adv_update_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9a406ebfefac3dd09935a4ae0e317817)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

更新广播（Advertising）。

<a id="r_ga1776e310b9d80898e6b32d50c4fe0b49"></a>

```c
int bt_le_adv_stop (void)
```

相关声明：[bt_le_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1776e310b9d80898e6b32d50c4fe0b49)。

停止广播（Advertising）。

<a id="r_gad02b855dd7a26e3910b247fa73f19297"></a>

```c
int bt_le_ext_adv_create (const struct bt_le_adv_param *param, const struct bt_le_ext_adv_cb *cb, struct bt_le_ext_adv **adv)
```

相关声明：[bt_le_ext_adv_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[bt_le_ext_adv_cb](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

创建广播集（Advertising Set）。

<a id="r_gaf0f436c55482d9429f674303ae3aa815"></a>

```c
int bt_le_ext_adv_start (struct bt_le_ext_adv *adv, const struct bt_le_ext_adv_start_param *param)
```

相关声明：[bt_le_ext_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0f436c55482d9429f674303ae3aa815)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_start_param](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md)。

使用给定广播集（Advertising Set）启动广播。

<a id="r_ga1c864c4b183f9a86c9f70a11471c5b15"></a>

```c
int bt_le_ext_adv_stop (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_ext_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c864c4b183f9a86c9f70a11471c5b15)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

停止给定广播集（Advertising Set）的广播。

<a id="r_gad731f829b3566be3e56485b2a64f80b1"></a>

```c
int bt_le_ext_adv_set_data (struct bt_le_ext_adv *adv, const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_ext_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad731f829b3566be3e56485b2a64f80b1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

设置广播集的广播数据或扫描响应数据（Advertising / Scan Response Data）。

<a id="r_ga1aabdb81cb1a1841ff0fb91d849123fc"></a>

```c
int bt_le_ext_adv_update_param (struct bt_le_ext_adv *adv, const struct bt_le_adv_param *param)
```

相关声明：[bt_le_ext_adv_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)。

更新广播参数（Advertising Parameters）。

<a id="r_ga62310a27f7fea925dfcf3abd7c454787"></a>

```c
int bt_le_ext_adv_delete (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_ext_adv_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga62310a27f7fea925dfcf3abd7c454787)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

删除广播集（Advertising Set）。

<a id="r_gaf8b28f54c68251024b869f3b0d1c1282"></a>

```c
uint8_t bt_le_ext_adv_get_index (const struct bt_le_ext_adv *adv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_ext_adv_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf8b28f54c68251024b869f3b0d1c1282)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

获取广播集（Advertising Set）的数组索引。

<a id="r_gac06c9f55cf1da46e0d64b4d9af984ecb"></a>

```c
int bt_le_ext_adv_get_info (const struct bt_le_ext_adv *adv, struct bt_le_ext_adv_info *info)
```

相关声明：[bt_le_ext_adv_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac06c9f55cf1da46e0d64b4d9af984ecb)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_info](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md)。

获取广播集信息（Advertising Set Info）。

<a id="r_gaa72029a2759123ec776061d2e80bf3a1"></a>

```c
int bt_le_per_adv_set_param (struct bt_le_ext_adv *adv, const struct bt_le_per_adv_param *param)
```

相关声明：[bt_le_per_adv_set_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa72029a2759123ec776061d2e80bf3a1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_per_adv_param](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md)。

设置或更新周期性广播参数（Periodic Advertising Parameters）。

<a id="r_gafd0e7ccca93a8347a4ca6cca88e77899"></a>

```c
int bt_le_per_adv_set_data (const struct bt_le_ext_adv *adv, const struct bt_data *ad, size_t ad_len)
```

相关声明：[bt_le_per_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

设置或更新周期性广播数据（Periodic Advertising Data）。

<a id="r_ga59e9fc635846ab92af19d483de58ed88"></a>

```c
int bt_le_per_adv_update_did (const struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_update_did](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59e9fc635846ab92af19d483de58ed88)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

更新周期性广播的广播数据标识符（Advertising Data Identifier，DID），不改变数据。

<a id="r_ga7de30fe5040b85bb9212e3a8fec4ac45"></a>

```c
int bt_le_per_adv_set_subevent_data (const struct bt_le_ext_adv *adv, uint8_t num_subevents, const struct bt_le_per_adv_subevent_data_params *params)
```

相关声明：[bt_le_per_adv_set_subevent_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7de30fe5040b85bb9212e3a8fec4ac45)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_per_adv_subevent_data_params](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md)。

设置带响应的周期性广播（Periodic Advertising with Responses）的子事件数据。

<a id="r_ga0f23f4ed48e8679646f247ea0d687094"></a>

```c
int bt_le_per_adv_start (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0f23f4ed48e8679646f247ea0d687094)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动周期性广播（Periodic Advertising）。

<a id="r_ga1b15206fc552d597c12af369d48ff7d5"></a>

```c
int bt_le_per_adv_stop (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1b15206fc552d597c12af369d48ff7d5)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

停止周期性广播（Periodic Advertising）。

<a id="r_ga8d05bd864d98b5b43595eb256e464024"></a>

```c
uint8_t bt_le_per_adv_sync_get_index (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_per_adv_sync_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8d05bd864d98b5b43595eb256e464024)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

获取周期性广播同步对象（Periodic Advertising Sync Object）的数组索引。

<a id="r_ga59532b37412b1b93f81cf5cc1bab0534"></a>

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_index (uint8_t index)
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_lookup_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59532b37412b1b93f81cf5cc1bab0534)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据数组索引获取周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_gabfaf265a48dd09ea02d114e2023c14a6"></a>

```c
int bt_le_per_adv_sync_get_info (struct bt_le_per_adv_sync *per_adv_sync, struct bt_le_per_adv_sync_info *info)
```

相关声明：[bt_le_per_adv_sync_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfaf265a48dd09ea02d114e2023c14a6)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_info](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md)。

获取周期性广播同步信息（Periodic Advertising Sync Information）。

<a id="r_ga83126917373c0bcaa24964dd1d8bde46"></a>

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_addr (const bt_addr_le_t *adv_addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_lookup_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga83126917373c0bcaa24964dd1d8bde46)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据广播者地址查找现有周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_ga061bf84b989b2c96ab51d2ca0debb017"></a>

```c
int bt_le_per_adv_sync_create (const struct bt_le_per_adv_sync_param *param, struct bt_le_per_adv_sync **out_sync)
```

相关声明：[bt_le_per_adv_sync_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga061bf84b989b2c96ab51d2ca0debb017)、[bt_le_per_adv_sync_param](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

创建周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_gaa0c218ff3c78b26dcfaa726ee30267a6"></a>

```c
int bt_le_per_adv_sync_delete (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0c218ff3c78b26dcfaa726ee30267a6)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

删除周期性广播同步（Periodic Advertising Sync）。

<a id="r_ga4ee87bbf79e6ac844d14c3dafb2dadf4"></a>

```c
int bt_le_per_adv_sync_cb_register (struct bt_le_per_adv_sync_cb *cb)
```

相关声明：[bt_le_per_adv_sync_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4ee87bbf79e6ac844d14c3dafb2dadf4)、[bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)。

注册周期性广播同步回调（Periodic Advertising Sync Callbacks）。

<a id="r_gab1576c66b08dc855b2d17fc562f36724"></a>

```c
int bt_le_per_adv_sync_cb_unregister (struct bt_le_per_adv_sync_cb *cb)
```

相关声明：[bt_le_per_adv_sync_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab1576c66b08dc855b2d17fc562f36724)、[bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)。

注销周期性广播同步回调（Periodic Advertising Sync Callbacks）。

<a id="r_ga07e4510de7e72c6ed6196b3da9fb40be"></a>

```c
int bt_le_per_adv_sync_recv_enable (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_recv_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga07e4510de7e72c6ed6196b3da9fb40be)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

允许某个同步接收周期性广播报告（Periodic Advertising Reports）。

<a id="r_ga3dc0c6a0c6a77f4db63ee2ff8329a4c5"></a>

```c
int bt_le_per_adv_sync_recv_disable (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_recv_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

禁止某个同步接收周期性广播报告（Periodic Advertising Reports）。

<a id="r_gaf81a1dd7a628d1a2f25c6b53b0679809"></a>

```c
int bt_le_per_adv_sync_transfer (const struct bt_le_per_adv_sync *per_adv_sync, const struct bt_conn *conn, uint16_t service_data)
```

相关声明：[bt_le_per_adv_sync_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf81a1dd7a628d1a2f25c6b53b0679809)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将周期性广播同步信息（Periodic Advertising Sync Information）传输给对端设备。

<a id="r_gac96199a4e5e6cfb789c1bd1c0e67d6fe"></a>

```c
int bt_le_per_adv_set_info_transfer (const struct bt_le_ext_adv *adv, const struct bt_conn *conn, uint16_t service_data)
```

相关声明：[bt_le_per_adv_set_info_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac96199a4e5e6cfb789c1bd1c0e67d6fe)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

传输有关周期性广播集（Periodic Advertising Set）的信息。

<a id="r_gaa0658bd53df1d5e8e89e13330e4fd0ae"></a>

```c
int bt_le_per_adv_sync_transfer_subscribe (const struct bt_conn *conn, const struct bt_le_per_adv_sync_transfer_param *param)
```

相关声明：[bt_le_per_adv_sync_transfer_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0658bd53df1d5e8e89e13330e4fd0ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_per_adv_sync_transfer_param](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md)。

订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

<a id="r_ga08f872078045bbef4aca19761f25eeb8"></a>

```c
int bt_le_per_adv_sync_transfer_unsubscribe (const struct bt_conn *conn)
```

相关声明：[bt_le_per_adv_sync_transfer_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga08f872078045bbef4aca19761f25eeb8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

取消订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

<a id="r_ga27c4961f3c7270a7f1caeadb4107854b"></a>

```c
int bt_le_per_adv_list_add (const bt_addr_le_t *addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga27c4961f3c7270a7f1caeadb4107854b)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向周期性广播列表（Periodic Advertising List）添加设备。

<a id="r_ga100efac4a49984e06202c63c4e5955cd"></a>

```c
int bt_le_per_adv_list_remove (const bt_addr_le_t *addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga100efac4a49984e06202c63c4e5955cd)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从周期性广播列表（Periodic Advertising List）移除设备。

<a id="r_ga5909bd768c23a19a42a660e3b814c981"></a>

```c
int bt_le_per_adv_list_clear (void)
```

相关声明：[bt_le_per_adv_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5909bd768c23a19a42a660e3b814c981)。

清空周期性广播列表（Periodic Advertising List）。

<a id="r_gac5e19c26b53a08dadb8efa7ecc692ad6"></a>

```c
int bt_le_scan_start (const struct bt_le_scan_param *param, bt_le_scan_cb_t cb)
```

相关声明：[bt_le_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac5e19c26b53a08dadb8efa7ecc692ad6)、[bt_le_scan_param](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md)、[bt_le_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c53d22b6e2dee38c825c58f3eeee9b4)。

启动低功耗蓝牙扫描（LE Scanning）。

<a id="r_gaa2de1a1ab523606b36a4c445fb0c3b84"></a>

```c
int bt_le_scan_stop (void)
```

相关声明：[bt_le_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa2de1a1ab523606b36a4c445fb0c3b84)。

停止低功耗蓝牙扫描（LE Scanning）。

<a id="r_ga80e870fa1de40c404c64624bef439067"></a>

```c
int bt_le_scan_cb_register (struct bt_le_scan_cb *cb)
```

相关声明：[bt_le_scan_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga80e870fa1de40c404c64624bef439067)、[bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)。

注册扫描器数据包回调（Scanner Packet Callbacks）。

<a id="r_gac2718f2128b3f8c79b12d760771c8378"></a>

```c
void bt_le_scan_cb_unregister (struct bt_le_scan_cb *cb)
```

相关声明：[bt_le_scan_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac2718f2128b3f8c79b12d760771c8378)、[bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)。

注销扫描器数据包回调（Scanner Packet Callbacks）。

<a id="r_ga40f2f7fdb09aba3c5137f680e67792f0"></a>

```c
int bt_le_filter_accept_list_add (const bt_addr_le_t *addr)
```

相关声明：[bt_le_filter_accept_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga40f2f7fdb09aba3c5137f680e67792f0)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将低功耗蓝牙设备（LE Device）添加到过滤接受列表（Filter Accept List）。

<a id="r_ga0532ed768ab4f9d69c202066d2f87e66"></a>

```c
int bt_le_filter_accept_list_remove (const bt_addr_le_t *addr)
```

相关声明：[bt_le_filter_accept_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0532ed768ab4f9d69c202066d2f87e66)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

从过滤接受列表（Filter Accept List）移除低功耗蓝牙设备（LE Device）。

<a id="r_gac87df899d1e363c63162988157ee6d00"></a>

```c
int bt_le_filter_accept_list_clear (void)
```

相关声明：[bt_le_filter_accept_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac87df899d1e363c63162988157ee6d00)。

清空过滤接受列表（Filter Accept List）。

<a id="r_gabc115fd3fff6d00ae878a31613bf70aa"></a>

```c
int bt_le_set_chan_map (uint8_t chan_map[5])
```

相关声明：[bt_le_set_chan_map](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabc115fd3fff6d00ae878a31613bf70aa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置低功耗蓝牙信道映射（LE Channel Map）。

<a id="r_ga9ab41e118b5496c196e56b8b5d023275"></a>

```c
int bt_le_set_rpa_timeout (uint16_t new_rpa_timeout)
```

相关声明：[bt_le_set_rpa_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9ab41e118b5496c196e56b8b5d023275)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在运行时设置可解析私有地址（Resolvable Private Address）的超时时间。

<a id="r_ga652eef01e5256e0d820cd1f4db877429"></a>

```c
void bt_data_parse (struct net_buf_simple *ad, bool(*func)(struct bt_data *data, void *user_data), void *user_data)
```

相关声明：[bt_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga652eef01e5256e0d820cd1f4db877429)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

用于解析广播数据、扩展查询响应（EIR）数据或带外（OOB）数据的辅助函数。

<a id="r_ga296d1adf3c9ed2f2c65bb75b887d59ee"></a>

```c
int bt_le_oob_get_local (uint8_t id, struct bt_le_oob *oob)
```

相关声明：[bt_le_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga296d1adf3c9ed2f2c65bb75b887d59ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)。

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

<a id="r_ga7486aab863ca497a50dacf81657f48d4"></a>

```c
int bt_le_ext_adv_oob_get_local (struct bt_le_ext_adv *adv, struct bt_le_oob *oob)
```

相关声明：[bt_le_ext_adv_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7486aab863ca497a50dacf81657f48d4)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)。

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

<a id="r_gaceabbbe6e844650f791010e53c9df6a4"></a>

```c
int bt_unpair (uint8_t id, const bt_addr_le_t *addr)
```

相关声明：[bt_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaceabbbe6e844650f791010e53c9df6a4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

清除配对信息（Pairing Information）。

<a id="r_gaad380b7f8984f8522c1b79f9bdc04905"></a>

```c
void bt_foreach_bond (uint8_t id, void(*func)(const struct bt_bond_info *info, void *user_data), void *user_data)
```

相关声明：[bt_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad380b7f8984f8522c1b79f9bdc04905)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bond_info](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md)。

遍历全部现有绑定（Bonds）。

<a id="r_ga5b5e51f79896d674bf6b70b2251e79d4"></a>

```c
enum bt_le_addr_res_support bt_le_bond_addr_res_support (uint8_t id, const bt_addr_le_t *peer)
```

相关声明：[bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)、[bt_le_bond_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

获取已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

<a id="r_ga8046c2b06d3dad0d6c8184de492517d2"></a>

```c
int bt_configure_data_path (uint8_t dir, uint8_t id, uint8_t vs_config_len, const uint8_t *vs_config)
```

相关声明：[bt_configure_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8046c2b06d3dad0d6c8184de492517d2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置厂商数据路径（Vendor Data Path）。

<a id="r_ga731f4b37a9e5cc13a6816ea23f751b0b"></a>

```c
int bt_le_per_adv_sync_subevent (struct bt_le_per_adv_sync *per_adv_sync, struct bt_le_per_adv_sync_subevent_params *params)
```

相关声明：[bt_le_per_adv_sync_subevent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga731f4b37a9e5cc13a6816ea23f751b0b)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_subevent_params](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md)。

与子事件（Subevents）的一个子集同步。

<a id="r_gaae6b8583f7d5457f20b03dccd146425e"></a>

```c
int bt_le_per_adv_set_response_data (struct bt_le_per_adv_sync *per_adv_sync, const struct bt_le_per_adv_response_params *params, const struct net_buf_simple *data)
```

相关声明：[bt_le_per_adv_set_response_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaae6b8583f7d5457f20b03dccd146425e)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_response_params](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

设置带响应周期性广播（PAwR）中特定子事件的某个响应时隙（Response Slot）的数据。

<a id="r_ga309a67de79cc215db1d33251f267f361"></a>

```c
bool bt_le_bond_exists (uint8_t id, const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_le_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga309a67de79cc215db1d33251f267f361)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查由低功耗蓝牙地址（Bluetooth LE Address）标识的设备是否已绑定（Bonded）。


## 1.6\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/bluetooth/gap.h](../api_source_transport_clock_reference/P016_gap.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/crypto.h](../api_source_reference/P072_crypto.h_源码浏览.md)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/bluetooth/classic/classic.h](../api_source_reference/P095_classic.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [bt_le_ext_adv_sent_info](../bluetooth_connection_model_reference/P107_bt_le_ext_adv_sent_info_结构体.md)
- [bt_le_ext_adv_connected_info](../bluetooth_connection_model_reference/P104_bt_le_ext_adv_connected_info_结构体.md)
- [bt_le_ext_adv_scanned_info](../bluetooth_connection_model_reference/P106_bt_le_ext_adv_scanned_info_结构体.md)
- [bt_le_per_adv_data_request](../bluetooth_connection_model_reference/P112_bt_le_per_adv_data_request_结构体.md)
- [bt_le_per_adv_response_info](../bluetooth_connection_model_reference/P114_bt_le_per_adv_response_info_结构体.md)
- [bt_le_ext_adv_cb](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md)
- [bt_le_local_features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md)
- [bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)
- [bt_le_per_adv_param](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md)
- [bt_le_ext_adv_start_param](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md)
- [bt_le_ext_adv_info](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md)
- [bt_le_per_adv_subevent_data_params](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md)
- [bt_le_per_adv_sync_synced_info](../bluetooth_connection_model_reference/P124_bt_le_per_adv_sync_synced_info_结构体.md)
- [bt_le_per_adv_sync_term_info](../bluetooth_connection_model_reference/P125_bt_le_per_adv_sync_term_info_结构体.md)
- [bt_le_per_adv_sync_recv_info](../bluetooth_connection_model_reference/P121_bt_le_per_adv_sync_recv_info_结构体.md)
- [bt_le_per_adv_sync_state_info](../bluetooth_connection_model_reference/P122_bt_le_per_adv_sync_state_info_结构体.md)
- [bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)
- [bt_le_per_adv_sync_param](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md)
- [bt_le_per_adv_sync_info](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md)
- [bt_le_per_adv_sync_transfer_param](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md)
- [bt_le_scan_param](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md)
- [bt_le_scan_recv_info](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md)
- [bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)
- [bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)
- [bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)
- [bt_bond_info](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md)
- [bt_le_per_adv_sync_subevent_params](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md)
- [bt_le_per_adv_response_params](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md)
- [BT_ID_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaded4b52c9bb87fd4d19b1eb9361973e5)
- [BT_IRK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga17419cd0fcc4660f09ac5dbad3a042f2)
- [BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa26f90b188caa50ca12247b7911a0a5f)
- [BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a81b4b9ce53511c62889790a79b0f6a34)
- [BT_LE_ADV_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga71555b857cf8c2a47c36e4dafa7accf4)
- [BT_LE_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9557269dd36b624b49e76c511c3a0cc1)
- [BT_LE_ADV_CONN_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1f5edc3c4cbead62e32cef8cc7b83725)
- [BT_LE_ADV_CONN_FAST_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa700527b1caf3bef27d96a3f91a29f69)
- [BT_LE_ADV_CONN_FAST_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga684a1110a8973bc17211f6f0824beccd)
- [BT_LE_ADV_CONN_DIR_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab89e033ed3fd116c94120d177dfdc839)
- [BT_LE_ADV_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1610555bf59f1d691d640f245957fdce)
- [BT_LE_ADV_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6ef9fb7a469b03265c7adc99ea19a11b)
- [BT_LE_ADV_OPT_USE_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e)
- [BT_LE_EXT_ADV_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaeaaef4dede5d45251dfe12f329e070b7)
- [BT_LE_EXT_ADV_SCAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5dd57fc7f0e213db08655e631a2f314e)
- [BT_LE_EXT_ADV_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaabc0385f6a5307b48ec43af6aae7dea6)
- [BT_LE_EXT_ADV_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7e46a64af0036c433c2e940ce7db0a05)
- [BT_LE_EXT_ADV_CODED_NCONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0e911d3aafdd0c926590b3272a3da564)
- [BT_LE_EXT_ADV_CODED_NCONN_IDENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac67c52693154ebbeedbb31e100513812)
- [BT_LE_EXT_ADV_START_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0d4c5b05deb5466a0e29c153263b489)
- [BT_LE_EXT_ADV_START_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9b2cefbcb0a85116cadb68f6d80c6429)
- [BT_LE_EXT_ADV_START_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8c83a6f322a479bc24a576a7f091312e)
- [BT_LE_PER_ADV_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga880567278a81098ae55f52f624c61041)
- [BT_LE_PER_ADV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf46e54f8fcda7b65b659685bb225d243)
- [BT_LE_PER_ADV_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8f6a00faaaab2a91ac943c71ed041ac1)
- [BT_LE_SCAN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac9f372ca16afb1c2f0e100c5b1b94cd5)
- [BT_LE_SCAN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga57ace75133343ba8de7fa965f452ee3d)
- [BT_LE_SCAN_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac137ea4ce32697582a337116ffa41da5)
- [BT_LE_SCAN_ACTIVE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9bd9701db0459c066ed7c18343f60911)
- [BT_LE_SCAN_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)
- [BT_LE_SCAN_PASSIVE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8d8ccc9ea1db2c96deae1603ec1c78a3)
- [BT_LE_SCAN_CODED_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga06380c4ae6289c704a143b9d192bc35f)
- [BT_LE_SCAN_CODED_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1e5a4589304babc6b0d49019ebcff6b0)
- [bt_ready_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5398783ab4a5dc854b18e37fb10774eb)
- [bt_le_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c53d22b6e2dee38c825c58f3eeee9b4)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_le_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafbf81dab68b0e484d4742471c722fc28)
- [BT_LE_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf)
- [BT_LE_ADV_OPT_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)
- [BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)
- [BT_LE_ADV_OPT_DIR_ADDR_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)
- [BT_LE_ADV_OPT_FILTER_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5)
- [BT_LE_ADV_OPT_FILTER_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf)
- [BT_LE_ADV_OPT_NOTIFY_SCAN_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b)
- [BT_LE_ADV_OPT_SCANNABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9)
- [BT_LE_ADV_OPT_EXT_ADV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)
- [BT_LE_ADV_OPT_NO_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b)
- [BT_LE_ADV_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1)
- [BT_LE_ADV_OPT_ANONYMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab)
- [BT_LE_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859)
- [BT_LE_ADV_OPT_DISABLE_CHAN_37](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779)
- [BT_LE_ADV_OPT_DISABLE_CHAN_38](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275)
- [BT_LE_ADV_OPT_DISABLE_CHAN_39](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28)
- [BT_LE_ADV_OPT_USE_NRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e)
- [BT_LE_ADV_OPT_REQUIRE_S2_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e)
- [BT_LE_ADV_OPT_REQUIRE_S8_CODING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8)
- [BT_LE_ADV_OPT_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)
- [bt_le_per_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae60a45dde6b4d9f4c54a2a6070254f11)
- [BT_LE_PER_ADV_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)
- [BT_LE_PER_ADV_OPT_USE_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f)
- [BT_LE_PER_ADV_OPT_INCLUDE_ADI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403)
- [bt_le_ext_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga544ccde35638d8f580942d830fe9f242)
- [BT_LE_EXT_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d)
- [BT_LE_EXT_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07)
- [bt_le_per_adv_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga6bb77c0808c761753650cde28ddb013e)
- [BT_LE_PER_ADV_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c)
- [BT_LE_PER_ADV_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b)
- [BT_LE_PER_ADV_STATE_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3)
- [bt_le_per_adv_sync_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac942d7e3cae8fca22080f93bf9528ee9)
- [BT_LE_PER_ADV_SYNC_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c)
- [BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)
- [BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53)
- [BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b)
- [BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e)
- [BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320)
- [bt_le_per_adv_sync_transfer_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga820c5f3721e72662e558cc4576b6111b)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc)
- [BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c)
- [bt_le_scan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab4b5773898e2a1eef21557915a21c996)
- [BT_LE_SCAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185)
- [BT_LE_SCAN_OPT_FILTER_DUPLICATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394)
- [BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae)
- [BT_LE_SCAN_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb)
- [BT_LE_SCAN_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6)
- [BT_LE_SCAN_OPT_EXT_FILTER_POLICY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d)
- [bt_le_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf980473379afa477c09e19912d40d29e)
- [BT_LE_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)
- [BT_LE_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)
- [bt_le_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad0039d4b524a0eef31158dc9b24a497)
- [BT_LE_ADDR_RES_SUPPORT_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9)
- [BT_LE_ADDR_RES_SUPPORT_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab)
- [BT_LE_ADDR_RES_SUPPORT_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c)
- [bt_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac45d16bfe21c3c38e834c293e5ebc42b)
- [bt_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0a58e5a050170e84a80f8d5bb3516ec7)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa8bf6854e7ad1fe7e0805737576e5d1a)
- [bt_set_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac8bb3609a3d6da69ff736809e45f5c8a)
- [bt_get_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad922d894b25e86de3f81ce77200a13fd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_get_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga35b76ea7ce79721e47ca4164e08b2dfb)
- [bt_set_appearance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0729453790aab1bd3d52c623be3b35a)
- [bt_id_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga06d0ae35cbf4382679cc3cfe612cee4d)
- [bt_id_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gae11eb8ad254418c38a0e8689df25a159)
- [bt_id_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabb3353edc8a3a8d29a0370049b20cbe4)
- [bt_id_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf6cd906690a51ebed04bea4f4ef716ff)
- [bt_id_reset_irk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7a595421c232b15ad96b52f0300fd960)
- [bt_le_get_local_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga650faa2a86f54499f4bc5a8657a55a87)
- [bt_le_adv_param_set_tx_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga453074db3964f1b57b92ac7afb0b4fac)
- [bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_le_adv_update_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9a406ebfefac3dd09935a4ae0e317817)
- [bt_le_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1776e310b9d80898e6b32d50c4fe0b49)
- [bt_le_ext_adv_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_ext_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0f436c55482d9429f674303ae3aa815)
- [bt_le_ext_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1c864c4b183f9a86c9f70a11471c5b15)
- [bt_le_ext_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad731f829b3566be3e56485b2a64f80b1)
- [bt_le_ext_adv_update_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1aabdb81cb1a1841ff0fb91d849123fc)
- [bt_le_ext_adv_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga62310a27f7fea925dfcf3abd7c454787)
- [bt_le_ext_adv_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf8b28f54c68251024b869f3b0d1c1282)
- [bt_le_ext_adv_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac06c9f55cf1da46e0d64b4d9af984ecb)
- [bt_le_per_adv_set_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa72029a2759123ec776061d2e80bf3a1)
- [bt_le_per_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)
- [bt_le_per_adv_update_did](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59e9fc635846ab92af19d483de58ed88)
- [bt_le_per_adv_set_subevent_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7de30fe5040b85bb9212e3a8fec4ac45)
- [bt_le_per_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0f23f4ed48e8679646f247ea0d687094)
- [bt_le_per_adv_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga1b15206fc552d597c12af369d48ff7d5)
- [bt_le_per_adv_sync_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8d05bd864d98b5b43595eb256e464024)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_le_per_adv_sync_lookup_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga59532b37412b1b93f81cf5cc1bab0534)
- [bt_le_per_adv_sync_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabfaf265a48dd09ea02d114e2023c14a6)
- [bt_le_per_adv_sync_lookup_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga83126917373c0bcaa24964dd1d8bde46)
- [bt_le_per_adv_sync_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga061bf84b989b2c96ab51d2ca0debb017)
- [bt_le_per_adv_sync_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0c218ff3c78b26dcfaa726ee30267a6)
- [bt_le_per_adv_sync_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4ee87bbf79e6ac844d14c3dafb2dadf4)
- [bt_le_per_adv_sync_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gab1576c66b08dc855b2d17fc562f36724)
- [bt_le_per_adv_sync_recv_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga07e4510de7e72c6ed6196b3da9fb40be)
- [bt_le_per_adv_sync_recv_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)
- [bt_le_per_adv_sync_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf81a1dd7a628d1a2f25c6b53b0679809)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_le_per_adv_set_info_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac96199a4e5e6cfb789c1bd1c0e67d6fe)
- [bt_le_per_adv_sync_transfer_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0658bd53df1d5e8e89e13330e4fd0ae)
- [bt_le_per_adv_sync_transfer_unsubscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga08f872078045bbef4aca19761f25eeb8)
- [bt_le_per_adv_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga27c4961f3c7270a7f1caeadb4107854b)
- [bt_le_per_adv_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga100efac4a49984e06202c63c4e5955cd)
- [bt_le_per_adv_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5909bd768c23a19a42a660e3b814c981)
- [bt_le_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac5e19c26b53a08dadb8efa7ecc692ad6)
- [bt_le_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa2de1a1ab523606b36a4c445fb0c3b84)
- [bt_le_scan_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga80e870fa1de40c404c64624bef439067)
- [bt_le_scan_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac2718f2128b3f8c79b12d760771c8378)
- [bt_le_filter_accept_list_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga40f2f7fdb09aba3c5137f680e67792f0)
- [bt_le_filter_accept_list_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga0532ed768ab4f9d69c202066d2f87e66)
- [bt_le_filter_accept_list_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gac87df899d1e363c63162988157ee6d00)
- [bt_le_set_chan_map](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gabc115fd3fff6d00ae878a31613bf70aa)
- [bt_le_set_rpa_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga9ab41e118b5496c196e56b8b5d023275)
- [bt_data_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga652eef01e5256e0d820cd1f4db877429)
- [bt_le_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga296d1adf3c9ed2f2c65bb75b887d59ee)
- [bt_le_ext_adv_oob_get_local](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga7486aab863ca497a50dacf81657f48d4)
- [bt_unpair](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaceabbbe6e844650f791010e53c9df6a4)
- [bt_foreach_bond](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaad380b7f8984f8522c1b79f9bdc04905)
- [bt_le_bond_addr_res_support](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga5b5e51f79896d674bf6b70b2251e79d4)
- [bt_configure_data_path](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga8046c2b06d3dad0d6c8184de492517d2)
- [bt_le_per_adv_sync_subevent](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga731f4b37a9e5cc13a6816ea23f751b0b)
- [bt_le_per_adv_set_response_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaae6b8583f7d5457f20b03dccd146425e)
- [bt_le_bond_exists](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga309a67de79cc215db1d33251f267f361)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__mesh__cdb.h_文件参考.md)
