---
id: learning.zephyr-docs.api-bluetooth-connection-reference.page-1
title: 连接管理（Connection management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_连接管理（Connection management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接管理（Connection management）

<a id="details"></a>

连接管理（Connection Management）。引入版本（Since）：1.0。接口版本（Version）：1.0.1。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Fle_5Fconn_5Fparam"></a>

```c
struct bt_le_conn_param
```

相关声明：[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)。

低功耗蓝牙连接（LE Connection）的连接参数。

<a id="r_bt_5Fconn_5Fle_5Fphy_5Finfo"></a>

```c
struct bt_conn_le_phy_info
```

相关声明：[bt_conn_le_phy_info](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md)。

LE 连接的物理层（PHY）信息。

<a id="r_bt_5Fconn_5Fle_5Fphy_5Fparam"></a>

```c
struct bt_conn_le_phy_param
```

相关声明：[bt_conn_le_phy_param](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md)。

LE 连接的首选 PHY 参数。

<a id="r_bt_5Fconn_5Fle_5Fdata_5Flen_5Finfo"></a>

```c
struct bt_conn_le_data_len_info
```

相关声明：[bt_conn_le_data_len_info](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md)。

LE 连接的连接数据长度（Connection Data Length）信息。

<a id="r_bt_5Fconn_5Fle_5Fdata_5Flen_5Fparam"></a>

```c
struct bt_conn_le_data_len_param
```

相关声明：[bt_conn_le_data_len_param](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md)。

LE 连接的连接数据长度参数。

<a id="r_bt_5Fconn_5Fle_5Fsubrate_5Fparam"></a>

```c
struct bt_conn_le_subrate_param
```

相关声明：[bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)。

LE 连接的连接子速率参数。

<a id="r_bt_5Fconn_5Fle_5Fsubrating_5Finfo"></a>

```c
struct bt_conn_le_subrating_info
```

相关声明：[bt_conn_le_subrating_info](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md)。

LE 连接的子速率信息。

<a id="r_bt_5Fconn_5Fle_5Fsubrate_5Fchanged"></a>

```c
struct bt_conn_le_subrate_changed
```

相关声明：[bt_conn_le_subrate_changed](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md)。

LE 连接已更新的子速率（Subrating）连接参数。

<a id="r_bt_5Fconn_5Fle_5Fmin_5Fconn_5Finterval_5Fgroup"></a>

```c
struct bt_conn_le_min_conn_interval_group
```

相关声明：[bt_conn_le_min_conn_interval_group](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md)。

支持的最小连接间隔组（Minimum Supported Connection Interval Group）。

<a id="r_bt_5Fconn_5Fle_5Fmin_5Fconn_5Finterval_5Finfo"></a>

```c
struct bt_conn_le_min_conn_interval_info
```

相关声明：[bt_conn_le_min_conn_interval_info](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md)。

支持的最小连接间隔信息。

<a id="r_bt_5Fconn_5Fle_5Fconn_5Frate_5Fparam"></a>

```c
struct bt_conn_le_conn_rate_param
```

相关声明：[bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)。

低功耗（LE）连接的连接速率参数。

<a id="r_bt_5Fconn_5Fle_5Fconn_5Frate_5Fchanged"></a>

```c
struct bt_conn_le_conn_rate_changed
```

相关声明：[bt_conn_le_conn_rate_changed](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md)。

已更新的连接速率（Connection Rate）参数。

<a id="r_bt_5Fconn_5Fle_5Fread_5Fall_5Fremote_5Ffeat_5Fcomplete"></a>

```c
struct bt_conn_le_read_all_remote_feat_complete
```

相关声明：[bt_conn_le_read_all_remote_feat_complete](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)。

读取全部远端功能（Read All Remote Features）完成回调的参数。

<a id="r_bt_5Fconn_5Fle_5Fframe_5Fspace_5Fupdate_5Fparam"></a>

```c
struct bt_conn_le_frame_space_update_param
```

相关声明：[bt_conn_le_frame_space_update_param](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md)。

帧间隔更新（Frame Space Update）参数。

<a id="r_bt_5Fconn_5Fle_5Fframe_5Fspace_5Fupdated"></a>

```c
struct bt_conn_le_frame_space_updated
```

相关声明：[bt_conn_le_frame_space_updated](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md)。

帧间隔更新完成回调的参数。

<a id="r_bt_5Fconn_5Fle_5Fcs_5Fcapabilities"></a>

```c
struct bt_conn_le_cs_capabilities
```

相关声明：[bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)。

支持信道探测（Channel Sounding，CS）的 LE 连接的远端信道探测能力。

<a id="r_bt_5Fconn_5Fle_5Fcs_5Ffae_5Ftable"></a>

```c
struct bt_conn_le_cs_fae_table
```

相关声明：[bt_conn_le_cs_fae_table](../bluetooth_connection_model_reference/P016_bt_conn_le_cs_fae_table_结构体.md)。

支持 CS 的 LE 连接的远端 FAE 表（FAE Table）。

<a id="r_bt_5Fconn_5Fle_5Fcs_5Fconfig"></a>

```c
struct bt_conn_le_cs_config
```

相关声明：[bt_conn_le_cs_config](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md)。

信道探测（Channel Sounding）配置。

<a id="r_bt_5Fconn_5Fle_5Fcs_5Fsubevent_5Fresult"></a>

```c
struct bt_conn_le_cs_subevent_result
```

相关声明：[bt_conn_le_cs_subevent_result](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md)。

支持 CS 的 LE 连接的子事件（Subevent）数据。

<a id="r_bt_5Fconn_5Fle_5Finfo"></a>

```c
struct bt_conn_le_info
```

相关声明：[bt_conn_le_info](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md)。

LE 连接信息结构体。

<a id="r_bt_5Fconn_5Fbr_5Finfo"></a>

```c
struct bt_conn_br_info
```

相关声明：[bt_conn_br_info](../bluetooth_connection_model_reference/P006_bt_conn_br_info_结构体.md)。

BR/EDR 连接信息（Connection Info）结构体。

<a id="r_bt_5Fconn_5Fsco_5Finfo"></a>

```c
struct bt_conn_sco_info
```

相关声明：[bt_conn_sco_info](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md)。

同步面向连接（SCO）连接信息结构体。

<a id="r_bt_5Fsecurity_5Finfo"></a>

```c
struct bt_security_info
```

相关声明：[bt_security_info](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md)。

安全信息（Security Info）结构。

<a id="r_bt_5Fconn_5Finfo"></a>

```c
struct bt_conn_info
```

相关声明：[bt_conn_info](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md)。

连接信息结构体（Connection Info Structure）。

<a id="r_bt_5Fconn_5Fle_5Fremote_5Finfo"></a>

```c
struct bt_conn_le_remote_info
```

相关声明：[bt_conn_le_remote_info](../bluetooth_connection_model_reference/P031_bt_conn_le_remote_info_结构体.md)。

LE 连接的远端信息结构体。

<a id="r_bt_5Fconn_5Fbr_5Fremote_5Finfo"></a>

```c
struct bt_conn_br_remote_info
```

相关声明：[bt_conn_br_remote_info](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md)。

BR/EDR 连接的远端信息（Remote Info）结构体。

<a id="r_bt_5Fconn_5Fremote_5Finfo"></a>

```c
struct bt_conn_remote_info
```

相关声明：[bt_conn_remote_info](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md)。

连接的远端信息结构体。

<a id="r_bt_5Fconn_5Fle_5Ftx_5Fpower"></a>

```c
struct bt_conn_le_tx_power
```

相关声明：[bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)。

LE 发射功率等级（Transmit Power Level）结构体。

<a id="r_bt_5Fconn_5Fle_5Ftx_5Fpower_5Freport"></a>

```c
struct bt_conn_le_tx_power_report
```

相关声明：[bt_conn_le_tx_power_report](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md)。

LE 发射功率报告（Transmit Power Reporting）结构体。

<a id="r_bt_5Fconn_5Fle_5Fpath_5Floss_5Fthreshold_5Freport"></a>

```c
struct bt_conn_le_path_loss_threshold_report
```

相关声明：[bt_conn_le_path_loss_threshold_report](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md)。

LE 路径损耗监测阈值变化报告（Path Loss Monitoring Threshold Change Report）结构体。

<a id="r_bt_5Fconn_5Fle_5Fpath_5Floss_5Freporting_5Fparam"></a>

```c
struct bt_conn_le_path_loss_reporting_param
```

相关声明：[bt_conn_le_path_loss_reporting_param](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md)。

核心规范（Core Spec）定义的 LE 路径损耗监测参数（Path Loss Monitoring Parameters）结构体。

<a id="r_bt_5Fconn_5Fle_5Fcreate_5Fparam"></a>

```c
struct bt_conn_le_create_param
```

相关声明：[bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)。

<a id="r_bt_5Fconn_5Fle_5Fcreate_5Fsynced_5Fparam"></a>

```c
struct bt_conn_le_create_synced_param
```

相关声明：[bt_conn_le_create_synced_param](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md)。

<a id="r_bt_5Fconn_5Fle_5Fcs_5Fprocedure_5Fenable_5Fcomplete"></a>

```c
struct bt_conn_le_cs_procedure_enable_complete
```

相关声明：[bt_conn_le_cs_procedure_enable_complete](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)。

<a id="r_bt_5Fconn_5Fbr_5Fcb"></a>

```c
struct bt_conn_br_cb
```

相关声明：[bt_conn_br_cb](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md)。

BR/EDR 专用连接回调。

<a id="r_bt_5Fconn_5Fcb"></a>

```c
struct bt_conn_cb
```

相关声明：[bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)。

连接回调结构体（Connection Callback Structure）。

<a id="r_bt_5Fconn_5Foob_5Finfo"></a>

```c
struct bt_conn_oob_info
```

相关声明：[bt_conn_oob_info](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md)。

带外（Out-of-Band，OOB）配对信息结构体。

<a id="r_bt_5Fconn_5Fpairing_5Ffeat"></a>

```c
struct bt_conn_pairing_feat
```

相关声明：[bt_conn_pairing_feat](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md)。

配对请求（Pairing Request）与配对响应（Pairing Response）信息结构体。

<a id="r_bt_5Fconn_5Fauth_5Fcb"></a>

```c
struct bt_conn_auth_cb
```

相关声明：[bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)。

认证配对（Authenticated Pairing）回调结构体。

<a id="r_bt_5Fconn_5Fauth_5Finfo_5Fcb"></a>

```c
struct bt_conn_auth_info_cb
```

相关声明：[bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)。

认证配对信息回调结构体。

<a id="r_bt_5Fbr_5Fconn_5Fparam"></a>

```c
struct bt_br_conn_param
```

相关声明：[bt_br_conn_param](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md)。

基本速率／增强数据速率（BR/EDR）连接的连接参数。

<a id="r_bt_5Fconn"></a>

```c
struct bt_conn
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

表示与远端设备连接的不透明类型（Opaque Type）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga81de567c4c8cb691ef8b02633b42e342"></a>

```c
#define BT_LE_CONN_PARAM_INIT(int_min, int_max, lat, to)
```

相关声明：[BT_LE_CONN_PARAM_INIT](#ga81de567c4c8cb691ef8b02633b42e342)。

初始化连接参数（Connection Parameters）。

<a id="r_ga940d55c0d84c0cb8f09bc41074ae50d0"></a>

```c
#define BT_LE_CONN_PARAM(int_min, int_max, lat, to)
```

相关声明：[BT_LE_CONN_PARAM](#ga940d55c0d84c0cb8f09bc41074ae50d0)。

用于内联声明连接参数（Connection Parameters）的辅助宏。

<a id="r_ga82df8f439aeb3a156f4238deb085534a"></a>

```c
#define BT_LE_CONN_PARAM_DEFAULT
```

相关声明：[BT_LE_CONN_PARAM_DEFAULT](#ga82df8f439aeb3a156f4238deb085534a)。

默认低功耗蓝牙连接参数（LE Connection Parameters）：连接间隔 30–50 ms，延迟 0，超时 4 s。

<a id="r_gabca56de0c82c14995738952dafb1fe2d"></a>

```c
#define BT_CONN_LE_PHY_PARAM_INIT(_pref_tx_phy, _pref_rx_phy)
```

相关声明：[BT_CONN_LE_PHY_PARAM_INIT](#gabca56de0c82c14995738952dafb1fe2d)。

初始化物理层参数（PHY Parameters）。

<a id="r_ga39b69f0978f74b5f13f829e908b7cebb"></a>

```c
#define BT_CONN_LE_PHY_PARAM(_pref_tx_phy, _pref_rx_phy)
```

相关声明：[BT_CONN_LE_PHY_PARAM](#ga39b69f0978f74b5f13f829e908b7cebb)。

用于内联声明物理层参数（PHY Parameters）的辅助宏。

<a id="r_ga3ec555bb4ace5e9c7c13735820fd31de"></a>

```c
#define BT_CONN_LE_PHY_PARAM_1M
```

相关声明：[BT_CONN_LE_PHY_PARAM_1M](#ga3ec555bb4ace5e9c7c13735820fd31de)。

仅低功耗蓝牙 1M 物理层（LE 1M PHY）。

<a id="r_ga633126e356658886e9fa3f3217cb4e2c"></a>

```c
#define BT_CONN_LE_PHY_PARAM_2M
```

相关声明：[BT_CONN_LE_PHY_PARAM_2M](#ga633126e356658886e9fa3f3217cb4e2c)。

仅低功耗蓝牙 2M 物理层（LE 2M PHY）。

<a id="r_ga4915244a6cd70995514d6dde1ee0b45f"></a>

```c
#define BT_CONN_LE_PHY_PARAM_CODED
```

相关声明：[BT_CONN_LE_PHY_PARAM_CODED](#ga4915244a6cd70995514d6dde1ee0b45f)。

仅低功耗蓝牙编码物理层（LE Coded PHY）。

<a id="r_ga02c9d7a04ccf2f043293aed7a7f767a7"></a>

```c
#define BT_CONN_LE_PHY_PARAM_ALL
```

相关声明：[BT_CONN_LE_PHY_PARAM_ALL](#ga02c9d7a04ccf2f043293aed7a7f767a7)。

全部低功耗蓝牙物理层（LE PHYs）。

<a id="r_ga98f9dab71897382cf1187259a3b5660e"></a>

```c
#define BT_CONN_LE_DATA_LEN_PARAM_INIT(_tx_max_len, _tx_max_time)
```

相关声明：[BT_CONN_LE_DATA_LEN_PARAM_INIT](#ga98f9dab71897382cf1187259a3b5660e)。

初始化发送数据长度参数（Transmit Data Length Parameters）。

<a id="r_ga102b97de8689fe3fb53f9691009de87f"></a>

```c
#define BT_CONN_LE_DATA_LEN_PARAM(_tx_max_len, _tx_max_time)
```

相关声明：[BT_CONN_LE_DATA_LEN_PARAM](#ga102b97de8689fe3fb53f9691009de87f)。

用于内联声明发送数据长度参数（Transmit Data Length Parameters）的辅助宏。

<a id="r_gaf66746d834f7556dc77659741e27e0c9"></a>

```c
#define BT_LE_DATA_LEN_PARAM_DEFAULT
```

相关声明：[BT_LE_DATA_LEN_PARAM_DEFAULT](#gaf66746d834f7556dc77659741e27e0c9)。

默认低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="r_ga9cc26afda3c507cb5439184fedcd61ba"></a>

```c
#define BT_LE_DATA_LEN_PARAM_MAX
```

相关声明：[BT_LE_DATA_LEN_PARAM_MAX](#ga9cc26afda3c507cb5439184fedcd61ba)。

最大低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="r_gadcb74ad947485dd81dfd59a82d3b0db6"></a>

```c
#define BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS 41
```

相关声明：[BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS](#gadcb74ad947485dd81dfd59a82d3b0db6)。

允许的最大连接间隔组数（Maximum Connection Interval Groups）。

<a id="r_gacce78fed479c9d7e9b394488d5e466d7"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS](#gacce78fed479c9d7e9b394488d5e466d7)。

<a id="r_ga1b9b7d5bd6500ef1195c5da0275247ee"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL](#ga1b9b7d5bd6500ef1195c5da0275247ee)。

<a id="r_gacdf0d72c8f6dfe6e13c714148f04df3c"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS](#gacdf0d72c8f6dfe6e13c714148f04df3c)。

<a id="r_gaf01791831e52ee5976679fc0fac9118c"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_MAX (10000U)
```

相关声明：[BT_CONN_LE_FRAME_SPACE_MAX](#gaf01791831e52ee5976679fc0fac9118c)。

最大帧间隔（Maximum frame space），单位为微秒。

<a id="r_ga5354b9973117f94b88c61fb0ea726a4b"></a>

```c
#define BT_CONN_LE_CS_MODE_MAIN_MODE_PART(x)
```

相关声明：[BT_CONN_LE_CS_MODE_MAIN_MODE_PART](#ga5354b9973117f94b88c61fb0ea726a4b)。

从 bt_conn_le_cs_mode 提取主模式部分（Main Mode）。

<a id="r_ga19d2cd20af6f2652164a5677ee8863d5"></a>

```c
#define BT_CONN_LE_CS_MODE_SUB_MODE_PART(x)
```

相关声明：[BT_CONN_LE_CS_MODE_SUB_MODE_PART](#ga19d2cd20af6f2652164a5677ee8863d5)。

从 bt_conn_le_cs_mode 提取子模式部分（Sub-mode）。

<a id="r_ga707cc62b12c89478aebd0488a464a776"></a>

```c
#define BT_CONN_INTERVAL_TO_MS(interval)
```

相关声明：[BT_CONN_INTERVAL_TO_MS](#ga707cc62b12c89478aebd0488a464a776)。

将连接间隔（Connection Interval）转换为毫秒。

<a id="r_ga0a5fac126005684847ee7509bb98e382"></a>

```c
#define BT_CONN_INTERVAL_TO_US(interval)
```

相关声明：[BT_CONN_INTERVAL_TO_US](#ga0a5fac126005684847ee7509bb98e382)。

将连接间隔（Connection Interval）转换为微秒。

<a id="r_gaf4b1395e345f1bf01b83a890bf9a5083"></a>

```c
#define BT_CONN_SCI_INTERVAL_TO_US(_interval)
```

相关声明：[BT_CONN_SCI_INTERVAL_TO_US](#gaf4b1395e345f1bf01b83a890bf9a5083)。

将较短连接间隔（Shorter Connection Interval）转换为微秒。

<a id="r_ga5e4ec28058d93bede65ccb9d20014e2e"></a>

```c
#define bt_conn_dst_str(_conn)
```

相关声明：[bt_conn_dst_str](#ga5e4ec28058d93bede65ccb9d20014e2e)。

获取指向连接目标，即对端地址（Destination / Peer Address）字符串的指针。

<a id="r_ga8ac93a19c34d2821c158f310879fe00d"></a>

```c
#define BT_CONN_LE_CREATE_PARAM_INIT(_options, _interval, _window)
```

相关声明：[BT_CONN_LE_CREATE_PARAM_INIT](#ga8ac93a19c34d2821c158f310879fe00d)。

初始化创建连接参数（Create Connection Parameters）。

<a id="r_gae86425d432078e2ddca260eebc2802f1"></a>

```c
#define BT_CONN_LE_CREATE_PARAM(_options, _interval, _window)
```

相关声明：[BT_CONN_LE_CREATE_PARAM](#gae86425d432078e2ddca260eebc2802f1)。

用于内联声明创建连接参数（Create Connection Parameters）的辅助宏。

<a id="r_gab4203c55c20d83256ca036148c14a00d"></a>

```c
#define BT_CONN_LE_CREATE_CONN
```

相关声明：[BT_CONN_LE_CREATE_CONN](#gab4203c55c20d83256ca036148c14a00d)。

默认低功耗蓝牙创建连接参数（LE Create Connection Parameters）。

<a id="r_gaaba7c37a5c6e98e7b62ac12bde814d5d"></a>

```c
#define BT_CONN_LE_CREATE_CONN_AUTO
```

相关声明：[BT_CONN_LE_CREATE_CONN_AUTO](#gaaba7c37a5c6e98e7b62ac12bde814d5d)。

使用过滤接受列表（Filter Accept List）的默认低功耗蓝牙创建连接参数。

<a id="r_ga3fac32ef426900046d8e38bbd4b7c2d2"></a>

```c
#define BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP 0xFF
```

相关声明：[BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP](#ga3fac32ef426900046d8e38bbd4b7c2d2)。

表示 L2CAP 连接参数更新过程（Connection Parameter Update Procedure，CPUP）被拒绝的合成错误值（Synthetic Error Value）。

<a id="r_ga9227880a1ae5fc373d334171e1450f00"></a>

```c
#define BT_CONN_CB_DEFINE(_name)
```

相关声明：[BT_CONN_CB_DEFINE](#ga9227880a1ae5fc373d334171e1450f00)。

为连接事件（Connection Events）注册回调结构体。

<a id="r_ga988dbb7aea2ac136e3bc8efdf6f7478c"></a>

```c
#define BT_PASSKEY_RAND 0xffffffff
```

相关声明：[BT_PASSKEY_RAND](#ga988dbb7aea2ac136e3bc8efdf6f7478c)。

使用 bt_conn_auth_cb 的 app_passkey 回调时，可用于生成随机配对口令（Passkey）的特殊口令值。

<a id="r_ga986f563bfb741c70fbee39b3948d9d8d"></a>

```c
#define BT_BR_CONN_PARAM_INIT(role_switch)
```

相关声明：[BT_BR_CONN_PARAM_INIT](#ga986f563bfb741c70fbee39b3948d9d8d)。

初始化基本速率／增强数据速率连接参数（BR/EDR Connection Parameters）。

<a id="r_ga6f99f4adfcef36a4d738783921965ca6"></a>

```c
#define BT_BR_CONN_PARAM(role_switch)
```

相关声明：[BT_BR_CONN_PARAM](#ga6f99f4adfcef36a4d738783921965ca6)。

用于内联声明 BR／EDR 连接参数（Connection Parameters）的辅助宏。

<a id="r_ga5ccdbff63a430a37a8a8077d8792f706"></a>

```c
#define BT_BR_CONN_PARAM_DEFAULT BT_BR_CONN_PARAM(true)
```

相关声明：[BT_BR_CONN_PARAM_DEFAULT](#ga5ccdbff63a430a37a8a8077d8792f706)、[BT_BR_CONN_PARAM](#ga6f99f4adfcef36a4d738783921965ca6)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

默认 BR／EDR 连接参数：允许角色切换（Role Switch）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga08eb37185a763212e65c47ab4c886eca"></a>

```c
enum { BT_CONN_LE_PHY_OPT_NONE = 0 , BT_CONN_LE_PHY_OPT_CODED_S2 = (1UL << (0)) , BT_CONN_LE_PHY_OPT_CODED_S8 = (1UL << (1)) }
```

相关声明：[BT_CONN_LE_PHY_OPT_NONE](#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)、[BT_CONN_LE_PHY_OPT_CODED_S2](#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34)、[BT_CONN_LE_PHY_OPT_CODED_S8](#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0)。

连接物理层选项（Connection PHY options）。

<a id="r_gae60f156d2aa01814ad485786e00c4ca7"></a>

```c
enum bt_conn_le_frame_space_update_initiator { BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST , BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER , BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER }
```

相关声明：[bt_conn_le_frame_space_update_initiator](#gae60f156d2aa01814ad485786e00c4ca7)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](#ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](#ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](#ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4)。

帧间隔更新发起方（Frame Space Update Initiator）。

<a id="r_gab8dde20ae75b51f1e28dbeed06001f20"></a>

```c
enum bt_conn_type { BT_CONN_TYPE_LE = (1UL << (0)) , BT_CONN_TYPE_BR = (1UL << (1)) , BT_CONN_TYPE_SCO = (1UL << (2)) , BT_CONN_TYPE_ISO = (1UL << (3)) , BT_CONN_TYPE_ALL }
```

相关声明：[bt_conn_type](#gab8dde20ae75b51f1e28dbeed06001f20)、[BT_CONN_TYPE_LE](#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)、[BT_CONN_TYPE_BR](#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)、[BT_CONN_TYPE_SCO](#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)、[BT_CONN_TYPE_ISO](#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)、[BT_CONN_TYPE_ALL](#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)。

连接类型（Connection Type）。

<a id="r_gafe14d64a64383b097760764697b035e2"></a>

```c
enum bt_conn_le_cs_capability_rtt_aa_only { BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_AA_ONLY_10NS , BT_CONN_LE_CS_RTT_AA_ONLY_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_aa_only](#gafe14d64a64383b097760764697b035e2)、[BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP](#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94)、[BT_CONN_LE_CS_RTT_AA_ONLY_10NS](#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a)、[BT_CONN_LE_CS_RTT_AA_ONLY_150NS](#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6)。

支持的仅接入地址往返时间精度（AA-Only RTT Precision）。

<a id="r_ga1892ec23ca3b1818287a9d7dafc16433"></a>

```c
enum bt_conn_le_cs_capability_rtt_sounding { BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_SOUNDING_10NS , BT_CONN_LE_CS_RTT_SOUNDING_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_sounding](#ga1892ec23ca3b1818287a9d7dafc16433)、[BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP](#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14)、[BT_CONN_LE_CS_RTT_SOUNDING_10NS](#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb)、[BT_CONN_LE_CS_RTT_SOUNDING_150NS](#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584)。

支持的探测序列往返时间精度（Sounding Sequence RTT Precision）。

<a id="r_ga5568443825fc1ce9534753d8918aa813"></a>

```c
enum bt_conn_le_cs_capability_rtt_random_payload { BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS , BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_random_payload](#ga5568443825fc1ce9534753d8918aa813)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP](#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS](#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS](#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db)。

支持的随机有效载荷往返时间精度（Random Payload RTT Precision）。

<a id="r_ga2f757b15d1d5006ce2fa6a7a78082156"></a>

```c
enum bt_conn_le_cs_mode { BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_1 , BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_2 , BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_3 , BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1 , BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3 , BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2 }
```

相关声明：[bt_conn_le_cs_mode](#ga2f757b15d1d5006ce2fa6a7a78082156)、[BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE](#gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a)、[BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE](#gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a)、[BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE](#gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf)、[BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1](#gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7)、[BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3](#gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26)、[BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2](#gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac)。

信道探测模式（Channel Sounding Mode），包括主模式与子模式。

<a id="r_ga0e6f6d4fdbdfc3ed75fef4a95136076f"></a>

```c
enum bt_conn_le_cs_role { BT_CONN_LE_CS_ROLE_INITIATOR , BT_CONN_LE_CS_ROLE_REFLECTOR }
```

相关声明：[bt_conn_le_cs_role](#ga0e6f6d4fdbdfc3ed75fef4a95136076f)、[BT_CONN_LE_CS_ROLE_INITIATOR](#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4)、[BT_CONN_LE_CS_ROLE_REFLECTOR](#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968)。

信道探测角色（Channel Sounding Role）。

<a id="r_gaffd6abf9b92cc8d8463797a73b840f51"></a>

```c
enum bt_conn_le_cs_rtt_type { BT_CONN_LE_CS_RTT_TYPE_AA_ONLY = BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY , BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND , BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND , BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND }
```

相关声明：[bt_conn_le_cs_rtt_type](#gaffd6abf9b92cc8d8463797a73b840f51)、[BT_CONN_LE_CS_RTT_TYPE_AA_ONLY](#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088)、[BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING](#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)、[BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING](#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)、[BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM](#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad)、[BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM](#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91)、[BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM](#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f)、[BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM](#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5)。

信道探测往返时间类型（Channel Sounding RTT Type）。

<a id="r_gaadbf6a4dba28aec90ea07b7da634e1bb"></a>

```c
enum bt_conn_le_cs_sync_phy { BT_CONN_LE_CS_SYNC_1M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_1M , BT_CONN_LE_CS_SYNC_2M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M , BT_CONN_LE_CS_SYNC_2M_2BT_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT }
```

相关声明：[bt_conn_le_cs_sync_phy](#gaadbf6a4dba28aec90ea07b7da634e1bb)、[BT_CONN_LE_CS_SYNC_1M_PHY](#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95)、[BT_CONN_LE_CS_SYNC_2M_PHY](#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6)、[BT_CONN_LE_CS_SYNC_2M_2BT_PHY](#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b)。

CS 同步使用的信道探测物理层（Channel Sounding PHY）。

<a id="r_ga34e4837a77c7afd6999095985ddad4f0"></a>

```c
enum bt_conn_le_cs_chsel_type { BT_CONN_LE_CS_CHSEL_TYPE_3B = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B , BT_CONN_LE_CS_CHSEL_TYPE_3C = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C }
```

相关声明：[bt_conn_le_cs_chsel_type](#ga34e4837a77c7afd6999095985ddad4f0)、[BT_CONN_LE_CS_CHSEL_TYPE_3B](#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1)、[BT_CONN_LE_CS_CHSEL_TYPE_3C](#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6)。

信道探测信道选择类型（Channel Sounding Channel Selection Type）。

<a id="r_gaf2331ec1f1222de51fc4f30566e1c52b"></a>

```c
enum bt_conn_le_cs_ch3c_shape { BT_CONN_LE_CS_CH3C_SHAPE_HAT = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT , BT_CONN_LE_CS_CH3C_SHAPE_X = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X }
```

相关声明：[bt_conn_le_cs_ch3c_shape](#gaf2331ec1f1222de51fc4f30566e1c52b)、[BT_CONN_LE_CS_CH3C_SHAPE_HAT](#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea)、[BT_CONN_LE_CS_CH3C_SHAPE_X](#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622)。

信道探测信道序列形状（Channel Sounding Channel Sequence Shape）。

<a id="r_ga9a1dc2010c5237466de87160944630d3"></a>

```c
enum bt_conn_le_cs_procedure_done_status { BT_CONN_LE_CS_PROCEDURE_COMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE , BT_CONN_LE_CS_PROCEDURE_INCOMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL , BT_CONN_LE_CS_PROCEDURE_ABORTED = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED }
```

相关声明：[bt_conn_le_cs_procedure_done_status](#ga9a1dc2010c5237466de87160944630d3)、[BT_CONN_LE_CS_PROCEDURE_COMPLETE](#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f)、[BT_CONN_LE_CS_PROCEDURE_INCOMPLETE](#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82)、[BT_CONN_LE_CS_PROCEDURE_ABORTED](#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)。

过程完成状态（Procedure Done Status）。

<a id="r_ga8e54a191b889b1d5ed3e1fbb648d9bc7"></a>

```c
enum bt_conn_le_cs_subevent_done_status { BT_CONN_LE_CS_SUBEVENT_COMPLETE = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE , BT_CONN_LE_CS_SUBEVENT_ABORTED = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED }
```

相关声明：[bt_conn_le_cs_subevent_done_status](#ga8e54a191b889b1d5ed3e1fbb648d9bc7)、[BT_CONN_LE_CS_SUBEVENT_COMPLETE](#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)、[BT_CONN_LE_CS_SUBEVENT_ABORTED](#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)。

子事件完成状态（Subevent Done Status）。

<a id="r_ga3196a0eb1c7497e93d7c646713d2fc79"></a>

```c
enum bt_conn_le_cs_procedure_abort_reason { BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT , BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED , BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS , BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED , BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED }
```

相关声明：[bt_conn_le_cs_procedure_abort_reason](#ga3196a0eb1c7497e93d7c646713d2fc79)、[BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED](#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d)、[BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED](#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0)、[BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS](#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02)、[BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED](#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744)、[BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED](#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886)。

过程中止原因（Procedure Abort Reason）。

<a id="r_ga6394906c6da40c9bebfaeb05de9fd5be"></a>

```c
enum bt_conn_le_cs_subevent_abort_reason { BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT , BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED , BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC , BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT , BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED }
```

相关声明：[bt_conn_le_cs_subevent_abort_reason](#ga6394906c6da40c9bebfaeb05de9fd5be)、[BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED](#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c)、[BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED](#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d)、[BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC](#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d)、[BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT](#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd)、[BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED](#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3)。

子事件中止原因（Subevent Abort Reason）。

<a id="r_ga9c54d2e44903cf7c4e5c97e223069dbc"></a>

```c
enum { BT_CONN_ROLE_CENTRAL = 0 , BT_CONN_ROLE_PERIPHERAL = 1 }
```

相关声明：[BT_CONN_ROLE_CENTRAL](#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)、[BT_CONN_ROLE_PERIPHERAL](#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)。

<a id="r_ga9442c1479db60e2db40a2ea6de565282"></a>

```c
enum bt_conn_state { BT_CONN_STATE_DISCONNECTED , BT_CONN_STATE_CONNECTING , BT_CONN_STATE_CONNECTED , BT_CONN_STATE_DISCONNECTING }
```

相关声明：[bt_conn_state](#ga9442c1479db60e2db40a2ea6de565282)、[BT_CONN_STATE_DISCONNECTED](#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)、[BT_CONN_STATE_CONNECTING](#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)、[BT_CONN_STATE_CONNECTED](#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)、[BT_CONN_STATE_DISCONNECTING](#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)。

<a id="r_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>

```c
enum bt_security_t { BT_SECURITY_L0 , BT_SECURITY_L1 , BT_SECURITY_L2 , BT_SECURITY_L3 , BT_SECURITY_L4 , BT_SECURITY_FORCE_PAIR = (1UL << (7)) }
```

相关声明：[bt_security_t](#gaf0c56cd26c4147f6c9f0faa11fa01783)、[BT_SECURITY_L0](#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)、[BT_SECURITY_L1](#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)、[BT_SECURITY_L2](#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)、[BT_SECURITY_L3](#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)、[BT_SECURITY_L4](#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)、[BT_SECURITY_FORCE_PAIR](#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)。

安全级别（Security Level）。

<a id="r_ga2f8712bbf3410de5cbe6ce489fe30e5e"></a>

```c
enum bt_security_flag { BT_SECURITY_FLAG_SC = (1UL << (0)) , BT_SECURITY_FLAG_OOB = (1UL << (1)) }
```

相关声明：[bt_security_flag](#ga2f8712bbf3410de5cbe6ce489fe30e5e)、[BT_SECURITY_FLAG_SC](#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)、[BT_SECURITY_FLAG_OOB](#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)。

安全信息标志（Security Info Flags）。

<a id="r_ga737d8118f8aba8985292d92d0604b190"></a>

```c
enum bt_conn_le_tx_power_phy { BT_CONN_LE_TX_POWER_PHY_NONE , BT_CONN_LE_TX_POWER_PHY_1M , BT_CONN_LE_TX_POWER_PHY_2M , BT_CONN_LE_TX_POWER_PHY_CODED_S8 , BT_CONN_LE_TX_POWER_PHY_CODED_S2 }
```

相关声明：[bt_conn_le_tx_power_phy](#ga737d8118f8aba8985292d92d0604b190)、[BT_CONN_LE_TX_POWER_PHY_NONE](#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)、[BT_CONN_LE_TX_POWER_PHY_1M](#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)、[BT_CONN_LE_TX_POWER_PHY_2M](#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)、[BT_CONN_LE_TX_POWER_PHY_CODED_S8](#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)、[BT_CONN_LE_TX_POWER_PHY_CODED_S2](#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)。

<a id="r_gaf43d7aa3ad1c8d2bde8b04e650fe7b7e"></a>

```c
enum bt_conn_le_path_loss_zone { BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW , BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE , BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH , BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE }
```

相关声明：[bt_conn_le_path_loss_zone](#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW](#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE](#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH](#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705)、[BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE](#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942)。

已进入的路径损耗区域（Path Loss Zone）。

<a id="r_ga57465d3a61214531ddaffc2c30939043"></a>

```c
enum bt_conn_auth_keypress { BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED = 0x00 , BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED = 0x01 , BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED = 0x02 , BT_CONN_AUTH_KEYPRESS_CLEARED = 0x03 , BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED = 0x04 }
```

相关声明：[bt_conn_auth_keypress](#ga57465d3a61214531ddaffc2c30939043)、[BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED](#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)、[BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED](#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)、[BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED](#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)、[BT_CONN_AUTH_KEYPRESS_CLEARED](#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)、[BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED](#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)。

配对口令按键通知类型（Passkey Keypress Notification Type）。

<a id="r_ga3afc8024ddbcd3bf5a809706e39f74bc"></a>

```c
enum { BT_CONN_LE_OPT_NONE = 0 , BT_CONN_LE_OPT_CODED = (1UL << (0)) , BT_CONN_LE_OPT_NO_1M = (1UL << (1)) }
```

相关声明：[BT_CONN_LE_OPT_NONE](#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)、[BT_CONN_LE_OPT_CODED](#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)、[BT_CONN_LE_OPT_NO_1M](#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)。

<a id="r_gaa9420ff489fd5857ff076406442679ff"></a>

```c
enum bt_security_err { BT_SECURITY_ERR_SUCCESS , BT_SECURITY_ERR_AUTH_FAIL , BT_SECURITY_ERR_PIN_OR_KEY_MISSING , BT_SECURITY_ERR_OOB_NOT_AVAILABLE , BT_SECURITY_ERR_AUTH_REQUIREMENT , BT_SECURITY_ERR_PAIR_NOT_SUPPORTED , BT_SECURITY_ERR_PAIR_NOT_ALLOWED , BT_SECURITY_ERR_INVALID_PARAM , BT_SECURITY_ERR_KEY_REJECTED , BT_SECURITY_ERR_UNSPECIFIED }
```

相关声明：[bt_security_err](#gaa9420ff489fd5857ff076406442679ff)、[BT_SECURITY_ERR_SUCCESS](#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)、[BT_SECURITY_ERR_AUTH_FAIL](#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)、[BT_SECURITY_ERR_PIN_OR_KEY_MISSING](#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)、[BT_SECURITY_ERR_OOB_NOT_AVAILABLE](#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)、[BT_SECURITY_ERR_AUTH_REQUIREMENT](#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)、[BT_SECURITY_ERR_PAIR_NOT_SUPPORTED](#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)、[BT_SECURITY_ERR_PAIR_NOT_ALLOWED](#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)、[BT_SECURITY_ERR_INVALID_PARAM](#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)、[BT_SECURITY_ERR_KEY_REJECTED](#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)、[BT_SECURITY_ERR_UNSPECIFIED](#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)。

<a id="r_gaf3653de72793f775e33fd9eb04c3e7a2"></a>

```c
enum bt_conn_le_cs_procedure_enable_state { BT_CONN_LE_CS_PROCEDURES_DISABLED = BT_HCI_OP_LE_CS_PROCEDURES_DISABLED , BT_CONN_LE_CS_PROCEDURES_ENABLED = BT_HCI_OP_LE_CS_PROCEDURES_ENABLED }
```

相关声明：[bt_conn_le_cs_procedure_enable_state](#gaf3653de72793f775e33fd9eb04c3e7a2)、[BT_CONN_LE_CS_PROCEDURES_DISABLED](#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83)、[BT_CONN_LE_CS_PROCEDURES_ENABLED](#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac)。

<a id="r_gab7acdbdf273fc760799cf0d8cf71591c"></a>

```c
enum bt_conn_le_cs_tone_antenna_config_selection { BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1 = BT_HCI_OP_LE_CS_ACI_0 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1 = BT_HCI_OP_LE_CS_ACI_1 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1 = BT_HCI_OP_LE_CS_ACI_2 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1 = BT_HCI_OP_LE_CS_ACI_3 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2 = BT_HCI_OP_LE_CS_ACI_4 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3 = BT_HCI_OP_LE_CS_ACI_5 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4 = BT_HCI_OP_LE_CS_ACI_6 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2 = BT_HCI_OP_LE_CS_ACI_7 }
```

相关声明：[bt_conn_le_cs_tone_antenna_config_selection](#gab7acdbdf273fc760799cf0d8cf71591c)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1](#ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1](#ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1](#ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1](#ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2](#ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3](#ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4](#ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2](#ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2)。

CS 测试音调天线配置选择（CS Test Tone Antenna Config Selection）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga060d51eb2208de6f805b1fc0672d2d0c"></a>

```c
struct bt_conn * bt_conn_ref (struct bt_conn *conn)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_ref](#ga060d51eb2208de6f805b1fc0672d2d0c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

增加连接的引用计数（Reference Count）。

<a id="r_ga4b18c6b22a9f02be0d7d078b2ce51ff6"></a>

```c
void bt_conn_unref (struct bt_conn *conn)
```

相关声明：[bt_conn_unref](#ga4b18c6b22a9f02be0d7d078b2ce51ff6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

减少连接的引用计数（Reference Count）。

<a id="r_gaf073384538a67c242b00150904176f66"></a>

```c
static struct bt_conn * bt_conn_take (struct bt_conn **orig)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_take](#gaf073384538a67c242b00150904176f66)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

接管连接指针的所有权（Ownership），将原指针设为 NULL。

<a id="r_gaf1aeec9b9893450423cf066a6f471824"></a>

```c
void bt_conn_drop (struct bt_conn **orig)
```

相关声明：[bt_conn_drop](#gaf1aeec9b9893450423cf066a6f471824)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

释放连接引用（Connection Reference）并清空指针。

<a id="r_ga5bdf8e8efc85138d3631dc1efffc3916"></a>

```c
void bt_conn_foreach (enum bt_conn_type type, void(*func)(struct bt_conn *conn, void *data), void *data)
```

相关声明：[bt_conn_foreach](#ga5bdf8e8efc85138d3631dc1efffc3916)、[bt_conn_type](#gab8dde20ae75b51f1e28dbeed06001f20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

遍历全部 bt_conn 对象。

<a id="r_ga1bfe349efd8a7de31e9457fe439d746a"></a>

```c
struct bt_conn * bt_conn_lookup_addr_le (uint8_t id, const bt_addr_le_t *peer)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_lookup_addr_le](#ga1bfe349efd8a7de31e9457fe439d746a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

根据地址查找现有连接（Connection）。

<a id="r_ga77108581b8f61485ca840e4bf7a17087"></a>

```c
const bt_addr_le_t * bt_conn_get_dst (const struct bt_conn *conn)
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_conn_get_dst](#ga77108581b8f61485ca840e4bf7a17087)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的目标，即对端地址（Destination / Peer Address）。

<a id="r_gad4aed76b80cc815f748ad0e84ae3d87c"></a>

```c
uint8_t bt_conn_index (const struct bt_conn *conn)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_index](#gad4aed76b80cc815f748ad0e84ae3d87c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的数组索引（Array Index）。

<a id="r_ga2de54f2ac83f0d8dca2a85a9fbfadcaa"></a>

```c
int bt_conn_get_info (const struct bt_conn *conn, struct bt_conn_info *info)
```

相关声明：[bt_conn_get_info](#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_info](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md)。

获取连接信息（Connection Info）。

<a id="r_gaf3d55f1f8efc630b495389ced3ee3fa5"></a>

```c
bool bt_conn_is_type (const struct bt_conn *conn, enum bt_conn_type type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_conn_is_type](#gaf3d55f1f8efc630b495389ced3ee3fa5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_type](#gab8dde20ae75b51f1e28dbeed06001f20)。

确定连接类型（Connection Type）的函数。

<a id="r_gac4e0bd799fc87b65367129685f57c2bd"></a>

```c
int bt_conn_get_remote_info (const struct bt_conn *conn, struct bt_conn_remote_info *remote_info)
```

相关声明：[bt_conn_get_remote_info](#gac4e0bd799fc87b65367129685f57c2bd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_remote_info](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md)。

获取远端设备的连接信息（Connection Info）。

<a id="r_gaa5289154bc508444f68df7abcef18aca"></a>

```c
int bt_conn_le_get_tx_power_level (struct bt_conn *conn, struct bt_conn_le_tx_power *tx_power_level)
```

相关声明：[bt_conn_le_get_tx_power_level](#gaa5289154bc508444f68df7abcef18aca)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)。

获取连接发射功率等级（Transmit Power Level）。

<a id="r_gaa79eada87d698f4998af876d03d7e92b"></a>

```c
int bt_conn_le_enhanced_get_tx_power_level (struct bt_conn *conn, struct bt_conn_le_tx_power *tx_power)
```

相关声明：[bt_conn_le_enhanced_get_tx_power_level](#gaa79eada87d698f4998af876d03d7e92b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)。

获取本地增强连接发射功率等级（Enhanced Connection Transmit Power Level）。

<a id="r_ga0843a2e0b6f16ebd132a3a512cfd27a4"></a>

```c
int bt_conn_le_get_remote_tx_power_level (struct bt_conn *conn, enum bt_conn_le_tx_power_phy phy)
```

相关声明：[bt_conn_le_get_remote_tx_power_level](#ga0843a2e0b6f16ebd132a3a512cfd27a4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power_phy](#ga737d8118f8aba8985292d92d0604b190)。

获取远端，即对端发射功率等级（Peer Transmit Power Level）。

<a id="r_gaa1f38911acee0534a8a6e414018c6fb6"></a>

```c
int bt_conn_le_set_tx_power_report_enable (struct bt_conn *conn, bool local_enable, bool remote_enable)
```

相关声明：[bt_conn_le_set_tx_power_report_enable](#gaa1f38911acee0534a8a6e414018c6fb6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用发射功率报告（Transmit Power Reporting）。

<a id="r_ga6be5f3bf064ba03dc2307fdd2b634637"></a>

```c
int bt_conn_le_set_path_loss_mon_param (struct bt_conn *conn, const struct bt_conn_le_path_loss_reporting_param *param)
```

相关声明：[bt_conn_le_set_path_loss_mon_param](#ga6be5f3bf064ba03dc2307fdd2b634637)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_path_loss_reporting_param](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md)。

设置路径损耗监测参数（Path Loss Monitoring Parameters）。

<a id="r_ga90ae27bcc6f71f32be56efe8ecbc165d"></a>

```c
int bt_conn_le_set_path_loss_mon_enable (struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_le_set_path_loss_mon_enable](#ga90ae27bcc6f71f32be56efe8ecbc165d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用路径损耗监测（Path Loss Monitoring）。

<a id="r_gac7bb456c530c7e08b4fa9f4d478fdaf9"></a>

```c
int bt_conn_le_subrate_set_defaults (const struct bt_conn_le_subrate_param *params)
```

相关声明：[bt_conn_le_subrate_set_defaults](#gac7bb456c530c7e08b4fa9f4d478fdaf9)、[bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)。

设置默认连接子速率参数（Connection Subrating Parameters）。

<a id="r_ga754ed218fe9577f2d0ef6d508cfc5a0b"></a>

```c
int bt_conn_le_subrate_request (struct bt_conn *conn, const struct bt_conn_le_subrate_param *params)
```

相关声明：[bt_conn_le_subrate_request](#ga754ed218fe9577f2d0ef6d508cfc5a0b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)。

请求新的子速率参数（Subrating Parameters）。

<a id="r_ga2e7e836d94a5330ae01e14dbd3e29f14"></a>

```c
int bt_conn_le_read_min_conn_interval_groups (struct bt_conn_le_min_conn_interval_info *info)
```

相关声明：[bt_conn_le_read_min_conn_interval_groups](#ga2e7e836d94a5330ae01e14dbd3e29f14)、[bt_conn_le_min_conn_interval_info](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md)。

读取支持的最小连接间隔组（Minimum Supported Connection Interval Groups）。

<a id="r_ga9af26600acdf5b3a8b8ea0a32e14b497"></a>

```c
int bt_conn_le_read_min_conn_interval (uint16_t *min_interval_us)
```

相关声明：[bt_conn_le_read_min_conn_interval](#ga9af26600acdf5b3a8b8ea0a32e14b497)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取支持的最小连接间隔（Minimum Supported Connection Interval）。

<a id="r_gac9b111639f9b982cd97e13f313e51461"></a>

```c
int bt_conn_le_conn_rate_set_defaults (const struct bt_conn_le_conn_rate_param *params)
```

相关声明：[bt_conn_le_conn_rate_set_defaults](#gac9b111639f9b982cd97e13f313e51461)、[bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)。

设置默认连接速率参数（Connection Rate Parameters）。

<a id="r_ga2e4188482deeda71f8e5d42a07538f31"></a>

```c
int bt_conn_le_conn_rate_request (struct bt_conn *conn, const struct bt_conn_le_conn_rate_param *params)
```

相关声明：[bt_conn_le_conn_rate_request](#ga2e4188482deeda71f8e5d42a07538f31)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)。

请求新的连接速率参数（Connection Rate Parameters）。

<a id="r_gac0dbbdb95ef868f35006622932dc8901"></a>

```c
int bt_conn_le_read_all_remote_features (struct bt_conn *conn, uint8_t pages_requested)
```

相关声明：[bt_conn_le_read_all_remote_features](#gac0dbbdb95ef868f35006622932dc8901)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取远端特性页（Remote Feature Pages）。

<a id="r_gab734fbc307eff3c5bddf7c5e6ddd341b"></a>

```c
int bt_conn_le_frame_space_update (struct bt_conn *conn, const struct bt_conn_le_frame_space_update_param *params)
```

相关声明：[bt_conn_le_frame_space_update](#gab734fbc307eff3c5bddf7c5e6ddd341b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_frame_space_update_param](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md)。

更新帧间隔（Frame Space）。

<a id="r_gab44a964725f54ed2d37de17c6e2fd3eb"></a>

```c
int bt_conn_le_param_update (struct bt_conn *conn, const struct bt_le_conn_param *param)
```

相关声明：[bt_conn_le_param_update](#gab44a964725f54ed2d37de17c6e2fd3eb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)。

更新连接参数（Connection Parameters）。

<a id="r_ga8a2006f6e34b20c7e8ef65a73f431a57"></a>

```c
int bt_conn_le_data_len_update (struct bt_conn *conn, const struct bt_conn_le_data_len_param *param)
```

相关声明：[bt_conn_le_data_len_update](#ga8a2006f6e34b20c7e8ef65a73f431a57)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_data_len_param](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md)。

更新连接发送数据长度参数（Transmit Data Length Parameters）。

<a id="r_gae13ed81b1e7928f44b8fdf85995b3e58"></a>

```c
int bt_conn_le_phy_update (struct bt_conn *conn, const struct bt_conn_le_phy_param *param)
```

相关声明：[bt_conn_le_phy_update](#gae13ed81b1e7928f44b8fdf85995b3e58)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_phy_param](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md)。

更新连接物理层参数（PHY Parameters）。

<a id="r_ga7c8e7a7616e7b56f97da7ff4bc0fc7ba"></a>

```c
int bt_conn_le_set_default_phy (uint8_t pref_tx_phy, uint8_t pref_rx_phy)
```

相关声明：[bt_conn_le_set_default_phy](#ga7c8e7a7616e7b56f97da7ff4bc0fc7ba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新默认物理层参数（PHY Parameters），用于此后经低功耗蓝牙传输（LE Transport）建立的全部连接。

<a id="r_ga14e7c852b0271781594e742ae509c5d3"></a>

```c
int bt_conn_disconnect (struct bt_conn *conn, uint8_t reason)
```

相关声明：[bt_conn_disconnect](#ga14e7c852b0271781594e742ae509c5d3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

断开远端设备或取消待处理连接（Pending Connection）。

<a id="r_ga8d66f3e0262a51279e9fa8b3139252e6"></a>

```c
int bt_conn_le_create (const bt_addr_le_t *peer, const struct bt_conn_le_create_param *create_param, const struct bt_le_conn_param *conn_param, struct bt_conn **conn)
```

相关声明：[bt_conn_le_create](#ga8d66f3e0262a51279e9fa8b3139252e6)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发起与远端设备的低功耗蓝牙连接（LE Connection）。

<a id="r_ga98f99c893e444d1ad1ecd9139803c0b1"></a>

```c
int bt_conn_le_create_synced (const struct bt_le_ext_adv *adv, const struct bt_conn_le_create_synced_param *synced_param, const struct bt_le_conn_param *conn_param, struct bt_conn **conn)
```

相关声明：[bt_conn_le_create_synced](#ga98f99c893e444d1ad1ecd9139803c0b1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_conn_le_create_synced_param](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

创建与已同步设备（Synced Device）的连接。

<a id="r_gaecfaf2cb44772511dbb585de8f76f09b"></a>

```c
int bt_conn_le_create_auto (const struct bt_conn_le_create_param *create_param, const struct bt_le_conn_param *conn_param)
```

相关声明：[bt_conn_le_create_auto](#gaecfaf2cb44772511dbb585de8f76f09b)、[bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)。

自动连接过滤接受列表（Filter Accept List）中的远端设备。

<a id="r_ga62dc2663b4fa39a33adb76dc9a136aa4"></a>

```c
int bt_conn_create_auto_stop (void)
```

相关声明：[bt_conn_create_auto_stop](#ga62dc2663b4fa39a33adb76dc9a136aa4)。

停止自动创建连接（Automatic Connect Creation）。

<a id="r_gae001f1268e1ff42c3c974c95dcb6735d"></a>

```c
int bt_conn_set_security (struct bt_conn *conn, bt_security_t sec)
```

相关声明：[bt_conn_set_security](#gae001f1268e1ff42c3c974c95dcb6735d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_security_t](#gaf0c56cd26c4147f6c9f0faa11fa01783)。

设置连接的安全等级（Security Level）。

<a id="r_ga4b43ef0f30146808e560991a302e88ad"></a>

```c
bt_security_t bt_conn_get_security (const struct bt_conn *conn)
```

相关声明：[bt_security_t](#gaf0c56cd26c4147f6c9f0faa11fa01783)、[bt_conn_get_security](#ga4b43ef0f30146808e560991a302e88ad)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的安全等级（Security Level）。

<a id="r_gaff3e6aa16b68e5da7dab53289295545e"></a>

```c
uint8_t bt_conn_enc_key_size (const struct bt_conn *conn)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_enc_key_size](#gaff3e6aa16b68e5da7dab53289295545e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取加密密钥大小（Encryption Key Size）。

<a id="r_gaa9b79cd44734c1e560d6f30509be4d0b"></a>

```c
int bt_conn_cb_register (struct bt_conn_cb *cb)
```

相关声明：[bt_conn_cb_register](#gaa9b79cd44734c1e560d6f30509be4d0b)、[bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)。

注册连接回调（Connection Callbacks）。

<a id="r_gad2f90b34390e3c3697fd455ae4ef5f31"></a>

```c
int bt_conn_cb_unregister (struct bt_conn_cb *cb)
```

相关声明：[bt_conn_cb_unregister](#gad2f90b34390e3c3697fd455ae4ef5f31)、[bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)。

注销连接回调（Connection Callbacks）。

<a id="r_ga327444a6987b8e0b573fe758d2f75886"></a>

```c
static const char * bt_security_err_to_str (enum bt_security_err err)
```

相关声明：[bt_security_err_to_str](#ga327444a6987b8e0b573fe758d2f75886)、[bt_security_err](#gaa9420ff489fd5857ff076406442679ff)。

将安全错误（Security Error）转换为字符串。

<a id="r_ga014db594b17a3b5d7d954e64ad8de759"></a>

```c
void bt_set_bondable (bool enable)
```

相关声明：[bt_set_bondable](#ga014db594b17a3b5d7d954e64ad8de759)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用绑定（Bonding）。

<a id="r_ga0c84d5597a71fe38788a88063fd19a2d"></a>

```c
bool bt_get_bondable (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_get_bondable](#ga0c84d5597a71fe38788a88063fd19a2d)。

获取绑定标志（Bonding Flag）。

<a id="r_ga4165819d12dd96e00dfa2fd6f4b95669"></a>

```c
int bt_conn_set_bondable (struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_set_bondable](#ga4165819d12dd96e00dfa2fd6f4b95669)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置／清除给定连接的绑定标志（Bonding Flag）。

<a id="r_gad02f8fe587efd543c0c81cace3f63d63"></a>

```c
void bt_le_oob_set_sc_flag (bool enable)
```

相关声明：[bt_le_oob_set_sc_flag](#gad02f8fe587efd543c0c81cace3f63d63)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

允许／禁止使用远端低功耗安全连接带外数据（LE SC OOB Data）进行配对。

<a id="r_ga978770d46d7c8af854a61261c14cb892"></a>

```c
void bt_le_oob_set_legacy_flag (bool enable)
```

相关声明：[bt_le_oob_set_legacy_flag](#ga978770d46d7c8af854a61261c14cb892)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

允许／禁止使用远端传统带外数据（Legacy OOB Data）进行配对。

<a id="r_ga0f889983cfabafe826b4feb6899b95ba"></a>

```c
int bt_le_oob_set_legacy_tk (struct bt_conn *conn, const uint8_t *tk)
```

相关声明：[bt_le_oob_set_legacy_tk](#ga0f889983cfabafe826b4feb6899b95ba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置用于配对的带外临时密钥（OOB Temporary Key）。

<a id="r_gac365f9748ad0737f09142ee1de982503"></a>

```c
int bt_le_oob_set_sc_data (struct bt_conn *conn, const struct bt_le_oob_sc_data *oobd_local, const struct bt_le_oob_sc_data *oobd_remote)
```

相关声明：[bt_le_oob_set_sc_data](#gac365f9748ad0737f09142ee1de982503)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)。

在低功耗安全连接（LE Secure Connections，SC）配对过程中设置带外数据（OOB Data）。

<a id="r_ga096552403b5bcd0107f69eded772b1ee"></a>

```c
int bt_le_oob_get_sc_data (struct bt_conn *conn, const struct bt_le_oob_sc_data **oobd_local, const struct bt_le_oob_sc_data **oobd_remote)
```

相关声明：[bt_le_oob_get_sc_data](#ga096552403b5bcd0107f69eded772b1ee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)。

获取低功耗安全连接（LE Secure Connections，SC）配对过程使用的带外数据（OOB Data）。

<a id="r_ga1bf13d2dfdbdf0a72f9b1c759ef23f60"></a>

```c
int bt_conn_auth_cb_register (const struct bt_conn_auth_cb *cb)
```

相关声明：[bt_conn_auth_cb_register](#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)、[bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)。

注册认证回调（Authentication Callbacks）。

<a id="r_ga81077385583d71c248a1eb6aab9ee86e"></a>

```c
int bt_conn_auth_cb_overlay (struct bt_conn *conn, const struct bt_conn_auth_cb *cb)
```

相关声明：[bt_conn_auth_cb_overlay](#ga81077385583d71c248a1eb6aab9ee86e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)。

为给定连接覆盖所使用的认证回调（Authentication Callbacks）。

<a id="r_gac6684a8089ebd495b539d661cf9fd13f"></a>

```c
int bt_conn_auth_info_cb_register (struct bt_conn_auth_info_cb *cb)
```

相关声明：[bt_conn_auth_info_cb_register](#gac6684a8089ebd495b539d661cf9fd13f)、[bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)。

注册认证信息回调（Authentication Information Callbacks）。

<a id="r_gac73a60b8b6b569b84fe17f707fa33f37"></a>

```c
int bt_conn_auth_info_cb_unregister (struct bt_conn_auth_info_cb *cb)
```

相关声明：[bt_conn_auth_info_cb_unregister](#gac73a60b8b6b569b84fe17f707fa33f37)、[bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)。

注销认证信息回调（Authentication Information Callbacks）。

<a id="r_ga3906d8d3d192e8a6ad1bf6b7acc32ff0"></a>

```c
int bt_conn_auth_passkey_entry (struct bt_conn *conn, unsigned int passkey)
```

相关声明：[bt_conn_auth_passkey_entry](#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使用输入的配对口令（Passkey）回复。

<a id="r_ga2987a902da4f5cfe3671c60d154ced7e"></a>

```c
int bt_conn_auth_keypress_notify (struct bt_conn *conn, enum bt_conn_auth_keypress type)
```

相关声明：[bt_conn_auth_keypress_notify](#ga2987a902da4f5cfe3671c60d154ced7e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_auth_keypress](#ga57465d3a61214531ddaffc2c30939043)。

配对期间发送配对口令按键通知（Passkey Keypress Notification）。

<a id="r_ga89e5fc4bcab3f5598d20a9cd8ace5f59"></a>

```c
int bt_conn_auth_cancel (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_cancel](#ga89e5fc4bcab3f5598d20a9cd8ace5f59)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

取消正在进行的认证配对（Authenticated Pairing）。

<a id="r_gab8c3ecf2a3d68e54379917844a29d995"></a>

```c
int bt_conn_auth_passkey_confirm (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_passkey_confirm](#gab8c3ecf2a3d68e54379917844a29d995)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

回复使用者是否已确认配对口令（Passkey）匹配。

<a id="r_ga3e15b9deb6787d3e415bbea35c9aa91d"></a>

```c
int bt_conn_auth_pairing_confirm (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_pairing_confirm](#ga3e15b9deb6787d3e415bbea35c9aa91d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

回复使用者是否已确认传入的配对请求（Incoming Pairing）。

<a id="r_ga4002a1b092832807218afa8ad279ab98"></a>

```c
int bt_conn_auth_pincode_entry (struct bt_conn *conn, const char *pin)
```

相关声明：[bt_conn_auth_pincode_entry](#ga4002a1b092832807218afa8ad279ab98)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

使用输入的 PIN 码（PIN Code）回复。

<a id="r_gaf7849f332386f8903d35d6904f6c82b9"></a>

```c
struct bt_conn * bt_conn_create_br (const bt_addr_t *peer, const struct bt_br_conn_param *param)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_create_br](#gaf7849f332386f8903d35d6904f6c82b9)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_br_conn_param](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md)。

发起与远端设备的 BR／EDR 连接（Connection）。

<a id="r_ga11ae1b656683cebe9db6a53e5166ad7a"></a>

```c
struct bt_conn * bt_conn_lookup_addr_br (const bt_addr_t *peer)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_lookup_addr_br](#ga11ae1b656683cebe9db6a53e5166ad7a)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

根据地址查找现有基本速率连接（BR Connection）。

<a id="r_ga1b02a1ce8e48ad483d73d1efd803618c"></a>

```c
const bt_addr_t * bt_conn_get_dst_br (const struct bt_conn *conn)
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_conn_get_dst_br](#ga1b02a1ce8e48ad483d73d1efd803618c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的目标，即对端地址（Destination / Peer Address）。

<a id="r_ga3a7741f1e884168168a09e9ec5f28c49"></a>

```c
int bt_conn_br_switch_role (const struct bt_conn *conn, uint8_t role)
```

相关声明：[bt_conn_br_switch_role](#ga3a7741f1e884168168a09e9ec5f28c49)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改 conn 的角色（Role）。

<a id="r_gab6c2073091d1d08032c51aadb904ea3f"></a>

```c
int bt_conn_br_set_role_switch_enable (const struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_br_set_role_switch_enable](#gab6c2073091d1d08032c51aadb904ea3f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过设置连接的链路策略（Link Policy），启用／禁用该连接的角色切换（Role Switch）。

<a id="r_ga641f7f4ce7fe0641948a798881ecedcb"></a>

```c
int bt_conn_br_enter_sniff_mode (struct bt_conn *conn, uint16_t min_interval, uint16_t max_interval, uint16_t attempt, uint16_t timeout)
```

相关声明：[bt_conn_br_enter_sniff_mode](#ga641f7f4ce7fe0641948a798881ecedcb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查蓝牙连接并进入嗅探模式（Sniff Mode）。

<a id="r_gab1aedad7da2eecc6c30acbfcdf9fbfec"></a>

```c
int bt_conn_br_exit_sniff_mode (struct bt_conn *conn)
```

相关声明：[bt_conn_br_exit_sniff_mode](#gab1aedad7da2eecc6c30acbfcdf9fbfec)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

检查蓝牙连接并退出嗅探模式（Sniff Mode）。

<a id="r_ga910157e30fad972e8c606d1e1645603e"></a>

```c
int bt_conn_br_set_sniff_subrating (struct bt_conn *conn, uint16_t max_latency, uint16_t min_remote_timeout, uint16_t min_local_timeout)
```

相关声明：[bt_conn_br_set_sniff_subrating](#ga910157e30fad972e8c606d1e1645603e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BR／EDR 嗅探子速率参数（Sniff Subrating Parameters）。

<a id="r_ga76f872637f9b34c701c80d71ce7e585c"></a>

```c
int bt_conn_br_get_supervision_timeout (struct bt_conn *conn, uint16_t *timeout)
```

相关声明：[bt_conn_br_get_supervision_timeout](#ga76f872637f9b34c701c80d71ce7e585c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 BR／EDR 监督超时时间（Supervision Timeout）。

<a id="r_ga8516a5304ec78362ab66a9f18968d20d"></a>

```c
int bt_conn_br_set_supervision_timeout (struct bt_conn *conn, uint16_t timeout)
```

相关声明：[bt_conn_br_set_supervision_timeout](#ga8516a5304ec78362ab66a9f18968d20d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BR／EDR 监督超时时间（Supervision Timeout）。

<a id="r_gae5073b3666aff788f6f389d010a918a6"></a>

```c
int bt_conn_br_change_packet_type (const struct bt_conn *conn, uint16_t packet_type)
```

相关声明：[bt_conn_br_change_packet_type](#gae5073b3666aff788f6f389d010a918a6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更改 BR／EDR 连接数据包类型（Connection Packet Type）。

## 1.5\_详细说明（Detailed Documentation）

<a id="ga6f99f4adfcef36a4d738783921965ca6"></a>

### `BT_BR_CONN_PARAM`

```c
#define BT_BR_CONN_PARAM ( role_switch)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((struct bt_br_conn_param[]) { \
        BT_BR_CONN_PARAM_INIT(role_switch) \
 })
```

用于内联声明 BR／EDR 连接参数（Connection Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role_switch` | 允许角色切换（Role Switch）时为 `true`。 |

<a id="ga5ccdbff63a430a37a8a8077d8792f706"></a>

### `BT_BR_CONN_PARAM_DEFAULT`

```c
#define BT_BR_CONN_PARAM_DEFAULT BT_BR_CONN_PARAM(true)
```

```c
#include <zephyr/bluetooth/conn.h>
```

默认 BR／EDR 连接参数：允许角色切换（Role Switch）。

<a id="ga986f563bfb741c70fbee39b3948d9d8d"></a>

### `BT_BR_CONN_PARAM_INIT`

```c
#define BT_BR_CONN_PARAM_INIT ( role_switch)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
{ \
        .allow_role_switch = (role_switch), \
}
```

初始化基本速率／增强数据速率连接参数（BR/EDR Connection Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role_switch` | 允许角色切换（Role Switch）时为 `true`。 |

<a id="ga9227880a1ae5fc373d334171e1450f00"></a>

### `BT_CONN_CB_DEFINE`

```c
#define BT_CONN_CB_DEFINE ( _name)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(bt_conn_cb,                \
                                        _CONCAT(bt_conn_cb_,    \
                                                _name))
```

为连接事件（Connection Events）注册回调结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 回调结构体名称（Callback Structure Name）。 |

<a id="ga5e4ec28058d93bede65ccb9d20014e2e"></a>

### `bt_conn_dst_str`

```c
#define bt_conn_dst_str ( _conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
bt_conn_dst_tmp_str(_conn).str
```

获取指向连接目标，即对端地址（Destination / Peer Address）字符串的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_conn` | 指向连接对象（Connection Object）的指针。 |

**返回（Returns）**：返回值（Returns）：字符串指针，仅在完整表达式（Full Expression）结束之前有效。实际使用中，这主要适合用作 `printk`／`printf` 或日志调用的输入参数。

<a id="ga707cc62b12c89478aebd0488a464a776"></a>

### `BT_CONN_INTERVAL_TO_MS`

```c
#define BT_CONN_INTERVAL_TO_MS ( interval)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((interval) * 5U / 4U)
```

将连接间隔（Connection Interval）转换为毫秒。

乘以 `1.25` 可得到毫秒数（Milliseconds）。

注意，此结果可能不准确，例如 `7.5 ms` 无法用整数精确表示（Integer Representation）。

<a id="ga0a5fac126005684847ee7509bb98e382"></a>

### `BT_CONN_INTERVAL_TO_US`

```c
#define BT_CONN_INTERVAL_TO_US ( interval)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((interval) * 1250U)
```

将连接间隔（Connection Interval）转换为微秒。

乘以 `1250` 可得到微秒数（Microseconds）。

<a id="gab4203c55c20d83256ca036148c14a00d"></a>

### `BT_CONN_LE_CREATE_CONN`

```c
#define BT_CONN_LE_CREATE_CONN
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_CREATE_PARAM(BT_CONN_LE_OPT_NONE, \
                        BT_GAP_SCAN_FAST_INTERVAL, \
                        BT_GAP_SCAN_FAST_INTERVAL)
```

默认低功耗蓝牙创建连接参数（LE Create Connection Parameters）。

将扫描间隔（Scan Interval）设为与扫描窗口（Scan Window）相等，即可连续扫描。

<a id="gaaba7c37a5c6e98e7b62ac12bde814d5d"></a>

### `BT_CONN_LE_CREATE_CONN_AUTO`

```c
#define BT_CONN_LE_CREATE_CONN_AUTO
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_CREATE_PARAM(BT_CONN_LE_OPT_NONE, \
                        BT_GAP_SCAN_FAST_INTERVAL, \
                        BT_GAP_SCAN_FAST_WINDOW)
```

使用过滤接受列表（Filter Accept List）的默认低功耗蓝牙创建连接参数。

扫描窗口（Scan Window）：`30 ms`；扫描间隔（Scan Interval）：`60 ms`。

<a id="gae86425d432078e2ddca260eebc2802f1"></a>

### `BT_CONN_LE_CREATE_PARAM`

```c
#define BT_CONN_LE_CREATE_PARAM ( _options, _interval, _window )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((struct bt_conn_le_create_param[]) { \
        BT_CONN_LE_CREATE_PARAM_INIT(_options, _interval, _window) \
 })
```

用于内联声明创建连接参数（Create Connection Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_options` | 创建连接选项（Create Connection Options）。 |
| `_interval` | 创建连接时的扫描间隔（Scan Interval），单位为 `N * 0.625 ms`。 |
| `_window` | 创建连接时的扫描窗口（Scan Window），单位为 `N * 0.625 ms`。 |

<a id="ga8ac93a19c34d2821c158f310879fe00d"></a>

### `BT_CONN_LE_CREATE_PARAM_INIT`

```c
#define BT_CONN_LE_CREATE_PARAM_INIT ( _options, _interval, _window )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
{ \
        .options = (_options), \
        .interval = (_interval), \
        .window = (_window), \
        .interval_coded = 0, \
        .window_coded = 0, \
        .timeout = 0, \
}
```

初始化创建连接参数（Create Connection Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_options` | 创建连接选项（Create Connection Options）。 |
| `_interval` | 创建连接时的扫描间隔（Scan Interval），单位为 `N * 0.625 ms`。 |
| `_window` | 创建连接时的扫描窗口（Scan Window），单位为 `N * 0.625 ms`。 |

<a id="ga5354b9973117f94b88c61fb0ea726a4b"></a>

### `BT_CONN_LE_CS_MODE_MAIN_MODE_PART`

```c
#define BT_CONN_LE_CS_MODE_MAIN_MODE_PART ( x)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((x) & 0x3)
```

从 bt_conn_le_cs_mode 提取主模式部分（Main Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | `bt_conn_le_cs_mode` 值（Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 对应 `BT_HCI_OP_LE_CS_MAIN_MODE_1`（`0x01`）。 |
| `2` | 对应 `BT_HCI_OP_LE_CS_MAIN_MODE_2`（`0x02`）。 |
| `3` | 对应 `BT_HCI_OP_LE_CS_MAIN_MODE_3`（`0x03`）。 |

**说明（Note）**：注意（Note）：返回值与 HCI 主模式（Main Mode）值一致。

<a id="ga19d2cd20af6f2652164a5677ee8863d5"></a>

### `BT_CONN_LE_CS_MODE_SUB_MODE_PART`

```c
#define BT_CONN_LE_CS_MODE_SUB_MODE_PART ( x)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
(((x) >> 4) & 0x3)
```

从 bt_conn_le_cs_mode 提取子模式部分（Sub-mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | `bt_conn_le_cs_mode` 值（Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | `BT_HCI_OP_LE_CS_SUB_MODE_UNUSED`（`0xFF`）的内部编码（Internal Encoding）。 |
| `1` | 对应 `BT_HCI_OP_LE_CS_SUB_MODE_1`（`0x01`）。 |
| `2` | 对应 `BT_HCI_OP_LE_CS_SUB_MODE_2`（`0x02`）。 |
| `3` | 对应 `BT_HCI_OP_LE_CS_SUB_MODE_3`（`0x03`）。 |

**说明（Note）**：注意（Note）：数值 `0` 编码表示 HCI 值 `0xFF`，以便 `bt_conn_le_cs_mode` 能够存放在一个字节中。要获得 HCI 子模式值，使用 `(sub_mode == 0 ? 0xFF : sub_mode)`；其中 `sub_mode` 是此宏返回的值。

<a id="ga102b97de8689fe3fb53f9691009de87f"></a>

### `BT_CONN_LE_DATA_LEN_PARAM`

```c
#define BT_CONN_LE_DATA_LEN_PARAM ( _tx_max_len, _tx_max_time )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((struct bt_conn_le_data_len_param[]) { \
        BT_CONN_LE_DATA_LEN_PARAM_INIT(_tx_max_len, _tx_max_time) \
 })
```

用于内联声明发送数据长度参数（Transmit Data Length Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_tx_max_len` | 链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。 |
| `_tx_max_time` | 链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。 |

<a id="ga98f9dab71897382cf1187259a3b5660e"></a>

### `BT_CONN_LE_DATA_LEN_PARAM_INIT`

```c
#define BT_CONN_LE_DATA_LEN_PARAM_INIT ( _tx_max_len, _tx_max_time )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
{ \
        .tx_max_len = (_tx_max_len), \
        .tx_max_time = (_tx_max_time), \
}
```

初始化发送数据长度参数（Transmit Data Length Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_tx_max_len` | 链路层发送载荷的最大大小（Maximum Link Layer transmission payload size），单位为字节。 |
| `_tx_max_time` | 链路层发送载荷的最长时间（Maximum Link Layer transmission payload time），单位为微秒。 |

<a id="gaf01791831e52ee5976679fc0fac9118c"></a>

### `BT_CONN_LE_FRAME_SPACE_MAX`

```c
#define BT_CONN_LE_FRAME_SPACE_MAX (10000U)
```

```c
#include <zephyr/bluetooth/conn.h>
```

最大帧间隔（Maximum frame space），单位为微秒。

定义见蓝牙核心规范（Bluetooth Core Specification）第 4 卷、E 部分、第 7.8.151 节。

<a id="ga1b9b7d5bd6500ef1195c5da0275247ee"></a>

### `BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL`

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
(BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK | \
 BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK | \
 BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK)
```

<a id="gacce78fed479c9d7e9b394488d5e466d7"></a>

### `BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS`

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
(BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK | \
 BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK)
```

<a id="gacdf0d72c8f6dfe6e13c714148f04df3c"></a>

### `BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS`

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
(BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK | \
 BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK)
```

<a id="gadcb74ad947485dd81dfd59a82d3b0db6"></a>

### `BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS`

```c
#define BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS 41
```

```c
#include <zephyr/bluetooth/conn.h>
```

允许的最大连接间隔组数（Maximum Connection Interval Groups）。

根据 HCI 事件大小约束，实际最多为 `41` 组（Groups）：`(HCI event max size - cmd_complete overhead - response fields) / sizeof(group)`，即 `(255 - 4 - 3) / 6 = 41` 组。

<a id="ga39b69f0978f74b5f13f829e908b7cebb"></a>

### `BT_CONN_LE_PHY_PARAM`

```c
#define BT_CONN_LE_PHY_PARAM ( _pref_tx_phy, _pref_rx_phy )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((struct bt_conn_le_phy_param []) { \
        BT_CONN_LE_PHY_PARAM_INIT(_pref_tx_phy, _pref_rx_phy) \
 })
```

用于内联声明物理层参数（PHY Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_pref_tx_phy` | 首选发送物理层的位掩码（Preferred transmit PHYs）。 |
| `_pref_rx_phy` | 首选接收物理层的位掩码（Preferred receive PHYs）。 |

<a id="ga3ec555bb4ace5e9c7c13735820fd31de"></a>

### `BT_CONN_LE_PHY_PARAM_1M`

```c
#define BT_CONN_LE_PHY_PARAM_1M
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_1M, \
BT_GAP_LE_PHY_1M)
```

仅低功耗蓝牙 1M 物理层（LE 1M PHY）。

<a id="ga633126e356658886e9fa3f3217cb4e2c"></a>

### `BT_CONN_LE_PHY_PARAM_2M`

```c
#define BT_CONN_LE_PHY_PARAM_2M
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_2M, \
BT_GAP_LE_PHY_2M)
```

仅低功耗蓝牙 2M 物理层（LE 2M PHY）。

<a id="ga02c9d7a04ccf2f043293aed7a7f767a7"></a>

### `BT_CONN_LE_PHY_PARAM_ALL`

```c
#define BT_CONN_LE_PHY_PARAM_ALL
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_1M |   \
BT_GAP_LE_PHY_2M |   \
BT_GAP_LE_PHY_CODED, \
BT_GAP_LE_PHY_1M |   \
BT_GAP_LE_PHY_2M |   \
BT_GAP_LE_PHY_CODED)
```

全部低功耗蓝牙物理层（LE PHYs）。

<a id="ga4915244a6cd70995514d6dde1ee0b45f"></a>

### `BT_CONN_LE_PHY_PARAM_CODED`

```c
#define BT_CONN_LE_PHY_PARAM_CODED
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_PHY_PARAM(BT_GAP_LE_PHY_CODED, \
BT_GAP_LE_PHY_CODED)
```

仅低功耗蓝牙编码物理层（LE Coded PHY）。

<a id="gabca56de0c82c14995738952dafb1fe2d"></a>

### `BT_CONN_LE_PHY_PARAM_INIT`

```c
#define BT_CONN_LE_PHY_PARAM_INIT ( _pref_tx_phy, _pref_rx_phy )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
{ \
        .options = BT_CONN_LE_PHY_OPT_NONE, \
        .pref_tx_phy = (_pref_tx_phy), \
        .pref_rx_phy = (_pref_rx_phy), \
}
```

初始化物理层参数（PHY Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_pref_tx_phy` | 首选发送物理层的位掩码（Preferred transmit PHYs）。 |
| `_pref_rx_phy` | 首选接收物理层的位掩码（Preferred receive PHYs）。 |

<a id="ga3fac32ef426900046d8e38bbd4b7c2d2"></a>

### `BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP`

```c
#define BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP 0xFF
```

```c
#include <zephyr/bluetooth/conn.h>
```

表示 L2CAP 连接参数更新过程（Connection Parameter Update Procedure，CPUP）被拒绝的合成错误值（Synthetic Error Value）。

当远端不支持 HCI 连接参数请求过程（Connection Parameter Request，CPR），且后备的 L2CAP 连接参数更新过程（CPUP）被拒绝时，将此值作为 `hci_err` 参数传给 `bt_conn_cb::le_param_update_rejected`。这是主机内部的哨兵值（Sentinel），不是真实的 HCI 错误码。

<a id="gaf4b1395e345f1bf01b83a890bf9a5083"></a>

### `BT_CONN_SCI_INTERVAL_TO_US`

```c
#define BT_CONN_SCI_INTERVAL_TO_US ( _interval)
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((_interval) * BT_HCI_LE_SCI_INTERVAL_UNIT_US)
```

将较短连接间隔（Shorter Connection Interval）转换为微秒。

乘以 `125` 可得到微秒数（Microseconds）。

<a id="ga940d55c0d84c0cb8f09bc41074ae50d0"></a>

### `BT_LE_CONN_PARAM`

```c
#define BT_LE_CONN_PARAM ( int_min, int_max, lat, to )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
((struct bt_le_conn_param[]) { \
        BT_LE_CONN_PARAM_INIT(int_min, int_max, lat, to) \
 })
```

用于内联声明连接参数（Connection Parameters）的辅助宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `int_min` | 最小连接间隔（Minimum Connection Interval），单位为 `N * 1.25 ms`。 |
| `int_max` | 最大连接间隔（Maximum Connection Interval），单位为 `N * 1.25 ms`。 |
| `lat` | 连接延迟（Connection Latency）。 |
| `to` | 连接监督超时（Supervision Timeout），单位为 `N * 10 ms`。 |

<a id="ga82df8f439aeb3a156f4238deb085534a"></a>

### `BT_LE_CONN_PARAM_DEFAULT`

```c
#define BT_LE_CONN_PARAM_DEFAULT
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_LE_CONN_PARAM(BT_GAP_INIT_CONN_INT_MIN, BT_GAP_INIT_CONN_INT_MAX, 0,                    \
                 BT_GAP_MS_TO_CONN_TIMEOUT(4000))
```

默认低功耗蓝牙连接参数（LE Connection Parameters）：连接间隔 30–50 ms，延迟 0，超时 4 s。

<a id="ga81de567c4c8cb691ef8b02633b42e342"></a>

### `BT_LE_CONN_PARAM_INIT`

```c
#define BT_LE_CONN_PARAM_INIT ( int_min, int_max, lat, to )
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
{ \
        .interval_min = (int_min), \
        .interval_max = (int_max), \
        .latency = (lat), \
        .timeout = (to), \
}
```

初始化连接参数（Connection Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `int_min` | 最小连接间隔（Minimum Connection Interval），单位为 `N * 1.25 ms`。 |
| `int_max` | 最大连接间隔（Maximum Connection Interval），单位为 `N * 1.25 ms`。 |
| `lat` | 连接延迟（Connection Latency）。 |
| `to` | 连接监督超时（Supervision Timeout），单位为 `N * 10 ms`。 |

<a id="gaf66746d834f7556dc77659741e27e0c9"></a>

### `BT_LE_DATA_LEN_PARAM_DEFAULT`

```c
#define BT_LE_DATA_LEN_PARAM_DEFAULT
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_DATA_LEN_PARAM(BT_GAP_DATA_LEN_DEFAULT, \
                          BT_GAP_DATA_TIME_DEFAULT)
```

默认低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="ga9cc26afda3c507cb5439184fedcd61ba"></a>

### `BT_LE_DATA_LEN_PARAM_MAX`

```c
#define BT_LE_DATA_LEN_PARAM_MAX
```

```c
#include <zephyr/bluetooth/conn.h>
```

展开值（Value）：

```c
BT_CONN_LE_DATA_LEN_PARAM(BT_GAP_DATA_LEN_MAX, \
                          BT_GAP_DATA_TIME_MAX)
```

最大低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="ga988dbb7aea2ac136e3bc8efdf6f7478c"></a>

### `BT_PASSKEY_RAND`

```c
#define BT_PASSKEY_RAND 0xffffffff
```

```c
#include <zephyr/bluetooth/conn.h>
```

使用 bt_conn_auth_cb 的 app_passkey 回调时，可用于生成随机配对口令（Passkey）的特殊口令值。

<a id="ga3afc8024ddbcd3bf5a809706e39f74bc"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_CONN_LE_OPT_CODED` | 启用低功耗编码物理层（LE Coded PHY），并启用该物理层上的扫描。 |
| `BT_CONN_LE_OPT_NO_1M` | 禁用低功耗 1M 物理层（LE 1M PHY），并禁用该物理层上的扫描。注意（Note）：需要 `BT_CONN_LE_OPT_CODED`。 |

**说明（Note）**：注意（Note）：需要 `BT_CONN_LE_OPT_CODED`。

<a id="ga9c54d2e44903cf7c4e5c97e223069dbc"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_ROLE_CENTRAL` |  |
| `BT_CONN_ROLE_PERIPHERAL` |  |

<a id="ga08eb37185a763212e65c47ab4c886eca"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/bluetooth/conn.h>
```

连接物理层选项（Connection PHY options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_PHY_OPT_NONE` | 未指定选项时使用的便捷值（Convenience Value）。 |
| `BT_CONN_LE_PHY_OPT_CODED_S2` | 发送时优先使用 `S=2` 编码的 LE Coded 物理层（PHY）。 |
| `BT_CONN_LE_PHY_OPT_CODED_S8` | 发送时优先使用 `S=8` 编码的 LE Coded 物理层（PHY）。 |

<a id="ga57465d3a61214531ddaffc2c30939043"></a>

### `bt_conn_auth_keypress`

```c
enum bt_conn_auth_keypress
```

```c
#include <zephyr/bluetooth/conn.h>
```

配对口令按键通知类型（Passkey Keypress Notification Type）。

数值与核心规范中配对按键通知协议数据单元（Pairing Keypress Notification PDU）的取值相同。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED` |  |
| `BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED` |  |
| `BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED` |  |
| `BT_CONN_AUTH_KEYPRESS_CLEARED` |  |
| `BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED` |  |

<a id="gafe14d64a64383b097760764697b035e2"></a>

### `bt_conn_le_cs_capability_rtt_aa_only`

```c
enum bt_conn_le_cs_capability_rtt_aa_only
```

```c
#include <zephyr/bluetooth/conn.h>
```

支持的仅接入地址往返时间精度（AA-Only RTT Precision）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP` | 不支持仅使用接入地址的往返时间变体（AA-Only RTT Variant）。 |
| `BT_CONN_LE_CS_RTT_AA_ONLY_10NS` | 飞行时间精度（Time-of-flight Accuracy）为 `10 ns`。 |
| `BT_CONN_LE_CS_RTT_AA_ONLY_150NS` | 飞行时间精度（Time-of-flight Accuracy）为 `150 ns`。 |

<a id="ga5568443825fc1ce9534753d8918aa813"></a>

### `bt_conn_le_cs_capability_rtt_random_payload`

```c
enum bt_conn_le_cs_capability_rtt_random_payload
```

```c
#include <zephyr/bluetooth/conn.h>
```

支持的随机有效载荷往返时间精度（Random Payload RTT Precision）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP` | 不支持随机载荷往返时间变体（Random Payload RTT Variant）。 |
| `BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS` | 飞行时间精度（Time-of-flight Accuracy）为 `10 ns`。 |
| `BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS` | 飞行时间精度（Time-of-flight Accuracy）为 `150 ns`。 |

<a id="ga1892ec23ca3b1818287a9d7dafc16433"></a>

### `bt_conn_le_cs_capability_rtt_sounding`

```c
enum bt_conn_le_cs_capability_rtt_sounding
```

```c
#include <zephyr/bluetooth/conn.h>
```

支持的探测序列往返时间精度（Sounding Sequence RTT Precision）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP` | 不支持探测序列往返时间变体（Sounding Sequence RTT Variant）。 |
| `BT_CONN_LE_CS_RTT_SOUNDING_10NS` | 飞行时间精度（Time-of-flight Accuracy）为 `10 ns`。 |
| `BT_CONN_LE_CS_RTT_SOUNDING_150NS` | 飞行时间精度（Time-of-flight Accuracy）为 `150 ns`。 |

<a id="gaf2331ec1f1222de51fc4f30566e1c52b"></a>

### `bt_conn_le_cs_ch3c_shape`

```c
enum bt_conn_le_cs_ch3c_shape
```

```c
#include <zephyr/bluetooth/conn.h>
```

信道探测信道序列形状（Channel Sounding Channel Sequence Shape）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_CH3C_SHAPE_HAT` | 对用户指定的信道序列使用帽形（Hat Shape）。 |
| `BT_CONN_LE_CS_CH3C_SHAPE_X` | 对用户指定的信道序列使用 X 形（X Shape）。 |

<a id="ga34e4837a77c7afd6999095985ddad4f0"></a>

### `bt_conn_le_cs_chsel_type`

```c
enum bt_conn_le_cs_chsel_type
```

```c
#include <zephyr/bluetooth/conn.h>
```

信道探测信道选择类型（Channel Sounding Channel Selection Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_CHSEL_TYPE_3B` | 对非模式 0 的信道探测步骤（CS Steps）使用信道选择算法 3b（Channel Selection Algorithm #3b）。 |
| `BT_CONN_LE_CS_CHSEL_TYPE_3C` | 对非模式 0 的信道探测步骤（CS Steps）使用信道选择算法 3c（Channel Selection Algorithm #3c）。 |

<a id="ga2f757b15d1d5006ce2fa6a7a78082156"></a>

### `bt_conn_le_cs_mode`

```c
enum bt_conn_le_cs_mode
```

```c
#include <zephyr/bluetooth/conn.h>
```

信道探测模式（Channel Sounding Mode），包括主模式与子模式。

表示信道探测（Channel Sounding，CS）的主模式与子模式组合。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE` | 主模式 1：往返时间（RTT）；子模式：未使用。 |
| `BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE` | 主模式 2：基于相位的测距（PBR）；子模式：未使用。 |
| `BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE` | 主模式 3：往返时间（RTT）与基于相位的测距（PBR）；子模式：未使用。 |
| `BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1` | 主模式 2：基于相位的测距（PBR）；子模式 1：往返时间（RTT）。 |
| `BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3` | 主模式 2：基于相位的测距（PBR）；子模式 3：往返时间（RTT）与基于相位的测距（PBR）。 |
| `BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2` | 主模式 3：往返时间（RTT）与基于相位的测距（PBR）；子模式 2：基于相位的测距（PBR）。 |

**说明（Note）**：注意（Note）：底层数值采用内部编码（Internal Encoding），不属于稳定 API。检查原始枚举值时，不要假定它是 HCI 值的直接拼接。

**参阅（See Also）**：另请参见（See Also）：`BT_CONN_LE_CS_MODE_MAIN_MODE_PART`、`BT_CONN_LE_CS_MODE_SUB_MODE_PART`。

<a id="ga3196a0eb1c7497e93d7c646713d2fc79"></a>

### `bt_conn_le_cs_procedure_abort_reason`

```c
enum bt_conn_le_cs_procedure_abort_reason
```

```c
#include <zephyr/bluetooth/conn.h>
```

过程中止原因（Procedure Abort Reason）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED` |  |
| `BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED` |  |
| `BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS` |  |
| `BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED` |  |
| `BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED` |  |

<a id="ga9a1dc2010c5237466de87160944630d3"></a>

### `bt_conn_le_cs_procedure_done_status`

```c
enum bt_conn_le_cs_procedure_done_status
```

```c
#include <zephyr/bluetooth/conn.h>
```

过程完成状态（Procedure Done Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_PROCEDURE_COMPLETE` |  |
| `BT_CONN_LE_CS_PROCEDURE_INCOMPLETE` |  |
| `BT_CONN_LE_CS_PROCEDURE_ABORTED` |  |

<a id="gaf3653de72793f775e33fd9eb04c3e7a2"></a>

### `bt_conn_le_cs_procedure_enable_state`

```c
enum bt_conn_le_cs_procedure_enable_state
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_PROCEDURES_DISABLED` |  |
| `BT_CONN_LE_CS_PROCEDURES_ENABLED` |  |

<a id="ga0e6f6d4fdbdfc3ed75fef4a95136076f"></a>

### `bt_conn_le_cs_role`

```c
enum bt_conn_le_cs_role
```

```c
#include <zephyr/bluetooth/conn.h>
```

信道探测角色（Channel Sounding Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_ROLE_INITIATOR` | 信道探测发起方角色（CS Initiator Role）。 |
| `BT_CONN_LE_CS_ROLE_REFLECTOR` | 信道探测反射方角色（CS Reflector Role）。 |

<a id="gaffd6abf9b92cc8d8463797a73b840f51"></a>

### `bt_conn_le_cs_rtt_type`

```c
enum bt_conn_le_cs_rtt_type
```

```c
#include <zephyr/bluetooth/conn.h>
```

信道探测往返时间类型（Channel Sounding RTT Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_RTT_TYPE_AA_ONLY` | 仅接入地址（AA）的往返时间（RTT）测量。 |
| `BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING` | 采用 32 位探测序列（Sounding Sequence）的 RTT。 |
| `BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING` | 采用 96 位探测序列（Sounding Sequence）的 RTT。 |
| `BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM` | 采用 32 位随机序列（Random Sequence）的 RTT。 |
| `BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM` | 采用 64 位随机序列（Random Sequence）的 RTT。 |
| `BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM` | 采用 96 位随机序列（Random Sequence）的 RTT。 |
| `BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM` | 采用 128 位随机序列（Random Sequence）的 RTT。 |

<a id="ga6394906c6da40c9bebfaeb05de9fd5be"></a>

### `bt_conn_le_cs_subevent_abort_reason`

```c
enum bt_conn_le_cs_subevent_abort_reason
```

```c
#include <zephyr/bluetooth/conn.h>
```

子事件中止原因（Subevent Abort Reason）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED` |  |
| `BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED` |  |
| `BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC` |  |
| `BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT` |  |
| `BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED` |  |

<a id="ga8e54a191b889b1d5ed3e1fbb648d9bc7"></a>

### `bt_conn_le_cs_subevent_done_status`

```c
enum bt_conn_le_cs_subevent_done_status
```

```c
#include <zephyr/bluetooth/conn.h>
```

子事件完成状态（Subevent Done Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_SUBEVENT_COMPLETE` |  |
| `BT_CONN_LE_CS_SUBEVENT_ABORTED` |  |

<a id="gaadbf6a4dba28aec90ea07b7da634e1bb"></a>

### `bt_conn_le_cs_sync_phy`

```c
enum bt_conn_le_cs_sync_phy
```

```c
#include <zephyr/bluetooth/conn.h>
```

CS 同步使用的信道探测物理层（Channel Sounding PHY）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_CS_SYNC_1M_PHY` | LE 1M 物理层（LE 1M PHY）。 |
| `BT_CONN_LE_CS_SYNC_2M_PHY` | LE 2M 物理层（LE 2M PHY）。 |
| `BT_CONN_LE_CS_SYNC_2M_2BT_PHY` | 低功耗 2M 2BT 物理层（LE 2M 2BT PHY）。 |

<a id="gab7acdbdf273fc760799cf0d8cf71591c"></a>

### `bt_conn_le_cs_tone_antenna_config_selection`

```c
enum bt_conn_le_cs_tone_antenna_config_selection
```

```c
#include <zephyr/bluetooth/conn.h>
```

CS 测试音调天线配置选择（CS Test Tone Antenna Config Selection）。

参见蓝牙核心规范（Bluetooth Core Specification）第 6 卷 A 部分第 5.3 节，以及第 6 卷 H 部分第 4.7 节。

这些枚举值（Enum Values）是下表中的索引，其中 `N_AP` 为最大天线路径数量，范围是 `[1, 4]`。

天线配置表（Antenna Configuration Table）：

| 配置索引（Config Index） | 总路径数（Total Paths） | 发起方天线数（Initiator: # Antennas） | 反射方天线数（Reflector: # Antennas） | 配置（Config） |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1 | 1 | 1:1 |
| 1 | 2 | 2 | 1 | N_AP:1 |
| 2 | 3 | 3 | 1 | N_AP:1 |
| 3 | 4 | 4 | 1 | N_AP:1 |
| 4 | 2 | 1 | 2 | 1:N_AP |
| 5 | 3 | 1 | 3 | 1:N_AP |
| 6 | 4 | 1 | 4 | 1:N_AP |
| 7 | 4 | 2 | 2 | 2:2 |



因此，可能的天线配置（Antenna Configurations）分为四组：

- `1:1` 配置：发起方（Initiator）与反射方（Reflector）各支持 1 根天线。
- `1:N_AP` 配置：发起方（Initiator）支持 1 根天线，反射方（Reflector）支持 `N_AP` 根天线，其中 `N_AP` 范围为 `[2, 4]`。
- `N_AP:1` 配置：发起方（Initiator）支持 `N_AP` 根天线，反射方（Reflector）支持 1 根天线，其中 `N_AP` 范围为 `[2, 4]`。
- `2:2` 配置：发起方（Initiator）与反射方（Reflector）各支持 2 根天线，且 `N_AP = 4`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1` | 发起方（Initiator，设备 A）：1 根天线；反射方（Reflector，设备 B）：1 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1` | 发起方（Initiator，设备 A）：2 根天线；反射方（Reflector，设备 B）：1 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1` | 发起方（Initiator，设备 A）：3 根天线；反射方（Reflector，设备 B）：1 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1` | 发起方（Initiator，设备 A）：4 根天线；反射方（Reflector，设备 B）：1 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2` | 发起方（Initiator，设备 A）：1 根天线；反射方（Reflector，设备 B）：2 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3` | 发起方（Initiator，设备 A）：1 根天线；反射方（Reflector，设备 B）：3 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4` | 发起方（Initiator，设备 A）：1 根天线；反射方（Reflector，设备 B）：4 根天线。 |
| `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2` | 发起方（Initiator，设备 A）：2 根天线；反射方（Reflector，设备 B）：2 根天线。 |

<a id="gae60f156d2aa01814ad485786e00c4ca7"></a>

### `bt_conn_le_frame_space_update_initiator`

```c
enum bt_conn_le_frame_space_update_initiator
```

```c
#include <zephyr/bluetooth/conn.h>
```

帧间隔更新发起方（Frame Space Update Initiator）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST` | 由本地主机（Local Host）发起。 |
| `BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER` | 由本地控制器（Local Controller）发起。 |
| `BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER` | 由对端（Peer）发起。 |

<a id="gaf43d7aa3ad1c8d2bde8b04e650fe7b7e"></a>

### `bt_conn_le_path_loss_zone`

```c
enum bt_conn_le_path_loss_zone
```

```c
#include <zephyr/bluetooth/conn.h>
```

已进入的路径损耗区域（Path Loss Zone）。

最近一次低功耗路径损耗监测阈值变更事件（LE Path Loss Monitoring Threshold Change）中进入的路径损耗区间，定义见核心规范 5.4 版第 4 卷 E 部分第 7.7.65.32 节。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW` | 已进入低路径损耗区间（Low Path Loss Zone）。 |
| `BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE` | 已进入中路径损耗区间（Middle Path Loss Zone）。 |
| `BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH` | 已进入高路径损耗区间（High Path Loss Zone）。 |
| `BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE` | 路径损耗（Path Loss）变为不可用。 |

**说明（Note）**：注意（Note）：新增了 `BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE`，用于通知路径损耗变为不可用。

<a id="ga737d8118f8aba8985292d92d0604b190"></a>

### `bt_conn_le_tx_power_phy`

```c
enum bt_conn_le_tx_power_phy
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_LE_TX_POWER_PHY_NONE` | 未设置物理层（PHY）时使用的便捷宏。 |
| `BT_CONN_LE_TX_POWER_PHY_1M` | LE 1M 物理层（LE 1M PHY）。 |
| `BT_CONN_LE_TX_POWER_PHY_2M` | LE 2M 物理层（LE 2M PHY）。 |
| `BT_CONN_LE_TX_POWER_PHY_CODED_S8` | 采用 `S=8` 编码的低功耗编码物理层（LE Coded PHY）。 |
| `BT_CONN_LE_TX_POWER_PHY_CODED_S2` | 采用 `S=2` 编码的低功耗编码物理层（LE Coded PHY）。 |

<a id="ga9442c1479db60e2db40a2ea6de565282"></a>

### `bt_conn_state`

```c
enum bt_conn_state
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_STATE_DISCONNECTED` | 信道已断开（Disconnected）。 |
| `BT_CONN_STATE_CONNECTING` | 信道处于正在连接状态（Connecting）。 |
| `BT_CONN_STATE_CONNECTED` | 通道已连接（Connected），可以承载上层流量。 |
| `BT_CONN_STATE_DISCONNECTING` | 信道处于正在断开状态（Disconnecting）。 |

<a id="gab8dde20ae75b51f1e28dbeed06001f20"></a>

### `bt_conn_type`

```c
enum bt_conn_type
```

```c
#include <zephyr/bluetooth/conn.h>
```

连接类型（Connection Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CONN_TYPE_LE` | 低功耗连接类型（LE Connection Type）。 |
| `BT_CONN_TYPE_BR` | 基本速率／增强数据率连接类型（BR/EDR Connection Type）。 |
| `BT_CONN_TYPE_SCO` | 同步面向连接类型（SCO Connection Type）。 |
| `BT_CONN_TYPE_ISO` | 等时连接类型（ISO Connection Type）。 |
| `BT_CONN_TYPE_ALL` | 全部连接类型（All Connection Type）。 |

<a id="gaa9420ff489fd5857ff076406442679ff"></a>

### `bt_security_err`

```c
enum bt_security_err
```

```c
#include <zephyr/bluetooth/conn.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SECURITY_ERR_SUCCESS` | 安全过程成功（Security Procedure Successful）。 |
| `BT_SECURITY_ERR_AUTH_FAIL` | 认证失败（Authentication Failed）。 |
| `BT_SECURITY_ERR_PIN_OR_KEY_MISSING` | 缺少 PIN 或加密密钥（Encryption Key）。 |
| `BT_SECURITY_ERR_OOB_NOT_AVAILABLE` | 带外数据（OOB Data）不可用。 |
| `BT_SECURITY_ERR_AUTH_REQUIREMENT` | 无法达到所请求的安全级别（Security Level）。 |
| `BT_SECURITY_ERR_PAIR_NOT_SUPPORTED` | 不支持配对（Pairing Not Supported）。 |
| `BT_SECURITY_ERR_PAIR_NOT_ALLOWED` | 不允许配对（Pairing Not Allowed）。 |
| `BT_SECURITY_ERR_INVALID_PARAM` | 参数无效（Invalid Parameters）。 |
| `BT_SECURITY_ERR_KEY_REJECTED` | 分发的密钥被拒绝（Distributed Key Rejected）。 |
| `BT_SECURITY_ERR_UNSPECIFIED` | 配对失败（Pairing Failed），但无法给出确切原因。 |

<a id="ga2f8712bbf3410de5cbe6ce489fe30e5e"></a>

### `bt_security_flag`

```c
enum bt_security_flag
```

```c
#include <zephyr/bluetooth/conn.h>
```

安全信息标志（Security Info Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SECURITY_FLAG_SC` | 使用安全连接（Secure Connections）完成配对。 |
| `BT_SECURITY_FLAG_OOB` | 使用带外方法（Out of Band，OOB）完成配对。 |

<a id="gaf0c56cd26c4147f6c9f0faa11fa01783"></a>

### `bt_security_t`

```c
enum bt_security_t
```

```c
#include <zephyr/bluetooth/conn.h>
```

安全级别（Security Level）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_SECURITY_L0` | 级别 0（Level 0）：仅用于 BR/EDR 的特殊情况，例如 SDP。 |
| `BT_SECURITY_L1` | 级别 1（Level 1）：无加密，也无身份验证（Authentication）。 |
| `BT_SECURITY_L2` | 级别 2（Level 2）：有加密，无身份验证，即无中间人攻击防护（MITM）。 |
| `BT_SECURITY_L3` | 级别 3（Level 3）：有加密和身份验证，具备中间人攻击防护（MITM）。 |
| `BT_SECURITY_L4` | 级别 4（Level 4）：经过身份验证的安全连接（Authenticated Secure Connections），并使用 128 位密钥。 |
| `BT_SECURITY_FORCE_PAIR` | 强制执行新配对过程（Pairing Procedure）的标志位，与请求的安全级别按位或组合。 |

<a id="ga89e5fc4bcab3f5598d20a9cd8ace5f59"></a>

### `bt_conn_auth_cancel()`

```c
int bt_conn_auth_cancel ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

取消正在进行的认证配对（Authenticated Pairing）。

此函数允许取消正在进行的需身份验证配对（Authenticated Pairing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="ga81077385583d71c248a1eb6aab9ee86e"></a>

### `bt_conn_auth_cb_overlay()`

```c
int bt_conn_auth_cb_overlay ( struct bt_conn * conn, const struct bt_conn_auth_cb * cb )
```

```c
#include <zephyr/bluetooth/conn.h>
```

为给定连接覆盖所使用的认证回调（Authentication Callbacks）。

此函数仅适用于蓝牙低功耗连接（Bluetooth LE Connections），必须启用 `CONFIG_BT_SMP`。

如果安全管理协议（SMP）模块中的安全过程已开始，就不能覆盖给定连接的身份验证回调（Authentication Callbacks）。每个连接只能调用此函数一次。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="ga1bf13d2dfdbdf0a72f9b1c759ef23f60"></a>

### `bt_conn_auth_cb_register()`

```c
int bt_conn_auth_cb_register ( const struct bt_conn_auth_cb * cb)
```

```c
#include <zephyr/bluetooth/conn.h>
```

注册认证回调（Authentication Callbacks）。

注册回调以处理需身份验证的配对（Authenticated Pairing）。传入 `NULL` 会注销此前的回调结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="gac6684a8089ebd495b539d661cf9fd13f"></a>

### `bt_conn_auth_info_cb_register()`

```c
int bt_conn_auth_info_cb_register ( struct bt_conn_auth_info_cb * cb)
```

```c
#include <zephyr/bluetooth/conn.h>
```

注册认证信息回调（Authentication Information Callbacks）。

注册回调以获取需身份验证的配对信息（Authenticated Pairing Information），可以多次注册。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="gac73a60b8b6b569b84fe17f707fa33f37"></a>

### `bt_conn_auth_info_cb_unregister()`

```c
int bt_conn_auth_info_cb_unregister ( struct bt_conn_auth_info_cb * cb)
```

```c
#include <zephyr/bluetooth/conn.h>
```

注销认证信息回调（Authentication Information Callbacks）。

注销回调，停止接收需身份验证的配对信息（Authenticated Pairing Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则返回负错误码。

<a id="ga2987a902da4f5cfe3671c60d154ced7e"></a>

### `bt_conn_auth_keypress_notify()`

```c
int bt_conn_auth_keypress_notify ( struct bt_conn * conn, enum bt_conn_auth_keypress type )
```

```c
#include <zephyr/bluetooth/conn.h>
```

配对期间发送配对口令按键通知（Passkey Keypress Notification）。

只有在 `bt_conn_auth_cb` 结构的 `passkey_entry` 回调被调用后，才能调用此函数。

需要启用 `CONFIG_BT_PASSKEY_KEYPRESS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 通知（Notification）的目的连接，类型为 `BT_CONN_TYPE_LE`。 |
| `type` | 要发送的按键事件类型（Keypress Event Type）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | API 使用不当（Improper Use）。 |
| `-ENOMEM` | 分配失败（Failed to Allocate）。 |
| `-ENOBUFS` | 分配失败（Failed to Allocate）。 |

**参阅（See Also）**：另请参见（See Also）：`bt_conn_auth_keypress`。

**返回（Returns）**：返回值（Returns）：`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga3e15b9deb6787d3e415bbea35c9aa91d"></a>

### `bt_conn_auth_pairing_confirm()`

```c
int bt_conn_auth_pairing_confirm ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

回复使用者是否已确认传入的配对请求（Incoming Pairing）。

只有在 `bt_conn_auth_cb` 结构的 `pairing_confirm` 回调被调用，且用户确认了传入的配对请求后，才应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="gab8c3ecf2a3d68e54379917844a29d995"></a>

### `bt_conn_auth_passkey_confirm()`

```c
int bt_conn_auth_passkey_confirm ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

回复使用者是否已确认配对口令（Passkey）匹配。

只有在 `bt_conn_auth_cb` 结构的 `passkey_confirm` 回调被调用后，才应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="ga3906d8d3d192e8a6ad1bf6b7acc32ff0"></a>

### `bt_conn_auth_passkey_entry()`

```c
int bt_conn_auth_passkey_entry ( struct bt_conn * conn, unsigned int passkey )
```

```c
#include <zephyr/bluetooth/conn.h>
```

使用输入的配对口令（Passkey）回复。

只有在 `bt_conn_auth_cb` 结构的 `passkey_entry` 回调被调用后，才应调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `passkey` | 输入的配对口令（Passkey）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="ga4002a1b092832807218afa8ad279ab98"></a>

### `bt_conn_auth_pincode_entry()`

```c
int bt_conn_auth_pincode_entry ( struct bt_conn * conn, const char * pin )
```

```c
#include <zephyr/bluetooth/conn.h>
```

使用输入的 PIN 码（PIN Code）回复。

只有在 `bt_conn_auth_cb` 结构的 PIN 码回调被调用后，才应调用此函数。该函数用于遗留的蓝牙 2.0 设备（Legacy 2.0 Devices）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `pin` | 输入的 PIN 码（PIN Code）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_BR` 连接。

<a id="gae5073b3666aff788f6f389d010a918a6"></a>

### `bt_conn_br_change_packet_type()`

```c
int bt_conn_br_change_packet_type ( const struct bt_conn * conn, uint16_t packet_type )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更改 BR／EDR 连接数据包类型（Connection Packet Type）。

改变已建立的 BR/EDR ACL 连接可使用的数据包类型（Packet Types）。这样可以动态调整连接支持的用户数据类型，以优化吞吐量（Throughput）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `packet_type` | 原始 HCI BR/EDR ACL `Packet_Type` 字段，由 `BT_HCI_ACL_PKT_TYPE_*` 值组成。对于基本速率数据包类型位，置位表示允许使用该类型。对于 `BT_HCI_ACL_PKT_TYPE_NO_*` 位，置位表示不得使用对应的 EDR 数据包类型，含义遵循蓝牙规范。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败。 |

<a id="ga641f7f4ce7fe0641948a798881ecedcb"></a>

### `bt_conn_br_enter_sniff_mode()`

```c
int bt_conn_br_enter_sniff_mode ( struct bt_conn * conn, uint16_t min_interval, uint16_t max_interval, uint16_t attempt, uint16_t timeout )
```

```c
#include <zephyr/bluetooth/conn.h>
```

检查蓝牙连接并进入嗅探模式（Sniff Mode）。

此函数用于指定要进入嗅探模式（Sniff Mode）的 ACL 链路连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `bt_conn` 类型的 `conn` 连接对象。 |
| `min_interval` | 最小嗅探间隔（Minimum Sniff Interval）。 |
| `max_interval` | 最大嗅探间隔（Maximum Sniff Interval）。 |
| `attempt` | 嗅探尝试（Sniff Attempt）的基带接收时隙数量。 |
| `timeout` | 嗅探超时（Sniff Timeout）的基带接收时隙数量。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_POWER_MODE_CONTROL` 时可用。

<a id="gab1aedad7da2eecc6c30acbfcdf9fbfec"></a>

### `bt_conn_br_exit_sniff_mode()`

```c
int bt_conn_br_exit_sniff_mode ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

检查蓝牙连接并退出嗅探模式（Sniff Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `bt_conn` 类型的 `conn` 连接对象。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_POWER_MODE_CONTROL` 时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，否则为非零值。

<a id="ga76f872637f9b34c701c80d71ce7e585c"></a>

### `bt_conn_br_get_supervision_timeout()`

```c
int bt_conn_br_get_supervision_timeout ( struct bt_conn * conn, uint16_t * timeout )
```

```c
#include <zephyr/bluetooth/conn.h>
```

读取 BR／EDR 监督超时时间（Supervision Timeout）。

读取 BR/EDR 连接当前的链路监督超时（Link Supervision Timeout）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `timeout` | 用于保存监督超时值（Supervision Timeout）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为非零值。

<a id="gab6c2073091d1d08032c51aadb904ea3f"></a>

### `bt_conn_br_set_role_switch_enable()`

```c
int bt_conn_br_set_role_switch_enable ( const struct bt_conn * conn, bool enable )
```

```c
#include <zephyr/bluetooth/conn.h>
```

通过设置连接的链路策略（Link Policy），启用／禁用该连接的角色切换（Role Switch）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `enable` | 启用／禁用控制器角色切换（Role Switch）的值。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-ENOBUFS` 表示 HCI 命令缓冲区不可用；`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_BR` 连接。

<a id="ga910157e30fad972e8c606d1e1645603e"></a>

### `bt_conn_br_set_sniff_subrating()`

```c
int bt_conn_br_set_sniff_subrating ( struct bt_conn * conn, uint16_t max_latency, uint16_t min_remote_timeout, uint16_t min_local_timeout )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置 BR／EDR 嗅探子速率参数（Sniff Subrating Parameters）。

配置 BR/EDR 连接的嗅探子速率（Sniff Subrating）参数。嗅探子速率通过减少设备需要监听的嗅探锚点（Sniff Anchor Points）数量，进一步节省功耗。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `max_latency` | 允许的最大嗅探子速率延迟（Sniff Subrate Latency），单位为 `0.625 ms` 的基带时隙。范围为 `0x0002` 至 `0xFFFE`。 |
| `min_remote_timeout` | 远端设备的最小嗅探模式超时（Sniff Mode Timeout），单位为 `0.625 ms` 的基带时隙。范围为 `0x0000` 至 `0xFFFE`。 |
| `min_local_timeout` | 本地设备的最小嗅探模式超时（Sniff Mode Timeout），单位为 `0.625 ms` 的基带时隙。范围为 `0x0000` 至 `0xFFFE`。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_POWER_MODE_CONTROL` 时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，否则为非零值。

<a id="ga8516a5304ec78362ab66a9f18968d20d"></a>

### `bt_conn_br_set_supervision_timeout()`

```c
int bt_conn_br_set_supervision_timeout ( struct bt_conn * conn, uint16_t timeout )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置 BR／EDR 监督超时时间（Supervision Timeout）。

每条物理链路都有一个用于链路监督（Link Supervision）的定时器。它用于检测由设备移出范围、受到干扰阻断、设备断电或类似故障引起的物理链路丢失。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `timeout` | 链路监督超时（Link Supervision Timeout）。数值范围：`0x0001` 至 `0xFFFF`；时间范围：`0.625 ms` 至 `40.9 s`。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为非零值。

<a id="ga3a7741f1e884168168a09e9ec5f28c49"></a>

### `bt_conn_br_switch_role()`

```c
int bt_conn_br_switch_role ( const struct bt_conn * conn, uint8_t role )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更改 conn 的角色（Role）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `role` | 希望切换到的角色（Role），取值为 `hci_types.h` 中的 `BT_HCI_ROLE_CENTRAL` 或 `BT_HCI_ROLE_PERIPHERAL`。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-ENOBUFS` 表示 HCI 命令缓冲区不可用；`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_BR` 连接。

<a id="gaa9b79cd44734c1e560d6f30509be4d0b"></a>

### `bt_conn_cb_register()`

```c
int bt_conn_cb_register ( struct bt_conn_cb * cb)
```

```c
#include <zephyr/bluetooth/conn.h>
```

注册连接回调（Connection Callbacks）。

注册回调以监视连接状态（Connection State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct），必须指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EEXIST` | `cb` 已注册（Registered）时。 |

<a id="gad2f90b34390e3c3697fd455ae4ef5f31"></a>

### `bt_conn_cb_unregister()`

```c
int bt_conn_cb_unregister ( struct bt_conn_cb * cb)
```

```c
#include <zephyr/bluetooth/conn.h>
```

注销连接回调（Connection Callbacks）。

注销连接状态回调（Connection State Callbacks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调结构体（Callback Struct）指向持续有效的内存。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `cb` 为 `NULL` 时。 |
| `-ENOENT` | `cb` 未注册（Registered）时。 |

<a id="ga62dc2663b4fa39a33adb76dc9a136aa4"></a>

### `bt_conn_create_auto_stop()`

```c
int bt_conn_create_auto_stop ( void )
```

```c
#include <zephyr/bluetooth/conn.h>
```

停止自动创建连接（Automatic Connect Creation）。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaf7849f332386f8903d35d6904f6c82b9"></a>

### `bt_conn_create_br()`

```c
struct bt_conn * bt_conn_create_br ( const bt_addr_t * peer, const struct bt_br_conn_param * param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

发起与远端设备的 BR／EDR 连接（Connection）。

允许使用远端地址，向对端发起新的 BR/EDR 链路（Link）。

调用者获得连接对象（Connection Object）的一个新引用；使用完该对象后，必须通过 bt_conn_unref() 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer` | 远端地址（Remote address）。 |
| `param` | 初始连接参数（Initial Connection Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为有效连接对象，否则为 `NULL`。

<a id="ga14e7c852b0271781594e742ae509c5d3"></a>

### `bt_conn_disconnect()`

```c
int bt_conn_disconnect ( struct bt_conn * conn, uint8_t reason )
```

```c
#include <zephyr/bluetooth/conn.h>
```

断开远端设备或取消待处理连接（Pending Connection）。

使用指定原因码（Reason Code）断开活动连接，或取消待建立的传出连接（Pending Outgoing Connection）。

正常断开连接的原因码应为 `BT_HCI_ERR_REMOTE_USER_TERM_CONN`。

接受以下断开原因（Disconnect Reasons）：

- 身份验证失败：`BT_HCI_ERR_AUTH_FAIL`。
- 远端用户终止连接：`BT_HCI_ERR_REMOTE_USER_TERM_CONN`。
- 远端资源不足：`BT_HCI_ERR_REMOTE_LOW_RESOURCES`。
- 远端关机：`BT_HCI_ERR_REMOTE_POWER_OFF`。
- 不支持的远端特性：`BT_HCI_ERR_UNSUPP_REMOTE_FEATURE`。
- 不支持配对：`BT_HCI_ERR_PAIRING_NOT_SUPPORTED`，仅用于 BR/EDR 连接。
- 不可接受的连接参数：`BT_HCI_ERR_UNACCEPT_CONN_PARAM`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要断开的连接（Connection）。 |
| `reason` | 断开连接的原因码（Reason Code）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaf1aeec9b9893450423cf066a6f471824"></a>

### `bt_conn_drop()`

```c
void bt_conn_drop ( struct bt_conn ** orig)
```

```c
#include <zephyr/bluetooth/conn.h>
```

释放连接引用（Connection Reference）并清空指针。

对 `orig` 执行原子交换（Atomic Exchange），将其设为 `NULL`；如果原值不是 `NULL`，则释放原值的一次引用（Unreference）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `orig` | 指向待丢弃连接指针的指针，不能为空（`NULL`）。返回时，`*orig` 设为 `NULL`。 |

<a id="gaff3e6aa16b68e5da7dab53289295545e"></a>

### `bt_conn_enc_key_size()`

```c
uint8_t bt_conn_enc_key_size ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取加密密钥大小（Encryption Key Size）。

此函数获取加密密钥大小（Encryption Key Size）。如果未启用安全保护，即未启用加密，则返回 `0`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：加密密钥大小；如果 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接，则返回 `0`。

<a id="ga5bdf8e8efc85138d3631dc1efffc3916"></a>

### `bt_conn_foreach()`

```c
void bt_conn_foreach ( enum bt_conn_type type, void(* func )(struct bt_conn *conn, void *data), void * data )
```

```c
#include <zephyr/bluetooth/conn.h>
```

遍历全部 bt_conn 对象。

遍历主机分配器（Host Allocator）中仍然存活的全部 `bt_conn` 对象。

要找到已建立的连接，请结合 `bt_conn_get_info` 使用，并检查 `bt_conn_info::state` 是否为 `BT_CONN_STATE_CONNECTED`。

线程安全性（Thread Safety）：此 API 是线程安全的，但对于本次调用期间分配的对象，不保证提供顺序一致（Sequentially Consistent）的视图。例如，遍历被抢占期间依次分配了 A、B、C，结果可能包含 A 和 C，却遗漏 B。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 连接类型（Connection Type）。 |
| `func` | 针对每个连接调用的函数（Function）。 |
| `data` | 传给回调函数（Callback Function）的数据。 |

<a id="ga77108581b8f61485ca840e4bf7a17087"></a>

### `bt_conn_get_dst()`

```c
const bt_addr_le_t * bt_conn_get_dst ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接的目标，即对端地址（Destination / Peer Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：如果 `conn` 是有效的 `BT_CONN_TYPE_LE` 连接，则返回目的地址。

<a id="ga1b02a1ce8e48ad483d73d1efd803618c"></a>

### `bt_conn_get_dst_br()`

```c
const bt_addr_t * bt_conn_get_dst_br ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接的目标，即对端地址（Destination / Peer Address）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：如果 `conn` 是有效的 `BT_CONN_TYPE_BR` 连接，则返回目的地址。

<a id="ga2de54f2ac83f0d8dca2a85a9fbfadcaa"></a>

### `bt_conn_get_info()`

```c
int bt_conn_get_info ( const struct bt_conn * conn, struct bt_conn_info * info )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接信息（Connection Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `info` | 连接信息对象（Connection Info Object）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gac4e0bd799fc87b65367129685f57c2bd"></a>

### `bt_conn_get_remote_info()`

```c
int bt_conn_get_remote_info ( const struct bt_conn * conn, struct bt_conn_remote_info * remote_info )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取远端设备的连接信息（Connection Info）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `remote_info` | 连接远端信息对象（Remote Info Object）。 |

**说明（Note）**：注意（Note）：要获取远端版本信息，即版本、制造商和子版本，必须启用 `CONFIG_BT_REMOTE_VERSION`。连接建立后立即交换远端信息。应用可通过 `remote_info_available` 回调获知远端信息何时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EBUSY` 表示远端信息尚不可用；`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。

<a id="ga4b43ef0f30146808e560991a302e88ad"></a>

### `bt_conn_get_security()`

```c
bt_security_t bt_conn_get_security ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接的安全等级（Security Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：启用 `CONFIG_BT_SMP` 或 `CONFIG_BT_CLASSIC` 时，返回连接安全级别（Security Level）；否则返回 `BT_SECURITY_L1`。如果 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接，则返回 `BT_SECURITY_L0`。

<a id="gad4aed76b80cc815f748ad0e84ae3d87c"></a>

### `bt_conn_index()`

```c
uint8_t bt_conn_index ( const struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接的数组索引（Array Index）。

此函数用于将 `bt_conn` 映射到连接数组的索引（Index）。该数组有 `CONFIG_BT_MAX_CONN` 个元素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：连接对象的索引，范围为 `0..CONFIG_BT_MAX_CONN-1`。

<a id="gaf3d55f1f8efc630b495389ced3ee3fa5"></a>

### `bt_conn_is_type()`

```c
bool bt_conn_is_type ( const struct bt_conn * conn, enum bt_conn_type type )
```

```c
#include <zephyr/bluetooth/conn.h>
```

确定连接类型（Connection Type）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection object）。 |
| `type` | 要匹配的类型（Types）。可以同时提供多种类型，例如 `BT_CONN_TYPE_LE \| BT_CONN_TYPE_SCO`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | `conn` 的类型为 `type`。 |
| `false` | `conn` 为 `NULL`，或其类型不是 `type`。 |

<a id="ga2e4188482deeda71f8e5d42a07538f31"></a>

### `bt_conn_le_conn_rate_request()`

```c
int bt_conn_le_conn_rate_request ( struct bt_conn * conn, const struct bt_conn_le_conn_rate_param * params )
```

```c
#include <zephyr/bluetooth/conn.h>
```

请求新的连接速率参数（Connection Rate Parameters）。

请求改变连接参数（Connection Parameters），包括子速率参数（Subrate Parameters）。如果支持，可将连接间隔调整到基准连接间隔值（Baseline ConnInterval Values，BCV）以下，并采用更细的粒度。

应已知本地和对端控制器的有效间隔（Valid Intervals），参见 `bt_conn_le_read_min_conn_interval_groups`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `params` | 连接速率参数（Connection Rate Parameters）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_SHORTER_CONNECTION_INTERVALS` 时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gac9b111639f9b982cd97e13f313e51461"></a>

### `bt_conn_le_conn_rate_set_defaults()`

```c
int bt_conn_le_conn_rate_set_defaults ( const struct bt_conn_le_conn_rate_param * params)
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置默认连接速率参数（Connection Rate Parameters）。

配置本设备接受的连接速率值范围（Connection Rate Range）；该范围用于外围设备（Peripheral）发起连接速率更新过程时。

配置的界限（Configured Bounds）：

- 仅适用于本次调用之后建立的连接（Connections）。
- 对于指定连接，其界限会被该连接上的任何 `bt_conn_le_conn_rate_request` 调用覆盖（Override）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 连接速率参数（Connection Rate Parameters）。 |

**注意（Attention）**：注意（Attention）：仅在同时启用 Kconfig 选项 `CONFIG_BT_SHORTER_CONNECTION_INTERVALS` 和 `CONFIG_BT_CENTRAL` 时可用。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga8d66f3e0262a51279e9fa8b3139252e6"></a>

### `bt_conn_le_create()`

```c
int bt_conn_le_create ( const bt_addr_le_t * peer, const struct bt_conn_le_create_param * create_param, const struct bt_le_conn_param * conn_param, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/conn.h>
```

发起与远端设备的低功耗蓝牙连接（LE Connection）。

允许使用远端地址，向对端发起新的低功耗链路（LE Link）。

调用方获得连接对象的一个新引用（Reference），使用完毕后必须通过 `bt_conn_unref()` 释放。如果启用 `CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE`，且解引用后的 `conn` 非 `NULL`，此函数返回 `-EINVAL`。

使用通用连接建立过程（General Connection Establishment Procedure）。

如果未启用 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`，应用必须先禁用显式扫描（Explicit Scanning），再发起新的低功耗连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] peer` | 远端地址（Remote address）。 |
| `[in] create_param` | 创建连接参数（Create Connection Parameters）。 |
| `[in] conn_param` | 初始连接参数（Initial Connection Parameters）。 |
| `[out] conn` | 成功时为有效连接对象（Connection Object）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="gaecfaf2cb44772511dbb585de8f76f09b"></a>

### `bt_conn_le_create_auto()`

```c
int bt_conn_le_create_auto ( const struct bt_conn_le_create_param * create_param, const struct bt_le_conn_param * conn_param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

自动连接过滤接受列表（Filter Accept List）中的远端设备。

使用自动连接建立过程（Auto Connection Establishment Procedure）。该过程持续到建立一个连接，或通过 `bt_conn_create_auto_stop` 停止。要连接过滤器接受列表（Filter Accept List）中的全部设备，应在新连接建立后的 `connected` 回调中再次启动该过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `create_param` | 创建连接参数（Create Connection Parameters）。 |
| `conn_param` | 初始连接参数（Initial Connection Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-ENOMEM` 表示没有可用的空闲连接对象。

<a id="ga98f99c893e444d1ad1ecd9139803c0b1"></a>

### `bt_conn_le_create_synced()`

```c
int bt_conn_le_create_synced ( const struct bt_le_ext_adv * adv, const struct bt_conn_le_create_synced_param * synced_param, const struct bt_le_conn_param * conn_param, struct bt_conn ** conn )
```

```c
#include <zephyr/bluetooth/conn.h>
```

创建与已同步设备（Synced Device）的连接。

从带响应的周期广播序列（Periodic Advertising with Responses，PAwR Train）向已同步设备发起连接。

调用方获得连接对象的一个新引用（Reference），使用完毕后必须通过 `bt_conn_unref()` 释放。如果启用 `CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE`，且解引用后的 `conn` 非 `NULL`，此函数返回 `-EINVAL`。

使用周期广播连接过程（Periodic Advertising Connection Procedure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] adv` | PAwR 广播方所属的广播集（Advertising Set）。 |
| `[in] synced_param` | 创建连接参数（Create Connection Parameters）。 |
| `[in] conn_param` | 初始连接参数（Initial Connection Parameters）。 |
| `[out] conn` | 成功时为有效连接对象（Connection Object）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga8a2006f6e34b20c7e8ef65a73f431a57"></a>

### `bt_conn_le_data_len_update()`

```c
int bt_conn_le_data_len_update ( struct bt_conn * conn, const struct bt_conn_le_data_len_param * param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更新连接发送数据长度参数（Transmit Data Length Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `param` | 更新后的数据长度参数（Data Length Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gaa79eada87d698f4998af876d03d7e92b"></a>

### `bt_conn_le_enhanced_get_tx_power_level()`

```c
int bt_conn_le_enhanced_get_tx_power_level ( struct bt_conn * conn, struct bt_conn_le_tx_power * tx_power )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取本地增强连接发射功率等级（Enhanced Connection Transmit Power Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `tx_power` | 发送功率级别描述符（Transmit Power Level Descriptor）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOBUFS` | HCI 命令缓冲区（Command Buffer）不可用。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

**返回（Returns）**：返回值（Returns）：`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gab734fbc307eff3c5bddf7c5e6ddd341b"></a>

### `bt_conn_le_frame_space_update()`

```c
int bt_conn_le_frame_space_update ( struct bt_conn * conn, const struct bt_conn_le_frame_space_update_param * params )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更新帧间隔（Frame Space）。

请求修改连接的帧间隔参数（Frame Space Parameters）。过程完成后，此函数触发 `frame_space_updated` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `params` | 帧间隔更新参数（Frame Space Update Parameters）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_FRAME_SPACE_UPDATE` 时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga0843a2e0b6f16ebd132a3a512cfd27a4"></a>

### `bt_conn_le_get_remote_tx_power_level()`

```c
int bt_conn_le_get_remote_tx_power_level ( struct bt_conn * conn, enum bt_conn_le_tx_power_phy phy )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取远端，即对端发射功率等级（Peer Transmit Power Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `phy` | 物理层信息（PHY Information）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOBUFS` | HCI 命令缓冲区（Command Buffer）不可用。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

**返回（Returns）**：返回值（Returns）：`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gaa5289154bc508444f68df7abcef18aca"></a>

### `bt_conn_le_get_tx_power_level()`

```c
int bt_conn_le_get_tx_power_level ( struct bt_conn * conn, struct bt_conn_le_tx_power * tx_power_level )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取连接发射功率等级（Transmit Power Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `tx_power_level` | 发送功率级别描述符（Transmit Power Level Descriptor）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-ENOBUFS` 表示 HCI 命令缓冲区不可用；`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gab44a964725f54ed2d37de17c6e2fd3eb"></a>

### `bt_conn_le_param_update()`

```c
int bt_conn_le_param_update ( struct bt_conn * conn, const struct bt_le_conn_param * param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更新连接参数（Connection Parameters）。

如果本地设备处于外围设备角色（Peripheral Role），则会延迟更新连接参数。该延迟可以通过 `CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT` 配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `param` | 更新后的连接参数（Connection Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gae13ed81b1e7928f44b8fdf85995b3e58"></a>

### `bt_conn_le_phy_update()`

```c
int bt_conn_le_phy_update ( struct bt_conn * conn, const struct bt_conn_le_phy_param * param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更新连接物理层参数（PHY Parameters）。

更新连接首选的发送和接收物理层（PHY）。使用 `BT_GAP_LE_PHY_NONE` 表示无偏好。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `param` | 更新后的连接参数（Connection Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gac0dbbdb95ef868f35006622932dc8901"></a>

### `bt_conn_le_read_all_remote_features()`

```c
int bt_conn_le_read_all_remote_features ( struct bt_conn * conn, uint8_t pages_requested )
```

```c
#include <zephyr/bluetooth/conn.h>
```

读取远端特性页（Remote Feature Pages）。

请求远端特性页（Remote Feature Pages），从第 `0` 页开始，数量以 `pages_requested` 或对端支持的页数为限，最多 `10` 页。过程完成后，此函数触发 `read_all_remote_feat_complete` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `pages_requested` | 要向对端请求的特性页数量（Number of Feature Pages），最多 `10` 页。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_LE_EXTENDED_FEAT_SET` 时可用。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga9af26600acdf5b3a8b8ea0a32e14b497"></a>

### `bt_conn_le_read_min_conn_interval()`

```c
int bt_conn_le_read_min_conn_interval ( uint16_t * min_interval_us)
```

```c
#include <zephyr/bluetooth/conn.h>
```

读取支持的最小连接间隔（Minimum Supported Connection Interval）。

从本地控制器读取其支持的最小连接间隔（Minimum Connection Interval）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `min_interval_us` | 指向变量的指针，用于接收最小连接间隔，单位为微秒（Microseconds）。 |

**参阅（See Also）**：另请参见（See Also）：若需要间隔组信息，使用 `bt_conn_le_read_min_conn_interval_groups`。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_SHORTER_CONNECTION_INTERVALS` 时可用。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga2e7e836d94a5330ae01e14dbd3e29f14"></a>

### `bt_conn_le_read_min_conn_interval_groups()`

```c
int bt_conn_le_read_min_conn_interval_groups ( struct bt_conn_le_min_conn_interval_info * info)
```

```c
#include <zephyr/bluetooth/conn.h>
```

读取支持的最小连接间隔组（Minimum Supported Connection Interval Groups）。

从本地控制器读取最小受支持连接间隔（Minimum Supported Connection Interval）及受支持的间隔组（Interval Groups）。这些信息描述本地控制器的能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 指向结构的指针，用于接收最小连接间隔信息（Minimum Connection Interval Information）。 |

**参阅（See Also）**：另请参见（See Also）：如果只需要 `bt_conn_le_min_conn_interval_info::min_supported_conn_interval_us`，使用 `bt_conn_le_read_min_conn_interval`。

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_SHORTER_CONNECTION_INTERVALS` 时可用。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga7c8e7a7616e7b56f97da7ff4bc0fc7ba"></a>

### `bt_conn_le_set_default_phy()`

```c
int bt_conn_le_set_default_phy ( uint8_t pref_tx_phy, uint8_t pref_rx_phy )
```

```c
#include <zephyr/bluetooth/conn.h>
```

更新默认物理层参数（PHY Parameters），用于此后经低功耗蓝牙传输（LE Transport）建立的全部连接。

更新低功耗传输（LE Transport）首选的发送和接收物理层（PHY）。使用 `BT_GAP_LE_PHY_NONE` 表示无偏好。可选 PHY 值参见 `bt_gap_le_phy`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pref_tx_phy` | 首选发送物理层参数（Transmitter PHY Parameters）。 |
| `pref_rx_phy` | 首选接收物理层参数（Receiver PHY Parameters）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga90ae27bcc6f71f32be56efe8ecbc165d"></a>

### `bt_conn_le_set_path_loss_mon_enable()`

```c
int bt_conn_le_set_path_loss_mon_enable ( struct bt_conn * conn, bool enable )
```

```c
#include <zephyr/bluetooth/conn.h>
```

启用或禁用路径损耗监测（Path Loss Monitoring）。

启用或禁用路径损耗监测（Path Loss Monitoring），以决定控制器是否向主机发送路径损耗阈值事件（Path Loss Threshold Events）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `enable` | 启用／禁用路径损耗报告（Path Loss Reporting）。 |

**说明（Note）**：注意（Note）：使用此 API 必须设置 `CONFIG_BT_PATH_LOSS_MONITORING`。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga6be5f3bf064ba03dc2307fdd2b634637"></a>

### `bt_conn_le_set_path_loss_mon_param()`

```c
int bt_conn_le_set_path_loss_mon_param ( struct bt_conn * conn, const struct bt_conn_le_path_loss_reporting_param * param )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置路径损耗监测参数（Path Loss Monitoring Parameters）。

修改给定 `conn` 句柄的路径损耗阈值变更事件（Path Loss Threshold Change Events）配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `param` | 路径损耗监测参数（Path Loss Monitoring Parameters）。 |

**说明（Note）**：注意（Note）：使用此 API 必须设置 `CONFIG_BT_PATH_LOSS_MONITORING`。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gaa1f38911acee0534a8a6e414018c6fb6"></a>

### `bt_conn_le_set_tx_power_report_enable()`

```c
int bt_conn_le_set_tx_power_report_enable ( struct bt_conn * conn, bool local_enable, bool remote_enable )
```

```c
#include <zephyr/bluetooth/conn.h>
```

启用发射功率报告（Transmit Power Reporting）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `local_enable` | 启用／禁用本地报告（Local Reporting）。 |
| `remote_enable` | 启用／禁用远端报告（Remote Reporting）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOBUFS` | HCI 命令缓冲区（Command Buffer）不可用。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

**返回（Returns）**：返回值（Returns）：`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga754ed218fe9577f2d0ef6d508cfc5a0b"></a>

### `bt_conn_le_subrate_request()`

```c
int bt_conn_le_subrate_request ( struct bt_conn * conn, const struct bt_conn_le_subrate_param * params )
```

```c
#include <zephyr/bluetooth/conn.h>
```

请求新的子速率参数（Subrating Parameters）。

请求修改连接的子速率参数（Subrating Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `params` | 子速率参数（Subrating Parameters）。 |

**说明（Note）**：注意（Note）：使用此 API 必须设置 `CONFIG_BT_SUBRATING`。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gac7bb456c530c7e08b4fa9f4d478fdaf9"></a>

### `bt_conn_le_subrate_set_defaults()`

```c
int bt_conn_le_subrate_set_defaults ( const struct bt_conn_le_subrate_param * params)
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置默认连接子速率参数（Connection Subrating Parameters）。

修改未来全部 ACL 连接的默认子速率参数（Default Subrating Parameters），适用于本地设备作为中心设备（Central）的连接。此命令不影响现有连接。为具体连接设置的参数始终优先。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `params` | 子速率参数（Subrating Parameters）。 |

**说明（Note）**：注意（Note）：使用此 API 必须设置 `CONFIG_BT_SUBRATING` 和 `CONFIG_BT_CENTRAL`。

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ga11ae1b656683cebe9db6a53e5166ad7a"></a>

### `bt_conn_lookup_addr_br()`

```c
struct bt_conn * bt_conn_lookup_addr_br ( const bt_addr_t * peer)
```

```c
#include <zephyr/bluetooth/conn.h>
```

根据地址查找现有基本速率连接（BR Connection）。

根据远端地址查找现有基本速率连接（BR Connection）。

调用者获得连接对象（Connection Object）的一个新引用；使用完该对象后，必须通过 bt_conn_unref() 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer` | 远端地址（Remote address）。 |

**返回（Returns）**：返回值（Returns）：连接对象；未找到时为 `NULL`。

<a id="ga1bfe349efd8a7de31e9457fe439d746a"></a>

### `bt_conn_lookup_addr_le()`

```c
struct bt_conn * bt_conn_lookup_addr_le ( uint8_t id, const bt_addr_le_t * peer )
```

```c
#include <zephyr/bluetooth/conn.h>
```

根据地址查找现有连接（Connection）。

根据远端地址（Remote Address）查找现有连接。

调用者获得连接对象（Connection Object）的一个新引用；使用完该对象后，必须通过 bt_conn_unref() 释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 本地身份（Local Identity），多数情况下为 `BT_ID_DEFAULT`。 |
| `peer` | 远端地址（Remote address）。 |

**返回（Returns）**：返回值（Returns）：连接对象；未找到时为 `NULL`。

<a id="ga060d51eb2208de6f805b1fc0672d2d0c"></a>

### `bt_conn_ref()`

```c
struct bt_conn * bt_conn_ref ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

增加连接的引用计数（Reference Count）。

增加连接对象的引用计数（Reference Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**说明（Note）**：注意（Note）：引用计数为零时返回 `NULL`。

**返回（Returns）**：返回值（Returns）：引用计数已增加的连接对象；引用计数为零时为 `NULL`。

<a id="ga4165819d12dd96e00dfa2fd6f4b95669"></a>

### `bt_conn_set_bondable()`

```c
int bt_conn_set_bondable ( struct bt_conn * conn, bool enable )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置／清除给定连接的绑定标志（Bonding Flag）。

为给定连接，设置／清除 SMP 配对请求／响应数据中身份验证要求（Authentication Requirements）的绑定标志（Bonding Flag）。

如果 SMP 模块中的安全过程已经开始，则不能设置／清除给定连接的绑定标志（Bonding Flag）。每个连接只能调用此函数一次。

如果未为给定连接设置／清除绑定标志（Bonding Flag），其值取决于通过 `bt_set_bondable` 设置的全局配置。全局配置的默认值由 Kconfig 选项 `CONFIG_BT_BONDABLE` 定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `enable` | 允许／禁止绑定（Bondable）的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EALREADY` | 已处于请求的状态（Requested State）。 |

**返回（Returns）**：返回值（Returns）：`conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接时，返回 `-EINVAL`；`conn` 是有效 LE 连接但无法获取 SMP 上下文时，也返回 `-EINVAL`。

<a id="gae001f1268e1ff42c3c974c95dcb6735d"></a>

### `bt_conn_set_security()`

```c
int bt_conn_set_security ( struct bt_conn * conn, bt_security_t sec )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置连接的安全等级（Security Level）。

此函数为连接启用安全保护，即加密（Encryption）。如果设备保存了对端的绑定信息（Bond Information），且密钥强度足够，就启用加密。如果连接已使用足够强的密钥加密，则此函数不执行任何操作。

如果设备没有对端的绑定信息（Bond Information），且尚未配对，则发起配对过程（Pairing Procedure）。注意，`sec` 不影响配对过程选择的安全级别；该选择由已注册的 `bt_conn_auth_cb` 中的值控制。如果设备已有绑定信息或已经配对，但密钥过弱，也会发起配对过程。

如果由于本地或远端设备限制，例如输入／输出能力（I/O Capabilities），无法达到 `sec` 所定义的所需安全级别，或已达到已配对设备数量上限，此函数可能返回错误。

如果本地或对端设备已经发起配对过程（Pairing Procedure），此函数可能返回错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接对象（Connection Object）。 |
| `sec` | 请求的最低安全级别（Minimum Security Level）。 |

**说明（Note）**：注意（Note）：启用 `CONFIG_BT_SMP_SC_ONLY` 时，安全级别始终为 `4`；启用 `CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY` 时，安全级别始终为 `3`。如果 `sec` 中启用了 `BT_SECURITY_FORCE_PAIR`，则始终发起配对过程。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 连接。`-EALREADY` 表示已有安全请求（Security Request）正在处理中，即外围设备发送的请求尚未得到响应；原请求保持不变，它携带的安全级别也不会改变。

<a id="gaf073384538a67c242b00150904176f66"></a>

### `bt_conn_take()`

```c
struct bt_conn * bt_conn_take ( struct bt_conn ** orig)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/conn.h>
```

接管连接指针的所有权（Ownership），将原指针设为 NULL。

对 `orig` 执行原子交换（Atomic Exchange），将其设为 `NULL` 并返回原值。不修改引用计数；`orig` 持有的引用转移给调用方，调用方最终必须通过 `bt_conn_unref()` 释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `orig` | 指向待转移连接指针的指针，不能为空（`NULL`）。返回时，`*orig` 设为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：`orig` 原来指向的连接，可能为 `NULL`。

<a id="ga4b18c6b22a9f02be0d7d078b2ce51ff6"></a>

### `bt_conn_unref()`

```c
void bt_conn_unref ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/conn.h>
```

减少连接的引用计数（Reference Count）。

减少连接对象的引用计数（Reference Count）。除非该指针变量即将离开作用域，否则建议改用 `bt_conn_drop`；它还会将指针设为 `NULL`，防止意外复用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

<a id="ga0c84d5597a71fe38788a88063fd19a2d"></a>

### `bt_get_bondable()`

```c
bool bt_get_bondable ( void )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取绑定标志（Bonding Flag）。

获取当前绑定标志（Bonding Flag）。该标志初始值取决于 Kconfig 选项 `CONFIG_BT_BONDABLE`，可通过 `bt_set_bondable()` 更新。

**返回（Returns）**：返回值（Returns）：当前绑定标志（Bonding Flag）。

<a id="ga096552403b5bcd0107f69eded772b1ee"></a>

### `bt_le_oob_get_sc_data()`

```c
int bt_le_oob_get_sc_data ( struct bt_conn * conn, const struct bt_le_oob_sc_data ** oobd_local, const struct bt_le_oob_sc_data ** oobd_remote )
```

```c
#include <zephyr/bluetooth/conn.h>
```

获取低功耗安全连接（LE Secure Connections，SC）配对过程使用的带外数据（OOB Data）。

此函数允许在低功耗安全连接配对过程（LE SC Pairing Procedure）期间，获取通过 `bt_le_oob_set_sc_data()` API 设置的带外数据（OOB Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `oobd_local` | 本地带外数据（Local OOB Data）；未设置时为 `NULL`。 |
| `oobd_remote` | 远端带外数据（Remote OOB Data）；未设置时为 `NULL`。 |

**说明（Note）**：注意（Note）：仅在关联的连接对象保持有效期间，带外数据（OOB Data）才可用。

**返回（Returns）**：返回值（Returns）：成功时为零，否则为错误码。协议错误（Protocol Error）为正值，协议栈内部错误为负 POSIX 错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="ga978770d46d7c8af854a61261c14cb892"></a>

### `bt_le_oob_set_legacy_flag()`

```c
void bt_le_oob_set_legacy_flag ( bool enable)
```

```c
#include <zephyr/bluetooth/conn.h>
```

允许／禁止使用远端传统带外数据（Legacy OOB Data）进行配对。

设置／清除遗留 SMP 配对请求／响应数据中的带外数据标志（OOB Data Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 允许／禁止使用远端遗留带外数据（Legacy OOB Data）的值。 |

<a id="ga0f889983cfabafe826b4feb6899b95ba"></a>

### `bt_le_oob_set_legacy_tk()`

```c
int bt_le_oob_set_legacy_tk ( struct bt_conn * conn, const uint8_t * tk )
```

```c
#include <zephyr/bluetooth/conn.h>
```

设置用于配对的带外临时密钥（OOB Temporary Key）。

此函数用于为低功耗遗留配对过程（LE Legacy Pairing Procedure）设置带外数据（OOB Data）。仅当配对采用遗留方法时，才应响应 `oob_data_request()` 回调调用本函数。译注：原文“legacy method is user pairing”存在语病，此处按上下文译为配对使用遗留方法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `tk` | 指向 16 字节临时密钥（TK）数组的指针。每次新的配对过程都应随机生成 TK 值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |

**返回（Returns）**：返回值（Returns）：`conn` 不是有效的 `BT_CONN_TYPE_LE` 连接时返回 `-EINVAL`；`tk` 为 `NULL` 时也返回 `-EINVAL`。

<a id="gac365f9748ad0737f09142ee1de982503"></a>

### `bt_le_oob_set_sc_data()`

```c
int bt_le_oob_set_sc_data ( struct bt_conn * conn, const struct bt_le_oob_sc_data * oobd_local, const struct bt_le_oob_sc_data * oobd_remote )
```

```c
#include <zephyr/bluetooth/conn.h>
```

在低功耗安全连接（LE Secure Connections，SC）配对过程中设置带外数据（OOB Data）。

此函数用于在低功耗安全连接配对过程（LE SC Pairing Procedure）期间设置带外数据（OOB Data）。仅在使用 LE SC 方法配对时，才应响应 `oob_data_request()` 回调调用本函数。

用户应根据回调中收到的信息提交带外数据（OOB Data）。可能有三种配置：仅有本地数据、仅有远端数据，或本地与远端数据都有。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | `BT_CONN_TYPE_LE` 连接对象（Connection Object）。 |
| `oobd_local` | 本地带外数据（Local OOB Data）；不存在时为 `NULL`。 |
| `oobd_remote` | 远端带外数据（Remote OOB Data）；不存在时为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为零，否则为错误码。协议错误（Protocol Error）为正值，协议栈内部错误为负 POSIX 错误码。`-EINVAL` 表示 `conn` 不是有效的 `BT_CONN_TYPE_LE` 连接。

<a id="gad02f8fe587efd543c0c81cace3f63d63"></a>

### `bt_le_oob_set_sc_flag()`

```c
void bt_le_oob_set_sc_flag ( bool enable)
```

```c
#include <zephyr/bluetooth/conn.h>
```

允许／禁止使用远端低功耗安全连接带外数据（LE SC OOB Data）进行配对。

设置／清除 LE SC SMP 配对请求／响应数据中的带外数据标志（OOB Data Flag）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 允许／禁止使用远端 LE SC 带外数据（OOB Data）的值。 |

<a id="ga327444a6987b8e0b573fe758d2f75886"></a>

### `bt_security_err_to_str()`

```c
const char * bt_security_err_to_str ( enum bt_security_err err)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/conn.h>
```

将安全错误（Security Error）转换为字符串。

**返回（Returns）**：返回值（Returns）：安全错误码的字符串表示。如果未启用 `CONFIG_BT_SECURITY_ERR_TO_STR`，则只返回空字符串。

<a id="ga014db594b17a3b5d7d954e64ad8de759"></a>

### `bt_set_bondable()`

```c
void bt_set_bondable ( bool enable)
```

```c
#include <zephyr/bluetooth/conn.h>
```

启用／禁用绑定（Bonding）。

设置／清除 SMP 配对请求／响应数据中身份验证要求（Authentication Requirements）的绑定标志（Bonding Flag）。初始值取决于 `BT_BONDABLE` Kconfig 设置。绝大多数应用不必调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 允许／禁止绑定（Bondable）的值。 |


## 1.6\_原页交叉引用（Cross References）

- [bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)
- [bt_conn_le_phy_info](../bluetooth_connection_model_reference/P028_bt_conn_le_phy_info_结构体.md)
- [bt_conn_le_phy_param](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md)
- [bt_conn_le_data_len_info](../bluetooth_connection_model_reference/P019_bt_conn_le_data_len_info_结构体.md)
- [bt_conn_le_data_len_param](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md)
- [bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)
- [bt_conn_le_subrating_info](../bluetooth_connection_model_reference/P034_bt_conn_le_subrating_info_结构体.md)
- [bt_conn_le_subrate_changed](../bluetooth_connection_model_reference/P032_bt_conn_le_subrate_changed_结构体.md)
- [bt_conn_le_min_conn_interval_group](../bluetooth_connection_model_reference/P024_bt_conn_le_min_conn_interval_group_结构体.md)
- [bt_conn_le_min_conn_interval_info](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md)
- [bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)
- [bt_conn_le_conn_rate_changed](../bluetooth_connection_model_reference/P010_bt_conn_le_conn_rate_changed_结构体.md)
- [bt_conn_le_read_all_remote_feat_complete](../bluetooth_connection_model_reference/P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)
- [bt_conn_le_frame_space_update_param](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md)
- [bt_conn_le_frame_space_updated](../bluetooth_connection_model_reference/P022_bt_conn_le_frame_space_updated_结构体.md)
- [bt_conn_le_cs_capabilities](../bluetooth_connection_model_reference/P014_bt_conn_le_cs_capabilities_结构体.md)
- [bt_conn_le_cs_fae_table](../bluetooth_connection_model_reference/P016_bt_conn_le_cs_fae_table_结构体.md)
- [bt_conn_le_cs_config](../bluetooth_connection_model_reference/P015_bt_conn_le_cs_config_结构体.md)
- [bt_conn_le_cs_subevent_result](../bluetooth_connection_model_reference/P018_bt_conn_le_cs_subevent_result_结构体.md)
- [bt_conn_le_info](../bluetooth_connection_model_reference/P023_bt_conn_le_info_结构体.md)
- [bt_conn_br_info](../bluetooth_connection_model_reference/P006_bt_conn_br_info_结构体.md)
- [bt_conn_sco_info](../bluetooth_connection_model_reference/P040_bt_conn_sco_info_结构体.md)
- [bt_security_info](../bluetooth_connection_model_reference/P130_bt_security_info_结构体.md)
- [bt_conn_info](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md)
- [bt_conn_le_remote_info](../bluetooth_connection_model_reference/P031_bt_conn_le_remote_info_结构体.md)
- [bt_conn_br_remote_info](../bluetooth_connection_model_reference/P007_bt_conn_br_remote_info_结构体.md)
- [bt_conn_remote_info](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md)
- [bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)
- [bt_conn_le_tx_power_report](../bluetooth_connection_model_reference/P036_bt_conn_le_tx_power_report_结构体.md)
- [bt_conn_le_path_loss_threshold_report](../bluetooth_connection_model_reference/P027_bt_conn_le_path_loss_threshold_report_结构体.md)
- [bt_conn_le_path_loss_reporting_param](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md)
- [bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)
- [bt_conn_le_create_synced_param](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md)
- [bt_conn_le_cs_procedure_enable_complete](../bluetooth_connection_model_reference/P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)
- [bt_conn_br_cb](../bluetooth_connection_model_reference/P005_bt_conn_br_cb_结构体.md)
- [bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)
- [bt_conn_oob_info](../bluetooth_connection_model_reference/P037_bt_conn_oob_info_结构体.md)
- [bt_conn_pairing_feat](../bluetooth_connection_model_reference/P038_bt_conn_pairing_feat_结构体.md)
- [bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)
- [bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)
- [bt_br_conn_param](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [zephyr/bluetooth/conn.h](../api_file_kernel_network_reference/P003_zephyr__bluetooth__conn.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [BT_GAP_SCAN_FAST_INTERVAL](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga747caa714962215453a966a323e77cf8)
- [BT_GAP_SCAN_FAST_WINDOW](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga100e1c20813630848a1a80390e8a06a0)
- [BT_HCI_OP_LE_CS_MAIN_MODE_1](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#af1b7924e50ba017e59d697fd8814d491)
- [BT_HCI_OP_LE_CS_MAIN_MODE_2](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a714152a085bbc317b539d6e973ccffc6)
- [BT_HCI_OP_LE_CS_MAIN_MODE_3](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a5d2af0ed5e0cc5cf7d9f0baae512ff68)
- [BT_HCI_OP_LE_CS_SUB_MODE_UNUSED](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#ab3fce1eb448b0ade581e4e12b2d56039)
- [BT_HCI_OP_LE_CS_SUB_MODE_1](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a219243d501bbcb6d62668398cde79fca)
- [BT_HCI_OP_LE_CS_SUB_MODE_2](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#ada09c787fca0a1d54bb754635489b51e)
- [BT_HCI_OP_LE_CS_SUB_MODE_3](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a4b48c199b6b75e9dd62ec36883b40aa4)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a1ff1899e87988795cb56cf3ac69fc661)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#ac390cbfa78d9027cbb6b9cda5e11c9c6)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#af7216a6ef4ccc35e081d7b18513af2d2)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a7f490f8f8ac13199da1c2af10adea5de)
- [BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a1e3128522364b82dc7a3ba05f89b96fc)
- [BT_GAP_LE_PHY_1M](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752)
- [BT_GAP_LE_PHY_2M](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8)
- [BT_GAP_LE_PHY_CODED](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3)
- [bt_conn_cb::le_param_update_rejected](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md#a2179943b5f64302e38c64f075a5b6a9e)
- [BT_HCI_LE_SCI_INTERVAL_UNIT_US](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a47b99bb33143c6a936af1462ce791313)
- [BT_GAP_INIT_CONN_INT_MIN](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gadaa7f1547c4ea22936087c181d82a552)
- [BT_GAP_INIT_CONN_INT_MAX](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1)
- [BT_GAP_MS_TO_CONN_TIMEOUT](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga24f79cacceeea262987f3cdaf2ef6bc3)
- [BT_GAP_DATA_LEN_DEFAULT](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga90cfab7c375a8af6f9224a5635cbd023)
- [BT_GAP_DATA_TIME_DEFAULT](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga245249c0b6f8ccc419f2132f76362908)
- [BT_GAP_DATA_LEN_MAX](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gacf5f35866d4677bd45c6e567886cabb9)
- [BT_GAP_DATA_TIME_MAX](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga379b5d8d7f243abbc584c288cd01815f)
- [CONFIG_BT_SMP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)
- [CONFIG_BT_PASSKEY_KEYPRESS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PASSKEY_KEYPRESS)
- [CONFIG_BT_POWER_MODE_CONTROL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_POWER_MODE_CONTROL)
- [BT_HCI_ROLE_CENTRAL](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a150ea8f2095d8510bde3ebd65d521c29)
- [BT_HCI_ROLE_PERIPHERAL](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a9ca37afd4638ef94cdd55302bd4c99b3)
- [hci_types.h](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md)
- [远端用户终止连接：`BT_HCI_ERR_REMOTE_USER_TERM_CONN`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#ac0e3b44027180d7a2dedb59395c4b111)
- [身份验证失败：`BT_HCI_ERR_AUTH_FAIL`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a070d51dd0de3288f9811f90a558c889b)
- [远端资源不足：`BT_HCI_ERR_REMOTE_LOW_RESOURCES`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a5eeadfb220c24b2e7f5ce3fd21e5d46a)
- [远端关机：`BT_HCI_ERR_REMOTE_POWER_OFF`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a083f1fc52300f7e47c2f8d4e50551851)
- [不支持的远端特性：`BT_HCI_ERR_UNSUPP_REMOTE_FEATURE`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a516751f02bd497a020783f69bcf71453)
- [BT_HCI_ERR_PAIRING_NOT_SUPPORTED](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a059c7d5619823eddf2c541b40a6464cb)
- [不可接受的连接参数：`BT_HCI_ERR_UNACCEPT_CONN_PARAM`。](../api_file_mesh_acpi_reference/P005_zephyr__bluetooth__hci_types.h_文件参考.md#a712e214942c0d151597ce04e9d0df453)
- [bt_conn_info::state](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md#ae566e2382b69ff27314dc1dd632dbdbc)
- [CONFIG_BT_REMOTE_VERSION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_REMOTE_VERSION)
- [CONFIG_BT_CLASSIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [CONFIG_BT_SHORTER_CONNECTION_INTERVALS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SHORTER_CONNECTION_INTERVALS)
- [CONFIG_BT_CENTRAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CENTRAL)
- [CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN_CHECK_NULL_BEFORE_CREATE)
- [CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)
- [CONFIG_BT_FRAME_SPACE_UPDATE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_FRAME_SPACE_UPDATE)
- [CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN_PARAM_UPDATE_TIMEOUT)
- [BT_GAP_LE_PHY_NONE](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#gga691d9793fd21c41b2c192d65cc2bf6c4aaf7e1b40f6464a603e5116db269cacab)
- [CONFIG_BT_LE_EXTENDED_FEAT_SET](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LE_EXTENDED_FEAT_SET)
- [bt_conn_le_min_conn_interval_info::min_supported_conn_interval_us](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md#aa39299ca32657e9f684e88875e7517dc)
- [bt_gap_le_phy](../api_media_cellular_topic_reference/P002_定义与分配编号（Defines and Assigned Numbers）.md#ga691d9793fd21c41b2c192d65cc2bf6c4)
- [CONFIG_BT_PATH_LOSS_MONITORING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PATH_LOSS_MONITORING)
- [CONFIG_BT_SUBRATING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SUBRATING)
- [CONFIG_BT_SMP_SC_ONLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_SC_ONLY)
- [CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_OOB_LEGACY_PAIR_ONLY)
- [CONFIG_BT_BONDABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BONDABLE)
- [CONFIG_BT_SECURITY_ERR_TO_STR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SECURITY_ERR_TO_STR)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructbt__br__conn__param_html"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructbt__conn__cb_html"></a>
<a id="agroup__bt__conn_html_gae86425d432078e2ddca260eebc2802f1"></a>
<a id="agroup__bt__conn_html_gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9"></a>
<a id="agroup__bt__gap__defines_html_ga747caa714962215453a966a323e77cf8"></a>
<a id="agroup__bt__gap__defines_html_ga100e1c20813630848a1a80390e8a06a0"></a>
<a id="astructbt__conn__le__create__param_html"></a>
<a id="astructbt__conn__le__data__len__param_html"></a>
<a id="ahci__types_8h_html_a1ff1899e87988795cb56cf3ac69fc661"></a>
<a id="ahci__types_8h_html_ac390cbfa78d9027cbb6b9cda5e11c9c6"></a>
<a id="ahci__types_8h_html_af7216a6ef4ccc35e081d7b18513af2d2"></a>
<a id="ahci__types_8h_html_a1e3128522364b82dc7a3ba05f89b96fc"></a>
<a id="ahci__types_8h_html_a7f490f8f8ac13199da1c2af10adea5de"></a>
<a id="astructbt__conn__le__phy__param_html"></a>
<a id="agroup__bt__conn_html_ga39b69f0978f74b5f13f829e908b7cebb"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a53eff400720a20fe1a91da4834bad752"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a662049cc8293959194bcb481e1dd50a8"></a>
<a id="agroup__bt__gap__defines_html_gga691d9793fd21c41b2c192d65cc2bf6c4a97d042e48448fdf6a9e35e5d38cb14c3"></a>
<a id="agroup__bt__conn_html_gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98"></a>
<a id="ahci__types_8h_html_a47b99bb33143c6a936af1462ce791313"></a>
<a id="astructbt__le__conn__param_html"></a>
<a id="agroup__bt__conn_html_ga940d55c0d84c0cb8f09bc41074ae50d0"></a>
<a id="agroup__bt__gap__defines_html_ga24f79cacceeea262987f3cdaf2ef6bc3"></a>
<a id="agroup__bt__gap__defines_html_ga8a6e6ce5e7024c40cc7cae6d4f5c2ed1"></a>
<a id="agroup__bt__gap__defines_html_gadaa7f1547c4ea22936087c181d82a552"></a>
<a id="agroup__bt__conn_html_ga102b97de8689fe3fb53f9691009de87f"></a>
<a id="agroup__bt__gap__defines_html_ga245249c0b6f8ccc419f2132f76362908"></a>
<a id="agroup__bt__gap__defines_html_ga90cfab7c375a8af6f9224a5635cbd023"></a>
<a id="agroup__bt__gap__defines_html_ga379b5d8d7f243abbc584c288cd01815f"></a>
<a id="agroup__bt__gap__defines_html_gacf5f35866d4677bd45c6e567886cabb9"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9"></a>
<a id="gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b"></a>
<a id="gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9"></a>
<a id="gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30"></a>
<a id="gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0"></a>
<a id="gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98"></a>
<a id="gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34"></a>
<a id="gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0"></a>
<a id="gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6"></a>
<a id="gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1"></a>
<a id="gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529"></a>
<a id="gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da"></a>
<a id="gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8"></a>
<a id="ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94"></a>
<a id="ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a"></a>
<a id="ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6"></a>
<a id="gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d"></a>
<a id="gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741"></a>
<a id="gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db"></a>
<a id="gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14"></a>
<a id="gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb"></a>
<a id="gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584"></a>
<a id="ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea"></a>
<a id="ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622"></a>
<a id="gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1"></a>
<a id="gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26"></a>
<a id="gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac"></a>
<a id="gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d"></a>
<a id="gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0"></a>
<a id="gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02"></a>
<a id="gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744"></a>
<a id="gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886"></a>
<a id="gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f"></a>
<a id="gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82"></a>
<a id="gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b"></a>
<a id="ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83"></a>
<a id="ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac"></a>
<a id="gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4"></a>
<a id="gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f"></a>
<a id="ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5"></a>
<a id="gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c"></a>
<a id="gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d"></a>
<a id="gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d"></a>
<a id="gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd"></a>
<a id="gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3"></a>
<a id="gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146"></a>
<a id="gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202"></a>
<a id="ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95"></a>
<a id="ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6"></a>
<a id="ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb"></a>
<a id="ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2"></a>
<a id="ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c"></a>
<a id="ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495"></a>
<a id="ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4"></a>
<a id="ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8"></a>
<a id="ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec"></a>
<a id="ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705"></a>
<a id="ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942"></a>
<a id="gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a"></a>
<a id="gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046"></a>
<a id="gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800"></a>
<a id="gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2"></a>
<a id="gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296"></a>
<a id="gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587"></a>
<a id="gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd"></a>
<a id="gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f"></a>
<a id="gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f"></a>
<a id="ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2"></a>
<a id="ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6"></a>
<a id="ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953"></a>
<a id="ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee"></a>
<a id="ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216"></a>
<a id="ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242"></a>
<a id="gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6"></a>
<a id="gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81"></a>
<a id="ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md)
