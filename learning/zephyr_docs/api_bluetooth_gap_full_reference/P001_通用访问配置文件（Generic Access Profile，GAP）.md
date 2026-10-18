---
id: learning.zephyr-docs.api-bluetooth-gap-full-reference.page-1
title: 通用访问配置文件（Generic Access Profile，GAP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_通用访问配置文件（Generic Access Profile，GAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用访问配置文件（Generic Access Profile，GAP）

<a id="details"></a>

通用访问配置文件（Generic Access Profile，GAP）。GAP 定义蓝牙的基本操作，包括设备发现、配对和连接管理。Zephyr 的 GAP 实现同时支持经典蓝牙（Classic Bluetooth）和低功耗蓝牙（Bluetooth Low Energy，LE），提供广播者（Broadcaster）、观察者（Observer）、外设（Peripheral）及中心设备（Central）等角色。这些角色定义设备在蓝牙网络中进行广播、扫描及建立连接时的行为。自 1.0 起提供，版本 1.1.1。自 1.0 起提供，版本 1.1.1。译注：原页的起始版本与版本号重复列出，此处保留。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_bt_5Fgap_5Fdefines"></a>

相关声明：[定义与分配编号（Defines and Assigned Numbers）](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md)。

蓝牙通用接入配置文件（Generic Access Profile）的定义和分配编号。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

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

<a id="r_bt_5Fbr_5Fdiscovery_5Fresult"></a>

```c
struct bt_br_discovery_result
```

相关声明：[bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)。

BR/EDR 发现结果结构体。

<a id="r_bt_5Fbr_5Fdiscovery_5Fparam"></a>

```c
struct bt_br_discovery_param
```

相关声明：[bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)。

BR/EDR 发现（Discovery）参数。

<a id="r_bt_5Fbr_5Fdiscovery_5Fcb"></a>

```c
struct bt_br_discovery_cb
```

相关声明：[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

<a id="r_bt_5Fbr_5Foob"></a>

```c
struct bt_br_oob
```

相关声明：[bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)。

<a id="r_bt_5Fbr_5Fpage_5Fscan_5Fparam"></a>

```c
struct bt_br_page_scan_param
```

相关声明：[bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)。

寻呼扫描（Page Scan）参数。

<a id="r_bt_5Fbr_5Finquiry_5Fscan_5Fparam"></a>

```c
struct bt_br_inquiry_scan_param
```

相关声明：[bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)。

BR/EDR 查询扫描（Inquiry Scan）参数。

<a id="r_bt_5Fbr_5Fbond_5Finfo"></a>

```c
struct bt_br_bond_info
```

相关声明：[bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)。

与远端设备的绑定（Bond）信息。

<a id="r_bt_5Fle_5Fext_5Fadv"></a>

```c
struct bt_le_ext_adv
```

相关声明：[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

表示广播者（Advertiser）的不透明类型。

<a id="r_bt_5Fle_5Fper_5Fadv_5Fsync"></a>

```c
struct bt_le_per_adv_sync
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

表示周期广播同步（Periodic Advertising Sync）的不透明类型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.3\_宏定义（Macros）

<a id="r_gaded4b52c9bb87fd4d19b1eb9361973e5"></a>

```c
#define BT_ID_DEFAULT 0
```

相关声明：[BT_ID_DEFAULT](#gaded4b52c9bb87fd4d19b1eb9361973e5)。

引用第一个身份地址（Identity Address）的身份句柄（Identity Handle）。

<a id="r_ga17419cd0fcc4660f09ac5dbad3a042f2"></a>

```c
#define BT_IRK_SIZE 16U
```

相关声明：[BT_IRK_SIZE](#ga17419cd0fcc4660f09ac5dbad3a042f2)。

身份解析密钥（Identity Resolving Key）的大小，单位为八位字节。

<a id="r_gaa26f90b188caa50ca12247b7911a0a5f"></a>

```c
#define BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE
```

相关声明：[BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE](#gaa26f90b188caa50ca12247b7911a0a5f)、[BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a81b4b9ce53511c62889790a79b0f6a34)。

本地支持特性（Local Supported Features）的八位字节数。

<a id="r_ga71555b857cf8c2a47c36e4dafa7accf4"></a>

```c
#define BT_LE_ADV_PARAM_INIT(_options, _int_min, _int_max, _peer)
```

相关声明：[BT_LE_ADV_PARAM_INIT](#ga71555b857cf8c2a47c36e4dafa7accf4)。

初始化广播参数（Advertising Parameters）。

<a id="r_ga9557269dd36b624b49e76c511c3a0cc1"></a>

```c
#define BT_LE_ADV_PARAM(_options, _int_min, _int_max, _peer)
```

相关声明：[BT_LE_ADV_PARAM](#ga9557269dd36b624b49e76c511c3a0cc1)。

用于内联声明广播参数（Advertising Parameters）的辅助宏。

<a id="r_ga1f5edc3c4cbead62e32cef8cc7b83725"></a>

```c
#define BT_LE_ADV_CONN_DIR(_peer)
```

相关声明：[BT_LE_ADV_CONN_DIR](#ga1f5edc3c4cbead62e32cef8cc7b83725)。

<a id="r_gaa700527b1caf3bef27d96a3f91a29f69"></a>

```c
#define BT_LE_ADV_CONN_FAST_1
```

相关声明：[BT_LE_ADV_CONN_FAST_1](#gaa700527b1caf3bef27d96a3f91a29f69)。

通用访问配置文件（GAP）推荐的、由使用者发起的可连接广播参数（Connectable Advertising Parameters）。

<a id="r_ga684a1110a8973bc17211f6f0824beccd"></a>

```c
#define BT_LE_ADV_CONN_FAST_2
```

相关声明：[BT_LE_ADV_CONN_FAST_2](#ga684a1110a8973bc17211f6f0824beccd)。

GAP 推荐的可连接广播参数，用于不可连接广播事件（Non-connectable Advertising Events）。（原文同时使用 connectable 与 non-connectable，保留其表述。）

<a id="r_gab89e033ed3fd116c94120d177dfdc839"></a>

```c
#define BT_LE_ADV_CONN_DIR_LOW_DUTY(_peer)
```

相关声明：[BT_LE_ADV_CONN_DIR_LOW_DUTY](#gab89e033ed3fd116c94120d177dfdc839)。

<a id="r_ga1610555bf59f1d691d640f245957fdce"></a>

```c
#define BT_LE_ADV_NCONN
```

相关声明：[BT_LE_ADV_NCONN](#ga1610555bf59f1d691d640f245957fdce)。

使用私有地址（Private Address）的不可连接广播（Non-connectable Advertising）。

<a id="r_ga6ef9fb7a469b03265c7adc99ea19a11b"></a>

```c
#define BT_LE_ADV_NCONN_IDENTITY
```

相关声明：[BT_LE_ADV_NCONN_IDENTITY](#ga6ef9fb7a469b03265c7adc99ea19a11b)。

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接广播（Non-connectable Advertising）。

<a id="r_gaeaaef4dede5d45251dfe12f329e070b7"></a>

```c
#define BT_LE_EXT_ADV_CONN
```

相关声明：[BT_LE_EXT_ADV_CONN](#gaeaaef4dede5d45251dfe12f329e070b7)。

可连接的扩展广播（Connectable Extended Advertising）。

<a id="r_ga5dd57fc7f0e213db08655e631a2f314e"></a>

```c
#define BT_LE_EXT_ADV_SCAN
```

相关声明：[BT_LE_EXT_ADV_SCAN](#ga5dd57fc7f0e213db08655e631a2f314e)。

可扫描的扩展广播（Scannable Extended Advertising）。

<a id="r_gaabc0385f6a5307b48ec43af6aae7dea6"></a>

```c
#define BT_LE_EXT_ADV_NCONN
```

相关声明：[BT_LE_EXT_ADV_NCONN](#gaabc0385f6a5307b48ec43af6aae7dea6)。

使用私有地址（Private Address）的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_ga7e46a64af0036c433c2e940ce7db0a05"></a>

```c
#define BT_LE_EXT_ADV_NCONN_IDENTITY
```

相关声明：[BT_LE_EXT_ADV_NCONN_IDENTITY](#ga7e46a64af0036c433c2e940ce7db0a05)。

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_ga0e911d3aafdd0c926590b3272a3da564"></a>

```c
#define BT_LE_EXT_ADV_CODED_NCONN
```

相关声明：[BT_LE_EXT_ADV_CODED_NCONN](#ga0e911d3aafdd0c926590b3272a3da564)。

在编码物理层（Coded PHY）上使用私有地址的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_gac67c52693154ebbeedbb31e100513812"></a>

```c
#define BT_LE_EXT_ADV_CODED_NCONN_IDENTITY
```

相关声明：[BT_LE_EXT_ADV_CODED_NCONN_IDENTITY](#gac67c52693154ebbeedbb31e100513812)。

在编码物理层（Coded PHY）上使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="r_gaf0d4c5b05deb5466a0e29c153263b489"></a>

```c
#define BT_LE_EXT_ADV_START_PARAM_INIT(_timeout, _n_evts)
```

相关声明：[BT_LE_EXT_ADV_START_PARAM_INIT](#gaf0d4c5b05deb5466a0e29c153263b489)。

用于内联初始化扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

<a id="r_ga9b2cefbcb0a85116cadb68f6d80c6429"></a>

```c
#define BT_LE_EXT_ADV_START_PARAM(_timeout, _n_evts)
```

相关声明：[BT_LE_EXT_ADV_START_PARAM](#ga9b2cefbcb0a85116cadb68f6d80c6429)。

用于内联声明扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

<a id="r_ga8c83a6f322a479bc24a576a7f091312e"></a>

```c
#define BT_LE_EXT_ADV_START_DEFAULT BT_LE_EXT_ADV_START_PARAM(0, 0)
```

相关声明：[BT_LE_EXT_ADV_START_DEFAULT](#ga8c83a6f322a479bc24a576a7f091312e)、[BT_LE_EXT_ADV_START_PARAM](#ga9b2cefbcb0a85116cadb68f6d80c6429)。

<a id="r_ga880567278a81098ae55f52f624c61041"></a>

```c
#define BT_LE_PER_ADV_PARAM_INIT(_int_min, _int_max, _options)
```

相关声明：[BT_LE_PER_ADV_PARAM_INIT](#ga880567278a81098ae55f52f624c61041)。

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

<a id="r_gaf46e54f8fcda7b65b659685bb225d243"></a>

```c
#define BT_LE_PER_ADV_PARAM(_int_min, _int_max, _options)
```

相关声明：[BT_LE_PER_ADV_PARAM](#gaf46e54f8fcda7b65b659685bb225d243)。

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

<a id="r_ga8f6a00faaaab2a91ac943c71ed041ac1"></a>

```c
#define BT_LE_PER_ADV_DEFAULT
```

相关声明：[BT_LE_PER_ADV_DEFAULT](#ga8f6a00faaaab2a91ac943c71ed041ac1)。

<a id="r_gac9f372ca16afb1c2f0e100c5b1b94cd5"></a>

```c
#define BT_LE_SCAN_PARAM_INIT(_type, _options, _interval, _window)
```

相关声明：[BT_LE_SCAN_PARAM_INIT](#gac9f372ca16afb1c2f0e100c5b1b94cd5)。

初始化扫描参数（Scan Parameters）。

<a id="r_ga57ace75133343ba8de7fa965f452ee3d"></a>

```c
#define BT_LE_SCAN_PARAM(_type, _options, _interval, _window)
```

相关声明：[BT_LE_SCAN_PARAM](#ga57ace75133343ba8de7fa965f452ee3d)。

用于内联声明扫描参数（Scan Parameters）的辅助宏。

<a id="r_gac137ea4ce32697582a337116ffa41da5"></a>

```c
#define BT_LE_SCAN_ACTIVE
```

相关声明：[BT_LE_SCAN_ACTIVE](#gac137ea4ce32697582a337116ffa41da5)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

<a id="r_ga9bd9701db0459c066ed7c18343f60911"></a>

```c
#define BT_LE_SCAN_ACTIVE_CONTINUOUS
```

相关声明：[BT_LE_SCAN_ACTIVE_CONTINUOUS](#ga9bd9701db0459c066ed7c18343f60911)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏，其中 window == interval。

<a id="r_ga8ceaef6f0fbf4fe2d76d47e8f59aeb11"></a>

```c
#define BT_LE_SCAN_PASSIVE
```

相关声明：[BT_LE_SCAN_PASSIVE](#ga8ceaef6f0fbf4fe2d76d47e8f59aeb11)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

<a id="r_ga8d8ccc9ea1db2c96deae1603ec1c78a3"></a>

```c
#define BT_LE_SCAN_PASSIVE_CONTINUOUS
```

相关声明：[BT_LE_SCAN_PASSIVE_CONTINUOUS](#ga8d8ccc9ea1db2c96deae1603ec1c78a3)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏，其中 window == interval。

<a id="r_ga06380c4ae6289c704a143b9d192bc35f"></a>

```c
#define BT_LE_SCAN_CODED_ACTIVE
```

相关声明：[BT_LE_SCAN_CODED_ACTIVE](#ga06380c4ae6289c704a143b9d192bc35f)。

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

<a id="r_ga1e5a4589304babc6b0d49019ebcff6b0"></a>

```c
#define BT_LE_SCAN_CODED_PASSIVE
```

相关声明：[BT_LE_SCAN_CODED_PASSIVE](#ga1e5a4589304babc6b0d49019ebcff6b0)。

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

<a id="r_ga925f510c862c9a36539f4df1db0009d6"></a>

```c
#define BT_BR_EIR_SIZE_MAX 240
```

相关声明：[BT_BR_EIR_SIZE_MAX](#ga925f510c862c9a36539f4df1db0009d6)。

扩展查询响应（Extended Inquiry Response）的最大大小。

<a id="r_gada5bcc61877ac75849dc3c2867ad2505"></a>

```c
#define BT_BR_SCAN_INTERVAL_MIN 0x0012
```

相关声明：[BT_BR_SCAN_INTERVAL_MIN](#gada5bcc61877ac75849dc3c2867ad2505)。

BR/EDR 最小扫描间隔（Scan Interval）：0x0012，即 11.25 ms，单位为 0.625 ms。

<a id="r_ga03ede7b8791a42172f28882f9da8f52e"></a>

```c
#define BT_BR_SCAN_INTERVAL_MAX 0x1000
```

相关声明：[BT_BR_SCAN_INTERVAL_MAX](#ga03ede7b8791a42172f28882f9da8f52e)。

BR/EDR 最大扫描间隔（Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_gac69aaf3d5de86a2ba1ab7a7194256c79"></a>

```c
#define BT_BR_SCAN_WINDOW_MIN 0x0011
```

相关声明：[BT_BR_SCAN_WINDOW_MIN](#gac69aaf3d5de86a2ba1ab7a7194256c79)。

BR/EDR 最小扫描窗口（Scan Window）：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga1b29c1de2a023f5b892939cda856f491"></a>

```c
#define BT_BR_SCAN_WINDOW_MAX 0x1000
```

相关声明：[BT_BR_SCAN_WINDOW_MAX](#ga1b29c1de2a023f5b892939cda856f491)。

BR/EDR 最大扫描窗口（Scan Window）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_gaff027ae0fe3fbac63db9c87f8e480214"></a>

```c
#define BT_BR_SCAN_INIT(_interval, _window, _type)
```

相关声明：[BT_BR_SCAN_INIT](#gaff027ae0fe3fbac63db9c87f8e480214)。

初始化基本速率扫描参数（BR Scan Parameters）。

<a id="r_ga4d053fafbc0faed58c3305efdd581838"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM(_interval, _window, _type)
```

相关声明：[BT_BR_PAGE_SCAN_PARAM](#ga4d053fafbc0faed58c3305efdd581838)。

用于内联声明 BR/EDR 寻呼扫描参数（Page Scan Parameters）的辅助宏。

<a id="r_ga8c22bfb02c45f522794e6e3f0054ffa0"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_R0
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_R0](#ga8c22bfb02c45f522794e6e3f0054ffa0)。

R0 的默认寻呼扫描参数（Default Page Scan Parameters）。

<a id="r_ga9f20d66911eaedeb26c93281e21febb6"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_FAST_R1](#ga9f20d66911eaedeb26c93281e21febb6)。

R1 的快速寻呼扫描参数（Fast Page Scan Parameters）。

<a id="r_ga6c58418072c3cb5cc35193414a20f98f"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1](#ga6c58418072c3cb5cc35193414a20f98f)。

R1 的中速寻呼扫描参数（Medium Page Scan Parameters）。

<a id="r_gae2641df344fc7bd32ad0ed7c185538a7"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R1
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_SLOW_R1](#gae2641df344fc7bd32ad0ed7c185538a7)。

R1 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

<a id="r_gab0bcacaa4d7ddfe85918ed26b7525eb7"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R2
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_FAST_R2](#gab0bcacaa4d7ddfe85918ed26b7525eb7)。

R2 的快速寻呼扫描参数（Fast Page Scan Parameters）。

<a id="r_ga1558b2c9183c631cd8a7fa0988598184"></a>

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R2
```

相关声明：[BT_BR_PAGE_SCAN_PARAM_SLOW_R2](#ga1558b2c9183c631cd8a7fa0988598184)。

R2 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

<a id="r_ga7a9e4560e84fa43e7c1f3cad39bdf24e"></a>

```c
#define BT_BR_INQUIRY_SCAN_PARAM(_interval, _window, _type)
```

相关声明：[BT_BR_INQUIRY_SCAN_PARAM](#ga7a9e4560e84fa43e7c1f3cad39bdf24e)。

用于内联声明 BR/EDR 查询扫描参数（Inquiry Scan Parameters）的辅助宏。

<a id="r_gabe6aa0d2210ab0507d3b06bfd7000aaa"></a>

```c
#define BT_BR_INQUIRY_SCAN_PARAM_DEFAULT
```

相关声明：[BT_BR_INQUIRY_SCAN_PARAM_DEFAULT](#gabe6aa0d2210ab0507d3b06bfd7000aaa)。

默认查询扫描参数（Default Inquiry Scan Parameters）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.4\_类型定义（Typedefs）

<a id="r_ga5398783ab4a5dc854b18e37fb10774eb"></a>

```c
typedef void(* bt_ready_cb_t) (int err)
```

相关声明：[bt_ready_cb_t](#ga5398783ab4a5dc854b18e37fb10774eb)。

通知蓝牙（Bluetooth）已启用的回调。

<a id="r_ga1c53d22b6e2dee38c825c58f3eeee9b4"></a>

```c
typedef void bt_le_scan_cb_t(const bt_addr_le_t *addr, int8_t rssi, uint8_t adv_type, struct net_buf_simple *buf)
```

相关声明：[bt_le_scan_cb_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

报告低功耗蓝牙（LE）扫描结果的回调类型（Callback Type）。

<a id="r_gab661e90ad27ce1a280cefc15c5ad040c"></a>

```c
typedef enum bt_br_conn_req_rsp(* bt_br_conn_req_func_t) (const bt_addr_t *addr, uint32_t cod)
```

相关声明：[bt_br_conn_req_rsp](#gabfc34fe6f398d6526acc7c5afde8a689)、[bt_br_conn_req_func_t](#gab661e90ad27ce1a280cefc15c5ad040c)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

传入 BR/EDR 连接请求（Incoming Connection Requests）的回调类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.5\_枚举（Enumerations）

<a id="r_gafbf81dab68b0e484d4742471c722fc28"></a>

```c
enum bt_le_adv_opt { BT_LE_ADV_OPT_NONE = 0 , BT_LE_ADV_OPT_CONN = (1UL << (0)) | (1UL << (1)) , BT_LE_ADV_OPT_USE_IDENTITY = (1UL << (2)) , BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY = (1UL << (4)) , BT_LE_ADV_OPT_DIR_ADDR_RPA = (1UL << (5)) , BT_LE_ADV_OPT_FILTER_SCAN_REQ = (1UL << (6)) , BT_LE_ADV_OPT_FILTER_CONN = (1UL << (7)) , BT_LE_ADV_OPT_NOTIFY_SCAN_REQ = (1UL << (8)) , BT_LE_ADV_OPT_SCANNABLE = (1UL << (9)) , BT_LE_ADV_OPT_EXT_ADV = (1UL << (10)) , BT_LE_ADV_OPT_NO_2M = (1UL << (11)) , BT_LE_ADV_OPT_CODED = (1UL << (12)) , BT_LE_ADV_OPT_ANONYMOUS = (1UL << (13)) , BT_LE_ADV_OPT_USE_TX_POWER = (1UL << (14)) , BT_LE_ADV_OPT_DISABLE_CHAN_37 = (1UL << (15)) , BT_LE_ADV_OPT_DISABLE_CHAN_38 = (1UL << (16)) , BT_LE_ADV_OPT_DISABLE_CHAN_39 = (1UL << (17)) , BT_LE_ADV_OPT_USE_NRPA = (1UL << (19)) , BT_LE_ADV_OPT_REQUIRE_S2_CODING = (1UL << (20)) , BT_LE_ADV_OPT_REQUIRE_S8_CODING = (1UL << (21)) , BT_LE_ADV_OPT_TX_POWER = (1UL << (22)) }
```

相关声明：[bt_le_adv_opt](#gafbf81dab68b0e484d4742471c722fc28)、[BT_LE_ADV_OPT_NONE](#ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf)、[BT_LE_ADV_OPT_CONN](#ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169)、[BT_LE_ADV_OPT_USE_IDENTITY](#ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e)、[BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY](#ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872)、[BT_LE_ADV_OPT_DIR_ADDR_RPA](#ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f)、[BT_LE_ADV_OPT_FILTER_SCAN_REQ](#ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5)、[BT_LE_ADV_OPT_FILTER_CONN](#ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf)、[BT_LE_ADV_OPT_NOTIFY_SCAN_REQ](#ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b)、[BT_LE_ADV_OPT_SCANNABLE](#ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9)、[BT_LE_ADV_OPT_EXT_ADV](#ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab)、[BT_LE_ADV_OPT_NO_2M](#ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b)、[BT_LE_ADV_OPT_CODED](#ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1)、[BT_LE_ADV_OPT_ANONYMOUS](#ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab)、[BT_LE_ADV_OPT_USE_TX_POWER](#ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859)、[BT_LE_ADV_OPT_DISABLE_CHAN_37](#ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779)、[BT_LE_ADV_OPT_DISABLE_CHAN_38](#ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275)、[BT_LE_ADV_OPT_DISABLE_CHAN_39](#ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28)、[BT_LE_ADV_OPT_USE_NRPA](#ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e)、[BT_LE_ADV_OPT_REQUIRE_S2_CODING](#ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e)、[BT_LE_ADV_OPT_REQUIRE_S8_CODING](#ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8)、[BT_LE_ADV_OPT_TX_POWER](#ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56)。

广播选项（Advertising Options）。

<a id="r_gae60a45dde6b4d9f4c54a2a6070254f11"></a>

```c
enum bt_le_per_adv_opt { BT_LE_PER_ADV_OPT_NONE = 0 , BT_LE_PER_ADV_OPT_USE_TX_POWER = (1UL << (1)) , BT_LE_PER_ADV_OPT_INCLUDE_ADI = (1UL << (2)) }
```

相关声明：[bt_le_per_adv_opt](#gae60a45dde6b4d9f4c54a2a6070254f11)、[BT_LE_PER_ADV_OPT_NONE](#ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518)、[BT_LE_PER_ADV_OPT_USE_TX_POWER](#ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f)、[BT_LE_PER_ADV_OPT_INCLUDE_ADI](#ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403)。

周期性广播选项（Periodic Advertising Options）。

<a id="r_ga544ccde35638d8f580942d830fe9f242"></a>

```c
enum bt_le_ext_adv_state { BT_LE_EXT_ADV_STATE_DISABLED , BT_LE_EXT_ADV_STATE_ENABLED }
```

相关声明：[bt_le_ext_adv_state](#ga544ccde35638d8f580942d830fe9f242)、[BT_LE_EXT_ADV_STATE_DISABLED](#gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d)、[BT_LE_EXT_ADV_STATE_ENABLED](#gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07)。

广播状态（Advertising States）。

<a id="r_ga6bb77c0808c761753650cde28ddb013e"></a>

```c
enum bt_le_per_adv_state { BT_LE_PER_ADV_STATE_NONE , BT_LE_PER_ADV_STATE_DISABLED , BT_LE_PER_ADV_STATE_ENABLED }
```

相关声明：[bt_le_per_adv_state](#ga6bb77c0808c761753650cde28ddb013e)、[BT_LE_PER_ADV_STATE_NONE](#gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c)、[BT_LE_PER_ADV_STATE_DISABLED](#gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b)、[BT_LE_PER_ADV_STATE_ENABLED](#gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3)。

周期性广播状态（Periodic Advertising States）。

<a id="r_gac942d7e3cae8fca22080f93bf9528ee9"></a>

```c
enum bt_le_per_adv_sync_opt { BT_LE_PER_ADV_SYNC_OPT_NONE = 0 , BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST = (1UL << (0)) , BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED = (1UL << (1)) , BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE = (1UL << (2)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA = (1UL << (3)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US = (1UL << (4)) , BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US = (1UL << (5)) , BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT = (1UL << (6)) }
```

相关声明：[bt_le_per_adv_sync_opt](#gac942d7e3cae8fca22080f93bf9528ee9)、[BT_LE_PER_ADV_SYNC_OPT_NONE](#ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c)、[BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST](#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)、[BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED](#ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53)、[BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE](#ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA](#ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US](#ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b)、[BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US](#ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e)、[BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT](#ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320)。

周期性广播同步选项（Periodic Advertising Sync Options）。

<a id="r_ga820c5f3721e72662e558cc4576b6111b"></a>

```c
enum bt_le_per_adv_sync_transfer_opt { BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE = 0 , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA = (1UL << (0)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US = (1UL << (1)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US = (1UL << (2)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE = (1UL << (3)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED = (1UL << (4)) , BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES = (1UL << (5)) }
```

相关声明：[bt_le_per_adv_sync_transfer_opt](#ga820c5f3721e72662e558cc4576b6111b)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE](#gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA](#gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US](#gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US](#gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE](#gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED](#gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc)、[BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES](#gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c)。

周期性广播同步传输选项（Periodic Advertising Sync Transfer Options）。

<a id="r_gab4b5773898e2a1eef21557915a21c996"></a>

```c
enum bt_le_scan_opt { BT_LE_SCAN_OPT_NONE = 0 , BT_LE_SCAN_OPT_FILTER_DUPLICATE = (1UL << (0)) , BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST = (1UL << (1)) , BT_LE_SCAN_OPT_CODED = (1UL << (2)) , BT_LE_SCAN_OPT_NO_1M = (1UL << (3)) , BT_LE_SCAN_OPT_EXT_FILTER_POLICY = (1UL << (4)) }
```

相关声明：[bt_le_scan_opt](#gab4b5773898e2a1eef21557915a21c996)、[BT_LE_SCAN_OPT_NONE](#ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185)、[BT_LE_SCAN_OPT_FILTER_DUPLICATE](#ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394)、[BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST](#ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae)、[BT_LE_SCAN_OPT_CODED](#ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb)、[BT_LE_SCAN_OPT_NO_1M](#ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6)、[BT_LE_SCAN_OPT_EXT_FILTER_POLICY](#ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d)。

<a id="r_gaf980473379afa477c09e19912d40d29e"></a>

```c
enum bt_le_scan_type { BT_LE_SCAN_TYPE_PASSIVE = 0x00 , BT_LE_SCAN_TYPE_ACTIVE = 0x01 }
```

相关声明：[bt_le_scan_type](#gaf980473379afa477c09e19912d40d29e)、[BT_LE_SCAN_TYPE_PASSIVE](#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)、[BT_LE_SCAN_TYPE_ACTIVE](#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)。

<a id="r_gaad0039d4b524a0eef31158dc9b24a497"></a>

```c
enum bt_le_addr_res_support { BT_LE_ADDR_RES_SUPPORT_UNKNOWN , BT_LE_ADDR_RES_SUPPORT_NO , BT_LE_ADDR_RES_SUPPORT_YES }
```

相关声明：[bt_le_addr_res_support](#gaad0039d4b524a0eef31158dc9b24a497)、[BT_LE_ADDR_RES_SUPPORT_UNKNOWN](#ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9)、[BT_LE_ADDR_RES_SUPPORT_NO](#ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab)、[BT_LE_ADDR_RES_SUPPORT_YES](#ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c)。

已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

<a id="r_gabfc34fe6f398d6526acc7c5afde8a689"></a>

```c
enum bt_br_conn_req_rsp { BT_BR_CONN_REQ_ACCEPT_CENTRAL = BT_HCI_ROLE_CENTRAL , BT_BR_CONN_REQ_ACCEPT_PERIPHERAL = BT_HCI_ROLE_PERIPHERAL , BT_BR_CONN_REQ_REJECT_NO_RESOURCES = BT_HCI_ERR_INSUFFICIENT_RESOURCES , BT_BR_CONN_REQ_REJECT_SECURITY = BT_HCI_ERR_INSUFFICIENT_SECURITY , BT_BR_CONN_REQ_REJECT_ADDR = BT_HCI_ERR_BD_ADDR_UNACCEPTABLE }
```

相关声明：[bt_br_conn_req_rsp](#gabfc34fe6f398d6526acc7c5afde8a689)、[BT_BR_CONN_REQ_ACCEPT_CENTRAL](#ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f)、[BT_BR_CONN_REQ_ACCEPT_PERIPHERAL](#ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97)、[BT_BR_CONN_REQ_REJECT_NO_RESOURCES](#ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a)、[BT_BR_CONN_REQ_REJECT_SECURITY](#ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35)、[BT_BR_CONN_REQ_REJECT_ADDR](#ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908)。

BR/EDR 连接请求响应码（Connection Request Response Codes）。

<a id="r_ga03757f934de6f13f95f02316b098875d"></a>

```c
enum bt_br_scan_type { BT_BR_SCAN_TYPE_STANDARD = 0 , BT_BR_SCAN_TYPE_INTERLACED = 1 }
```

相关声明：[bt_br_scan_type](#ga03757f934de6f13f95f02316b098875d)、[BT_BR_SCAN_TYPE_STANDARD](#gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7)、[BT_BR_SCAN_TYPE_INTERLACED](#gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d)。

寻呼扫描类型（Page Scan Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.6\_函数（Functions）

<a id="r_gac45d16bfe21c3c38e834c293e5ebc42b"></a>

```c
int bt_enable (bt_ready_cb_t cb)
```

相关声明：[bt_enable](#gac45d16bfe21c3c38e834c293e5ebc42b)、[bt_ready_cb_t](#ga5398783ab4a5dc854b18e37fb10774eb)。

启用蓝牙（Bluetooth）。

<a id="r_ga0a58e5a050170e84a80f8d5bb3516ec7"></a>

```c
int bt_disable (void)
```

相关声明：[bt_disable](#ga0a58e5a050170e84a80f8d5bb3516ec7)。

禁用蓝牙（Bluetooth）。

<a id="r_gaa8bf6854e7ad1fe7e0805737576e5d1a"></a>

```c
bool bt_is_ready (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_is_ready](#gaa8bf6854e7ad1fe7e0805737576e5d1a)。

检查蓝牙（Bluetooth）是否就绪。

<a id="r_gac8bb3609a3d6da69ff736809e45f5c8a"></a>

```c
int bt_set_name (const char *name)
```

相关声明：[bt_set_name](#gac8bb3609a3d6da69ff736809e45f5c8a)。

设置蓝牙设备名称（Bluetooth Device Name）。

<a id="r_gad922d894b25e86de3f81ce77200a13fd"></a>

```c
const char * bt_get_name (void)
```

相关声明：[bt_get_name](#gad922d894b25e86de3f81ce77200a13fd)。

获取蓝牙设备名称（Bluetooth Device Name）。

<a id="r_ga35b76ea7ce79721e47ca4164e08b2dfb"></a>

```c
uint16_t bt_get_appearance (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_get_appearance](#ga35b76ea7ce79721e47ca4164e08b2dfb)。

获取本地蓝牙外观值（Bluetooth Appearance）。

<a id="r_gaf0729453790aab1bd3d52c623be3b35a"></a>

```c
int bt_set_appearance (uint16_t new_appearance)
```

相关声明：[bt_set_appearance](#gaf0729453790aab1bd3d52c623be3b35a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置本地蓝牙外观值（Bluetooth Appearance）。

<a id="r_ga06d0ae35cbf4382679cc3cfe612cee4d"></a>

```c
void bt_id_get (bt_addr_le_t *addrs, size_t *count)
```

相关声明：[bt_id_get](#ga06d0ae35cbf4382679cc3cfe612cee4d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

获取当前配置的身份地址（Identity Addresses）。

<a id="r_gae11eb8ad254418c38a0e8689df25a159"></a>

```c
int bt_id_create (bt_addr_le_t *addr, uint8_t *irk)
```

相关声明：[bt_id_create](#gae11eb8ad254418c38a0e8689df25a159)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建新的身份地址（Identity Address）。

<a id="r_gabb3353edc8a3a8d29a0370049b20cbe4"></a>

```c
int bt_id_reset (uint8_t id, bt_addr_le_t *addr, uint8_t *irk)
```

相关声明：[bt_id_reset](#gabb3353edc8a3a8d29a0370049b20cbe4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

重置／回收身份地址（Identity Address）以供重用。

<a id="r_gaf6cd906690a51ebed04bea4f4ef716ff"></a>

```c
int bt_id_delete (uint8_t id)
```

相关声明：[bt_id_delete](#gaf6cd906690a51ebed04bea4f4ef716ff)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

删除身份地址（Identity Address）。

<a id="r_ga7a595421c232b15ad96b52f0300fd960"></a>

```c
int bt_id_reset_irk (uint8_t id, uint8_t *irk)
```

相关声明：[bt_id_reset_irk](#ga7a595421c232b15ad96b52f0300fd960)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

重置某个身份的本地身份解析密钥（Identity Resolving Key，IRK）。

<a id="r_ga650faa2a86f54499f4bc5a8657a55a87"></a>

```c
int bt_le_get_local_features (struct bt_le_local_features *local_features)
```

相关声明：[bt_le_get_local_features](#ga650faa2a86f54499f4bc5a8657a55a87)、[bt_le_local_features](../bluetooth_connection_model_reference/P109_bt_le_local_features_结构体.md)。

获取本地低功耗蓝牙控制器特性（Bluetooth LE Controller Features）。

<a id="r_ga453074db3964f1b57b92ac7afb0b4fac"></a>

```c
static void bt_le_adv_param_set_tx_power (struct bt_le_adv_param *param, int8_t tx_power)
```

相关声明：[bt_le_adv_param_set_tx_power](#ga453074db3964f1b57b92ac7afb0b4fac)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置广播参数结构体（Advertising Parameter Struct）中的发射功率（TX Power）。

<a id="r_gad2e3caef88d52d720e8e4d21df767b02"></a>

```c
int bt_le_adv_start (const struct bt_le_adv_param *param, const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_adv_start](#gad2e3caef88d52d720e8e4d21df767b02)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

启动广播（Advertising）。

<a id="r_ga9a406ebfefac3dd09935a4ae0e317817"></a>

```c
int bt_le_adv_update_data (const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_adv_update_data](#ga9a406ebfefac3dd09935a4ae0e317817)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

更新广播（Advertising）。

<a id="r_ga1776e310b9d80898e6b32d50c4fe0b49"></a>

```c
int bt_le_adv_stop (void)
```

相关声明：[bt_le_adv_stop](#ga1776e310b9d80898e6b32d50c4fe0b49)。

停止广播（Advertising）。

<a id="r_gad02b855dd7a26e3910b247fa73f19297"></a>

```c
int bt_le_ext_adv_create (const struct bt_le_adv_param *param, const struct bt_le_ext_adv_cb *cb, struct bt_le_ext_adv **adv)
```

相关声明：[bt_le_ext_adv_create](#gad02b855dd7a26e3910b247fa73f19297)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)、[bt_le_ext_adv_cb](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

创建广播集（Advertising Set）。

<a id="r_gaf0f436c55482d9429f674303ae3aa815"></a>

```c
int bt_le_ext_adv_start (struct bt_le_ext_adv *adv, const struct bt_le_ext_adv_start_param *param)
```

相关声明：[bt_le_ext_adv_start](#gaf0f436c55482d9429f674303ae3aa815)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_start_param](../bluetooth_connection_model_reference/P108_bt_le_ext_adv_start_param_结构体.md)。

使用给定广播集（Advertising Set）启动广播。

<a id="r_ga1c864c4b183f9a86c9f70a11471c5b15"></a>

```c
int bt_le_ext_adv_stop (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_ext_adv_stop](#ga1c864c4b183f9a86c9f70a11471c5b15)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

停止给定广播集（Advertising Set）的广播。

<a id="r_gad731f829b3566be3e56485b2a64f80b1"></a>

```c
int bt_le_ext_adv_set_data (struct bt_le_ext_adv *adv, const struct bt_data *ad, size_t ad_len, const struct bt_data *sd, size_t sd_len)
```

相关声明：[bt_le_ext_adv_set_data](#gad731f829b3566be3e56485b2a64f80b1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

设置广播集的广播数据或扫描响应数据（Advertising / Scan Response Data）。

<a id="r_ga1aabdb81cb1a1841ff0fb91d849123fc"></a>

```c
int bt_le_ext_adv_update_param (struct bt_le_ext_adv *adv, const struct bt_le_adv_param *param)
```

相关声明：[bt_le_ext_adv_update_param](#ga1aabdb81cb1a1841ff0fb91d849123fc)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_adv_param](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md)。

更新广播参数（Advertising Parameters）。

<a id="r_ga62310a27f7fea925dfcf3abd7c454787"></a>

```c
int bt_le_ext_adv_delete (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_ext_adv_delete](#ga62310a27f7fea925dfcf3abd7c454787)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

删除广播集（Advertising Set）。

<a id="r_gaf8b28f54c68251024b869f3b0d1c1282"></a>

```c
uint8_t bt_le_ext_adv_get_index (const struct bt_le_ext_adv *adv)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_ext_adv_get_index](#gaf8b28f54c68251024b869f3b0d1c1282)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

获取广播集（Advertising Set）的数组索引。

<a id="r_gac06c9f55cf1da46e0d64b4d9af984ecb"></a>

```c
int bt_le_ext_adv_get_info (const struct bt_le_ext_adv *adv, struct bt_le_ext_adv_info *info)
```

相关声明：[bt_le_ext_adv_get_info](#gac06c9f55cf1da46e0d64b4d9af984ecb)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_info](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md)。

获取广播集信息（Advertising Set Info）。

<a id="r_gaa72029a2759123ec776061d2e80bf3a1"></a>

```c
int bt_le_per_adv_set_param (struct bt_le_ext_adv *adv, const struct bt_le_per_adv_param *param)
```

相关声明：[bt_le_per_adv_set_param](#gaa72029a2759123ec776061d2e80bf3a1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_per_adv_param](../bluetooth_connection_model_reference/P113_bt_le_per_adv_param_结构体.md)。

设置或更新周期性广播参数（Periodic Advertising Parameters）。

<a id="r_gafd0e7ccca93a8347a4ca6cca88e77899"></a>

```c
int bt_le_per_adv_set_data (const struct bt_le_ext_adv *adv, const struct bt_data *ad, size_t ad_len)
```

相关声明：[bt_le_per_adv_set_data](#gafd0e7ccca93a8347a4ca6cca88e77899)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

设置或更新周期性广播数据（Periodic Advertising Data）。

<a id="r_ga59e9fc635846ab92af19d483de58ed88"></a>

```c
int bt_le_per_adv_update_did (const struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_update_did](#ga59e9fc635846ab92af19d483de58ed88)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

更新周期性广播的广播数据标识符（Advertising Data Identifier，DID），不改变数据。

<a id="r_ga7de30fe5040b85bb9212e3a8fec4ac45"></a>

```c
int bt_le_per_adv_set_subevent_data (const struct bt_le_ext_adv *adv, uint8_t num_subevents, const struct bt_le_per_adv_subevent_data_params *params)
```

相关声明：[bt_le_per_adv_set_subevent_data](#ga7de30fe5040b85bb9212e3a8fec4ac45)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_per_adv_subevent_data_params](../bluetooth_connection_model_reference/P116_bt_le_per_adv_subevent_data_params_结构体.md)。

设置带响应的周期性广播（Periodic Advertising with Responses）的子事件数据。

<a id="r_ga0f23f4ed48e8679646f247ea0d687094"></a>

```c
int bt_le_per_adv_start (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_start](#ga0f23f4ed48e8679646f247ea0d687094)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

启动周期性广播（Periodic Advertising）。

<a id="r_ga1b15206fc552d597c12af369d48ff7d5"></a>

```c
int bt_le_per_adv_stop (struct bt_le_ext_adv *adv)
```

相关声明：[bt_le_per_adv_stop](#ga1b15206fc552d597c12af369d48ff7d5)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

停止周期性广播（Periodic Advertising）。

<a id="r_ga8d05bd864d98b5b43595eb256e464024"></a>

```c
uint8_t bt_le_per_adv_sync_get_index (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_per_adv_sync_get_index](#ga8d05bd864d98b5b43595eb256e464024)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

获取周期性广播同步对象（Periodic Advertising Sync Object）的数组索引。

<a id="r_ga59532b37412b1b93f81cf5cc1bab0534"></a>

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_index (uint8_t index)
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_lookup_index](#ga59532b37412b1b93f81cf5cc1bab0534)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据数组索引获取周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_gabfaf265a48dd09ea02d114e2023c14a6"></a>

```c
int bt_le_per_adv_sync_get_info (struct bt_le_per_adv_sync *per_adv_sync, struct bt_le_per_adv_sync_info *info)
```

相关声明：[bt_le_per_adv_sync_get_info](#gabfaf265a48dd09ea02d114e2023c14a6)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_info](../bluetooth_connection_model_reference/P119_bt_le_per_adv_sync_info_结构体.md)。

获取周期性广播同步信息（Periodic Advertising Sync Information）。

<a id="r_ga83126917373c0bcaa24964dd1d8bde46"></a>

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_addr (const bt_addr_le_t *adv_addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_lookup_addr](#ga83126917373c0bcaa24964dd1d8bde46)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据广播者地址查找现有周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_ga061bf84b989b2c96ab51d2ca0debb017"></a>

```c
int bt_le_per_adv_sync_create (const struct bt_le_per_adv_sync_param *param, struct bt_le_per_adv_sync **out_sync)
```

相关声明：[bt_le_per_adv_sync_create](#ga061bf84b989b2c96ab51d2ca0debb017)、[bt_le_per_adv_sync_param](../bluetooth_connection_model_reference/P120_bt_le_per_adv_sync_param_结构体.md)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

创建周期性广播同步对象（Periodic Advertising Sync Object）。

<a id="r_gaa0c218ff3c78b26dcfaa726ee30267a6"></a>

```c
int bt_le_per_adv_sync_delete (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_delete](#gaa0c218ff3c78b26dcfaa726ee30267a6)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

删除周期性广播同步（Periodic Advertising Sync）。

<a id="r_ga4ee87bbf79e6ac844d14c3dafb2dadf4"></a>

```c
int bt_le_per_adv_sync_cb_register (struct bt_le_per_adv_sync_cb *cb)
```

相关声明：[bt_le_per_adv_sync_cb_register](#ga4ee87bbf79e6ac844d14c3dafb2dadf4)、[bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)。

注册周期性广播同步回调（Periodic Advertising Sync Callbacks）。

<a id="r_gab1576c66b08dc855b2d17fc562f36724"></a>

```c
int bt_le_per_adv_sync_cb_unregister (struct bt_le_per_adv_sync_cb *cb)
```

相关声明：[bt_le_per_adv_sync_cb_unregister](#gab1576c66b08dc855b2d17fc562f36724)、[bt_le_per_adv_sync_cb](../bluetooth_connection_model_reference/P118_bt_le_per_adv_sync_cb_结构体.md)。

注销周期性广播同步回调（Periodic Advertising Sync Callbacks）。

<a id="r_ga07e4510de7e72c6ed6196b3da9fb40be"></a>

```c
int bt_le_per_adv_sync_recv_enable (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_recv_enable](#ga07e4510de7e72c6ed6196b3da9fb40be)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

允许某个同步接收周期性广播报告（Periodic Advertising Reports）。

<a id="r_ga3dc0c6a0c6a77f4db63ee2ff8329a4c5"></a>

```c
int bt_le_per_adv_sync_recv_disable (struct bt_le_per_adv_sync *per_adv_sync)
```

相关声明：[bt_le_per_adv_sync_recv_disable](#ga3dc0c6a0c6a77f4db63ee2ff8329a4c5)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

禁止某个同步接收周期性广播报告（Periodic Advertising Reports）。

<a id="r_gaf81a1dd7a628d1a2f25c6b53b0679809"></a>

```c
int bt_le_per_adv_sync_transfer (const struct bt_le_per_adv_sync *per_adv_sync, const struct bt_conn *conn, uint16_t service_data)
```

相关声明：[bt_le_per_adv_sync_transfer](#gaf81a1dd7a628d1a2f25c6b53b0679809)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将周期性广播同步信息（Periodic Advertising Sync Information）传输给对端设备。

<a id="r_gac96199a4e5e6cfb789c1bd1c0e67d6fe"></a>

```c
int bt_le_per_adv_set_info_transfer (const struct bt_le_ext_adv *adv, const struct bt_conn *conn, uint16_t service_data)
```

相关声明：[bt_le_per_adv_set_info_transfer](#gac96199a4e5e6cfb789c1bd1c0e67d6fe)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

传输有关周期性广播集（Periodic Advertising Set）的信息。

<a id="r_gaa0658bd53df1d5e8e89e13330e4fd0ae"></a>

```c
int bt_le_per_adv_sync_transfer_subscribe (const struct bt_conn *conn, const struct bt_le_per_adv_sync_transfer_param *param)
```

相关声明：[bt_le_per_adv_sync_transfer_subscribe](#gaa0658bd53df1d5e8e89e13330e4fd0ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_per_adv_sync_transfer_param](../bluetooth_connection_model_reference/P126_bt_le_per_adv_sync_transfer_param_结构体.md)。

订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

<a id="r_ga08f872078045bbef4aca19761f25eeb8"></a>

```c
int bt_le_per_adv_sync_transfer_unsubscribe (const struct bt_conn *conn)
```

相关声明：[bt_le_per_adv_sync_transfer_unsubscribe](#ga08f872078045bbef4aca19761f25eeb8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

取消订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

<a id="r_ga27c4961f3c7270a7f1caeadb4107854b"></a>

```c
int bt_le_per_adv_list_add (const bt_addr_le_t *addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_list_add](#ga27c4961f3c7270a7f1caeadb4107854b)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向周期性广播列表（Periodic Advertising List）添加设备。

<a id="r_ga100efac4a49984e06202c63c4e5955cd"></a>

```c
int bt_le_per_adv_list_remove (const bt_addr_le_t *addr, uint8_t sid)
```

相关声明：[bt_le_per_adv_list_remove](#ga100efac4a49984e06202c63c4e5955cd)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从周期性广播列表（Periodic Advertising List）移除设备。

<a id="r_ga5909bd768c23a19a42a660e3b814c981"></a>

```c
int bt_le_per_adv_list_clear (void)
```

相关声明：[bt_le_per_adv_list_clear](#ga5909bd768c23a19a42a660e3b814c981)。

清空周期性广播列表（Periodic Advertising List）。

<a id="r_gac5e19c26b53a08dadb8efa7ecc692ad6"></a>

```c
int bt_le_scan_start (const struct bt_le_scan_param *param, bt_le_scan_cb_t cb)
```

相关声明：[bt_le_scan_start](#gac5e19c26b53a08dadb8efa7ecc692ad6)、[bt_le_scan_param](../bluetooth_connection_model_reference/P128_bt_le_scan_param_结构体.md)、[bt_le_scan_cb_t](#ga1c53d22b6e2dee38c825c58f3eeee9b4)。

启动低功耗蓝牙扫描（LE Scanning）。

<a id="r_gaa2de1a1ab523606b36a4c445fb0c3b84"></a>

```c
int bt_le_scan_stop (void)
```

相关声明：[bt_le_scan_stop](#gaa2de1a1ab523606b36a4c445fb0c3b84)。

停止低功耗蓝牙扫描（LE Scanning）。

<a id="r_ga80e870fa1de40c404c64624bef439067"></a>

```c
int bt_le_scan_cb_register (struct bt_le_scan_cb *cb)
```

相关声明：[bt_le_scan_cb_register](#ga80e870fa1de40c404c64624bef439067)、[bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)。

注册扫描器数据包回调（Scanner Packet Callbacks）。

<a id="r_gac2718f2128b3f8c79b12d760771c8378"></a>

```c
void bt_le_scan_cb_unregister (struct bt_le_scan_cb *cb)
```

相关声明：[bt_le_scan_cb_unregister](#gac2718f2128b3f8c79b12d760771c8378)、[bt_le_scan_cb](../bluetooth_connection_model_reference/P127_bt_le_scan_cb_结构体.md)。

注销扫描器数据包回调（Scanner Packet Callbacks）。

<a id="r_ga40f2f7fdb09aba3c5137f680e67792f0"></a>

```c
int bt_le_filter_accept_list_add (const bt_addr_le_t *addr)
```

相关声明：[bt_le_filter_accept_list_add](#ga40f2f7fdb09aba3c5137f680e67792f0)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

将低功耗蓝牙设备（LE Device）添加到过滤接受列表（Filter Accept List）。

<a id="r_ga0532ed768ab4f9d69c202066d2f87e66"></a>

```c
int bt_le_filter_accept_list_remove (const bt_addr_le_t *addr)
```

相关声明：[bt_le_filter_accept_list_remove](#ga0532ed768ab4f9d69c202066d2f87e66)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

从过滤接受列表（Filter Accept List）移除低功耗蓝牙设备（LE Device）。

<a id="r_gac87df899d1e363c63162988157ee6d00"></a>

```c
int bt_le_filter_accept_list_clear (void)
```

相关声明：[bt_le_filter_accept_list_clear](#gac87df899d1e363c63162988157ee6d00)。

清空过滤接受列表（Filter Accept List）。

<a id="r_gabc115fd3fff6d00ae878a31613bf70aa"></a>

```c
int bt_le_set_chan_map (uint8_t chan_map[5])
```

相关声明：[bt_le_set_chan_map](#gabc115fd3fff6d00ae878a31613bf70aa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置低功耗蓝牙信道映射（LE Channel Map）。

<a id="r_ga9ab41e118b5496c196e56b8b5d023275"></a>

```c
int bt_le_set_rpa_timeout (uint16_t new_rpa_timeout)
```

相关声明：[bt_le_set_rpa_timeout](#ga9ab41e118b5496c196e56b8b5d023275)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在运行时设置可解析私有地址（Resolvable Private Address）的超时时间。

<a id="r_ga652eef01e5256e0d820cd1f4db877429"></a>

```c
void bt_data_parse (struct net_buf_simple *ad, bool(*func)(struct bt_data *data, void *user_data), void *user_data)
```

相关声明：[bt_data_parse](#ga652eef01e5256e0d820cd1f4db877429)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)。

用于解析广播数据、扩展查询响应（EIR）数据或带外（OOB）数据的辅助函数。

<a id="r_ga296d1adf3c9ed2f2c65bb75b887d59ee"></a>

```c
int bt_le_oob_get_local (uint8_t id, struct bt_le_oob *oob)
```

相关声明：[bt_le_oob_get_local](#ga296d1adf3c9ed2f2c65bb75b887d59ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)。

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

<a id="r_ga7486aab863ca497a50dacf81657f48d4"></a>

```c
int bt_le_ext_adv_oob_get_local (struct bt_le_ext_adv *adv, struct bt_le_oob *oob)
```

相关声明：[bt_le_ext_adv_oob_get_local](#ga7486aab863ca497a50dacf81657f48d4)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_le_oob](../bluetooth_connection_model_reference/P110_bt_le_oob_结构体.md)。

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

<a id="r_gaceabbbe6e844650f791010e53c9df6a4"></a>

```c
int bt_unpair (uint8_t id, const bt_addr_le_t *addr)
```

相关声明：[bt_unpair](#gaceabbbe6e844650f791010e53c9df6a4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

清除配对信息（Pairing Information）。

<a id="r_gaad380b7f8984f8522c1b79f9bdc04905"></a>

```c
void bt_foreach_bond (uint8_t id, void(*func)(const struct bt_bond_info *info, void *user_data), void *user_data)
```

相关声明：[bt_foreach_bond](#gaad380b7f8984f8522c1b79f9bdc04905)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bond_info](../bluetooth_connection_model_reference/P001_bt_bond_info_结构体.md)。

遍历全部现有绑定（Bonds）。

<a id="r_ga5b5e51f79896d674bf6b70b2251e79d4"></a>

```c
enum bt_le_addr_res_support bt_le_bond_addr_res_support (uint8_t id, const bt_addr_le_t *peer)
```

相关声明：[bt_le_addr_res_support](#gaad0039d4b524a0eef31158dc9b24a497)、[bt_le_bond_addr_res_support](#ga5b5e51f79896d674bf6b70b2251e79d4)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

获取已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

<a id="r_ga8046c2b06d3dad0d6c8184de492517d2"></a>

```c
int bt_configure_data_path (uint8_t dir, uint8_t id, uint8_t vs_config_len, const uint8_t *vs_config)
```

相关声明：[bt_configure_data_path](#ga8046c2b06d3dad0d6c8184de492517d2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置厂商数据路径（Vendor Data Path）。

<a id="r_ga731f4b37a9e5cc13a6816ea23f751b0b"></a>

```c
int bt_le_per_adv_sync_subevent (struct bt_le_per_adv_sync *per_adv_sync, struct bt_le_per_adv_sync_subevent_params *params)
```

相关声明：[bt_le_per_adv_sync_subevent](#ga731f4b37a9e5cc13a6816ea23f751b0b)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_subevent_params](../bluetooth_connection_model_reference/P123_bt_le_per_adv_sync_subevent_params_结构体.md)。

与子事件（Subevents）的一个子集同步。

<a id="r_gaae6b8583f7d5457f20b03dccd146425e"></a>

```c
int bt_le_per_adv_set_response_data (struct bt_le_per_adv_sync *per_adv_sync, const struct bt_le_per_adv_response_params *params, const struct net_buf_simple *data)
```

相关声明：[bt_le_per_adv_set_response_data](#gaae6b8583f7d5457f20b03dccd146425e)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_response_params](../bluetooth_connection_model_reference/P115_bt_le_per_adv_response_params_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

设置带响应周期性广播（PAwR）中特定子事件的某个响应时隙（Response Slot）的数据。

<a id="r_ga309a67de79cc215db1d33251f267f361"></a>

```c
bool bt_le_bond_exists (uint8_t id, const bt_addr_le_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_le_bond_exists](#ga309a67de79cc215db1d33251f267f361)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

检查由低功耗蓝牙地址（Bluetooth LE Address）标识的设备是否已绑定（Bonded）。

<a id="r_ga9760190192dde5c498ec96628468be8d"></a>

```c
int bt_br_discovery_start (const struct bt_br_discovery_param *param, struct bt_br_discovery_result *results, size_t count)
```

相关声明：[bt_br_discovery_start](#ga9760190192dde5c498ec96628468be8d)、[bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)、[bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)。

开始 BR/EDR 发现（Discovery）。

<a id="r_ga567c71b49399fe7e1a5593edbf005e3a"></a>

```c
int bt_br_discovery_stop (void)
```

相关声明：[bt_br_discovery_stop](#ga567c71b49399fe7e1a5593edbf005e3a)。

停止 BR/EDR 发现（Discovery）。

<a id="r_ga430de0ad30da7322c5353941f1f6a133"></a>

```c
void bt_br_discovery_cb_register (struct bt_br_discovery_cb *cb)
```

相关声明：[bt_br_discovery_cb_register](#ga430de0ad30da7322c5353941f1f6a133)、[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

注册发现数据包回调（Discovery Packet Callbacks）。

<a id="r_ga25ab96ac005237aee739bf32fc1aac94"></a>

```c
void bt_br_discovery_cb_unregister (struct bt_br_discovery_cb *cb)
```

相关声明：[bt_br_discovery_cb_unregister](#ga25ab96ac005237aee739bf32fc1aac94)、[bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)。

注销发现数据包回调（Discovery Packet Callbacks）。

<a id="r_ga2ec860d06c45098624b106b59fbab634"></a>

```c
int bt_br_oob_get_local (struct bt_br_oob *oob)
```

相关声明：[bt_br_oob_get_local](#ga2ec860d06c45098624b106b59fbab634)、[bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)。

获取 BR/EDR 本地带外信息（Out Of Band Information）。

<a id="r_gae3376fdd364e9b9d6e304ec589ba00f5"></a>

```c
int bt_br_set_discoverable (bool enable, bool limited)
```

相关声明：[bt_br_set_discoverable](#gae3376fdd364e9b9d6e304ec589ba00f5)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用控制器的可发现状态（Discoverable State）。

<a id="r_ga66c29ea0ccb8b8ff5610c1fc53fe1eb9"></a>

```c
int bt_br_set_connectable (bool enable, bt_br_conn_req_func_t func)
```

相关声明：[bt_br_set_connectable](#ga66c29ea0ccb8b8ff5610c1fc53fe1eb9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_br_conn_req_func_t](#gab661e90ad27ce1a280cefc15c5ad040c)。

启用／禁用控制器的可连接状态（Connectable State）。

<a id="r_ga78c5fc5f71d08b0c800967ee7696fc83"></a>

```c
int bt_br_page_scan_update_param (const struct bt_br_page_scan_param *param)
```

相关声明：[bt_br_page_scan_update_param](#ga78c5fc5f71d08b0c800967ee7696fc83)、[bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)。

更新 BR/EDR 寻呼扫描参数（Page Scan Parameters）。

<a id="r_ga6ca71da8c9eed3d317200aa1f6babc7d"></a>

```c
int bt_br_inquiry_scan_update_param (const struct bt_br_inquiry_scan_param *param)
```

相关声明：[bt_br_inquiry_scan_update_param](#ga6ca71da8c9eed3d317200aa1f6babc7d)、[bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)。

更新 BR/EDR 查询扫描参数（Inquiry Scan Parameters）。

<a id="r_ga201f64881ccc13169d072d9cc04948ba"></a>

```c
int bt_br_set_class_of_device (uint32_t cod)
```

相关声明：[bt_br_set_class_of_device](#ga201f64881ccc13169d072d9cc04948ba)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置本地 BR/EDR 控制器的设备类别（Class of Device）。

<a id="r_gab49521adee2b653dbec04fbf833e22d9"></a>

```c
int bt_br_get_class_of_device (uint32_t *cod)
```

相关声明：[bt_br_get_class_of_device](#gab49521adee2b653dbec04fbf833e22d9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取本地 BR/EDR 控制器的设备类别（Class of Device）。

<a id="r_gad88cf1dec20264f9bdde91571efe8dce"></a>

```c
bool bt_br_bond_exists (const bt_addr_t *addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_br_bond_exists](#gad88cf1dec20264f9bdde91571efe8dce)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

检查经典蓝牙设备地址（Bluetooth Classic Device Address）是否已绑定（Bonded）。

<a id="r_gaccab07100ab64fd805fe1d468bc889ac"></a>

```c
int bt_br_unpair (const bt_addr_t *addr)
```

相关声明：[bt_br_unpair](#gaccab07100ab64fd805fe1d468bc889ac)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

清除经典蓝牙配对信息（Classic Pairing Information）。

<a id="r_ga4c82193c50c616d9319c87ebcffabe66"></a>

```c
void bt_br_foreach_bond (void(*func)(const struct bt_br_bond_info *info, void *user_data), void *user_data)
```

相关声明：[bt_br_foreach_bond](#ga4c82193c50c616d9319c87ebcffabe66)、[bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)。

遍历全部已有经典蓝牙绑定（Classic Bonds）。

<a id="r_gab28ba977a94f63476f360d358868f8f6"></a>

```c
int bt_br_write_eir (const struct bt_data *eir, size_t eir_count, bool fec_required)
```

相关声明：[bt_br_write_eir](#gab28ba977a94f63476f360d358868f8f6)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

写入扩展查询响应数据（Extended Inquiry Response Data）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.7\_预定义的 BR/EDR 寻呼扫描间隔与窗口（Defined BR/EDR Page Scan Intervals and Windows）

<a id="r_ga05ad85ffd00e23052ab5cbb6ff5ee709"></a>

```c
#define BT_BR_PAGE_SCAN_INTERVAL_R0 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_INTERVAL_R0](#ga05ad85ffd00e23052ab5cbb6ff5ee709)。

默认寻呼扫描间隔（Page Scan Interval），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga13e5b00e35b3c338c0326dbee03c9268"></a>

```c
#define BT_BR_PAGE_SCAN_WINDOW_R0 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_WINDOW_R0](#ga13e5b00e35b3c338c0326dbee03c9268)。

默认寻呼扫描窗口（Page Scan Window），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga17ea91d5b363d5dba321cc38e4283dbc"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R1 0x00a0
```

相关声明：[BT_BR_PAGE_SCAN_FAST_INTERVAL_R1](#ga17ea91d5b363d5dba321cc38e4283dbc)。

快速寻呼扫描间隔（Page Scan Interval），R1：0x00a0，即 100.0 ms，单位为 0.625 ms。

<a id="r_gaf1bfd9a2c5a846a1232520de20a326eb"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_FAST_WINDOW_R1](#gaf1bfd9a2c5a846a1232520de20a326eb)。

快速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga6c2a8ae86cb80756beee0bcbdb18c8b6"></a>

```c
#define BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1](#ga6c2a8ae86cb80756beee0bcbdb18c8b6)。

中速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_ga61c49f57aea54f455ef89de40c354cc5"></a>

```c
#define BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1](#ga61c49f57aea54f455ef89de40c354cc5)。

中速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_gaf955175076f985e932c0ab0ed9e58743"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1 0x0800
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1](#gaf955175076f985e932c0ab0ed9e58743)。

慢速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="r_gaf26216f17eb0142791decac9377538f4"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R1 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_WINDOW_R1](#gaf26216f17eb0142791decac9377538f4)。

慢速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_gadd743fae64449eaf337566a19e06fc6d"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R2 0x1000
```

相关声明：[BT_BR_PAGE_SCAN_FAST_INTERVAL_R2](#gadd743fae64449eaf337566a19e06fc6d)。

快速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga1bd5dcfa2c47bacca1bdaee493d261c4"></a>

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R2 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_FAST_WINDOW_R2](#ga1bd5dcfa2c47bacca1bdaee493d261c4)。

快速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="r_ga365abe1219cb283880f93de9b7f2e3d3"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2 0x1000
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2](#ga365abe1219cb283880f93de9b7f2e3d3)。

慢速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga440177ed725266616455bd135f414ea8"></a>

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R2 0x0011
```

相关声明：[BT_BR_PAGE_SCAN_SLOW_WINDOW_R2](#ga440177ed725266616455bd135f414ea8)。

慢速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

## 1.8\_预定义的 BR 查询扫描间隔与窗口（Defined BR Inquiry Scan Intervals and Windows）

<a id="r_ga1770fa93707cf5ea6b57498be1aa9b26"></a>

```c
#define BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT 0x1000
```

相关声明：[BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT](#ga1770fa93707cf5ea6b57498be1aa9b26)。

默认查询扫描间隔（Inquiry Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="r_ga6bc842be90369deb05fb4720ced19395"></a>

```c
#define BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT 0x0012
```

相关声明：[BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT](#ga6bc842be90369deb05fb4720ced19395)。

默认查询扫描窗口（Inquiry Scan Window）：0x0012，即 11.25 ms，单位为 0.625 ms。

## 1.9\_详细说明（Detailed Documentation）

<a id="ga925f510c862c9a36539f4df1db0009d6"></a>

### `BT_BR_EIR_SIZE_MAX`

```c
#define BT_BR_EIR_SIZE_MAX 240
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

扩展查询响应（Extended Inquiry Response）的最大大小。

<a id="ga1770fa93707cf5ea6b57498be1aa9b26"></a>

### `BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT`

```c
#define BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT 0x1000
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

默认查询扫描间隔（Inquiry Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="ga7a9e4560e84fa43e7c1f3cad39bdf24e"></a>

### `BT_BR_INQUIRY_SCAN_PARAM`

```c
#define BT_BR_INQUIRY_SCAN_PARAM ( _interval, _window, _type )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
((const struct bt_br_inquiry_scan_param[]){BT_BR_SCAN_INIT(_interval, _window, _type)})
```

用于内联声明 BR/EDR 查询扫描参数（Inquiry Scan Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 查询扫描间隔（Inquiry Scan Interval），单位为 N × 0.625 毫秒。 |
| `_window` | 查询扫描窗口（Inquiry Scan Window），单位为 N × 0.625 毫秒。 |
| `_type` | `BT_BR_SCAN_TYPE_STANDARD` 或 `BT_BR_SCAN_TYPE_INTERLACED`。 |

<a id="gabe6aa0d2210ab0507d3b06bfd7000aaa"></a>

### `BT_BR_INQUIRY_SCAN_PARAM_DEFAULT`

```c
#define BT_BR_INQUIRY_SCAN_PARAM_DEFAULT
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_INQUIRY_SCAN_PARAM(BT_BR_INQUIRY_SCAN_INTERVAL_DEFAULT,                              \
                         BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT, BT_BR_SCAN_TYPE_STANDARD)
```

默认查询扫描参数（Default Inquiry Scan Parameters）。

查询扫描间隔设为 2.560 秒，以 0.625 毫秒为单位时为 `0x1000`；查询扫描窗口设为 11.25 毫秒，以 0.625 毫秒为单位时为 `0x0012`。扫描类型设为标准扫描（Standard）。

<a id="ga6bc842be90369deb05fb4720ced19395"></a>

### `BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT`

```c
#define BT_BR_INQUIRY_SCAN_WINDOW_DEFAULT 0x0012
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

默认查询扫描窗口（Inquiry Scan Window）：0x0012，即 11.25 ms，单位为 0.625 ms。

<a id="ga17ea91d5b363d5dba321cc38e4283dbc"></a>

### `BT_BR_PAGE_SCAN_FAST_INTERVAL_R1`

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R1 0x00a0
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

快速寻呼扫描间隔（Page Scan Interval），R1：0x00a0，即 100.0 ms，单位为 0.625 ms。

<a id="gadd743fae64449eaf337566a19e06fc6d"></a>

### `BT_BR_PAGE_SCAN_FAST_INTERVAL_R2`

```c
#define BT_BR_PAGE_SCAN_FAST_INTERVAL_R2 0x1000
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

快速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="gaf1bfd9a2c5a846a1232520de20a326eb"></a>

### `BT_BR_PAGE_SCAN_FAST_WINDOW_R1`

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R1 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

快速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="ga1bd5dcfa2c47bacca1bdaee493d261c4"></a>

### `BT_BR_PAGE_SCAN_FAST_WINDOW_R2`

```c
#define BT_BR_PAGE_SCAN_FAST_WINDOW_R2 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

快速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="ga05ad85ffd00e23052ab5cbb6ff5ee709"></a>

### `BT_BR_PAGE_SCAN_INTERVAL_R0`

```c
#define BT_BR_PAGE_SCAN_INTERVAL_R0 0x0800
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

默认寻呼扫描间隔（Page Scan Interval），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="ga6c2a8ae86cb80756beee0bcbdb18c8b6"></a>

### `BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1`

```c
#define BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1 0x0800
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

中速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="ga61c49f57aea54f455ef89de40c354cc5"></a>

### `BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1`

```c
#define BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

中速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="ga4d053fafbc0faed58c3305efdd581838"></a>

### `BT_BR_PAGE_SCAN_PARAM`

```c
#define BT_BR_PAGE_SCAN_PARAM ( _interval, _window, _type )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
((const struct bt_br_page_scan_param[]) { \
        BT_BR_SCAN_INIT(_interval, _window, _type) \
})
```

用于内联声明 BR/EDR 寻呼扫描参数（Page Scan Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 寻呼扫描间隔（Page Scan Interval），单位为 N × 0.625 毫秒。 |
| `_window` | 寻呼扫描窗口（Page Scan Window），单位为 N × 0.625 毫秒。 |
| `_type` | `BT_BR_SCAN_TYPE_STANDARD` 或 `BT_BR_SCAN_TYPE_INTERLACED`。 |

<a id="ga9f20d66911eaedeb26c93281e21febb6"></a>

### `BT_BR_PAGE_SCAN_PARAM_FAST_R1`

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R1
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM(BT_BR_PAGE_SCAN_FAST_INTERVAL_R1, \
BT_BR_PAGE_SCAN_FAST_WINDOW_R1, \
BT_BR_SCAN_TYPE_INTERLACED)
```

R1 的快速寻呼扫描参数（Fast Page Scan Parameters）。

寻呼扫描间隔设为 100 毫秒，以 0.625 毫秒为单位时为 `0x00A0`；寻呼扫描窗口设为 10.625 毫秒，以 0.625 毫秒为单位时为 `0x0011`。扫描类型设为交错扫描（Interlaced）。

<a id="gab0bcacaa4d7ddfe85918ed26b7525eb7"></a>

### `BT_BR_PAGE_SCAN_PARAM_FAST_R2`

```c
#define BT_BR_PAGE_SCAN_PARAM_FAST_R2
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM( \
BT_BR_PAGE_SCAN_FAST_INTERVAL_R2, \
BT_BR_PAGE_SCAN_FAST_WINDOW_R2, \
BT_BR_SCAN_TYPE_INTERLACED)
```

R2 的快速寻呼扫描参数（Fast Page Scan Parameters）。

寻呼扫描间隔设为 2.560 秒，以 0.625 毫秒为单位时为 `0x1000`；寻呼扫描窗口设为 10.625 毫秒，以 0.625 毫秒为单位时为 `0x0011`。扫描类型设为交错扫描（Interlaced）。

<a id="ga6c58418072c3cb5cc35193414a20f98f"></a>

### `BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1`

```c
#define BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM( \
BT_BR_PAGE_SCAN_MEDIUM_INTERVAL_R1, \
BT_BR_PAGE_SCAN_MEDIUM_WINDOW_R1, \
BT_BR_SCAN_TYPE_INTERLACED)
```

R1 的中速寻呼扫描参数（Medium Page Scan Parameters）。

寻呼扫描间隔设为 1.280 秒，以 0.625 毫秒为单位时为 `0x0800`；寻呼扫描窗口设为 10.625 毫秒，以 0.625 毫秒为单位时为 `0x0011`。扫描类型设为交错扫描（Interlaced）。

<a id="ga8c22bfb02c45f522794e6e3f0054ffa0"></a>

### `BT_BR_PAGE_SCAN_PARAM_R0`

```c
#define BT_BR_PAGE_SCAN_PARAM_R0
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM(BT_BR_PAGE_SCAN_INTERVAL_R0, \
BT_BR_PAGE_SCAN_WINDOW_R0, \
BT_BR_SCAN_TYPE_STANDARD)
```

R0 的默认寻呼扫描参数（Default Page Scan Parameters）。

寻呼扫描间隔和窗口均设为 1.280 秒，以 0.625 毫秒为单位时为 `0x0800`。扫描类型设为标准扫描（Standard）。

<a id="gae2641df344fc7bd32ad0ed7c185538a7"></a>

### `BT_BR_PAGE_SCAN_PARAM_SLOW_R1`

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R1
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM( \
BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1, \
BT_BR_PAGE_SCAN_SLOW_WINDOW_R1, \
BT_BR_SCAN_TYPE_STANDARD)
```

R1 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

寻呼扫描间隔设为 1.280 秒，以 0.625 毫秒为单位时为 `0x0800`；寻呼扫描窗口设为 10.625 毫秒，以 0.625 毫秒为单位时为 `0x0011`。扫描类型设为标准扫描（Standard）。

<a id="ga1558b2c9183c631cd8a7fa0988598184"></a>

### `BT_BR_PAGE_SCAN_PARAM_SLOW_R2`

```c
#define BT_BR_PAGE_SCAN_PARAM_SLOW_R2
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
BT_BR_PAGE_SCAN_PARAM( \
BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2, \
BT_BR_PAGE_SCAN_SLOW_WINDOW_R2, \
BT_BR_SCAN_TYPE_STANDARD)
```

R2 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

寻呼扫描间隔设为 2.560 秒，以 0.625 毫秒为单位时为 `0x1000`；寻呼扫描窗口设为 10.625 毫秒，以 0.625 毫秒为单位时为 `0x0011`。扫描类型设为标准扫描（Standard）。

<a id="gaf955175076f985e932c0ab0ed9e58743"></a>

### `BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1`

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R1 0x0800
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

慢速寻呼扫描间隔（Page Scan Interval），R1：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="ga365abe1219cb283880f93de9b7f2e3d3"></a>

### `BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2`

```c
#define BT_BR_PAGE_SCAN_SLOW_INTERVAL_R2 0x1000
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

慢速寻呼扫描间隔（Page Scan Interval），R2：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="gaf26216f17eb0142791decac9377538f4"></a>

### `BT_BR_PAGE_SCAN_SLOW_WINDOW_R1`

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R1 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

慢速寻呼扫描窗口（Page Scan Window），R1：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="ga440177ed725266616455bd135f414ea8"></a>

### `BT_BR_PAGE_SCAN_SLOW_WINDOW_R2`

```c
#define BT_BR_PAGE_SCAN_SLOW_WINDOW_R2 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

慢速寻呼扫描窗口（Page Scan Window），R2：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="ga13e5b00e35b3c338c0326dbee03c9268"></a>

### `BT_BR_PAGE_SCAN_WINDOW_R0`

```c
#define BT_BR_PAGE_SCAN_WINDOW_R0 0x0800
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

默认寻呼扫描窗口（Page Scan Window），R0：0x0800，即 1.280 s，单位为 0.625 ms。

<a id="gaff027ae0fe3fbac63db9c87f8e480214"></a>

### `BT_BR_SCAN_INIT`

```c
#define BT_BR_SCAN_INIT ( _interval, _window, _type )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

展开值（Value）：

```c
{ \
        .interval = (_interval), \
        .window = (_window), \
        .type = (_type) \
}
```

初始化基本速率扫描参数（BR Scan Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_interval` | 扫描间隔（Scan Interval）。 |
| `_window` | 扫描窗口（Scan Window）。 |
| `_type` | 扫描类型（Scan type）。 |

<a id="ga03ede7b8791a42172f28882f9da8f52e"></a>

### `BT_BR_SCAN_INTERVAL_MAX`

```c
#define BT_BR_SCAN_INTERVAL_MAX 0x1000
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

BR/EDR 最大扫描间隔（Scan Interval）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="gada5bcc61877ac75849dc3c2867ad2505"></a>

### `BT_BR_SCAN_INTERVAL_MIN`

```c
#define BT_BR_SCAN_INTERVAL_MIN 0x0012
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

BR/EDR 最小扫描间隔（Scan Interval）：0x0012，即 11.25 ms，单位为 0.625 ms。

<a id="ga1b29c1de2a023f5b892939cda856f491"></a>

### `BT_BR_SCAN_WINDOW_MAX`

```c
#define BT_BR_SCAN_WINDOW_MAX 0x1000
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

BR/EDR 最大扫描窗口（Scan Window）：0x1000，即 2.560 s，单位为 0.625 ms。

<a id="gac69aaf3d5de86a2ba1ab7a7194256c79"></a>

### `BT_BR_SCAN_WINDOW_MIN`

```c
#define BT_BR_SCAN_WINDOW_MIN 0x0011
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

BR/EDR 最小扫描窗口（Scan Window）：0x0011，即 10.625 ms，单位为 0.625 ms。

<a id="gaded4b52c9bb87fd4d19b1eb9361973e5"></a>

### `BT_ID_DEFAULT`

```c
#define BT_ID_DEFAULT 0
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

引用第一个身份地址（Identity Address）的身份句柄（Identity Handle）。

这是用于指定默认身份地址（Identity Address）的便捷宏，有助于提高代码可读性，尤其适用于仅支持一个身份地址的情况。

<a id="ga17419cd0fcc4660f09ac5dbad3a042f2"></a>

### `BT_IRK_SIZE`

```c
#define BT_IRK_SIZE 16U
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

身份解析密钥（Identity Resolving Key）的大小，单位为八位字节。

<a id="ga1f5edc3c4cbead62e32cef8cc7b83725"></a>

### `BT_LE_ADV_CONN_DIR`

```c
#define BT_LE_ADV_CONN_DIR ( _peer)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, 0, 0, _peer)
```

<a id="gab89e033ed3fd116c94120d177dfdc839"></a>

### `BT_LE_ADV_CONN_DIR_LOW_DUTY`

```c
#define BT_LE_ADV_CONN_DIR_LOW_DUTY ( _peer)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN | BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY,                      \
                BT_GAP_ADV_FAST_INT_MIN_2, BT_GAP_ADV_FAST_INT_MAX_2, _peer)
```

<a id="gaa700527b1caf3bef27d96a3f91a29f69"></a>

### `BT_LE_ADV_CONN_FAST_1`

```c
#define BT_LE_ADV_CONN_FAST_1
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_1, BT_GAP_ADV_FAST_INT_MAX_1,  \
                NULL)
```

通用访问配置文件（GAP）推荐的、由使用者发起的可连接广播参数（Connectable Advertising Parameters）。

此定义设置推荐的默认参数，适用于应用很可能正在等待设备被连接或被发现的情况。

对于用户发起的广播，GAP 建议广播者使用 `BT_LE_ADV_CONN_FAST_1` 设置的广播参数。这可能包括用户与设备进行的任何交互、按下专用蓝牙唤醒按钮，或介于两者之间的操作；具体解释由应用开发者决定。

这些参数设置考虑了以下模式：

- 非定向可连接模式（Undirected Connectable Mode）。
- 有限可发现模式（Limited Discoverable Mode），并发送可连接的非定向广播事件。
- 通用可发现模式（General Discoverable Mode），并发送可连接的非定向广播事件。
- 定向可连接模式（Directed Connectable Mode），并发送低占空比定向广播事件。

参见《蓝牙核心规范》（Bluetooth Core Specification）：

- 6.0 版，第 3 卷，C 部分，附录 A“计时器与常量”（Timers and Constants），`T_GAP(adv_fast_interval1)`。
- 6.0 版，第 3 卷，C 部分，第 9.3.11 节“连接建立定时参数”（Connection Establishment Timing Parameters）。

**说明（Note）**：注意：这些参数仅为建议。例如，应用可以使用较长的间隔节省电池电量，但会牺牲响应速度；应考虑仅在超时后，才进入间隔更长的低功耗状态。这是有限可发现模式（Limited Discoverable Mode）的推荐设置。

<a id="ga684a1110a8973bc17211f6f0824beccd"></a>

### `BT_LE_ADV_CONN_FAST_2`

```c
#define BT_LE_ADV_CONN_FAST_2
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_2, BT_GAP_ADV_FAST_INT_MAX_2,  \
                NULL)
```

GAP 推荐的可连接广播参数，用于不可连接广播事件（Non-connectable Advertising Events）。（原文同时使用 connectable 与 non-connectable，保留其表述。）

此定义为用户发起的广播或发送不可连接广播事件设置推荐的默认参数。

这些参数设置考虑了以下模式：

- 不可发现模式（Non-Discoverable Mode）。
- 不可连接模式（Non-Connectable Mode）。
- 有限可发现模式（Limited Discoverable Mode）。
- 通用可发现模式（General Discoverable Mode）。

参见《蓝牙核心规范》（Bluetooth Core Specification）：

- 6.0 版，第 3 卷，C 部分，附录 A“计时器与常量”（Timers and Constants），`T_GAP(adv_fast_interval2)`。
- 6.0 版，第 3 卷，C 部分，第 9.3.11 节“连接建立定时参数”（Connection Establishment Timing Parameters）。

<a id="ga1610555bf59f1d691d640f245957fdce"></a>

### `BT_LE_ADV_NCONN`

```c
#define BT_LE_ADV_NCONN
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(0, BT_GAP_ADV_FAST_INT_MIN_2, \
BT_GAP_ADV_FAST_INT_MAX_2, NULL)
```

使用私有地址（Private Address）的不可连接广播（Non-connectable Advertising）。

<a id="ga6ef9fb7a469b03265c7adc99ea19a11b"></a>

### `BT_LE_ADV_NCONN_IDENTITY`

```c
#define BT_LE_ADV_NCONN_IDENTITY
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_USE_IDENTITY, \
BT_GAP_ADV_FAST_INT_MIN_2, \
BT_GAP_ADV_FAST_INT_MAX_2, \
NULL)
```

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接广播（Non-connectable Advertising）。

<a id="ga9557269dd36b624b49e76c511c3a0cc1"></a>

### `BT_LE_ADV_PARAM`

```c
#define BT_LE_ADV_PARAM ( _options, _int_min, _int_max, _peer )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
((const struct bt_le_adv_param[]) { \
        BT_LE_ADV_PARAM_INIT(_options, _int_min, _int_max, _peer) \
 })
```

用于内联声明广播参数（Advertising Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_options` | 广播选项（Advertising Options）。 |
| `_int_min` | 最小广播间隔（Minimum Advertising Interval）。 |
| `_int_max` | 最大广播间隔（Maximum Advertising Interval）。 |
| `_peer` | 对端地址。非定向广播（Undirected Advertising）时设为 `NULL`，定向广播（Directed Advertising）时设为对端地址。 |

<a id="ga71555b857cf8c2a47c36e4dafa7accf4"></a>

### `BT_LE_ADV_PARAM_INIT`

```c
#define BT_LE_ADV_PARAM_INIT ( _options, _int_min, _int_max, _peer )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
{ \
        .id = BT_ID_DEFAULT, \
        .sid = 0, \
        .secondary_max_skip = 0, \
        .options = (_options), \
        .interval_min = (_int_min), \
        .interval_max = (_int_max), \
        .peer = (_peer), \
}
```

初始化广播参数（Advertising Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_options` | 广播选项（Advertising Options）。 |
| `_int_min` | 最小广播间隔（Minimum Advertising Interval）。 |
| `_int_max` | 最大广播间隔（Maximum Advertising Interval）。 |
| `_peer` | 对端地址。非定向广播（Undirected Advertising）时设为 `NULL`，定向广播（Directed Advertising）时设为对端地址。 |

<a id="ga0e911d3aafdd0c926590b3272a3da564"></a>

### `BT_LE_EXT_ADV_CODED_NCONN`

```c
#define BT_LE_EXT_ADV_CODED_NCONN
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
BT_LE_ADV_OPT_CODED, \
BT_GAP_ADV_FAST_INT_MIN_2, \
BT_GAP_ADV_FAST_INT_MAX_2, \
NULL)
```

在编码物理层（Coded PHY）上使用私有地址的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="gac67c52693154ebbeedbb31e100513812"></a>

### `BT_LE_EXT_ADV_CODED_NCONN_IDENTITY`

```c
#define BT_LE_EXT_ADV_CODED_NCONN_IDENTITY
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | BT_LE_ADV_OPT_CODED | \
                BT_LE_ADV_OPT_USE_IDENTITY, \
                BT_GAP_ADV_FAST_INT_MIN_2, \
                BT_GAP_ADV_FAST_INT_MAX_2, NULL)
```

在编码物理层（Coded PHY）上使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="gaeaaef4dede5d45251dfe12f329e070b7"></a>

### `BT_LE_EXT_ADV_CONN`

```c
#define BT_LE_EXT_ADV_CONN
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | BT_LE_ADV_OPT_CONN, BT_GAP_ADV_FAST_INT_MIN_2,     \
                BT_GAP_ADV_FAST_INT_MAX_2, NULL)
```

可连接的扩展广播（Connectable Extended Advertising）。

<a id="gaabc0385f6a5307b48ec43af6aae7dea6"></a>

### `BT_LE_EXT_ADV_NCONN`

```c
#define BT_LE_EXT_ADV_NCONN
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV, \
BT_GAP_ADV_FAST_INT_MIN_2, \
BT_GAP_ADV_FAST_INT_MAX_2, NULL)
```

使用私有地址（Private Address）的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="ga7e46a64af0036c433c2e940ce7db0a05"></a>

### `BT_LE_EXT_ADV_NCONN_IDENTITY`

```c
#define BT_LE_EXT_ADV_NCONN_IDENTITY
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
                BT_LE_ADV_OPT_USE_IDENTITY, \
                BT_GAP_ADV_FAST_INT_MIN_2, \
                BT_GAP_ADV_FAST_INT_MAX_2, NULL)
```

使用 BT_LE_ADV_OPT_USE_IDENTITY 的不可连接扩展广播（Non-connectable Extended Advertising）。

<a id="ga5dd57fc7f0e213db08655e631a2f314e"></a>

### `BT_LE_EXT_ADV_SCAN`

```c
#define BT_LE_EXT_ADV_SCAN
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_ADV_PARAM(BT_LE_ADV_OPT_EXT_ADV | \
BT_LE_ADV_OPT_SCANNABLE, \
BT_GAP_ADV_FAST_INT_MIN_2, \
BT_GAP_ADV_FAST_INT_MAX_2, \
NULL)
```

可扫描的扩展广播（Scannable Extended Advertising）。

<a id="ga8c83a6f322a479bc24a576a7f091312e"></a>

### `BT_LE_EXT_ADV_START_DEFAULT`

```c
#define BT_LE_EXT_ADV_START_DEFAULT BT_LE_EXT_ADV_START_PARAM(0, 0)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="ga9b2cefbcb0a85116cadb68f6d80c6429"></a>

### `BT_LE_EXT_ADV_START_PARAM`

```c
#define BT_LE_EXT_ADV_START_PARAM ( _timeout, _n_evts )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
((const struct bt_le_ext_adv_start_param[]) { \
        BT_LE_EXT_ADV_START_PARAM_INIT((_timeout), (_n_evts)) \
})
```

用于内联声明扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_timeout` | 广播者超时时间（Advertiser Timeout）。 |
| `_n_evts` | 广播事件数量（Number of Advertising Events）。 |

<a id="gaf0d4c5b05deb5466a0e29c153263b489"></a>

### `BT_LE_EXT_ADV_START_PARAM_INIT`

```c
#define BT_LE_EXT_ADV_START_PARAM_INIT ( _timeout, _n_evts )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
{ \
        .timeout = (_timeout), \
        .num_events = (_n_evts), \
}
```

用于内联初始化扩展广播启动参数（Extended Advertising Start Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_timeout` | 广播者超时时间（Advertiser Timeout）。 |
| `_n_evts` | 广播事件数量（Number of Advertising Events）。 |

<a id="gaa26f90b188caa50ca12247b7911a0a5f"></a>

### `BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE`

```c
#define BT_LE_LOCAL_SUPPORTED_FEATURES_SIZE BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

本地支持特性（Local Supported Features）的八位字节数。

数值 8 对应 LE 控制器支持特性的第 0 页。后续所有支持特性页均需要 24 字节。

<a id="ga8f6a00faaaab2a91ac943c71ed041ac1"></a>

### `BT_LE_PER_ADV_DEFAULT`

```c
#define BT_LE_PER_ADV_DEFAULT
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_PER_ADV_PARAM(BT_GAP_PER_ADV_SLOW_INT_MIN, \
BT_GAP_PER_ADV_SLOW_INT_MAX, \
BT_LE_PER_ADV_OPT_NONE)
```

<a id="gaf46e54f8fcda7b65b659685bb225d243"></a>

### `BT_LE_PER_ADV_PARAM`

```c
#define BT_LE_PER_ADV_PARAM ( _int_min, _int_max, _options )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
((struct bt_le_per_adv_param[]) { \
        BT_LE_PER_ADV_PARAM_INIT(_int_min, _int_max, _options) \
})
```

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_int_min` | 最小周期广播间隔（Minimum Periodic Advertising Interval），单位为 N × 1.25 毫秒。 |
| `_int_max` | 最大周期广播间隔（Maximum Periodic Advertising Interval），单位为 N × 1.25 毫秒。 |
| `_options` | 周期广播属性位域（Periodic Advertising Properties Bitfield），参见 `bt_le_adv_opt` 字段。 |

<a id="ga880567278a81098ae55f52f624c61041"></a>

### `BT_LE_PER_ADV_PARAM_INIT`

```c
#define BT_LE_PER_ADV_PARAM_INIT ( _int_min, _int_max, _options )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
{ \
        .interval_min = (_int_min), \
        .interval_max = (_int_max), \
        .options = (_options), \
}
```

用于内联声明周期性广播参数（Periodic Advertising Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_int_min` | 最小周期广播间隔（Minimum Periodic Advertising Interval），单位为 N × 1.25 毫秒。 |
| `_int_max` | 最大周期广播间隔（Maximum Periodic Advertising Interval），单位为 N × 1.25 毫秒。 |
| `_options` | 周期广播属性位域（Periodic Advertising Properties Bitfield），参见 `bt_le_adv_opt` 字段。 |

<a id="gac137ea4ce32697582a337116ffa41da5"></a>

### `BT_LE_SCAN_ACTIVE`

```c
#define BT_LE_SCAN_ACTIVE
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
BT_GAP_SCAN_FAST_INTERVAL, \
BT_GAP_SCAN_FAST_WINDOW)
```

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

<a id="ga9bd9701db0459c066ed7c18343f60911"></a>

### `BT_LE_SCAN_ACTIVE_CONTINUOUS`

```c
#define BT_LE_SCAN_ACTIVE_CONTINUOUS
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
BT_GAP_SCAN_FAST_INTERVAL_MIN, \
BT_GAP_SCAN_FAST_WINDOW)
```

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏，其中 window == interval。

应使用连续扫描（Continuous Scanning），以尽可能提高接收到广播包的机会。

<a id="ga06380c4ae6289c704a143b9d192bc35f"></a>

### `BT_LE_SCAN_CODED_ACTIVE`

```c
#define BT_LE_SCAN_CODED_ACTIVE
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_ACTIVE, \
                 BT_LE_SCAN_OPT_CODED | \
                 BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                 BT_GAP_SCAN_FAST_INTERVAL, \
                 BT_GAP_SCAN_FAST_WINDOW)
```

用于启用主动扫描（Active Scanning）以发现新设备的辅助宏。

除 1M PHY 外，还包含编码物理层（Coded PHY）扫描。

<a id="ga1e5a4589304babc6b0d49019ebcff6b0"></a>

### `BT_LE_SCAN_CODED_PASSIVE`

```c
#define BT_LE_SCAN_CODED_PASSIVE
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
                 BT_LE_SCAN_OPT_CODED | \
                 BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
                 BT_GAP_SCAN_FAST_INTERVAL, \
                 BT_GAP_SCAN_FAST_WINDOW)
```

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

除 1M PHY 外，还包含编码物理层（Coded PHY）扫描。

如果已知设备识别所需的信息（例如 UUID）位于广播数据（Advertising Data）中，应使用此宏。

<a id="ga57ace75133343ba8de7fa965f452ee3d"></a>

### `BT_LE_SCAN_PARAM`

```c
#define BT_LE_SCAN_PARAM ( _type, _options, _interval, _window )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
((struct bt_le_scan_param[]) { \
        BT_LE_SCAN_PARAM_INIT(_type, _options, _interval, _window) \
 })
```

用于内联声明扫描参数（Scan Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 扫描类型，取值为 `BT_LE_SCAN_TYPE_ACTIVE` 或 `BT_LE_SCAN_TYPE_PASSIVE`。 |
| `_options` | 扫描选项（Scan Options）。 |
| `_interval` | 扫描间隔（Scan Interval），单位为 N × 0.625 毫秒。 |
| `_window` | 扫描窗口（Scan Window），单位为 N × 0.625 毫秒。 |

<a id="gac9f372ca16afb1c2f0e100c5b1b94cd5"></a>

### `BT_LE_SCAN_PARAM_INIT`

```c
#define BT_LE_SCAN_PARAM_INIT ( _type, _options, _interval, _window )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
{ \
        .type = (_type), \
        .options = (_options), \
        .interval = (_interval), \
        .window = (_window), \
        .timeout = 0, \
        .interval_coded = 0, \
        .window_coded = 0, \
}
```

初始化扫描参数（Scan Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_type` | 扫描类型，取值为 `BT_LE_SCAN_TYPE_ACTIVE` 或 `BT_LE_SCAN_TYPE_PASSIVE`。 |
| `_options` | 扫描选项（Scan Options）。 |
| `_interval` | 扫描间隔（Scan Interval），单位为 N × 0.625 毫秒。 |
| `_window` | 扫描窗口（Scan Window），单位为 N × 0.625 毫秒。 |

<a id="ga8ceaef6f0fbf4fe2d76d47e8f59aeb11"></a>

### `BT_LE_SCAN_PASSIVE`

```c
#define BT_LE_SCAN_PASSIVE
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
BT_GAP_SCAN_FAST_INTERVAL, \
BT_GAP_SCAN_FAST_WINDOW)
```

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏。

如果已知设备识别所需的信息（例如 UUID）位于广播数据（Advertising Data）中，应使用此宏。

<a id="ga8d8ccc9ea1db2c96deae1603ec1c78a3"></a>

### `BT_LE_SCAN_PASSIVE_CONTINUOUS`

```c
#define BT_LE_SCAN_PASSIVE_CONTINUOUS
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

展开值（Value）：

```c
BT_LE_SCAN_PARAM(BT_LE_SCAN_TYPE_PASSIVE, \
BT_LE_SCAN_OPT_FILTER_DUPLICATE, \
BT_GAP_SCAN_FAST_INTERVAL_MIN, \
BT_GAP_SCAN_FAST_WINDOW)
```

用于启用被动扫描（Passive Scanning）以发现新设备的辅助宏，其中 window == interval。

如果已知设备识别所需的信息（例如 UUID）位于广播数据（Advertising Data）中，应使用此宏。

<a id="gab661e90ad27ce1a280cefc15c5ad040c"></a>

### `bt_br_conn_req_func_t`

```c
typedef enum bt_br_conn_req_rsp(* bt_br_conn_req_func_t) (const bt_addr_t *addr, uint32_t cod)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

传入 BR/EDR 连接请求（Incoming Connection Requests）的回调类型。

当远端经典蓝牙（Bluetooth Classic）设备尝试与本地控制器建立连接时，调用此回调。应用必须返回响应码以接受或拒绝连接；接受时还必须指定所需角色。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 尝试发起连接的远端设备地址。 |
| `cod` | 远端设备的设备类别（Class of Device）。 |

**返回（Returns）**：返回值：`bt_br_conn_req_rsp` 响应码，指示接受还是拒绝连接，并在接受时指示所需角色。

<a id="ga1c53d22b6e2dee38c825c58f3eeee9b4"></a>

### `bt_le_scan_cb_t`

```c
typedef void bt_le_scan_cb_t(const bt_addr_le_t *addr, int8_t rssi, uint8_t adv_type, struct net_buf_simple *buf)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

报告低功耗蓝牙（LE）扫描结果的回调类型（Callback Type）。

此类型的函数传给 `bt_le_scan_start`；每发现一个 LE 设备，都会调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 广播器的低功耗地址及类型（Advertiser LE address and type）。 |
| `rssi` | 广播者的信号强度，单位为 dBm，范围为 -127 至 +20。数值不可用时，可设为 `BT_GAP_RSSI_INVALID`。 |
| `adv_type` | 广播者发出的广播响应类型，使用 `bt_gap_adv_type` 中的值。 |
| `buf` | 包含广播数据（Advertiser data）的缓冲区。 |

<a id="ga5398783ab4a5dc854b18e37fb10774eb"></a>

### `bt_ready_cb_t`

```c
typedef void(* bt_ready_cb_t) (int err)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

通知蓝牙（Bluetooth）已启用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时返回零，否则返回负错误码。 |

<a id="gabfc34fe6f398d6526acc7c5afde8a689"></a>

### `bt_br_conn_req_rsp`

```c
enum bt_br_conn_req_rsp
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

BR/EDR 连接请求响应码（Connection Request Response Codes）。

传入 BR/EDR 连接请求的响应码，连接请求回调用它来接受或拒绝连接。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BR_CONN_REQ_ACCEPT_CENTRAL` | 以中心设备（Central）角色接受连接。 |
| `BT_BR_CONN_REQ_ACCEPT_PERIPHERAL` | 以外设（Peripheral）角色接受连接。 |
| `BT_BR_CONN_REQ_REJECT_NO_RESOURCES` | 由于资源不足而拒绝连接。 |
| `BT_BR_CONN_REQ_REJECT_SECURITY` | 由于安全性不足而拒绝连接。 |
| `BT_BR_CONN_REQ_REJECT_ADDR` | 由于设备地址不可接受而拒绝连接。 |

<a id="ga03757f934de6f13f95f02316b098875d"></a>

### `bt_br_scan_type`

```c
enum bt_br_scan_type
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

寻呼扫描类型（Page Scan Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BR_SCAN_TYPE_STANDARD` | 标准扫描（Standard Scan），默认值。 |
| `BT_BR_SCAN_TYPE_INTERLACED` | 交错扫描（Interlaced Scan），仅限 1.2 设备。 |

<a id="gaad0039d4b524a0eef31158dc9b24a497"></a>

### `bt_le_addr_res_support`

```c
enum bt_le_addr_res_support
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_ADDR_RES_SUPPORT_UNKNOWN` | 尚未询问对端，或者无法读取其回答。 |
| `BT_LE_ADDR_RES_SUPPORT_NO` | 对端不支持地址解析（Address Resolution）。 |
| `BT_LE_ADDR_RES_SUPPORT_YES` | 对端支持地址解析（Address Resolution）。支持情况是一项静态能力，并不保证对端在任何给定时刻都已启用地址解析。 |

<a id="gafbf81dab68b0e484d4742471c722fc28"></a>

### `bt_le_adv_opt`

```c
enum bt_le_adv_opt
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

广播选项（Advertising Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_ADV_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_LE_ADV_OPT_CONN` | 可连接广播（Connectable Advertising）。启动时预先分配一个连接对象，分配失败则 API 返回 `-ENOMEM`。停止可连接广播会释放该对象，并触发 `bt_conn_cb::recycled`。广播集创建连接后立即停止，此操作由控制器自动执行。注意：若要在建立连接后继续广播，应用应监听 `bt_conn_cb::connected` 事件并重新启动广播集。所有连接对象都在使用时，无法启动广播者；此时应延迟到 `bt_conn_cb::recycled` 再启动。若要在断开连接后继续广播，应监听 `bt_conn_cb::recycled`。 |
| `BT_LE_ADV_OPT_USE_IDENTITY` | 使用身份地址（Identity Address）进行广播，即将身份地址用作广播者地址。警告：这会损害设备隐私，因此使用本选项时必须谨慎。注意：广播所用地址与 `bt_le_oob_get_local` 返回的地址不同，应使用 `bt_id_get` 获取 LE 地址。 |
| `BT_LE_ADV_OPT_DIR_MODE_LOW_DUTY` | 低占空比定向广播（Low Duty Cycle Directed Advertising）。使用低占空比定向广播模式，否则使用高占空比模式。 |
| `BT_LE_ADV_OPT_DIR_ADDR_RPA` | 向启用了隐私功能的对端进行定向广播。允许在定向广播中使用可解析私有地址（Resolvable Private Address，RPA）作为目标地址。如果远端设备启用了隐私功能，并支持解析定向广播中的目标地址，则必须启用此选项。启用 `CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES` 后，主机在创建绑定（Bond）时读取对端的中心设备地址解析（Central Address Resolution）特征；若已知对端不支持地址解析，向它广播会失败并返回 `-ENOTSUP`；可通过 `bt_le_bond_addr_res_support` 查询其回答。若支持情况未知，应用有责任通过读取该特征进行检查。 |
| `BT_LE_ADV_OPT_FILTER_SCAN_REQ` | 使用过滤接受列表（Filter Accept List）过滤可以请求扫描响应数据的设备。 |
| `BT_LE_ADV_OPT_FILTER_CONN` | 使用过滤接受列表（Filter Accept List）过滤可以发起连接的设备。 |
| `BT_LE_ADV_OPT_NOTIFY_SCAN_REQ` | 向主动扫描器（Active Scanner）发送扫描响应数据后通知应用。 |
| `BT_LE_ADV_OPT_SCANNABLE` | 支持扫描响应数据（Scan Response Data）。与 `BT_LE_ADV_OPT_EXT_ADV` 一起使用时，本选项不能同时与 `BT_LE_ADV_OPT_CONN` 使用，且必须设置扫描响应数据。 |
| `BT_LE_ADV_OPT_EXT_ADV` | 使用扩展广播（Extended Advertising）。此选项在广播集中启用扩展广播：在三个主广播信道上发送一个小型头部包，指向将在 37 个次广播信道之一发送的广播数据包。广播者在 LE 1M PHY 上发送主广播，在 LE 2M PHY 上发送次广播，并在 LE 2M PHY 上建立连接。未启用此选项时，广播者在三个主广播信道上发送广播数据。注意：启用此选项要求扫描广播包的对端设备支持扩展广播；不能将它与 `bt_le_adv_start` 一起使用。 |
| `BT_LE_ADV_OPT_NO_2M` | 禁止在次广播信道上使用 LE 2M PHY。如果扫描器不支持 LE 2M PHY，可能需要禁用它。广播者在 LE 1M PHY 上发送主广播和次广播，并在 LE 1M PHY 上建立连接。注意：已设置 `BT_LE_ADV_OPT_CODED` 时不能设置本选项；要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |
| `BT_LE_ADV_OPT_CODED` | 在 LE 编码物理层（LE Coded PHY，长距离）上进行广播。广播者在此 PHY 上同时发送主广播和次广播，通信距离增加，代价是数据速率降低、功耗增加。连接在 LE Coded PHY 上建立。注意：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |
| `BT_LE_ADV_OPT_ANONYMOUS` | 广播时不携带设备地址，包括身份地址或 RPA。注意：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |
| `BT_LE_ADV_OPT_USE_TX_POWER` | 广播时包含发射功率（Transmit Power）。注意：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |
| `BT_LE_ADV_OPT_DISABLE_CHAN_37` | 禁用信道索引 37 上的广播。 |
| `BT_LE_ADV_OPT_DISABLE_CHAN_38` | 禁用信道索引 38 上的广播。 |
| `BT_LE_ADV_OPT_DISABLE_CHAN_39` | 禁用信道索引 39 上的广播。 |
| `BT_LE_ADV_OPT_USE_NRPA` | 使用不可解析私有地址（Non-Resolvable Private Address，NRPA）进行广播。更新广播参数时会设置一个新的 NRPA。这是一项高级功能，大多数用户应改为启用 `CONFIG_BT_EXT_ADV`。注意：与 `BT_LE_ADV_OPT_USE_IDENTITY` 互斥。 |
| `BT_LE_ADV_OPT_REQUIRE_S2_CODING` | 将广播者配置为在 LE 编码物理层（LE Coded PHY）上使用 S=2 编码方案，即将所要求的编码方案设为 S=2。S=2 是 LE Coded PHY 的编码选项之一，与 S=8 相比数据速率更高，代价是通信距离缩短。只有主、次广播信道均指定 LE Coded PHY，且控制器支持 LE 广播编码选择（Advertising Coding Selection）特性时，才会设置此方案；否则默认不要求特定编码方案。注意：仅在启用 Kconfig 选项 `CONFIG_BT_EXT_ADV_CODING_SELECTION` 时可用。 |
| `BT_LE_ADV_OPT_REQUIRE_S8_CODING` | 将广播者配置为在 LE 编码物理层（LE Coded PHY）上使用 S=8 编码方案，即将所要求的编码方案设为 S=8。S=8 是 LE Coded PHY 的编码选项之一，与 S=2 相比通信距离更远，代价是数据速率降低。只有主、次广播信道均指定 LE Coded PHY，且控制器支持 LE 广播编码选择（Advertising Coding Selection）特性时，才会设置此方案；否则默认不要求特定编码方案。注意：仅在启用 Kconfig 选项 `CONFIG_BT_EXT_ADV_CODING_SELECTION` 时可用。 |
| `BT_LE_ADV_OPT_TX_POWER` | 为广播集请求特定发射功率（TX Power）等级。设置后，将 `bt_le_adv_param::tx_power` 字段作为期望发射功率传给控制器；控制器选择最接近的受支持等级，并通过 `bt_le_ext_adv_info::tx_power` 报告实际值。未设置时，控制器自由选择发射功率，相当于 `BT_HCI_LE_ADV_TX_POWER_NO_PREF`。 |

**说明（Note）**：注意：若要在建立连接后继续广播，应用应监听 `bt_conn_cb::connected` 事件并重新启动广播集。所有连接对象都在使用时，无法启动广播者；此时应延迟到 `bt_conn_cb::recycled` 再启动。若要在断开连接后继续广播，应监听 `bt_conn_cb::recycled`。

**警告（Warning）**：警告：这会损害设备隐私，因此使用本选项时必须谨慎。

**说明（Note）**：注意：广播所用地址与 `bt_le_oob_get_local` 返回的地址不同，应使用 `bt_id_get` 获取 LE 地址。

**说明（Note）**：注意：启用此选项要求扫描广播包的对端设备支持扩展广播（Extended Advertising）。不能将它与 `bt_le_adv_start` 一起使用。

**说明（Note）**：注意：已设置 `BT_LE_ADV_OPT_CODED` 时不能设置本选项；要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

**说明（Note）**：注意：与 `BT_LE_ADV_OPT_USE_IDENTITY` 互斥。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_EXT_ADV_CODING_SELECTION` 时可用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_EXT_ADV_CODING_SELECTION` 时可用。

<a id="ga544ccde35638d8f580942d830fe9f242"></a>

### `bt_le_ext_adv_state`

```c
enum bt_le_ext_adv_state
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

广播状态（Advertising States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_EXT_ADV_STATE_DISABLED` | 广播集（Advertising Set）已创建，但尚未启用。 |
| `BT_LE_EXT_ADV_STATE_ENABLED` | 广播集（Advertising Set）已启用。 |

<a id="gae60a45dde6b4d9f4c54a2a6070254f11"></a>

### `bt_le_per_adv_opt`

```c
enum bt_le_per_adv_opt
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

周期性广播选项（Periodic Advertising Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_PER_ADV_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_LE_PER_ADV_OPT_USE_TX_POWER` | 广播时包含发射功率（Transmit Power）。注意：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |
| `BT_LE_PER_ADV_OPT_INCLUDE_ADI` | 广播时包含广播数据信息（AdvDataInfo，ADI）。注意：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。 |

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

**说明（Note）**：注意（Note）：要求在 `bt_le_adv_param::options` 中设置 `BT_LE_ADV_OPT_EXT_ADV` 位，参见 `bt_le_adv_opt` 字段。

<a id="ga6bb77c0808c761753650cde28ddb013e"></a>

### `bt_le_per_adv_state`

```c
enum bt_le_per_adv_state
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

周期性广播状态（Periodic Advertising States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_PER_ADV_STATE_NONE` | 尚未配置周期广播（Periodic Advertising）。 |
| `BT_LE_PER_ADV_STATE_DISABLED` | 广播集已配置周期广播（Periodic Advertising），但尚未启用。 |
| `BT_LE_PER_ADV_STATE_ENABLED` | 周期广播（Periodic Advertising）已启用。 |

<a id="gac942d7e3cae8fca22080f93bf9528ee9"></a>

### `bt_le_per_adv_sync_opt`

```c
enum bt_le_per_adv_sync_opt
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

周期性广播同步选项（Periodic Advertising Sync Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_PER_ADV_SYNC_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST` | 使用周期广播列表（Periodic Advertising List）与广播者同步。设置此选项后，忽略参数中的地址和广播集标识符（SID）。 |
| `BT_LE_PER_ADV_SYNC_OPT_REPORTING_INITIALLY_DISABLED` | 禁用周期广播报告（Periodic Advertising Report）。在启用之前，不处理任何广播报告。 |
| `BT_LE_PER_ADV_SYNC_OPT_FILTER_DUPLICATE` | 过滤重复的周期广播报告（Periodic Advertising Report）。 |
| `BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOA` | 同步带有到达角（Angle of Arrival，AoA）恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_1US` | 同步带有出发角（Angle of Departure，AoD）1 微秒恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_OPT_DONT_SYNC_AOD_2US` | 同步带有出发角（Angle of Departure，AoD）2 微秒恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_OPT_SYNC_ONLY_CONST_TONE_EXT` | 不同步不含恒定音调扩展（Constant Tone Extension，CTE）的数据包。 |

<a id="ga820c5f3721e72662e558cc4576b6111b"></a>

### `bt_le_per_adv_sync_transfer_opt`

```c
enum bt_le_per_adv_sync_transfer_opt
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

周期性广播同步传输选项（Periodic Advertising Sync Transfer Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOA` | 排除到达角（Angle of Arrival，AoA）。不同步带有 AoA 恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_1US` | 排除出发角（Angle of Departure，AoD）1 微秒。不同步带有 AoD 1 微秒恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_NO_AOD_2US` | 排除出发角（Angle of Departure，AoD）2。不同步带有 AoD 2 微秒恒定音调扩展（CTE）的广播。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_SYNC_ONLY_CTE` | 仅同步带有恒定音调扩展（Constant Tone Extension，CTE）的数据包。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED` | 同步收到的周期广播同步传输（PAST）数据包，但不生成同步报告。本选项不得与 `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES` 同时设置。 |
| `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_FILTER_DUPLICATES` | 同步收到的周期广播同步传输（PAST）数据包，并在过滤重复项后生成同步报告。本选项不得与 `BT_LE_PER_ADV_SYNC_TRANSFER_OPT_REPORTING_INITIALLY_DISABLED` 同时设置。 |

<a id="gab4b5773898e2a1eef21557915a21c996"></a>

### `bt_le_scan_opt`

```c
enum bt_le_scan_opt
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_SCAN_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_LE_SCAN_OPT_FILTER_DUPLICATE` | 过滤重复项（Filter Duplicates）。 |
| `BT_LE_SCAN_OPT_FILTER_ACCEPT_LIST` | 使用过滤接受列表（Filter Accept List）进行过滤。 |
| `BT_LE_SCAN_OPT_CODED` | 启用编码物理层（Coded PHY，长距离）扫描。 |
| `BT_LE_SCAN_OPT_NO_1M` | 禁用 1M PHY 扫描。注意：需要 `BT_LE_SCAN_OPT_CODED`。 |
| `BT_LE_SCAN_OPT_EXT_FILTER_POLICY` | 使用扩展扫描器过滤策略（Extended Scanner Filter Policy）。还报告目标地址为可解析私有地址（RPA）、但控制器无法解析的定向广播，目标地址通过 `bt_le_scan_recv_info::direct_addr` 报告。注意：需要 `CONFIG_BT_SCAN_EXT_FILTER_POLICY`；如果该配置被禁用却设置了本选项，`bt_le_scan_start` 返回 `-EINVAL`。还要求控制器支持扩展扫描器过滤策略，否则 `bt_le_scan_start` 返回 `-ENOTSUP`。 |

**说明（Note）**：注意：需要 `BT_LE_SCAN_OPT_CODED`。

**说明（Note）**：注意：需要 `CONFIG_BT_SCAN_EXT_FILTER_POLICY`；如果该配置被禁用却设置了本选项，`bt_le_scan_start` 返回 `-EINVAL`。还要求控制器支持扩展扫描器过滤策略（Extended Scanner Filter Policies），否则 `bt_le_scan_start` 返回 `-ENOTSUP`。

<a id="gaf980473379afa477c09e19912d40d29e"></a>

### `bt_le_scan_type`

```c
enum bt_le_scan_type
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_SCAN_TYPE_PASSIVE` | 扫描时不向广播者请求附加信息。 |
| `BT_LE_SCAN_TYPE_ACTIVE` | 扫描并向广播者请求附加信息。使用此扫描类型会自动向所有设备发送扫描请求，扫描响应与广播报告使用相同的接收方式和回调。 |

<a id="gad88cf1dec20264f9bdde91571efe8dce"></a>

### `bt_br_bond_exists()`

```c
bool bt_br_bond_exists ( const bt_addr_t * addr)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

检查经典蓝牙设备地址（Bluetooth Classic Device Address）是否已绑定（Bonded）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 经典蓝牙（Bluetooth Classic）设备地址。 |

**返回（Returns）**：返回值：如果 `addr` 已绑定（Bonded），则返回 `true`。

<a id="ga430de0ad30da7322c5353941f1f6a133"></a>

### `bt_br_discovery_cb_register()`

```c
void bt_br_discovery_cb_register ( struct bt_br_discovery_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

注册发现数据包回调（Discovery Packet Callbacks）。

将回调结构加入监视查询（Inquiry）活动的回调结构列表。

所有查询（Inquiry）活动都会调用此回调，与启动发现时使用的 API 无关。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

<a id="ga25ab96ac005237aee739bf32fc1aac94"></a>

### `bt_br_discovery_cb_unregister()`

```c
void bt_br_discovery_cb_unregister ( struct bt_br_discovery_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

注销发现数据包回调（Discovery Packet Callbacks）。

从发现回调列表（Discovery Callback List）中移除该回调结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

<a id="ga9760190192dde5c498ec96628468be8d"></a>

### `bt_br_discovery_start()`

```c
int bt_br_discovery_start ( const struct bt_br_discovery_param * param, struct bt_br_discovery_result * results, size_t count )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

开始 BR/EDR 发现（Discovery）。

启动 BR/EDR 发现，即查询（Inquiry），并通过指定回调提供结果。发现结果通过 `bt_br_discovery_cb_register` 注册的回调通知。如果会话期间收到的查询结果多于提供的存储空间所能容纳的数量，则仅报告接收信号强度指示（RSSI）最高的结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 发现参数（Discovery Parameters）。 |
| `results` | 用于保存发现结果的存储空间。 |
| `count` | 存储空间中可容纳的结果数量，有效范围为 1–255。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga567c71b49399fe7e1a5593edbf005e3a"></a>

### `bt_br_discovery_stop()`

```c
int bt_br_discovery_stop ( void )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

停止 BR/EDR 发现（Discovery）。

停止正在进行的 BR/EDR 发现。如果由本调用停止发现，则不报告结果。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga4c82193c50c616d9319c87ebcffabe66"></a>

### `bt_br_foreach_bond()`

```c
void bt_br_foreach_bond ( void(* func )(const struct bt_br_bond_info *info, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

遍历全部已有经典蓝牙绑定（Classic Bonds）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 对每个绑定（Bond）调用的函数。 |
| `user_data` | 传给回调函数（Callback Function）的数据。 |

<a id="gab49521adee2b653dbec04fbf833e22d9"></a>

### `bt_br_get_class_of_device()`

```c
int bt_br_get_class_of_device ( uint32_t * cod)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

获取本地 BR/EDR 控制器的设备类别（Class of Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cod` | 指向用于保存当前设备类别（Class of Device）值的位置的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 如果蓝牙设备尚未就绪。 |
| `-EINVAL` | 如果 `cod` 为 `NULL`。 |
| `Other` | 失败时返回负错误码。 |

<a id="ga6ca71da8c9eed3d317200aa1f6babc7d"></a>

### `bt_br_inquiry_scan_update_param()`

```c
int bt_br_inquiry_scan_update_param ( const struct bt_br_inquiry_scan_param * param)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

更新 BR/EDR 查询扫描参数（Inquiry Scan Parameters）。

本函数更新本地 BR/EDR 控制器的查询扫描参数（Inquiry Scan Parameters）。这些参数决定控制器如何处理查询请求。

本函数验证提供的间隔、窗口和扫描类型等参数，并发送相应的主机控制器接口（HCI）命令，更新控制器的查询扫描活动和扫描类型。

用户可通过辅助宏 `BT_BR_INQUIRY_SCAN_PARAM` 定义自有值，设置自定义查询扫描参数；也可使用蓝牙规范定义的预设标准参数：

- `BT_BR_INQUIRY_SCAN_PARAM_DEFAULT`：默认查询扫描参数（Default Inquiry Scan Parameters）。这些预设参数用于满足常见使用场景，并确保符合蓝牙规范。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 查询扫描参数（Inquiry Scan Parameters）包括：`interval` 为连续查询扫描之间的时间，以 0.625 毫秒为单位，必须位于 `[0x0012, 0x1000]`；`window` 为单次查询扫描时长，以 0.625 毫秒为单位，必须位于 `[0x0011, 0x1000]`；`type` 为查询扫描类型，例如标准（Standard）或交错（Interlaced）。 |

**返回（Returns）**：返回值：成功时返回 0；提供的参数无效时返回 `-EINVAL`；设备未就绪时返回 `-EAGAIN`；HCI 命令内存分配失败时返回 `-ENOBUFS`；内部失败时返回其他负错误码。

<a id="ga2ec860d06c45098624b106b59fbab634"></a>

### `bt_br_oob_get_local()`

```c
int bt_br_oob_get_local ( struct bt_br_oob * oob)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

获取 BR/EDR 本地带外信息（Out Of Band Information）。

本函数获取本地控制器信息，可用于带外配对（Out Of Band Pairing）或连接创建流程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `oob` | 带外信息（Out Of Band Information，OOB）。 |

<a id="ga78c5fc5f71d08b0c800967ee7696fc83"></a>

### `bt_br_page_scan_update_param()`

```c
int bt_br_page_scan_update_param ( const struct bt_br_page_scan_param * param)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

更新 BR/EDR 寻呼扫描参数（Page Scan Parameters）。

本函数更新本地 BR/EDR 控制器的寻呼扫描参数（Page Scan Parameters）。这些参数决定控制器如何监听远端设备传入的连接请求。

本函数验证提供的间隔、窗口和扫描类型等参数，并发送相应的主机控制器接口（HCI）命令，更新控制器的寻呼扫描活动和扫描类型。

用户可通过辅助宏 `BT_BR_PAGE_SCAN_PARAM()` 定义自有值，设置自定义寻呼扫描参数；也可使用蓝牙规范定义的预设标准参数：

- `BT_BR_PAGE_SCAN_PARAM_R0`：默认寻呼扫描参数（Default Page Scan Parameters）。
- `BT_BR_PAGE_SCAN_PARAM_FAST_R1`：R1 的快速寻呼扫描参数（Fast Page Scan Parameters）。
- `BT_BR_PAGE_SCAN_PARAM_MEDIUM_R1`：R1 的中等寻呼扫描参数（Medium Page Scan Parameters）。
- `BT_BR_PAGE_SCAN_PARAM_SLOW_R1`：R1 的慢速寻呼扫描参数（Slow Page Scan Parameters）。
- `BT_BR_PAGE_SCAN_PARAM_FAST_R2`：R2 的快速寻呼扫描参数（Fast Page Scan Parameters）。
- `BT_BR_PAGE_SCAN_PARAM_SLOW_R2`：R2 的慢速寻呼扫描参数（Slow Page Scan Parameters）。

这些预设参数用于满足常见使用场景，并确保符合蓝牙规范。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 寻呼扫描参数（Page Scan Parameters）包括：`interval` 为连续寻呼扫描之间的时间，以 0.625 毫秒为单位，必须位于 `[0x0012, 0x1000]`；`window` 为单次寻呼扫描时长，以 0.625 毫秒为单位，必须位于 `[0x0011, 0x1000]`；`type` 为寻呼扫描类型，例如标准（Standard）或交错（Interlaced）。 |

**返回（Returns）**：返回值：成功时返回 0；提供的参数无效时返回 `-EINVAL`；设备未就绪时返回 `-EAGAIN`；HCI 命令内存分配失败时返回 `-ENOBUFS`；内部失败时返回其他负错误码。

<a id="ga201f64881ccc13169d072d9cc04948ba"></a>

### `bt_br_set_class_of_device()`

```c
int bt_br_set_class_of_device ( uint32_t cod)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

设置本地 BR/EDR 控制器的设备类别（Class of Device）。

本函数将设备类别（Class of Device，COD）值写入 BR/EDR 控制器。远端设备在发现过程中使用 COD 识别设备类型及其提供的服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cod` | 要设置的设备类别（COD）值，应由主要服务类别位（`BT_COD_MAJOR_SVC_CLASS_*`）、主要设备类别位（`BT_COD_MAJOR_DEVICE_CLASS_*`）以及次要设备类别位（`BT_COD_MINOR_DEVICE_CLASS_*`）组合而成。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 如果蓝牙设备尚未就绪。 |
| `-EINVAL` | 如果提供的 COD 值试图直接设置有限可发现位，而此操作不被允许。 |
| `Other` | 底层 HCI 命令失败时返回的负错误码。 |

**说明（Note）**：注意：不能通过本函数直接设置有限可发现模式位（`BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER`）。应通过 `bt_br_set_discoverable()` 的 `limited` 参数启用有限可发现模式（Limited Discoverable Mode），它会自动设置对应的 COD 位。

**参阅（See Also）**：另见：`bt_br_set_discoverable()`、`bt_br_get_class_of_device()`。

<a id="ga66c29ea0ccb8b8ff5610c1fc53fe1eb9"></a>

### `bt_br_set_connectable()`

```c
int bt_br_set_connectable ( bool enable, bt_br_conn_req_func_t func )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

启用／禁用控制器的可连接状态（Connectable State）。

允许使本地控制器进入可连接状态（Connectable）。这意味着控制器开始在寻呼扫描（PAGE SCAN）信道上监听设备请求。若禁用此状态，也会取消之前已设置的可发现状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 允许／禁止控制器进入可连接状态的值。 |
| `func` | 处理传入连接请求的回调函数。如果 `enable` 为 `false`，则忽略本参数。如果 `func` 为 `NULL`，则在内部接受 `conn_req`，默认角色为外设（Peripheral）；启用 `CONFIG_BT_ACCEPT_CONN_AS_CENTRAL` 时，可执行角色切换请求。若提供 `func`，则将 `conn_req` 交给回调，由应用决定接受还是拒绝连接，以及所需连接角色。 |

**返回（Returns）**：返回值：无法设置请求的状态，或者该状态已经设置时，返回负值；成功时返回零。

<a id="gae3376fdd364e9b9d6e304ec589ba00f5"></a>

### `bt_br_set_discoverable()`

```c
int bt_br_set_discoverable ( bool enable, bool limited )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

启用／禁用控制器的可发现状态（Discoverable State）。

允许本地控制器在查询扫描（INQUIRY SCAN）信道上监听，并响应发起通用查询（General Inquiry）的设备。启用此状态前，必须先处于可连接状态。

设备进入有限可发现模式（Limited Discoverable Mode）后，控制器将在该模式中停留 `CONFIG_BT_LIMITED_DISCOVERABLE_DURATION` 秒，然后退出可发现模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 允许／禁止控制器进入可发现状态的值。 |
| `limited` | 允许／禁止控制器进入有限可发现模式的值。 |

**返回（Returns）**：返回值：无法设置请求的状态，或者该状态已经设置时，返回负值；成功时返回零。

<a id="gaccab07100ab64fd805fe1d468bc889ac"></a>

### `bt_br_unpair()`

```c
int bt_br_unpair ( const bt_addr_t * addr)
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

清除经典蓝牙配对信息（Classic Pairing Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 远端地址。使用 `NULL` 或 `BT_ADDR_ANY` 可清除所有远端设备。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="gab28ba977a94f63476f360d358868f8f6"></a>

### `bt_br_write_eir()`

```c
int bt_br_write_eir ( const struct bt_data * eir, size_t eir_count, bool fec_required )
```

```c
#include <zephyr/bluetooth/classic/classic.h>
```

写入扩展查询响应数据（Extended Inquiry Response Data）。

写入扩展查询响应（Extended Inquiry Response，EIR）流程中要发送的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `eir` | 要包含在扩展查询响应（EIR）中的 `bt_data` 元素数组。 |
| `eir_count` | `eir` 数组中的元素数量。 |
| `fec_required` | 是否需要前向纠错（FEC）编码，取值为 `true`／`false`。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为非零值。

<a id="ga8046c2b06d3dad0d6c8184de492517d2"></a>

### `bt_configure_data_path()`

```c
int bt_configure_data_path ( uint8_t dir, uint8_t id, uint8_t vs_config_len, const uint8_t * vs_config )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

配置厂商数据路径（Vendor Data Path）。

请求控制器配置控制器与主机之间指定方向的数据传输路径（Data Transport Path）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要配置的方向，取值为 `BT_HCI_DATAPATH_DIR_HOST_TO_CTLR` 或 `BT_HCI_DATAPATH_DIR_CTLR_TO_HOST`。 |
| `id` | 厂商专用逻辑传输信道 ID，范围为 `[BT_HCI_DATAPATH_ID_VS..BT_HCI_DATAPATH_ID_VS_END]`。 |
| `vs_config_len` | 附加厂商专用配置数据的长度。 |
| `vs_config` | 指向附加厂商专用配置数据的指针。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga652eef01e5256e0d820cd1f4db877429"></a>

### `bt_data_parse()`

```c
void bt_data_parse ( struct net_buf_simple * ad, bool(* func )(struct bt_data *data, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

用于解析广播数据、扩展查询响应（EIR）数据或带外（OOB）数据的辅助函数。

用于解析扩展查询响应（EIR）、广播数据（AD）及带外（OOB）数据块中基本 AD 类型的辅助函数。最常见的场景是：在传给 `bt_le_scan_start` 的回调中，对收到的广播数据调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ad` | 传给 `bt_le_scan_cb_t` 回调的广播数据。 |
| `func` | 每找到一个数据元素（Element）就会调用的回调函数（Callback Function）。回调应返回 `true` 继续解析，或返回 `false` 停止解析。 |
| `user_data` | 要传递给回调（Callback）的用户数据（User Data）。 |

**警告（Warning）**：警告：本辅助函数在解析时会消耗 `ad`。若之后还需使用原始数据，用户应保留副本。可在调用前用 `net_buf_simple_save` 保存状态，调用后再用 `net_buf_simple_restore` 恢复。

<a id="ga0a58e5a050170e84a80f8d5bb3516ec7"></a>

### `bt_disable()`

```c
int bt_disable ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

禁用蓝牙（Bluetooth）。

禁用蓝牙。不能在 `bt_enable` 完成之前调用。

如果调用 `bt_enable()` 时提供了就绪回调（Ready Callback），则初始化异步执行。在就绪回调触发前调用 `bt_disable()` 会返回 `-EAGAIN`；调用者应在就绪回调之后重试。

本 API 会清除所有未通过 `CONFIG_BT_SETTINGS` 持久保存的已配置身份地址和密钥。可以在重新启用协议栈之前，通过 `settings_load` 恢复这些信息。

本 API 不会清除之前注册的回调，包括 `bt_le_scan_cb_register`、`bt_conn_cb_register` 和 `bt_br_discovery_cb_register`。也就是说，之后重新启用蓝牙子系统时，应用不得重复注册这些回调。

关闭并释放主机控制器接口（HCI）资源。结果取决于架构。

如果 HCI 驱动无法关闭传输通道，则返回该错误，蓝牙保持未就绪状态，因为此时主机已经拆除了自身状态，包括连接。可以再次调用 `bt_disable()`。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | HCI 驱动不支持关闭其传输通道。蓝牙保持原状态。 |
| `-EALREADY` | 蓝牙已经禁用，或者正在禁用。 |
| `-EAGAIN` | 蓝牙仍在启用过程中；启用 `CONFIG_BT_SETTINGS` 时，此过程还包括加载蓝牙设置。待 `bt_is_ready()` 返回 `true` 后重试。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac45d16bfe21c3c38e834c293e5ebc42b"></a>

### `bt_enable()`

```c
int bt_enable ( bt_ready_cb_t cb)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

启用蓝牙（Bluetooth）。

启用蓝牙。必须在调用任何需要与本地蓝牙硬件通信的函数之前调用。

启用 `CONFIG_BT_SETTINGS` 时，应用必须在此 API 成功完成之后加载蓝牙设置，随后才能使用蓝牙 API。仅在调用本函数之前加载设置是不够的。可以使用 `settings_load`，或以 `"bt"` 为参数调用 `settings_load_subtree` 加载蓝牙设置。后者仅选择性加载蓝牙设置；如果此前已经调用过 `settings_load`，推荐使用后者。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 用于通知完成的回调；传入 `NULL` 则同步执行启用操作。回调从协议栈内部的线程上下文调用，绝不从中断服务程序（ISR）调用；参见回调执行上下文（Callback Execution Contexts）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 蓝牙已经启用，或者正在启用。 |
| `-EAGAIN` | 蓝牙正在禁用；待 `bt_disable()` 返回后重试。 |
| `-ENODEV` | HCI 驱动尚未就绪。 |
| `-ETIMEDOUT` | 控制器未响应任何命令。HCI 传输通道已关闭，因此无需先调用 `bt_disable()` 即可再次调用 `bt_enable()`。若提供了 `cb`，则通过回调交付此错误。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaad380b7f8984f8522c1b79f9bdc04905"></a>

### `bt_foreach_bond()`

```c
void bt_foreach_bond ( uint8_t id, void(* func )(const struct bt_bond_info *info, void *user_data), void * user_data )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

遍历全部现有绑定（Bonds）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份句柄（Identity Handle），通常为 `BT_ID_DEFAULT`，对应遍历时使用的身份地址。 |
| `func` | 对每个绑定（Bond）调用的函数。 |
| `user_data` | 传给回调函数（Callback Function）的数据。 |

<a id="ga35b76ea7ce79721e47ca4164e08b2dfb"></a>

### `bt_get_appearance()`

```c
uint16_t bt_get_appearance ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取本地蓝牙外观值（Bluetooth Appearance）。

蓝牙外观（Bluetooth Appearance）通过外观值（Appearance Value）描述设备的外部外观。

**参阅（See Also）**：另见：Bluetooth SIG《分配编号》（Assigned Numbers）文档第 2.6 节。

**返回（Returns）**：返回值：本地蓝牙主机的外观值（Appearance Value）。

<a id="gad922d894b25e86de3f81ce77200a13fd"></a>

### `bt_get_name()`

```c
const char * bt_get_name ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取蓝牙设备名称（Bluetooth Device Name）。

获取蓝牙 GAP 设备名称（Device Name）。

**返回（Returns）**：返回值：蓝牙设备名称。

<a id="gae11eb8ad254418c38a0e8689df25a159"></a>

### `bt_id_create()`

```c
int bt_id_create ( bt_addr_le_t * addr, uint8_t * irk )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

创建新的身份地址（Identity Address）。

使用给定地址和身份解析密钥（IRK）创建新的身份地址。本函数可以在 `bt_enable` 之前调用，但只有在 `bt_enable` 之后使用本 API，新身份地址才会持久存入闪存。原因是持久化设置在 `bt_enable` 之后加载，如果协议栈盲目覆盖闪存内容，可能造成冲突。如果提供的是预定义地址，也不会将其写入闪存，因为这表明应用有自己的地址来源，并能在每次上电时重复此过程，再保存到闪存属于冗余。

在 `bt_enable` 之前调用本函数时，不支持生成随机静态地址（Random Static Address）或随机 IRK。

如果应用希望协议栈随机生成身份地址并存入闪存以便日后恢复，应先使用 `bt_enable` 初始化协议栈，再调用 `settings_load`，然后通过 `bt_id_get` 检查恢复了多少个身份地址。如果恢复的数量不足，应用可调用本函数创建新的身份地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 新身份地址要使用的地址。若为 `NULL` 或初始化为 `BT_ADDR_LE_ANY`，协议栈将生成新的随机静态地址（Random Static Address）；若参数非 `NULL`，函数返回时会将生成的地址复制到该参数。 |
| `irk` | 此身份地址使用的身份解析密钥（Identity Resolving Key，IRK），长度为 `BT_IRK_SIZE` 个八位组。若全部为零或为 `NULL`，协议栈将生成随机 IRK；若参数非 `NULL`，函数返回时会将密钥复制回该参数。未启用隐私配置 `CONFIG_BT_PRIVACY` 时，本参数必须为 `NULL`。 |

**说明（Note）**：注意：启用 `CONFIG_BT_HCI_SET_PUBLIC_ADDR` 后，首次调用可以将公共地址（Public Address）设为控制器身份，但必须在 `bt_enable` 之前，且不存在其他身份。

**返回（Returns）**：返回值：成功时返回大于等于 0 的身份句柄（Identity Handle），失败时返回负错误码。

<a id="gaf6cd906690a51ebed04bea4f4ef716ff"></a>

### `bt_id_delete()`

```c
int bt_id_delete ( uint8_t id)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

删除身份地址（Identity Address）。

传入有效身份句柄（Identity Handle）时，本函数断开所有使用它创建的、与对应身份地址关联的连接，移除相关配对密钥或其他数据，然后将该身份标记为已删除，使其不能用于任何操作。若要重新使用该身份地址占用的槽位，必须使用 `bt_id_reset` API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 现有身份句柄（Identity Handle）。 |

**说明（Note）**：注意：不能删除默认身份地址，即 `BT_ID_DEFAULT` 对应的地址。若请求删除，本 API 返回错误。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga06d0ae35cbf4382679cc3cfe612cee4d"></a>

### `bt_id_get()`

```c
void bt_id_get ( bt_addr_le_t * addrs, size_t * count )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取当前配置的身份地址（Identity Addresses）。

返回当前配置的身份地址数组。为确保能获取所有可用身份地址，`addrs` 数组的元素数量应为 `CONFIG_BT_ID_MAX`。某些 API（如 `bt_le_adv_param`）要求的身份句柄（Identity Handle），就是身份地址在 `addrs` 数组中的索引。

若将 `addrs` 传为 `NULL`，则返回的 `count` 为所有可用身份地址的数量；随后可再次调用本函数，并提供非 `NULL` 的 `addrs` 参数来获取它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addrs` | 用于保存已配置身份地址的数组。 |
| `count` | 应初始化为数组大小；函数返回后，其中保存实际返回的身份地址数量。 |

**说明（Note）**：注意：已删除的身份地址可能在返回数组中显示为 `BT_ADDR_LE_ANY`。

<a id="gabb3353edc8a3a8d29a0370049b20cbe4"></a>

### `bt_id_reset()`

```c
int bt_id_reset ( uint8_t id, bt_addr_le_t * addr, uint8_t * irk )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

重置／回收身份地址（Identity Address）以供重用。

传入已有身份句柄（Identity Handle）时，本函数断开所有使用它创建的、与对应身份地址关联的连接，移除相关配对密钥或其他数据，然后依据 `addr` 和 `irk` 参数，在同一槽位创建新的身份地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 现有身份句柄（Identity Handle）。 |
| `addr` | 新身份地址要使用的地址。若为 `NULL` 或初始化为 `BT_ADDR_LE_ANY`，协议栈将生成新的静态随机地址（Static Random Address），并在函数返回时将其复制到给定参数。 |
| `irk` | 此身份地址使用的身份解析密钥（Identity Resolving Key，IRK），长度为 `BT_IRK_SIZE` 个八位组。若全部为零或为 `NULL`，协议栈将生成随机 IRK；若参数非 `NULL`，函数返回时会将密钥复制回该参数。未启用隐私配置 `CONFIG_BT_PRIVACY` 时，本参数必须为 `NULL`。 |

**说明（Note）**：注意：不能重置默认身份地址，即 `BT_ID_DEFAULT` 对应的地址。若请求重置，本 API 返回错误。

**返回（Returns）**：返回值：成功时返回大于等于 0 的身份句柄（Identity Handle），失败时返回负错误码。

<a id="ga7a595421c232b15ad96b52f0300fd960"></a>

### `bt_id_reset_irk()`

```c
int bt_id_reset_irk ( uint8_t id, uint8_t * irk )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

重置某个身份的本地身份解析密钥（Identity Resolving Key，IRK）。

替换给定身份的身份解析密钥（IRK），并在启用 `CONFIG_BT_SETTINGS` 时将其持久存入闪存。调用前必须移除现有绑定（Bond），因为已绑定的对端保留旧 IRK，无法解析使用新 IRK 生成的可解析私有地址（RPA）。未启用 `CONFIG_BT_SETTINGS` 时，新 IRK 在重启后丢失。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` id` | 身份索引（Identity Index），由 `bt_id_get` 返回，或使用 `BT_ID_DEFAULT`。必须小于当前已配置身份的数量。 |
| `[in,out] irk` | 此身份要使用的身份解析密钥（Identity Resolving Key，IRK），长度为 `BT_IRK_SIZE` 个八位组。若为 `NULL` 或全部为零，协议栈生成新的随机 IRK；缓冲区非 `NULL` 时，将新密钥复制回该缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 蓝牙协议栈尚未就绪。 |
| `-EINVAL` | `id` 超出范围。 |
| `-EALREADY` | 身份槽位（Identity Slot）为空。 |
| `-EBUSY` | 存在活动广播集，或者扫描／连接发起操作正在使用此身份，或者已有创建的扩展广播集分配给此身份。 |
| `-ENOTEMPTY` | 此身份存在绑定（Bond），请先调用 `bt_unpair`。 |
| `-EIO` | 随机身份解析密钥（IRK）生成失败。 |
| `-ENOTSUP` | 不支持随机生成。 |

**说明（Note）**：注意：与 `bt_id_reset` 不同，本函数也接受 `BT_ID_DEFAULT`，因为它不修改身份地址。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PRIVACY` 时可用。

**说明（Note）**：注意：调用本函数之前，必须通过 `bt_enable` 启用蓝牙协议栈。使用扩展广播时，必须先删除分配给此身份的广播集，仅停止广播集是不够的。

<a id="gaa8bf6854e7ad1fe7e0805737576e5d1a"></a>

### `bt_is_ready()`

```c
bool bt_is_ready ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

检查蓝牙（Bluetooth）是否就绪。

**返回（Returns）**：返回值：蓝牙就绪时返回 `true`，否则返回 `false`。

<a id="ga453074db3964f1b57b92ac7afb0b4fac"></a>

### `bt_le_adv_param_set_tx_power()`

```c
void bt_le_adv_param_set_tx_power ( struct bt_le_adv_param * param, int8_t tx_power )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置广播参数结构体（Advertising Parameter Struct）中的发射功率（TX Power）。

便捷辅助函数，可在一次调用中设置 `bt_le_adv_param::tx_power`，并在 `bt_le_adv_param::options` 中启用 `BT_LE_ADV_OPT_TX_POWER`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 要更新的广播参数。 |
| `tx_power` | 请求的发射功率（TX Power），单位为 dBm。有效范围为 `BT_HCI_LE_ADV_TX_POWER_MIN` 至 `BT_HCI_LE_ADV_TX_POWER_MAX`。 |

<a id="gad2e3caef88d52d720e8e4d21df767b02"></a>

### `bt_le_adv_start()`

```c
int bt_le_adv_start ( const struct bt_le_adv_param * param, const struct bt_data * ad, size_t ad_len, const struct bt_data * sd, size_t sd_len )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

启动广播（Advertising）。

设置广播数据、扫描响应数据和广播参数，然后启动广播。

设置 `param.peer` 时，向该对端设备执行定向广播。此时忽略函数的其他参数。

本函数不能在 `param.options` 含有 `BT_LE_ADV_OPT_EXT_ADV` 时使用。扩展广播（Extended Advertising）必须使用 `bt_le_ext_adv_*` 函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 广播参数（Advertising Parameters）。 |
| `ad` | 要用于广播数据包的数据。 |
| `ad_len` | `ad` 中的元素数量。 |
| `sd` | 要用于扫描响应数据包的数据。 |
| `sd_len` | `sd` 中的元素数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 使用了 `BT_LE_ADV_OPT_DIR_ADDR_RPA`，且根据 `bt_le_bond_addr_res_support` 的报告，已知对端不支持地址解析。 |

**返回（Returns）**：返回值：成功时返回零，否则返回负错误码。`-ENOMEM` 表示没有可供可连接广播者使用的空闲连接对象。

**返回（Returns）**：返回值：请求可连接广播，且控制器已建立的连接数量达到上限时，返回 `-ECONNREFUSED`。仅使用 Zephyr 控制器时保证返回此错误码；其他控制器在这种情况下可能返回 `-EIO`。

<a id="ga1776e310b9d80898e6b32d50c4fe0b49"></a>

### `bt_le_adv_stop()`

```c
int bt_le_adv_stop ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

停止广播（Advertising）。

停止正在进行的广播。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga9a406ebfefac3dd09935a4ae0e317817"></a>

### `bt_le_adv_update_data()`

```c
int bt_le_adv_update_data ( const struct bt_data * ad, size_t ad_len, const struct bt_data * sd, size_t sd_len )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

更新广播（Advertising）。

更新广播数据和扫描响应数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ad` | 要用于广播数据包的数据。 |
| `ad_len` | `ad` 中的元素数量。 |
| `sd` | 要用于扫描响应数据包的数据。 |
| `sd_len` | `sd` 中的元素数量。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga5b5e51f79896d674bf6b70b2251e79d4"></a>

### `bt_le_bond_addr_res_support()`

```c
enum bt_le_addr_res_support bt_le_bond_addr_res_support ( uint8_t id, const bt_addr_le_t * peer )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取已绑定对端（Bonded Peer）对地址解析（Address Resolution）的支持情况。

不支持地址解析的对端无法解析定向广播的目标地址，因此只能通过未使用 `BT_LE_ADV_OPT_DIR_ADDR_RPA` 的定向广播联系到它。

回答值来自对端的中心设备地址解析（Central Address Resolution）特征。启用 `CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES` 后，主机在创建绑定（Bond）时读取该特征；只要回答仍未知，后续连接到对端时就会再次尝试。该选项禁用、与对端没有绑定，或者尚未读取该特征时，回答为未知。自动读取完成通过 `bt_conn_auth_info_cb::addr_res_support_read` 通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份句柄（Identity Handle），通常为 `BT_ID_DEFAULT`。 |
| `peer` | 已绑定对端的身份地址（Identity Address）。 |

**返回（Returns）**：返回值：对端对地址解析（Address Resolution）的支持情况。

<a id="ga309a67de79cc215db1d33251f267f361"></a>

### `bt_le_bond_exists()`

```c
bool bt_le_bond_exists ( uint8_t id, const bt_addr_le_t * addr )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

检查由低功耗蓝牙地址（Bluetooth LE Address）标识的设备是否已绑定（Bonded）。

有效的蓝牙低功耗身份地址（Bluetooth LE Identity Address）必须是公开地址（Public Address）或静态随机地址（Random Static Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份句柄（Identity Handle），通常为 `BT_ID_DEFAULT`，对应本次函数调用所针对的身份地址。 |
| `addr` | 蓝牙低功耗设备地址（Bluetooth LE Device Address）。 |

**返回（Returns）**：返回值：如果 `addr` 与本地 `id` 已绑定（Bonded），则返回 `true`。

<a id="gad02b855dd7a26e3910b247fa73f19297"></a>

### `bt_le_ext_adv_create()`

```c
int bt_le_ext_adv_create ( const struct bt_le_adv_param * param, const struct bt_le_ext_adv_cb * cb, struct bt_le_ext_adv ** adv )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

创建广播集（Advertising Set）。

创建一个具有独立参数和数据的广播集（Advertising Set）实例。该广播集在通过 `bt_le_ext_adv_delete` 删除前一直有效。可通过 `bt_le_ext_adv_update_param` 更新广播参数，通过 `bt_le_ext_adv_start` 启动广播。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 广播参数（Advertising Parameters）。 |
| `[in] cb` | 用于通知广播者活动的回调结构，可以为 `NULL`。在广播集整个生命周期内，必须指向有效内存。 |
| `[out] adv` | 成功时得到有效的广播集对象。 |

**说明（Note）**：注意：可通过 `CONFIG_BT_EXT_ADV_MAX_ADV_SET` 控制支持的扩展广播集数量。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga62310a27f7fea925dfcf3abd7c454787"></a>

### `bt_le_ext_adv_delete()`

```c
int bt_le_ext_adv_delete ( struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

删除广播集（Advertising Set）。

删除广播集并释放其资源。如果此前已达到 `CONFIG_BT_EXT_ADV_MAX_ADV_SET` 上限，删除后就可以创建新的广播集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaf8b28f54c68251024b869f3b0d1c1282"></a>

### `bt_le_ext_adv_get_index()`

```c
uint8_t bt_le_ext_adv_get_index ( const struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取广播集（Advertising Set）的数组索引。

本函数将 `bt_adv` 映射为广播集数组中的索引。该数组有 `CONFIG_BT_EXT_ADV_MAX_ADV_SET` 个元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集（Advertising Set）。 |

**返回（Returns）**：返回值：广播集对象的索引，范围为 `0..CONFIG_BT_EXT_ADV_MAX_ADV_SET-1`。

<a id="gac06c9f55cf1da46e0d64b4d9af984ecb"></a>

### `bt_le_ext_adv_get_info()`

```c
int bt_le_ext_adv_get_info ( const struct bt_le_ext_adv * adv, struct bt_le_ext_adv_info * info )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取广播集信息（Advertising Set Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `info` | 广播集信息对象（Advertising Set Info Object）。仅在成功时，其中的值才有效。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `adv` 不是有效广播集，或者 `info` 为 `NULL`。 |

<a id="ga7486aab863ca497a50dacf81657f48d4"></a>

### `bt_le_ext_adv_oob_get_local()`

```c
int bt_le_ext_adv_oob_get_local ( struct bt_le_ext_adv * adv, struct bt_le_oob * oob )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

本函数获取本地信息，可用于带外配对（Out of Band Pairing）或连接创建。

启用隐私配置 `CONFIG_BT_PRIVACY` 时，这会生成新的可解析私有地址（Resolvable Private Address，RPA），有效期为 `CONFIG_BT_RPA_TIMEOUT` 秒。此地址由该广播集使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] adv` | 广播集对象（Advertising set object）。 |
| `[out] oob` | LE 带外信息（LE OOB Information）。 |

**说明（Note）**：注意：为多个广播集生成带外（OOB）信息时，必须同时生成全部 OOB 信息。启用隐私功能时，若正在创建连接，则不能刷新可解析私有地址（RPA），应等待连接完成回调（Connected Callback）。本函数随机生成配对流程使用的密码材料，每次新的配对流程都应重新调用。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="gad731f829b3566be3e56485b2a64f80b1"></a>

### `bt_le_ext_adv_set_data()`

```c
int bt_le_ext_adv_set_data ( struct bt_le_ext_adv * adv, const struct bt_data * ad, size_t ad_len, const struct bt_data * sd, size_t sd_len )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置广播集的广播数据或扫描响应数据（Advertising / Scan Response Data）。

设置广播数据或扫描响应数据。如果广播集当前正在广播，则在后续广播事件中更新数据。

同时启用 `BT_LE_ADV_OPT_EXT_ADV` 和 `BT_LE_ADV_OPT_SCANNABLE` 时，忽略广播数据，仅使用扫描响应数据。未启用 `BT_LE_ADV_OPT_SCANNABLE` 时，忽略扫描响应数据，仅使用广播数据。

如果广播集配置为在主广播信道发送广播数据，则最大数据长度为 `BT_GAP_ADV_MAX_ADV_DATA_LEN` 个八位组。如果广播集配置为扩展广播，则最大数据长度由控制器定义，允许的最高上限为 `BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN` 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `ad` | 要用于广播数据包的数据。 |
| `ad_len` | `ad` 中的元素数量。 |
| `sd` | 要用于扫描响应数据包的数据。 |
| `sd_len` | `sd` 中的元素数量。 |

**说明（Note）**：注意：扩展广播（Extended Advertising）在 Bluetooth 5.0 中引入，传统扫描器（Legacy Scanner）不支持接收任何扩展广播包。在广播过程中更新数据时，广播数据和扫描响应数据的长度必须小于或等于单个广播包可容纳的长度，否则必须先停止广播者。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaf0f436c55482d9429f674303ae3aa815"></a>

### `bt_le_ext_adv_start()`

```c
int bt_le_ext_adv_start ( struct bt_le_ext_adv * adv, const struct bt_le_ext_adv_start_param * param )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

使用给定广播集（Advertising Set）启动广播。

如果广播者受到 `param.timeout` 或 `param.num_events` 限制，则达到限制时通过 `bt_le_ext_adv_cb::sent` 回调通知应用。如果同时限制超时时间和广播事件数量，则先达到的限制使广播者停止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `param` | 广播启动参数（Advertising Start Parameters）。 |

**说明（Note）**：注意：可通过 `bt_le_ext_adv_create` 创建广播集 `adv`。

<a id="ga1c864c4b183f9a86c9f70a11471c5b15"></a>

### `bt_le_ext_adv_stop()`

```c
int bt_le_ext_adv_stop ( struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

停止给定广播集（Advertising Set）的广播。

停止指定广播集的广播。使用本函数时，不会调用广播发送完成回调（Advertising Sent Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga1aabdb81cb1a1841ff0fb91d849123fc"></a>

### `bt_le_ext_adv_update_param()`

```c
int bt_le_ext_adv_update_param ( struct bt_le_ext_adv * adv, const struct bt_le_adv_param * param )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

更新广播参数（Advertising Parameters）。

更新广播参数。如果广播集当前正在广播，本函数返回错误。调用前应先停止广播集。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `param` | 广播参数（Advertising Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga40f2f7fdb09aba3c5137f680e67792f0"></a>

### `bt_le_filter_accept_list_add()`

```c
int bt_le_filter_accept_list_add ( const bt_addr_le_t * addr)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

将低功耗蓝牙设备（LE Device）添加到过滤接受列表（Filter Accept List）。

将对端设备的 LE 地址加入过滤接受列表（Filter Accept List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙 LE 身份地址（Identity Address）。 |

**说明（Note）**：注意：当某个 LE 角色正在使用过滤接受列表（Filter Accept List）时，不能修改它。例如广播者或扫描器使用该列表，或者正在通过该列表自动连接设备。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="gac87df899d1e363c63162988157ee6d00"></a>

### `bt_le_filter_accept_list_clear()`

```c
int bt_le_filter_accept_list_clear ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

清空过滤接受列表（Filter Accept List）。

清空过滤接受列表（Filter Accept List）中的所有设备。

**说明（Note）**：注意：当某个 LE 角色正在使用过滤接受列表（Filter Accept List）时，不能修改它。例如广播者或扫描器使用该列表，或者正在通过该列表自动连接设备。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga0532ed768ab4f9d69c202066d2f87e66"></a>

### `bt_le_filter_accept_list_remove()`

```c
int bt_le_filter_accept_list_remove ( const bt_addr_le_t * addr)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

从过滤接受列表（Filter Accept List）移除低功耗蓝牙设备（LE Device）。

从过滤接受列表（Filter Accept List）移除对端设备的 LE 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙 LE 身份地址（Identity Address）。 |

**说明（Note）**：注意：当某个 LE 角色正在使用过滤接受列表（Filter Accept List）时，不能修改它。例如广播者或扫描器使用该列表，或者正在通过该列表自动连接设备。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga650faa2a86f54499f4bc5a8657a55a87"></a>

### `bt_le_get_local_features()`

```c
int bt_le_get_local_features ( struct bt_le_local_features * local_features)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取本地低功耗蓝牙控制器特性（Bluetooth LE Controller Features）。

只能在 `bt_enable` 之后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `local_features` | 要填充信息的本地特性结构（Local Features Struct）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EAGAIN` | 信息尚不可用。 |
| `-EINVAL` | `local_features` 为 `NULL`。 |

<a id="ga296d1adf3c9ed2f2c65bb75b887d59ee"></a>

### `bt_le_oob_get_local()`

```c
int bt_le_oob_get_local ( uint8_t id, struct bt_le_oob * oob )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取本地低功耗蓝牙带外信息（LE Out of Band Information，OOB）。

本函数获取本地信息，可用于带外配对（Out of Band Pairing）或连接创建。

启用隐私配置 `CONFIG_BT_PRIVACY` 时，这会生成新的可解析私有地址（Resolvable Private Address，RPA），有效期为 `CONFIG_BT_RPA_TIMEOUT` 秒。此地址用于由 `bt_le_adv_start` 启动的广播、主动扫描及连接创建。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] id` | 本地身份句柄（Identity Handle），通常为 `BT_ID_DEFAULT`，对应本次函数调用所针对的身份地址。 |
| `[out] oob` | LE 带外信息（LE OOB Information）。 |

**说明（Note）**：注意：启用隐私功能时，若正在创建连接，则不能刷新可解析私有地址（RPA），应等待连接完成回调（Connected Callback）。此外，未启用扩展广播配置 `CONFIG_BT_EXT_ADV`，或控制器不支持扩展广播时，以下情况也不能刷新：广播者使用随机静态身份地址（Random Static Identity Address）作为另一个本地身份地址并已启用；或者本地身份地址与其他角色使用的本地身份地址冲突。本函数随机生成配对流程使用的密码材料，每次新的配对流程都应重新调用。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga27c4961f3c7270a7f1caeadb4107854b"></a>

### `bt_le_per_adv_list_add()`

```c
int bt_le_per_adv_list_add ( const bt_addr_le_t * addr, uint8_t sid )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

向周期性广播列表（Periodic Advertising List）添加设备。

将对端设备的 LE 地址加入周期广播列表（Periodic Advertising List），使得可以自动创建与该设备的周期广播同步。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙 LE 身份地址（Identity Address）。 |
| `sid` | 广播集标识符（SID）。此值从扫描回调的 `bt_le_scan_recv_info` 获取。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga5909bd768c23a19a42a660e3b814c981"></a>

### `bt_le_per_adv_list_clear()`

```c
int bt_le_per_adv_list_clear ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

清空周期性广播列表（Periodic Advertising List）。

清空整个周期广播列表（Periodic Advertising List）。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga100efac4a49984e06202c63c4e5955cd"></a>

### `bt_le_per_adv_list_remove()`

```c
int bt_le_per_adv_list_remove ( const bt_addr_le_t * addr, uint8_t sid )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

从周期性广播列表（Periodic Advertising List）移除设备。

从周期广播列表（Periodic Advertising List）移除对端设备的 LE 地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 蓝牙 LE 身份地址（Identity Address）。 |
| `sid` | 广播集标识符（SID）。此值从扫描回调的 `bt_le_scan_recv_info` 获取。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gafd0e7ccca93a8347a4ca6cca88e77899"></a>

### `bt_le_per_adv_set_data()`

```c
int bt_le_per_adv_set_data ( const struct bt_le_ext_adv * adv, const struct bt_data * ad, size_t ad_len )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置或更新周期性广播数据（Periodic Advertising Data）。

只能在既不可扫描、不可连接、也不匿名的扩展广播集上设置或更新周期广播数据。也就是说，不能为 `adv` 设置广播选项 `BT_LE_ADV_OPT_SCANNABLE`、`BT_LE_ADV_OPT_CONN` 和 `BT_LE_ADV_OPT_ANONYMOUS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `ad` | 广播数据（Advertising Data）。 |
| `ad_len` | 广播数据长度。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gac96199a4e5e6cfb789c1bd1c0e67d6fe"></a>

### `bt_le_per_adv_set_info_transfer()`

```c
int bt_le_per_adv_set_info_transfer ( const struct bt_le_ext_adv * adv, const struct bt_conn * conn, uint16_t service_data )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

传输有关周期性广播集（Periodic Advertising Set）的信息。

这使另一设备能够快速同步到本设备的周期广播集（Periodic Advertising Set）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 要传输信息的周期广播集。 |
| `conn` | 将接收信息的对端设备。 |
| `service_data` | 提供给远端主机的应用服务数据（Application Service Data）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaa72029a2759123ec776061d2e80bf3a1"></a>

### `bt_le_per_adv_set_param()`

```c
int bt_le_per_adv_set_param ( struct bt_le_ext_adv * adv, const struct bt_le_per_adv_param * param )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置或更新周期性广播参数（Periodic Advertising Parameters）。

只能在既不可扫描、不可连接、也不匿名的扩展广播集上设置或更新周期广播参数。也就是说，不能为 `adv` 设置广播选项 `BT_LE_ADV_OPT_SCANNABLE`、`BT_LE_ADV_OPT_CONN` 和 `BT_LE_ADV_OPT_ANONYMOUS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |
| `param` | 广播参数（Advertising Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaae6b8583f7d5457f20b03dccd146425e"></a>

### `bt_le_per_adv_set_response_data()`

```c
int bt_le_per_adv_set_response_data ( struct bt_le_per_adv_sync * per_adv_sync, const struct bt_le_per_adv_response_params * params, const struct net_buf_simple * data )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置带响应周期性广播（PAwR）中特定子事件的某个响应时隙（Response Slot）的数据。

应用调用本函数设置响应数据。每个响应时隙（Response Slot）的数据只能发送一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `params` | 参数（Parameters）。 |
| `data` | 要发送的响应数据。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga7de30fe5040b85bb9212e3a8fec4ac45"></a>

### `bt_le_per_adv_set_subevent_data()`

```c
int bt_le_per_adv_set_subevent_data ( const struct bt_le_ext_adv * adv, uint8_t num_subevents, const struct bt_le_per_adv_subevent_data_params * params )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置带响应的周期性广播（Periodic Advertising with Responses）的子事件数据。

响应数据请求，为带响应周期广播（Periodic Advertising with Responses，PAwR）广播者的一个或多个子事件设置数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 该带响应周期广播（PAwR）序列所属的扩展广播者。 |
| `num_subevents` | 要设置数据的子事件数量。 |
| `params` | 子事件参数（Subevent Parameters）。 |

**说明（Note）**：前置条件：`params` 中有 `num_subevents` 个元素，且控制器已请求 `params` 中这些子事件的数据。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga0f23f4ed48e8679646f247ea0d687094"></a>

### `bt_le_per_adv_start()`

```c
int bt_le_per_adv_start ( struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

启动周期性广播（Periodic Advertising）。

周期广播（Periodic Advertising）可独立于扩展广播（Extended Advertising）启用，但在发送任何周期广播数据之前，两者都必须启用。周期广播和扩展广播可按任意顺序启用。

周期广播启用后将持续进行，直到调用 `bt_le_per_adv_stop`，或者通过 `bt_le_ext_adv_delete` 删除广播集。调用 `bt_le_ext_adv_stop` 不会停止周期广播。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga1b15206fc552d597c12af369d48ff7d5"></a>

### `bt_le_per_adv_stop()`

```c
int bt_le_per_adv_stop ( struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

停止周期性广播（Periodic Advertising）。

周期广播（Periodic Advertising）可独立于扩展广播（Extended Advertising）禁用。禁用周期广播不会禁用扩展广播。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga4ee87bbf79e6ac844d14c3dafb2dadf4"></a>

### `bt_le_per_adv_sync_cb_register()`

```c
int bt_le_per_adv_sync_cb_register ( struct bt_le_per_adv_sync_cb * cb)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

注册周期性广播同步回调（Periodic Advertising Sync Callbacks）。

将回调结构加入周期广播同步（Periodic Advertising Sync）的回调结构列表。

所有周期广播同步活动都会调用此回调，包括同步成功、同步终止及收到数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EEXIST` | `cb` 已注册（Registered）时。 |

<a id="gab1576c66b08dc855b2d17fc562f36724"></a>

### `bt_le_per_adv_sync_cb_unregister()`

```c
int bt_le_per_adv_sync_cb_unregister ( struct bt_le_per_adv_sync_cb * cb)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

注销周期性广播同步回调（Periodic Advertising Sync Callbacks）。

从周期广播同步回调列表中移除该回调结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Zero` | 成功时的返回值；否则返回负错误码。译注：原文仅写“on success”，未在此说明成功值。 |

<a id="ga061bf84b989b2c96ab51d2ca0debb017"></a>

### `bt_le_per_adv_sync_create()`

```c
int bt_le_per_adv_sync_create ( const struct bt_le_per_adv_sync_param * param, struct bt_le_per_adv_sync ** out_sync )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

创建周期性广播同步对象（Periodic Advertising Sync Object）。

创建周期广播同步对象（Periodic Advertising Sync Object），用于尝试同步广播者的周期广播报告。此时应禁用扫描，或者启用扩展扫描（Extended Scan）。

本函数不会超时，将持续查找广播者，直到找到它或调用 `bt_le_per_adv_sync_delete`。因此，如果预期应在合理时间内找到广播者，建议使用本功能时自行实现超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] param` | 周期广播同步参数（Periodic Advertising Sync Parameters）。 |
| `[out] out_sync` | 周期广播同步对象（Periodic Advertising Sync Object）。译注：原文为不完整短语“Periodic advertising sync object on.”，未补充其末尾缺失的含义。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaa0c218ff3c78b26dcfaa726ee30267a6"></a>

### `bt_le_per_adv_sync_delete()`

```c
int bt_le_per_adv_sync_delete ( struct bt_le_per_adv_sync * per_adv_sync)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

删除周期性广播同步（Periodic Advertising Sync）。

删除周期广播同步对象（Periodic Advertising Sync Object）。无论同步处于何种状态，都可以调用。如果正在同步，则取消同步；如果已建立同步，则终止同步。之后，该周期广播同步对象失效。

如果同步对象正在同步，必须等控制器完成取消该对象后，才能创建新的周期广播同步对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga8d05bd864d98b5b43595eb256e464024"></a>

### `bt_le_per_adv_sync_get_index()`

```c
uint8_t bt_le_per_adv_sync_get_index ( struct bt_le_per_adv_sync * per_adv_sync)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取周期性广播同步对象（Periodic Advertising Sync Object）的数组索引。

本函数获取周期广播同步对象数组中的索引。该数组有 `CONFIG_BT_PER_ADV_SYNC_MAX` 个元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |

**返回（Returns）**：返回值：周期广播同步对象的索引，范围为 `0..CONFIG_BT_PER_ADV_SYNC_MAX-1`。

<a id="gabfaf265a48dd09ea02d114e2023c14a6"></a>

### `bt_le_per_adv_sync_get_info()`

```c
int bt_le_per_adv_sync_get_info ( struct bt_le_per_adv_sync * per_adv_sync, struct bt_le_per_adv_sync_info * info )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

获取周期性广播同步信息（Periodic Advertising Sync Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic Advertising Sync Object）。 |
| `info` | 周期广播同步信息对象（Periodic Advertising Sync Info Object）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga83126917373c0bcaa24964dd1d8bde46"></a>

### `bt_le_per_adv_sync_lookup_addr()`

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_addr ( const bt_addr_le_t * adv_addr, uint8_t sid )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

根据广播者地址查找现有周期性广播同步对象（Periodic Advertising Sync Object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv_addr` | 广播者地址（Advertiser Address）。 |
| `sid` | 周期广播集标识符（Periodic Advertising Set ID）。 |

**返回（Returns）**：返回值：周期广播同步对象；未找到时返回 `NULL`。

<a id="ga59532b37412b1b93f81cf5cc1bab0534"></a>

### `bt_le_per_adv_sync_lookup_index()`

```c
struct bt_le_per_adv_sync * bt_le_per_adv_sync_lookup_index ( uint8_t index)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

根据数组索引获取周期性广播同步对象（Periodic Advertising Sync Object）。

本函数根据数组索引获取周期广播同步对象。该数组有 `CONFIG_BT_PER_ADV_SYNC_MAX` 个元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 周期广播同步对象的索引，范围为 `0..CONFIG_BT_PER_ADV_SYNC_MAX-1`。 |

**返回（Returns）**：返回值：数组索引对应的周期广播同步对象；索引无效时返回 `NULL`。

<a id="ga3dc0c6a0c6a77f4db63ee2ff8329a4c5"></a>

### `bt_le_per_adv_sync_recv_disable()`

```c
int bt_le_per_adv_sync_recv_disable ( struct bt_le_per_adv_sync * per_adv_sync)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

禁止某个同步接收周期性广播报告（Periodic Advertising Reports）。

如果已经禁用同步报告接收，返回 `-EALREADY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga07e4510de7e72c6ed6196b3da9fb40be"></a>

### `bt_le_per_adv_sync_recv_enable()`

```c
int bt_le_per_adv_sync_recv_enable ( struct bt_le_per_adv_sync * per_adv_sync)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

允许某个同步接收周期性广播报告（Periodic Advertising Reports）。

如果该同步已经在接收报告，返回 `-EALREADY`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga731f4b37a9e5cc13a6816ea23f751b0b"></a>

### `bt_le_per_adv_sync_subevent()`

```c
int bt_le_per_adv_sync_subevent ( struct bt_le_per_adv_sync * per_adv_sync, struct bt_le_per_adv_sync_subevent_params * params )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

与子事件（Subevents）的一个子集同步。

在发出此命令之前，控制器同步到哪些子事件（Subevent）是未指定的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `params` | 子事件同步参数（Subevent Sync Parameters）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaf81a1dd7a628d1a2f25c6b53b0679809"></a>

### `bt_le_per_adv_sync_transfer()`

```c
int bt_le_per_adv_sync_transfer ( const struct bt_le_per_adv_sync * per_adv_sync, const struct bt_conn * conn, uint16_t service_data )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

将周期性广播同步信息（Periodic Advertising Sync Information）传输给对端设备。

这使另一设备能够快速同步到本设备当前已同步的同一周期广播序列（Periodic Advertising Train）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `per_adv_sync` | 要传输的周期广播同步（Periodic Advertising Sync）。 |
| `conn` | 将接收同步信息的对端设备。 |
| `service_data` | 提供给远端主机的应用服务数据（Application Service Data）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaa0658bd53df1d5e8e89e13330e4fd0ae"></a>

### `bt_le_per_adv_sync_transfer_subscribe()`

```c
int bt_le_per_adv_sync_transfer_subscribe ( const struct bt_conn * conn, const struct bt_le_per_adv_sync_transfer_param * param )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

设置参数，允许其他设备传输周期广播同步（Periodic Advertising Sync）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要设置参数的连接。若为 `NULL`，则设置适用于所有连接的默认参数；针对特定连接设置的参数始终优先。 |
| `param` | 周期广播同步传输参数（Periodic Advertising Sync Transfer Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga08f872078045bbef4aca19761f25eeb8"></a>

### `bt_le_per_adv_sync_transfer_unsubscribe()`

```c
int bt_le_per_adv_sync_transfer_unsubscribe ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

取消订阅周期性广播同步传输（Periodic Advertising Sync Transfers，PAST）。

移除允许其他设备传输周期广播同步的参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要移除参数的连接。若为 `NULL`，则移除适用于所有连接的默认参数。取消订阅特定设备后，其他设备仍可传输周期广播同步。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga59e9fc635846ab92af19d483de58ed88"></a>

### `bt_le_per_adv_update_did()`

```c
int bt_le_per_adv_update_did ( const struct bt_le_ext_adv * adv)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

更新周期性广播的广播数据标识符（Advertising Data Identifier，DID），不改变数据。

发送操作类型为“数据不变”（Unchanged Data）的 HCI 命令，使控制器更新周期广播协议数据单元（PDU）中的广播数据信息（ADI）字段，即 DID，而不修改广播数据载荷。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising Set Object）。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV` 时可用。

**说明（Note）**：注意：调用本函数前，广播集必须已通过 `bt_le_per_adv_start` 启动周期广播，必须包含数据，并且已通过 `BT_LE_PER_ADV_OPT_INCLUDE_ADI` 启用 ADI 包含功能。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga80e870fa1de40c404c64624bef439067"></a>

### `bt_le_scan_cb_register()`

```c
int bt_le_scan_cb_register ( struct bt_le_scan_cb * cb)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

注册扫描器数据包回调（Scanner Packet Callbacks）。

将回调结构加入监视扫描器活动的回调结构列表。

所有扫描器活动都会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EEXIST` | `cb` 已注册（Registered）时。 |

<a id="gac2718f2128b3f8c79b12d760771c8378"></a>

### `bt_le_scan_cb_unregister()`

```c
void bt_le_scan_cb_unregister ( struct bt_le_scan_cb * cb)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

注销扫描器数据包回调（Scanner Packet Callbacks）。

从扫描器回调列表中移除该回调结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

<a id="gac5e19c26b53a08dadb8efa7ecc692ad6"></a>

### `bt_le_scan_start()`

```c
int bt_le_scan_start ( const struct bt_le_scan_param * param, bt_le_scan_cb_t cb )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

启动低功耗蓝牙扫描（LE Scanning）。

使用给定参数启动 LE 扫描，并通过指定回调提供结果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 扫描参数（Scan parameters）。 |
| `cb` | 通知扫描结果的回调。如果倾向于通过 `bt_le_scan_cb_register` 注册回调，则本参数可以为 `NULL`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 如果扫描器已经在另一个线程中启动过程中。 |
| `-EINVAL` | 如果已设置 `BT_LE_SCAN_OPT_EXT_FILTER_POLICY`，但禁用了 `CONFIG_BT_SCAN_EXT_FILTER_POLICY`。 |
| `-ENOTSUP` | 如果已设置 `BT_LE_SCAN_OPT_EXT_FILTER_POLICY`，但控制器不支持扩展扫描器过滤策略（Extended Scanner Filter Policies）。 |

**说明（Note）**：注意：禁用 `CONFIG_BT_PRIVACY` 时，LE 扫描器默认不使用本地设备的身份地址（Identity Address），防止主动扫描器向广播者请求附加信息时泄露身份地址。若要启用定向广播报告，必须启用 `CONFIG_BT_SCAN_WITH_IDENTITY`。这一限制不适用于控制器无法解析目标地址的定向广播：使用 `BT_LE_SCAN_OPT_EXT_FILTER_POLICY` 时始终报告它们，因为它们无法泄露本地身份地址。启用 `CONFIG_BT_PRIVACY` 且 `param.type` 为 `BT_LE_SCAN_TYPE_ACTIVE` 时，不支持设置 `param.timeout`；提供非零超时将返回 `-EINVAL`。通过 `CONFIG_BT_EXT_ADV` 启用扩展广播支持后，扫描器会自动扫描扩展广播包。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="gaa2de1a1ab523606b36a4c445fb0c3b84"></a>

### `bt_le_scan_stop()`

```c
int bt_le_scan_stop ( void )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

停止低功耗蓝牙扫描（LE Scanning）。

停止正在进行的 LE 扫描。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 扫描器正在另一个线程中启动或停止。 |

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="gabc115fd3fff6d00ae878a31613bf70aa"></a>

### `bt_le_set_chan_map()`

```c
int bt_le_set_chan_map ( uint8_t chan_map[5])
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置低功耗蓝牙信道映射（LE Channel Map）。

用于通知控制器已知的信道分类（Channel Classification）。主机可将信道映射中的相应位分别设为 0 或 1，指示信道质量差或未知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan_map` | 信道映射（Channel Map）。共 5 个八位组，每一位表示一个信道；仅低 37 位有效。 |

**说明（Note）**：注意：连续两次调用本函数之间必须至少间隔一秒。

**返回（Returns）**：返回值（Returns）：成功返回 0，否则返回错误码；协议错误返回正值，协议栈内部错误返回负的 POSIX 错误码。

<a id="ga9ab41e118b5496c196e56b8b5d023275"></a>

### `bt_le_set_rpa_timeout()`

```c
int bt_le_set_rpa_timeout ( uint16_t new_rpa_timeout)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

在运行时设置可解析私有地址（Resolvable Private Address）的超时时间。

新的可解析私有地址（RPA）超时值用于下一次 RPA 轮换及之后所有轮换，直到通过本 API 安排另一次覆盖值。

初始时使用 `CONFIG_BT_RPA_TIMEOUT` 作为 RPA 超时时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `new_rpa_timeout` | 可解析私有地址（Resolvable Private Address，RPA）超时时间，单位为秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | RPA 超时值无效。有效范围为 1–3600 秒。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_RPA_TIMEOUT_DYNAMIC` 时可用。

<a id="gaf0729453790aab1bd3d52c623be3b35a"></a>

### `bt_set_appearance()`

```c
int bt_set_appearance ( uint16_t new_appearance)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置本地蓝牙外观值（Bluetooth Appearance）。

启用 `CONFIG_BT_SETTINGS` 时，自动保存新的外观值（Appearance），使其在重启后保留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `new_appearance` | 外观值（Appearance Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `other` | 持久化存储失败，外观值未更新。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC` 时可用。

<a id="gac8bb3609a3d6da69ff736809e45f5c8a"></a>

### `bt_set_name()`

```c
int bt_set_name ( const char * name)
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

设置蓝牙设备名称（Bluetooth Device Name）。

设置蓝牙 GAP 设备名称（Device Name）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 新名称，必须以空字符（NUL）结尾。 |

**说明（Note）**：注意：广播数据不会自动更新。如果广播数据中包含设备名称，调用本函数后，应通过 `bt_le_adv_update_data` 或 `bt_le_ext_adv_set_data` 更新其中的名称。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_DEVICE_NAME_DYNAMIC` 时可用。

**参阅（See Also）**：另见：`CONFIG_BT_DEVICE_NAME_MAX`。

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="gaceabbbe6e844650f791010e53c9df6a4"></a>

### `bt_unpair()`

```c
int bt_unpair ( uint8_t id, const bt_addr_le_t * addr )
```

```c
#include <zephyr/bluetooth/bluetooth.h>
```

清除配对信息（Pairing Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份句柄（Identity Handle），通常为 `BT_ID_DEFAULT`，对应本次函数调用所针对的身份地址。 |
| `addr` | 远端地址。使用 `NULL` 或 `BT_ADDR_LE_ANY` 可清除所有远端设备。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。


## 1.10\_原页交叉引用（Cross References）

- [定义与分配编号（Defines and Assigned Numbers）](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md)
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
- [bt_br_discovery_result](../bluetooth_service_model_reference/P013_bt_br_discovery_result_结构体.md)
- [bt_br_discovery_param](../bluetooth_service_model_reference/P012_bt_br_discovery_param_结构体.md)
- [bt_br_discovery_cb](../bluetooth_service_model_reference/P011_bt_br_discovery_cb_结构体.md)
- [bt_br_oob](../bluetooth_service_model_reference/P015_bt_br_oob_结构体.md)
- [bt_br_page_scan_param](../bluetooth_service_model_reference/P016_bt_br_page_scan_param_结构体.md)
- [bt_br_inquiry_scan_param](../bluetooth_service_model_reference/P014_bt_br_inquiry_scan_param_结构体.md)
- [bt_br_bond_info](../bluetooth_service_model_reference/P009_bt_br_bond_info_结构体.md)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a81b4b9ce53511c62889790a79b0f6a34)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/classic/classic.h](../api_file_audio_test_reference/P005_zephyr__bluetooth__classic__classic.h_文件参考.md)
- [zephyr/bluetooth/bluetooth.h](../api_file_bluetooth_media_reference/P001_zephyr__bluetooth__bluetooth.h_文件参考.md)
- [BT_GAP_ADV_FAST_INT_MIN_2](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga9573e6bcdae3aae9d51c0becbbd7ac60)
- [BT_GAP_ADV_FAST_INT_MAX_2](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gaebc3ce60836522d883f664227a3ffcfb)
- [BT_GAP_ADV_FAST_INT_MIN_1](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga397a52fe616416665b46a2bc454c2e11)
- [BT_GAP_ADV_FAST_INT_MAX_1](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga13acf16d3d8edd39636bb10df752775a)
- [BT_GAP_PER_ADV_SLOW_INT_MIN](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gab51898ce46ee9ae468ed7ffc1d117321)
- [BT_GAP_PER_ADV_SLOW_INT_MAX](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gaa618da2a7c217527b0d962315caa1c22)
- [BT_GAP_SCAN_FAST_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga747caa714962215453a966a323e77cf8)
- [BT_GAP_SCAN_FAST_WINDOW](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga100e1c20813630848a1a80390e8a06a0)
- [BT_GAP_SCAN_FAST_INTERVAL_MIN](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gae9356673ee78d9abb27891738344513a)
- [BT_GAP_RSSI_INVALID](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga64b5c5e429dadf1e875984f69cd399dc)
- [bt_gap_adv_type](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga07833ed1f79708d5f6a5d0c2e01d4dca)
- [bt_conn_cb::recycled](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a1bd8d99988ad0ae3f79aad3d03fcbd8b)
- [bt_conn_cb::connected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#ab3618150bfeea9492095ba27ce978c69)
- [CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_AUTO_READ_CENTRAL_ADDR_RES)
- [bt_le_adv_param::options](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a2a978c60153eb03697769bc72928f4ef)
- [CONFIG_BT_EXT_ADV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV)
- [CONFIG_BT_EXT_ADV_CODING_SELECTION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV_CODING_SELECTION)
- [bt_le_adv_param::tx_power](../bluetooth_connection_model_reference/P092_bt_le_adv_param_结构体.md#a1c09c2bcf9600a644e194ecd3367d200)
- [bt_le_ext_adv_info::tx_power](../bluetooth_connection_model_reference/P105_bt_le_ext_adv_info_结构体.md#a485e4a8124fddee897fe744836cbfb24)
- [BT_HCI_LE_ADV_TX_POWER_NO_PREF](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a7f4fcc517033a4743ded39503b35ce29)
- [bt_le_scan_recv_info::direct_addr](../bluetooth_connection_model_reference/P129_bt_le_scan_recv_info_结构体.md#a8885283f39e3ece5d7ff7d5b5d588696)
- [CONFIG_BT_SCAN_EXT_FILTER_POLICY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_EXT_FILTER_POLICY)
- [BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga01883ae9792f486644dc96dd0559c72d)
- [CONFIG_BT_ACCEPT_CONN_AS_CENTRAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ACCEPT_CONN_AS_CENTRAL)
- [CONFIG_BT_LIMITED_DISCOVERABLE_DURATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LIMITED_DISCOVERABLE_DURATION)
- [net_buf_simple_save](../api_sensor_network_buffer_reference/P001_网络缓冲区库（Network Buffer Library）.md#gabf5b098aa0926d9b7fb88baff8a3e2d8)
- [net_buf_simple_restore](../api_sensor_network_buffer_reference/P001_网络缓冲区库（Network Buffer Library）.md#gaedd36481657a7a9d108659d56e131721)
- [CONFIG_BT_SETTINGS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS)
- [settings_load](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#ga89c6d618df81f197cc5c1a2018b00648)
- [bt_conn_cb_register](../api_bluetooth_connection_reference/P001_连接管理（Connection management）.md#gaa9b79cd44734c1e560d6f30509be4d0b)
- [settings_load_subtree](https://docs.zephyrproject.org/latest/doxygen/html/group__settings.html#gab80e8a21c80243359b652386f7ce2424)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [CONFIG_BT_HCI_SET_PUBLIC_ADDR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SET_PUBLIC_ADDR)
- [CONFIG_BT_PRIVACY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PRIVACY)
- [CONFIG_BT_ID_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ID_MAX)
- [BT_ADDR_LE_ANY](../api_usb_gnss_topic_reference/P002_设备地址（Device Address）.md#ga17e9efacd50c682b2f709c217e920d48)
- [BT_HCI_LE_ADV_TX_POWER_MIN](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#aa4ce6784e6ee46069fd109dc1869e716)
- [BT_HCI_LE_ADV_TX_POWER_MAX](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#aa3bfec7459966cf805afcf5186d53103)
- [bt_conn_auth_info_cb::addr_res_support_read](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md#a44896258f0221d4f0a55cc1fb785b06c)
- [CONFIG_BT_EXT_ADV_MAX_ADV_SET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV_MAX_ADV_SET)
- [CONFIG_BT_RPA_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA_TIMEOUT)
- [BT_GAP_ADV_MAX_ADV_DATA_LEN](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga39ab5040c9471631486da7dbebd9c36f)
- [BT_GAP_ADV_MAX_EXT_ADV_DATA_LEN](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga53af114e4925482739dc50dc84c2f641)
- [bt_le_ext_adv_cb::sent](../bluetooth_connection_model_reference/P103_bt_le_ext_adv_cb_结构体.md#a85b8887c9ef443d18b71e9561e7dde60)
- [CONFIG_BT_PER_ADV_SYNC_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_MAX)
- [CONFIG_BT_PER_ADV](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV)
- [CONFIG_BT_SCAN_WITH_IDENTITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_WITH_IDENTITY)
- [CONFIG_BT_RPA_TIMEOUT_DYNAMIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA_TIMEOUT_DYNAMIC)
- [CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_APPEARANCE_DYNAMIC)
- [CONFIG_BT_DEVICE_NAME_DYNAMIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_DYNAMIC)
- [CONFIG_BT_DEVICE_NAME_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME_MAX)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__gap_html_gaff027ae0fe3fbac63db9c87f8e480214"></a>
<a id="astructbt__br__inquiry__scan__param_html"></a>
<a id="agroup__bt__gap_html_ga1770fa93707cf5ea6b57498be1aa9b26"></a>
<a id="agroup__bt__gap_html_ga6bc842be90369deb05fb4720ced19395"></a>
<a id="agroup__bt__gap_html_ga7a9e4560e84fa43e7c1f3cad39bdf24e"></a>
<a id="agroup__bt__gap_html_gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7"></a>
<a id="astructbt__br__page__scan__param_html"></a>
<a id="agroup__bt__gap_html_ga17ea91d5b363d5dba321cc38e4283dbc"></a>
<a id="agroup__bt__gap_html_ga4d053fafbc0faed58c3305efdd581838"></a>
<a id="agroup__bt__gap_html_gaf1bfd9a2c5a846a1232520de20a326eb"></a>
<a id="agroup__bt__gap_html_gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d"></a>
<a id="agroup__bt__gap_html_ga1bd5dcfa2c47bacca1bdaee493d261c4"></a>
<a id="agroup__bt__gap_html_gadd743fae64449eaf337566a19e06fc6d"></a>
<a id="agroup__bt__gap_html_ga61c49f57aea54f455ef89de40c354cc5"></a>
<a id="agroup__bt__gap_html_ga6c2a8ae86cb80756beee0bcbdb18c8b6"></a>
<a id="agroup__bt__gap_html_ga05ad85ffd00e23052ab5cbb6ff5ee709"></a>
<a id="agroup__bt__gap_html_ga13e5b00e35b3c338c0326dbee03c9268"></a>
<a id="agroup__bt__gap_html_gaf26216f17eb0142791decac9377538f4"></a>
<a id="agroup__bt__gap_html_gaf955175076f985e932c0ab0ed9e58743"></a>
<a id="agroup__bt__gap_html_ga365abe1219cb283880f93de9b7f2e3d3"></a>
<a id="agroup__bt__gap_html_ga440177ed725266616455bd135f414ea8"></a>
<a id="agroup__bt__gap_html_ga9557269dd36b624b49e76c511c3a0cc1"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169"></a>
<a id="agroup__bt__gap__defines_html_ga9573e6bcdae3aae9d51c0becbbd7ac60"></a>
<a id="agroup__bt__gap__defines_html_gaebc3ce60836522d883f664227a3ffcfb"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872"></a>
<a id="agroup__bt__gap__defines_html_ga13acf16d3d8edd39636bb10df752775a"></a>
<a id="agroup__bt__gap__defines_html_ga397a52fe616416665b46a2bc454c2e11"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e"></a>
<a id="astructbt__le__adv__param_html"></a>
<a id="agroup__bt__gap_html_gaded4b52c9bb87fd4d19b1eb9361973e5"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab"></a>
<a id="agroup__bt__gap_html_ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9"></a>
<a id="astructbt__le__ext__adv__start__param_html"></a>
<a id="agroup__bt__gap__defines_html_gaa618da2a7c217527b0d962315caa1c22"></a>
<a id="agroup__bt__gap__defines_html_gab51898ce46ee9ae468ed7ffc1d117321"></a>
<a id="agroup__bt__gap_html_gaf46e54f8fcda7b65b659685bb225d243"></a>
<a id="agroup__bt__gap_html_ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518"></a>
<a id="astructbt__le__per__adv__param_html"></a>
<a id="agroup__bt__gap__defines_html_ga100e1c20813630848a1a80390e8a06a0"></a>
<a id="agroup__bt__gap__defines_html_ga747caa714962215453a966a323e77cf8"></a>
<a id="agroup__bt__gap_html_ga57ace75133343ba8de7fa965f452ee3d"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394"></a>
<a id="agroup__bt__gap_html_ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22"></a>
<a id="agroup__bt__gap__defines_html_gae9356673ee78d9abb27891738344513a"></a>
<a id="agroup__bt__gap_html_ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb"></a>
<a id="agroup__bt__gap_html_ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006"></a>
<a id="astructbt__le__scan__param_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabfc34fe6f398d6526acc7c5afde8a689ac01fd21779b5c5bcd883ab4f678ef26f"></a>
<a id="ggabfc34fe6f398d6526acc7c5afde8a689ab5ad28e0358b20440da3851278a69e97"></a>
<a id="ggabfc34fe6f398d6526acc7c5afde8a689af1920d7300473810a412d508dfddf95a"></a>
<a id="ggabfc34fe6f398d6526acc7c5afde8a689a22574d1fc663afc2595ce8222867ee35"></a>
<a id="ggabfc34fe6f398d6526acc7c5afde8a689aee59dd0540295ce4313804ce08c07908"></a>
<a id="gga03757f934de6f13f95f02316b098875da53ce32b8981ffb385d1f680f11d8feb7"></a>
<a id="gga03757f934de6f13f95f02316b098875daac2a0585a4115768dcac602ffe87399d"></a>
<a id="ggaad0039d4b524a0eef31158dc9b24a497a32a025f5c47db4957e72d292e748eda9"></a>
<a id="ggaad0039d4b524a0eef31158dc9b24a497a1fcee00e6de549746f81de0bf43caeab"></a>
<a id="ggaad0039d4b524a0eef31158dc9b24a497a1d636d176d18199b7d5bcb17865b3a1c"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a928b376123819cb0a69fbb5b35608dbf"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28aa1407c130bb1cdf1e1dcaaac457d3169"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a407cf5ae358d3c00dd7e47dfaad3ec6e"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28afd164ec5476f5e2d9aedf50032946872"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28abdcf1c80662061fa30575e1f9fc6cf6f"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a807ba316edc49c8448a8ff7d497173f5"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ad5efef3d01731110dbd71d5a5dc9baaf"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a1563b053f457833d1a3d11c8dc4d394b"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ae60eafe69ef10b84f61a1f4accf789c9"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ae33ae9d8e43cce82e47fa73999d415ab"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ae864aefcdfbecaffe823b9b144fe0a6b"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ad01c4962a350d3218ba0cabd713708b1"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a185e0f884f8b0ce79625448638de8fab"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28aecff4fe3ac3d1fba3f6fa76c77713859"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ab46741616f8bfe50c4b492d1f7970779"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28abd9cb02691d7e025fe3fea9a80123275"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a89f7494620236c976bf1a76a880e2a28"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a22958d8539d661ad7ca8d3f1173e7e5e"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28a9a35ede118224d6ed17f252fff6bb47e"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28aa6a61768ad4102f199d3970791118bb8"></a>
<a id="ggafbf81dab68b0e484d4742471c722fc28ab9ee87ad3a24312174ae46f904fe9c56"></a>
<a id="gga544ccde35638d8f580942d830fe9f242a4423f4792711b21cf38a4e63c148760d"></a>
<a id="gga544ccde35638d8f580942d830fe9f242afe851bf904c1cfed3ff10a57430d6a07"></a>
<a id="ggae60a45dde6b4d9f4c54a2a6070254f11aa2c689d726eacfb18d87655b1f587518"></a>
<a id="ggae60a45dde6b4d9f4c54a2a6070254f11a9524537e4cb726f4ff10ba93381bb27f"></a>
<a id="ggae60a45dde6b4d9f4c54a2a6070254f11a38cebc2ae885ff630b34c603e2ec6403"></a>
<a id="gga6bb77c0808c761753650cde28ddb013ead690730da823fcb31f102f154a23b01c"></a>
<a id="gga6bb77c0808c761753650cde28ddb013eac26ccfbb5c715b515ef82c1993eff03b"></a>
<a id="gga6bb77c0808c761753650cde28ddb013ea492cf25dc85090cfa72d5e2bdc0917f3"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9aeeef50a544edc104b39e4ef0c9a58d6c"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9ae35a6eb572a2842e4cc2fc3677e19b53"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9a9ec2b0c346c2cab7f61c2efcc8e37db2"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9aaa256e560f013eb74415d817154b8f4e"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9a99034652a92249e6d04065d68352020b"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9a0f52e38e513ec7eefcbc5c86c36f002e"></a>
<a id="ggac942d7e3cae8fca22080f93bf9528ee9a5c702876d70d5eadc4df6e59d96b8320"></a>
<a id="gga820c5f3721e72662e558cc4576b6111baef90aceabc3f9d0b17b7f3415152fca2"></a>
<a id="gga820c5f3721e72662e558cc4576b6111ba2694870b7ebd2dcd0b3834367f7d7061"></a>
<a id="gga820c5f3721e72662e558cc4576b6111bab0725048806858083be9ab3fcd9a36ed"></a>
<a id="gga820c5f3721e72662e558cc4576b6111ba433ae469b27e820fdfd2a1d562010991"></a>
<a id="gga820c5f3721e72662e558cc4576b6111baed2f78d682b5fbd1adf89c2f005e4f48"></a>
<a id="gga820c5f3721e72662e558cc4576b6111ba3f0be549ca5cac1cfbdec2f2227e73dc"></a>
<a id="gga820c5f3721e72662e558cc4576b6111bad924f620ed6fdadbbea03f8e343b9d0c"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996aad3f19e5849b6d6813fa88257082e185"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996a0af65ac48e068f7e6f1815cb151d4394"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996af7a25b6790b138b2b88de3c7d81cb0ae"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996a16f171c649dd090333e9822a92b4bbdb"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996a7ff0c79b2675e7b7512379e2cbedc0a6"></a>
<a id="ggab4b5773898e2a1eef21557915a21c996a79cdd7e96e41f4236642edfbcb1b666d"></a>
<a id="ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006"></a>
<a id="ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md)
