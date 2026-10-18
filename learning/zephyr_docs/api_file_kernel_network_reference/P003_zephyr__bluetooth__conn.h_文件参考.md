---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-3
title: zephyr__bluetooth__conn.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_bluetooth\_\_conn.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙连接（Bluetooth Connection）的处理。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/direction.h>
#include <zephyr/bluetooth/gap.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

蓝牙连接（Bluetooth Connection）的处理。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga81de567c4c8cb691ef8b02633b42e342"></a>

```c
#define BT_LE_CONN_PARAM_INIT(int_min, int_max, lat, to)
```

相关声明：[BT_LE_CONN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga81de567c4c8cb691ef8b02633b42e342)。

初始化连接参数（Connection Parameters）。

<a id="r_ga940d55c0d84c0cb8f09bc41074ae50d0"></a>

```c
#define BT_LE_CONN_PARAM(int_min, int_max, lat, to)
```

相关声明：[BT_LE_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga940d55c0d84c0cb8f09bc41074ae50d0)。

用于内联声明连接参数（Connection Parameters）的辅助宏。

<a id="r_ga82df8f439aeb3a156f4238deb085534a"></a>

```c
#define BT_LE_CONN_PARAM_DEFAULT
```

相关声明：[BT_LE_CONN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga82df8f439aeb3a156f4238deb085534a)。

默认低功耗蓝牙连接参数（LE Connection Parameters）：连接间隔 30–50 ms，延迟 0，超时 4 s。

<a id="r_gabca56de0c82c14995738952dafb1fe2d"></a>

```c
#define BT_CONN_LE_PHY_PARAM_INIT(_pref_tx_phy, _pref_rx_phy)
```

相关声明：[BT_CONN_LE_PHY_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gabca56de0c82c14995738952dafb1fe2d)。

初始化物理层参数（PHY Parameters）。

<a id="r_ga39b69f0978f74b5f13f829e908b7cebb"></a>

```c
#define BT_CONN_LE_PHY_PARAM(_pref_tx_phy, _pref_rx_phy)
```

相关声明：[BT_CONN_LE_PHY_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga39b69f0978f74b5f13f829e908b7cebb)。

用于内联声明物理层参数（PHY Parameters）的辅助宏。

<a id="r_ga3ec555bb4ace5e9c7c13735820fd31de"></a>

```c
#define BT_CONN_LE_PHY_PARAM_1M
```

相关声明：[BT_CONN_LE_PHY_PARAM_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3ec555bb4ace5e9c7c13735820fd31de)。

仅低功耗蓝牙 1M 物理层（LE 1M PHY）。

<a id="r_ga633126e356658886e9fa3f3217cb4e2c"></a>

```c
#define BT_CONN_LE_PHY_PARAM_2M
```

相关声明：[BT_CONN_LE_PHY_PARAM_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga633126e356658886e9fa3f3217cb4e2c)。

仅低功耗蓝牙 2M 物理层（LE 2M PHY）。

<a id="r_ga4915244a6cd70995514d6dde1ee0b45f"></a>

```c
#define BT_CONN_LE_PHY_PARAM_CODED
```

相关声明：[BT_CONN_LE_PHY_PARAM_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4915244a6cd70995514d6dde1ee0b45f)。

仅低功耗蓝牙编码物理层（LE Coded PHY）。

<a id="r_ga02c9d7a04ccf2f043293aed7a7f767a7"></a>

```c
#define BT_CONN_LE_PHY_PARAM_ALL
```

相关声明：[BT_CONN_LE_PHY_PARAM_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga02c9d7a04ccf2f043293aed7a7f767a7)。

全部低功耗蓝牙物理层（LE PHYs）。

<a id="r_ga98f9dab71897382cf1187259a3b5660e"></a>

```c
#define BT_CONN_LE_DATA_LEN_PARAM_INIT(_tx_max_len, _tx_max_time)
```

相关声明：[BT_CONN_LE_DATA_LEN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga98f9dab71897382cf1187259a3b5660e)。

初始化发送数据长度参数（Transmit Data Length Parameters）。

<a id="r_ga102b97de8689fe3fb53f9691009de87f"></a>

```c
#define BT_CONN_LE_DATA_LEN_PARAM(_tx_max_len, _tx_max_time)
```

相关声明：[BT_CONN_LE_DATA_LEN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga102b97de8689fe3fb53f9691009de87f)。

用于内联声明发送数据长度参数（Transmit Data Length Parameters）的辅助宏。

<a id="r_gaf66746d834f7556dc77659741e27e0c9"></a>

```c
#define BT_LE_DATA_LEN_PARAM_DEFAULT
```

相关声明：[BT_LE_DATA_LEN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf66746d834f7556dc77659741e27e0c9)。

默认低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="r_ga9cc26afda3c507cb5439184fedcd61ba"></a>

```c
#define BT_LE_DATA_LEN_PARAM_MAX
```

相关声明：[BT_LE_DATA_LEN_PARAM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9cc26afda3c507cb5439184fedcd61ba)。

最大低功耗蓝牙数据长度参数（LE Data Length Parameters）。

<a id="r_gadcb74ad947485dd81dfd59a82d3b0db6"></a>

```c
#define BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS 41
```

相关声明：[BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gadcb74ad947485dd81dfd59a82d3b0db6)。

允许的最大连接间隔组数（Maximum Connection Interval Groups）。

<a id="r_gacce78fed479c9d7e9b394488d5e466d7"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gacce78fed479c9d7e9b394488d5e466d7)。

<a id="r_ga1b9b7d5bd6500ef1195c5da0275247ee"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b9b7d5bd6500ef1195c5da0275247ee)。

<a id="r_gacdf0d72c8f6dfe6e13c714148f04df3c"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS
```

相关声明：[BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gacdf0d72c8f6dfe6e13c714148f04df3c)。

<a id="r_gaf01791831e52ee5976679fc0fac9118c"></a>

```c
#define BT_CONN_LE_FRAME_SPACE_MAX (10000U)
```

相关声明：[BT_CONN_LE_FRAME_SPACE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf01791831e52ee5976679fc0fac9118c)。

最大帧间隔（Maximum frame space），单位为微秒。

<a id="r_ga5354b9973117f94b88c61fb0ea726a4b"></a>

```c
#define BT_CONN_LE_CS_MODE_MAIN_MODE_PART(x)
```

相关声明：[BT_CONN_LE_CS_MODE_MAIN_MODE_PART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5354b9973117f94b88c61fb0ea726a4b)。

从 bt_conn_le_cs_mode 提取主模式部分（Main Mode）。

<a id="r_ga19d2cd20af6f2652164a5677ee8863d5"></a>

```c
#define BT_CONN_LE_CS_MODE_SUB_MODE_PART(x)
```

相关声明：[BT_CONN_LE_CS_MODE_SUB_MODE_PART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga19d2cd20af6f2652164a5677ee8863d5)。

从 bt_conn_le_cs_mode 提取子模式部分（Sub-mode）。

<a id="r_ga707cc62b12c89478aebd0488a464a776"></a>

```c
#define BT_CONN_INTERVAL_TO_MS(interval)
```

相关声明：[BT_CONN_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga707cc62b12c89478aebd0488a464a776)。

将连接间隔（Connection Interval）转换为毫秒。

<a id="r_ga0a5fac126005684847ee7509bb98e382"></a>

```c
#define BT_CONN_INTERVAL_TO_US(interval)
```

相关声明：[BT_CONN_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0a5fac126005684847ee7509bb98e382)。

将连接间隔（Connection Interval）转换为微秒。

<a id="r_gaf4b1395e345f1bf01b83a890bf9a5083"></a>

```c
#define BT_CONN_SCI_INTERVAL_TO_US(_interval)
```

相关声明：[BT_CONN_SCI_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf4b1395e345f1bf01b83a890bf9a5083)。

将较短连接间隔（Shorter Connection Interval）转换为微秒。

<a id="r_ga5e4ec28058d93bede65ccb9d20014e2e"></a>

```c
#define bt_conn_dst_str(_conn)
```

相关声明：[bt_conn_dst_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5e4ec28058d93bede65ccb9d20014e2e)。

获取指向连接目标，即对端地址（Destination / Peer Address）字符串的指针。

<a id="r_ga8ac93a19c34d2821c158f310879fe00d"></a>

```c
#define BT_CONN_LE_CREATE_PARAM_INIT(_options, _interval, _window)
```

相关声明：[BT_CONN_LE_CREATE_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8ac93a19c34d2821c158f310879fe00d)。

初始化创建连接参数（Create Connection Parameters）。

<a id="r_gae86425d432078e2ddca260eebc2802f1"></a>

```c
#define BT_CONN_LE_CREATE_PARAM(_options, _interval, _window)
```

相关声明：[BT_CONN_LE_CREATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae86425d432078e2ddca260eebc2802f1)。

用于内联声明创建连接参数（Create Connection Parameters）的辅助宏。

<a id="r_gab4203c55c20d83256ca036148c14a00d"></a>

```c
#define BT_CONN_LE_CREATE_CONN
```

相关声明：[BT_CONN_LE_CREATE_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab4203c55c20d83256ca036148c14a00d)。

默认低功耗蓝牙创建连接参数（LE Create Connection Parameters）。

<a id="r_gaaba7c37a5c6e98e7b62ac12bde814d5d"></a>

```c
#define BT_CONN_LE_CREATE_CONN_AUTO
```

相关声明：[BT_CONN_LE_CREATE_CONN_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaaba7c37a5c6e98e7b62ac12bde814d5d)。

使用过滤接受列表（Filter Accept List）的默认低功耗蓝牙创建连接参数。

<a id="r_ga3fac32ef426900046d8e38bbd4b7c2d2"></a>

```c
#define BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP 0xFF
```

相关声明：[BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3fac32ef426900046d8e38bbd4b7c2d2)。

表示 L2CAP 连接参数更新过程（Connection Parameter Update Procedure，CPUP）被拒绝的合成错误值（Synthetic Error Value）。

<a id="r_ga9227880a1ae5fc373d334171e1450f00"></a>

```c
#define BT_CONN_CB_DEFINE(_name)
```

相关声明：[BT_CONN_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9227880a1ae5fc373d334171e1450f00)。

为连接事件（Connection Events）注册回调结构体。

<a id="r_ga988dbb7aea2ac136e3bc8efdf6f7478c"></a>

```c
#define BT_PASSKEY_RAND 0xffffffff
```

相关声明：[BT_PASSKEY_RAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga988dbb7aea2ac136e3bc8efdf6f7478c)。

使用 bt_conn_auth_cb 的 app_passkey 回调时，可用于生成随机配对口令（Passkey）的特殊口令值。

<a id="r_ga986f563bfb741c70fbee39b3948d9d8d"></a>

```c
#define BT_BR_CONN_PARAM_INIT(role_switch)
```

相关声明：[BT_BR_CONN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga986f563bfb741c70fbee39b3948d9d8d)。

初始化基本速率／增强数据速率连接参数（BR/EDR Connection Parameters）。

<a id="r_ga6f99f4adfcef36a4d738783921965ca6"></a>

```c
#define BT_BR_CONN_PARAM(role_switch)
```

相关声明：[BT_BR_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6f99f4adfcef36a4d738783921965ca6)。

用于内联声明 BR／EDR 连接参数（Connection Parameters）的辅助宏。

<a id="r_ga5ccdbff63a430a37a8a8077d8792f706"></a>

```c
#define BT_BR_CONN_PARAM_DEFAULT BT_BR_CONN_PARAM(true)
```

相关声明：[BT_BR_CONN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5ccdbff63a430a37a8a8077d8792f706)、[BT_BR_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6f99f4adfcef36a4d738783921965ca6)、[true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

默认 BR／EDR 连接参数：允许角色切换（Role Switch）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_ga08eb37185a763212e65c47ab4c886eca"></a>

```c
enum { BT_CONN_LE_PHY_OPT_NONE = 0 , BT_CONN_LE_PHY_OPT_CODED_S2 = (1UL << (0)) , BT_CONN_LE_PHY_OPT_CODED_S8 = (1UL << (1)) }
```

相关声明：[BT_CONN_LE_PHY_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)、[BT_CONN_LE_PHY_OPT_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34)、[BT_CONN_LE_PHY_OPT_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0)。

连接物理层选项（Connection PHY options）。

<a id="r_gae60f156d2aa01814ad485786e00c4ca7"></a>

```c
enum bt_conn_le_frame_space_update_initiator { BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST , BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER , BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER }
```

相关声明：[bt_conn_le_frame_space_update_initiator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae60f156d2aa01814ad485786e00c4ca7)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495)、[BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4)。

帧间隔更新发起方（Frame Space Update Initiator）。

<a id="r_gab8dde20ae75b51f1e28dbeed06001f20"></a>

```c
enum bt_conn_type { BT_CONN_TYPE_LE = (1UL << (0)) , BT_CONN_TYPE_BR = (1UL << (1)) , BT_CONN_TYPE_SCO = (1UL << (2)) , BT_CONN_TYPE_ISO = (1UL << (3)) , BT_CONN_TYPE_ALL }
```

相关声明：[bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)、[BT_CONN_TYPE_LE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)、[BT_CONN_TYPE_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)、[BT_CONN_TYPE_SCO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)、[BT_CONN_TYPE_ISO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)、[BT_CONN_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)。

连接类型（Connection Type）。

<a id="r_gafe14d64a64383b097760764697b035e2"></a>

```c
enum bt_conn_le_cs_capability_rtt_aa_only { BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_AA_ONLY_10NS , BT_CONN_LE_CS_RTT_AA_ONLY_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_aa_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gafe14d64a64383b097760764697b035e2)、[BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94)、[BT_CONN_LE_CS_RTT_AA_ONLY_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a)、[BT_CONN_LE_CS_RTT_AA_ONLY_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6)。

支持的仅接入地址往返时间精度（AA-Only RTT Precision）。

<a id="r_ga1892ec23ca3b1818287a9d7dafc16433"></a>

```c
enum bt_conn_le_cs_capability_rtt_sounding { BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_SOUNDING_10NS , BT_CONN_LE_CS_RTT_SOUNDING_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_sounding](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1892ec23ca3b1818287a9d7dafc16433)、[BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14)、[BT_CONN_LE_CS_RTT_SOUNDING_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb)、[BT_CONN_LE_CS_RTT_SOUNDING_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584)。

支持的探测序列往返时间精度（Sounding Sequence RTT Precision）。

<a id="r_ga5568443825fc1ce9534753d8918aa813"></a>

```c
enum bt_conn_le_cs_capability_rtt_random_payload { BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP = 0 , BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS , BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS }
```

相关声明：[bt_conn_le_cs_capability_rtt_random_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5568443825fc1ce9534753d8918aa813)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741)、[BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db)。

支持的随机有效载荷往返时间精度（Random Payload RTT Precision）。

<a id="r_ga2f757b15d1d5006ce2fa6a7a78082156"></a>

```c
enum bt_conn_le_cs_mode { BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_1 , BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_2 , BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE = BT_HCI_OP_LE_CS_MAIN_MODE_3 , BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1 , BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3 , BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2 }
```

相关声明：[bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)、[BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a)、[BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a)、[BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf)、[BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7)、[BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26)、[BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac)。

信道探测模式（Channel Sounding Mode），包括主模式与子模式。

<a id="r_ga0e6f6d4fdbdfc3ed75fef4a95136076f"></a>

```c
enum bt_conn_le_cs_role { BT_CONN_LE_CS_ROLE_INITIATOR , BT_CONN_LE_CS_ROLE_REFLECTOR }
```

相关声明：[bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)、[BT_CONN_LE_CS_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4)、[BT_CONN_LE_CS_ROLE_REFLECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968)。

信道探测角色（Channel Sounding Role）。

<a id="r_gaffd6abf9b92cc8d8463797a73b840f51"></a>

```c
enum bt_conn_le_cs_rtt_type { BT_CONN_LE_CS_RTT_TYPE_AA_ONLY = BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY , BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND , BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND , BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND , BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM = BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND }
```

相关声明：[bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)、[BT_CONN_LE_CS_RTT_TYPE_AA_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088)、[BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)、[BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)、[BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad)、[BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91)、[BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f)、[BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5)。

信道探测往返时间类型（Channel Sounding RTT Type）。

<a id="r_gaadbf6a4dba28aec90ea07b7da634e1bb"></a>

```c
enum bt_conn_le_cs_sync_phy { BT_CONN_LE_CS_SYNC_1M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_1M , BT_CONN_LE_CS_SYNC_2M_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M , BT_CONN_LE_CS_SYNC_2M_2BT_PHY = BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT }
```

相关声明：[bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)、[BT_CONN_LE_CS_SYNC_1M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95)、[BT_CONN_LE_CS_SYNC_2M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6)、[BT_CONN_LE_CS_SYNC_2M_2BT_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b)。

CS 同步使用的信道探测物理层（Channel Sounding PHY）。

<a id="r_ga34e4837a77c7afd6999095985ddad4f0"></a>

```c
enum bt_conn_le_cs_chsel_type { BT_CONN_LE_CS_CHSEL_TYPE_3B = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B , BT_CONN_LE_CS_CHSEL_TYPE_3C = BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C }
```

相关声明：[bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)、[BT_CONN_LE_CS_CHSEL_TYPE_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1)、[BT_CONN_LE_CS_CHSEL_TYPE_3C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6)。

信道探测信道选择类型（Channel Sounding Channel Selection Type）。

<a id="r_gaf2331ec1f1222de51fc4f30566e1c52b"></a>

```c
enum bt_conn_le_cs_ch3c_shape { BT_CONN_LE_CS_CH3C_SHAPE_HAT = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT , BT_CONN_LE_CS_CH3C_SHAPE_X = BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X }
```

相关声明：[bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)、[BT_CONN_LE_CS_CH3C_SHAPE_HAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea)、[BT_CONN_LE_CS_CH3C_SHAPE_X](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622)。

信道探测信道序列形状（Channel Sounding Channel Sequence Shape）。

<a id="r_ga9a1dc2010c5237466de87160944630d3"></a>

```c
enum bt_conn_le_cs_procedure_done_status { BT_CONN_LE_CS_PROCEDURE_COMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE , BT_CONN_LE_CS_PROCEDURE_INCOMPLETE = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL , BT_CONN_LE_CS_PROCEDURE_ABORTED = BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED }
```

相关声明：[bt_conn_le_cs_procedure_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9a1dc2010c5237466de87160944630d3)、[BT_CONN_LE_CS_PROCEDURE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f)、[BT_CONN_LE_CS_PROCEDURE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82)、[BT_CONN_LE_CS_PROCEDURE_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)。

过程完成状态（Procedure Done Status）。

<a id="r_ga8e54a191b889b1d5ed3e1fbb648d9bc7"></a>

```c
enum bt_conn_le_cs_subevent_done_status { BT_CONN_LE_CS_SUBEVENT_COMPLETE = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE , BT_CONN_LE_CS_SUBEVENT_ABORTED = BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED }
```

相关声明：[bt_conn_le_cs_subevent_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8e54a191b889b1d5ed3e1fbb648d9bc7)、[BT_CONN_LE_CS_SUBEVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)、[BT_CONN_LE_CS_SUBEVENT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)。

子事件完成状态（Subevent Done Status）。

<a id="r_ga3196a0eb1c7497e93d7c646713d2fc79"></a>

```c
enum bt_conn_le_cs_procedure_abort_reason { BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT , BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED , BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS , BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED , BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED = BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED }
```

相关声明：[bt_conn_le_cs_procedure_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3196a0eb1c7497e93d7c646713d2fc79)、[BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d)、[BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0)、[BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02)、[BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744)、[BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886)。

过程中止原因（Procedure Abort Reason）。

<a id="r_ga6394906c6da40c9bebfaeb05de9fd5be"></a>

```c
enum bt_conn_le_cs_subevent_abort_reason { BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT , BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED , BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC , BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT , BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED = BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED }
```

相关声明：[bt_conn_le_cs_subevent_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6394906c6da40c9bebfaeb05de9fd5be)、[BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c)、[BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d)、[BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d)、[BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd)、[BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3)。

子事件中止原因（Subevent Abort Reason）。

<a id="r_ga9c54d2e44903cf7c4e5c97e223069dbc"></a>

```c
enum { BT_CONN_ROLE_CENTRAL = 0 , BT_CONN_ROLE_PERIPHERAL = 1 }
```

相关声明：[BT_CONN_ROLE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)、[BT_CONN_ROLE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)。

<a id="r_ga9442c1479db60e2db40a2ea6de565282"></a>

```c
enum bt_conn_state { BT_CONN_STATE_DISCONNECTED , BT_CONN_STATE_CONNECTING , BT_CONN_STATE_CONNECTED , BT_CONN_STATE_DISCONNECTING }
```

相关声明：[bt_conn_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9442c1479db60e2db40a2ea6de565282)、[BT_CONN_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)、[BT_CONN_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)、[BT_CONN_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)、[BT_CONN_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)。

<a id="r_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>

```c
enum bt_security_t { BT_SECURITY_L0 , BT_SECURITY_L1 , BT_SECURITY_L2 , BT_SECURITY_L3 , BT_SECURITY_L4 , BT_SECURITY_FORCE_PAIR = (1UL << (7)) }
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[BT_SECURITY_L0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)、[BT_SECURITY_L1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)、[BT_SECURITY_L2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)、[BT_SECURITY_L3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)、[BT_SECURITY_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)、[BT_SECURITY_FORCE_PAIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)。

安全级别（Security Level）。

<a id="r_ga2f8712bbf3410de5cbe6ce489fe30e5e"></a>

```c
enum bt_security_flag { BT_SECURITY_FLAG_SC = (1UL << (0)) , BT_SECURITY_FLAG_OOB = (1UL << (1)) }
```

相关声明：[bt_security_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f8712bbf3410de5cbe6ce489fe30e5e)、[BT_SECURITY_FLAG_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)、[BT_SECURITY_FLAG_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)。

安全信息标志（Security Info Flags）。

<a id="r_ga737d8118f8aba8985292d92d0604b190"></a>

```c
enum bt_conn_le_tx_power_phy { BT_CONN_LE_TX_POWER_PHY_NONE , BT_CONN_LE_TX_POWER_PHY_1M , BT_CONN_LE_TX_POWER_PHY_2M , BT_CONN_LE_TX_POWER_PHY_CODED_S8 , BT_CONN_LE_TX_POWER_PHY_CODED_S2 }
```

相关声明：[bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)、[BT_CONN_LE_TX_POWER_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)、[BT_CONN_LE_TX_POWER_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)、[BT_CONN_LE_TX_POWER_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)、[BT_CONN_LE_TX_POWER_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)、[BT_CONN_LE_TX_POWER_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)。

<a id="r_gaf43d7aa3ad1c8d2bde8b04e650fe7b7e"></a>

```c
enum bt_conn_le_path_loss_zone { BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW , BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE , BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH , BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE }
```

相关声明：[bt_conn_le_path_loss_zone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec)、[BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705)、[BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942)。

已进入的路径损耗区域（Path Loss Zone）。

<a id="r_ga57465d3a61214531ddaffc2c30939043"></a>

```c
enum bt_conn_auth_keypress { BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED = 0x00 , BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED = 0x01 , BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED = 0x02 , BT_CONN_AUTH_KEYPRESS_CLEARED = 0x03 , BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED = 0x04 }
```

相关声明：[bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)、[BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)、[BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)、[BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)、[BT_CONN_AUTH_KEYPRESS_CLEARED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)、[BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)。

配对口令按键通知类型（Passkey Keypress Notification Type）。

<a id="r_ga3afc8024ddbcd3bf5a809706e39f74bc"></a>

```c
enum { BT_CONN_LE_OPT_NONE = 0 , BT_CONN_LE_OPT_CODED = (1UL << (0)) , BT_CONN_LE_OPT_NO_1M = (1UL << (1)) }
```

相关声明：[BT_CONN_LE_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)、[BT_CONN_LE_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)、[BT_CONN_LE_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)。

<a id="r_gaa9420ff489fd5857ff076406442679ff"></a>

```c
enum bt_security_err { BT_SECURITY_ERR_SUCCESS , BT_SECURITY_ERR_AUTH_FAIL , BT_SECURITY_ERR_PIN_OR_KEY_MISSING , BT_SECURITY_ERR_OOB_NOT_AVAILABLE , BT_SECURITY_ERR_AUTH_REQUIREMENT , BT_SECURITY_ERR_PAIR_NOT_SUPPORTED , BT_SECURITY_ERR_PAIR_NOT_ALLOWED , BT_SECURITY_ERR_INVALID_PARAM , BT_SECURITY_ERR_KEY_REJECTED , BT_SECURITY_ERR_UNSPECIFIED }
```

相关声明：[bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)、[BT_SECURITY_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)、[BT_SECURITY_ERR_AUTH_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)、[BT_SECURITY_ERR_PIN_OR_KEY_MISSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)、[BT_SECURITY_ERR_OOB_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)、[BT_SECURITY_ERR_AUTH_REQUIREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)、[BT_SECURITY_ERR_PAIR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)、[BT_SECURITY_ERR_PAIR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)、[BT_SECURITY_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)、[BT_SECURITY_ERR_KEY_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)、[BT_SECURITY_ERR_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)。

<a id="r_gaf3653de72793f775e33fd9eb04c3e7a2"></a>

```c
enum bt_conn_le_cs_procedure_enable_state { BT_CONN_LE_CS_PROCEDURES_DISABLED = BT_HCI_OP_LE_CS_PROCEDURES_DISABLED , BT_CONN_LE_CS_PROCEDURES_ENABLED = BT_HCI_OP_LE_CS_PROCEDURES_ENABLED }
```

相关声明：[bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)、[BT_CONN_LE_CS_PROCEDURES_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83)、[BT_CONN_LE_CS_PROCEDURES_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac)。

<a id="r_gab7acdbdf273fc760799cf0d8cf71591c"></a>

```c
enum bt_conn_le_cs_tone_antenna_config_selection { BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1 = BT_HCI_OP_LE_CS_ACI_0 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1 = BT_HCI_OP_LE_CS_ACI_1 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1 = BT_HCI_OP_LE_CS_ACI_2 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1 = BT_HCI_OP_LE_CS_ACI_3 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2 = BT_HCI_OP_LE_CS_ACI_4 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3 = BT_HCI_OP_LE_CS_ACI_5 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4 = BT_HCI_OP_LE_CS_ACI_6 , BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2 = BT_HCI_OP_LE_CS_ACI_7 }
```

相关声明：[bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb)、[BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2)。

CS 测试音调天线配置选择（CS Test Tone Antenna Config Selection）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_ga060d51eb2208de6f805b1fc0672d2d0c"></a>

```c
struct bt_conn * bt_conn_ref (struct bt_conn *conn)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga060d51eb2208de6f805b1fc0672d2d0c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

增加连接的引用计数（Reference Count）。

<a id="r_ga4b18c6b22a9f02be0d7d078b2ce51ff6"></a>

```c
void bt_conn_unref (struct bt_conn *conn)
```

相关声明：[bt_conn_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

减少连接的引用计数（Reference Count）。

<a id="r_gaf073384538a67c242b00150904176f66"></a>

```c
static struct bt_conn * bt_conn_take (struct bt_conn **orig)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_take](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf073384538a67c242b00150904176f66)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

接管连接指针的所有权（Ownership），将原指针设为 NULL。

<a id="r_gaf1aeec9b9893450423cf066a6f471824"></a>

```c
void bt_conn_drop (struct bt_conn **orig)
```

相关声明：[bt_conn_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf1aeec9b9893450423cf066a6f471824)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

释放连接引用（Connection Reference）并清空指针。

<a id="r_ga5bdf8e8efc85138d3631dc1efffc3916"></a>

```c
void bt_conn_foreach (enum bt_conn_type type, void(*func)(struct bt_conn *conn, void *data), void *data)
```

相关声明：[bt_conn_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5bdf8e8efc85138d3631dc1efffc3916)、[bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

遍历全部 bt_conn 对象。

<a id="r_ga1bfe349efd8a7de31e9457fe439d746a"></a>

```c
struct bt_conn * bt_conn_lookup_addr_le (uint8_t id, const bt_addr_le_t *peer)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_lookup_addr_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bfe349efd8a7de31e9457fe439d746a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

根据地址查找现有连接（Connection）。

<a id="r_ga77108581b8f61485ca840e4bf7a17087"></a>

```c
const bt_addr_le_t * bt_conn_get_dst (const struct bt_conn *conn)
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_conn_get_dst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga77108581b8f61485ca840e4bf7a17087)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的目标，即对端地址（Destination / Peer Address）。

<a id="r_gad4aed76b80cc815f748ad0e84ae3d87c"></a>

```c
uint8_t bt_conn_index (const struct bt_conn *conn)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad4aed76b80cc815f748ad0e84ae3d87c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的数组索引（Array Index）。

<a id="r_ga2de54f2ac83f0d8dca2a85a9fbfadcaa"></a>

```c
int bt_conn_get_info (const struct bt_conn *conn, struct bt_conn_info *info)
```

相关声明：[bt_conn_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_info](../bluetooth_connection_model_reference/P009_bt_conn_info_结构体.md)。

获取连接信息（Connection Info）。

<a id="r_gaf3d55f1f8efc630b495389ced3ee3fa5"></a>

```c
bool bt_conn_is_type (const struct bt_conn *conn, enum bt_conn_type type)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_conn_is_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3d55f1f8efc630b495389ced3ee3fa5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)。

确定连接类型（Connection Type）的函数。

<a id="r_gac4e0bd799fc87b65367129685f57c2bd"></a>

```c
int bt_conn_get_remote_info (const struct bt_conn *conn, struct bt_conn_remote_info *remote_info)
```

相关声明：[bt_conn_get_remote_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac4e0bd799fc87b65367129685f57c2bd)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_remote_info](../bluetooth_connection_model_reference/P039_bt_conn_remote_info_结构体.md)。

获取远端设备的连接信息（Connection Info）。

<a id="r_gaa5289154bc508444f68df7abcef18aca"></a>

```c
int bt_conn_le_get_tx_power_level (struct bt_conn *conn, struct bt_conn_le_tx_power *tx_power_level)
```

相关声明：[bt_conn_le_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa5289154bc508444f68df7abcef18aca)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)。

获取连接发射功率等级（Transmit Power Level）。

<a id="r_gaa79eada87d698f4998af876d03d7e92b"></a>

```c
int bt_conn_le_enhanced_get_tx_power_level (struct bt_conn *conn, struct bt_conn_le_tx_power *tx_power)
```

相关声明：[bt_conn_le_enhanced_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa79eada87d698f4998af876d03d7e92b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power](../bluetooth_connection_model_reference/P035_bt_conn_le_tx_power_结构体.md)。

获取本地增强连接发射功率等级（Enhanced Connection Transmit Power Level）。

<a id="r_ga0843a2e0b6f16ebd132a3a512cfd27a4"></a>

```c
int bt_conn_le_get_remote_tx_power_level (struct bt_conn *conn, enum bt_conn_le_tx_power_phy phy)
```

相关声明：[bt_conn_le_get_remote_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0843a2e0b6f16ebd132a3a512cfd27a4)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)。

获取远端，即对端发射功率等级（Peer Transmit Power Level）。

<a id="r_gaa1f38911acee0534a8a6e414018c6fb6"></a>

```c
int bt_conn_le_set_tx_power_report_enable (struct bt_conn *conn, bool local_enable, bool remote_enable)
```

相关声明：[bt_conn_le_set_tx_power_report_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa1f38911acee0534a8a6e414018c6fb6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用发射功率报告（Transmit Power Reporting）。

<a id="r_ga6be5f3bf064ba03dc2307fdd2b634637"></a>

```c
int bt_conn_le_set_path_loss_mon_param (struct bt_conn *conn, const struct bt_conn_le_path_loss_reporting_param *param)
```

相关声明：[bt_conn_le_set_path_loss_mon_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6be5f3bf064ba03dc2307fdd2b634637)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_path_loss_reporting_param](../bluetooth_connection_model_reference/P026_bt_conn_le_path_loss_reporting_param_结构体.md)。

设置路径损耗监测参数（Path Loss Monitoring Parameters）。

<a id="r_ga90ae27bcc6f71f32be56efe8ecbc165d"></a>

```c
int bt_conn_le_set_path_loss_mon_enable (struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_le_set_path_loss_mon_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga90ae27bcc6f71f32be56efe8ecbc165d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用路径损耗监测（Path Loss Monitoring）。

<a id="r_gac7bb456c530c7e08b4fa9f4d478fdaf9"></a>

```c
int bt_conn_le_subrate_set_defaults (const struct bt_conn_le_subrate_param *params)
```

相关声明：[bt_conn_le_subrate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac7bb456c530c7e08b4fa9f4d478fdaf9)、[bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)。

设置默认连接子速率参数（Connection Subrating Parameters）。

<a id="r_ga754ed218fe9577f2d0ef6d508cfc5a0b"></a>

```c
int bt_conn_le_subrate_request (struct bt_conn *conn, const struct bt_conn_le_subrate_param *params)
```

相关声明：[bt_conn_le_subrate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga754ed218fe9577f2d0ef6d508cfc5a0b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_subrate_param](../bluetooth_connection_model_reference/P033_bt_conn_le_subrate_param_结构体.md)。

请求新的子速率参数（Subrating Parameters）。

<a id="r_ga2e7e836d94a5330ae01e14dbd3e29f14"></a>

```c
int bt_conn_le_read_min_conn_interval_groups (struct bt_conn_le_min_conn_interval_info *info)
```

相关声明：[bt_conn_le_read_min_conn_interval_groups](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e7e836d94a5330ae01e14dbd3e29f14)、[bt_conn_le_min_conn_interval_info](../bluetooth_connection_model_reference/P025_bt_conn_le_min_conn_interval_info_结构体.md)。

读取支持的最小连接间隔组（Minimum Supported Connection Interval Groups）。

<a id="r_ga9af26600acdf5b3a8b8ea0a32e14b497"></a>

```c
int bt_conn_le_read_min_conn_interval (uint16_t *min_interval_us)
```

相关声明：[bt_conn_le_read_min_conn_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9af26600acdf5b3a8b8ea0a32e14b497)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取支持的最小连接间隔（Minimum Supported Connection Interval）。

<a id="r_gac9b111639f9b982cd97e13f313e51461"></a>

```c
int bt_conn_le_conn_rate_set_defaults (const struct bt_conn_le_conn_rate_param *params)
```

相关声明：[bt_conn_le_conn_rate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac9b111639f9b982cd97e13f313e51461)、[bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)。

设置默认连接速率参数（Connection Rate Parameters）。

<a id="r_ga2e4188482deeda71f8e5d42a07538f31"></a>

```c
int bt_conn_le_conn_rate_request (struct bt_conn *conn, const struct bt_conn_le_conn_rate_param *params)
```

相关声明：[bt_conn_le_conn_rate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e4188482deeda71f8e5d42a07538f31)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_conn_rate_param](../bluetooth_connection_model_reference/P011_bt_conn_le_conn_rate_param_结构体.md)。

请求新的连接速率参数（Connection Rate Parameters）。

<a id="r_gac0dbbdb95ef868f35006622932dc8901"></a>

```c
int bt_conn_le_read_all_remote_features (struct bt_conn *conn, uint8_t pages_requested)
```

相关声明：[bt_conn_le_read_all_remote_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac0dbbdb95ef868f35006622932dc8901)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取远端特性页（Remote Feature Pages）。

<a id="r_gab734fbc307eff3c5bddf7c5e6ddd341b"></a>

```c
int bt_conn_le_frame_space_update (struct bt_conn *conn, const struct bt_conn_le_frame_space_update_param *params)
```

相关声明：[bt_conn_le_frame_space_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab734fbc307eff3c5bddf7c5e6ddd341b)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_frame_space_update_param](../bluetooth_connection_model_reference/P021_bt_conn_le_frame_space_update_param_结构体.md)。

更新帧间隔（Frame Space）。

<a id="r_gab44a964725f54ed2d37de17c6e2fd3eb"></a>

```c
int bt_conn_le_param_update (struct bt_conn *conn, const struct bt_le_conn_param *param)
```

相关声明：[bt_conn_le_param_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab44a964725f54ed2d37de17c6e2fd3eb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)。

更新连接参数（Connection Parameters）。

<a id="r_ga8a2006f6e34b20c7e8ef65a73f431a57"></a>

```c
int bt_conn_le_data_len_update (struct bt_conn *conn, const struct bt_conn_le_data_len_param *param)
```

相关声明：[bt_conn_le_data_len_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8a2006f6e34b20c7e8ef65a73f431a57)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_data_len_param](../bluetooth_connection_model_reference/P020_bt_conn_le_data_len_param_结构体.md)。

更新连接发送数据长度参数（Transmit Data Length Parameters）。

<a id="r_gae13ed81b1e7928f44b8fdf85995b3e58"></a>

```c
int bt_conn_le_phy_update (struct bt_conn *conn, const struct bt_conn_le_phy_param *param)
```

相关声明：[bt_conn_le_phy_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae13ed81b1e7928f44b8fdf85995b3e58)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_le_phy_param](../bluetooth_connection_model_reference/P029_bt_conn_le_phy_param_结构体.md)。

更新连接物理层参数（PHY Parameters）。

<a id="r_ga7c8e7a7616e7b56f97da7ff4bc0fc7ba"></a>

```c
int bt_conn_le_set_default_phy (uint8_t pref_tx_phy, uint8_t pref_rx_phy)
```

相关声明：[bt_conn_le_set_default_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga7c8e7a7616e7b56f97da7ff4bc0fc7ba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新默认物理层参数（PHY Parameters），用于此后经低功耗蓝牙传输（LE Transport）建立的全部连接。

<a id="r_ga14e7c852b0271781594e742ae509c5d3"></a>

```c
int bt_conn_disconnect (struct bt_conn *conn, uint8_t reason)
```

相关声明：[bt_conn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga14e7c852b0271781594e742ae509c5d3)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

断开远端设备或取消待处理连接（Pending Connection）。

<a id="r_ga8d66f3e0262a51279e9fa8b3139252e6"></a>

```c
int bt_conn_le_create (const bt_addr_le_t *peer, const struct bt_conn_le_create_param *create_param, const struct bt_le_conn_param *conn_param, struct bt_conn **conn)
```

相关声明：[bt_conn_le_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8d66f3e0262a51279e9fa8b3139252e6)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发起与远端设备的低功耗蓝牙连接（LE Connection）。

<a id="r_ga98f99c893e444d1ad1ecd9139803c0b1"></a>

```c
int bt_conn_le_create_synced (const struct bt_le_ext_adv *adv, const struct bt_conn_le_create_synced_param *synced_param, const struct bt_le_conn_param *conn_param, struct bt_conn **conn)
```

相关声明：[bt_conn_le_create_synced](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga98f99c893e444d1ad1ecd9139803c0b1)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_conn_le_create_synced_param](../bluetooth_connection_model_reference/P013_bt_conn_le_create_synced_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

创建与已同步设备（Synced Device）的连接。

<a id="r_gaecfaf2cb44772511dbb585de8f76f09b"></a>

```c
int bt_conn_le_create_auto (const struct bt_conn_le_create_param *create_param, const struct bt_le_conn_param *conn_param)
```

相关声明：[bt_conn_le_create_auto](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaecfaf2cb44772511dbb585de8f76f09b)、[bt_conn_le_create_param](../bluetooth_connection_model_reference/P012_bt_conn_le_create_param_结构体.md)、[bt_le_conn_param](../bluetooth_connection_model_reference/P093_bt_le_conn_param_结构体.md)。

自动连接过滤接受列表（Filter Accept List）中的远端设备。

<a id="r_ga62dc2663b4fa39a33adb76dc9a136aa4"></a>

```c
int bt_conn_create_auto_stop (void)
```

相关声明：[bt_conn_create_auto_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga62dc2663b4fa39a33adb76dc9a136aa4)。

停止自动创建连接（Automatic Connect Creation）。

<a id="r_gae001f1268e1ff42c3c974c95dcb6735d"></a>

```c
int bt_conn_set_security (struct bt_conn *conn, bt_security_t sec)
```

相关声明：[bt_conn_set_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae001f1268e1ff42c3c974c95dcb6735d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)。

设置连接的安全等级（Security Level）。

<a id="r_ga4b43ef0f30146808e560991a302e88ad"></a>

```c
bt_security_t bt_conn_get_security (const struct bt_conn *conn)
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[bt_conn_get_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b43ef0f30146808e560991a302e88ad)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的安全等级（Security Level）。

<a id="r_gaff3e6aa16b68e5da7dab53289295545e"></a>

```c
uint8_t bt_conn_enc_key_size (const struct bt_conn *conn)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_enc_key_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaff3e6aa16b68e5da7dab53289295545e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取加密密钥大小（Encryption Key Size）。

<a id="r_gaa9b79cd44734c1e560d6f30509be4d0b"></a>

```c
int bt_conn_cb_register (struct bt_conn_cb *cb)
```

相关声明：[bt_conn_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9b79cd44734c1e560d6f30509be4d0b)、[bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)。

注册连接回调（Connection Callbacks）。

<a id="r_gad2f90b34390e3c3697fd455ae4ef5f31"></a>

```c
int bt_conn_cb_unregister (struct bt_conn_cb *cb)
```

相关声明：[bt_conn_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad2f90b34390e3c3697fd455ae4ef5f31)、[bt_conn_cb](../bluetooth_connection_model_reference/P008_bt_conn_cb_结构体.md)。

注销连接回调（Connection Callbacks）。

<a id="r_ga327444a6987b8e0b573fe758d2f75886"></a>

```c
static const char * bt_security_err_to_str (enum bt_security_err err)
```

相关声明：[bt_security_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga327444a6987b8e0b573fe758d2f75886)、[bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)。

将安全错误（Security Error）转换为字符串。

<a id="r_ga014db594b17a3b5d7d954e64ad8de759"></a>

```c
void bt_set_bondable (bool enable)
```

相关声明：[bt_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga014db594b17a3b5d7d954e64ad8de759)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用绑定（Bonding）。

<a id="r_ga0c84d5597a71fe38788a88063fd19a2d"></a>

```c
bool bt_get_bondable (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_get_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0c84d5597a71fe38788a88063fd19a2d)。

获取绑定标志（Bonding Flag）。

<a id="r_ga4165819d12dd96e00dfa2fd6f4b95669"></a>

```c
int bt_conn_set_bondable (struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4165819d12dd96e00dfa2fd6f4b95669)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置／清除给定连接的绑定标志（Bonding Flag）。

<a id="r_gad02f8fe587efd543c0c81cace3f63d63"></a>

```c
void bt_le_oob_set_sc_flag (bool enable)
```

相关声明：[bt_le_oob_set_sc_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad02f8fe587efd543c0c81cace3f63d63)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

允许／禁止使用远端低功耗安全连接带外数据（LE SC OOB Data）进行配对。

<a id="r_ga978770d46d7c8af854a61261c14cb892"></a>

```c
void bt_le_oob_set_legacy_flag (bool enable)
```

相关声明：[bt_le_oob_set_legacy_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga978770d46d7c8af854a61261c14cb892)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

允许／禁止使用远端传统带外数据（Legacy OOB Data）进行配对。

<a id="r_ga0f889983cfabafe826b4feb6899b95ba"></a>

```c
int bt_le_oob_set_legacy_tk (struct bt_conn *conn, const uint8_t *tk)
```

相关声明：[bt_le_oob_set_legacy_tk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0f889983cfabafe826b4feb6899b95ba)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置用于配对的带外临时密钥（OOB Temporary Key）。

<a id="r_gac365f9748ad0737f09142ee1de982503"></a>

```c
int bt_le_oob_set_sc_data (struct bt_conn *conn, const struct bt_le_oob_sc_data *oobd_local, const struct bt_le_oob_sc_data *oobd_remote)
```

相关声明：[bt_le_oob_set_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac365f9748ad0737f09142ee1de982503)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)。

在低功耗安全连接（LE Secure Connections，SC）配对过程中设置带外数据（OOB Data）。

<a id="r_ga096552403b5bcd0107f69eded772b1ee"></a>

```c
int bt_le_oob_get_sc_data (struct bt_conn *conn, const struct bt_le_oob_sc_data **oobd_local, const struct bt_le_oob_sc_data **oobd_remote)
```

相关声明：[bt_le_oob_get_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga096552403b5bcd0107f69eded772b1ee)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)、[bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)。

获取低功耗安全连接（LE Secure Connections，SC）配对过程使用的带外数据（OOB Data）。

<a id="r_ga1bf13d2dfdbdf0a72f9b1c759ef23f60"></a>

```c
int bt_conn_auth_cb_register (const struct bt_conn_auth_cb *cb)
```

相关声明：[bt_conn_auth_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)、[bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)。

注册认证回调（Authentication Callbacks）。

<a id="r_ga81077385583d71c248a1eb6aab9ee86e"></a>

```c
int bt_conn_auth_cb_overlay (struct bt_conn *conn, const struct bt_conn_auth_cb *cb)
```

相关声明：[bt_conn_auth_cb_overlay](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga81077385583d71c248a1eb6aab9ee86e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_auth_cb](../bluetooth_connection_model_reference/P003_bt_conn_auth_cb_结构体.md)。

为给定连接覆盖所使用的认证回调（Authentication Callbacks）。

<a id="r_gac6684a8089ebd495b539d661cf9fd13f"></a>

```c
int bt_conn_auth_info_cb_register (struct bt_conn_auth_info_cb *cb)
```

相关声明：[bt_conn_auth_info_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac6684a8089ebd495b539d661cf9fd13f)、[bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)。

注册认证信息回调（Authentication Information Callbacks）。

<a id="r_gac73a60b8b6b569b84fe17f707fa33f37"></a>

```c
int bt_conn_auth_info_cb_unregister (struct bt_conn_auth_info_cb *cb)
```

相关声明：[bt_conn_auth_info_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac73a60b8b6b569b84fe17f707fa33f37)、[bt_conn_auth_info_cb](../bluetooth_connection_model_reference/P004_bt_conn_auth_info_cb_结构体.md)。

注销认证信息回调（Authentication Information Callbacks）。

<a id="r_ga3906d8d3d192e8a6ad1bf6b7acc32ff0"></a>

```c
int bt_conn_auth_passkey_entry (struct bt_conn *conn, unsigned int passkey)
```

相关声明：[bt_conn_auth_passkey_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使用输入的配对口令（Passkey）回复。

<a id="r_ga2987a902da4f5cfe3671c60d154ced7e"></a>

```c
int bt_conn_auth_keypress_notify (struct bt_conn *conn, enum bt_conn_auth_keypress type)
```

相关声明：[bt_conn_auth_keypress_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2987a902da4f5cfe3671c60d154ced7e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)。

配对期间发送配对口令按键通知（Passkey Keypress Notification）。

<a id="r_ga89e5fc4bcab3f5598d20a9cd8ace5f59"></a>

```c
int bt_conn_auth_cancel (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga89e5fc4bcab3f5598d20a9cd8ace5f59)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

取消正在进行的认证配对（Authenticated Pairing）。

<a id="r_gab8c3ecf2a3d68e54379917844a29d995"></a>

```c
int bt_conn_auth_passkey_confirm (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_passkey_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8c3ecf2a3d68e54379917844a29d995)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

回复使用者是否已确认配对口令（Passkey）匹配。

<a id="r_ga3e15b9deb6787d3e415bbea35c9aa91d"></a>

```c
int bt_conn_auth_pairing_confirm (struct bt_conn *conn)
```

相关声明：[bt_conn_auth_pairing_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3e15b9deb6787d3e415bbea35c9aa91d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

回复使用者是否已确认传入的配对请求（Incoming Pairing）。

<a id="r_ga4002a1b092832807218afa8ad279ab98"></a>

```c
int bt_conn_auth_pincode_entry (struct bt_conn *conn, const char *pin)
```

相关声明：[bt_conn_auth_pincode_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4002a1b092832807218afa8ad279ab98)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

使用输入的 PIN 码（PIN Code）回复。

<a id="r_gaf7849f332386f8903d35d6904f6c82b9"></a>

```c
struct bt_conn * bt_conn_create_br (const bt_addr_t *peer, const struct bt_br_conn_param *param)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_create_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf7849f332386f8903d35d6904f6c82b9)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_br_conn_param](../bluetooth_service_model_reference/P010_bt_br_conn_param_结构体.md)。

发起与远端设备的 BR／EDR 连接（Connection）。

<a id="r_ga11ae1b656683cebe9db6a53e5166ad7a"></a>

```c
struct bt_conn * bt_conn_lookup_addr_br (const bt_addr_t *peer)
```

相关声明：[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_conn_lookup_addr_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga11ae1b656683cebe9db6a53e5166ad7a)、[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)。

根据地址查找现有基本速率连接（BR Connection）。

<a id="r_ga1b02a1ce8e48ad483d73d1efd803618c"></a>

```c
const bt_addr_t * bt_conn_get_dst_br (const struct bt_conn *conn)
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bt_conn_get_dst_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b02a1ce8e48ad483d73d1efd803618c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取连接的目标，即对端地址（Destination / Peer Address）。

<a id="r_ga3a7741f1e884168168a09e9ec5f28c49"></a>

```c
int bt_conn_br_switch_role (const struct bt_conn *conn, uint8_t role)
```

相关声明：[bt_conn_br_switch_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3a7741f1e884168168a09e9ec5f28c49)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更改 conn 的角色（Role）。

<a id="r_gab6c2073091d1d08032c51aadb904ea3f"></a>

```c
int bt_conn_br_set_role_switch_enable (const struct bt_conn *conn, bool enable)
```

相关声明：[bt_conn_br_set_role_switch_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab6c2073091d1d08032c51aadb904ea3f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过设置连接的链路策略（Link Policy），启用／禁用该连接的角色切换（Role Switch）。

<a id="r_ga641f7f4ce7fe0641948a798881ecedcb"></a>

```c
int bt_conn_br_enter_sniff_mode (struct bt_conn *conn, uint16_t min_interval, uint16_t max_interval, uint16_t attempt, uint16_t timeout)
```

相关声明：[bt_conn_br_enter_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga641f7f4ce7fe0641948a798881ecedcb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查蓝牙连接并进入嗅探模式（Sniff Mode）。

<a id="r_gab1aedad7da2eecc6c30acbfcdf9fbfec"></a>

```c
int bt_conn_br_exit_sniff_mode (struct bt_conn *conn)
```

相关声明：[bt_conn_br_exit_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab1aedad7da2eecc6c30acbfcdf9fbfec)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

检查蓝牙连接并退出嗅探模式（Sniff Mode）。

<a id="r_ga910157e30fad972e8c606d1e1645603e"></a>

```c
int bt_conn_br_set_sniff_subrating (struct bt_conn *conn, uint16_t max_latency, uint16_t min_remote_timeout, uint16_t min_local_timeout)
```

相关声明：[bt_conn_br_set_sniff_subrating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga910157e30fad972e8c606d1e1645603e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BR／EDR 嗅探子速率参数（Sniff Subrating Parameters）。

<a id="r_ga76f872637f9b34c701c80d71ce7e585c"></a>

```c
int bt_conn_br_get_supervision_timeout (struct bt_conn *conn, uint16_t *timeout)
```

相关声明：[bt_conn_br_get_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga76f872637f9b34c701c80d71ce7e585c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取 BR／EDR 监督超时时间（Supervision Timeout）。

<a id="r_ga8516a5304ec78362ab66a9f18968d20d"></a>

```c
int bt_conn_br_set_supervision_timeout (struct bt_conn *conn, uint16_t timeout)
```

相关声明：[bt_conn_br_set_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8516a5304ec78362ab66a9f18968d20d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 BR／EDR 监督超时时间（Supervision Timeout）。

<a id="r_gae5073b3666aff788f6f389d010a918a6"></a>

```c
int bt_conn_br_change_packet_type (const struct bt_conn *conn, uint16_t packet_type)
```

相关声明：[bt_conn_br_change_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae5073b3666aff788f6f389d010a918a6)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更改 BR／EDR 连接数据包类型（Connection Packet Type）。


## 3.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/bluetooth/direction.h](../api_source_reference/P132_direction.h_源码浏览.md)
- [zephyr/bluetooth/gap.h](../api_source_transport_clock_reference/P016_gap.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
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
- [BT_LE_CONN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga81de567c4c8cb691ef8b02633b42e342)
- [BT_LE_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga940d55c0d84c0cb8f09bc41074ae50d0)
- [BT_LE_CONN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga82df8f439aeb3a156f4238deb085534a)
- [BT_CONN_LE_PHY_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gabca56de0c82c14995738952dafb1fe2d)
- [BT_CONN_LE_PHY_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga39b69f0978f74b5f13f829e908b7cebb)
- [BT_CONN_LE_PHY_PARAM_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3ec555bb4ace5e9c7c13735820fd31de)
- [BT_CONN_LE_PHY_PARAM_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga633126e356658886e9fa3f3217cb4e2c)
- [BT_CONN_LE_PHY_PARAM_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4915244a6cd70995514d6dde1ee0b45f)
- [BT_CONN_LE_PHY_PARAM_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga02c9d7a04ccf2f043293aed7a7f767a7)
- [BT_CONN_LE_DATA_LEN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga98f9dab71897382cf1187259a3b5660e)
- [BT_CONN_LE_DATA_LEN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga102b97de8689fe3fb53f9691009de87f)
- [BT_LE_DATA_LEN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf66746d834f7556dc77659741e27e0c9)
- [BT_LE_DATA_LEN_PARAM_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9cc26afda3c507cb5439184fedcd61ba)
- [BT_CONN_LE_MAX_CONN_INTERVAL_GROUPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gadcb74ad947485dd81dfd59a82d3b0db6)
- [BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL_IFS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gacce78fed479c9d7e9b394488d5e466d7)
- [BT_CONN_LE_FRAME_SPACE_TYPES_MASK_ACL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b9b7d5bd6500ef1195c5da0275247ee)
- [BT_CONN_LE_FRAME_SPACE_TYPES_MASK_CIS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gacdf0d72c8f6dfe6e13c714148f04df3c)
- [BT_CONN_LE_FRAME_SPACE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf01791831e52ee5976679fc0fac9118c)
- [BT_CONN_LE_CS_MODE_MAIN_MODE_PART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5354b9973117f94b88c61fb0ea726a4b)
- [bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)
- [BT_CONN_LE_CS_MODE_SUB_MODE_PART](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga19d2cd20af6f2652164a5677ee8863d5)
- [BT_CONN_INTERVAL_TO_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga707cc62b12c89478aebd0488a464a776)
- [BT_CONN_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0a5fac126005684847ee7509bb98e382)
- [BT_CONN_SCI_INTERVAL_TO_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf4b1395e345f1bf01b83a890bf9a5083)
- [bt_conn_dst_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5e4ec28058d93bede65ccb9d20014e2e)
- [BT_CONN_LE_CREATE_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8ac93a19c34d2821c158f310879fe00d)
- [BT_CONN_LE_CREATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae86425d432078e2ddca260eebc2802f1)
- [BT_CONN_LE_CREATE_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab4203c55c20d83256ca036148c14a00d)
- [BT_CONN_LE_CREATE_CONN_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaaba7c37a5c6e98e7b62ac12bde814d5d)
- [BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3fac32ef426900046d8e38bbd4b7c2d2)
- [BT_CONN_CB_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9227880a1ae5fc373d334171e1450f00)
- [BT_PASSKEY_RAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga988dbb7aea2ac136e3bc8efdf6f7478c)
- [BT_BR_CONN_PARAM_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga986f563bfb741c70fbee39b3948d9d8d)
- [BT_BR_CONN_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6f99f4adfcef36a4d738783921965ca6)
- [BT_BR_CONN_PARAM_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5ccdbff63a430a37a8a8077d8792f706)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [BT_CONN_LE_PHY_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad5786a93b9eecfa5c5092713739cfc98)
- [BT_CONN_LE_PHY_OPT_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaa42e6ff627268b9eef111375d591f9f34)
- [BT_CONN_LE_PHY_OPT_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga08eb37185a763212e65c47ab4c886ecaad1d46128ba2516810af7383e850929e0)
- [bt_conn_le_frame_space_update_initiator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae60f156d2aa01814ad485786e00c4ca7)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7aabb0edb792a8fbfe91f8a8847672b67c)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a9fae7a5909e7c6974361ab71be717495)
- [BT_CONN_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggae60f156d2aa01814ad485786e00c4ca7a8ce5e76ef31654408105b5505f63a4c4)
- [bt_conn_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8dde20ae75b51f1e28dbeed06001f20)
- [BT_CONN_TYPE_LE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)
- [BT_CONN_TYPE_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)
- [BT_CONN_TYPE_SCO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a99c578f145d29b9a7ce1e5d8ca4a8953)
- [BT_CONN_TYPE_ISO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a5fa83a247fcb7bdb19761ab546e790ee)
- [BT_CONN_TYPE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a1bb23b11dc52242911aa6d94947d5836)
- [bt_conn_le_cs_capability_rtt_aa_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gafe14d64a64383b097760764697b035e2)
- [BT_CONN_LE_CS_RTT_AA_ONLY_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a288abc3e9a886eb3ab2b8f32c7913d94)
- [BT_CONN_LE_CS_RTT_AA_ONLY_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2af81e06eb920435cc68ccfa3ee6cee34a)
- [BT_CONN_LE_CS_RTT_AA_ONLY_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggafe14d64a64383b097760764697b035e2a788566d99b00e42f48aceb7d7c0229e6)
- [bt_conn_le_cs_capability_rtt_sounding](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1892ec23ca3b1818287a9d7dafc16433)
- [BT_CONN_LE_CS_RTT_SOUNDING_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a9d4f71899fb3ad7212fe3f544bd55d14)
- [BT_CONN_LE_CS_RTT_SOUNDING_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433aaafb75f1fab71f3f1daee1db96fc44bb)
- [BT_CONN_LE_CS_RTT_SOUNDING_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga1892ec23ca3b1818287a9d7dafc16433a529c39021229684361aeb33251b2c584)
- [bt_conn_le_cs_capability_rtt_random_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5568443825fc1ce9534753d8918aa813)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_NOT_SUPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813acd51ea3eb01cb91c9fda392af42bcd2d)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813ab79f96814227514fe5aeeee21a219741)
- [BT_CONN_LE_CS_RTT_RANDOM_PAYLOAD_150NS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga5568443825fc1ce9534753d8918aa813af50e6d16f23f5b12e41a9c6fce8716db)
- [BT_CONN_LE_CS_MAIN_MODE_1_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a78b56a5342bf31a57de235dddf5e499a)
- [BT_CONN_LE_CS_MAIN_MODE_2_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a8f5842c33912ea291388ae380e54565a)
- [BT_CONN_LE_CS_MAIN_MODE_3_NO_SUB_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a43e2dea6e52df54423bb7a6aaabcbdbf)
- [BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ac4f05c5aea07cfc19a606caebd7201f7)
- [BT_CONN_LE_CS_MAIN_MODE_2_SUB_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156ad6df550b1f4908268752841224bbab26)
- [BT_CONN_LE_CS_MAIN_MODE_3_SUB_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f757b15d1d5006ce2fa6a7a78082156a35b1c587320f31ec1c1bcfe6913c57ac)
- [bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)
- [BT_CONN_LE_CS_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fad3172d9c6319a579ee9923f3d28279f4)
- [BT_CONN_LE_CS_ROLE_REFLECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga0e6f6d4fdbdfc3ed75fef4a95136076fa5fbcf5ba6c42da7deca9f92d6b92c968)
- [bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)
- [BT_CONN_LE_CS_RTT_TYPE_AA_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51aa9b85139381d29cdfb6adb756544e088)
- [BT_CONN_LE_CS_RTT_TYPE_32_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a6350cf2f1d91e496ec49ddd09f7044fc)
- [BT_CONN_LE_CS_RTT_TYPE_96_BIT_SOUNDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a243bb67b834cda207b61cc7ea65bdab2)
- [BT_CONN_LE_CS_RTT_TYPE_32_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ac05977c1622cc7383a1035a63b33ecad)
- [BT_CONN_LE_CS_RTT_TYPE_64_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ae14f994d1c3329695d0257caffd20f91)
- [BT_CONN_LE_CS_RTT_TYPE_96_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51ab0d60b2e7e26ab862df16d926fc2198f)
- [BT_CONN_LE_CS_RTT_TYPE_128_BIT_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaffd6abf9b92cc8d8463797a73b840f51a8edae9d98c26da94ec152fa1f1f690f5)
- [bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)
- [BT_CONN_LE_CS_SYNC_1M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bba4ff9aa9e9c41dbdc288360d354775e95)
- [BT_CONN_LE_CS_SYNC_2M_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaa0fc3809d1d71f4fdfe632ffe0a57cd6)
- [BT_CONN_LE_CS_SYNC_2M_2BT_PHY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaadbf6a4dba28aec90ea07b7da634e1bbaba211d71eb3eccecb93b8e5b4e956e7b)
- [bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)
- [BT_CONN_LE_CS_CHSEL_TYPE_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ac0d5b6a9d1a0c02fce0472b07ec6b0f1)
- [BT_CONN_LE_CS_CHSEL_TYPE_3C](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga34e4837a77c7afd6999095985ddad4f0ab2dde3a39fba7129203fc9afc23a5bd6)
- [bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)
- [BT_CONN_LE_CS_CH3C_SHAPE_HAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba1235210de336af7cac9777d2f91408ea)
- [BT_CONN_LE_CS_CH3C_SHAPE_X](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf2331ec1f1222de51fc4f30566e1c52ba5ddc8d83fa6f143b985bd2f891018622)
- [bt_conn_le_cs_procedure_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9a1dc2010c5237466de87160944630d3)
- [BT_CONN_LE_CS_PROCEDURE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a17689e9502318b16c35a4792ecc6e73f)
- [BT_CONN_LE_CS_PROCEDURE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a295b2e0d0fff2ea730a00e7916065b82)
- [BT_CONN_LE_CS_PROCEDURE_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)
- [bt_conn_le_cs_subevent_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8e54a191b889b1d5ed3e1fbb648d9bc7)
- [BT_CONN_LE_CS_SUBEVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)
- [BT_CONN_LE_CS_SUBEVENT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)
- [bt_conn_le_cs_procedure_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3196a0eb1c7497e93d7c646713d2fc79)
- [BT_CONN_LE_CS_PROCEDURE_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ac1ef74618cb45abd9161cd4d9141570d)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a0a5f18ca51c837f9621d0212997b2ce0)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_TOO_FEW_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79a9aa1742041d4958399bb411982c3bc02)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_CHMAP_INSTANT_PASSED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79af817bbbc221a3615da50e14c14086744)
- [BT_CONN_LE_CS_PROCEDURE_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3196a0eb1c7497e93d7c646713d2fc79ade9e8345ff7946844ba7df3e7379a886)
- [bt_conn_le_cs_subevent_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6394906c6da40c9bebfaeb05de9fd5be)
- [BT_CONN_LE_CS_SUBEVENT_NOT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30b6d4dc4a32556cedd61ed1bbfbf12c)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_REQUESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea938fcb8be6a45efce064c881bc668f8d)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_NO_CS_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabacfa9f390d61d7471c81669bcc0243d)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_SCHED_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5beabaafdce9a596454fe4f23c50afba2ddd)
- [BT_CONN_LE_CS_SUBEVENT_ABORT_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga6394906c6da40c9bebfaeb05de9fd5bea30c5743ef2b358390fd93bd775f72bc3)
- [BT_CONN_ROLE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca865df4804411a07dad18b422a0a41d30)
- [BT_CONN_ROLE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9c54d2e44903cf7c4e5c97e223069dbca586a3966c9400109d9743dd29fa6a7b0)
- [bt_conn_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9442c1479db60e2db40a2ea6de565282)
- [BT_CONN_STATE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a77cbc47923589fac3cf69dff9f900587)
- [BT_CONN_STATE_CONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a34929910cfd74b0fdaed9e6bdf9168bd)
- [BT_CONN_STATE_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282a5bc1bccbc075ac7faa4279878c65298f)
- [BT_CONN_STATE_DISCONNECTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9442c1479db60e2db40a2ea6de565282aba0061089377c6f030449aa2a08a4f9f)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [BT_SECURITY_L0](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a4118114ff442c8f3f43d76f884ee072e)
- [BT_SECURITY_L1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab206382e5417c7513fa57ef43c0b8f1b)
- [BT_SECURITY_L2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783ab41339994f194ae5b56f496e5ad9015a)
- [BT_SECURITY_L3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a5f2688ea3a3dd1c1ffb1df8f01dc3631)
- [BT_SECURITY_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783a199d97cd8f5283114164e673e4f46d81)
- [BT_SECURITY_FORCE_PAIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf0c56cd26c4147f6c9f0faa11fa01783aaef159a9eab5d1cd7a7ed2d3cee30bae)
- [bt_security_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f8712bbf3410de5cbe6ce489fe30e5e)
- [BT_SECURITY_FLAG_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5ead96691877bddebc0d2dc836d36ae53e6)
- [BT_SECURITY_FLAG_OOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga2f8712bbf3410de5cbe6ce489fe30e5eaacd15813b53f635a5ce8485d2aee3198)
- [bt_conn_le_tx_power_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga737d8118f8aba8985292d92d0604b190)
- [BT_CONN_LE_TX_POWER_PHY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a3f8bcd59ef4a1e308761041cd9d8221a)
- [BT_CONN_LE_TX_POWER_PHY_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190adcc75a9e7951316f072c306198364046)
- [BT_CONN_LE_TX_POWER_PHY_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190af38f1c897674b7796e63687c6a3d8800)
- [BT_CONN_LE_TX_POWER_PHY_CODED_S8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190ac916b3e64f99c89b48ff353dfb7f33b2)
- [BT_CONN_LE_TX_POWER_PHY_CODED_S2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga737d8118f8aba8985292d92d0604b190a8b5a5fc8e5a106ef582a0052c2550296)
- [bt_conn_le_path_loss_zone](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf43d7aa3ad1c8d2bde8b04e650fe7b7e)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea17765999979bb1bac00769ea742d53d8)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_MIDDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea06bd101d7cc98d39403ed16719542dec)
- [BT_CONN_LE_PATH_LOSS_ZONE_ENTERED_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea19fd0c4702ca5e08c8cbfb51b34bb705)
- [BT_CONN_LE_PATH_LOSS_ZONE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf43d7aa3ad1c8d2bde8b04e650fe7b7ea684ce653c5fffe9d49316d22904d3942)
- [bt_conn_auth_keypress](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga57465d3a61214531ddaffc2c30939043)
- [BT_CONN_AUTH_KEYPRESS_ENTRY_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c95ea06caee9106d994a4d136682d6)
- [BT_CONN_AUTH_KEYPRESS_DIGIT_ENTERED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a84d4a2d126fbbab1a6b1df82d3e84af1)
- [BT_CONN_AUTH_KEYPRESS_DIGIT_ERASED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043a52fc6b9a44af3e9e1577d8b4b056e529)
- [BT_CONN_AUTH_KEYPRESS_CLEARED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043ac5c181932f18aa64257bb6038324a7da)
- [BT_CONN_AUTH_KEYPRESS_ENTRY_COMPLETED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga57465d3a61214531ddaffc2c30939043adf0bfd84aa161a8c9bf5032b53c7f2a8)
- [BT_CONN_LE_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca0735f5f66af63a389886402d65bc2ee9)
- [BT_CONN_LE_OPT_CODED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bcaa8fb82585ac6b405ffb711ad434ddf3b)
- [BT_CONN_LE_OPT_NO_1M](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga3afc8024ddbcd3bf5a809706e39f74bca8b0037766be752bf60e61385a3f0b9d9)
- [bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)
- [BT_SECURITY_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffac6c961c46cc902106aff62f63f2f8c05)
- [BT_SECURITY_ERR_AUTH_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa8ad3317bf644acf6ddf404a3e1889cd7)
- [BT_SECURITY_ERR_PIN_OR_KEY_MISSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffaa93aba41a30ecc018c8874c428fe3171)
- [BT_SECURITY_ERR_OOB_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa04fbf27abe91464bb9fbf94ec2fa14e7)
- [BT_SECURITY_ERR_AUTH_REQUIREMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa36ae39a9d06da01c069fe2829233ecae)
- [BT_SECURITY_ERR_PAIR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa899c018b2037b41d73959e2ec84a7ca6)
- [BT_SECURITY_ERR_PAIR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffad0cb2a268ee2e8669cbfc4b553c8ec4f)
- [BT_SECURITY_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa55e6e65d1b995dc0cec435597f45a7f5)
- [BT_SECURITY_ERR_KEY_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa508e373e740abeb0135754aabc466216)
- [BT_SECURITY_ERR_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaa9420ff489fd5857ff076406442679ffa52cf38688cd106e31b260381c59fd242)
- [bt_conn_le_cs_procedure_enable_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3653de72793f775e33fd9eb04c3e7a2)
- [BT_CONN_LE_CS_PROCEDURES_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2aa24f08ba114af2ac928087527d514c83)
- [BT_CONN_LE_CS_PROCEDURES_ENABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggaf3653de72793f775e33fd9eb04c3e7a2a35ab078fac9e0ef608ca87c2a3db63ac)
- [bt_conn_le_cs_tone_antenna_config_selection](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab7acdbdf273fc760799cf0d8cf71591c)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca3bdbab03ae31a6340a10066476e9edac)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591caeb8a8776c0e54eada45de6a45f6ee1ea)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A3_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca957116fdc29742ec8e75284bbaa726b7)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A4_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591cabc273bf65c87ff09f72f85e8f0160bb7)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca92ac9a31531c26a23bd1b268e68815ba)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca6908e64a2774e0ddeca4b510ee56de33)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A1_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca9253d001290986ae07a262260a01fafb)
- [BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A2_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab7acdbdf273fc760799cf0d8cf71591ca5745021b56f9da077db312f104e855b2)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_conn_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga060d51eb2208de6f805b1fc0672d2d0c)
- [bt_conn_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b18c6b22a9f02be0d7d078b2ce51ff6)
- [bt_conn_take](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf073384538a67c242b00150904176f66)
- [bt_conn_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf1aeec9b9893450423cf066a6f471824)
- [bt_conn_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga5bdf8e8efc85138d3631dc1efffc3916)
- [bt_conn_lookup_addr_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bfe349efd8a7de31e9457fe439d746a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_conn_get_dst](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga77108581b8f61485ca840e4bf7a17087)
- [bt_conn_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad4aed76b80cc815f748ad0e84ae3d87c)
- [bt_conn_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2de54f2ac83f0d8dca2a85a9fbfadcaa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_conn_is_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf3d55f1f8efc630b495389ced3ee3fa5)
- [bt_conn_get_remote_info](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac4e0bd799fc87b65367129685f57c2bd)
- [bt_conn_le_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa5289154bc508444f68df7abcef18aca)
- [bt_conn_le_enhanced_get_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa79eada87d698f4998af876d03d7e92b)
- [bt_conn_le_get_remote_tx_power_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0843a2e0b6f16ebd132a3a512cfd27a4)
- [bt_conn_le_set_tx_power_report_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa1f38911acee0534a8a6e414018c6fb6)
- [bt_conn_le_set_path_loss_mon_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6be5f3bf064ba03dc2307fdd2b634637)
- [bt_conn_le_set_path_loss_mon_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga90ae27bcc6f71f32be56efe8ecbc165d)
- [bt_conn_le_subrate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac7bb456c530c7e08b4fa9f4d478fdaf9)
- [bt_conn_le_subrate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga754ed218fe9577f2d0ef6d508cfc5a0b)
- [bt_conn_le_read_min_conn_interval_groups](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e7e836d94a5330ae01e14dbd3e29f14)
- [bt_conn_le_read_min_conn_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9af26600acdf5b3a8b8ea0a32e14b497)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn_le_conn_rate_set_defaults](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac9b111639f9b982cd97e13f313e51461)
- [bt_conn_le_conn_rate_request](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2e4188482deeda71f8e5d42a07538f31)
- [bt_conn_le_read_all_remote_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac0dbbdb95ef868f35006622932dc8901)
- [bt_conn_le_frame_space_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab734fbc307eff3c5bddf7c5e6ddd341b)
- [bt_conn_le_param_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab44a964725f54ed2d37de17c6e2fd3eb)
- [bt_conn_le_data_len_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8a2006f6e34b20c7e8ef65a73f431a57)
- [bt_conn_le_phy_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae13ed81b1e7928f44b8fdf85995b3e58)
- [bt_conn_le_set_default_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga7c8e7a7616e7b56f97da7ff4bc0fc7ba)
- [bt_conn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga14e7c852b0271781594e742ae509c5d3)
- [bt_conn_le_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8d66f3e0262a51279e9fa8b3139252e6)
- [bt_conn_le_create_synced](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga98f99c893e444d1ad1ecd9139803c0b1)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_conn_le_create_auto](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaecfaf2cb44772511dbb585de8f76f09b)
- [bt_conn_create_auto_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga62dc2663b4fa39a33adb76dc9a136aa4)
- [bt_conn_set_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae001f1268e1ff42c3c974c95dcb6735d)
- [bt_conn_get_security](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4b43ef0f30146808e560991a302e88ad)
- [bt_conn_enc_key_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaff3e6aa16b68e5da7dab53289295545e)
- [bt_conn_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9b79cd44734c1e560d6f30509be4d0b)
- [bt_conn_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad2f90b34390e3c3697fd455ae4ef5f31)
- [bt_security_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga327444a6987b8e0b573fe758d2f75886)
- [bt_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga014db594b17a3b5d7d954e64ad8de759)
- [bt_get_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0c84d5597a71fe38788a88063fd19a2d)
- [bt_conn_set_bondable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4165819d12dd96e00dfa2fd6f4b95669)
- [bt_le_oob_set_sc_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gad02f8fe587efd543c0c81cace3f63d63)
- [bt_le_oob_set_legacy_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga978770d46d7c8af854a61261c14cb892)
- [bt_le_oob_set_legacy_tk](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0f889983cfabafe826b4feb6899b95ba)
- [bt_le_oob_set_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac365f9748ad0737f09142ee1de982503)
- [bt_le_oob_sc_data](../bluetooth_connection_model_reference/P111_bt_le_oob_sc_data_结构体.md)
- [bt_le_oob_get_sc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga096552403b5bcd0107f69eded772b1ee)
- [bt_conn_auth_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1bf13d2dfdbdf0a72f9b1c759ef23f60)
- [bt_conn_auth_cb_overlay](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga81077385583d71c248a1eb6aab9ee86e)
- [bt_conn_auth_info_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac6684a8089ebd495b539d661cf9fd13f)
- [bt_conn_auth_info_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac73a60b8b6b569b84fe17f707fa33f37)
- [bt_conn_auth_passkey_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3906d8d3d192e8a6ad1bf6b7acc32ff0)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bt_conn_auth_keypress_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2987a902da4f5cfe3671c60d154ced7e)
- [bt_conn_auth_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga89e5fc4bcab3f5598d20a9cd8ace5f59)
- [bt_conn_auth_passkey_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab8c3ecf2a3d68e54379917844a29d995)
- [bt_conn_auth_pairing_confirm](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3e15b9deb6787d3e415bbea35c9aa91d)
- [bt_conn_auth_pincode_entry](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga4002a1b092832807218afa8ad279ab98)
- [bt_conn_create_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf7849f332386f8903d35d6904f6c82b9)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [bt_conn_lookup_addr_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga11ae1b656683cebe9db6a53e5166ad7a)
- [bt_conn_get_dst_br](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga1b02a1ce8e48ad483d73d1efd803618c)
- [bt_conn_br_switch_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3a7741f1e884168168a09e9ec5f28c49)
- [bt_conn_br_set_role_switch_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab6c2073091d1d08032c51aadb904ea3f)
- [bt_conn_br_enter_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga641f7f4ce7fe0641948a798881ecedcb)
- [bt_conn_br_exit_sniff_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab1aedad7da2eecc6c30acbfcdf9fbfec)
- [bt_conn_br_set_sniff_subrating](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga910157e30fad972e8c606d1e1645603e)
- [bt_conn_br_get_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga76f872637f9b34c701c80d71ce7e585c)
- [bt_conn_br_set_supervision_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8516a5304ec78362ab66a9f18968d20d)
- [bt_conn_br_change_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae5073b3666aff788f6f389d010a918a6)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__pinctrl__ch32v20x_30x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__i3c.h_文件参考.md)
