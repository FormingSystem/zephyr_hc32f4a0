---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-5
title: zephyr__bluetooth__hci_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_hci\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
#include <zephyr/types.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Fsco_5Fhdr"></a>

```c
struct bt_hci_sco_hdr
```

相关声明：[bt_hci_sco_hdr](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fhdr"></a>

```c
struct bt_hci_evt_hdr
```

相关声明：[bt_hci_evt_hdr](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Facl_5Fhdr"></a>

```c
struct bt_hci_acl_hdr
```

相关声明：[bt_hci_acl_hdr](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fiso_5Fsdu_5Fhdr"></a>

```c
struct bt_hci_iso_sdu_hdr
```

相关声明：[bt_hci_iso_sdu_hdr](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fiso_5Fsdu_5Fts_5Fhdr"></a>

```c
struct bt_hci_iso_sdu_ts_hdr
```

相关声明：[bt_hci_iso_sdu_ts_hdr](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fiso_5Fhdr"></a>

```c
struct bt_hci_iso_hdr
```

相关声明：[bt_hci_iso_hdr](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fcmd_5Fhdr"></a>

```c
struct bt_hci_cmd_hdr
```

相关声明：[bt_hci_cmd_hdr](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md)。

<a id="r_bt_5Fhci_5Fop_5Finquiry"></a>

```c
struct bt_hci_op_inquiry
```

相关声明：[bt_hci_op_inquiry](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fconnect"></a>

```c
struct bt_hci_cp_connect
```

相关声明：[bt_hci_cp_connect](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fdisconnect"></a>

```c
struct bt_hci_cp_disconnect
```

相关声明：[bt_hci_cp_disconnect](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fconnect_5Fcancel"></a>

```c
struct bt_hci_cp_connect_cancel
```

相关声明：[bt_hci_cp_connect_cancel](../bluetooth_hci_model_reference/P014_bt_hci_cp_connect_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fconnect_5Fcancel"></a>

```c
struct bt_hci_rp_connect_cancel
```

相关声明：[bt_hci_rp_connect_cancel](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Faccept_5Fconn_5Freq"></a>

```c
struct bt_hci_cp_accept_conn_req
```

相关声明：[bt_hci_cp_accept_conn_req](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fsetup_5Fsync_5Fconn"></a>

```c
struct bt_hci_cp_setup_sync_conn
```

相关声明：[bt_hci_cp_setup_sync_conn](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Faccept_5Fsync_5Fconn_5Freq"></a>

```c
struct bt_hci_cp_accept_sync_conn_req
```

相关声明：[bt_hci_cp_accept_sync_conn_req](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Freject_5Fconn_5Freq"></a>

```c
struct bt_hci_cp_reject_conn_req
```

相关声明：[bt_hci_cp_reject_conn_req](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Flink_5Fkey_5Freply"></a>

```c
struct bt_hci_cp_link_key_reply
```

相关声明：[bt_hci_cp_link_key_reply](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Flink_5Fkey_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_link_key_neg_reply
```

相关声明：[bt_hci_cp_link_key_neg_reply](../bluetooth_hci_model_reference/P139_bt_hci_cp_link_key_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fpin_5Fcode_5Freply"></a>

```c
struct bt_hci_cp_pin_code_reply
```

相关声明：[bt_hci_cp_pin_code_reply](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fpin_5Fcode_5Freply"></a>

```c
struct bt_hci_rp_pin_code_reply
```

相关声明：[bt_hci_rp_pin_code_reply](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fpin_5Fcode_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_pin_code_neg_reply
```

相关声明：[bt_hci_cp_pin_code_neg_reply](../bluetooth_hci_model_reference/P147_bt_hci_cp_pin_code_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fpin_5Fcode_5Fneg_5Freply"></a>

```c
struct bt_hci_rp_pin_code_neg_reply
```

相关声明：[bt_hci_rp_pin_code_neg_reply](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fchange_5Fconn_5Fpacket_5Ftype"></a>

```c
struct bt_hci_cp_change_conn_packet_type
```

相关声明：[bt_hci_cp_change_conn_packet_type](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md)。

主机控制器接口（Host Controller Interface，HCI）的更改连接包类型（Change Connection Packet Type）命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fauth_5Frequested"></a>

```c
struct bt_hci_cp_auth_requested
```

相关声明：[bt_hci_cp_auth_requested](../bluetooth_hci_model_reference/P009_bt_hci_cp_auth_requested_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fset_5Fconn_5Fencrypt"></a>

```c
struct bt_hci_cp_set_conn_encrypt
```

相关声明：[bt_hci_cp_set_conn_encrypt](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fremote_5Fname_5Frequest"></a>

```c
struct bt_hci_cp_remote_name_request
```

相关声明：[bt_hci_cp_remote_name_request](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fremote_5Fname_5Fcancel"></a>

```c
struct bt_hci_cp_remote_name_cancel
```

相关声明：[bt_hci_cp_remote_name_cancel](../bluetooth_hci_model_reference/P162_bt_hci_cp_remote_name_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fremote_5Fname_5Fcancel"></a>

```c
struct bt_hci_rp_remote_name_cancel
```

相关声明：[bt_hci_rp_remote_name_cancel](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fremote_5Ffeatures"></a>

```c
struct bt_hci_cp_read_remote_features
```

相关声明：[bt_hci_cp_read_remote_features](../bluetooth_hci_model_reference/P157_bt_hci_cp_read_remote_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fremote_5Fext_5Ffeatures"></a>

```c
struct bt_hci_cp_read_remote_ext_features
```

相关声明：[bt_hci_cp_read_remote_ext_features](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fremote_5Fversion_5Finfo"></a>

```c
struct bt_hci_cp_read_remote_version_info
```

相关声明：[bt_hci_cp_read_remote_version_info](../bluetooth_hci_model_reference/P158_bt_hci_cp_read_remote_version_info_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fio_5Fcapability_5Freply"></a>

```c
struct bt_hci_cp_io_capability_reply
```

相关声明：[bt_hci_cp_io_capability_reply](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fuser_5Fconfirm_5Freply"></a>

```c
struct bt_hci_cp_user_confirm_reply
```

相关声明：[bt_hci_cp_user_confirm_reply](../bluetooth_hci_model_reference/P172_bt_hci_cp_user_confirm_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fuser_5Fconfirm_5Freply"></a>

```c
struct bt_hci_rp_user_confirm_reply
```

相关声明：[bt_hci_rp_user_confirm_reply](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fuser_5Fpasskey_5Freply"></a>

```c
struct bt_hci_cp_user_passkey_reply
```

相关声明：[bt_hci_cp_user_passkey_reply](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fuser_5Fpasskey_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_user_passkey_neg_reply
```

相关声明：[bt_hci_cp_user_passkey_neg_reply](../bluetooth_hci_model_reference/P173_bt_hci_cp_user_passkey_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fio_5Fcapability_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_io_capability_neg_reply
```

相关声明：[bt_hci_cp_io_capability_neg_reply](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fswitch_5Frole"></a>

```c
struct bt_hci_cp_switch_role
```

相关声明：[bt_hci_cp_switch_role](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Flink_5Fpolicy_5Fsettings"></a>

```c
struct bt_hci_cp_read_link_policy_settings
```

相关声明：[bt_hci_cp_read_link_policy_settings](../bluetooth_hci_model_reference/P153_bt_hci_cp_read_link_policy_settings_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Flink_5Fpolicy_5Fsettings"></a>

```c
struct bt_hci_rp_read_link_policy_settings
```

相关声明：[bt_hci_rp_read_link_policy_settings](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Flink_5Fpolicy_5Fsettings"></a>

```c
struct bt_hci_cp_write_link_policy_settings
```

相关声明：[bt_hci_cp_write_link_policy_settings](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fdefault_5Flink_5Fpolicy_5Fsettings"></a>

```c
struct bt_hci_rp_read_default_link_policy_settings
```

相关声明：[bt_hci_rp_read_default_link_policy_settings](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fdefault_5Flink_5Fpolicy_5Fsettings"></a>

```c
struct bt_hci_cp_write_default_link_policy_settings
```

相关声明：[bt_hci_cp_write_default_link_policy_settings](../bluetooth_hci_model_reference/P188_bt_hci_cp_write_default_link_policy_settings_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fsniff_5Fmode"></a>

```c
struct bt_hci_cp_sniff_mode
```

相关声明：[bt_hci_cp_sniff_mode](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fexit_5Fsniff_5Fmode"></a>

```c
struct bt_hci_cp_exit_sniff_mode
```

相关声明：[bt_hci_cp_exit_sniff_mode](../bluetooth_hci_model_reference/P016_bt_hci_cp_exit_sniff_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fsniff_5Fsubrating"></a>

```c
struct bt_hci_cp_sniff_subrating
```

相关声明：[bt_hci_cp_sniff_subrating](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md)。

HCI 嗅探子速率（Sniff Subrating）命令参数。

<a id="r_bt_5Fhci_5Frp_5Fsniff_5Fsubrating"></a>

```c
struct bt_hci_rp_sniff_subrating
```

相关声明：[bt_hci_rp_sniff_subrating](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md)。

HCI 嗅探子速率（Sniff Subrating）返回参数。

<a id="r_bt_5Fhci_5Fcp_5Fset_5Fevent_5Fmask"></a>

```c
struct bt_hci_cp_set_event_mask
```

相关声明：[bt_hci_cp_set_event_mask](../bluetooth_hci_model_reference/P166_bt_hci_cp_set_event_mask_结构体.md)。

<a id="r_bt_5Fhci_5Fwrite_5Flocal_5Fname"></a>

```c
struct bt_hci_write_local_name
```

相关声明：[bt_hci_write_local_name](../bluetooth_hci_model_reference/P450_bt_hci_write_local_name_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fconn_5Faccept_5Ftimeout"></a>

```c
struct bt_hci_rp_read_conn_accept_timeout
```

相关声明：[bt_hci_rp_read_conn_accept_timeout](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fconn_5Faccept_5Ftimeout"></a>

```c
struct bt_hci_cp_write_conn_accept_timeout
```

相关声明：[bt_hci_cp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P186_bt_hci_cp_write_conn_accept_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fwrite_5Fconn_5Faccept_5Ftimeout"></a>

```c
struct bt_hci_rp_write_conn_accept_timeout
```

相关声明：[bt_hci_rp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P435_bt_hci_rp_write_conn_accept_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fpage_5Fscan_5Factivity"></a>

```c
struct bt_hci_cp_write_page_scan_activity
```

相关声明：[bt_hci_cp_write_page_scan_activity](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md)。

写入寻呼扫描活动参数（Write Page Scan Activity）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Finquiry_5Fscan_5Factivity"></a>

```c
struct bt_hci_cp_write_inquiry_scan_activity
```

相关声明：[bt_hci_cp_write_inquiry_scan_activity](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md)。

写入查询扫描活动参数（Write Inquiry Scan Activity）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fclass_5Fof_5Fdevice"></a>

```c
struct bt_hci_rp_read_class_of_device
```

相关声明：[bt_hci_rp_read_class_of_device](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fclass_5Fof_5Fdevice"></a>

```c
struct bt_hci_cp_write_class_of_device
```

相关声明：[bt_hci_cp_write_class_of_device](../bluetooth_hci_model_reference/P185_bt_hci_cp_write_class_of_device_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_cp_read_tx_power_level
```

相关声明：[bt_hci_cp_read_tx_power_level](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_rp_read_tx_power_level
```

相关声明：[bt_hci_rp_read_tx_power_level](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_cp_le_read_tx_power_level
```

相关声明：[bt_hci_cp_le_read_tx_power_level](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_rp_le_read_tx_power_level
```

相关声明：[bt_hci_rp_le_read_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Ftx_5Fpower_5Freport_5Fenable"></a>

```c
struct bt_hci_cp_le_set_tx_power_report_enable
```

相关声明：[bt_hci_cp_le_set_tx_power_report_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpath_5Floss_5Freporting_5Fparameters"></a>

```c
struct bt_hci_cp_le_set_path_loss_reporting_parameters
```

相关声明：[bt_hci_cp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fpath_5Floss_5Freporting_5Fparameters"></a>

```c
struct bt_hci_rp_le_set_path_loss_reporting_parameters
```

相关声明：[bt_hci_rp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpath_5Floss_5Freporting_5Fenable"></a>

```c
struct bt_hci_cp_le_set_path_loss_reporting_enable
```

相关声明：[bt_hci_cp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fpath_5Floss_5Freporting_5Fenable"></a>

```c
struct bt_hci_rp_le_set_path_loss_reporting_enable
```

相关声明：[bt_hci_rp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fdefault_5Fsubrate"></a>

```c
struct bt_hci_cp_le_set_default_subrate
```

相关声明：[bt_hci_cp_le_set_default_subrate](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fsubrate_5Frequest"></a>

```c
struct bt_hci_cp_le_subrate_request
```

相关声明：[bt_hci_cp_le_subrate_request](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fset_5Fctl_5Fto_5Fhost_5Fflow"></a>

```c
struct bt_hci_cp_set_ctl_to_host_flow
```

相关声明：[bt_hci_cp_set_ctl_to_host_flow](../bluetooth_hci_model_reference/P165_bt_hci_cp_set_ctl_to_host_flow_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fhost_5Fbuffer_5Fsize"></a>

```c
struct bt_hci_cp_host_buffer_size
```

相关声明：[bt_hci_cp_host_buffer_size](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md)。

<a id="r_bt_5Fhci_5Fhandle_5Fcount"></a>

```c
struct bt_hci_handle_count
```

相关声明：[bt_hci_handle_count](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fhost_5Fnum_5Fcompleted_5Fpackets"></a>

```c
struct bt_hci_cp_host_num_completed_packets
```

相关声明：[bt_hci_cp_host_num_completed_packets](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Flink_5Fsupervision_5Ftimeout"></a>

```c
struct bt_hci_cp_read_link_supervision_timeout
```

相关声明：[bt_hci_cp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P154_bt_hci_cp_read_link_supervision_timeout_结构体.md)。

读取链路监督超时（Read Link Supervision Timeout）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Frp_5Fread_5Flink_5Fsupervision_5Ftimeout"></a>

```c
struct bt_hci_rp_read_link_supervision_timeout
```

相关声明：[bt_hci_rp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md)。

读取链路监督超时（Read Link Supervision Timeout）的 HCI 响应参数。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Flink_5Fsupervision_5Ftimeout"></a>

```c
struct bt_hci_cp_write_link_supervision_timeout
```

相关声明：[bt_hci_cp_write_link_supervision_timeout](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md)。

写入链路监督超时（Write Link Supervision Timeout）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fiac_5Flap"></a>

```c
struct bt_hci_iac_lap
```

相关声明：[bt_hci_iac_lap](../bluetooth_hci_model_reference/P311_bt_hci_iac_lap_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fcurrent_5Fiac_5Flap"></a>

```c
struct bt_hci_cp_write_current_iac_lap
```

相关声明：[bt_hci_cp_write_current_iac_lap](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Finquiry_5Fscan_5Ftype"></a>

```c
struct bt_hci_cp_write_inquiry_scan_type
```

相关声明：[bt_hci_cp_write_inquiry_scan_type](../bluetooth_hci_model_reference/P192_bt_hci_cp_write_inquiry_scan_type_结构体.md)。

写入查询扫描类型（Write Inquiry Scan Type）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Finquiry_5Fmode"></a>

```c
struct bt_hci_cp_write_inquiry_mode
```

相关声明：[bt_hci_cp_write_inquiry_mode](../bluetooth_hci_model_reference/P190_bt_hci_cp_write_inquiry_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fpage_5Fscan_5Ftype"></a>

```c
struct bt_hci_cp_write_page_scan_type
```

相关声明：[bt_hci_cp_write_page_scan_type](../bluetooth_hci_model_reference/P197_bt_hci_cp_write_page_scan_type_结构体.md)。

写入寻呼扫描类型（Write Page Scan Type）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fext_5Finquiry_5Fresponse"></a>

```c
struct bt_hci_cp_write_ext_inquiry_response
```

相关声明：[bt_hci_cp_write_ext_inquiry_response](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md)。

写入扩展查询响应（Write Extended Inquiry Response）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fssp_5Fmode"></a>

```c
struct bt_hci_cp_write_ssp_mode
```

相关声明：[bt_hci_cp_write_ssp_mode](../bluetooth_hci_model_reference/P199_bt_hci_cp_write_ssp_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fset_5Fevent_5Fmask_5Fpage_5F2"></a>

```c
struct bt_hci_cp_set_event_mask_page_2
```

相关声明：[bt_hci_cp_set_event_mask_page_2](../bluetooth_hci_model_reference/P167_bt_hci_cp_set_event_mask_page_2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fle_5Fhost_5Fsupp"></a>

```c
struct bt_hci_cp_write_le_host_supp
```

相关声明：[bt_hci_cp_write_le_host_supp](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fsc_5Fhost_5Fsupp"></a>

```c
struct bt_hci_cp_write_sc_host_supp
```

相关声明：[bt_hci_cp_write_sc_host_supp](../bluetooth_hci_model_reference/P198_bt_hci_cp_write_sc_host_supp_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fauth_5Fpayload_5Ftimeout"></a>

```c
struct bt_hci_cp_read_auth_payload_timeout
```

相关声明：[bt_hci_cp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P149_bt_hci_cp_read_auth_payload_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fauth_5Fpayload_5Ftimeout"></a>

```c
struct bt_hci_rp_read_auth_payload_timeout
```

相关声明：[bt_hci_rp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fwrite_5Fauth_5Fpayload_5Ftimeout"></a>

```c
struct bt_hci_cp_write_auth_payload_timeout
```

相关声明：[bt_hci_cp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fwrite_5Fauth_5Fpayload_5Ftimeout"></a>

```c
struct bt_hci_rp_write_auth_payload_timeout
```

相关声明：[bt_hci_rp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fconfigure_5Fdata_5Fpath"></a>

```c
struct bt_hci_cp_configure_data_path
```

相关声明：[bt_hci_cp_configure_data_path](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fconfigure_5Fdata_5Fpath"></a>

```c
struct bt_hci_rp_configure_data_path
```

相关声明：[bt_hci_rp_configure_data_path](../bluetooth_hci_model_reference/P334_bt_hci_rp_configure_data_path_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Flocal_5Fversion_5Finfo"></a>

```c
struct bt_hci_rp_read_local_version_info
```

相关声明：[bt_hci_rp_read_local_version_info](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fsupported_5Fcommands"></a>

```c
struct bt_hci_rp_read_supported_commands
```

相关声明：[bt_hci_rp_read_supported_commands](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Flocal_5Fext_5Ffeatures"></a>

```c
struct bt_hci_cp_read_local_ext_features
```

相关声明：[bt_hci_cp_read_local_ext_features](../bluetooth_hci_model_reference/P155_bt_hci_cp_read_local_ext_features_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Flocal_5Fext_5Ffeatures"></a>

```c
struct bt_hci_rp_read_local_ext_features
```

相关声明：[bt_hci_rp_read_local_ext_features](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Flocal_5Ffeatures"></a>

```c
struct bt_hci_rp_read_local_features
```

相关声明：[bt_hci_rp_read_local_features](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fbuffer_5Fsize"></a>

```c
struct bt_hci_rp_read_buffer_size
```

相关声明：[bt_hci_rp_read_buffer_size](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fbd_5Faddr"></a>

```c
struct bt_hci_rp_read_bd_addr
```

相关声明：[bt_hci_rp_read_bd_addr](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md)。

<a id="r_bt_5Fhci_5Fstd_5Fcodec_5Finfo"></a>

```c
struct bt_hci_std_codec_info
```

相关声明：[bt_hci_std_codec_info](../bluetooth_hci_model_reference/P438_bt_hci_std_codec_info_结构体.md)。

<a id="r_bt_5Fhci_5Fstd_5Fcodecs"></a>

```c
struct bt_hci_std_codecs
```

相关声明：[bt_hci_std_codecs](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fcodec_5Finfo"></a>

```c
struct bt_hci_vs_codec_info
```

相关声明：[bt_hci_vs_codec_info](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fcodecs"></a>

```c
struct bt_hci_vs_codecs
```

相关声明：[bt_hci_vs_codecs](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fcodecs"></a>

```c
struct bt_hci_rp_read_codecs
```

相关声明：[bt_hci_rp_read_codecs](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md)。

<a id="r_bt_5Fhci_5Fstd_5Fcodec_5Finfo_5Fv2"></a>

```c
struct bt_hci_std_codec_info_v2
```

相关声明：[bt_hci_std_codec_info_v2](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fstd_5Fcodecs_5Fv2"></a>

```c
struct bt_hci_std_codecs_v2
```

相关声明：[bt_hci_std_codecs_v2](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fcodec_5Finfo_5Fv2"></a>

```c
struct bt_hci_vs_codec_info_v2
```

相关声明：[bt_hci_vs_codec_info_v2](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fcodecs_5Fv2"></a>

```c
struct bt_hci_vs_codecs_v2
```

相关声明：[bt_hci_vs_codecs_v2](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fcodecs_5Fv2"></a>

```c
struct bt_hci_rp_read_codecs_v2
```

相关声明：[bt_hci_rp_read_codecs_v2](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fcodec_5Fid"></a>

```c
struct bt_hci_cp_codec_id
```

相关声明：[bt_hci_cp_codec_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fcodec_5Fcapabilities"></a>

```c
struct bt_hci_cp_read_codec_capabilities
```

相关声明：[bt_hci_cp_read_codec_capabilities](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md)。

<a id="r_bt_5Fhci_5Fcodec_5Fcapability_5Finfo"></a>

```c
struct bt_hci_codec_capability_info
```

相关声明：[bt_hci_codec_capability_info](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fcodec_5Fcapabilities"></a>

```c
struct bt_hci_rp_read_codec_capabilities
```

相关声明：[bt_hci_rp_read_codec_capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fctlr_5Fdelay"></a>

```c
struct bt_hci_cp_read_ctlr_delay
```

相关声明：[bt_hci_cp_read_ctlr_delay](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fctlr_5Fdelay"></a>

```c
struct bt_hci_rp_read_ctlr_delay
```

相关声明：[bt_hci_rp_read_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Frssi"></a>

```c
struct bt_hci_cp_read_rssi
```

相关声明：[bt_hci_cp_read_rssi](../bluetooth_hci_model_reference/P159_bt_hci_cp_read_rssi_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Frssi"></a>

```c
struct bt_hci_rp_read_rssi
```

相关声明：[bt_hci_rp_read_rssi](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fread_5Fencryption_5Fkey_5Fsize"></a>

```c
struct bt_hci_cp_read_encryption_key_size
```

相关声明：[bt_hci_cp_read_encryption_key_size](../bluetooth_hci_model_reference/P152_bt_hci_cp_read_encryption_key_size_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fread_5Fencryption_5Fkey_5Fsize"></a>

```c
struct bt_hci_rp_read_encryption_key_size
```

相关声明：[bt_hci_rp_read_encryption_key_size](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fevent_5Fmask"></a>

```c
struct bt_hci_cp_le_set_event_mask
```

相关声明：[bt_hci_cp_le_set_event_mask](../bluetooth_hci_model_reference/P096_bt_hci_cp_le_set_event_mask_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fbuffer_5Fsize"></a>

```c
struct bt_hci_rp_le_read_buffer_size
```

相关声明：[bt_hci_rp_le_read_buffer_size](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Flocal_5Ffeatures"></a>

```c
struct bt_hci_rp_le_read_local_features
```

相关声明：[bt_hci_rp_le_read_local_features](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Frandom_5Faddress"></a>

```c
struct bt_hci_cp_le_set_random_address
```

相关声明：[bt_hci_cp_le_set_random_address](../bluetooth_hci_model_reference/P120_bt_hci_cp_le_set_random_address_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fadv_5Fparam"></a>

```c
struct bt_hci_cp_le_set_adv_param
```

相关声明：[bt_hci_cp_le_set_adv_param](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fchan_5Ftx_5Fpower"></a>

```c
struct bt_hci_rp_le_read_chan_tx_power
```

相关声明：[bt_hci_rp_le_read_chan_tx_power](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fadv_5Fdata"></a>

```c
struct bt_hci_cp_le_set_adv_data
```

相关声明：[bt_hci_cp_le_set_adv_data](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fscan_5Frsp_5Fdata"></a>

```c
struct bt_hci_cp_le_set_scan_rsp_data
```

相关声明：[bt_hci_cp_le_set_scan_rsp_data](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fadv_5Fenable"></a>

```c
struct bt_hci_cp_le_set_adv_enable
```

相关声明：[bt_hci_cp_le_set_adv_enable](../bluetooth_hci_model_reference/P083_bt_hci_cp_le_set_adv_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fscan_5Fparam"></a>

```c
struct bt_hci_cp_le_set_scan_param
```

相关声明：[bt_hci_cp_le_set_scan_param](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fscan_5Fenable"></a>

```c
struct bt_hci_cp_le_set_scan_enable
```

相关声明：[bt_hci_cp_le_set_scan_enable](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcreate_5Fconn"></a>

```c
struct bt_hci_cp_le_create_conn
```

相关声明：[bt_hci_cp_le_create_conn](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Ffal_5Fsize"></a>

```c
struct bt_hci_rp_le_read_fal_size
```

相关声明：[bt_hci_rp_le_read_fal_size](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fadd_5Fdev_5Fto_5Ffal"></a>

```c
struct bt_hci_cp_le_add_dev_to_fal
```

相关声明：[bt_hci_cp_le_add_dev_to_fal](../bluetooth_hci_model_reference/P022_bt_hci_cp_le_add_dev_to_fal_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Frem_5Fdev_5Ffrom_5Ffal"></a>

```c
struct bt_hci_cp_le_rem_dev_from_fal
```

相关声明：[bt_hci_cp_le_rem_dev_from_fal](../bluetooth_hci_model_reference/P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md)。

<a id="r_hci_5Fcp_5Fle_5Fconn_5Fupdate"></a>

```c
struct hci_cp_le_conn_update
```

相关声明：[hci_cp_le_conn_update](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fhost_5Fchan_5Fclassif"></a>

```c
struct bt_hci_cp_le_set_host_chan_classif
```

相关声明：[bt_hci_cp_le_set_host_chan_classif](../bluetooth_hci_model_reference/P104_bt_hci_cp_le_set_host_chan_classif_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fchan_5Fmap"></a>

```c
struct bt_hci_cp_le_read_chan_map
```

相关声明：[bt_hci_cp_le_read_chan_map](../bluetooth_hci_model_reference/P059_bt_hci_cp_le_read_chan_map_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fchan_5Fmap"></a>

```c
struct bt_hci_rp_le_read_chan_map
```

相关声明：[bt_hci_rp_le_read_chan_map](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fremote_5Ffeatures"></a>

```c
struct bt_hci_cp_le_read_remote_features
```

相关声明：[bt_hci_cp_le_read_remote_features](../bluetooth_hci_model_reference/P066_bt_hci_cp_le_read_remote_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fencrypt"></a>

```c
struct bt_hci_cp_le_encrypt
```

相关声明：[bt_hci_cp_le_encrypt](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fencrypt"></a>

```c
struct bt_hci_rp_le_encrypt
```

相关声明：[bt_hci_rp_le_encrypt](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Frand"></a>

```c
struct bt_hci_rp_le_rand
```

相关声明：[bt_hci_rp_le_rand](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fstart_5Fencryption"></a>

```c
struct bt_hci_cp_le_start_encryption
```

相关声明：[bt_hci_cp_le_start_encryption](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fltk_5Freq_5Freply"></a>

```c
struct bt_hci_cp_le_ltk_req_reply
```

相关声明：[bt_hci_cp_le_ltk_req_reply](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fltk_5Freq_5Freply"></a>

```c
struct bt_hci_rp_le_ltk_req_reply
```

相关声明：[bt_hci_rp_le_ltk_req_reply](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fltk_5Freq_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_le_ltk_req_neg_reply
```

相关声明：[bt_hci_cp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P050_bt_hci_cp_le_ltk_req_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fltk_5Freq_5Fneg_5Freply"></a>

```c
struct bt_hci_rp_le_ltk_req_neg_reply
```

相关声明：[bt_hci_rp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fsupp_5Fstates"></a>

```c
struct bt_hci_rp_le_read_supp_states
```

相关声明：[bt_hci_rp_le_read_supp_states](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Frx_5Ftest"></a>

```c
struct bt_hci_cp_le_rx_test
```

相关声明：[bt_hci_cp_le_rx_test](../bluetooth_hci_model_reference/P078_bt_hci_cp_le_rx_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Ftx_5Ftest"></a>

```c
struct bt_hci_cp_le_tx_test
```

相关声明：[bt_hci_cp_le_tx_test](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Ftest_5Fend"></a>

```c
struct bt_hci_rp_le_test_end
```

相关声明：[bt_hci_rp_le_test_end](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fconn_5Fparam_5Freq_5Freply"></a>

```c
struct bt_hci_cp_le_conn_param_req_reply
```

相关声明：[bt_hci_cp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fconn_5Fparam_5Freq_5Freply"></a>

```c
struct bt_hci_rp_le_conn_param_req_reply
```

相关声明：[bt_hci_rp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fconn_5Fparam_5Freq_5Fneg_5Freply"></a>

```c
struct bt_hci_cp_le_conn_param_req_neg_reply
```

相关声明：[bt_hci_cp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fconn_5Fparam_5Freq_5Fneg_5Freply"></a>

```c
struct bt_hci_rp_le_conn_param_req_neg_reply
```

相关声明：[bt_hci_rp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fdata_5Flen"></a>

```c
struct bt_hci_cp_le_set_data_len
```

相关声明：[bt_hci_cp_le_set_data_len](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fdata_5Flen"></a>

```c
struct bt_hci_rp_le_set_data_len
```

相关声明：[bt_hci_rp_le_set_data_len](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fdefault_5Fdata_5Flen"></a>

```c
struct bt_hci_rp_le_read_default_data_len
```

相关声明：[bt_hci_rp_le_read_default_data_len](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fwrite_5Fdefault_5Fdata_5Flen"></a>

```c
struct bt_hci_cp_le_write_default_data_len
```

相关声明：[bt_hci_cp_le_write_default_data_len](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fgenerate_5Fdhkey"></a>

```c
struct bt_hci_cp_le_generate_dhkey
```

相关声明：[bt_hci_cp_le_generate_dhkey](../bluetooth_hci_model_reference/P045_bt_hci_cp_le_generate_dhkey_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fgenerate_5Fdhkey_5Fv2"></a>

```c
struct bt_hci_cp_le_generate_dhkey_v2
```

相关声明：[bt_hci_cp_le_generate_dhkey_v2](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fadd_5Fdev_5Fto_5Frl"></a>

```c
struct bt_hci_cp_le_add_dev_to_rl
```

相关声明：[bt_hci_cp_le_add_dev_to_rl](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Frem_5Fdev_5Ffrom_5Frl"></a>

```c
struct bt_hci_cp_le_rem_dev_from_rl
```

相关声明：[bt_hci_cp_le_rem_dev_from_rl](../bluetooth_hci_model_reference/P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Frl_5Fsize"></a>

```c
struct bt_hci_rp_le_read_rl_size
```

相关声明：[bt_hci_rp_le_read_rl_size](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fpeer_5Frpa"></a>

```c
struct bt_hci_cp_le_read_peer_rpa
```

相关声明：[bt_hci_cp_le_read_peer_rpa](../bluetooth_hci_model_reference/P063_bt_hci_cp_le_read_peer_rpa_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fpeer_5Frpa"></a>

```c
struct bt_hci_rp_le_read_peer_rpa
```

相关声明：[bt_hci_rp_le_read_peer_rpa](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Flocal_5Frpa"></a>

```c
struct bt_hci_cp_le_read_local_rpa
```

相关声明：[bt_hci_cp_le_read_local_rpa](../bluetooth_hci_model_reference/P062_bt_hci_cp_le_read_local_rpa_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Flocal_5Frpa"></a>

```c
struct bt_hci_rp_le_read_local_rpa
```

相关声明：[bt_hci_rp_le_read_local_rpa](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Faddr_5Fres_5Fenable"></a>

```c
struct bt_hci_cp_le_set_addr_res_enable
```

相关声明：[bt_hci_cp_le_set_addr_res_enable](../bluetooth_hci_model_reference/P081_bt_hci_cp_le_set_addr_res_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Frpa_5Ftimeout"></a>

```c
struct bt_hci_cp_le_set_rpa_timeout
```

相关声明：[bt_hci_cp_le_set_rpa_timeout](../bluetooth_hci_model_reference/P121_bt_hci_cp_le_set_rpa_timeout_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fmax_5Fdata_5Flen"></a>

```c
struct bt_hci_rp_le_read_max_data_len
```

相关声明：[bt_hci_rp_le_read_max_data_len](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fphy"></a>

```c
struct bt_hci_cp_le_read_phy
```

相关声明：[bt_hci_cp_le_read_phy](../bluetooth_hci_model_reference/P064_bt_hci_cp_le_read_phy_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fphy"></a>

```c
struct bt_hci_rp_le_read_phy
```

相关声明：[bt_hci_rp_le_read_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fdefault_5Fphy"></a>

```c
struct bt_hci_cp_le_set_default_phy
```

相关声明：[bt_hci_cp_le_set_default_phy](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fphy"></a>

```c
struct bt_hci_cp_le_set_phy
```

相关声明：[bt_hci_cp_le_set_phy](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fenh_5Frx_5Ftest"></a>

```c
struct bt_hci_cp_le_enh_rx_test
```

相关声明：[bt_hci_cp_le_enh_rx_test](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fenh_5Ftx_5Ftest"></a>

```c
struct bt_hci_cp_le_enh_tx_test
```

相关声明：[bt_hci_cp_le_enh_tx_test](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fadv_5Fset_5Frandom_5Faddr"></a>

```c
struct bt_hci_cp_le_set_adv_set_random_addr
```

相关声明：[bt_hci_cp_le_set_adv_set_random_addr](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fadv_5Fparam"></a>

```c
struct bt_hci_cp_le_set_ext_adv_param
```

相关声明：[bt_hci_cp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fext_5Fadv_5Fparam"></a>

```c
struct bt_hci_rp_le_set_ext_adv_param
```

相关声明：[bt_hci_rp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fadv_5Fparam_5Fv2"></a>

```c
struct bt_hci_cp_le_set_ext_adv_param_v2
```

相关声明：[bt_hci_cp_le_set_ext_adv_param_v2](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fadv_5Fdata"></a>

```c
struct bt_hci_cp_le_set_ext_adv_data
```

相关声明：[bt_hci_cp_le_set_ext_adv_data](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fscan_5Frsp_5Fdata"></a>

```c
struct bt_hci_cp_le_set_ext_scan_rsp_data
```

相关声明：[bt_hci_cp_le_set_ext_scan_rsp_data](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md)。

<a id="r_bt_5Fhci_5Fext_5Fadv_5Fset"></a>

```c
struct bt_hci_ext_adv_set
```

相关声明：[bt_hci_ext_adv_set](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fadv_5Fenable"></a>

```c
struct bt_hci_cp_le_set_ext_adv_enable
```

相关声明：[bt_hci_cp_le_set_ext_adv_enable](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fmax_5Fadv_5Fdata_5Flen"></a>

```c
struct bt_hci_rp_le_read_max_adv_data_len
```

相关声明：[bt_hci_rp_le_read_max_adv_data_len](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fnum_5Fadv_5Fsets"></a>

```c
struct bt_hci_rp_le_read_num_adv_sets
```

相关声明：[bt_hci_rp_le_read_num_adv_sets](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fremove_5Fadv_5Fset"></a>

```c
struct bt_hci_cp_le_remove_adv_set
```

相关声明：[bt_hci_cp_le_remove_adv_set](../bluetooth_hci_model_reference/P074_bt_hci_cp_le_remove_adv_set_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fper_5Fadv_5Fparam"></a>

```c
struct bt_hci_cp_le_set_per_adv_param
```

相关声明：[bt_hci_cp_le_set_per_adv_param](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fper_5Fadv_5Fdata"></a>

```c
struct bt_hci_cp_le_set_per_adv_data
```

相关声明：[bt_hci_cp_le_set_per_adv_data](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fper_5Fadv_5Fenable"></a>

```c
struct bt_hci_cp_le_set_per_adv_enable
```

相关声明：[bt_hci_cp_le_set_per_adv_enable](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fext_5Fscan_5Fphy"></a>

```c
struct bt_hci_ext_scan_phy
```

相关声明：[bt_hci_ext_scan_phy](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fscan_5Fparam"></a>

```c
struct bt_hci_cp_le_set_ext_scan_param
```

相关声明：[bt_hci_cp_le_set_ext_scan_param](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fext_5Fscan_5Fenable"></a>

```c
struct bt_hci_cp_le_set_ext_scan_enable
```

相关声明：[bt_hci_cp_le_set_ext_scan_enable](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fext_5Fconn_5Fphy"></a>

```c
struct bt_hci_ext_conn_phy
```

相关声明：[bt_hci_ext_conn_phy](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fext_5Fcreate_5Fconn"></a>

```c
struct bt_hci_cp_le_ext_create_conn
```

相关声明：[bt_hci_cp_le_ext_create_conn](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fext_5Fcreate_5Fconn_5Fv2"></a>

```c
struct bt_hci_cp_le_ext_create_conn_v2
```

相关声明：[bt_hci_cp_le_ext_create_conn_v2](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpawr_5Fsubevent_5Fdata_5Felement"></a>

```c
struct bt_hci_cp_le_set_pawr_subevent_data_element
```

相关声明：[bt_hci_cp_le_set_pawr_subevent_data_element](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpawr_5Fsubevent_5Fdata"></a>

```c
struct bt_hci_cp_le_set_pawr_subevent_data
```

相关声明：[bt_hci_cp_le_set_pawr_subevent_data](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpawr_5Fresponse_5Fdata"></a>

```c
struct bt_hci_cp_le_set_pawr_response_data
```

相关声明：[bt_hci_cp_le_set_pawr_response_data](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fpawr_5Fsync_5Fsubevent"></a>

```c
struct bt_hci_cp_le_set_pawr_sync_subevent
```

相关声明：[bt_hci_cp_le_set_pawr_sync_subevent](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fper_5Fadv_5Fparam_5Fv2"></a>

```c
struct bt_hci_cp_le_set_per_adv_param_v2
```

相关声明：[bt_hci_cp_le_set_per_adv_param_v2](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fper_5Fadv_5Fcreate_5Fsync"></a>

```c
struct bt_hci_cp_le_per_adv_create_sync
```

相关声明：[bt_hci_cp_le_per_adv_create_sync](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fper_5Fadv_5Fterminate_5Fsync"></a>

```c
struct bt_hci_cp_le_per_adv_terminate_sync
```

相关声明：[bt_hci_cp_le_per_adv_terminate_sync](../bluetooth_hci_model_reference/P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fadd_5Fdev_5Fto_5Fper_5Fadv_5Flist"></a>

```c
struct bt_hci_cp_le_add_dev_to_per_adv_list
```

相关声明：[bt_hci_cp_le_add_dev_to_per_adv_list](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Frem_5Fdev_5Ffrom_5Fper_5Fadv_5Flist"></a>

```c
struct bt_hci_cp_le_rem_dev_from_per_adv_list
```

相关声明：[bt_hci_cp_le_rem_dev_from_per_adv_list](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fper_5Fadv_5Flist_5Fsize"></a>

```c
struct bt_hci_rp_le_read_per_adv_list_size
```

相关声明：[bt_hci_rp_le_read_per_adv_list_size](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Ftx_5Fpower"></a>

```c
struct bt_hci_rp_le_read_tx_power
```

相关声明：[bt_hci_rp_le_read_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Frf_5Fpath_5Fcomp"></a>

```c
struct bt_hci_rp_le_read_rf_path_comp
```

相关声明：[bt_hci_rp_le_read_rf_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fwrite_5Frf_5Fpath_5Fcomp"></a>

```c
struct bt_hci_cp_le_write_rf_path_comp
```

相关声明：[bt_hci_cp_le_write_rf_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fprivacy_5Fmode"></a>

```c
struct bt_hci_cp_le_set_privacy_mode
```

相关声明：[bt_hci_cp_le_set_privacy_mode](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Frx_5Ftest_5Fv3"></a>

```c
struct bt_hci_cp_le_rx_test_v3
```

相关声明：[bt_hci_cp_le_rx_test_v3](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Ftx_5Ftest_5Fv3"></a>

```c
struct bt_hci_cp_le_tx_test_v3
```

相关声明：[bt_hci_cp_le_tx_test_v3](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fcl_5Fcte_5Ftx_5Fparams"></a>

```c
struct bt_hci_cp_le_set_cl_cte_tx_params
```

相关声明：[bt_hci_cp_le_set_cl_cte_tx_params](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fcl_5Fcte_5Ftx_5Fenable"></a>

```c
struct bt_hci_cp_le_set_cl_cte_tx_enable
```

相关声明：[bt_hci_cp_le_set_cl_cte_tx_enable](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fcl_5Fcte_5Fsampling_5Fenable"></a>

```c
struct bt_hci_cp_le_set_cl_cte_sampling_enable
```

相关声明：[bt_hci_cp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fcl_5Fcte_5Fsampling_5Fenable"></a>

```c
struct bt_hci_rp_le_set_cl_cte_sampling_enable
```

相关声明：[bt_hci_rp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fconn_5Fcte_5Frx_5Fparams"></a>

```c
struct bt_hci_cp_le_set_conn_cte_rx_params
```

相关声明：[bt_hci_cp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fconn_5Fcte_5Frx_5Fparams"></a>

```c
struct bt_hci_rp_le_set_conn_cte_rx_params
```

相关声明：[bt_hci_rp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fconn_5Fcte_5Ftx_5Fparams"></a>

```c
struct bt_hci_cp_le_set_conn_cte_tx_params
```

相关声明：[bt_hci_cp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fconn_5Fcte_5Ftx_5Fparams"></a>

```c
struct bt_hci_rp_le_set_conn_cte_tx_params
```

相关声明：[bt_hci_rp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fconn_5Fcte_5Freq_5Fenable"></a>

```c
struct bt_hci_cp_le_conn_cte_req_enable
```

相关声明：[bt_hci_cp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fconn_5Fcte_5Freq_5Fenable"></a>

```c
struct bt_hci_rp_le_conn_cte_req_enable
```

相关声明：[bt_hci_rp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fconn_5Fcte_5Frsp_5Fenable"></a>

```c
struct bt_hci_cp_le_conn_cte_rsp_enable
```

相关声明：[bt_hci_cp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fconn_5Fcte_5Frsp_5Fenable"></a>

```c
struct bt_hci_rp_le_conn_cte_rsp_enable
```

相关声明：[bt_hci_rp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fant_5Finfo"></a>

```c
struct bt_hci_rp_le_read_ant_info
```

相关声明：[bt_hci_rp_le_read_ant_info](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fper_5Fadv_5Frecv_5Fenable"></a>

```c
struct bt_hci_cp_le_set_per_adv_recv_enable
```

相关声明：[bt_hci_cp_le_set_per_adv_recv_enable](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fper_5Fadv_5Fsync_5Ftransfer"></a>

```c
struct bt_hci_cp_le_per_adv_sync_transfer
```

相关声明：[bt_hci_cp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fper_5Fadv_5Fsync_5Ftransfer"></a>

```c
struct bt_hci_rp_le_per_adv_sync_transfer
```

相关声明：[bt_hci_rp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fper_5Fadv_5Fset_5Finfo_5Ftransfer"></a>

```c
struct bt_hci_cp_le_per_adv_set_info_transfer
```

相关声明：[bt_hci_cp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fper_5Fadv_5Fset_5Finfo_5Ftransfer"></a>

```c
struct bt_hci_rp_le_per_adv_set_info_transfer
```

相关声明：[bt_hci_rp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fpast_5Fparam"></a>

```c
struct bt_hci_cp_le_past_param
```

相关声明：[bt_hci_cp_le_past_param](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fpast_5Fparam"></a>

```c
struct bt_hci_rp_le_past_param
```

相关声明：[bt_hci_rp_le_past_param](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fdefault_5Fpast_5Fparam"></a>

```c
struct bt_hci_cp_le_default_past_param
```

相关声明：[bt_hci_cp_le_default_past_param](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fdefault_5Fpast_5Fparam"></a>

```c
struct bt_hci_rp_le_default_past_param
```

相关声明：[bt_hci_rp_le_default_past_param](../bluetooth_hci_model_reference/P341_bt_hci_rp_le_default_past_param_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fbuffer_5Fsize_5Fv2"></a>

```c
struct bt_hci_rp_le_read_buffer_size_v2
```

相关声明：[bt_hci_rp_le_read_buffer_size_v2](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fiso_5Ftx_5Fsync"></a>

```c
struct bt_hci_cp_le_read_iso_tx_sync
```

相关声明：[bt_hci_cp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fiso_5Ftx_5Fsync"></a>

```c
struct bt_hci_rp_le_read_iso_tx_sync
```

相关声明：[bt_hci_rp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md)。

<a id="r_bt_5Fhci_5Fcis_5Fparams"></a>

```c
struct bt_hci_cis_params
```

相关声明：[bt_hci_cis_params](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fcig_5Fparams"></a>

```c
struct bt_hci_cp_le_set_cig_params
```

相关声明：[bt_hci_cp_le_set_cig_params](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fcig_5Fparams"></a>

```c
struct bt_hci_rp_le_set_cig_params
```

相关声明：[bt_hci_rp_le_set_cig_params](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md)。

<a id="r_bt_5Fhci_5Fcis_5Fparams_5Ftest"></a>

```c
struct bt_hci_cis_params_test
```

相关声明：[bt_hci_cis_params_test](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fcig_5Fparams_5Ftest"></a>

```c
struct bt_hci_cp_le_set_cig_params_test
```

相关声明：[bt_hci_cp_le_set_cig_params_test](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fcig_5Fparams_5Ftest"></a>

```c
struct bt_hci_rp_le_set_cig_params_test
```

相关声明：[bt_hci_rp_le_set_cig_params_test](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcis"></a>

```c
struct bt_hci_cis
```

相关声明：[bt_hci_cis](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcreate_5Fcis"></a>

```c
struct bt_hci_cp_le_create_cis
```

相关声明：[bt_hci_cp_le_create_cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fremove_5Fcig"></a>

```c
struct bt_hci_cp_le_remove_cig
```

相关声明：[bt_hci_cp_le_remove_cig](../bluetooth_hci_model_reference/P075_bt_hci_cp_le_remove_cig_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fremove_5Fcig"></a>

```c
struct bt_hci_rp_le_remove_cig
```

相关声明：[bt_hci_rp_le_remove_cig](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Faccept_5Fcis"></a>

```c
struct bt_hci_cp_le_accept_cis
```

相关声明：[bt_hci_cp_le_accept_cis](../bluetooth_hci_model_reference/P021_bt_hci_cp_le_accept_cis_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Freject_5Fcis"></a>

```c
struct bt_hci_cp_le_reject_cis
```

相关声明：[bt_hci_cp_le_reject_cis](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Freject_5Fcis"></a>

```c
struct bt_hci_rp_le_reject_cis
```

相关声明：[bt_hci_rp_le_reject_cis](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcreate_5Fbig"></a>

```c
struct bt_hci_cp_le_create_big
```

相关声明：[bt_hci_cp_le_create_big](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcreate_5Fbig_5Ftest"></a>

```c
struct bt_hci_cp_le_create_big_test
```

相关声明：[bt_hci_cp_le_create_big_test](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fterminate_5Fbig"></a>

```c
struct bt_hci_cp_le_terminate_big
```

相关声明：[bt_hci_cp_le_terminate_big](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fbig_5Fcreate_5Fsync"></a>

```c
struct bt_hci_cp_le_big_create_sync
```

相关声明：[bt_hci_cp_le_big_create_sync](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fbig_5Fterminate_5Fsync"></a>

```c
struct bt_hci_cp_le_big_terminate_sync
```

相关声明：[bt_hci_cp_le_big_terminate_sync](../bluetooth_hci_model_reference/P026_bt_hci_cp_le_big_terminate_sync_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fbig_5Fterminate_5Fsync"></a>

```c
struct bt_hci_rp_le_big_terminate_sync
```

相关声明：[bt_hci_rp_le_big_terminate_sync](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Freq_5Fpeer_5Fsca"></a>

```c
struct bt_hci_cp_le_req_peer_sca
```

相关声明：[bt_hci_cp_le_req_peer_sca](../bluetooth_hci_model_reference/P077_bt_hci_cp_le_req_peer_sca_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fsetup_5Fiso_5Fpath"></a>

```c
struct bt_hci_cp_le_setup_iso_path
```

相关声明：[bt_hci_cp_le_setup_iso_path](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fsetup_5Fiso_5Fpath"></a>

```c
struct bt_hci_rp_le_setup_iso_path
```

相关声明：[bt_hci_rp_le_setup_iso_path](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fremove_5Fiso_5Fpath"></a>

```c
struct bt_hci_cp_le_remove_iso_path
```

相关声明：[bt_hci_cp_le_remove_iso_path](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fremove_5Fiso_5Fpath"></a>

```c
struct bt_hci_rp_le_remove_iso_path
```

相关声明：[bt_hci_rp_le_remove_iso_path](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fiso_5Ftransmit_5Ftest"></a>

```c
struct bt_hci_cp_le_iso_transmit_test
```

相关声明：[bt_hci_cp_le_iso_transmit_test](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fiso_5Ftransmit_5Ftest"></a>

```c
struct bt_hci_rp_le_iso_transmit_test
```

相关声明：[bt_hci_rp_le_iso_transmit_test](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fiso_5Freceive_5Ftest"></a>

```c
struct bt_hci_cp_le_iso_receive_test
```

相关声明：[bt_hci_cp_le_iso_receive_test](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fiso_5Freceive_5Ftest"></a>

```c
struct bt_hci_rp_le_iso_receive_test
```

相关声明：[bt_hci_rp_le_iso_receive_test](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Ftest_5Fcounters"></a>

```c
struct bt_hci_cp_le_read_test_counters
```

相关声明：[bt_hci_cp_le_read_test_counters](../bluetooth_hci_model_reference/P068_bt_hci_cp_le_read_test_counters_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Ftest_5Fcounters"></a>

```c
struct bt_hci_rp_le_read_test_counters
```

相关声明：[bt_hci_rp_le_read_test_counters](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fiso_5Ftest_5Fend"></a>

```c
struct bt_hci_cp_le_iso_test_end
```

相关声明：[bt_hci_cp_le_iso_test_end](../bluetooth_hci_model_reference/P048_bt_hci_cp_le_iso_test_end_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fiso_5Ftest_5Fend"></a>

```c
struct bt_hci_rp_le_iso_test_end
```

相关声明：[bt_hci_rp_le_iso_test_end](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fhost_5Ffeature"></a>

```c
struct bt_hci_cp_le_set_host_feature
```

相关声明：[bt_hci_cp_le_set_host_feature](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fset_5Fhost_5Ffeature"></a>

```c
struct bt_hci_rp_le_set_host_feature
```

相关声明：[bt_hci_rp_le_set_host_feature](../bluetooth_hci_model_reference/P388_bt_hci_rp_le_set_host_feature_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fiso_5Flink_5Fquality"></a>

```c
struct bt_hci_cp_le_read_iso_link_quality
```

相关声明：[bt_hci_cp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P060_bt_hci_cp_le_read_iso_link_quality_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fiso_5Flink_5Fquality"></a>

```c
struct bt_hci_rp_le_read_iso_link_quality
```

相关声明：[bt_hci_rp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Ftx_5Ftest_5Fv4"></a>

```c
struct bt_hci_cp_le_tx_test_v4
```

相关声明：[bt_hci_cp_le_tx_test_v4](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Fall_5Flocal_5Fsupported_5Ffeatures"></a>

```c
struct bt_hci_rp_le_read_all_local_supported_features
```

相关声明：[bt_hci_rp_le_read_all_local_supported_features](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fall_5Fremote_5Ffeatures"></a>

```c
struct bt_hci_cp_le_read_all_remote_features
```

相关声明：[bt_hci_cp_le_read_all_remote_features](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Ftx_5Ftest_5Fv4_5Ftx_5Fpower"></a>

```c
struct bt_hci_cp_le_tx_test_v4_tx_power
```

相关声明：[bt_hci_cp_le_tx_test_v4_tx_power](../bluetooth_hci_model_reference/P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Flocal_5Fsupported_5Fcapabilities"></a>

```c
struct bt_hci_rp_le_read_local_supported_capabilities
```

相关声明：[bt_hci_rp_le_read_local_supported_capabilities](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fle_5Fread_5Flocal_5Fsupported_5Fcapabilities_5Fv2"></a>

```c
struct bt_hci_rp_le_read_local_supported_capabilities_v2
```

相关声明：[bt_hci_rp_le_read_local_supported_capabilities_v2](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md)。

低功耗读取本地支持能力（LE Read Local Supported Capabilities，v2）命令的 HCI 响应参数。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fremote_5Fsupported_5Fcapabilities"></a>

```c
struct bt_hci_cp_le_read_remote_supported_capabilities
```

相关声明：[bt_hci_cp_le_read_remote_supported_capabilities](../bluetooth_hci_model_reference/P067_bt_hci_cp_le_read_remote_supported_capabilities_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fwrite_5Fcached_5Fremote_5Fsupported_5Fcapabilities"></a>

```c
struct bt_hci_cp_le_write_cached_remote_supported_capabilities
```

相关声明：[bt_hci_cp_le_write_cached_remote_supported_capabilities](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fwrite_5Fcached_5Fremote_5Fsupported_5Fcapabilities_5Fv2"></a>

```c
struct bt_hci_cp_le_write_cached_remote_supported_capabilities_v2
```

相关声明：[bt_hci_cp_le_write_cached_remote_supported_capabilities_v2](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md)。

低功耗信道探测写入已缓存远端支持能力（LE CS Write Cached Remote Supported Capabilities，v2）的 HCI 命令参数。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fsecurity_5Fenable"></a>

```c
struct bt_hci_cp_le_security_enable
```

相关声明：[bt_hci_cp_le_security_enable](../bluetooth_hci_model_reference/P080_bt_hci_cp_le_security_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcs_5Fset_5Fdefault_5Fsettings"></a>

```c
struct bt_hci_cp_le_cs_set_default_settings
```

相关声明：[bt_hci_cp_le_cs_set_default_settings](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fread_5Fremote_5Ffae_5Ftable"></a>

```c
struct bt_hci_cp_le_read_remote_fae_table
```

相关声明：[bt_hci_cp_le_read_remote_fae_table](../bluetooth_hci_model_reference/P065_bt_hci_cp_le_read_remote_fae_table_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fwrite_5Fcached_5Fremote_5Ffae_5Ftable"></a>

```c
struct bt_hci_cp_le_write_cached_remote_fae_table
```

相关声明：[bt_hci_cp_le_write_cached_remote_fae_table](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fset_5Fprocedure_5Fparameters"></a>

```c
struct bt_hci_cp_le_set_procedure_parameters
```

相关声明：[bt_hci_cp_le_set_procedure_parameters](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fprocedure_5Fenable"></a>

```c
struct bt_hci_cp_le_procedure_enable
```

相关声明：[bt_hci_cp_le_procedure_enable](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md)。

<a id="r_bt_5Fhci_5Fop_5Fle_5Fcs_5Ftest"></a>

```c
struct bt_hci_op_le_cs_test
```

相关声明：[bt_hci_op_le_cs_test](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcs_5Fcreate_5Fconfig"></a>

```c
struct bt_hci_cp_le_cs_create_config
```

相关声明：[bt_hci_cp_le_cs_create_config](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fcs_5Fremove_5Fconfig"></a>

```c
struct bt_hci_cp_le_cs_remove_config
```

相关声明：[bt_hci_cp_le_cs_remove_config](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fle_5Fframe_5Fspace_5Fupdate"></a>

```c
struct bt_hci_cp_le_frame_space_update
```

相关声明：[bt_hci_cp_le_frame_space_update](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md)。

<a id="r_bt_5Fhci_5Fle_5Fread_5Fmin_5Fsupported_5Fconn_5Finterval_5Fgroup"></a>

```c
struct bt_hci_le_read_min_supported_conn_interval_group
```

相关声明：[bt_hci_le_read_min_supported_conn_interval_group](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md)。

<a id="r_bt_5Fhci_5Fop_5Fle_5Fread_5Fmin_5Fsupported_5Fconn_5Finterval"></a>

```c
struct bt_hci_op_le_read_min_supported_conn_interval
```

相关声明：[bt_hci_op_le_read_min_supported_conn_interval](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md)。

<a id="r_bt_5Fhci_5Fop_5Fle_5Fset_5Fdefault_5Frate_5Fparameters"></a>

```c
struct bt_hci_op_le_set_default_rate_parameters
```

相关声明：[bt_hci_op_le_set_default_rate_parameters](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md)。

<a id="r_bt_5Fhci_5Fop_5Fle_5Fconnection_5Frate_5Frequest"></a>

```c
struct bt_hci_op_le_connection_rate_request
```

相关声明：[bt_hci_op_le_connection_rate_request](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Finquiry_5Fcomplete"></a>

```c
struct bt_hci_evt_inquiry_complete
```

相关声明：[bt_hci_evt_inquiry_complete](../bluetooth_hci_model_reference/P218_bt_hci_evt_inquiry_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fconn_5Fcomplete"></a>

```c
struct bt_hci_evt_conn_complete
```

相关声明：[bt_hci_evt_conn_complete](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fconn_5Frequest"></a>

```c
struct bt_hci_evt_conn_request
```

相关声明：[bt_hci_evt_conn_request](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fdisconn_5Fcomplete"></a>

```c
struct bt_hci_evt_disconn_complete
```

相关声明：[bt_hci_evt_disconn_complete](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fauth_5Fcomplete"></a>

```c
struct bt_hci_evt_auth_complete
```

相关声明：[bt_hci_evt_auth_complete](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fremote_5Fname_5Freq_5Fcomplete"></a>

```c
struct bt_hci_evt_remote_name_req_complete
```

相关声明：[bt_hci_evt_remote_name_req_complete](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fencrypt_5Fchange"></a>

```c
struct bt_hci_evt_encrypt_change
```

相关声明：[bt_hci_evt_encrypt_change](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fremote_5Ffeatures"></a>

```c
struct bt_hci_evt_remote_features
```

相关声明：[bt_hci_evt_remote_features](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fremote_5Fversion_5Finfo"></a>

```c
struct bt_hci_evt_remote_version_info
```

相关声明：[bt_hci_evt_remote_version_info](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fcmd_5Fcomplete"></a>

```c
struct bt_hci_evt_cmd_complete
```

相关声明：[bt_hci_evt_cmd_complete](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fcc_5Fstatus"></a>

```c
struct bt_hci_evt_cc_status
```

相关声明：[bt_hci_evt_cc_status](../bluetooth_hci_model_reference/P205_bt_hci_evt_cc_status_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fcmd_5Fstatus"></a>

```c
struct bt_hci_evt_cmd_status
```

相关声明：[bt_hci_evt_cmd_status](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fhardware_5Ferror"></a>

```c
struct bt_hci_evt_hardware_error
```

相关声明：[bt_hci_evt_hardware_error](../bluetooth_hci_model_reference/P216_bt_hci_evt_hardware_error_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Frole_5Fchange"></a>

```c
struct bt_hci_evt_role_change
```

相关声明：[bt_hci_evt_role_change](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fnum_5Fcompleted_5Fpackets"></a>

```c
struct bt_hci_evt_num_completed_packets
```

相关声明：[bt_hci_evt_num_completed_packets](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fmode_5Fchange"></a>

```c
struct bt_hci_evt_mode_change
```

相关声明：[bt_hci_evt_mode_change](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fpin_5Fcode_5Freq"></a>

```c
struct bt_hci_evt_pin_code_req
```

相关声明：[bt_hci_evt_pin_code_req](../bluetooth_hci_model_reference/P289_bt_hci_evt_pin_code_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Flink_5Fkey_5Freq"></a>

```c
struct bt_hci_evt_link_key_req
```

相关声明：[bt_hci_evt_link_key_req](../bluetooth_hci_model_reference/P282_bt_hci_evt_link_key_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Flink_5Fkey_5Fnotify"></a>

```c
struct bt_hci_evt_link_key_notify
```

相关声明：[bt_hci_evt_link_key_notify](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fdata_5Fbuf_5Foverflow"></a>

```c
struct bt_hci_evt_data_buf_overflow
```

相关声明：[bt_hci_evt_data_buf_overflow](../bluetooth_hci_model_reference/P211_bt_hci_evt_data_buf_overflow_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fconn_5Fpkt_5Ftype_5Fchanged"></a>

```c
struct bt_hci_evt_conn_pkt_type_changed
```

相关声明：[bt_hci_evt_conn_pkt_type_changed](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md)。

HCI 连接包类型已变化（Connection Packet Type Changed）事件参数。

<a id="r_bt_5Fhci_5Fevt_5Finquiry_5Fresult_5Fwith_5Frssi"></a>

```c
struct bt_hci_evt_inquiry_result_with_rssi
```

相关声明：[bt_hci_evt_inquiry_result_with_rssi](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fremote_5Fext_5Ffeatures"></a>

```c
struct bt_hci_evt_remote_ext_features
```

相关声明：[bt_hci_evt_remote_ext_features](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fsync_5Festablished_5Fv2"></a>

```c
struct bt_hci_evt_le_per_adv_sync_established_v2
```

相关声明：[bt_hci_evt_le_per_adv_sync_established_v2](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadvertising_5Freport_5Fv2"></a>

```c
struct bt_hci_evt_le_per_advertising_report_v2
```

相关声明：[bt_hci_evt_le_per_advertising_report_v2](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fpast_5Freceived_5Fv2"></a>

```c
struct bt_hci_evt_le_past_received_v2
```

相关声明：[bt_hci_evt_le_past_received_v2](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fsubevent_5Fdata_5Frequest"></a>

```c
struct bt_hci_evt_le_per_adv_subevent_data_request
```

相关声明：[bt_hci_evt_le_per_adv_subevent_data_request](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fresponse"></a>

```c
struct bt_hci_evt_le_per_adv_response
```

相关声明：[bt_hci_evt_le_per_adv_response](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fresponse_5Freport"></a>

```c
struct bt_hci_evt_le_per_adv_response_report
```

相关声明：[bt_hci_evt_le_per_adv_response_report](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fenh_5Fconn_5Fcomplete_5Fv2"></a>

```c
struct bt_hci_evt_le_enh_conn_complete_v2
```

相关声明：[bt_hci_evt_le_enh_conn_complete_v2](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fsync_5Fconn_5Fcomplete"></a>

```c
struct bt_hci_evt_sync_conn_complete
```

相关声明：[bt_hci_evt_sync_conn_complete](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fextended_5Finquiry_5Fresult"></a>

```c
struct bt_hci_evt_extended_inquiry_result
```

相关声明：[bt_hci_evt_extended_inquiry_result](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fencrypt_5Fkey_5Frefresh_5Fcomplete"></a>

```c
struct bt_hci_evt_encrypt_key_refresh_complete
```

相关声明：[bt_hci_evt_encrypt_key_refresh_complete](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fio_5Fcapa_5Freq"></a>

```c
struct bt_hci_evt_io_capa_req
```

相关声明：[bt_hci_evt_io_capa_req](../bluetooth_hci_model_reference/P220_bt_hci_evt_io_capa_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fio_5Fcapa_5Fresp"></a>

```c
struct bt_hci_evt_io_capa_resp
```

相关声明：[bt_hci_evt_io_capa_resp](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fuser_5Fconfirm_5Freq"></a>

```c
struct bt_hci_evt_user_confirm_req
```

相关声明：[bt_hci_evt_user_confirm_req](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fuser_5Fpasskey_5Freq"></a>

```c
struct bt_hci_evt_user_passkey_req
```

相关声明：[bt_hci_evt_user_passkey_req](../bluetooth_hci_model_reference/P299_bt_hci_evt_user_passkey_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fssp_5Fcomplete"></a>

```c
struct bt_hci_evt_ssp_complete
```

相关声明：[bt_hci_evt_ssp_complete](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fuser_5Fpasskey_5Fnotify"></a>

```c
struct bt_hci_evt_user_passkey_notify
```

相关声明：[bt_hci_evt_user_passkey_notify](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fmeta_5Fevent"></a>

```c
struct bt_hci_evt_le_meta_event
```

相关声明：[bt_hci_evt_le_meta_event](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fauth_5Fpayload_5Ftimeout_5Fexp"></a>

```c
struct bt_hci_evt_auth_payload_timeout_exp
```

相关声明：[bt_hci_evt_auth_payload_timeout_exp](../bluetooth_hci_model_reference/P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconn_5Fcomplete"></a>

```c
struct bt_hci_evt_le_conn_complete
```

相关声明：[bt_hci_evt_le_conn_complete](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fadvertising_5Finfo"></a>

```c
struct bt_hci_evt_le_advertising_info
```

相关声明：[bt_hci_evt_le_advertising_info](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fadvertising_5Freport"></a>

```c
struct bt_hci_evt_le_advertising_report
```

相关声明：[bt_hci_evt_le_advertising_report](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconn_5Fupdate_5Fcomplete"></a>

```c
struct bt_hci_evt_le_conn_update_complete
```

相关声明：[bt_hci_evt_le_conn_update_complete](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fremote_5Ffeat_5Fcomplete"></a>

```c
struct bt_hci_evt_le_remote_feat_complete
```

相关声明：[bt_hci_evt_le_remote_feat_complete](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fltk_5Frequest"></a>

```c
struct bt_hci_evt_le_ltk_request
```

相关声明：[bt_hci_evt_le_ltk_request](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconn_5Fparam_5Freq"></a>

```c
struct bt_hci_evt_le_conn_param_req
```

相关声明：[bt_hci_evt_le_conn_param_req](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fdata_5Flen_5Fchange"></a>

```c
struct bt_hci_evt_le_data_len_change
```

相关声明：[bt_hci_evt_le_data_len_change](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fp256_5Fpublic_5Fkey_5Fcomplete"></a>

```c
struct bt_hci_evt_le_p256_public_key_complete
```

相关声明：[bt_hci_evt_le_p256_public_key_complete](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fgenerate_5Fdhkey_5Fcomplete"></a>

```c
struct bt_hci_evt_le_generate_dhkey_complete
```

相关声明：[bt_hci_evt_le_generate_dhkey_complete](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fenh_5Fconn_5Fcomplete"></a>

```c
struct bt_hci_evt_le_enh_conn_complete
```

相关声明：[bt_hci_evt_le_enh_conn_complete](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fdirect_5Fadv_5Finfo"></a>

```c
struct bt_hci_evt_le_direct_adv_info
```

相关声明：[bt_hci_evt_le_direct_adv_info](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fdirect_5Fadv_5Freport"></a>

```c
struct bt_hci_evt_le_direct_adv_report
```

相关声明：[bt_hci_evt_le_direct_adv_report](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fphy_5Fupdate_5Fcomplete"></a>

```c
struct bt_hci_evt_le_phy_update_complete
```

相关声明：[bt_hci_evt_le_phy_update_complete](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fext_5Fadvertising_5Finfo"></a>

```c
struct bt_hci_evt_le_ext_advertising_info
```

相关声明：[bt_hci_evt_le_ext_advertising_info](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fext_5Fadvertising_5Freport"></a>

```c
struct bt_hci_evt_le_ext_advertising_report
```

相关声明：[bt_hci_evt_le_ext_advertising_report](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fsync_5Festablished"></a>

```c
struct bt_hci_evt_le_per_adv_sync_established
```

相关声明：[bt_hci_evt_le_per_adv_sync_established](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadvertising_5Freport"></a>

```c
struct bt_hci_evt_le_per_advertising_report
```

相关声明：[bt_hci_evt_le_per_advertising_report](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fper_5Fadv_5Fsync_5Flost"></a>

```c
struct bt_hci_evt_le_per_adv_sync_lost
```

相关声明：[bt_hci_evt_le_per_adv_sync_lost](../bluetooth_hci_model_reference/P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fadv_5Fset_5Fterminated"></a>

```c
struct bt_hci_evt_le_adv_set_terminated
```

相关声明：[bt_hci_evt_le_adv_set_terminated](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fscan_5Freq_5Freceived"></a>

```c
struct bt_hci_evt_le_scan_req_received
```

相关声明：[bt_hci_evt_le_scan_req_received](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fchan_5Fsel_5Falgo"></a>

```c
struct bt_hci_evt_le_chan_sel_algo
```

相关声明：[bt_hci_evt_le_chan_sel_algo](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md)。

<a id="r_bt_5Fhci_5Fle_5Fiq_5Fsample"></a>

```c
struct bt_hci_le_iq_sample
```

相关声明：[bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconnectionless_5Fiq_5Freport"></a>

```c
struct bt_hci_evt_le_connectionless_iq_report
```

相关声明：[bt_hci_evt_le_connectionless_iq_report](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconnection_5Fiq_5Freport"></a>

```c
struct bt_hci_evt_le_connection_iq_report
```

相关声明：[bt_hci_evt_le_connection_iq_report](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcte_5Freq_5Ffailed"></a>

```c
struct bt_hci_evt_le_cte_req_failed
```

相关声明：[bt_hci_evt_le_cte_req_failed](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fpast_5Freceived"></a>

```c
struct bt_hci_evt_le_past_received
```

相关声明：[bt_hci_evt_le_past_received](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcis_5Festablished"></a>

```c
struct bt_hci_evt_le_cis_established
```

相关声明：[bt_hci_evt_le_cis_established](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcis_5Freq"></a>

```c
struct bt_hci_evt_le_cis_req
```

相关声明：[bt_hci_evt_le_cis_req](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fbig_5Fcomplete"></a>

```c
struct bt_hci_evt_le_big_complete
```

相关声明：[bt_hci_evt_le_big_complete](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fbig_5Fterminate"></a>

```c
struct bt_hci_evt_le_big_terminate
```

相关声明：[bt_hci_evt_le_big_terminate](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fbig_5Fsync_5Festablished"></a>

```c
struct bt_hci_evt_le_big_sync_established
```

相关声明：[bt_hci_evt_le_big_sync_established](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fbig_5Fsync_5Flost"></a>

```c
struct bt_hci_evt_le_big_sync_lost
```

相关声明：[bt_hci_evt_le_big_sync_lost](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Freq_5Fpeer_5Fsca_5Fcomplete"></a>

```c
struct bt_hci_evt_le_req_peer_sca_complete
```

相关声明：[bt_hci_evt_le_req_peer_sca_complete](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fpath_5Floss_5Fthreshold"></a>

```c
struct bt_hci_evt_le_path_loss_threshold
```

相关声明：[bt_hci_evt_le_path_loss_threshold](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Ftransmit_5Fpower_5Freport"></a>

```c
struct bt_hci_evt_le_transmit_power_report
```

相关声明：[bt_hci_evt_le_transmit_power_report](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fbiginfo_5Fadv_5Freport"></a>

```c
struct bt_hci_evt_le_biginfo_adv_report
```

相关声明：[bt_hci_evt_le_biginfo_adv_report](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fsubrate_5Fchange"></a>

```c
struct bt_hci_evt_le_subrate_change
```

相关声明：[bt_hci_evt_le_subrate_change](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcis_5Festablished_5Fv2"></a>

```c
struct bt_hci_evt_le_cis_established_v2
```

相关声明：[bt_hci_evt_le_cis_established_v2](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fread_5Fall_5Fremote_5Ffeat_5Fcomplete"></a>

```c
struct bt_hci_evt_le_read_all_remote_feat_complete
```

相关声明：[bt_hci_evt_le_read_all_remote_feat_complete](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fread_5Fremote_5Fsupported_5Fcapabilities_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_read_remote_supported_capabilities_complete
```

相关声明：[bt_hci_evt_le_cs_read_remote_supported_capabilities_complete](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fread_5Fremote_5Fsupported_5Fcapabilities_5Fcomplete_5Fv2"></a>

```c
struct bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2
```

相关声明：[bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md)。

低功耗信道探测读取远端支持能力完成（LE CS Read Remote Supported Capabilities Complete，v2）的 HCI 事件参数。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fread_5Fremote_5Ffae_5Ftable_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_read_remote_fae_table_complete
```

相关声明：[bt_hci_evt_le_cs_read_remote_fae_table_complete](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fsecurity_5Fenable_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_security_enable_complete
```

相关声明：[bt_hci_evt_le_cs_security_enable_complete](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fconfig_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_config_complete
```

相关声明：[bt_hci_evt_le_cs_config_complete](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F0_5Finitiator"></a>

```c
struct bt_hci_le_cs_step_data_mode_0_initiator
```

相关声明：[bt_hci_le_cs_step_data_mode_0_initiator](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md)。

子事件结果步骤数据格式（Subevent Result Step Data Format）：模式 0 发起方（Initiator）。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F0_5Freflector"></a>

```c
struct bt_hci_le_cs_step_data_mode_0_reflector
```

相关声明：[bt_hci_le_cs_step_data_mode_0_reflector](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md)。

子事件结果步骤数据格式：模式 0 反射方（Reflector）。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F1"></a>

```c
struct bt_hci_le_cs_step_data_mode_1
```

相关声明：[bt_hci_le_cs_step_data_mode_1](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md)。

子事件结果步骤数据格式：模式 1。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F1_5Fss_5Frtt"></a>

```c
struct bt_hci_le_cs_step_data_mode_1_ss_rtt
```

相关声明：[bt_hci_le_cs_step_data_mode_1_ss_rtt](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md)。

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 1。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Ftone_5Finfo"></a>

```c
struct bt_hci_le_cs_step_data_tone_info
```

相关声明：[bt_hci_le_cs_step_data_tone_info](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md)。

模式 2 和模式 3 中每条天线路径的步骤数据格式（Per-antenna Path Step Data Format）。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F2"></a>

```c
struct bt_hci_le_cs_step_data_mode_2
```

相关声明：[bt_hci_le_cs_step_data_mode_2](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md)。

子事件结果步骤数据格式：模式 2。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F3"></a>

```c
struct bt_hci_le_cs_step_data_mode_3
```

相关声明：[bt_hci_le_cs_step_data_mode_3](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md)。

子事件结果步骤数据格式：模式 3。

<a id="r_bt_5Fhci_5Fle_5Fcs_5Fstep_5Fdata_5Fmode_5F3_5Fss_5Frtt"></a>

```c
struct bt_hci_le_cs_step_data_mode_3_ss_rtt
```

相关声明：[bt_hci_le_cs_step_data_mode_3_ss_rtt](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md)。

子事件结果步骤数据格式：支持探测序列往返时间（Sounding Sequence RTT）的模式 3。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fsubevent_5Fresult_5Fstep"></a>

```c
struct bt_hci_evt_le_cs_subevent_result_step
```

相关声明：[bt_hci_evt_le_cs_subevent_result_step](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fsubevent_5Fresult"></a>

```c
struct bt_hci_evt_le_cs_subevent_result
```

相关声明：[bt_hci_evt_le_cs_subevent_result](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fsubevent_5Fresult_5Fcontinue"></a>

```c
struct bt_hci_evt_le_cs_subevent_result_continue
```

相关声明：[bt_hci_evt_le_cs_subevent_result_continue](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Ftest_5Fend_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_test_end_complete
```

相关声明：[bt_hci_evt_le_cs_test_end_complete](../bluetooth_hci_model_reference/P249_bt_hci_evt_le_cs_test_end_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fcs_5Fprocedure_5Fenable_5Fcomplete"></a>

```c
struct bt_hci_evt_le_cs_procedure_enable_complete
```

相关声明：[bt_hci_evt_le_cs_procedure_enable_complete](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fframe_5Fspace_5Fupdate_5Fcomplete"></a>

```c
struct bt_hci_evt_le_frame_space_update_complete
```

相关声明：[bt_hci_evt_le_frame_space_update_complete](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fle_5Fconn_5Frate_5Fchange"></a>

```c
struct bt_hci_evt_le_conn_rate_change
```

相关声明：[bt_hci_evt_le_conn_rate_change](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a2a578399cd3a1ed875ba2c8a49b8129b"></a>

```c
#define BT_HCI_H4_NONE 0x00 /* None of the known packet types */
```

相关声明：[BT_HCI_H4_NONE](#a2a578399cd3a1ed875ba2c8a49b8129b)。

<a id="r_a524788ee4d21fe9a4625c35e1756bfe9"></a>

```c
#define BT_HCI_H4_CMD 0x01 /* HCI Command packet */
```

相关声明：[BT_HCI_H4_CMD](#a524788ee4d21fe9a4625c35e1756bfe9)。

<a id="r_a17386452bbd60c85959296b6539232bd"></a>

```c
#define BT_HCI_H4_ACL 0x02 /* HCI ACL Data packet */
```

相关声明：[BT_HCI_H4_ACL](#a17386452bbd60c85959296b6539232bd)。

<a id="r_a9e1c93f187ed5864cebefccea1b3faa2"></a>

```c
#define BT_HCI_H4_SCO 0x03 /* HCI Synchronous Data packet */
```

相关声明：[BT_HCI_H4_SCO](#a9e1c93f187ed5864cebefccea1b3faa2)。

<a id="r_a783053bc2846063e50755f1590e81ba8"></a>

```c
#define BT_HCI_H4_EVT 0x04 /* HCI Event packet */
```

相关声明：[BT_HCI_H4_EVT](#a783053bc2846063e50755f1590e81ba8)。

<a id="r_af5e6a53cc7d9619f4ac2ea5bd3256149"></a>

```c
#define BT_HCI_H4_ISO 0x05 /* HCI ISO Data packet */
```

相关声明：[BT_HCI_H4_ISO](#af5e6a53cc7d9619f4ac2ea5bd3256149)。

<a id="r_a1109fda761e1ef8c6df935cf97fdc646"></a>

```c
#define BT_HCI_OWN_ADDR_PUBLIC 0x00
```

相关声明：[BT_HCI_OWN_ADDR_PUBLIC](#a1109fda761e1ef8c6df935cf97fdc646)。

<a id="r_a8693ea59b948960e627d62785515996e"></a>

```c
#define BT_HCI_OWN_ADDR_RANDOM 0x01
```

相关声明：[BT_HCI_OWN_ADDR_RANDOM](#a8693ea59b948960e627d62785515996e)。

<a id="r_a92a5db1ce46bbf3ddeaab4da76bc6685"></a>

```c
#define BT_HCI_OWN_ADDR_RPA_OR_PUBLIC 0x02
```

相关声明：[BT_HCI_OWN_ADDR_RPA_OR_PUBLIC](#a92a5db1ce46bbf3ddeaab4da76bc6685)。

<a id="r_aec05e679e29fde812e9a066e672405b4"></a>

```c
#define BT_HCI_OWN_ADDR_RPA_OR_RANDOM 0x03
```

相关声明：[BT_HCI_OWN_ADDR_RPA_OR_RANDOM](#aec05e679e29fde812e9a066e672405b4)。

<a id="r_a115907057c92a59a407d261133946b59"></a>

```c
#define BT_HCI_OWN_ADDR_RPA_MASK 0x02
```

相关声明：[BT_HCI_OWN_ADDR_RPA_MASK](#a115907057c92a59a407d261133946b59)。

<a id="r_aebc5bd975899f765afe697ab322db114"></a>

```c
#define BT_HCI_PEER_ADDR_RPA_UNRESOLVED 0xfe
```

相关声明：[BT_HCI_PEER_ADDR_RPA_UNRESOLVED](#aebc5bd975899f765afe697ab322db114)。

<a id="r_a1e6d78149d0990511b2b6dffb617069e"></a>

```c
#define BT_HCI_PEER_ADDR_ANONYMOUS 0xff
```

相关声明：[BT_HCI_PEER_ADDR_ANONYMOUS](#a1e6d78149d0990511b2b6dffb617069e)。

<a id="r_a90a6c0c50f915c347b75ac3ca46996ac"></a>

```c
#define BT_ENC_KEY_SIZE_MIN 0x07
```

相关声明：[BT_ENC_KEY_SIZE_MIN](#a90a6c0c50f915c347b75ac3ca46996ac)。

<a id="r_a4c274cd6947d37bf4f895ca0002c4f63"></a>

```c
#define BT_ENC_KEY_SIZE_MAX 0x10
```

相关声明：[BT_ENC_KEY_SIZE_MAX](#a4c274cd6947d37bf4f895ca0002c4f63)。

<a id="r_aa85640ad3a1aa78cf862a5d8b2567fa1"></a>

```c
#define BT_HCI_ADV_HANDLE_INVALID 0xff
```

相关声明：[BT_HCI_ADV_HANDLE_INVALID](#aa85640ad3a1aa78cf862a5d8b2567fa1)。

<a id="r_a4e4a6e6bb2dc713de8cb7c12139583ed"></a>

```c
#define BT_HCI_SYNC_HANDLE_INVALID 0xffff
```

相关声明：[BT_HCI_SYNC_HANDLE_INVALID](#a4e4a6e6bb2dc713de8cb7c12139583ed)。

<a id="r_a98554ced76600577254b4124b27ef8a8"></a>

```c
#define BT_HCI_PAWR_SUBEVENT_MAX 128
```

相关声明：[BT_HCI_PAWR_SUBEVENT_MAX](#a98554ced76600577254b4124b27ef8a8)。

<a id="r_acb8daef29a7f5f2d11a169fd10ae0caa"></a>

```c
#define BT_HCI_SCO_HDR_SIZE 3
```

相关声明：[BT_HCI_SCO_HDR_SIZE](#acb8daef29a7f5f2d11a169fd10ae0caa)。

<a id="r_a0edb7e700cfa557e7fb8ec44f5eea961"></a>

```c
#define BT_HCI_EVT_HDR_SIZE 2
```

相关声明：[BT_HCI_EVT_HDR_SIZE](#a0edb7e700cfa557e7fb8ec44f5eea961)。

<a id="r_ae8c5ddd450d47b45a310bc979207ebff"></a>

```c
#define BT_ACL_START_NO_FLUSH 0x00
```

相关声明：[BT_ACL_START_NO_FLUSH](#ae8c5ddd450d47b45a310bc979207ebff)。

<a id="r_a0bfb8a0bac96eb223eb8229c1dff9e7d"></a>

```c
#define BT_ACL_CONT 0x01
```

相关声明：[BT_ACL_CONT](#a0bfb8a0bac96eb223eb8229c1dff9e7d)。

<a id="r_a49c9728293c37e718c009ad973f6d43e"></a>

```c
#define BT_ACL_START 0x02
```

相关声明：[BT_ACL_START](#a49c9728293c37e718c009ad973f6d43e)。

<a id="r_ad6f24425a0818730d2377e159698922b"></a>

```c
#define BT_ACL_COMPLETE 0x03
```

相关声明：[BT_ACL_COMPLETE](#ad6f24425a0818730d2377e159698922b)。

<a id="r_a343e6550f9a24a59c5a08efd2dab16bb"></a>

```c
#define BT_ACL_POINT_TO_POINT 0x00
```

相关声明：[BT_ACL_POINT_TO_POINT](#a343e6550f9a24a59c5a08efd2dab16bb)。

<a id="r_a2f9e6232229ae1bed3d835b5f6531a76"></a>

```c
#define BT_ACL_BROADCAST 0x01
```

相关声明：[BT_ACL_BROADCAST](#a2f9e6232229ae1bed3d835b5f6531a76)。

<a id="r_a28a9f26ba563e2687856aff39b044039"></a>

```c
#define BT_ACL_HANDLE_MASK BIT_MASK(12)
```

相关声明：[BT_ACL_HANDLE_MASK](#a28a9f26ba563e2687856aff39b044039)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a500341d3485843d85dc034ce6f8a908c"></a>

```c
#define bt_acl_handle(h)
```

相关声明：[bt_acl_handle](#a500341d3485843d85dc034ce6f8a908c)。

<a id="r_a499f8647747fd6b7b82d9b3280b4b048"></a>

```c
#define bt_acl_flags(h)
```

相关声明：[bt_acl_flags](#a499f8647747fd6b7b82d9b3280b4b048)。

<a id="r_ae358e74ce455f11bb134700ec80fe07b"></a>

```c
#define bt_acl_flags_pb(f)
```

相关声明：[bt_acl_flags_pb](#ae358e74ce455f11bb134700ec80fe07b)。

<a id="r_a55cfcca3e0a6a7401e57e7430421093e"></a>

```c
#define bt_acl_flags_bc(f)
```

相关声明：[bt_acl_flags_bc](#a55cfcca3e0a6a7401e57e7430421093e)。

<a id="r_aa08e6239d84ce55153baa41f46814363"></a>

```c
#define bt_acl_handle_pack(h, f)
```

相关声明：[bt_acl_handle_pack](#aa08e6239d84ce55153baa41f46814363)。

<a id="r_a7418d845532d6b077a9695454fa65bc5"></a>

```c
#define BT_HCI_ACL_HDR_SIZE 4
```

相关声明：[BT_HCI_ACL_HDR_SIZE](#a7418d845532d6b077a9695454fa65bc5)。

<a id="r_a9ef86241b4dfb462ec31c855bce4ee28"></a>

```c
#define BT_ISO_START 0x00
```

相关声明：[BT_ISO_START](#a9ef86241b4dfb462ec31c855bce4ee28)。

<a id="r_a06c43e91abee990343ece9c22f5a515e"></a>

```c
#define BT_ISO_CONT 0x01
```

相关声明：[BT_ISO_CONT](#a06c43e91abee990343ece9c22f5a515e)。

<a id="r_a1db9801de1c97b2d15cf9d2f0ec2a5f0"></a>

```c
#define BT_ISO_SINGLE 0x02
```

相关声明：[BT_ISO_SINGLE](#a1db9801de1c97b2d15cf9d2f0ec2a5f0)。

<a id="r_ac2da3db69ba73112fff5bf16ef386cb3"></a>

```c
#define BT_ISO_END 0x03
```

相关声明：[BT_ISO_END](#ac2da3db69ba73112fff5bf16ef386cb3)。

<a id="r_adcdb9dd367b64a820a040724c1c42c15"></a>

```c
#define bt_iso_handle(h)
```

相关声明：[bt_iso_handle](#adcdb9dd367b64a820a040724c1c42c15)。

<a id="r_a54e2f7efc0f22287d65bdd560dd7ec78"></a>

```c
#define bt_iso_flags(h)
```

相关声明：[bt_iso_flags](#a54e2f7efc0f22287d65bdd560dd7ec78)。

<a id="r_a7ea328491745f1bde6e2b376c19cc380"></a>

```c
#define bt_iso_flags_pb(f)
```

相关声明：[bt_iso_flags_pb](#a7ea328491745f1bde6e2b376c19cc380)。

<a id="r_aed6d45daf19ce7fadc1c8fbcc79c9e8a"></a>

```c
#define bt_iso_flags_ts(f)
```

相关声明：[bt_iso_flags_ts](#aed6d45daf19ce7fadc1c8fbcc79c9e8a)。

<a id="r_a9bdbdc6e181731a58ec91d53cdade532"></a>

```c
#define bt_iso_pack_flags(pb, ts)
```

相关声明：[bt_iso_pack_flags](#a9bdbdc6e181731a58ec91d53cdade532)。

<a id="r_ab96b2d1b49a86ee96b2254b624b2e93f"></a>

```c
#define bt_iso_handle_pack(h, pb, ts)
```

相关声明：[bt_iso_handle_pack](#ab96b2d1b49a86ee96b2254b624b2e93f)。

<a id="r_a128d269790ccf3f8dcdeb51f80697ba0"></a>

```c
#define bt_iso_hdr_len(h)
```

相关声明：[bt_iso_hdr_len](#a128d269790ccf3f8dcdeb51f80697ba0)。

<a id="r_a52091a307cca85d8d39fbfe5be6b6179"></a>

```c
#define BT_ISO_DATA_VALID 0x00
```

相关声明：[BT_ISO_DATA_VALID](#a52091a307cca85d8d39fbfe5be6b6179)。

<a id="r_a7149213544fe2ac9e7d3d0fd64ecb271"></a>

```c
#define BT_ISO_DATA_INVALID 0x01
```

相关声明：[BT_ISO_DATA_INVALID](#a7149213544fe2ac9e7d3d0fd64ecb271)。

<a id="r_ae736b21ff7b99c4bb85df1a3f4bee9cd"></a>

```c
#define BT_ISO_DATA_NOP 0x02
```

相关声明：[BT_ISO_DATA_NOP](#ae736b21ff7b99c4bb85df1a3f4bee9cd)。

<a id="r_a0d540918a423992f5f244febcc82248a"></a>

```c
#define bt_iso_pkt_len(h)
```

相关声明：[bt_iso_pkt_len](#a0d540918a423992f5f244febcc82248a)。

<a id="r_a6dbade5730a92ea7f85017792939e941"></a>

```c
#define bt_iso_pkt_flags(h)
```

相关声明：[bt_iso_pkt_flags](#a6dbade5730a92ea7f85017792939e941)。

<a id="r_a3683be1ceedbcb97f61483b6fa4344e6"></a>

```c
#define bt_iso_pkt_len_pack(h, f)
```

相关声明：[bt_iso_pkt_len_pack](#a3683be1ceedbcb97f61483b6fa4344e6)。

<a id="r_a94b93cd856353f24afee5e4022cdbdb9"></a>

```c
#define BT_HCI_ISO_SDU_HDR_SIZE 4
```

相关声明：[BT_HCI_ISO_SDU_HDR_SIZE](#a94b93cd856353f24afee5e4022cdbdb9)。

<a id="r_a22db454317bc89afe092ab9127888441"></a>

```c
#define BT_HCI_ISO_SDU_TS_HDR_SIZE 8
```

相关声明：[BT_HCI_ISO_SDU_TS_HDR_SIZE](#a22db454317bc89afe092ab9127888441)。

<a id="r_a75c1f5e8a44b034004ecfebdb75ee4be"></a>

```c
#define BT_HCI_ISO_HDR_SIZE 4
```

相关声明：[BT_HCI_ISO_HDR_SIZE](#a75c1f5e8a44b034004ecfebdb75ee4be)。

<a id="r_acdf2b6de1459a7492415a8987ad9a896"></a>

```c
#define BT_HCI_CMD_HDR_SIZE 3
```

相关声明：[BT_HCI_CMD_HDR_SIZE](#acdf2b6de1459a7492415a8987ad9a896)。

<a id="r_a7d5bc35e597d03fbc65084b39771cf0b"></a>

```c
#define BT_CMD_TEST(cmd, octet, bit)
```

相关声明：[BT_CMD_TEST](#a7d5bc35e597d03fbc65084b39771cf0b)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

<a id="r_ae3aaad5ae408cb8c72a29ff7a8817c21"></a>

```c
#define BT_CMD_LE_STATES(cmd)
```

相关声明：[BT_CMD_LE_STATES](#ae3aaad5ae408cb8c72a29ff7a8817c21)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

<a id="r_a41e5b49e645ed511340a61f843f6b238"></a>

```c
#define BT_FEAT_TEST(feat, page, octet, bit)
```

相关声明：[BT_FEAT_TEST](#a41e5b49e645ed511340a61f843f6b238)。

<a id="r_a5508c481ff6b8fd46f2f2c077aaa90c9"></a>

```c
#define BT_FEAT_BREDR(feat)
```

相关声明：[BT_FEAT_BREDR](#a5508c481ff6b8fd46f2f2c077aaa90c9)。

<a id="r_a8b1df8d6b9e0dfcaa13635588cc3bfe3"></a>

```c
#define BT_FEAT_LE(feat)
```

相关声明：[BT_FEAT_LE](#a8b1df8d6b9e0dfcaa13635588cc3bfe3)。

<a id="r_ac26ebac4f1641d5ff4484f74579852d7"></a>

```c
#define BT_FEAT_EXT_FEATURES(feat)
```

相关声明：[BT_FEAT_EXT_FEATURES](#ac26ebac4f1641d5ff4484f74579852d7)。

<a id="r_af011519b6fb0477ac7f87e5dc98daed0"></a>

```c
#define BT_FEAT_HOST_SSP(feat)
```

相关声明：[BT_FEAT_HOST_SSP](#af011519b6fb0477ac7f87e5dc98daed0)。

<a id="r_a9ecf892ec94af8cbfd2e6c99310b1fa2"></a>

```c
#define BT_FEAT_SC(feat)
```

相关声明：[BT_FEAT_SC](#a9ecf892ec94af8cbfd2e6c99310b1fa2)。

<a id="r_a24f24640d9f52adb15336a1b17122346"></a>

```c
#define BT_FEAT_LMP_SCO_CAPABLE(feat)
```

相关声明：[BT_FEAT_LMP_SCO_CAPABLE](#a24f24640d9f52adb15336a1b17122346)。

<a id="r_a7622a2fc0a65f82a827ab3cc84e4e7c5"></a>

```c
#define BT_FEAT_LMP_ESCO_CAPABLE(feat)
```

相关声明：[BT_FEAT_LMP_ESCO_CAPABLE](#a7622a2fc0a65f82a827ab3cc84e4e7c5)。

<a id="r_ad59c138e945d7f27d3befc286b679e03"></a>

```c
#define BT_FEAT_HV2_PKT(feat)
```

相关声明：[BT_FEAT_HV2_PKT](#ad59c138e945d7f27d3befc286b679e03)。

<a id="r_aed6f11d60161c919b4d2b7eb13f46e47"></a>

```c
#define BT_FEAT_HV3_PKT(feat)
```

相关声明：[BT_FEAT_HV3_PKT](#aed6f11d60161c919b4d2b7eb13f46e47)。

<a id="r_ad154d0649e8e90c1102b74cae8327fa7"></a>

```c
#define BT_FEAT_EV4_PKT(feat)
```

相关声明：[BT_FEAT_EV4_PKT](#ad154d0649e8e90c1102b74cae8327fa7)。

<a id="r_a0a6b9afb4673dc852e1a4d8e867003c9"></a>

```c
#define BT_FEAT_EV5_PKT(feat)
```

相关声明：[BT_FEAT_EV5_PKT](#a0a6b9afb4673dc852e1a4d8e867003c9)。

<a id="r_a8dbbf37965a9d0ddab5a07f88d7cd7ca"></a>

```c
#define BT_FEAT_2EV3_PKT(feat)
```

相关声明：[BT_FEAT_2EV3_PKT](#a8dbbf37965a9d0ddab5a07f88d7cd7ca)。

<a id="r_a00aec89aa4d1504934e85ec79462b346"></a>

```c
#define BT_FEAT_3EV3_PKT(feat)
```

相关声明：[BT_FEAT_3EV3_PKT](#a00aec89aa4d1504934e85ec79462b346)。

<a id="r_a5219ff658b46cf28104a99f089854444"></a>

```c
#define BT_FEAT_3SLOT_PKT(feat)
```

相关声明：[BT_FEAT_3SLOT_PKT](#a5219ff658b46cf28104a99f089854444)。

<a id="r_abd616dd5af5ed3742be9bae400ded848"></a>

```c
#define BT_LE_FEAT_BIT_ENC 0
```

相关声明：[BT_LE_FEAT_BIT_ENC](#abd616dd5af5ed3742be9bae400ded848)。

<a id="r_ab816048bdd6c1e42b0e458abebb76572"></a>

```c
#define BT_LE_FEAT_BIT_CONN_PARAM_REQ 1
```

相关声明：[BT_LE_FEAT_BIT_CONN_PARAM_REQ](#ab816048bdd6c1e42b0e458abebb76572)。

<a id="r_ae5644021aff31996c09f6edf3ede197c"></a>

```c
#define BT_LE_FEAT_BIT_EXT_REJ_IND 2
```

相关声明：[BT_LE_FEAT_BIT_EXT_REJ_IND](#ae5644021aff31996c09f6edf3ede197c)。

<a id="r_aeaea6ea6595de9e3283fd6063bf7c579"></a>

```c
#define BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG 3
```

相关声明：[BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG](#aeaea6ea6595de9e3283fd6063bf7c579)。

<a id="r_a9b4dc56ef4433b0c0dc74a3d95cf289e"></a>

```c
#define BT_LE_FEAT_BIT_PING 4
```

相关声明：[BT_LE_FEAT_BIT_PING](#a9b4dc56ef4433b0c0dc74a3d95cf289e)。

<a id="r_ac09127210b281e5ee45fbc134df64aa6"></a>

```c
#define BT_LE_FEAT_BIT_DLE 5
```

相关声明：[BT_LE_FEAT_BIT_DLE](#ac09127210b281e5ee45fbc134df64aa6)。

<a id="r_a3c4196c04a73aa537baa845e061e9654"></a>

```c
#define BT_LE_FEAT_BIT_PRIVACY 6
```

相关声明：[BT_LE_FEAT_BIT_PRIVACY](#a3c4196c04a73aa537baa845e061e9654)。

<a id="r_a8f1fa8948f79bec50373e0342ab0969a"></a>

```c
#define BT_LE_FEAT_BIT_EXT_SCAN 7
```

相关声明：[BT_LE_FEAT_BIT_EXT_SCAN](#a8f1fa8948f79bec50373e0342ab0969a)。

<a id="r_afcbc8d664c8e924b777c06ffb4c17315"></a>

```c
#define BT_LE_FEAT_BIT_PHY_2M 8
```

相关声明：[BT_LE_FEAT_BIT_PHY_2M](#afcbc8d664c8e924b777c06ffb4c17315)。

<a id="r_aea19f3c3cdcec054c81c176d5aa5f319"></a>

```c
#define BT_LE_FEAT_BIT_SMI_TX 9
```

相关声明：[BT_LE_FEAT_BIT_SMI_TX](#aea19f3c3cdcec054c81c176d5aa5f319)。

<a id="r_a9430a65ea813861b6890252ed4748f19"></a>

```c
#define BT_LE_FEAT_BIT_SMI_RX 10
```

相关声明：[BT_LE_FEAT_BIT_SMI_RX](#a9430a65ea813861b6890252ed4748f19)。

<a id="r_a800686aa45cf336fbd6efc76b3752959"></a>

```c
#define BT_LE_FEAT_BIT_PHY_CODED 11
```

相关声明：[BT_LE_FEAT_BIT_PHY_CODED](#a800686aa45cf336fbd6efc76b3752959)。

<a id="r_ae1a0751e7c380117c4e31741712096a4"></a>

```c
#define BT_LE_FEAT_BIT_EXT_ADV 12
```

相关声明：[BT_LE_FEAT_BIT_EXT_ADV](#ae1a0751e7c380117c4e31741712096a4)。

<a id="r_a1ac5bab6d48775b4e63e249b5759a683"></a>

```c
#define BT_LE_FEAT_BIT_PER_ADV 13
```

相关声明：[BT_LE_FEAT_BIT_PER_ADV](#a1ac5bab6d48775b4e63e249b5759a683)。

<a id="r_a9120867d6f31465cb5f085b610d5ed70"></a>

```c
#define BT_LE_FEAT_BIT_CHAN_SEL_ALGO_2 14
```

相关声明：[BT_LE_FEAT_BIT_CHAN_SEL_ALGO_2](#a9120867d6f31465cb5f085b610d5ed70)。

<a id="r_a938f823110f31a3a5d034cbe9b9d26eb"></a>

```c
#define BT_LE_FEAT_BIT_PWR_CLASS_1 15
```

相关声明：[BT_LE_FEAT_BIT_PWR_CLASS_1](#a938f823110f31a3a5d034cbe9b9d26eb)。

<a id="r_ac8cf36c670ae359ec24e62efb4505758"></a>

```c
#define BT_LE_FEAT_BIT_MIN_USED_CHAN_PROC 16
```

相关声明：[BT_LE_FEAT_BIT_MIN_USED_CHAN_PROC](#ac8cf36c670ae359ec24e62efb4505758)。

<a id="r_aed34742e8554b830c3b6c4bf04f0e2db"></a>

```c
#define BT_LE_FEAT_BIT_CONN_CTE_REQ 17
```

相关声明：[BT_LE_FEAT_BIT_CONN_CTE_REQ](#aed34742e8554b830c3b6c4bf04f0e2db)。

<a id="r_aa5279a2ce26decb5856a6b709d0641c9"></a>

```c
#define BT_LE_FEAT_BIT_CONN_CTE_RESP 18
```

相关声明：[BT_LE_FEAT_BIT_CONN_CTE_RESP](#aa5279a2ce26decb5856a6b709d0641c9)。

<a id="r_a331e7697a3fdc073abba5dd0ff47346b"></a>

```c
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX 19
```

相关声明：[BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX](#a331e7697a3fdc073abba5dd0ff47346b)。

<a id="r_a6abf01c846a5d637ca98997f6cfc263d"></a>

```c
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX 20
```

相关声明：[BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX](#a6abf01c846a5d637ca98997f6cfc263d)。

<a id="r_a41eae1585972ae6792eb1a639c2e3a8e"></a>

```c
#define BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD 21
```

相关声明：[BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD](#a41eae1585972ae6792eb1a639c2e3a8e)。

<a id="r_a480fc67a1c8a2f36410f285ef0ee36e7"></a>

```c
#define BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA 22
```

相关声明：[BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA](#a480fc67a1c8a2f36410f285ef0ee36e7)。

<a id="r_a9d9449f1935d6522291eca581f3fa9b0"></a>

```c
#define BT_LE_FEAT_BIT_RX_CTE 23
```

相关声明：[BT_LE_FEAT_BIT_RX_CTE](#a9d9449f1935d6522291eca581f3fa9b0)。

<a id="r_aa05da01a6a9b9ac26423d6fc2661f3db"></a>

```c
#define BT_LE_FEAT_BIT_PAST_SEND 24
```

相关声明：[BT_LE_FEAT_BIT_PAST_SEND](#aa05da01a6a9b9ac26423d6fc2661f3db)。

<a id="r_a28a862eaf11f8b45237f3b87e4bb15c7"></a>

```c
#define BT_LE_FEAT_BIT_PAST_RECV 25
```

相关声明：[BT_LE_FEAT_BIT_PAST_RECV](#a28a862eaf11f8b45237f3b87e4bb15c7)。

<a id="r_a829e9d23a16912bad19448a6c4061e3b"></a>

```c
#define BT_LE_FEAT_BIT_SCA_UPDATE 26
```

相关声明：[BT_LE_FEAT_BIT_SCA_UPDATE](#a829e9d23a16912bad19448a6c4061e3b)。

<a id="r_a6d17dd4238ea471daca22f74e3cc3bcb"></a>

```c
#define BT_LE_FEAT_BIT_REMOTE_PUB_KEY_VALIDATE 27
```

相关声明：[BT_LE_FEAT_BIT_REMOTE_PUB_KEY_VALIDATE](#a6d17dd4238ea471daca22f74e3cc3bcb)。

<a id="r_aa98eed376b6d5263621f14c55d776088"></a>

```c
#define BT_LE_FEAT_BIT_CIS_CENTRAL 28
```

相关声明：[BT_LE_FEAT_BIT_CIS_CENTRAL](#aa98eed376b6d5263621f14c55d776088)。

<a id="r_a298fde96c2d6376e3333a99f7e03409d"></a>

```c
#define BT_LE_FEAT_BIT_CIS_PERIPHERAL 29
```

相关声明：[BT_LE_FEAT_BIT_CIS_PERIPHERAL](#a298fde96c2d6376e3333a99f7e03409d)。

<a id="r_af08a1ffd734d1c211f38d90b4fe72417"></a>

```c
#define BT_LE_FEAT_BIT_ISO_BROADCASTER 30
```

相关声明：[BT_LE_FEAT_BIT_ISO_BROADCASTER](#af08a1ffd734d1c211f38d90b4fe72417)。

<a id="r_a2fed771f5611212e48027025e11f7678"></a>

```c
#define BT_LE_FEAT_BIT_SYNC_RECEIVER 31
```

相关声明：[BT_LE_FEAT_BIT_SYNC_RECEIVER](#a2fed771f5611212e48027025e11f7678)。

<a id="r_a0d80ccb33d263abd3b42de1b69cfeeeb"></a>

```c
#define BT_LE_FEAT_BIT_ISO_CHANNELS 32
```

相关声明：[BT_LE_FEAT_BIT_ISO_CHANNELS](#a0d80ccb33d263abd3b42de1b69cfeeeb)。

<a id="r_ae58f5260530d1b94608874f5d03d766d"></a>

```c
#define BT_LE_FEAT_BIT_PWR_CTRL_REQ 33
```

相关声明：[BT_LE_FEAT_BIT_PWR_CTRL_REQ](#ae58f5260530d1b94608874f5d03d766d)。

<a id="r_a0138172a0ed78244d8d3ac9d6936cf85"></a>

```c
#define BT_LE_FEAT_BIT_PWR_CHG_IND 34
```

相关声明：[BT_LE_FEAT_BIT_PWR_CHG_IND](#a0138172a0ed78244d8d3ac9d6936cf85)。

<a id="r_a434fb43b6b3176393f5d22d3932d69fa"></a>

```c
#define BT_LE_FEAT_BIT_PATH_LOSS_MONITOR 35
```

相关声明：[BT_LE_FEAT_BIT_PATH_LOSS_MONITOR](#a434fb43b6b3176393f5d22d3932d69fa)。

<a id="r_ad5a8221cb25d79b63f1a574699983038"></a>

```c
#define BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP 36
```

相关声明：[BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP](#ad5a8221cb25d79b63f1a574699983038)。

<a id="r_aa45b06a49232372891ceb5e4496d46da"></a>

```c
#define BT_LE_FEAT_BIT_CONN_SUBRATING 37
```

相关声明：[BT_LE_FEAT_BIT_CONN_SUBRATING](#aa45b06a49232372891ceb5e4496d46da)。

<a id="r_adb884a30bc1a24e3dfb115cef7149c81"></a>

```c
#define BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP 38
```

相关声明：[BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP](#adb884a30bc1a24e3dfb115cef7149c81)。

<a id="r_af2a4be520b4d8c3eb56231b865738e90"></a>

```c
#define BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION 39
```

相关声明：[BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION](#af2a4be520b4d8c3eb56231b865738e90)。

<a id="r_a4d920d42e8042c9117f97e334f889f51"></a>

```c
#define BT_LE_FEAT_BIT_ADV_CODING_SEL 40
```

相关声明：[BT_LE_FEAT_BIT_ADV_CODING_SEL](#a4d920d42e8042c9117f97e334f889f51)。

<a id="r_ad711e7491883e1f1e068fe167cca8a4e"></a>

```c
#define BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST 41
```

相关声明：[BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST](#ad711e7491883e1f1e068fe167cca8a4e)。

<a id="r_a58d4aacb31998717b5943b7314622eb3"></a>

```c
#define BT_LE_FEAT_BIT_DECISION_ADV_FILTER 42
```

相关声明：[BT_LE_FEAT_BIT_DECISION_ADV_FILTER](#a58d4aacb31998717b5943b7314622eb3)。

<a id="r_af251cb9d905586fd53113f5920038dae"></a>

```c
#define BT_LE_FEAT_BIT_PAWR_ADVERTISER 43
```

相关声明：[BT_LE_FEAT_BIT_PAWR_ADVERTISER](#af251cb9d905586fd53113f5920038dae)。

<a id="r_a00bb51972e0db07be84d4f3dfd007cea"></a>

```c
#define BT_LE_FEAT_BIT_PAWR_SCANNER 44
```

相关声明：[BT_LE_FEAT_BIT_PAWR_SCANNER](#a00bb51972e0db07be84d4f3dfd007cea)。

<a id="r_ace0c3131b0a592ae60d8ef705ff54e7c"></a>

```c
#define BT_LE_FEAT_BIT_UNSEG_FRAMED_MODE 45
```

相关声明：[BT_LE_FEAT_BIT_UNSEG_FRAMED_MODE](#ace0c3131b0a592ae60d8ef705ff54e7c)。

<a id="r_ab918084874aace22954aa748333baf6d"></a>

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING 46
```

相关声明：[BT_LE_FEAT_BIT_CHANNEL_SOUNDING](#ab918084874aace22954aa748333baf6d)。

<a id="r_aa4572a11d78651ce775a010178c6dfa2"></a>

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST 47
```

相关声明：[BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST](#aa4572a11d78651ce775a010178c6dfa2)。

<a id="r_a705bd721edaa581f0046064ca39c2b69"></a>

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_TONE_QUAL_IND 48
```

相关声明：[BT_LE_FEAT_BIT_CHANNEL_SOUNDING_TONE_QUAL_IND](#a705bd721edaa581f0046064ca39c2b69)。

<a id="r_a51fc94e0f2ed1c6fe724c2846756cb31"></a>

```c
#define BT_LE_FEAT_BIT_EXTENDED_FEAT_SET 63
```

相关声明：[BT_LE_FEAT_BIT_EXTENDED_FEAT_SET](#a51fc94e0f2ed1c6fe724c2846756cb31)。

<a id="r_a06c9aa4e8165cfe3e359283f199b450c"></a>

```c
#define BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE 65
```

相关声明：[BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE](#a06c9aa4e8165cfe3e359283f199b450c)。

<a id="r_ac00a188cc19a04ff9523fd3a4e044b17"></a>

```c
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS 72
```

相关声明：[BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS](#ac00a188cc19a04ff9523fd3a4e044b17)。

<a id="r_a670eda9a27a581646c5bc17fc452b466"></a>

```c
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP 73
```

相关声明：[BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP](#a670eda9a27a581646c5bc17fc452b466)。

<a id="r_a6bf20989952fed3726bc45873beb896e"></a>

```c
#define BT_LE_FEAT_TEST(feat, n)
```

相关声明：[BT_LE_FEAT_TEST](#a6bf20989952fed3726bc45873beb896e)。

<a id="r_a51464aacf5bbcbfb873fa6c757bbcd79"></a>

```c
#define BT_FEAT_LE_ENCR(feat)
```

相关声明：[BT_FEAT_LE_ENCR](#a51464aacf5bbcbfb873fa6c757bbcd79)。

<a id="r_a554c027fb3946de6f861ea267968ba17"></a>

```c
#define BT_FEAT_LE_CONN_PARAM_REQ_PROC(feat)
```

相关声明：[BT_FEAT_LE_CONN_PARAM_REQ_PROC](#a554c027fb3946de6f861ea267968ba17)。

<a id="r_a132b2561dcd4140458fb612b6e0d8b25"></a>

```c
#define BT_FEAT_LE_PER_INIT_FEAT_XCHG(feat)
```

相关声明：[BT_FEAT_LE_PER_INIT_FEAT_XCHG](#a132b2561dcd4140458fb612b6e0d8b25)。

<a id="r_a62e7d152cd9dfabf5b1420945099ecb6"></a>

```c
#define BT_FEAT_LE_DLE(feat)
```

相关声明：[BT_FEAT_LE_DLE](#a62e7d152cd9dfabf5b1420945099ecb6)。

<a id="r_aaf11993f4938bb4894cdd317f9386fa3"></a>

```c
#define BT_FEAT_LE_PHY_2M(feat)
```

相关声明：[BT_FEAT_LE_PHY_2M](#aaf11993f4938bb4894cdd317f9386fa3)。

<a id="r_abb89a0bebe4046ae310b01dd27e02c99"></a>

```c
#define BT_FEAT_LE_PHY_CODED(feat)
```

相关声明：[BT_FEAT_LE_PHY_CODED](#abb89a0bebe4046ae310b01dd27e02c99)。

<a id="r_a0b2781f29085a5807d0b2235c32f5173"></a>

```c
#define BT_FEAT_LE_PRIVACY(feat)
```

相关声明：[BT_FEAT_LE_PRIVACY](#a0b2781f29085a5807d0b2235c32f5173)。

<a id="r_ad55c1593a92a868fff376b0d2d2154ad"></a>

```c
#define BT_FEAT_LE_EXT_SCAN(feat)
```

相关声明：[BT_FEAT_LE_EXT_SCAN](#ad55c1593a92a868fff376b0d2d2154ad)。

测试是否支持扩展扫描器过滤策略（Extended Scanner Filter Policies）功能。

<a id="r_a8bce94a732d28ce74ad2663e01da09b2"></a>

```c
#define BT_FEAT_LE_EXT_ADV(feat)
```

相关声明：[BT_FEAT_LE_EXT_ADV](#a8bce94a732d28ce74ad2663e01da09b2)。

<a id="r_a5d479d919db4920b7a53c054e4ae7a19"></a>

```c
#define BT_FEAT_LE_EXT_PER_ADV(feat)
```

相关声明：[BT_FEAT_LE_EXT_PER_ADV](#a5d479d919db4920b7a53c054e4ae7a19)。

<a id="r_a51316a5b67950e7644dfb71c4c6baa96"></a>

```c
#define BT_FEAT_LE_CONNECTION_CTE_REQ(feat)
```

相关声明：[BT_FEAT_LE_CONNECTION_CTE_REQ](#a51316a5b67950e7644dfb71c4c6baa96)。

<a id="r_a0cdc67a1345969d3504380fce94a4cda"></a>

```c
#define BT_FEAT_LE_CONNECTION_CTE_RESP(feat)
```

相关声明：[BT_FEAT_LE_CONNECTION_CTE_RESP](#a0cdc67a1345969d3504380fce94a4cda)。

<a id="r_a81e30f5630750ce4f805748fbe14b456"></a>

```c
#define BT_FEAT_LE_CONNECTIONLESS_CTE_TX(feat)
```

相关声明：[BT_FEAT_LE_CONNECTIONLESS_CTE_TX](#a81e30f5630750ce4f805748fbe14b456)。

<a id="r_aeb0639a8e5cbc904d7f5c02d72375913"></a>

```c
#define BT_FEAT_LE_CONNECTIONLESS_CTE_RX(feat)
```

相关声明：[BT_FEAT_LE_CONNECTIONLESS_CTE_RX](#aeb0639a8e5cbc904d7f5c02d72375913)。

<a id="r_ae503f9186d39fbea2347036c891fc8bf"></a>

```c
#define BT_FEAT_LE_ANT_SWITCH_TX_AOD(feat)
```

相关声明：[BT_FEAT_LE_ANT_SWITCH_TX_AOD](#ae503f9186d39fbea2347036c891fc8bf)。

<a id="r_a1c3c0e6a213b71e680ca24738047f09a"></a>

```c
#define BT_FEAT_LE_ANT_SWITCH_RX_AOA(feat)
```

相关声明：[BT_FEAT_LE_ANT_SWITCH_RX_AOA](#a1c3c0e6a213b71e680ca24738047f09a)。

<a id="r_adf4303d47abfab3bd23080c545b77ef7"></a>

```c
#define BT_FEAT_LE_RX_CTE(feat)
```

相关声明：[BT_FEAT_LE_RX_CTE](#adf4303d47abfab3bd23080c545b77ef7)。

<a id="r_a9e68dcf290273a4a140645c187cd7aee"></a>

```c
#define BT_FEAT_LE_PAST_SEND(feat)
```

相关声明：[BT_FEAT_LE_PAST_SEND](#a9e68dcf290273a4a140645c187cd7aee)。

<a id="r_a7a88046c26b3603a2bb8b0f2ee158b5f"></a>

```c
#define BT_FEAT_LE_PAST_RECV(feat)
```

相关声明：[BT_FEAT_LE_PAST_RECV](#a7a88046c26b3603a2bb8b0f2ee158b5f)。

<a id="r_adce7c3804a224e7b7317728fa27d4945"></a>

```c
#define BT_FEAT_LE_CIS_CENTRAL(feat)
```

相关声明：[BT_FEAT_LE_CIS_CENTRAL](#adce7c3804a224e7b7317728fa27d4945)。

<a id="r_a8a6860b285b3b4401021ba16f59404ce"></a>

```c
#define BT_FEAT_LE_CIS_PERIPHERAL(feat)
```

相关声明：[BT_FEAT_LE_CIS_PERIPHERAL](#a8a6860b285b3b4401021ba16f59404ce)。

<a id="r_a1c6fd06877a5606ae33aedc45a71f853"></a>

```c
#define BT_FEAT_LE_ISO_BROADCASTER(feat)
```

相关声明：[BT_FEAT_LE_ISO_BROADCASTER](#a1c6fd06877a5606ae33aedc45a71f853)。

<a id="r_af33c8331e204eeee2a7a02e2ad46c7a2"></a>

```c
#define BT_FEAT_LE_SYNC_RECEIVER(feat)
```

相关声明：[BT_FEAT_LE_SYNC_RECEIVER](#af33c8331e204eeee2a7a02e2ad46c7a2)。

<a id="r_a0b24b74715fbf84c2da2dd2cbbb34605"></a>

```c
#define BT_FEAT_LE_ISO_CHANNELS(feat)
```

相关声明：[BT_FEAT_LE_ISO_CHANNELS](#a0b24b74715fbf84c2da2dd2cbbb34605)。

<a id="r_a8ab0d3ca572861bb1c40191766481799"></a>

```c
#define BT_FEAT_LE_PWR_CTRL_REQ(feat)
```

相关声明：[BT_FEAT_LE_PWR_CTRL_REQ](#a8ab0d3ca572861bb1c40191766481799)。

<a id="r_a342ce6074faa59b507cf179868e612ba"></a>

```c
#define BT_FEAT_LE_PWR_CHG_IND(feat)
```

相关声明：[BT_FEAT_LE_PWR_CHG_IND](#a342ce6074faa59b507cf179868e612ba)。

<a id="r_a8d771bd34d22853f117dbbd41ef4afe5"></a>

```c
#define BT_FEAT_LE_PATH_LOSS_MONITOR(feat)
```

相关声明：[BT_FEAT_LE_PATH_LOSS_MONITOR](#a8d771bd34d22853f117dbbd41ef4afe5)。

<a id="r_a6213deacc8582f14546b23331d41c3a3"></a>

```c
#define BT_FEAT_LE_PER_ADV_ADI_SUPP(feat)
```

相关声明：[BT_FEAT_LE_PER_ADV_ADI_SUPP](#a6213deacc8582f14546b23331d41c3a3)。

<a id="r_a75bf595ba1e16deeeedb45a55f470620"></a>

```c
#define BT_FEAT_LE_CONN_SUBRATING(feat)
```

相关声明：[BT_FEAT_LE_CONN_SUBRATING](#a75bf595ba1e16deeeedb45a55f470620)。

<a id="r_a37adeecbf4c200cf8b060344718e7949"></a>

```c
#define BT_FEAT_LE_CONN_SUBRATING_HOST_SUPP(feat)
```

相关声明：[BT_FEAT_LE_CONN_SUBRATING_HOST_SUPP](#a37adeecbf4c200cf8b060344718e7949)。

<a id="r_abb7763cc16340d23bc7d687e60badcc0"></a>

```c
#define BT_FEAT_LE_CHANNEL_CLASSIFICATION(feat)
```

相关声明：[BT_FEAT_LE_CHANNEL_CLASSIFICATION](#abb7763cc16340d23bc7d687e60badcc0)。

<a id="r_af10735230c38d2b5a0baf5377212e827"></a>

```c
#define BT_FEAT_LE_ADV_CODING_SEL(feat)
```

相关声明：[BT_FEAT_LE_ADV_CODING_SEL](#af10735230c38d2b5a0baf5377212e827)。

<a id="r_aecf06a32c61c783305ad3817f9e5a596"></a>

```c
#define BT_FEAT_LE_ADV_CODING_SEL_HOST(feat)
```

相关声明：[BT_FEAT_LE_ADV_CODING_SEL_HOST](#aecf06a32c61c783305ad3817f9e5a596)。

<a id="r_ac5d15de2be03bc837afdb33905ea40be"></a>

```c
#define BT_FEAT_LE_PAWR_ADVERTISER(feat)
```

相关声明：[BT_FEAT_LE_PAWR_ADVERTISER](#ac5d15de2be03bc837afdb33905ea40be)。

<a id="r_a3ee6277e0e4db5e925912e8cb89269fa"></a>

```c
#define BT_FEAT_LE_PAWR_SCANNER(feat)
```

相关声明：[BT_FEAT_LE_PAWR_SCANNER](#a3ee6277e0e4db5e925912e8cb89269fa)。

<a id="r_a7b13b55fd2cfb4d756d3591215b47b7e"></a>

```c
#define BT_FEAT_LE_CHANNEL_SOUNDING(feat)
```

相关声明：[BT_FEAT_LE_CHANNEL_SOUNDING](#a7b13b55fd2cfb4d756d3591215b47b7e)。

<a id="r_aff2b8ca285698906deecfeff7447a74a"></a>

```c
#define BT_FEAT_LE_CHANNEL_SOUNDING_HOST(feat)
```

相关声明：[BT_FEAT_LE_CHANNEL_SOUNDING_HOST](#aff2b8ca285698906deecfeff7447a74a)。

<a id="r_a3d00c2d2897c0a994a136811d9e48f94"></a>

```c
#define BT_FEAT_LE_EXTENDED_FEAT_SET(feat)
```

相关声明：[BT_FEAT_LE_EXTENDED_FEAT_SET](#a3d00c2d2897c0a994a136811d9e48f94)。

<a id="r_aad2c245d9c1663da7a7ce91deaa1f252"></a>

```c
#define BT_FEAT_LE_FRAME_SPACE_UPDATE_SET(feat)
```

相关声明：[BT_FEAT_LE_FRAME_SPACE_UPDATE_SET](#aad2c245d9c1663da7a7ce91deaa1f252)。

<a id="r_a44f515be8315ee7dded3e3aa5c47a31c"></a>

```c
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS(feat)
```

相关声明：[BT_FEAT_LE_SHORTER_CONN_INTERVALS](#a44f515be8315ee7dded3e3aa5c47a31c)。

<a id="r_ac968c22e86f5b45fa10d109d47a1de33"></a>

```c
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS_HOST_SUPP(feat)
```

相关声明：[BT_FEAT_LE_SHORTER_CONN_INTERVALS_HOST_SUPP](#ac968c22e86f5b45fa10d109d47a1de33)。

<a id="r_abe5a1ddbede473f583106e3500dccdb1"></a>

```c
#define BT_FEAT_LE_CIS(feat)
```

相关声明：[BT_FEAT_LE_CIS](#abe5a1ddbede473f583106e3500dccdb1)。

<a id="r_a46b2f535c74178c8cc9359a7b1d2e140"></a>

```c
#define BT_FEAT_LE_BIS(feat)
```

相关声明：[BT_FEAT_LE_BIS](#a46b2f535c74178c8cc9359a7b1d2e140)。

<a id="r_a7b1b490bf00af8b0bf8ecbf4ef4aaba3"></a>

```c
#define BT_FEAT_LE_ISO(feat)
```

相关声明：[BT_FEAT_LE_ISO](#a7b1b490bf00af8b0bf8ecbf4ef4aaba3)。

<a id="r_abff5a0c6d1f3ab8ecf297d4ef29f7940"></a>

```c
#define BT_LE_STATES_PER_CONN_ADV(states)
```

相关声明：[BT_LE_STATES_PER_CONN_ADV](#abff5a0c6d1f3ab8ecf297d4ef29f7940)。

<a id="r_a9871a7d021f9e0bcfda278c82c3731d7"></a>

```c
#define BT_LE_STATES_SCAN_INIT(states)
```

相关声明：[BT_LE_STATES_SCAN_INIT](#a9871a7d021f9e0bcfda278c82c3731d7)。

<a id="r_ac886a10eed1313f6114fcfc3810a34f0"></a>

```c
#define BT_HCI_NO_BONDING 0x00
```

相关声明：[BT_HCI_NO_BONDING](#ac886a10eed1313f6114fcfc3810a34f0)。

<a id="r_a89c6d0d285c1c99c51c96d282fe593b9"></a>

```c
#define BT_HCI_NO_BONDING_MITM 0x01
```

相关声明：[BT_HCI_NO_BONDING_MITM](#a89c6d0d285c1c99c51c96d282fe593b9)。

<a id="r_aae1149095ff44d1b749e8b4b4d4aa32f"></a>

```c
#define BT_HCI_DEDICATED_BONDING 0x02
```

相关声明：[BT_HCI_DEDICATED_BONDING](#aae1149095ff44d1b749e8b4b4d4aa32f)。

<a id="r_aa1361f09852be86296cf91896d8f0853"></a>

```c
#define BT_HCI_DEDICATED_BONDING_MITM 0x03
```

相关声明：[BT_HCI_DEDICATED_BONDING_MITM](#aa1361f09852be86296cf91896d8f0853)。

<a id="r_ad777455cbcdfe02dd297dee5510e63b4"></a>

```c
#define BT_HCI_GENERAL_BONDING 0x04
```

相关声明：[BT_HCI_GENERAL_BONDING](#ad777455cbcdfe02dd297dee5510e63b4)。

<a id="r_a5b30ffdf3753d0a2a6c8ab025d32acef"></a>

```c
#define BT_HCI_GENERAL_BONDING_MITM 0x05
```

相关声明：[BT_HCI_GENERAL_BONDING_MITM](#a5b30ffdf3753d0a2a6c8ab025d32acef)。

<a id="r_a47ba0b282416c3e8f4275a38b7780b59"></a>

```c
#define BT_MITM 0x01
```

相关声明：[BT_MITM](#a47ba0b282416c3e8f4275a38b7780b59)。

<a id="r_ac656a702e4193044a59cac517099e2cf"></a>

```c
#define BT_IO_DISPLAY_ONLY 0x00
```

相关声明：[BT_IO_DISPLAY_ONLY](#ac656a702e4193044a59cac517099e2cf)。

<a id="r_a701d4fa8a4ebc07647f70264ad36153e"></a>

```c
#define BT_IO_DISPLAY_YESNO 0x01
```

相关声明：[BT_IO_DISPLAY_YESNO](#a701d4fa8a4ebc07647f70264ad36153e)。

<a id="r_a5a2a51ccedf3041c42ecdbd69e8c4a68"></a>

```c
#define BT_IO_KEYBOARD_ONLY 0x02
```

相关声明：[BT_IO_KEYBOARD_ONLY](#a5a2a51ccedf3041c42ecdbd69e8c4a68)。

<a id="r_ad68c0057160d5dacae12fce949fdaa32"></a>

```c
#define BT_IO_NO_INPUT_OUTPUT 0x03
```

相关声明：[BT_IO_NO_INPUT_OUTPUT](#ad68c0057160d5dacae12fce949fdaa32)。

<a id="r_aecb5b3886467c41baf979d01d8bde4a1"></a>

```c
#define HCI_PKT_TYPE_HV1 0x0020
```

相关声明：[HCI_PKT_TYPE_HV1](#aecb5b3886467c41baf979d01d8bde4a1)。

<a id="r_ae68633ce74639ec6f06d5ef4feee2d09"></a>

```c
#define HCI_PKT_TYPE_HV2 0x0040
```

相关声明：[HCI_PKT_TYPE_HV2](#ae68633ce74639ec6f06d5ef4feee2d09)。

<a id="r_aecd04ca27f536a1cb15aacf9ee80aba8"></a>

```c
#define HCI_PKT_TYPE_HV3 0x0080
```

相关声明：[HCI_PKT_TYPE_HV3](#aecd04ca27f536a1cb15aacf9ee80aba8)。

<a id="r_a4b048addd84409867177a97c785c4a73"></a>

```c
#define HCI_PKT_TYPE_SCO_HV1 0x0001
```

相关声明：[HCI_PKT_TYPE_SCO_HV1](#a4b048addd84409867177a97c785c4a73)。

<a id="r_a98f8217b27c0b9b7817c86520da45018"></a>

```c
#define HCI_PKT_TYPE_SCO_HV2 0x0002
```

相关声明：[HCI_PKT_TYPE_SCO_HV2](#a98f8217b27c0b9b7817c86520da45018)。

<a id="r_af67cdc23b6542e6d8323f14e17c7171d"></a>

```c
#define HCI_PKT_TYPE_SCO_HV3 0x0004
```

相关声明：[HCI_PKT_TYPE_SCO_HV3](#af67cdc23b6542e6d8323f14e17c7171d)。

<a id="r_a9530e916a0cf905e2185cd021320bfff"></a>

```c
#define HCI_PKT_TYPE_ESCO_EV3 0x0008
```

相关声明：[HCI_PKT_TYPE_ESCO_EV3](#a9530e916a0cf905e2185cd021320bfff)。

<a id="r_a3e0b6a1aa3818cb0c36f7883fd361c7e"></a>

```c
#define HCI_PKT_TYPE_ESCO_EV4 0x0010
```

相关声明：[HCI_PKT_TYPE_ESCO_EV4](#a3e0b6a1aa3818cb0c36f7883fd361c7e)。

<a id="r_a1f7474cb16a495bd81dc1f23d4103f70"></a>

```c
#define HCI_PKT_TYPE_ESCO_EV5 0x0020
```

相关声明：[HCI_PKT_TYPE_ESCO_EV5](#a1f7474cb16a495bd81dc1f23d4103f70)。

<a id="r_a1ccc4d6e5cfc560b7e2cb80c4c386607"></a>

```c
#define HCI_PKT_TYPE_ESCO_2EV3 0x0040
```

相关声明：[HCI_PKT_TYPE_ESCO_2EV3](#a1ccc4d6e5cfc560b7e2cb80c4c386607)。

<a id="r_ac5f09e3db1bc4d697ff705802e9ec3a0"></a>

```c
#define HCI_PKT_TYPE_ESCO_3EV3 0x0080
```

相关声明：[HCI_PKT_TYPE_ESCO_3EV3](#ac5f09e3db1bc4d697ff705802e9ec3a0)。

<a id="r_a1252be2692bcfb7a1256c63c4deed15d"></a>

```c
#define HCI_PKT_TYPE_ESCO_2EV5 0x0100
```

相关声明：[HCI_PKT_TYPE_ESCO_2EV5](#a1252be2692bcfb7a1256c63c4deed15d)。

<a id="r_aa45e51b1be89505fe599bc7983fcb950"></a>

```c
#define HCI_PKT_TYPE_ESCO_3EV5 0x0200
```

相关声明：[HCI_PKT_TYPE_ESCO_3EV5](#aa45e51b1be89505fe599bc7983fcb950)。

<a id="r_a8afe2c798b2d9657778f0815e3cb11c8"></a>

```c
#define ESCO_PKT_MASK
```

相关声明：[ESCO_PKT_MASK](#a8afe2c798b2d9657778f0815e3cb11c8)。

<a id="r_a1ef7929257a087f340f1f421cd8f51ce"></a>

```c
#define SCO_PKT_MASK
```

相关声明：[SCO_PKT_MASK](#a1ef7929257a087f340f1f421cd8f51ce)。

<a id="r_aa3a50b43beddbd76ae67b71e79a80175"></a>

```c
#define EDR_ESCO_PKT_MASK
```

相关声明：[EDR_ESCO_PKT_MASK](#aa3a50b43beddbd76ae67b71e79a80175)。

<a id="r_a5e79467b20a9173726c6be86b091e596"></a>

```c
#define BT_HCI_SCO 0x00
```

相关声明：[BT_HCI_SCO](#a5e79467b20a9173726c6be86b091e596)。

<a id="r_afee2289cd70b50f888518fd0b6b3f559"></a>

```c
#define BT_HCI_ACL 0x01
```

相关声明：[BT_HCI_ACL](#afee2289cd70b50f888518fd0b6b3f559)。

<a id="r_a4c57b051b336788e503a8521bb5ada80"></a>

```c
#define BT_HCI_ESCO 0x02
```

相关声明：[BT_HCI_ESCO](#a4c57b051b336788e503a8521bb5ada80)。

<a id="r_abb6c50fe170ffaaaf4a0827058331381"></a>

```c
#define BT_OGF_LINK_CTRL 0x01
```

相关声明：[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a1ec081ffdef36e4a6b32beafc5bf5b34"></a>

```c
#define BT_OGF_LINK_POLICY 0x02
```

相关声明：[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a2ac75061b53ef7fe66c8fd1dc4ab8ef4"></a>

```c
#define BT_OGF_BASEBAND 0x03
```

相关声明：[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_ac7c7348e291360169bf0ca5bb57b3d7e"></a>

```c
#define BT_OGF_INFO 0x04
```

相关声明：[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a5ce14b9103bd538f3610afd80284157e"></a>

```c
#define BT_OGF_STATUS 0x05
```

相关声明：[BT_OGF_STATUS](#a5ce14b9103bd538f3610afd80284157e)。

<a id="r_abb09db6a211185842f039eddb9fadca5"></a>

```c
#define BT_OGF_LE 0x08
```

相关声明：[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6b682cb6e4f489ffb67b05280b3dbd65"></a>

```c
#define BT_OGF_VS 0x3f
```

相关声明：[BT_OGF_VS](#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a7e006e0f69c498601f2c64a4ce3d8101"></a>

```c
#define BT_OP(ogf, ocf)
```

相关声明：[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)。

<a id="r_a1bf4881fa3237f4a5b22e5fdb417762b"></a>

```c
#define BT_OP_NOP 0x0000
```

相关声明：[BT_OP_NOP](#a1bf4881fa3237f4a5b22e5fdb417762b)。

<a id="r_af3ae81176a4ace13a562262ad53aeae6"></a>

```c
#define BT_OGF(opcode)
```

相关声明：[BT_OGF](#af3ae81176a4ace13a562262ad53aeae6)。

<a id="r_ac267cc5384724efba92df0be57379a89"></a>

```c
#define BT_OCF(opcode)
```

相关声明：[BT_OCF](#ac267cc5384724efba92df0be57379a89)。

<a id="r_adce48ff5cdde5f4f8ab5bc960717581a"></a>

```c
#define BT_HCI_OP_INQUIRY BT_OP(BT_OGF_LINK_CTRL, 0x0001) /* 0x0401 */
```

相关声明：[BT_HCI_OP_INQUIRY](#adce48ff5cdde5f4f8ab5bc960717581a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ae2d4e5e9cbf056bff03a668e74523442"></a>

```c
#define BT_HCI_OP_INQUIRY_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x0002) /* 0x0402 */
```

相关声明：[BT_HCI_OP_INQUIRY_CANCEL](#ae2d4e5e9cbf056bff03a668e74523442)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_addfd3dec2a69e7e5e2634c4fe63769f2"></a>

```c
#define BT_HCI_OP_CONNECT BT_OP(BT_OGF_LINK_CTRL, 0x0005) /* 0x0405 */
```

相关声明：[BT_HCI_OP_CONNECT](#addfd3dec2a69e7e5e2634c4fe63769f2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ab3d8612855550e52a0887e231371fbc2"></a>

```c
#define BT_HCI_OP_DISCONNECT BT_OP(BT_OGF_LINK_CTRL, 0x0006) /* 0x0406 */
```

相关声明：[BT_HCI_OP_DISCONNECT](#ab3d8612855550e52a0887e231371fbc2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ac50eb14115129bcc8c47016a6479149d"></a>

```c
#define BT_HCI_OP_CONNECT_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x0008) /* 0x0408 */
```

相关声明：[BT_HCI_OP_CONNECT_CANCEL](#ac50eb14115129bcc8c47016a6479149d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_af45bed44788b16be1b172c56c33eea34"></a>

```c
#define BT_HCI_OP_ACCEPT_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x0009) /* 0x0409 */
```

相关声明：[BT_HCI_OP_ACCEPT_CONN_REQ](#af45bed44788b16be1b172c56c33eea34)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_abf3f4da1f3de490c997e054bf29cc6e1"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_CVSD 0x00
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_CVSD](#abf3f4da1f3de490c997e054bf29cc6e1)。

<a id="r_acb33fc93ce1e276775d817972dabd2b1"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ULAW 0x01
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ULAW](#acb33fc93ce1e276775d817972dabd2b1)。

<a id="r_aad8fe65b6ce750e45f25af92707f85a2"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ALAW 0x02
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ALAW](#aad8fe65b6ce750e45f25af92707f85a2)。

<a id="r_ae52705d4968245a15c743afd15481702"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_TRANSPARENT 0x03
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_TRANSPARENT](#ae52705d4968245a15c743afd15481702)。

<a id="r_a69eba4973cb15e8b50bccb3f787a1b32"></a>

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_DEFAULT 0x00
```

相关声明：[BT_HCI_VOICE_SETTING_PCM_BIT_POS_DEFAULT](#a69eba4973cb15e8b50bccb3f787a1b32)。

<a id="r_ae0c3ab318909f00633efb3e6961ea663"></a>

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_8_BITS 0x00
```

相关声明：[BT_HCI_VOICE_SETTING_SAMPLE_SIZE_8_BITS](#ae0c3ab318909f00633efb3e6961ea663)。

<a id="r_a1369b9fe7bc657f5a2aec967faad0808"></a>

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_16_BITS 0x01
```

相关声明：[BT_HCI_VOICE_SETTING_SAMPLE_SIZE_16_BITS](#a1369b9fe7bc657f5a2aec967faad0808)。

<a id="r_af3ed0f4545c38aa48860ae0eac682b40"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_1_COMPLEMENT 0x00
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_1_COMPLEMENT](#af3ed0f4545c38aa48860ae0eac682b40)。

<a id="r_a370732fa8f51c824c784b084645ce437"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_2_COMPLEMENT 0x01
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_2_COMPLEMENT](#a370732fa8f51c824c784b084645ce437)。

<a id="r_a231c5dce10f275a96c5c5fd4afc13484"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_SIGNED 0x02
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_SIGNED](#a231c5dce10f275a96c5c5fd4afc13484)。

<a id="r_aadb335cd648a5e8942b4572e5623aec2"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_UNSIGNED 0x03
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_UNSIGNED](#aadb335cd648a5e8942b4572e5623aec2)。

<a id="r_ac6a8b4ce3e8ab55739c23cabe10df711"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_LINEAR 0x00
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_LINEAR](#ac6a8b4ce3e8ab55739c23cabe10df711)。

<a id="r_ab4b8b429d8b8c80b35bd0d8b7d9e03db"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_ULAW 0x01
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_ULAW](#ab4b8b429d8b8c80b35bd0d8b7d9e03db)。

<a id="r_a08e71787dd6643257e66d34e4ba92b1f"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_ALAW 0x02
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_ALAW](#a08e71787dd6643257e66d34e4ba92b1f)。

<a id="r_ab8d4ecdf12cf208bb39012b0aa6b2547"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK GENMASK(1, 0)
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK](#ab8d4ecdf12cf208bb39012b0aa6b2547)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a02fbd3478aad48191c1e68337070ff24"></a>

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK GENMASK(2, 4)
```

相关声明：[BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK](#a02fbd3478aad48191c1e68337070ff24)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a94baca9b3db3bff4abbbdddbbb571d0e"></a>

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK GENMASK(5, 5)
```

相关声明：[BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK](#a94baca9b3db3bff4abbbdddbbb571d0e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ac7fdeedc1f828f4add126a5f5b12c5d8"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_MASK GENMASK(7, 6)
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_MASK](#ac7fdeedc1f828f4add126a5f5b12c5d8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a05dce15a404d08bb44ccc73616a90082"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_MASK GENMASK(9, 8)
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_MASK](#a05dce15a404d08bb44ccc73616a90082)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a6570f5c7ac9cca8c4e27c60244b8cc4d"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP(val)
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP](#a6570f5c7ac9cca8c4e27c60244b8cc4d)。

<a id="r_aaa4ab55f0b2c5f7a1f23001d1b452e77"></a>

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP(val)
```

相关声明：[BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP](#aaa4ab55f0b2c5f7a1f23001d1b452e77)。

<a id="r_a7a0c75e8086231c6a3af00b0171b2437"></a>

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP(val)
```

相关声明：[BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP](#a7a0c75e8086231c6a3af00b0171b2437)。

<a id="r_a6f4d39439872aacfbed3deb5c80b3532"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_PREP(val)
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_PREP](#a6f4d39439872aacfbed3deb5c80b3532)。

<a id="r_ae44b949821dbed75ed1df869cfe5a8c2"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_PREP(val)
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_PREP](#ae44b949821dbed75ed1df869cfe5a8c2)。

<a id="r_af82c969110f65ad886997bfae3adcf3c"></a>

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_GET(val)
```

相关声明：[BT_HCI_VOICE_SETTING_AIR_CODING_FMT_GET](#af82c969110f65ad886997bfae3adcf3c)。

<a id="r_a4f930e86dcbeb4065220b2079245b54f"></a>

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_GET(val)
```

相关声明：[BT_HCI_VOICE_SETTING_PCM_BIT_POS_GET](#a4f930e86dcbeb4065220b2079245b54f)。

<a id="r_a054d5329a1c54b197b7a1d72a38e3c7e"></a>

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_GET(val)
```

相关声明：[BT_HCI_VOICE_SETTING_SAMPLE_SIZE_GET](#a054d5329a1c54b197b7a1d72a38e3c7e)。

<a id="r_abb4e34a3fd47ea87c1c2ba6319fe7327"></a>

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_GET(val)
```

相关声明：[BT_HCI_VOICE_SETTING_DATA_FMT_GET](#abb4e34a3fd47ea87c1c2ba6319fe7327)。

<a id="r_ad347325197bc72cf76cb457d7877ba36"></a>

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_GET(val)
```

相关声明：[BT_HCI_VOICE_SETTING_CODING_FMT_GET](#ad347325197bc72cf76cb457d7877ba36)。

<a id="r_ad3e5599b38db2c67e4b79396a29aa01f"></a>

```c
#define BT_HCI_VOICE_SETTINGS(air_coding_fmt, pcm_bit_pos, sample_size, data_fmt, coding_fmt)
```

相关声明：[BT_HCI_VOICE_SETTINGS](#ad3e5599b38db2c67e4b79396a29aa01f)。

<a id="r_a3efc934c628fb7712b8376d6754bee29"></a>

```c
#define BT_HCI_SCO_MAX_LATENCY_DEFAULT 0xffff /* do not care about SCO link latency */
```

相关声明：[BT_HCI_SCO_MAX_LATENCY_DEFAULT](#a3efc934c628fb7712b8376d6754bee29)。

<a id="r_a55e5c34e5388ca27dc0780a1e9950e85"></a>

```c
#define BT_HCI_SCO_RETRANS_EFFORT_DEFAULT 0xff /* do not care about SCO retransmission effort */
```

相关声明：[BT_HCI_SCO_RETRANS_EFFORT_DEFAULT](#a55e5c34e5388ca27dc0780a1e9950e85)。

<a id="r_ac4e12b8f7b89a658da7bbbaf371358e0"></a>

```c
#define BT_HCI_OP_SETUP_SYNC_CONN BT_OP(BT_OGF_LINK_CTRL, 0x0028) /* 0x0428 */
```

相关声明：[BT_HCI_OP_SETUP_SYNC_CONN](#ac4e12b8f7b89a658da7bbbaf371358e0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a97976c13fe03d346313bc19489d45360"></a>

```c
#define BT_HCI_OP_ACCEPT_SYNC_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x0029) /* 0x0429 */
```

相关声明：[BT_HCI_OP_ACCEPT_SYNC_CONN_REQ](#a97976c13fe03d346313bc19489d45360)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_aabb1f800ad4574e0350007af94cd786d"></a>

```c
#define BT_HCI_OP_REJECT_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x000a) /* 0x040a */
```

相关声明：[BT_HCI_OP_REJECT_CONN_REQ](#aabb1f800ad4574e0350007af94cd786d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a7da489e05d679c00f6cbbca0dfaaf136"></a>

```c
#define BT_HCI_OP_LINK_KEY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000b) /* 0x040b */
```

相关声明：[BT_HCI_OP_LINK_KEY_REPLY](#a7da489e05d679c00f6cbbca0dfaaf136)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a7db25bd8bdbd4351e0dcef1df8dc7077"></a>

```c
#define BT_HCI_OP_LINK_KEY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000c) /* 0x040c */
```

相关声明：[BT_HCI_OP_LINK_KEY_NEG_REPLY](#a7db25bd8bdbd4351e0dcef1df8dc7077)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a7713e5641070ac7fca91e027fc9b8c40"></a>

```c
#define BT_HCI_OP_PIN_CODE_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000d) /* 0x040d */
```

相关声明：[BT_HCI_OP_PIN_CODE_REPLY](#a7713e5641070ac7fca91e027fc9b8c40)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a5833de4cefd59cee9c614163de7e927b"></a>

```c
#define BT_HCI_OP_PIN_CODE_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000e) /* 0x040e */
```

相关声明：[BT_HCI_OP_PIN_CODE_NEG_REPLY](#a5833de4cefd59cee9c614163de7e927b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a8291666923a96840b1c15898d6013d66"></a>

```c
#define BT_HCI_OP_CHANGE_CONN_PACKET_TYPE BT_OP(BT_OGF_LINK_CTRL, 0x000f) /* 0x040f */
```

相关声明：[BT_HCI_OP_CHANGE_CONN_PACKET_TYPE](#a8291666923a96840b1c15898d6013d66)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

HCI 更改连接分组类型（Change Connection Packet Type）操作码（Opcode）。

<a id="r_ad7f6d9b786df4e2c8bca9b47bd5f6390"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH1 BIT(1)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_2DH1](#ad7f6d9b786df4e2c8bca9b47bd5f6390)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `2-DH1`。

<a id="r_a37863121200c9fbcbc9b61748909c796"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH1 BIT(2)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_3DH1](#a37863121200c9fbcbc9b61748909c796)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `3-DH1`。

<a id="r_aa677b6c5357585d36d81f0ea831e7568"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DM1 BIT(3)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DM1](#aa677b6c5357585d36d81f0ea831e7568)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DM1`。

<a id="r_ac0fe269d4e2d7f3794456f9a65e68113"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DH1 BIT(4)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DH1](#ac0fe269d4e2d7f3794456f9a65e68113)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DH1`。

<a id="r_adfc95ea6f5e2cc80af74138b27fae4b6"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH3 BIT(8)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_2DH3](#adfc95ea6f5e2cc80af74138b27fae4b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `2-DH3`。

<a id="r_abc26caf516ecfc413820e6bf0991010b"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH3 BIT(9)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_3DH3](#abc26caf516ecfc413820e6bf0991010b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `3-DH3`。

<a id="r_a72b4b642556556b959d6f9eda2a70770"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DM3 BIT(10)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DM3](#a72b4b642556556b959d6f9eda2a70770)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DM3`。

<a id="r_a972f90f9bfbf7b53d4f71f04d4c82ed5"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DH3 BIT(11)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DH3](#a972f90f9bfbf7b53d4f71f04d4c82ed5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DH3`。

<a id="r_ac75dba319c7875bbac25a3018bda5802"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH5 BIT(12)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_2DH5](#ac75dba319c7875bbac25a3018bda5802)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `2-DH5`。

<a id="r_a09023927fff243b8d2cc4c5223b42dca"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH5 BIT(13)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_NO_3DH5](#a09023927fff243b8d2cc4c5223b42dca)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

不得使用 `3-DH5`。

<a id="r_a23f80a9369c84786bff1330a4b07c3e7"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DM5 BIT(14)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DM5](#a23f80a9369c84786bff1330a4b07c3e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DM5`。

<a id="r_af4f275468c7d3266107587793a6be7c6"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_DH5 BIT(15)
```

相关声明：[BT_HCI_ACL_PKT_TYPE_DH5](#af4f275468c7d3266107587793a6be7c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

可以使用 `DH5`。

<a id="r_acc6b2545c83736d1b538e6c81d1f095c"></a>

```c
#define BT_HCI_ACL_PKT_TYPE_BR_MASK
```

相关声明：[BT_HCI_ACL_PKT_TYPE_BR_MASK](#acc6b2545c83736d1b538e6c81d1f095c)。

所有基本速率（Basic Rate，BR）ACL 分组类型的位掩码（Bitmask）。

<a id="r_a4c24e505f9c799275fc2f35619b7df97"></a>

```c
#define BT_HCI_OP_AUTH_REQUESTED BT_OP(BT_OGF_LINK_CTRL, 0x0011) /* 0x0411 */
```

相关声明：[BT_HCI_OP_AUTH_REQUESTED](#a4c24e505f9c799275fc2f35619b7df97)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ac32c04cf6bc9de299f0a307dbeed63f3"></a>

```c
#define BT_HCI_OP_SET_CONN_ENCRYPT BT_OP(BT_OGF_LINK_CTRL, 0x0013) /* 0x0413 */
```

相关声明：[BT_HCI_OP_SET_CONN_ENCRYPT](#ac32c04cf6bc9de299f0a307dbeed63f3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a2e759212d10ecd3a2e975379bf18d374"></a>

```c
#define BT_HCI_OP_REMOTE_NAME_REQUEST BT_OP(BT_OGF_LINK_CTRL, 0x0019) /* 0x0419 */
```

相关声明：[BT_HCI_OP_REMOTE_NAME_REQUEST](#a2e759212d10ecd3a2e975379bf18d374)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a76f79f4e14396297cc5db4ca8dba0c4c"></a>

```c
#define BT_HCI_OP_REMOTE_NAME_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x001a) /* 0x041a */
```

相关声明：[BT_HCI_OP_REMOTE_NAME_CANCEL](#a76f79f4e14396297cc5db4ca8dba0c4c)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ab6282249d4c14412674083007346b005"></a>

```c
#define BT_HCI_OP_READ_REMOTE_FEATURES BT_OP(BT_OGF_LINK_CTRL, 0x001b) /* 0x041b */
```

相关声明：[BT_HCI_OP_READ_REMOTE_FEATURES](#ab6282249d4c14412674083007346b005)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a87f6747b2b5d52a7886a1ec72100d9d0"></a>

```c
#define BT_HCI_OP_READ_REMOTE_EXT_FEATURES BT_OP(BT_OGF_LINK_CTRL, 0x001c) /* 0x041c */
```

相关声明：[BT_HCI_OP_READ_REMOTE_EXT_FEATURES](#a87f6747b2b5d52a7886a1ec72100d9d0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ae723b797305fe7a370b94d8c865e5708"></a>

```c
#define BT_HCI_OP_READ_REMOTE_VERSION_INFO BT_OP(BT_OGF_LINK_CTRL, 0x001d) /* 0x041d */
```

相关声明：[BT_HCI_OP_READ_REMOTE_VERSION_INFO](#ae723b797305fe7a370b94d8c865e5708)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a343a3c5c594dd25483fedf38c304a09a"></a>

```c
#define BT_HCI_OP_IO_CAPABILITY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002b) /* 0x042b */
```

相关声明：[BT_HCI_OP_IO_CAPABILITY_REPLY](#a343a3c5c594dd25483fedf38c304a09a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ab688441778a4239e1e8f2b2e0b74004f"></a>

```c
#define BT_HCI_OP_USER_CONFIRM_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002c) /* 0x042c */
```

相关声明：[BT_HCI_OP_USER_CONFIRM_REPLY](#ab688441778a4239e1e8f2b2e0b74004f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_aecc09326c190d2ab7b89f99375cd39bd"></a>

```c
#define BT_HCI_OP_USER_CONFIRM_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002d) /* 0x042d */
```

相关声明：[BT_HCI_OP_USER_CONFIRM_NEG_REPLY](#aecc09326c190d2ab7b89f99375cd39bd)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_ad1fce315b731f9978cd52a8c23994a10"></a>

```c
#define BT_HCI_OP_USER_PASSKEY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002e) /* 0x042e */
```

相关声明：[BT_HCI_OP_USER_PASSKEY_REPLY](#ad1fce315b731f9978cd52a8c23994a10)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a96f9c5c3439d829dfac94cca9ad1f015"></a>

```c
#define BT_HCI_OP_USER_PASSKEY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002f) /* 0x042f */
```

相关声明：[BT_HCI_OP_USER_PASSKEY_NEG_REPLY](#a96f9c5c3439d829dfac94cca9ad1f015)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a75d9a0acb6522dd0ae290572c4255540"></a>

```c
#define BT_HCI_OP_IO_CAPABILITY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x0034) /* 0x0434 */
```

相关声明：[BT_HCI_OP_IO_CAPABILITY_NEG_REPLY](#a75d9a0acb6522dd0ae290572c4255540)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_CTRL](#abb6c50fe170ffaaaf4a0827058331381)。

<a id="r_a58777d073768707b12220b7208aa0dcf"></a>

```c
#define BT_HCI_OP_SWITCH_ROLE BT_OP(BT_OGF_LINK_POLICY, 0x000b)
```

相关声明：[BT_HCI_OP_SWITCH_ROLE](#a58777d073768707b12220b7208aa0dcf)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a7fd831ad60e792a93724b6588e99574b"></a>

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_ROLE_SWITCH BIT(0)
```

相关声明：[BT_HCI_LINK_POLICY_SETTINGS_ENABLE_ROLE_SWITCH](#a7fd831ad60e792a93724b6588e99574b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac4681f15de605e921431b8cc673619ac"></a>

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_HOLD_MODE BIT(1)
```

相关声明：[BT_HCI_LINK_POLICY_SETTINGS_ENABLE_HOLD_MODE](#ac4681f15de605e921431b8cc673619ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afdbc756af5184efa28affc7f3c3aed97"></a>

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_SNIFF_SWITCH BIT(2)
```

相关声明：[BT_HCI_LINK_POLICY_SETTINGS_ENABLE_SNIFF_SWITCH](#afdbc756af5184efa28affc7f3c3aed97)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a37aedd6992f499b53ae16dea98be07d7"></a>

```c
#define BT_HCI_OP_READ_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000c)
```

相关声明：[BT_HCI_OP_READ_LINK_POLICY_SETTINGS](#a37aedd6992f499b53ae16dea98be07d7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a9b47fe0b9a5f34d031e9e45790f0522b"></a>

```c
#define BT_HCI_OP_WRITE_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000d)
```

相关声明：[BT_HCI_OP_WRITE_LINK_POLICY_SETTINGS](#a9b47fe0b9a5f34d031e9e45790f0522b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a0f01d3fc3b2cfb4287691b8f66a7cf71"></a>

```c
#define BT_HCI_OP_READ_DEFAULT_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000e)
```

相关声明：[BT_HCI_OP_READ_DEFAULT_LINK_POLICY_SETTINGS](#a0f01d3fc3b2cfb4287691b8f66a7cf71)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a4277a54a2dac31ac87b4f7841f871571"></a>

```c
#define BT_HCI_OP_WRITE_DEFAULT_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000f)
```

相关声明：[BT_HCI_OP_WRITE_DEFAULT_LINK_POLICY_SETTINGS](#a4277a54a2dac31ac87b4f7841f871571)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a65cd61abc9ad7854974fd98579ad41fe"></a>

```c
#define BT_HCI_OP_SNIFF_MODE BT_OP(BT_OGF_LINK_POLICY, 0x0003) /* 0x0803 */
```

相关声明：[BT_HCI_OP_SNIFF_MODE](#a65cd61abc9ad7854974fd98579ad41fe)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_a93951610963235f4ebd86e82c86a52a3"></a>

```c
#define BT_HCI_OP_EXIT_SNIFF_MODE BT_OP(BT_OGF_LINK_POLICY, 0x0004) /* 0x0804 */
```

相关声明：[BT_HCI_OP_EXIT_SNIFF_MODE](#a93951610963235f4ebd86e82c86a52a3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

<a id="r_af646337afbea8522c2617ddb525bdcf1"></a>

```c
#define BT_HCI_OP_SNIFF_SUBRATING BT_OP(BT_OGF_LINK_POLICY, 0x0011) /* 0x0811 */
```

相关声明：[BT_HCI_OP_SNIFF_SUBRATING](#af646337afbea8522c2617ddb525bdcf1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LINK_POLICY](#a1ec081ffdef36e4a6b32beafc5bf5b34)。

HCI Sniff 子速率（Sniff Subrating）命令操作码（Opcode）。

<a id="r_abb9bf6d936310a43c4a88244ad12640d"></a>

```c
#define BT_HCI_OP_SET_EVENT_MASK BT_OP(BT_OGF_BASEBAND, 0x0001) /* 0x0c01 */
```

相关声明：[BT_HCI_OP_SET_EVENT_MASK](#abb9bf6d936310a43c4a88244ad12640d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_abb515eb4ea9e66503bf1f375af01a6c0"></a>

```c
#define BT_HCI_OP_RESET BT_OP(BT_OGF_BASEBAND, 0x0003) /* 0x0c03 */
```

相关声明：[BT_HCI_OP_RESET](#abb515eb4ea9e66503bf1f375af01a6c0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a9b328487dbeeaa587e6f75011441f340"></a>

```c
#define BT_HCI_OP_WRITE_LOCAL_NAME BT_OP(BT_OGF_BASEBAND, 0x0013) /* 0x0c13 */
```

相关声明：[BT_HCI_OP_WRITE_LOCAL_NAME](#a9b328487dbeeaa587e6f75011441f340)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_af302a5e40644307f522154f3803572d0"></a>

```c
#define BT_HCI_OP_READ_CONN_ACCEPT_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0015) /* 0x0c15 */
```

相关声明：[BT_HCI_OP_READ_CONN_ACCEPT_TIMEOUT](#af302a5e40644307f522154f3803572d0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a6799bd267ef7c19b05ed2dd57baf0393"></a>

```c
#define BT_HCI_OP_WRITE_CONN_ACCEPT_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0016) /* 0x0c16 */
```

相关声明：[BT_HCI_OP_WRITE_CONN_ACCEPT_TIMEOUT](#a6799bd267ef7c19b05ed2dd57baf0393)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a5ef44fe1cca74a2258ffab1edd04acdf"></a>

```c
#define BT_HCI_OP_WRITE_PAGE_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0018) /* 0x0c18 */
```

相关声明：[BT_HCI_OP_WRITE_PAGE_TIMEOUT](#a5ef44fe1cca74a2258ffab1edd04acdf)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a0c8b9dc68ec6cd91ec0e9e565701a887"></a>

```c
#define BT_HCI_OP_WRITE_SCAN_ENABLE BT_OP(BT_OGF_BASEBAND, 0x001a) /* 0x0c1a */
```

相关声明：[BT_HCI_OP_WRITE_SCAN_ENABLE](#a0c8b9dc68ec6cd91ec0e9e565701a887)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a19b4c20d243de28462b686088e2971a3"></a>

```c
#define BT_BREDR_SCAN_DISABLED 0x00
```

相关声明：[BT_BREDR_SCAN_DISABLED](#a19b4c20d243de28462b686088e2971a3)。

<a id="r_a2f75eaee67bbb6c0211f3146d881278f"></a>

```c
#define BT_BREDR_SCAN_INQUIRY 0x01
```

相关声明：[BT_BREDR_SCAN_INQUIRY](#a2f75eaee67bbb6c0211f3146d881278f)。

<a id="r_a006d877a26f4e8dd0689b1324107a843"></a>

```c
#define BT_BREDR_SCAN_PAGE 0x02
```

相关声明：[BT_BREDR_SCAN_PAGE](#a006d877a26f4e8dd0689b1324107a843)。

<a id="r_a15a82766a1e11021d89a87e46fac6e91"></a>

```c
#define BT_HCI_OP_WRITE_PAGE_SCAN_ACTIVITY BT_OP(BT_OGF_BASEBAND, 0x001c) /* 0x0c1c */
```

相关声明：[BT_HCI_OP_WRITE_PAGE_SCAN_ACTIVITY](#a15a82766a1e11021d89a87e46fac6e91)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入寻呼扫描活动参数（Write Page Scan Activity）操作码。

<a id="r_a808b7afb7e390569f77d43602d894e34"></a>

```c
#define BT_HCI_OP_WRITE_INQUIRY_SCAN_ACTIVITY BT_OP(BT_OGF_BASEBAND, 0x001e) /* 0x0c1e */
```

相关声明：[BT_HCI_OP_WRITE_INQUIRY_SCAN_ACTIVITY](#a808b7afb7e390569f77d43602d894e34)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入查询扫描活动参数（Write Inquiry Scan Activity）操作码。

<a id="r_aa700370e995f2bfda85b385f70821c10"></a>

```c
#define BT_HCI_OP_READ_CLASS_OF_DEVICE BT_OP(BT_OGF_BASEBAND, 0x0023) /* 0x0c23 */
```

相关声明：[BT_HCI_OP_READ_CLASS_OF_DEVICE](#aa700370e995f2bfda85b385f70821c10)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_ace988e19fa62bf61654a329acaf99018"></a>

```c
#define BT_HCI_OP_WRITE_CLASS_OF_DEVICE BT_OP(BT_OGF_BASEBAND, 0x0024) /* 0x0c24 */
```

相关声明：[BT_HCI_OP_WRITE_CLASS_OF_DEVICE](#ace988e19fa62bf61654a329acaf99018)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_ac1ebc6168b2823aea2af2e2f89ffb6cd"></a>

```c
#define BT_TX_POWER_LEVEL_CURRENT 0x00
```

相关声明：[BT_TX_POWER_LEVEL_CURRENT](#ac1ebc6168b2823aea2af2e2f89ffb6cd)。

<a id="r_ad835bc44abee2e174f86cd55ac0338e3"></a>

```c
#define BT_TX_POWER_LEVEL_MAX 0x01
```

相关声明：[BT_TX_POWER_LEVEL_MAX](#ad835bc44abee2e174f86cd55ac0338e3)。

<a id="r_aaac00b7d9f9f96d1438643ee054ab21a"></a>

```c
#define BT_HCI_OP_READ_TX_POWER_LEVEL BT_OP(BT_OGF_BASEBAND, 0x002d) /* 0x0c2d */
```

相关声明：[BT_HCI_OP_READ_TX_POWER_LEVEL](#aaac00b7d9f9f96d1438643ee054ab21a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a740a01412d6fad277362634e1854f54b"></a>

```c
#define BT_HCI_LE_TX_POWER_PHY_1M 0x01
```

相关声明：[BT_HCI_LE_TX_POWER_PHY_1M](#a740a01412d6fad277362634e1854f54b)。

<a id="r_aa3eadebe7675de492b01ec117f72d808"></a>

```c
#define BT_HCI_LE_TX_POWER_PHY_2M 0x02
```

相关声明：[BT_HCI_LE_TX_POWER_PHY_2M](#aa3eadebe7675de492b01ec117f72d808)。

<a id="r_a66f2c7c03e65392c3477faddc14d9787"></a>

```c
#define BT_HCI_LE_TX_POWER_PHY_CODED_S8 0x03
```

相关声明：[BT_HCI_LE_TX_POWER_PHY_CODED_S8](#a66f2c7c03e65392c3477faddc14d9787)。

<a id="r_ab2bed6683929c37a3d087dba88309e45"></a>

```c
#define BT_HCI_LE_TX_POWER_PHY_CODED_S2 0x04
```

相关声明：[BT_HCI_LE_TX_POWER_PHY_CODED_S2](#ab2bed6683929c37a3d087dba88309e45)。

<a id="r_aebd5487b500c54a47a926bb1daa56f5e"></a>

```c
#define BT_HCI_OP_LE_ENH_READ_TX_POWER_LEVEL BT_OP(BT_OGF_LE, 0x0076) /* 0x2076 */
```

相关声明：[BT_HCI_OP_LE_ENH_READ_TX_POWER_LEVEL](#aebd5487b500c54a47a926bb1daa56f5e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac5bc187df83f28a48ba1f87f84aed54a"></a>

```c
#define BT_HCI_OP_LE_READ_REMOTE_TX_POWER_LEVEL BT_OP(BT_OGF_LE, 0x0077) /* 0x2077 */
```

相关声明：[BT_HCI_OP_LE_READ_REMOTE_TX_POWER_LEVEL](#ac5bc187df83f28a48ba1f87f84aed54a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a46bac5521c33da56df1d06ed7c472a06"></a>

```c
#define BT_HCI_LE_TX_POWER_REPORT_DISABLE 0x00
```

相关声明：[BT_HCI_LE_TX_POWER_REPORT_DISABLE](#a46bac5521c33da56df1d06ed7c472a06)。

<a id="r_a31f7372543b6dec580fe464ec011d752"></a>

```c
#define BT_HCI_LE_TX_POWER_REPORT_ENABLE 0x01
```

相关声明：[BT_HCI_LE_TX_POWER_REPORT_ENABLE](#a31f7372543b6dec580fe464ec011d752)。

<a id="r_aec22a58c052e856558b316b4f94f8561"></a>

```c
#define BT_HCI_OP_LE_SET_TX_POWER_REPORT_ENABLE BT_OP(BT_OGF_LE, 0x007A) /* 0x207A */
```

相关声明：[BT_HCI_OP_LE_SET_TX_POWER_REPORT_ENABLE](#aec22a58c052e856558b316b4f94f8561)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a48a3e41f8d6598e617d02ebc609911c6"></a>

```c
#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_PARAMETERS BT_OP(BT_OGF_LE, 0x0078) /* 0x2078 */
```

相关声明：[BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_PARAMETERS](#a48a3e41f8d6598e617d02ebc609911c6)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a9faae90b3adfcbcdf7da19c631e68a69"></a>

```c
#define BT_HCI_LE_PATH_LOSS_REPORTING_DISABLE 0x00
```

相关声明：[BT_HCI_LE_PATH_LOSS_REPORTING_DISABLE](#a9faae90b3adfcbcdf7da19c631e68a69)。

<a id="r_ab2e698e4ebbb45d9e3db0663ae5e4657"></a>

```c
#define BT_HCI_LE_PATH_LOSS_REPORTING_ENABLE 0x01
```

相关声明：[BT_HCI_LE_PATH_LOSS_REPORTING_ENABLE](#ab2e698e4ebbb45d9e3db0663ae5e4657)。

<a id="r_a09c0d554937de38a7b74661a2820237b"></a>

```c
#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_ENABLE BT_OP(BT_OGF_LE, 0x0079) /* 0x2079 */
```

相关声明：[BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_ENABLE](#a09c0d554937de38a7b74661a2820237b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a05c5f2cb7028e3ae831047e53b767836"></a>

```c
#define BT_HCI_OP_LE_SET_DEFAULT_SUBRATE BT_OP(BT_OGF_LE, 0x007D) /* 0x207D */
```

相关声明：[BT_HCI_OP_LE_SET_DEFAULT_SUBRATE](#a05c5f2cb7028e3ae831047e53b767836)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_af6825cfdac02620af56b8c747d1ef308"></a>

```c
#define BT_HCI_OP_LE_SUBRATE_REQUEST BT_OP(BT_OGF_LE, 0x007E) /* 0x207E */
```

相关声明：[BT_HCI_OP_LE_SUBRATE_REQUEST](#af6825cfdac02620af56b8c747d1ef308)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a252ef06a33818e117fc7f8146413cbd0"></a>

```c
#define BT_HCI_CTL_TO_HOST_FLOW_DISABLE 0x00
```

相关声明：[BT_HCI_CTL_TO_HOST_FLOW_DISABLE](#a252ef06a33818e117fc7f8146413cbd0)。

<a id="r_a4231ce6514091008191d5843b2c0b452"></a>

```c
#define BT_HCI_CTL_TO_HOST_FLOW_ENABLE 0x01
```

相关声明：[BT_HCI_CTL_TO_HOST_FLOW_ENABLE](#a4231ce6514091008191d5843b2c0b452)。

<a id="r_abe87fa64cb529d2cfe7ddf4fa045d3b5"></a>

```c
#define BT_HCI_OP_SET_CTL_TO_HOST_FLOW BT_OP(BT_OGF_BASEBAND, 0x0031) /* 0x0c31 */
```

相关声明：[BT_HCI_OP_SET_CTL_TO_HOST_FLOW](#abe87fa64cb529d2cfe7ddf4fa045d3b5)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a2e05f146890ad81be27dca91250bf69d"></a>

```c
#define BT_HCI_OP_HOST_BUFFER_SIZE BT_OP(BT_OGF_BASEBAND, 0x0033) /* 0x0c33 */
```

相关声明：[BT_HCI_OP_HOST_BUFFER_SIZE](#a2e05f146890ad81be27dca91250bf69d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a6c7afa8e3b324714bc5f8dce9702604d"></a>

```c
#define BT_HCI_OP_HOST_NUM_COMPLETED_PACKETS BT_OP(BT_OGF_BASEBAND, 0x0035) /* 0x0c35 */
```

相关声明：[BT_HCI_OP_HOST_NUM_COMPLETED_PACKETS](#a6c7afa8e3b324714bc5f8dce9702604d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a47baf48cd68227e3a7261653adc3f577"></a>

```c
#define BT_HCI_OP_READ_LINK_SUPERVISION_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0036) /* 0x0c36 */
```

相关声明：[BT_HCI_OP_READ_LINK_SUPERVISION_TIMEOUT](#a47baf48cd68227e3a7261653adc3f577)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 读取链路监督超时（Read Link Supervision Timeout）操作码。

<a id="r_a635b8ed8e93e89203b5ed16dbf5635d1"></a>

```c
#define BT_HCI_OP_WRITE_LINK_SUPERVISION_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0037) /* 0x0c37 */
```

相关声明：[BT_HCI_OP_WRITE_LINK_SUPERVISION_TIMEOUT](#a635b8ed8e93e89203b5ed16dbf5635d1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入链路监督超时（Write Link Supervision Timeout）操作码。

<a id="r_afd0a0fa1a8959d6390d59bd6d658432d"></a>

```c
#define BT_HCI_OP_WRITE_CURRENT_IAC_LAP BT_OP(BT_OGF_BASEBAND, 0x003a) /* 0x0c3a */
```

相关声明：[BT_HCI_OP_WRITE_CURRENT_IAC_LAP](#afd0a0fa1a8959d6390d59bd6d658432d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a8a3526f60f1d08f2cb63c2e26fae96b7"></a>

```c
#define BT_HCI_OP_WRITE_INQUIRY_SCAN_TYPE BT_OP(BT_OGF_BASEBAND, 0x0043) /* 0x0c43 */
```

相关声明：[BT_HCI_OP_WRITE_INQUIRY_SCAN_TYPE](#a8a3526f60f1d08f2cb63c2e26fae96b7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入查询扫描类型（Write Inquiry Scan Type）操作码。

<a id="r_a04985a29d0f131c09aeb9769689b727b"></a>

```c
#define BT_HCI_OP_WRITE_INQUIRY_MODE BT_OP(BT_OGF_BASEBAND, 0x0045) /* 0x0c45 */
```

相关声明：[BT_HCI_OP_WRITE_INQUIRY_MODE](#a04985a29d0f131c09aeb9769689b727b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a6b9898159d8f0259287704b2414b5511"></a>

```c
#define BT_HCI_OP_WRITE_PAGE_SCAN_TYPE BT_OP(BT_OGF_BASEBAND, 0x0047) /* 0x0c47 */
```

相关声明：[BT_HCI_OP_WRITE_PAGE_SCAN_TYPE](#a6b9898159d8f0259287704b2414b5511)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入寻呼扫描类型（Write Page Scan Type）操作码。

<a id="r_a08260407c93741e254a4427ba42c274d"></a>

```c
#define BT_HCI_EIR_MAX_DATA_LEN 240
```

相关声明：[BT_HCI_EIR_MAX_DATA_LEN](#a08260407c93741e254a4427ba42c274d)。

扩展查询响应（Extended Inquiry Response）数据的最大长度。

<a id="r_af9fce0fe5f15e5888a40d1d6c492fdc7"></a>

```c
#define BT_HCI_OP_WRITE_EXT_INQUIRY_RESPONSE BT_OP(BT_OGF_BASEBAND, 0x0052) /* 0x0c52 */
```

相关声明：[BT_HCI_OP_WRITE_EXT_INQUIRY_RESPONSE](#af9fce0fe5f15e5888a40d1d6c492fdc7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

HCI 写入扩展查询响应（Write Extended Inquiry Response）操作码。

<a id="r_ac7a73c5e38a2308d56f0dbaaf0a4795b"></a>

```c
#define BT_HCI_OP_WRITE_SSP_MODE BT_OP(BT_OGF_BASEBAND, 0x0056) /* 0x0c56 */
```

相关声明：[BT_HCI_OP_WRITE_SSP_MODE](#ac7a73c5e38a2308d56f0dbaaf0a4795b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_af5d2954950e00dfd5a69fc19db0fe530"></a>

```c
#define BT_HCI_OP_SET_EVENT_MASK_PAGE_2 BT_OP(BT_OGF_BASEBAND, 0x0063) /* 0x0c63 */
```

相关声明：[BT_HCI_OP_SET_EVENT_MASK_PAGE_2](#af5d2954950e00dfd5a69fc19db0fe530)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a2afc45fe32acff87265d36865c8d0b17"></a>

```c
#define BT_HCI_OP_LE_WRITE_LE_HOST_SUPP BT_OP(BT_OGF_BASEBAND, 0x006d) /* 0x0c6d */
```

相关声明：[BT_HCI_OP_LE_WRITE_LE_HOST_SUPP](#a2afc45fe32acff87265d36865c8d0b17)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a0480dd89b0f851d0a791b97138b01a5b"></a>

```c
#define BT_HCI_OP_WRITE_SC_HOST_SUPP BT_OP(BT_OGF_BASEBAND, 0x007a) /* 0x0c7a */
```

相关声明：[BT_HCI_OP_WRITE_SC_HOST_SUPP](#a0480dd89b0f851d0a791b97138b01a5b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a0ea6134bcd33e24b068f35d080cdc4e0"></a>

```c
#define BT_HCI_OP_READ_AUTH_PAYLOAD_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x007b) /* 0x0c7b */
```

相关声明：[BT_HCI_OP_READ_AUTH_PAYLOAD_TIMEOUT](#a0ea6134bcd33e24b068f35d080cdc4e0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_ae74450b7b643f947fa2e83a80e0e2fae"></a>

```c
#define BT_HCI_OP_WRITE_AUTH_PAYLOAD_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x007c) /* 0x0c7c */
```

相关声明：[BT_HCI_OP_WRITE_AUTH_PAYLOAD_TIMEOUT](#ae74450b7b643f947fa2e83a80e0e2fae)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_abc80a803d0e540541bcd889772e59940"></a>

```c
#define BT_HCI_OP_CONFIGURE_DATA_PATH BT_OP(BT_OGF_BASEBAND, 0x0083) /* 0x0c83 */
```

相关声明：[BT_HCI_OP_CONFIGURE_DATA_PATH](#abc80a803d0e540541bcd889772e59940)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_BASEBAND](#a2ac75061b53ef7fe66c8fd1dc4ab8ef4)。

<a id="r_a4947ee8a84f7cd81e242ee812b5b8760"></a>

```c
#define BT_HCI_VERSION_1_0B 0
```

相关声明：[BT_HCI_VERSION_1_0B](#a4947ee8a84f7cd81e242ee812b5b8760)。

版本（Version）1.0b。

<a id="r_a0fac5f104d8ab1539e84a900aafa9e43"></a>

```c
#define BT_HCI_VERSION_1_1 1
```

相关声明：[BT_HCI_VERSION_1_1](#a0fac5f104d8ab1539e84a900aafa9e43)。

版本（Version）1.1。

<a id="r_afe6fd8249a97d3762fe454bfb7eab021"></a>

```c
#define BT_HCI_VERSION_1_2 2
```

相关声明：[BT_HCI_VERSION_1_2](#afe6fd8249a97d3762fe454bfb7eab021)。

版本（Version）1.2。

<a id="r_afc0d24e2ba5e6b992aec81104cbf035e"></a>

```c
#define BT_HCI_VERSION_2_0 3
```

相关声明：[BT_HCI_VERSION_2_0](#afc0d24e2ba5e6b992aec81104cbf035e)。

版本（Version）2.0。

<a id="r_a98d73e8f548d5ae7eddff91a3e647aae"></a>

```c
#define BT_HCI_VERSION_2_1 4
```

相关声明：[BT_HCI_VERSION_2_1](#a98d73e8f548d5ae7eddff91a3e647aae)。

版本（Version）2.1。

<a id="r_acaf91cc6895552243c5b85c2fc007db5"></a>

```c
#define BT_HCI_VERSION_3_0 5
```

相关声明：[BT_HCI_VERSION_3_0](#acaf91cc6895552243c5b85c2fc007db5)。

版本（Version）3.0。

<a id="r_aeb77e725323c3f31c90482e676dad08a"></a>

```c
#define BT_HCI_VERSION_4_0 6
```

相关声明：[BT_HCI_VERSION_4_0](#aeb77e725323c3f31c90482e676dad08a)。

版本（Version）4.0。

<a id="r_a08cca779ede398a551359efccdaf3090"></a>

```c
#define BT_HCI_VERSION_4_1 7
```

相关声明：[BT_HCI_VERSION_4_1](#a08cca779ede398a551359efccdaf3090)。

版本（Version）4.1。

<a id="r_aa398d6e6fcca0b427a2ccd3a0a343835"></a>

```c
#define BT_HCI_VERSION_4_2 8
```

相关声明：[BT_HCI_VERSION_4_2](#aa398d6e6fcca0b427a2ccd3a0a343835)。

版本（Version）4.2。

<a id="r_a9a203a5a633d28c644b30125d437701a"></a>

```c
#define BT_HCI_VERSION_5_0 9
```

相关声明：[BT_HCI_VERSION_5_0](#a9a203a5a633d28c644b30125d437701a)。

版本（Version）5.0。

<a id="r_acfa0dbddfde8ee82b114dd34ff75c5bc"></a>

```c
#define BT_HCI_VERSION_5_1 10
```

相关声明：[BT_HCI_VERSION_5_1](#acfa0dbddfde8ee82b114dd34ff75c5bc)。

版本（Version）5.1。

<a id="r_aa4828a916c53d97de0541992d0359c09"></a>

```c
#define BT_HCI_VERSION_5_2 11
```

相关声明：[BT_HCI_VERSION_5_2](#aa4828a916c53d97de0541992d0359c09)。

版本（Version）5.2。

<a id="r_a37b04f40e68e821a1aac3b785903b379"></a>

```c
#define BT_HCI_VERSION_5_3 12
```

相关声明：[BT_HCI_VERSION_5_3](#a37b04f40e68e821a1aac3b785903b379)。

版本（Version）5.3。

<a id="r_ae8eadab2b7be415160f145bd63bae367"></a>

```c
#define BT_HCI_VERSION_5_4 13
```

相关声明：[BT_HCI_VERSION_5_4](#ae8eadab2b7be415160f145bd63bae367)。

版本（Version）5.4。

<a id="r_a66f6fbbc23991a16aa8bcfa2998f025f"></a>

```c
#define BT_HCI_VERSION_6_0 14
```

相关声明：[BT_HCI_VERSION_6_0](#a66f6fbbc23991a16aa8bcfa2998f025f)。

版本（Version）6.0。

<a id="r_a418b3f42ae31a5b4c92905602e54ac4b"></a>

```c
#define BT_HCI_VERSION_6_1 15
```

相关声明：[BT_HCI_VERSION_6_1](#a418b3f42ae31a5b4c92905602e54ac4b)。

版本（Version）6.1。

<a id="r_a440c203fc4aed922ef9e27ad90c8ad12"></a>

```c
#define BT_HCI_VERSION_6_2 16
```

相关声明：[BT_HCI_VERSION_6_2](#a440c203fc4aed922ef9e27ad90c8ad12)。

版本（Version）6.2。

<a id="r_ac458d1d93335e0c6562508ab9af48633"></a>

```c
#define BT_HCI_VERSION_6_3 17
```

相关声明：[BT_HCI_VERSION_6_3](#ac458d1d93335e0c6562508ab9af48633)。

版本（Version）6.3。

<a id="r_a195b8faf6d7d3e4f1b528185c73b4d67"></a>

```c
#define BT_HCI_OP_READ_LOCAL_VERSION_INFO BT_OP(BT_OGF_INFO, 0x0001) /* 0x1001 */
```

相关声明：[BT_HCI_OP_READ_LOCAL_VERSION_INFO](#a195b8faf6d7d3e4f1b528185c73b4d67)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_ac0d7533d221db0fa44cfb83135dfcc6a"></a>

```c
#define BT_HCI_OP_READ_SUPPORTED_COMMANDS BT_OP(BT_OGF_INFO, 0x0002) /* 0x1002 */
```

相关声明：[BT_HCI_OP_READ_SUPPORTED_COMMANDS](#ac0d7533d221db0fa44cfb83135dfcc6a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a882f120b35a9baa2f70bc33ef5ced6d3"></a>

```c
#define BT_HCI_OP_READ_LOCAL_EXT_FEATURES BT_OP(BT_OGF_INFO, 0x0004) /* 0x1004 */
```

相关声明：[BT_HCI_OP_READ_LOCAL_EXT_FEATURES](#a882f120b35a9baa2f70bc33ef5ced6d3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a8524505dff48ceb41c008c8662da6408"></a>

```c
#define BT_HCI_OP_READ_LOCAL_FEATURES BT_OP(BT_OGF_INFO, 0x0003) /* 0x1003 */
```

相关声明：[BT_HCI_OP_READ_LOCAL_FEATURES](#a8524505dff48ceb41c008c8662da6408)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_acd5d9ecda744969d4692e6ebface2e53"></a>

```c
#define BT_HCI_OP_READ_BUFFER_SIZE BT_OP(BT_OGF_INFO, 0x0005) /* 0x1005 */
```

相关声明：[BT_HCI_OP_READ_BUFFER_SIZE](#acd5d9ecda744969d4692e6ebface2e53)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a4ba1bf2078ac12686e2a7727f637f70b"></a>

```c
#define BT_HCI_OP_READ_BD_ADDR BT_OP(BT_OGF_INFO, 0x0009) /* 0x1009 */
```

相关声明：[BT_HCI_OP_READ_BD_ADDR](#a4ba1bf2078ac12686e2a7727f637f70b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a89eeffc2f46c776ecdb5eea81cb1f47a"></a>

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_ACL BIT(0)
```

相关声明：[BT_HCI_CODEC_TRANSPORT_MASK_BREDR_ACL](#a89eeffc2f46c776ecdb5eea81cb1f47a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab50b70f27bd9beb4da6fe8d4b91398c1"></a>

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_SCO BIT(1)
```

相关声明：[BT_HCI_CODEC_TRANSPORT_MASK_BREDR_SCO](#ab50b70f27bd9beb4da6fe8d4b91398c1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a38dd1118554de13f3f6f2853900212c5"></a>

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_CIS BIT(2)
```

相关声明：[BT_HCI_CODEC_TRANSPORT_MASK_LE_CIS](#a38dd1118554de13f3f6f2853900212c5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7d90fc1df2260a4067c3eb4ab169c406"></a>

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_BIS BIT(3)
```

相关声明：[BT_HCI_CODEC_TRANSPORT_MASK_LE_BIS](#a7d90fc1df2260a4067c3eb4ab169c406)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a73dfca6788b272380e6920d2907bf43f"></a>

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_ACL 0x00
```

相关声明：[BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_ACL](#a73dfca6788b272380e6920d2907bf43f)。

<a id="r_ad10d8c5ffd49cb183731a9ba97c0e058"></a>

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_SCO 0x01
```

相关声明：[BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_SCO](#ad10d8c5ffd49cb183731a9ba97c0e058)。

<a id="r_a5e53f28cedf59f18ce8d494f16933b3c"></a>

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_CIS 0x02
```

相关声明：[BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_CIS](#a5e53f28cedf59f18ce8d494f16933b3c)。

<a id="r_a560cb22e5f39c144e3d477eea5c32beb"></a>

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_BIS 0x03
```

相关声明：[BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_BIS](#a560cb22e5f39c144e3d477eea5c32beb)。

<a id="r_a0f74c19fabbcb3088e1a819d33a05a1c"></a>

```c
#define BT_HCI_DATAPATH_DIR_HOST_TO_CTLR 0x00
```

相关声明：[BT_HCI_DATAPATH_DIR_HOST_TO_CTLR](#a0f74c19fabbcb3088e1a819d33a05a1c)。

<a id="r_af8d89c712a3d27f9b6f92a31bea2a8c3"></a>

```c
#define BT_HCI_DATAPATH_DIR_CTLR_TO_HOST 0x01
```

相关声明：[BT_HCI_DATAPATH_DIR_CTLR_TO_HOST](#af8d89c712a3d27f9b6f92a31bea2a8c3)。

<a id="r_a5f748cb264265b9fc12f146ba47fa14c"></a>

```c
#define BT_HCI_DATAPATH_ID_HCI 0x00
```

相关声明：[BT_HCI_DATAPATH_ID_HCI](#a5f748cb264265b9fc12f146ba47fa14c)。

<a id="r_a0382b1713c7b2a774a8f004b6d1bc33f"></a>

```c
#define BT_HCI_DATAPATH_ID_VS 0x01
```

相关声明：[BT_HCI_DATAPATH_ID_VS](#a0382b1713c7b2a774a8f004b6d1bc33f)。

<a id="r_abf755f2839b36a3ac3431bff04193b2f"></a>

```c
#define BT_HCI_DATAPATH_ID_VS_END 0xfe
```

相关声明：[BT_HCI_DATAPATH_ID_VS_END](#abf755f2839b36a3ac3431bff04193b2f)。

<a id="r_a4f4939e7fa43ab73861f64d25b6549d8"></a>

```c
#define BT_HCI_CODING_FORMAT_ULAW_LOG 0x00
```

相关声明：[BT_HCI_CODING_FORMAT_ULAW_LOG](#a4f4939e7fa43ab73861f64d25b6549d8)。

<a id="r_a36f18d10467a580e9864eb8629b8ce01"></a>

```c
#define BT_HCI_CODING_FORMAT_ALAW_LOG 0x01
```

相关声明：[BT_HCI_CODING_FORMAT_ALAW_LOG](#a36f18d10467a580e9864eb8629b8ce01)。

<a id="r_a80dc369e54038df30f44ca4c13ee14d6"></a>

```c
#define BT_HCI_CODING_FORMAT_CVSD 0x02
```

相关声明：[BT_HCI_CODING_FORMAT_CVSD](#a80dc369e54038df30f44ca4c13ee14d6)。

<a id="r_ad93af498e2265c180a01055eca2a4de0"></a>

```c
#define BT_HCI_CODING_FORMAT_TRANSPARENT 0x03
```

相关声明：[BT_HCI_CODING_FORMAT_TRANSPARENT](#ad93af498e2265c180a01055eca2a4de0)。

<a id="r_a2630de3f8cc3ccc3d81f0f2fa4084587"></a>

```c
#define BT_HCI_CODING_FORMAT_LINEAR_PCM 0x04
```

相关声明：[BT_HCI_CODING_FORMAT_LINEAR_PCM](#a2630de3f8cc3ccc3d81f0f2fa4084587)。

<a id="r_a9178f80b7783c9cffb4574667d3033af"></a>

```c
#define BT_HCI_CODING_FORMAT_MSBC 0x05
```

相关声明：[BT_HCI_CODING_FORMAT_MSBC](#a9178f80b7783c9cffb4574667d3033af)。

<a id="r_a1fa62d6f28ef56ebe9c18d5ab86fbf8e"></a>

```c
#define BT_HCI_CODING_FORMAT_LC3 0x06
```

相关声明：[BT_HCI_CODING_FORMAT_LC3](#a1fa62d6f28ef56ebe9c18d5ab86fbf8e)。

<a id="r_a405e22871772b5155f99774178e4093d"></a>

```c
#define BT_HCI_CODING_FORMAT_G729A 0x07
```

相关声明：[BT_HCI_CODING_FORMAT_G729A](#a405e22871772b5155f99774178e4093d)。

<a id="r_a46839c453b81e80fb8e578f89dc31864"></a>

```c
#define BT_HCI_CODING_FORMAT_VS 0xFF
```

相关声明：[BT_HCI_CODING_FORMAT_VS](#a46839c453b81e80fb8e578f89dc31864)。

<a id="r_a8755487f4672f196051cc513894e4603"></a>

```c
#define BT_HCI_OP_READ_CODECS BT_OP(BT_OGF_INFO, 0x000b) /* 0x100b */
```

相关声明：[BT_HCI_OP_READ_CODECS](#a8755487f4672f196051cc513894e4603)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_acb09b1a94453c1c341decabc029bbc04"></a>

```c
#define BT_HCI_OP_READ_CODECS_V2 BT_OP(BT_OGF_INFO, 0x000d) /* 0x100d */
```

相关声明：[BT_HCI_OP_READ_CODECS_V2](#acb09b1a94453c1c341decabc029bbc04)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a4b9e24d16cd92ce6ee1d6444410cfb43"></a>

```c
#define BT_HCI_OP_READ_CODEC_CAPABILITIES BT_OP(BT_OGF_INFO, 0x000e) /* 0x100e */
```

相关声明：[BT_HCI_OP_READ_CODEC_CAPABILITIES](#a4b9e24d16cd92ce6ee1d6444410cfb43)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a9a183b26d18453d5daa6de2dcbe4d9a1"></a>

```c
#define BT_HCI_OP_READ_CTLR_DELAY BT_OP(BT_OGF_INFO, 0x000f) /* 0x100f */
```

相关声明：[BT_HCI_OP_READ_CTLR_DELAY](#a9a183b26d18453d5daa6de2dcbe4d9a1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_INFO](#ac7c7348e291360169bf0ca5bb57b3d7e)。

<a id="r_a528902591490d9d20a6966a042254b3a"></a>

```c
#define BT_HCI_OP_READ_RSSI BT_OP(BT_OGF_STATUS, 0x0005) /* 0x1405 */
```

相关声明：[BT_HCI_OP_READ_RSSI](#a528902591490d9d20a6966a042254b3a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_STATUS](#a5ce14b9103bd538f3610afd80284157e)。

<a id="r_ab4eedd90a583b3893c77f51aee16e3c0"></a>

```c
#define BT_HCI_ENCRYPTION_KEY_SIZE_MIN 7
```

相关声明：[BT_HCI_ENCRYPTION_KEY_SIZE_MIN](#ab4eedd90a583b3893c77f51aee16e3c0)。

<a id="r_ae4271fbdb039750aceac7c0712d4f3db"></a>

```c
#define BT_HCI_ENCRYPTION_KEY_SIZE_MAX 16
```

相关声明：[BT_HCI_ENCRYPTION_KEY_SIZE_MAX](#ae4271fbdb039750aceac7c0712d4f3db)。

<a id="r_adefeb2117010fa2d53937ce513e28a18"></a>

```c
#define BT_HCI_OP_READ_ENCRYPTION_KEY_SIZE BT_OP(BT_OGF_STATUS, 0x0008) /* 0x1408 */
```

相关声明：[BT_HCI_OP_READ_ENCRYPTION_KEY_SIZE](#adefeb2117010fa2d53937ce513e28a18)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_STATUS](#a5ce14b9103bd538f3610afd80284157e)。

<a id="r_aa9a3688473bf15c8845f52a3128362f7"></a>

```c
#define BT_HCI_OP_LE_SET_EVENT_MASK BT_OP(BT_OGF_LE, 0x0001) /* 0x2001 */
```

相关声明：[BT_HCI_OP_LE_SET_EVENT_MASK](#aa9a3688473bf15c8845f52a3128362f7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a965e30fec3f9b5956bd2ea38e57b8b00"></a>

```c
#define BT_HCI_OP_LE_READ_BUFFER_SIZE BT_OP(BT_OGF_LE, 0x0002) /* 0x2002 */
```

相关声明：[BT_HCI_OP_LE_READ_BUFFER_SIZE](#a965e30fec3f9b5956bd2ea38e57b8b00)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae4e1d6098793b91ee0e4974886b98336"></a>

```c
#define BT_HCI_OP_LE_READ_LOCAL_FEATURES BT_OP(BT_OGF_LE, 0x0003) /* 0x2003 */
```

相关声明：[BT_HCI_OP_LE_READ_LOCAL_FEATURES](#ae4e1d6098793b91ee0e4974886b98336)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_af34eced252d01bbc27bd8e19ed4dc80e"></a>

```c
#define BT_HCI_OP_LE_SET_RANDOM_ADDRESS BT_OP(BT_OGF_LE, 0x0005) /* 0x2005 */
```

相关声明：[BT_HCI_OP_LE_SET_RANDOM_ADDRESS](#af34eced252d01bbc27bd8e19ed4dc80e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a338499e51470b8910e9f663be8f55db5"></a>

```c
#define BT_HCI_ADV_IND 0x00
```

相关声明：[BT_HCI_ADV_IND](#a338499e51470b8910e9f663be8f55db5)。

<a id="r_afaecb8d6be1b1c0ce98db7edd8bad343"></a>

```c
#define BT_HCI_ADV_DIRECT_IND 0x01
```

相关声明：[BT_HCI_ADV_DIRECT_IND](#afaecb8d6be1b1c0ce98db7edd8bad343)。

<a id="r_ae94df1ac3bc14f42be1207531872104a"></a>

```c
#define BT_HCI_ADV_SCAN_IND 0x02
```

相关声明：[BT_HCI_ADV_SCAN_IND](#ae94df1ac3bc14f42be1207531872104a)。

<a id="r_a48e13ce185bf9612455c49484ff80bb9"></a>

```c
#define BT_HCI_ADV_NONCONN_IND 0x03
```

相关声明：[BT_HCI_ADV_NONCONN_IND](#a48e13ce185bf9612455c49484ff80bb9)。

<a id="r_a67c1c0c5349b2de661030138185d7b0d"></a>

```c
#define BT_HCI_ADV_DIRECT_IND_LOW_DUTY 0x04
```

相关声明：[BT_HCI_ADV_DIRECT_IND_LOW_DUTY](#a67c1c0c5349b2de661030138185d7b0d)。

<a id="r_afb3e678c87b81f9348749f1c5721ce26"></a>

```c
#define BT_HCI_ADV_SCAN_RSP 0x04
```

相关声明：[BT_HCI_ADV_SCAN_RSP](#afb3e678c87b81f9348749f1c5721ce26)。

<a id="r_ac89392b0484164812b77360d15d9984b"></a>

```c
#define BT_LE_ADV_INTERVAL_MIN 0x0020
```

相关声明：[BT_LE_ADV_INTERVAL_MIN](#ac89392b0484164812b77360d15d9984b)。

<a id="r_a6479fb2c964155cfcdd3cc48c3a45618"></a>

```c
#define BT_LE_ADV_INTERVAL_MAX 0x4000
```

相关声明：[BT_LE_ADV_INTERVAL_MAX](#a6479fb2c964155cfcdd3cc48c3a45618)。

<a id="r_af698d1a0fa7a384e2fa1231edec00caa"></a>

```c
#define BT_LE_EXT_ADV_INTERVAL_MAX 0xFFFFFFU
```

相关声明：[BT_LE_EXT_ADV_INTERVAL_MAX](#af698d1a0fa7a384e2fa1231edec00caa)。

最大低功耗蓝牙扩展广播间隔（LE Extended Advertising Interval）：`0xFFFFFF`，以 0.625 ms 为单位。

<a id="r_a607201e55561cdccf34e18ceac0f23b7"></a>

```c
#define BT_LE_ADV_INTERVAL_DEFAULT 0x0800
```

相关声明：[BT_LE_ADV_INTERVAL_DEFAULT](#a607201e55561cdccf34e18ceac0f23b7)。

<a id="r_af9652f7d96b61e7cc9f44f3d923bd962"></a>

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_37 0x01
```

相关声明：[BT_LE_ADV_CHAN_MAP_CHAN_37](#af9652f7d96b61e7cc9f44f3d923bd962)。

<a id="r_a07c18344ec56b22c8a3e902bc53ba191"></a>

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_38 0x02
```

相关声明：[BT_LE_ADV_CHAN_MAP_CHAN_38](#a07c18344ec56b22c8a3e902bc53ba191)。

<a id="r_a14be9af8f16dcdf70aebf251bcfb52f3"></a>

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_39 0x04
```

相关声明：[BT_LE_ADV_CHAN_MAP_CHAN_39](#a14be9af8f16dcdf70aebf251bcfb52f3)。

<a id="r_af96bfa8c912e66233f64b7cc1844b82e"></a>

```c
#define BT_LE_ADV_CHAN_MAP_ALL 0x07
```

相关声明：[BT_LE_ADV_CHAN_MAP_ALL](#af96bfa8c912e66233f64b7cc1844b82e)。

<a id="r_abc1615c8d22ab64844c3f3394023c1b4"></a>

```c
#define BT_LE_ADV_FP_NO_FILTER 0x00
```

相关声明：[BT_LE_ADV_FP_NO_FILTER](#abc1615c8d22ab64844c3f3394023c1b4)。

<a id="r_aba027e2aeacea1040c3b45ccaeb23d3c"></a>

```c
#define BT_LE_ADV_FP_FILTER_SCAN_REQ 0x01
```

相关声明：[BT_LE_ADV_FP_FILTER_SCAN_REQ](#aba027e2aeacea1040c3b45ccaeb23d3c)。

<a id="r_a5f3d27b78705afc3abff35e353eee9fa"></a>

```c
#define BT_LE_ADV_FP_FILTER_CONN_IND 0x02
```

相关声明：[BT_LE_ADV_FP_FILTER_CONN_IND](#a5f3d27b78705afc3abff35e353eee9fa)。

<a id="r_a980ff7f9bf7154c7866b5e302a1f2a55"></a>

```c
#define BT_LE_ADV_FP_FILTER_BOTH 0x03
```

相关声明：[BT_LE_ADV_FP_FILTER_BOTH](#a980ff7f9bf7154c7866b5e302a1f2a55)。

<a id="r_a446b6e7a74800ee657f5ddcf1c198d02"></a>

```c
#define BT_HCI_OP_LE_SET_ADV_PARAM BT_OP(BT_OGF_LE, 0x0006) /* 0x2006 */
```

相关声明：[BT_HCI_OP_LE_SET_ADV_PARAM](#a446b6e7a74800ee657f5ddcf1c198d02)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_afd47d6bbfd4688383aaa6b5014cf0019"></a>

```c
#define BT_HCI_OP_LE_READ_ADV_CHAN_TX_POWER BT_OP(BT_OGF_LE, 0x0007) /* 0x2007 */
```

相关声明：[BT_HCI_OP_LE_READ_ADV_CHAN_TX_POWER](#afd47d6bbfd4688383aaa6b5014cf0019)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_adb8f5236ac1b5eaa4c82d620c78c45aa"></a>

```c
#define BT_HCI_OP_LE_SET_ADV_DATA BT_OP(BT_OGF_LE, 0x0008) /* 0x2008 */
```

相关声明：[BT_HCI_OP_LE_SET_ADV_DATA](#adb8f5236ac1b5eaa4c82d620c78c45aa)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a81718bfe6796648eb5831f3cd03049c8"></a>

```c
#define BT_HCI_OP_LE_SET_SCAN_RSP_DATA BT_OP(BT_OGF_LE, 0x0009) /* 0x2009 */
```

相关声明：[BT_HCI_OP_LE_SET_SCAN_RSP_DATA](#a81718bfe6796648eb5831f3cd03049c8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae8361a3ca39019757304034c32391b47"></a>

```c
#define BT_HCI_LE_ADV_DISABLE 0x00
```

相关声明：[BT_HCI_LE_ADV_DISABLE](#ae8361a3ca39019757304034c32391b47)。

<a id="r_a6b8140956fbf85bd5aab2f1974b673f9"></a>

```c
#define BT_HCI_LE_ADV_ENABLE 0x01
```

相关声明：[BT_HCI_LE_ADV_ENABLE](#a6b8140956fbf85bd5aab2f1974b673f9)。

<a id="r_a5f218883bda0698b5c52fd6a34d5e9f0"></a>

```c
#define BT_HCI_OP_LE_SET_ADV_ENABLE BT_OP(BT_OGF_LE, 0x000a) /* 0x200a */
```

相关声明：[BT_HCI_OP_LE_SET_ADV_ENABLE](#a5f218883bda0698b5c52fd6a34d5e9f0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a56db98b00b57fd713f8cedbf34e2f8fa"></a>

```c
#define BT_HCI_OP_LE_SET_SCAN_PARAM BT_OP(BT_OGF_LE, 0x000b) /* 0x200b */
```

相关声明：[BT_HCI_OP_LE_SET_SCAN_PARAM](#a56db98b00b57fd713f8cedbf34e2f8fa)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2274aacde21083e9633fe59fbff0df87"></a>

```c
#define BT_HCI_LE_SCAN_PASSIVE 0x00
```

相关声明：[BT_HCI_LE_SCAN_PASSIVE](#a2274aacde21083e9633fe59fbff0df87)。

<a id="r_ac13c2e39ac1e13cf5cd2cfa248a6f316"></a>

```c
#define BT_HCI_LE_SCAN_ACTIVE 0x01
```

相关声明：[BT_HCI_LE_SCAN_ACTIVE](#ac13c2e39ac1e13cf5cd2cfa248a6f316)。

<a id="r_a278ccd7cfefd1a46f6de843b722f583a"></a>

```c
#define BT_HCI_LE_SCAN_FP_BASIC_NO_FILTER 0x00
```

相关声明：[BT_HCI_LE_SCAN_FP_BASIC_NO_FILTER](#a278ccd7cfefd1a46f6de843b722f583a)。

<a id="r_ac6f3763ab47d20efee1af16d8d019bf3"></a>

```c
#define BT_HCI_LE_SCAN_FP_BASIC_FILTER 0x01
```

相关声明：[BT_HCI_LE_SCAN_FP_BASIC_FILTER](#ac6f3763ab47d20efee1af16d8d019bf3)。

<a id="r_aed7fa63104bbc551bc0dbfa21e38744a"></a>

```c
#define BT_HCI_LE_SCAN_FP_EXT_NO_FILTER 0x02
```

相关声明：[BT_HCI_LE_SCAN_FP_EXT_NO_FILTER](#aed7fa63104bbc551bc0dbfa21e38744a)。

<a id="r_a45846e02e2630608b14f62f9b9020f9d"></a>

```c
#define BT_HCI_LE_SCAN_FP_EXT_FILTER 0x03
```

相关声明：[BT_HCI_LE_SCAN_FP_EXT_FILTER](#a45846e02e2630608b14f62f9b9020f9d)。

<a id="r_a894cf6904ec16b11f6d930d72d30fce6"></a>

```c
#define BT_HCI_OP_LE_SET_SCAN_ENABLE BT_OP(BT_OGF_LE, 0x000c) /* 0x200c */
```

相关声明：[BT_HCI_OP_LE_SET_SCAN_ENABLE](#a894cf6904ec16b11f6d930d72d30fce6)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a152712b517c9ee0452555408d14bbfa7"></a>

```c
#define BT_HCI_LE_SCAN_DISABLE 0x00
```

相关声明：[BT_HCI_LE_SCAN_DISABLE](#a152712b517c9ee0452555408d14bbfa7)。

<a id="r_a6859aeda42fe72b75d5cc1896b7e6afd"></a>

```c
#define BT_HCI_LE_SCAN_ENABLE 0x01
```

相关声明：[BT_HCI_LE_SCAN_ENABLE](#a6859aeda42fe72b75d5cc1896b7e6afd)。

<a id="r_a6fb35a340e8eecd7bc2602ed010aa6c1"></a>

```c
#define BT_HCI_LE_SCAN_FILTER_DUP_DISABLE 0x00
```

相关声明：[BT_HCI_LE_SCAN_FILTER_DUP_DISABLE](#a6fb35a340e8eecd7bc2602ed010aa6c1)。

<a id="r_a4c9503d4a13f78a1dc44e087af922793"></a>

```c
#define BT_HCI_LE_SCAN_FILTER_DUP_ENABLE 0x01
```

相关声明：[BT_HCI_LE_SCAN_FILTER_DUP_ENABLE](#a4c9503d4a13f78a1dc44e087af922793)。

<a id="r_aadde6f016c942c7907afddf7b6c94304"></a>

```c
#define BT_HCI_OP_LE_CREATE_CONN BT_OP(BT_OGF_LE, 0x000d) /* 0x200d */
```

相关声明：[BT_HCI_OP_LE_CREATE_CONN](#aadde6f016c942c7907afddf7b6c94304)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae1bd495a90fd902614014e7e1e2f1239"></a>

```c
#define BT_HCI_LE_CREATE_CONN_FP_NO_FILTER 0x00
```

相关声明：[BT_HCI_LE_CREATE_CONN_FP_NO_FILTER](#ae1bd495a90fd902614014e7e1e2f1239)。

<a id="r_ac04c2c0020d2972d6df169f39c421c08"></a>

```c
#define BT_HCI_LE_CREATE_CONN_FP_FILTER 0x01
```

相关声明：[BT_HCI_LE_CREATE_CONN_FP_FILTER](#ac04c2c0020d2972d6df169f39c421c08)。

<a id="r_acacd0832cddc00702da74b4a36e5c825"></a>

```c
#define BT_HCI_OP_LE_CREATE_CONN_CANCEL BT_OP(BT_OGF_LE, 0x000e) /* 0x200e */
```

相关声明：[BT_HCI_OP_LE_CREATE_CONN_CANCEL](#acacd0832cddc00702da74b4a36e5c825)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aeeba2e21bd5e33abbd48fa18f5e252f3"></a>

```c
#define BT_HCI_OP_LE_READ_FAL_SIZE BT_OP(BT_OGF_LE, 0x000f) /* 0x200f */
```

相关声明：[BT_HCI_OP_LE_READ_FAL_SIZE](#aeeba2e21bd5e33abbd48fa18f5e252f3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a592ce45c74bdabf1b25954b8021a50bb"></a>

```c
#define BT_HCI_OP_LE_CLEAR_FAL BT_OP(BT_OGF_LE, 0x0010) /* 0x2010 */
```

相关声明：[BT_HCI_OP_LE_CLEAR_FAL](#a592ce45c74bdabf1b25954b8021a50bb)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a103c6fada57c61fc3f994f8902f4123c"></a>

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_FAL BT_OP(BT_OGF_LE, 0x0011) /* 0x2011 */
```

相关声明：[BT_HCI_OP_LE_ADD_DEV_TO_FAL](#a103c6fada57c61fc3f994f8902f4123c)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aedbb03b04ed567e54642e42ae758538a"></a>

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_FAL BT_OP(BT_OGF_LE, 0x0012) /* 0x2012 */
```

相关声明：[BT_HCI_OP_LE_REM_DEV_FROM_FAL](#aedbb03b04ed567e54642e42ae758538a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac0c308b64ed89c9b7326982ef04ba6d3"></a>

```c
#define BT_HCI_OP_LE_CONN_UPDATE BT_OP(BT_OGF_LE, 0x0013) /* 0x2013 */
```

相关声明：[BT_HCI_OP_LE_CONN_UPDATE](#ac0c308b64ed89c9b7326982ef04ba6d3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6224aab014342d93bcb16c717cd52421"></a>

```c
#define BT_HCI_OP_LE_SET_HOST_CHAN_CLASSIF BT_OP(BT_OGF_LE, 0x0014) /* 0x2014 */
```

相关声明：[BT_HCI_OP_LE_SET_HOST_CHAN_CLASSIF](#a6224aab014342d93bcb16c717cd52421)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a9040e4b5e719d53cc324faa280a670a4"></a>

```c
#define BT_HCI_OP_LE_READ_CHAN_MAP BT_OP(BT_OGF_LE, 0x0015) /* 0x2015 */
```

相关声明：[BT_HCI_OP_LE_READ_CHAN_MAP](#a9040e4b5e719d53cc324faa280a670a4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac8d5165a3a5d190b8e2d31feb79a17c9"></a>

```c
#define BT_HCI_OP_LE_READ_REMOTE_FEATURES BT_OP(BT_OGF_LE, 0x0016) /* 0x2016 */
```

相关声明：[BT_HCI_OP_LE_READ_REMOTE_FEATURES](#ac8d5165a3a5d190b8e2d31feb79a17c9)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a99fdd1dbff627a2f627e7d9eced68326"></a>

```c
#define BT_HCI_OP_LE_ENCRYPT BT_OP(BT_OGF_LE, 0x0017) /* 0x2017 */
```

相关声明：[BT_HCI_OP_LE_ENCRYPT](#a99fdd1dbff627a2f627e7d9eced68326)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac3af817deaf472dbb2a825fd57b67f42"></a>

```c
#define BT_HCI_OP_LE_RAND BT_OP(BT_OGF_LE, 0x0018) /* 0x2018 */
```

相关声明：[BT_HCI_OP_LE_RAND](#ac3af817deaf472dbb2a825fd57b67f42)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_afececfce5819f1b8555ce47fbde2aa0b"></a>

```c
#define BT_HCI_OP_LE_START_ENCRYPTION BT_OP(BT_OGF_LE, 0x0019) /* 0x2019 */
```

相关声明：[BT_HCI_OP_LE_START_ENCRYPTION](#afececfce5819f1b8555ce47fbde2aa0b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a92050425248585bd1c3873e8593db362"></a>

```c
#define BT_HCI_OP_LE_LTK_REQ_REPLY BT_OP(BT_OGF_LE, 0x001a) /* 0x201a */
```

相关声明：[BT_HCI_OP_LE_LTK_REQ_REPLY](#a92050425248585bd1c3873e8593db362)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae04bd3c7ff17142f2b47e24accdf6a20"></a>

```c
#define BT_HCI_OP_LE_LTK_REQ_NEG_REPLY BT_OP(BT_OGF_LE, 0x001b) /* 0x201b */
```

相关声明：[BT_HCI_OP_LE_LTK_REQ_NEG_REPLY](#ae04bd3c7ff17142f2b47e24accdf6a20)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a286869ebde03594d56ecd8bc1aa7c73c"></a>

```c
#define BT_HCI_OP_LE_READ_SUPP_STATES BT_OP(BT_OGF_LE, 0x001c) /* 0x201c */
```

相关声明：[BT_HCI_OP_LE_READ_SUPP_STATES](#a286869ebde03594d56ecd8bc1aa7c73c)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_abd18c6854a0dc97c451b498816f206e4"></a>

```c
#define BT_HCI_OP_LE_RX_TEST BT_OP(BT_OGF_LE, 0x001d) /* 0x201d */
```

相关声明：[BT_HCI_OP_LE_RX_TEST](#abd18c6854a0dc97c451b498816f206e4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa9ce0f2db7b63303a9c61c37d052d7b7"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_PRBS9 0x00
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_PRBS9](#aa9ce0f2db7b63303a9c61c37d052d7b7)。

<a id="r_a51d26730c8f4c3c8491b33483bdb9494"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_11110000 0x01
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_11110000](#a51d26730c8f4c3c8491b33483bdb9494)。

<a id="r_aab044752b89bb4493a509580ae8eaf9b"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_10101010 0x02
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_10101010](#aab044752b89bb4493a509580ae8eaf9b)。

<a id="r_a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_PRBS15 0x03
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_PRBS15](#a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1)。

<a id="r_a5008205909cecc994b74c8a1cb1f92af"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_11111111 0x04
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_11111111](#a5008205909cecc994b74c8a1cb1f92af)。

<a id="r_a1fe8c26f174833a4dccbe192df2c6f7d"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_00000000 0x05
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_00000000](#a1fe8c26f174833a4dccbe192df2c6f7d)。

<a id="r_a13baca9e4517522c763c25882177a2a7"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_00001111 0x06
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_00001111](#a13baca9e4517522c763c25882177a2a7)。

<a id="r_a8f660f979b14d91abd9423e718921ebb"></a>

```c
#define BT_HCI_TEST_PKT_PAYLOAD_01010101 0x07
```

相关声明：[BT_HCI_TEST_PKT_PAYLOAD_01010101](#a8f660f979b14d91abd9423e718921ebb)。

<a id="r_af5fe87cbe280dcf26ddc21952e84e93e"></a>

```c
#define BT_HCI_OP_LE_TX_TEST BT_OP(BT_OGF_LE, 0x001e) /* 0x201e */
```

相关声明：[BT_HCI_OP_LE_TX_TEST](#af5fe87cbe280dcf26ddc21952e84e93e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a7ff8a81ae09ddb0d18f999fe454e41df"></a>

```c
#define BT_HCI_OP_LE_TEST_END BT_OP(BT_OGF_LE, 0x001f) /* 0x201f */
```

相关声明：[BT_HCI_OP_LE_TEST_END](#a7ff8a81ae09ddb0d18f999fe454e41df)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a8b824639d31fa9f579e73cf1f1344c85"></a>

```c
#define BT_HCI_OP_LE_CONN_PARAM_REQ_REPLY BT_OP(BT_OGF_LE, 0x0020) /* 0x2020 */
```

相关声明：[BT_HCI_OP_LE_CONN_PARAM_REQ_REPLY](#a8b824639d31fa9f579e73cf1f1344c85)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1fbca6b816791f1967278224f37782c1"></a>

```c
#define BT_HCI_OP_LE_CONN_PARAM_REQ_NEG_REPLY BT_OP(BT_OGF_LE, 0x0021) /* 0x2021 */
```

相关声明：[BT_HCI_OP_LE_CONN_PARAM_REQ_NEG_REPLY](#a1fbca6b816791f1967278224f37782c1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a5aeb49334449851866537ea8703f5ab0"></a>

```c
#define BT_HCI_OP_LE_SET_DATA_LEN BT_OP(BT_OGF_LE, 0x0022) /* 0x2022 */
```

相关声明：[BT_HCI_OP_LE_SET_DATA_LEN](#a5aeb49334449851866537ea8703f5ab0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa58d9ce08e0f1d4a3e5a2f2b1733a6d2"></a>

```c
#define BT_HCI_OP_LE_READ_DEFAULT_DATA_LEN BT_OP(BT_OGF_LE, 0x0023) /* 0x2023 */
```

相关声明：[BT_HCI_OP_LE_READ_DEFAULT_DATA_LEN](#aa58d9ce08e0f1d4a3e5a2f2b1733a6d2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae344c1ab9af250787b9ed8109ad3cde0"></a>

```c
#define BT_HCI_OP_LE_WRITE_DEFAULT_DATA_LEN BT_OP(BT_OGF_LE, 0x0024) /* 0x2024 */
```

相关声明：[BT_HCI_OP_LE_WRITE_DEFAULT_DATA_LEN](#ae344c1ab9af250787b9ed8109ad3cde0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ab1ff230560c1f7712e23a22eb44f0e69"></a>

```c
#define BT_HCI_OP_LE_P256_PUBLIC_KEY BT_OP(BT_OGF_LE, 0x0025) /* 0x2025 */
```

相关声明：[BT_HCI_OP_LE_P256_PUBLIC_KEY](#ab1ff230560c1f7712e23a22eb44f0e69)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_af2625fcbc0f29199f1a95dc9fe0f929d"></a>

```c
#define BT_HCI_OP_LE_GENERATE_DHKEY BT_OP(BT_OGF_LE, 0x0026) /* 0x2026 */
```

相关声明：[BT_HCI_OP_LE_GENERATE_DHKEY](#af2625fcbc0f29199f1a95dc9fe0f929d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa7bf82632c6df22096210de18902a465"></a>

```c
#define BT_HCI_OP_LE_GENERATE_DHKEY_V2 BT_OP(BT_OGF_LE, 0x005e) /* 0x205e */
```

相关声明：[BT_HCI_OP_LE_GENERATE_DHKEY_V2](#aa7bf82632c6df22096210de18902a465)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac85ab1283cd175fc575ebd98b52b3335"></a>

```c
#define BT_HCI_LE_KEY_TYPE_GENERATED 0x00
```

相关声明：[BT_HCI_LE_KEY_TYPE_GENERATED](#ac85ab1283cd175fc575ebd98b52b3335)。

<a id="r_a71f16c552b14042c00e98ea20c1e03c4"></a>

```c
#define BT_HCI_LE_KEY_TYPE_DEBUG 0x01
```

相关声明：[BT_HCI_LE_KEY_TYPE_DEBUG](#a71f16c552b14042c00e98ea20c1e03c4)。

<a id="r_a735c643e8afa27c4e7f7be9bfb09676a"></a>

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_RL BT_OP(BT_OGF_LE, 0x0027) /* 0x2027 */
```

相关声明：[BT_HCI_OP_LE_ADD_DEV_TO_RL](#a735c643e8afa27c4e7f7be9bfb09676a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac4c11605a4cd244ec3ffa972295396fa"></a>

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_RL BT_OP(BT_OGF_LE, 0x0028) /* 0x2028 */
```

相关声明：[BT_HCI_OP_LE_REM_DEV_FROM_RL](#ac4c11605a4cd244ec3ffa972295396fa)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a5efab85a3beac1fe3fc5a5294a2b1079"></a>

```c
#define BT_HCI_OP_LE_CLEAR_RL BT_OP(BT_OGF_LE, 0x0029) /* 0x2029 */
```

相关声明：[BT_HCI_OP_LE_CLEAR_RL](#a5efab85a3beac1fe3fc5a5294a2b1079)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a45b38708e807c784bd734ba1f69c7f86"></a>

```c
#define BT_HCI_OP_LE_READ_RL_SIZE BT_OP(BT_OGF_LE, 0x002a) /* 0x202a */
```

相关声明：[BT_HCI_OP_LE_READ_RL_SIZE](#a45b38708e807c784bd734ba1f69c7f86)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6c605e63bd1633f3423a915cf4db00e8"></a>

```c
#define BT_HCI_OP_LE_READ_PEER_RPA BT_OP(BT_OGF_LE, 0x002b) /* 0x202b */
```

相关声明：[BT_HCI_OP_LE_READ_PEER_RPA](#a6c605e63bd1633f3423a915cf4db00e8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_af8ec9d3b6889a8530bc5977b8594fea6"></a>

```c
#define BT_HCI_OP_LE_READ_LOCAL_RPA BT_OP(BT_OGF_LE, 0x002c) /* 0x202c */
```

相关声明：[BT_HCI_OP_LE_READ_LOCAL_RPA](#af8ec9d3b6889a8530bc5977b8594fea6)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a017742ee92c9ed7b80b41f339394f1e4"></a>

```c
#define BT_HCI_ADDR_RES_DISABLE 0x00
```

相关声明：[BT_HCI_ADDR_RES_DISABLE](#a017742ee92c9ed7b80b41f339394f1e4)。

<a id="r_a61e677658b5a730b13869ebc0dbbffbe"></a>

```c
#define BT_HCI_ADDR_RES_ENABLE 0x01
```

相关声明：[BT_HCI_ADDR_RES_ENABLE](#a61e677658b5a730b13869ebc0dbbffbe)。

<a id="r_a183431c86b7eb32b7c00e6b3a000f29e"></a>

```c
#define BT_HCI_OP_LE_SET_ADDR_RES_ENABLE BT_OP(BT_OGF_LE, 0x002d) /* 0x202d */
```

相关声明：[BT_HCI_OP_LE_SET_ADDR_RES_ENABLE](#a183431c86b7eb32b7c00e6b3a000f29e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aeabb8438460e694867d855cf7f8e3b31"></a>

```c
#define BT_HCI_OP_LE_SET_RPA_TIMEOUT BT_OP(BT_OGF_LE, 0x002e) /* 0x202e */
```

相关声明：[BT_HCI_OP_LE_SET_RPA_TIMEOUT](#aeabb8438460e694867d855cf7f8e3b31)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6c731f3c0644818489c146eeca9e3ea8"></a>

```c
#define BT_HCI_LE_MAX_TX_OCTETS_MIN 0x001B
```

相关声明：[BT_HCI_LE_MAX_TX_OCTETS_MIN](#a6c731f3c0644818489c146eeca9e3ea8)。

<a id="r_aec6c2a321f9700572fe8cf84d8bed238"></a>

```c
#define BT_HCI_LE_MAX_TX_OCTETS_MAX 0x00FB
```

相关声明：[BT_HCI_LE_MAX_TX_OCTETS_MAX](#aec6c2a321f9700572fe8cf84d8bed238)。

<a id="r_a6c192a213459f5cc7898faa8aa0f5f42"></a>

```c
#define BT_HCI_LE_MAX_RX_OCTETS_MIN 0x001B
```

相关声明：[BT_HCI_LE_MAX_RX_OCTETS_MIN](#a6c192a213459f5cc7898faa8aa0f5f42)。

<a id="r_a72d22456f1eb112a75b91faa40e3b776"></a>

```c
#define BT_HCI_LE_MAX_RX_OCTETS_MAX 0x00FB
```

相关声明：[BT_HCI_LE_MAX_RX_OCTETS_MAX](#a72d22456f1eb112a75b91faa40e3b776)。

<a id="r_ac7c6251a5342a591ff4c413820125f94"></a>

```c
#define BT_HCI_LE_MAX_TX_TIME_MIN 0x0148
```

相关声明：[BT_HCI_LE_MAX_TX_TIME_MIN](#ac7c6251a5342a591ff4c413820125f94)。

<a id="r_aae4ce04bdfd0ad339c87eb18616d8a8a"></a>

```c
#define BT_HCI_LE_MAX_TX_TIME_MAX 0x4290
```

相关声明：[BT_HCI_LE_MAX_TX_TIME_MAX](#aae4ce04bdfd0ad339c87eb18616d8a8a)。

<a id="r_a6666cbeff0cb43fa4c820ba92311fc11"></a>

```c
#define BT_HCI_LE_MAX_RX_TIME_MIN 0x0148
```

相关声明：[BT_HCI_LE_MAX_RX_TIME_MIN](#a6666cbeff0cb43fa4c820ba92311fc11)。

<a id="r_ad4c16d0e80cb6dc2b6fd65e72e331173"></a>

```c
#define BT_HCI_LE_MAX_RX_TIME_MAX 0x4290
```

相关声明：[BT_HCI_LE_MAX_RX_TIME_MAX](#ad4c16d0e80cb6dc2b6fd65e72e331173)。

<a id="r_aafb5872650d77d9f4c6ae43038ef2bf1"></a>

```c
#define BT_HCI_OP_LE_READ_MAX_DATA_LEN BT_OP(BT_OGF_LE, 0x002f) /* 0x202f */
```

相关声明：[BT_HCI_OP_LE_READ_MAX_DATA_LEN](#aafb5872650d77d9f4c6ae43038ef2bf1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a833ae32a3a5ffefbe57c7aa9cdf2e5a9"></a>

```c
#define BT_HCI_LE_PHY_1M 0x01
```

相关声明：[BT_HCI_LE_PHY_1M](#a833ae32a3a5ffefbe57c7aa9cdf2e5a9)。

<a id="r_a727a1780d5f3754a78dea0476c2b97bb"></a>

```c
#define BT_HCI_LE_PHY_2M 0x02
```

相关声明：[BT_HCI_LE_PHY_2M](#a727a1780d5f3754a78dea0476c2b97bb)。

<a id="r_ac5173dfe471fe4d1aad0f7d79904e46a"></a>

```c
#define BT_HCI_LE_PHY_CODED 0x03
```

相关声明：[BT_HCI_LE_PHY_CODED](#ac5173dfe471fe4d1aad0f7d79904e46a)。

<a id="r_ad2e063f4522a64ceeb36c1d95835e74e"></a>

```c
#define BT_HCI_OP_LE_READ_PHY BT_OP(BT_OGF_LE, 0x0030) /* 0x2030 */
```

相关声明：[BT_HCI_OP_LE_READ_PHY](#ad2e063f4522a64ceeb36c1d95835e74e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a7656d3400ccb540e8bd066cf1232c38e"></a>

```c
#define BT_HCI_LE_PHY_TX_ANY BIT(0)
```

相关声明：[BT_HCI_LE_PHY_TX_ANY](#a7656d3400ccb540e8bd066cf1232c38e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0fb6efaf47f2d676eb51b3fb99d0a691"></a>

```c
#define BT_HCI_LE_PHY_RX_ANY BIT(1)
```

相关声明：[BT_HCI_LE_PHY_RX_ANY](#a0fb6efaf47f2d676eb51b3fb99d0a691)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8101f257838639b46dcd0d50a92bba0c"></a>

```c
#define BT_HCI_LE_PHY_PREFER_1M BIT(0)
```

相关声明：[BT_HCI_LE_PHY_PREFER_1M](#a8101f257838639b46dcd0d50a92bba0c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae89ffa7723482ced707f8a57febce629"></a>

```c
#define BT_HCI_LE_PHY_PREFER_2M BIT(1)
```

相关声明：[BT_HCI_LE_PHY_PREFER_2M](#ae89ffa7723482ced707f8a57febce629)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab33fde130c9fdb99559b15455e827a7a"></a>

```c
#define BT_HCI_LE_PHY_PREFER_CODED BIT(2)
```

相关声明：[BT_HCI_LE_PHY_PREFER_CODED](#ab33fde130c9fdb99559b15455e827a7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaa4e3fd27b4157a617a5fb6817bc1881"></a>

```c
#define BT_HCI_OP_LE_SET_DEFAULT_PHY BT_OP(BT_OGF_LE, 0x0031) /* 0x2031 */
```

相关声明：[BT_HCI_OP_LE_SET_DEFAULT_PHY](#aaa4e3fd27b4157a617a5fb6817bc1881)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a61909ce217268c8cc6274f16d3db8484"></a>

```c
#define BT_HCI_LE_PHY_CODED_ANY 0x00
```

相关声明：[BT_HCI_LE_PHY_CODED_ANY](#a61909ce217268c8cc6274f16d3db8484)。

<a id="r_a54bf26868903f0178b0f9f70111ea6b7"></a>

```c
#define BT_HCI_LE_PHY_CODED_S2 0x01
```

相关声明：[BT_HCI_LE_PHY_CODED_S2](#a54bf26868903f0178b0f9f70111ea6b7)。

<a id="r_abe28c39a93e86d9ad5e6f0c08b09ef9c"></a>

```c
#define BT_HCI_LE_PHY_CODED_S8 0x02
```

相关声明：[BT_HCI_LE_PHY_CODED_S8](#abe28c39a93e86d9ad5e6f0c08b09ef9c)。

<a id="r_a1d21c4ffe4db8caafa374a9138e179fa"></a>

```c
#define BT_HCI_OP_LE_SET_PHY BT_OP(BT_OGF_LE, 0x0032) /* 0x2032 */
```

相关声明：[BT_HCI_OP_LE_SET_PHY](#a1d21c4ffe4db8caafa374a9138e179fa)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a631e672ab64e36a983d4d3aae789b237"></a>

```c
#define BT_HCI_LE_MOD_INDEX_STANDARD 0x00
```

相关声明：[BT_HCI_LE_MOD_INDEX_STANDARD](#a631e672ab64e36a983d4d3aae789b237)。

<a id="r_a423acd131760a1ab7b0671c45c9214ca"></a>

```c
#define BT_HCI_LE_MOD_INDEX_STABLE 0x01
```

相关声明：[BT_HCI_LE_MOD_INDEX_STABLE](#a423acd131760a1ab7b0671c45c9214ca)。

<a id="r_a27c179b4c8e85f840b41c4765613c99b"></a>

```c
#define BT_HCI_LE_RX_PHY_1M 0x01
```

相关声明：[BT_HCI_LE_RX_PHY_1M](#a27c179b4c8e85f840b41c4765613c99b)。

<a id="r_ac1db92b615a94b30e587a87d3637ad47"></a>

```c
#define BT_HCI_LE_RX_PHY_2M 0x02
```

相关声明：[BT_HCI_LE_RX_PHY_2M](#ac1db92b615a94b30e587a87d3637ad47)。

<a id="r_a689bc0f95a315c18ee4efbc556d31d60"></a>

```c
#define BT_HCI_LE_RX_PHY_CODED 0x03
```

相关声明：[BT_HCI_LE_RX_PHY_CODED](#a689bc0f95a315c18ee4efbc556d31d60)。

<a id="r_a51c3637712a8701ae7fee16806f677df"></a>

```c
#define BT_HCI_OP_LE_ENH_RX_TEST BT_OP(BT_OGF_LE, 0x0033) /* 0x2033 */
```

相关声明：[BT_HCI_OP_LE_ENH_RX_TEST](#a51c3637712a8701ae7fee16806f677df)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0cb0c8d33e23ff6e59241c88b9e5adee"></a>

```c
#define BT_HCI_LE_TX_PHY_1M 0x01
```

相关声明：[BT_HCI_LE_TX_PHY_1M](#a0cb0c8d33e23ff6e59241c88b9e5adee)。

<a id="r_a7de4598ca06439f89772f0e72306ac3c"></a>

```c
#define BT_HCI_LE_TX_PHY_2M 0x02
```

相关声明：[BT_HCI_LE_TX_PHY_2M](#a7de4598ca06439f89772f0e72306ac3c)。

<a id="r_a01d96d9e7bb61db9b3cd31d161b0abf4"></a>

```c
#define BT_HCI_LE_TX_PHY_CODED_S8 0x03
```

相关声明：[BT_HCI_LE_TX_PHY_CODED_S8](#a01d96d9e7bb61db9b3cd31d161b0abf4)。

<a id="r_a599195b97f069412e112df470bf2b536"></a>

```c
#define BT_HCI_LE_TX_PHY_CODED_S2 0x04
```

相关声明：[BT_HCI_LE_TX_PHY_CODED_S2](#a599195b97f069412e112df470bf2b536)。

<a id="r_a903b1ce0bfe7df7de86bae5fb143e88f"></a>

```c
#define BT_HCI_OP_LE_ENH_TX_TEST BT_OP(BT_OGF_LE, 0x0034) /* 0x2034 */
```

相关声明：[BT_HCI_OP_LE_ENH_TX_TEST](#a903b1ce0bfe7df7de86bae5fb143e88f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac96cefff0857a4d19025a2d9dec8333e"></a>

```c
#define BT_HCI_OP_LE_SET_ADV_SET_RANDOM_ADDR BT_OP(BT_OGF_LE, 0x0035) /* 0x2035 */
```

相关声明：[BT_HCI_OP_LE_SET_ADV_SET_RANDOM_ADDR](#ac96cefff0857a4d19025a2d9dec8333e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac9597c1c284e23578352a23bd66c9fad"></a>

```c
#define BT_HCI_LE_ADV_PROP_CONN BIT(0)
```

相关声明：[BT_HCI_LE_ADV_PROP_CONN](#ac9597c1c284e23578352a23bd66c9fad)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab886c4c7f33adf396ca3e09d0f38995d"></a>

```c
#define BT_HCI_LE_ADV_PROP_SCAN BIT(1)
```

相关声明：[BT_HCI_LE_ADV_PROP_SCAN](#ab886c4c7f33adf396ca3e09d0f38995d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acd154c93af2dc866cfe8bcf8e370dd3d"></a>

```c
#define BT_HCI_LE_ADV_PROP_DIRECT BIT(2)
```

相关声明：[BT_HCI_LE_ADV_PROP_DIRECT](#acd154c93af2dc866cfe8bcf8e370dd3d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0fb43dd85c3671420029027cbfbf8c11"></a>

```c
#define BT_HCI_LE_ADV_PROP_HI_DC_CONN BIT(3)
```

相关声明：[BT_HCI_LE_ADV_PROP_HI_DC_CONN](#a0fb43dd85c3671420029027cbfbf8c11)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a936310de47af573e0d1d5d9401097ba1"></a>

```c
#define BT_HCI_LE_ADV_PROP_LEGACY BIT(4)
```

相关声明：[BT_HCI_LE_ADV_PROP_LEGACY](#a936310de47af573e0d1d5d9401097ba1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a21c60f21a4de9136accc32b0a8a0325c"></a>

```c
#define BT_HCI_LE_ADV_PROP_ANON BIT(5)
```

相关声明：[BT_HCI_LE_ADV_PROP_ANON](#a21c60f21a4de9136accc32b0a8a0325c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abd14685442f2fe315a095516464fc92d"></a>

```c
#define BT_HCI_LE_ADV_PROP_TX_POWER BIT(6)
```

相关声明：[BT_HCI_LE_ADV_PROP_TX_POWER](#abd14685442f2fe315a095516464fc92d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1599475c6673d4fa0e00d16024df9a3b"></a>

```c
#define BT_HCI_LE_PRIM_ADV_INTERVAL_MIN 0x000020
```

相关声明：[BT_HCI_LE_PRIM_ADV_INTERVAL_MIN](#a1599475c6673d4fa0e00d16024df9a3b)。

<a id="r_a5b394658223fd700fa152c4deb2f956e"></a>

```c
#define BT_HCI_LE_PRIM_ADV_INTERVAL_MAX 0xFFFFFF
```

相关声明：[BT_HCI_LE_PRIM_ADV_INTERVAL_MAX](#a5b394658223fd700fa152c4deb2f956e)。

<a id="r_a39fa8033dcf14aa43dfad7cabc1cb429"></a>

```c
#define BT_HCI_LE_ADV_SCAN_REQ_ENABLE 1
```

相关声明：[BT_HCI_LE_ADV_SCAN_REQ_ENABLE](#a39fa8033dcf14aa43dfad7cabc1cb429)。

<a id="r_aa1f4b7ba3b48ea6bd7b8a34a7b831a25"></a>

```c
#define BT_HCI_LE_ADV_SCAN_REQ_DISABLE 0
```

相关声明：[BT_HCI_LE_ADV_SCAN_REQ_DISABLE](#aa1f4b7ba3b48ea6bd7b8a34a7b831a25)。

<a id="r_aa4ce6784e6ee46069fd109dc1869e716"></a>

```c
#define BT_HCI_LE_ADV_TX_POWER_MIN -127
```

相关声明：[BT_HCI_LE_ADV_TX_POWER_MIN](#aa4ce6784e6ee46069fd109dc1869e716)。

最小广播发射功率（Advertising TX Power），单位为 dBm；参见《核心规范》第 4 卷 E 部分 7.8.53。

<a id="r_aa3bfec7459966cf805afcf5186d53103"></a>

```c
#define BT_HCI_LE_ADV_TX_POWER_MAX 20
```

相关声明：[BT_HCI_LE_ADV_TX_POWER_MAX](#aa3bfec7459966cf805afcf5186d53103)。

最大广播发射功率（Advertising TX Power），单位为 dBm；参见《核心规范》第 4 卷 E 部分 7.8.53。

<a id="r_a7f4fcc517033a4743ded39503b35ce29"></a>

```c
#define BT_HCI_LE_ADV_TX_POWER_NO_PREF 0x7F
```

相关声明：[BT_HCI_LE_ADV_TX_POWER_NO_PREF](#a7f4fcc517033a4743ded39503b35ce29)。

广播发射功率（Advertising TX Power）：无偏好，由控制器选择。

<a id="r_a12d97417fa11a07b0af5370b595e9a17"></a>

```c
#define BT_HCI_LE_ADV_HANDLE_MAX 0xEF
```

相关声明：[BT_HCI_LE_ADV_HANDLE_MAX](#a12d97417fa11a07b0af5370b595e9a17)。

<a id="r_a973c2e0fc4cb22d58c47865b9e76b940"></a>

```c
#define BT_HCI_LE_EXT_ADV_SID_INVALID 0xFF
```

相关声明：[BT_HCI_LE_EXT_ADV_SID_INVALID](#a973c2e0fc4cb22d58c47865b9e76b940)。

<a id="r_a098efdd7908adafd26b8e3f63508c476"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM BT_OP(BT_OGF_LE, 0x0036) /* 0x2036 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_ADV_PARAM](#a098efdd7908adafd26b8e3f63508c476)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2ba70856f1e7fe8c6e7990ac9cdf5aaa"></a>

```c
#define BT_HCI_LE_ADV_PHY_OPTION_NO_REQUIRED 0x00
```

相关声明：[BT_HCI_LE_ADV_PHY_OPTION_NO_REQUIRED](#a2ba70856f1e7fe8c6e7990ac9cdf5aaa)。

<a id="r_ac707220fea6b3fc077b8b85267ed0030"></a>

```c
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S2 0x03
```

相关声明：[BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S2](#ac707220fea6b3fc077b8b85267ed0030)。

<a id="r_aab845a49577d93974b468187c948beff"></a>

```c
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S8 0x04
```

相关声明：[BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S8](#aab845a49577d93974b468187c948beff)。

<a id="r_a66ffb876e588d64ce2b2d9091de94806"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM_V2 BT_OP(BT_OGF_LE, 0x007F) /* 0x207F */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_ADV_PARAM_V2](#a66ffb876e588d64ce2b2d9091de94806)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a68c62ac99c4198dbadf6563e40ce33cb"></a>

```c
#define BT_HCI_LE_EXT_ADV_OP_INTERM_FRAG 0x00
```

相关声明：[BT_HCI_LE_EXT_ADV_OP_INTERM_FRAG](#a68c62ac99c4198dbadf6563e40ce33cb)。

<a id="r_a65b3ae46e1164815cda1325e55df4091"></a>

```c
#define BT_HCI_LE_EXT_ADV_OP_FIRST_FRAG 0x01
```

相关声明：[BT_HCI_LE_EXT_ADV_OP_FIRST_FRAG](#a65b3ae46e1164815cda1325e55df4091)。

<a id="r_aade6b8cac66aee356c857fcfae17ce65"></a>

```c
#define BT_HCI_LE_EXT_ADV_OP_LAST_FRAG 0x02
```

相关声明：[BT_HCI_LE_EXT_ADV_OP_LAST_FRAG](#aade6b8cac66aee356c857fcfae17ce65)。

<a id="r_a5394a0dbcd3856ffb8c63440d352120b"></a>

```c
#define BT_HCI_LE_EXT_ADV_OP_COMPLETE_DATA 0x03
```

相关声明：[BT_HCI_LE_EXT_ADV_OP_COMPLETE_DATA](#a5394a0dbcd3856ffb8c63440d352120b)。

<a id="r_a2860ae578d2332a1c76c7bfaa0714e08"></a>

```c
#define BT_HCI_LE_EXT_ADV_OP_UNCHANGED_DATA 0x04
```

相关声明：[BT_HCI_LE_EXT_ADV_OP_UNCHANGED_DATA](#a2860ae578d2332a1c76c7bfaa0714e08)。

<a id="r_aa1dbb6b62c021501320865ac77b5d6da"></a>

```c
#define BT_HCI_LE_EXT_ADV_FRAG_ENABLED 0x00
```

相关声明：[BT_HCI_LE_EXT_ADV_FRAG_ENABLED](#aa1dbb6b62c021501320865ac77b5d6da)。

<a id="r_a4d9626f1b9f0601708b3c38386b5f85c"></a>

```c
#define BT_HCI_LE_EXT_ADV_FRAG_DISABLED 0x01
```

相关声明：[BT_HCI_LE_EXT_ADV_FRAG_DISABLED](#a4d9626f1b9f0601708b3c38386b5f85c)。

<a id="r_a3b3f91c046b0656d489c228d75c8b3ff"></a>

```c
#define BT_HCI_LE_EXT_ADV_FRAG_MAX_LEN 251
```

相关声明：[BT_HCI_LE_EXT_ADV_FRAG_MAX_LEN](#a3b3f91c046b0656d489c228d75c8b3ff)。

<a id="r_a563769ae57bb58be9d7ee8e92019cb99"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_DATA BT_OP(BT_OGF_LE, 0x0037) /* 0x2037 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_ADV_DATA](#a563769ae57bb58be9d7ee8e92019cb99)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a586395798b3d827ab17634287862ef54"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_RSP_DATA BT_OP(BT_OGF_LE, 0x0038) /* 0x2038 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_SCAN_RSP_DATA](#a586395798b3d827ab17634287862ef54)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a99e9573f9bd290fb18f82a327ca55ecd"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_ENABLE BT_OP(BT_OGF_LE, 0x0039) /* 0x2039 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_ADV_ENABLE](#a99e9573f9bd290fb18f82a327ca55ecd)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0246ea11fada7570bf59e73250b49b95"></a>

```c
#define BT_HCI_OP_LE_READ_MAX_ADV_DATA_LEN BT_OP(BT_OGF_LE, 0x003a) /* 0x203a */
```

相关声明：[BT_HCI_OP_LE_READ_MAX_ADV_DATA_LEN](#a0246ea11fada7570bf59e73250b49b95)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a8d2a855322d0aa454ed00e1458cf9a38"></a>

```c
#define BT_HCI_OP_LE_READ_NUM_ADV_SETS BT_OP(BT_OGF_LE, 0x003b) /* 0x203b */
```

相关声明：[BT_HCI_OP_LE_READ_NUM_ADV_SETS](#a8d2a855322d0aa454ed00e1458cf9a38)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ae802afd7081a39f062f65e5c0994a9e4"></a>

```c
#define BT_HCI_OP_LE_REMOVE_ADV_SET BT_OP(BT_OGF_LE, 0x003c) /* 0x203c */
```

相关声明：[BT_HCI_OP_LE_REMOVE_ADV_SET](#ae802afd7081a39f062f65e5c0994a9e4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2f95e881ffcda381d8d8ad7ba8705e7d"></a>

```c
#define BT_HCI_OP_CLEAR_ADV_SETS BT_OP(BT_OGF_LE, 0x003d) /* 0x203d */
```

相关声明：[BT_HCI_OP_CLEAR_ADV_SETS](#a2f95e881ffcda381d8d8ad7ba8705e7d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a04f870ac03c1baca22ab5d984354f3bf"></a>

```c
#define BT_HCI_LE_PER_ADV_INTERVAL_MIN 0x0006
```

相关声明：[BT_HCI_LE_PER_ADV_INTERVAL_MIN](#a04f870ac03c1baca22ab5d984354f3bf)。

<a id="r_a2f2216a88cf77ccac1c9a2f6c5820746"></a>

```c
#define BT_HCI_LE_PER_ADV_INTERVAL_MAX 0xFFFF
```

相关声明：[BT_HCI_LE_PER_ADV_INTERVAL_MAX](#a2f2216a88cf77ccac1c9a2f6c5820746)。

<a id="r_a3a111d29fd682fa825f4f9c8c358243f"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_PARAM BT_OP(BT_OGF_LE, 0x003e) /* 0x203e */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_PARAM](#a3a111d29fd682fa825f4f9c8c358243f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa18edf54edfb8d0fcaca5941e8e5e493"></a>

```c
#define BT_HCI_LE_PER_ADV_OP_INTERM_FRAG 0x00
```

相关声明：[BT_HCI_LE_PER_ADV_OP_INTERM_FRAG](#aa18edf54edfb8d0fcaca5941e8e5e493)。

<a id="r_a8aeb4c76ec769879fc4796fc2919c459"></a>

```c
#define BT_HCI_LE_PER_ADV_OP_FIRST_FRAG 0x01
```

相关声明：[BT_HCI_LE_PER_ADV_OP_FIRST_FRAG](#a8aeb4c76ec769879fc4796fc2919c459)。

<a id="r_a7f2314472ccb051e87d1bb2f9b3fded8"></a>

```c
#define BT_HCI_LE_PER_ADV_OP_LAST_FRAG 0x02
```

相关声明：[BT_HCI_LE_PER_ADV_OP_LAST_FRAG](#a7f2314472ccb051e87d1bb2f9b3fded8)。

<a id="r_ada39c45c3c1c7576d4d9794dad115e61"></a>

```c
#define BT_HCI_LE_PER_ADV_OP_COMPLETE_DATA 0x03
```

相关声明：[BT_HCI_LE_PER_ADV_OP_COMPLETE_DATA](#ada39c45c3c1c7576d4d9794dad115e61)。

<a id="r_a7b3cd7870ba4af2ff483a831d2700466"></a>

```c
#define BT_HCI_LE_PER_ADV_FRAG_MAX_LEN 252
```

相关声明：[BT_HCI_LE_PER_ADV_FRAG_MAX_LEN](#a7b3cd7870ba4af2ff483a831d2700466)。

<a id="r_ae6611e7b72b057ac9d4004a1772fe435"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_DATA BT_OP(BT_OGF_LE, 0x003f) /* 0x203f */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_DATA](#ae6611e7b72b057ac9d4004a1772fe435)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1c03932d8c1e2c5436eaf45be093b4d4"></a>

```c
#define BT_HCI_LE_SET_PER_ADV_ENABLE_ENABLE BIT(0)
```

相关声明：[BT_HCI_LE_SET_PER_ADV_ENABLE_ENABLE](#a1c03932d8c1e2c5436eaf45be093b4d4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaf9b76b276b5cf7e02bb5e3b0a12ecf6"></a>

```c
#define BT_HCI_LE_SET_PER_ADV_ENABLE_ADI BIT(1)
```

相关声明：[BT_HCI_LE_SET_PER_ADV_ENABLE_ADI](#aaf9b76b276b5cf7e02bb5e3b0a12ecf6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3ae23554c13b099b50b129462e08afe4"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_ENABLE BT_OP(BT_OGF_LE, 0x0040) /* 0x2040 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_ENABLE](#a3ae23554c13b099b50b129462e08afe4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a7b0687c9e1faae997b76ece821338fd7"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_PARAM BT_OP(BT_OGF_LE, 0x0041) /* 0x2041 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_SCAN_PARAM](#a7b0687c9e1faae997b76ece821338fd7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0ef6a16a2b042b3e7623210fc5fcd1a0"></a>

```c
#define BT_HCI_LE_EXT_SCAN_PHY_1M BIT(0)
```

相关声明：[BT_HCI_LE_EXT_SCAN_PHY_1M](#a0ef6a16a2b042b3e7623210fc5fcd1a0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad0f0fe21e4e9136e09e0a443a7253759"></a>

```c
#define BT_HCI_LE_EXT_SCAN_PHY_2M BIT(1)
```

相关声明：[BT_HCI_LE_EXT_SCAN_PHY_2M](#ad0f0fe21e4e9136e09e0a443a7253759)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae15b1ae9e35d060b3a9619d293a7d9ac"></a>

```c
#define BT_HCI_LE_EXT_SCAN_PHY_CODED BIT(2)
```

相关声明：[BT_HCI_LE_EXT_SCAN_PHY_CODED](#ae15b1ae9e35d060b3a9619d293a7d9ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae9ba6da1a01dacc52c6a1a2c84d16948"></a>

```c
#define BT_HCI_LE_EXT_SCAN_FILTER_DUP_ENABLE_RESET 0x02
```

相关声明：[BT_HCI_LE_EXT_SCAN_FILTER_DUP_ENABLE_RESET](#ae9ba6da1a01dacc52c6a1a2c84d16948)。

<a id="r_af7a8256887657e482084d4ed3810195b"></a>

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_ENABLE BT_OP(BT_OGF_LE, 0x0042) /* 0x2042 */
```

相关声明：[BT_HCI_OP_LE_SET_EXT_SCAN_ENABLE](#af7a8256887657e482084d4ed3810195b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac498c9cd93b664b5bd2e58982d36d7ad"></a>

```c
#define BT_HCI_OP_LE_EXT_CREATE_CONN BT_OP(BT_OGF_LE, 0x0043) /* 0x2043 */
```

相关声明：[BT_HCI_OP_LE_EXT_CREATE_CONN](#ac498c9cd93b664b5bd2e58982d36d7ad)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1b6bc4da843ed8d04e0b9571465ffd12"></a>

```c
#define BT_HCI_OP_LE_EXT_CREATE_CONN_V2 BT_OP(BT_OGF_LE, 0x0085) /* 0x2085 */
```

相关声明：[BT_HCI_OP_LE_EXT_CREATE_CONN_V2](#a1b6bc4da843ed8d04e0b9571465ffd12)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a44e729aebc339ada5deb86ad9d350404"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_SUBEVENT_DATA BT_OP(BT_OGF_LE, 0x0082) /* 0x2082 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_SUBEVENT_DATA](#a44e729aebc339ada5deb86ad9d350404)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2be1e66c896dca2022c04164fd94da49"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_RESPONSE_DATA BT_OP(BT_OGF_LE, 0x0083) /* 0x2083 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_RESPONSE_DATA](#a2be1e66c896dca2022c04164fd94da49)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aea7f44f563c109be1676454412757fab"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_SYNC_SUBEVENT BT_OP(BT_OGF_LE, 0x0084) /* 0x2084 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_SYNC_SUBEVENT](#aea7f44f563c109be1676454412757fab)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1125bfc15404124bf4bd533520be0f77"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_PARAM_V2 BT_OP(BT_OGF_LE, 0x0086) /* 0x2086 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_PARAM_V2](#a1125bfc15404124bf4bd533520be0f77)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a490bb7d8cf236e49c60771a95d258247"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_USE_LIST BIT(0)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_USE_LIST](#a490bb7d8cf236e49c60771a95d258247)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a44f11af392e3188e699d8f987cb2f6d6"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_REPORTS_DISABLED BIT(1)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_REPORTS_DISABLED](#a44f11af392e3188e699d8f987cb2f6d6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a29c5cf397f94af42bdea484fa95a2a78"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_FILTER_DUPLICATE BIT(2)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_FILTER_DUPLICATE](#a29c5cf397f94af42bdea484fa95a2a78)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abb3c8fcfc0b48cf6dbebff206a2a9a48"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_FILTERING 0
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_FILTERING](#abb3c8fcfc0b48cf6dbebff206a2a9a48)。

<a id="r_a64c7e74877c8ca638217a09d503e742b"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOA BIT(0)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOA](#a64c7e74877c8ca638217a09d503e742b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad349244f13388a7437651e5c3909bcb9"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_1US BIT(1)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_1US](#ad349244f13388a7437651e5c3909bcb9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aae32740df5a3096a9b17b9c06e6cc3e9"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_2US BIT(2)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_2US](#aae32740df5a3096a9b17b9c06e6cc3e9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5532c8ee93198eb831c12b182e13a534"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_CTE BIT(3)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_CTE](#a5532c8ee93198eb831c12b182e13a534)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa3b526ab2ed1aeaab0e26a5390b3dcea"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ONLY_CTE BIT(4)
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ONLY_CTE](#aa3b526ab2ed1aeaab0e26a5390b3dcea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4c884821e7136f6f68bc4d92b394381a"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS 5
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS](#a4c884821e7136f6f68bc4d92b394381a)。

<a id="r_a6ad9e08bcef788c32481756f76df6a43"></a>

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_INVALID_VALUE (~BIT_MASK(BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS))
```

相关声明：[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_INVALID_VALUE](#a6ad9e08bcef788c32481756f76df6a43)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)、[BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS](#a4c884821e7136f6f68bc4d92b394381a)。

<a id="r_a589c2da26ce325d5cb45726c772cf7ab"></a>

```c
#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC BT_OP(BT_OGF_LE, 0x0044) /* 0x2044 */
```

相关声明：[BT_HCI_OP_LE_PER_ADV_CREATE_SYNC](#a589c2da26ce325d5cb45726c772cf7ab)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a3803042099104029f5b49536cb769e6c"></a>

```c
#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC_CANCEL BT_OP(BT_OGF_LE, 0x0045) /* 0x2045 */
```

相关声明：[BT_HCI_OP_LE_PER_ADV_CREATE_SYNC_CANCEL](#a3803042099104029f5b49536cb769e6c)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a57b7b3cab371b4dd230343dfbc5a5e98"></a>

```c
#define BT_HCI_OP_LE_PER_ADV_TERMINATE_SYNC BT_OP(BT_OGF_LE, 0x0046) /* 0x2046 */
```

相关声明：[BT_HCI_OP_LE_PER_ADV_TERMINATE_SYNC](#a57b7b3cab371b4dd230343dfbc5a5e98)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a393378ba85552bb5f41475a863ca649f"></a>

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0047) /* 0x2047 */
```

相关声明：[BT_HCI_OP_LE_ADD_DEV_TO_PER_ADV_LIST](#a393378ba85552bb5f41475a863ca649f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a8545e1ede192257a4383eea6b2e932b7"></a>

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0048) /* 0x2048 */
```

相关声明：[BT_HCI_OP_LE_REM_DEV_FROM_PER_ADV_LIST](#a8545e1ede192257a4383eea6b2e932b7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_affcd4a54d0b26d7b07e39157f17167b4"></a>

```c
#define BT_HCI_OP_LE_CLEAR_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0049) /* 0x2049 */
```

相关声明：[BT_HCI_OP_LE_CLEAR_PER_ADV_LIST](#affcd4a54d0b26d7b07e39157f17167b4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a3e2fd45c015809e131ac6b3f6a9c72fc"></a>

```c
#define BT_HCI_OP_LE_READ_PER_ADV_LIST_SIZE BT_OP(BT_OGF_LE, 0x004a) /* 0x204a */
```

相关声明：[BT_HCI_OP_LE_READ_PER_ADV_LIST_SIZE](#a3e2fd45c015809e131ac6b3f6a9c72fc)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a77d132306109474465575369db342dbd"></a>

```c
#define BT_HCI_OP_LE_READ_TX_POWER BT_OP(BT_OGF_LE, 0x004b) /* 0x204b */
```

相关声明：[BT_HCI_OP_LE_READ_TX_POWER](#a77d132306109474465575369db342dbd)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6c454d3276f7eaae542b13becad6482c"></a>

```c
#define BT_HCI_OP_LE_READ_RF_PATH_COMP BT_OP(BT_OGF_LE, 0x004c) /* 0x204c */
```

相关声明：[BT_HCI_OP_LE_READ_RF_PATH_COMP](#a6c454d3276f7eaae542b13becad6482c)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a766b66d1fc7df1d8924d060217de9b9b"></a>

```c
#define BT_HCI_OP_LE_WRITE_RF_PATH_COMP BT_OP(BT_OGF_LE, 0x004d) /* 0x204d */
```

相关声明：[BT_HCI_OP_LE_WRITE_RF_PATH_COMP](#a766b66d1fc7df1d8924d060217de9b9b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a423b143e474548458b8bcce59029f722"></a>

```c
#define BT_HCI_LE_PRIVACY_MODE_NETWORK 0x00
```

相关声明：[BT_HCI_LE_PRIVACY_MODE_NETWORK](#a423b143e474548458b8bcce59029f722)。

<a id="r_ae61d38e84e0d58be45ffaf521abad2f6"></a>

```c
#define BT_HCI_LE_PRIVACY_MODE_DEVICE 0x01
```

相关声明：[BT_HCI_LE_PRIVACY_MODE_DEVICE](#ae61d38e84e0d58be45ffaf521abad2f6)。

<a id="r_a7e1fad2d353904bb345f3a1579c98576"></a>

```c
#define BT_HCI_OP_LE_SET_PRIVACY_MODE BT_OP(BT_OGF_LE, 0x004e) /* 0x204e */
```

相关声明：[BT_HCI_OP_LE_SET_PRIVACY_MODE](#a7e1fad2d353904bb345f3a1579c98576)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6764be57300c8dac30a058ebf8387159"></a>

```c
#define BT_HCI_LE_TEST_CTE_DISABLED 0x00
```

相关声明：[BT_HCI_LE_TEST_CTE_DISABLED](#a6764be57300c8dac30a058ebf8387159)。

<a id="r_a1f45696f06d7bc3f4cc8393bd6967286"></a>

```c
#define BT_HCI_LE_TEST_CTE_TYPE_ANY 0x00
```

相关声明：[BT_HCI_LE_TEST_CTE_TYPE_ANY](#a1f45696f06d7bc3f4cc8393bd6967286)。

<a id="r_ac4ac180578ed3f662d91c43b5c6b6b53"></a>

```c
#define BT_HCI_LE_TEST_SLOT_DURATION_ANY 0x00
```

相关声明：[BT_HCI_LE_TEST_SLOT_DURATION_ANY](#ac4ac180578ed3f662d91c43b5c6b6b53)。

<a id="r_aef669f8887a165b4948eb651c91968c1"></a>

```c
#define BT_HCI_LE_TEST_SWITCH_PATTERN_LEN_ANY 0x00
```

相关声明：[BT_HCI_LE_TEST_SWITCH_PATTERN_LEN_ANY](#aef669f8887a165b4948eb651c91968c1)。

<a id="r_abe1567f7cf83148b3f2214b6e0787da0"></a>

```c
#define BT_HCI_OP_LE_RX_TEST_V3 BT_OP(BT_OGF_LE, 0x004f) /* 0x204f */
```

相关声明：[BT_HCI_OP_LE_RX_TEST_V3](#abe1567f7cf83148b3f2214b6e0787da0)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ad570a3edcefcf927e5253805e1d3d4e4"></a>

```c
#define BT_HCI_OP_LE_TX_TEST_V3 BT_OP(BT_OGF_LE, 0x0050) /* 0x2050 */
```

相关声明：[BT_HCI_OP_LE_TX_TEST_V3](#ad570a3edcefcf927e5253805e1d3d4e4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a80376d34b4d701d5f6092aa101ce0e6c"></a>

```c
#define BT_HCI_LE_CTE_LEN_MIN 0x2
```

相关声明：[BT_HCI_LE_CTE_LEN_MIN](#a80376d34b4d701d5f6092aa101ce0e6c)。

<a id="r_acdfe03ade99fa88779b68e435aea23e3"></a>

```c
#define BT_HCI_LE_CTE_LEN_MAX 0x14
```

相关声明：[BT_HCI_LE_CTE_LEN_MAX](#acdfe03ade99fa88779b68e435aea23e3)。

<a id="r_a9b3306f29525c50cd8bd501f7391e518"></a>

```c
#define BT_HCI_LE_AOA_CTE 0x0
```

相关声明：[BT_HCI_LE_AOA_CTE](#a9b3306f29525c50cd8bd501f7391e518)。

<a id="r_a8569e960c44660eb41cdccbe5aeb6ead"></a>

```c
#define BT_HCI_LE_AOD_CTE_1US 0x1
```

相关声明：[BT_HCI_LE_AOD_CTE_1US](#a8569e960c44660eb41cdccbe5aeb6ead)。

<a id="r_a970732caa95f5742fc18c91efbc7095b"></a>

```c
#define BT_HCI_LE_AOD_CTE_2US 0x2
```

相关声明：[BT_HCI_LE_AOD_CTE_2US](#a970732caa95f5742fc18c91efbc7095b)。

<a id="r_aeee9fd73771de54542f7ff24f95eceba"></a>

```c
#define BT_HCI_LE_NO_CTE 0xFF
```

相关声明：[BT_HCI_LE_NO_CTE](#aeee9fd73771de54542f7ff24f95eceba)。

<a id="r_aec2a77fadbb6bf24267d659a84b7c9a9"></a>

```c
#define BT_HCI_LE_CTE_COUNT_MIN 0x1
```

相关声明：[BT_HCI_LE_CTE_COUNT_MIN](#aec2a77fadbb6bf24267d659a84b7c9a9)。

<a id="r_a442df4f693ae5bb75d1d8f54fe204bda"></a>

```c
#define BT_HCI_LE_CTE_COUNT_MAX 0x10
```

相关声明：[BT_HCI_LE_CTE_COUNT_MAX](#a442df4f693ae5bb75d1d8f54fe204bda)。

<a id="r_a900509c6e7485b44de09a43555225ce8"></a>

```c
#define BT_HCI_OP_LE_SET_CL_CTE_TX_PARAMS BT_OP(BT_OGF_LE, 0x0051) /* 0x2051 */
```

相关声明：[BT_HCI_OP_LE_SET_CL_CTE_TX_PARAMS](#a900509c6e7485b44de09a43555225ce8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a5527fd8badb977f2ef061ba76468ccf3"></a>

```c
#define BT_HCI_OP_LE_SET_CL_CTE_TX_ENABLE BT_OP(BT_OGF_LE, 0x0052) /* 0x2052 */
```

相关声明：[BT_HCI_OP_LE_SET_CL_CTE_TX_ENABLE](#a5527fd8badb977f2ef061ba76468ccf3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1410330e31701a140eb8c0c73c943972"></a>

```c
#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_1US 0x1
```

相关声明：[BT_HCI_LE_ANTENNA_SWITCHING_SLOT_1US](#a1410330e31701a140eb8c0c73c943972)。

<a id="r_afa70fe0b1b9e277bfcb6bf7d6fc03564"></a>

```c
#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_2US 0x2
```

相关声明：[BT_HCI_LE_ANTENNA_SWITCHING_SLOT_2US](#afa70fe0b1b9e277bfcb6bf7d6fc03564)。

<a id="r_a85450acad700f8cef375d34235752650"></a>

```c
#define BT_HCI_LE_SAMPLE_CTE_ALL 0x0
```

相关声明：[BT_HCI_LE_SAMPLE_CTE_ALL](#a85450acad700f8cef375d34235752650)。

<a id="r_afd22fac7ff6d5006015159ffc978798a"></a>

```c
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MIN 0x1
```

相关声明：[BT_HCI_LE_SAMPLE_CTE_COUNT_MIN](#afd22fac7ff6d5006015159ffc978798a)。

<a id="r_a0c8888c4dfed6ab4c0f07a37ca3b2278"></a>

```c
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MAX 0x10
```

相关声明：[BT_HCI_LE_SAMPLE_CTE_COUNT_MAX](#a0c8888c4dfed6ab4c0f07a37ca3b2278)。

<a id="r_a728b9a505c9a2f719424bd277f7e8765"></a>

```c
#define BT_HCI_OP_LE_SET_CL_CTE_SAMPLING_ENABLE BT_OP(BT_OGF_LE, 0x0053) /* 0x2053 */
```

相关声明：[BT_HCI_OP_LE_SET_CL_CTE_SAMPLING_ENABLE](#a728b9a505c9a2f719424bd277f7e8765)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a8a079c51fc7c37f29afeda663206c59e"></a>

```c
#define BT_HCI_OP_LE_SET_CONN_CTE_RX_PARAMS BT_OP(BT_OGF_LE, 0x0054) /* 0x2054 */
```

相关声明：[BT_HCI_OP_LE_SET_CONN_CTE_RX_PARAMS](#a8a079c51fc7c37f29afeda663206c59e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ac80b68b1ca4f55a8a44b6bf0dfa7bfb3"></a>

```c
#define BT_HCI_LE_AOA_CTE_RSP BIT(0)
```

相关声明：[BT_HCI_LE_AOA_CTE_RSP](#ac80b68b1ca4f55a8a44b6bf0dfa7bfb3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a124137512b0f87a67fff694359d629d0"></a>

```c
#define BT_HCI_LE_AOD_CTE_RSP_1US BIT(1)
```

相关声明：[BT_HCI_LE_AOD_CTE_RSP_1US](#a124137512b0f87a67fff694359d629d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5c1dd462d05e4a5615f80402f892ecbc"></a>

```c
#define BT_HCI_LE_AOD_CTE_RSP_2US BIT(2)
```

相关声明：[BT_HCI_LE_AOD_CTE_RSP_2US](#a5c1dd462d05e4a5615f80402f892ecbc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad74e54836996fc3d02fbb245f9c72b5a"></a>

```c
#define BT_HCI_LE_SWITCH_PATTERN_LEN_MIN 0x2
```

相关声明：[BT_HCI_LE_SWITCH_PATTERN_LEN_MIN](#ad74e54836996fc3d02fbb245f9c72b5a)。

<a id="r_ad6bdc84c282a4e35ded32687cba94e9f"></a>

```c
#define BT_HCI_LE_SWITCH_PATTERN_LEN_MAX 0x4B
```

相关声明：[BT_HCI_LE_SWITCH_PATTERN_LEN_MAX](#ad6bdc84c282a4e35ded32687cba94e9f)。

<a id="r_af4110be6e09c80cd7362d9b2580243e7"></a>

```c
#define BT_HCI_OP_LE_SET_CONN_CTE_TX_PARAMS BT_OP(BT_OGF_LE, 0x0055) /* 0x2055 */
```

相关声明：[BT_HCI_OP_LE_SET_CONN_CTE_TX_PARAMS](#af4110be6e09c80cd7362d9b2580243e7)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ad9e1fa26a799b8730c17772482da7982"></a>

```c
#define BT_HCI_REQUEST_CTE_ONCE 0x0
```

相关声明：[BT_HCI_REQUEST_CTE_ONCE](#ad9e1fa26a799b8730c17772482da7982)。

<a id="r_a13875ad8ac3a77759afdb4b6a76ad3e8"></a>

```c
#define BT_HCI_REQUEST_CTE_INTERVAL_MIN 0x1
```

相关声明：[BT_HCI_REQUEST_CTE_INTERVAL_MIN](#a13875ad8ac3a77759afdb4b6a76ad3e8)。

<a id="r_a0a41f911f5f4b50b571c7f091393c7d8"></a>

```c
#define BT_HCI_REQUEST_CTE_INTERVAL_MAX 0xFFFF
```

相关声明：[BT_HCI_REQUEST_CTE_INTERVAL_MAX](#a0a41f911f5f4b50b571c7f091393c7d8)。

<a id="r_ae488ce598705cf60b78da985015bb42b"></a>

```c
#define BT_HCI_OP_LE_CONN_CTE_REQ_ENABLE BT_OP(BT_OGF_LE, 0x0056) /* 0x2056 */
```

相关声明：[BT_HCI_OP_LE_CONN_CTE_REQ_ENABLE](#ae488ce598705cf60b78da985015bb42b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a150b54d69fb6fe9175336fadb7d81bb8"></a>

```c
#define BT_HCI_OP_LE_CONN_CTE_RSP_ENABLE BT_OP(BT_OGF_LE, 0x0057) /* 0x2057 */
```

相关声明：[BT_HCI_OP_LE_CONN_CTE_RSP_ENABLE](#a150b54d69fb6fe9175336fadb7d81bb8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a41aac54cd90cfc58990ce93124ce7077"></a>

```c
#define BT_HCI_LE_1US_AOD_TX BIT(0)
```

相关声明：[BT_HCI_LE_1US_AOD_TX](#a41aac54cd90cfc58990ce93124ce7077)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a70edcf0bd7e63454996ef5d925e91bbf"></a>

```c
#define BT_HCI_LE_1US_AOD_RX BIT(1)
```

相关声明：[BT_HCI_LE_1US_AOD_RX](#a70edcf0bd7e63454996ef5d925e91bbf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a04a69a823bac190d0ac16f3c21481bde"></a>

```c
#define BT_HCI_LE_1US_AOA_RX BIT(2)
```

相关声明：[BT_HCI_LE_1US_AOA_RX](#a04a69a823bac190d0ac16f3c21481bde)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a112d3fb3d3ec663278aa4463fedbd89b"></a>

```c
#define BT_HCI_LE_NUM_ANT_MIN 0x1
```

相关声明：[BT_HCI_LE_NUM_ANT_MIN](#a112d3fb3d3ec663278aa4463fedbd89b)。

<a id="r_ad9ff685b2854b877e0cdd1ae93272ddf"></a>

```c
#define BT_HCI_LE_NUM_ANT_MAX 0x4B
```

相关声明：[BT_HCI_LE_NUM_ANT_MAX](#ad9ff685b2854b877e0cdd1ae93272ddf)。

<a id="r_a327330c5b69e8ec56dd18fcc3fdf0622"></a>

```c
#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MIN 0x2
```

相关声明：[BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MIN](#a327330c5b69e8ec56dd18fcc3fdf0622)。

<a id="r_a647de996dd2e75a8242e6459abd565f6"></a>

```c
#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MAX 0x4B
```

相关声明：[BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MAX](#a647de996dd2e75a8242e6459abd565f6)。

<a id="r_adee7271e25e6d66ba434502ab56674c3"></a>

```c
#define BT_HCI_LE_MAX_CTE_LEN_MIN 0x2
```

相关声明：[BT_HCI_LE_MAX_CTE_LEN_MIN](#adee7271e25e6d66ba434502ab56674c3)。

<a id="r_af54ba281111d90f3edb77c0abf9c57b1"></a>

```c
#define BT_HCI_LE_MAX_CTE_LEN_MAX 0x14
```

相关声明：[BT_HCI_LE_MAX_CTE_LEN_MAX](#af54ba281111d90f3edb77c0abf9c57b1)。

<a id="r_aff3ea5f19135609d5553cacec0d700a6"></a>

```c
#define BT_HCI_OP_LE_READ_ANT_INFO BT_OP(BT_OGF_LE, 0x0058) /* 0x2058 */
```

相关声明：[BT_HCI_OP_LE_READ_ANT_INFO](#aff3ea5f19135609d5553cacec0d700a6)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a1aaaffb3044bfd824aa6744867da0a97"></a>

```c
#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_ENABLE BIT(0)
```

相关声明：[BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_ENABLE](#a1aaaffb3044bfd824aa6744867da0a97)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a08fe0a16e8c1b3eb6b23869b37739f2d"></a>

```c
#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_FILTER_DUPLICATE BIT(1)
```

相关声明：[BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_FILTER_DUPLICATE](#a08fe0a16e8c1b3eb6b23869b37739f2d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a047efb565b182e90178513dc3db6390f"></a>

```c
#define BT_HCI_OP_LE_SET_PER_ADV_RECV_ENABLE BT_OP(BT_OGF_LE, 0x0059) /* 0x2059 */
```

相关声明：[BT_HCI_OP_LE_SET_PER_ADV_RECV_ENABLE](#a047efb565b182e90178513dc3db6390f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa1d0bc8ccc0e1e8835938f8e8d87b7f1"></a>

```c
#define BT_HCI_OP_LE_PER_ADV_SYNC_TRANSFER BT_OP(BT_OGF_LE, 0x005a) /* 0x205a */
```

相关声明：[BT_HCI_OP_LE_PER_ADV_SYNC_TRANSFER](#aa1d0bc8ccc0e1e8835938f8e8d87b7f1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ab7d661097af4cc612ac6631b18bbc7e3"></a>

```c
#define BT_HCI_OP_LE_PER_ADV_SET_INFO_TRANSFER BT_OP(BT_OGF_LE, 0x005b) /* 0x205b */
```

相关声明：[BT_HCI_OP_LE_PER_ADV_SET_INFO_TRANSFER](#ab7d661097af4cc612ac6631b18bbc7e3)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a65ff1c4a937422000f6f1eadea28ccba"></a>

```c
#define BT_HCI_LE_PAST_MODE_NO_SYNC 0x00
```

相关声明：[BT_HCI_LE_PAST_MODE_NO_SYNC](#a65ff1c4a937422000f6f1eadea28ccba)。

<a id="r_ac7233f9c34f5e33d765b68b55ebc9b9e"></a>

```c
#define BT_HCI_LE_PAST_MODE_NO_REPORTS 0x01
```

相关声明：[BT_HCI_LE_PAST_MODE_NO_REPORTS](#ac7233f9c34f5e33d765b68b55ebc9b9e)。

<a id="r_aaeac19606d3d5e7d0906b38e2c4b4c69"></a>

```c
#define BT_HCI_LE_PAST_MODE_SYNC 0x02
```

相关声明：[BT_HCI_LE_PAST_MODE_SYNC](#aaeac19606d3d5e7d0906b38e2c4b4c69)。

<a id="r_ab0232a2abc2b7c86b19ae89298ef8c4b"></a>

```c
#define BT_HCI_LE_PAST_MODE_SYNC_FILTER_DUPLICATES 0x03
```

相关声明：[BT_HCI_LE_PAST_MODE_SYNC_FILTER_DUPLICATES](#ab0232a2abc2b7c86b19ae89298ef8c4b)。

<a id="r_a3a3937965aeb187b6fb18da3b7731ed7"></a>

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOA BIT(0)
```

相关声明：[BT_HCI_LE_PAST_CTE_TYPE_NO_AOA](#a3a3937965aeb187b6fb18da3b7731ed7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a440aca4bf97bc6b583284ae6c8037a53"></a>

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_1US BIT(1)
```

相关声明：[BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_1US](#a440aca4bf97bc6b583284ae6c8037a53)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae2d9be5e54595cb5a426ae8909cdee1c"></a>

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_2US BIT(2)
```

相关声明：[BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_2US](#ae2d9be5e54595cb5a426ae8909cdee1c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af3d8cf0fb8af60c057ba8c24abaf3897"></a>

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_CTE BIT(3)
```

相关声明：[BT_HCI_LE_PAST_CTE_TYPE_NO_CTE](#af3d8cf0fb8af60c057ba8c24abaf3897)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6fca2634e0e5b0dd5d86b18666ed38e4"></a>

```c
#define BT_HCI_LE_PAST_CTE_TYPE_ONLY_CTE BIT(4)
```

相关声明：[BT_HCI_LE_PAST_CTE_TYPE_ONLY_CTE](#a6fca2634e0e5b0dd5d86b18666ed38e4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a177ec628eac4a7d535cfe6c07123cb34"></a>

```c
#define BT_HCI_OP_LE_PAST_PARAM BT_OP(BT_OGF_LE, 0x005c) /* 0x205c */
```

相关声明：[BT_HCI_OP_LE_PAST_PARAM](#a177ec628eac4a7d535cfe6c07123cb34)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a650fe2941ffe238b16fd99ed5e78b25a"></a>

```c
#define BT_HCI_OP_LE_DEFAULT_PAST_PARAM BT_OP(BT_OGF_LE, 0x005d) /* 0x205d */
```

相关声明：[BT_HCI_OP_LE_DEFAULT_PAST_PARAM](#a650fe2941ffe238b16fd99ed5e78b25a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa7e78541d152c21e101fab5a094c972f"></a>

```c
#define BT_HCI_OP_LE_READ_BUFFER_SIZE_V2 BT_OP(BT_OGF_LE, 0x0060) /* 0x2060 */
```

相关声明：[BT_HCI_OP_LE_READ_BUFFER_SIZE_V2](#aa7e78541d152c21e101fab5a094c972f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_acb7f49f17a60a4e29270c8719b7aeeed"></a>

```c
#define BT_HCI_OP_LE_READ_ISO_TX_SYNC BT_OP(BT_OGF_LE, 0x0061) /* 0x2061 */
```

相关声明：[BT_HCI_OP_LE_READ_ISO_TX_SYNC](#acb7f49f17a60a4e29270c8719b7aeeed)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a18b5fef3eb5b947ce328e17c1e7db02d"></a>

```c
#define BT_HCI_ISO_CIG_ID_MAX 0xFE
```

相关声明：[BT_HCI_ISO_CIG_ID_MAX](#a18b5fef3eb5b947ce328e17c1e7db02d)。

<a id="r_a26c78a4b760b97682269e66dfe6f99df"></a>

```c
#define BT_HCI_ISO_CIS_COUNT_MAX 0x1F
```

相关声明：[BT_HCI_ISO_CIS_COUNT_MAX](#a26c78a4b760b97682269e66dfe6f99df)。

<a id="r_a12e9af0e72013649da8afc7aa70a4e9c"></a>

```c
#define BT_HCI_ISO_SDU_INTERVAL_MIN 0x0000FF
```

相关声明：[BT_HCI_ISO_SDU_INTERVAL_MIN](#a12e9af0e72013649da8afc7aa70a4e9c)。

<a id="r_aa75800427e808756fc7c6d30da57de37"></a>

```c
#define BT_HCI_ISO_SDU_INTERVAL_MAX 0x0FFFFF
```

相关声明：[BT_HCI_ISO_SDU_INTERVAL_MAX](#aa75800427e808756fc7c6d30da57de37)。

<a id="r_a49f62e83dd51d17efd77c89337fdd537"></a>

```c
#define BT_HCI_ISO_WORST_CASE_SCA_VALID_MASK 0x07
```

相关声明：[BT_HCI_ISO_WORST_CASE_SCA_VALID_MASK](#a49f62e83dd51d17efd77c89337fdd537)。

<a id="r_aecaa88e04025e575c9bcda093f027400"></a>

```c
#define BT_HCI_ISO_PACKING_VALID_MASK 0x01
```

相关声明：[BT_HCI_ISO_PACKING_VALID_MASK](#aecaa88e04025e575c9bcda093f027400)。

<a id="r_aaf4b4fc224c8b5cfdca663250eb29350"></a>

```c
#define BT_HCI_ISO_FRAMING_VALID_MASK 0x01
```

相关声明：[BT_HCI_ISO_FRAMING_VALID_MASK](#aaf4b4fc224c8b5cfdca663250eb29350)。

<a id="r_a8d044df1bfab8381b7e334597b303588"></a>

```c
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MIN 0x0005
```

相关声明：[BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MIN](#a8d044df1bfab8381b7e334597b303588)。

<a id="r_a9794f59f8d28879753b39bd504cf55be"></a>

```c
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MAX 0x0FA0
```

相关声明：[BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MAX](#a9794f59f8d28879753b39bd504cf55be)。

<a id="r_a11e614cc72adb58bda2a2bdd5f4b36ef"></a>

```c
#define BT_HCI_ISO_CIS_ID_VALID_MAX 0xEF
```

相关声明：[BT_HCI_ISO_CIS_ID_VALID_MAX](#a11e614cc72adb58bda2a2bdd5f4b36ef)。

<a id="r_a9f3e990cadf1be179fcbac3f8ef74efe"></a>

```c
#define BT_HCI_ISO_MAX_SDU_VALID_MASK 0x0FFF
```

相关声明：[BT_HCI_ISO_MAX_SDU_VALID_MASK](#a9f3e990cadf1be179fcbac3f8ef74efe)。

<a id="r_ae055ed9714ca23bebd48bb399af04d83"></a>

```c
#define BT_HCI_ISO_PHY_VALID_MASK 0x07
```

相关声明：[BT_HCI_ISO_PHY_VALID_MASK](#ae055ed9714ca23bebd48bb399af04d83)。

<a id="r_a9d5e85ae1380fa85bae9d7e5e67aa0ae"></a>

```c
#define BT_HCI_ISO_INTERVAL_MIN 0x0004
```

相关声明：[BT_HCI_ISO_INTERVAL_MIN](#a9d5e85ae1380fa85bae9d7e5e67aa0ae)。

<a id="r_aaadbec2cc6adc2bb14d7117396023d06"></a>

```c
#define BT_HCI_ISO_INTERVAL_MAX 0x0C80
```

相关声明：[BT_HCI_ISO_INTERVAL_MAX](#aaadbec2cc6adc2bb14d7117396023d06)。

<a id="r_a0a4b2732026a6300d4b354eb6d93905d"></a>

```c
#define BT_HCI_OP_LE_SET_CIG_PARAMS BT_OP(BT_OGF_LE, 0x0062) /* 0x2062 */
```

相关声明：[BT_HCI_OP_LE_SET_CIG_PARAMS](#a0a4b2732026a6300d4b354eb6d93905d)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a54df2d12a0c07bab9fb3521dc69ff2f4"></a>

```c
#define BT_HCI_OP_LE_SET_CIG_PARAMS_TEST BT_OP(BT_OGF_LE, 0x0063) /* 0x2063 */
```

相关声明：[BT_HCI_OP_LE_SET_CIG_PARAMS_TEST](#a54df2d12a0c07bab9fb3521dc69ff2f4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a63c9af35a55d9b1ed1b253d057657608"></a>

```c
#define BT_HCI_OP_LE_CREATE_CIS BT_OP(BT_OGF_LE, 0x0064) /* 0x2064 */
```

相关声明：[BT_HCI_OP_LE_CREATE_CIS](#a63c9af35a55d9b1ed1b253d057657608)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ab623f680f2031fc03bd73199ebbf4e4e"></a>

```c
#define BT_HCI_OP_LE_REMOVE_CIG BT_OP(BT_OGF_LE, 0x0065) /* 0x2065 */
```

相关声明：[BT_HCI_OP_LE_REMOVE_CIG](#ab623f680f2031fc03bd73199ebbf4e4e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ade7635c85588941a2e628639be06ce7b"></a>

```c
#define BT_HCI_OP_LE_ACCEPT_CIS BT_OP(BT_OGF_LE, 0x0066) /* 0x2066 */
```

相关声明：[BT_HCI_OP_LE_ACCEPT_CIS](#ade7635c85588941a2e628639be06ce7b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a6c58ebc2082de8c2c3aafd9ee77dfd11"></a>

```c
#define BT_HCI_OP_LE_REJECT_CIS BT_OP(BT_OGF_LE, 0x0067) /* 0x2067 */
```

相关声明：[BT_HCI_OP_LE_REJECT_CIS](#a6c58ebc2082de8c2c3aafd9ee77dfd11)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2a57bb6089e3a064e62119188b555ba9"></a>

```c
#define BT_HCI_OP_LE_CREATE_BIG BT_OP(BT_OGF_LE, 0x0068) /* 0x2068 */
```

相关声明：[BT_HCI_OP_LE_CREATE_BIG](#a2a57bb6089e3a064e62119188b555ba9)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ad0f1ae4be3f5bb90ef967d88dcaaf353"></a>

```c
#define BT_HCI_OP_LE_CREATE_BIG_TEST BT_OP(BT_OGF_LE, 0x0069) /* 0x2069 */
```

相关声明：[BT_HCI_OP_LE_CREATE_BIG_TEST](#ad0f1ae4be3f5bb90ef967d88dcaaf353)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_acc5e6c17e33cf43f2a68cb93bb09ef20"></a>

```c
#define BT_HCI_OP_LE_TERMINATE_BIG BT_OP(BT_OGF_LE, 0x006a) /* 0x206a */
```

相关声明：[BT_HCI_OP_LE_TERMINATE_BIG](#acc5e6c17e33cf43f2a68cb93bb09ef20)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a47af328ede7f14e3d78c81de609af1c9"></a>

```c
#define BT_HCI_OP_LE_BIG_CREATE_SYNC BT_OP(BT_OGF_LE, 0x006b) /* 0x206b */
```

相关声明：[BT_HCI_OP_LE_BIG_CREATE_SYNC](#a47af328ede7f14e3d78c81de609af1c9)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa7576f4ab30ec7985b4afd08a08800d2"></a>

```c
#define BT_HCI_OP_LE_BIG_TERMINATE_SYNC BT_OP(BT_OGF_LE, 0x006c) /* 0x206c */
```

相关声明：[BT_HCI_OP_LE_BIG_TERMINATE_SYNC](#aa7576f4ab30ec7985b4afd08a08800d2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0057468b1638b07f799b62a24cd096d9"></a>

```c
#define BT_HCI_OP_LE_REQ_PEER_SC BT_OP(BT_OGF_LE, 0x006d) /* 0x206d */
```

相关声明：[BT_HCI_OP_LE_REQ_PEER_SC](#a0057468b1638b07f799b62a24cd096d9)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a97de1164704f5d3c517b9c2ff6b0584a"></a>

```c
#define BT_HCI_OP_LE_SETUP_ISO_PATH BT_OP(BT_OGF_LE, 0x006e) /* 0x206e */
```

相关声明：[BT_HCI_OP_LE_SETUP_ISO_PATH](#a97de1164704f5d3c517b9c2ff6b0584a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_addec65d76f67f07c029216435cf117c6"></a>

```c
#define BT_HCI_OP_LE_REMOVE_ISO_PATH BT_OP(BT_OGF_LE, 0x006f) /* 0x206f */
```

相关声明：[BT_HCI_OP_LE_REMOVE_ISO_PATH](#addec65d76f67f07c029216435cf117c6)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aa857bdd2e81c923ab540761986074557"></a>

```c
#define BT_HCI_ISO_TEST_ZERO_SIZE_SDU 0
```

相关声明：[BT_HCI_ISO_TEST_ZERO_SIZE_SDU](#aa857bdd2e81c923ab540761986074557)。

<a id="r_aed9e2581c74218e023100d63201721af"></a>

```c
#define BT_HCI_ISO_TEST_VARIABLE_SIZE_SDU 1
```

相关声明：[BT_HCI_ISO_TEST_VARIABLE_SIZE_SDU](#aed9e2581c74218e023100d63201721af)。

<a id="r_af5c0bf9fd20df7b4a4cdb7ce18fdc7fc"></a>

```c
#define BT_HCI_ISO_TEST_MAX_SIZE_SDU 2
```

相关声明：[BT_HCI_ISO_TEST_MAX_SIZE_SDU](#af5c0bf9fd20df7b4a4cdb7ce18fdc7fc)。

<a id="r_a740f1964df5bdb675906c87ad8ee0cef"></a>

```c
#define BT_HCI_OP_LE_ISO_TRANSMIT_TEST BT_OP(BT_OGF_LE, 0x0070) /* 0x2070 */
```

相关声明：[BT_HCI_OP_LE_ISO_TRANSMIT_TEST](#a740f1964df5bdb675906c87ad8ee0cef)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a467736569f030fbb433000e712f1b08e"></a>

```c
#define BT_HCI_OP_LE_ISO_RECEIVE_TEST BT_OP(BT_OGF_LE, 0x0071) /* 0x2071 */
```

相关声明：[BT_HCI_OP_LE_ISO_RECEIVE_TEST](#a467736569f030fbb433000e712f1b08e)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a2b988ffc8ffd10ce1dfde377afa699e1"></a>

```c
#define BT_HCI_OP_LE_ISO_READ_TEST_COUNTERS BT_OP(BT_OGF_LE, 0x0072) /* 0x2072 */
```

相关声明：[BT_HCI_OP_LE_ISO_READ_TEST_COUNTERS](#a2b988ffc8ffd10ce1dfde377afa699e1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a86436e6b0cb17de95b438f192bbff1d2"></a>

```c
#define BT_HCI_OP_LE_ISO_TEST_END BT_OP(BT_OGF_LE, 0x0073) /* 0x2073 */
```

相关声明：[BT_HCI_OP_LE_ISO_TEST_END](#a86436e6b0cb17de95b438f192bbff1d2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a29555bdcc7b439c2d0311fcb0721dc0b"></a>

```c
#define BT_HCI_OP_LE_SET_HOST_FEATURE BT_OP(BT_OGF_LE, 0x0074) /* 0x2074 */
```

相关声明：[BT_HCI_OP_LE_SET_HOST_FEATURE](#a29555bdcc7b439c2d0311fcb0721dc0b)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_acd6367a62d2c80d9f2e796d7b6ab1417"></a>

```c
#define BT_HCI_OP_LE_READ_ISO_LINK_QUALITY BT_OP(BT_OGF_LE, 0x0075) /* 0x2075 */
```

相关声明：[BT_HCI_OP_LE_READ_ISO_LINK_QUALITY](#acd6367a62d2c80d9f2e796d7b6ab1417)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a13827b7d7b656ea02c0620ec7b525f65"></a>

```c
#define BT_HCI_OP_LE_TX_TEST_V4 BT_OP(BT_OGF_LE, 0x007B) /* 0x207B */
```

相关声明：[BT_HCI_OP_LE_TX_TEST_V4](#a13827b7d7b656ea02c0620ec7b525f65)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a8633ee5d0e774f7936252177d6c2ac74"></a>

```c
#define BT_HCI_OP_LE_READ_ALL_LOCAL_SUPPORTED_FEATURES BT_OP(BT_OGF_LE, 0x0087) /* 0x2087 */
```

相关声明：[BT_HCI_OP_LE_READ_ALL_LOCAL_SUPPORTED_FEATURES](#a8633ee5d0e774f7936252177d6c2ac74)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a591f7071864e66aca2a3e85d63971be3"></a>

```c
#define BT_READ_ALL_LOCAL_FEATURES_SUPPORTED(supported_commands)
```

相关声明：[BT_READ_ALL_LOCAL_FEATURES_SUPPORTED](#a591f7071864e66aca2a3e85d63971be3)。

<a id="r_a6e9bed35ad3f4f3e4c5ef5dddb2f98c2"></a>

```c
#define BT_HCI_OP_LE_READ_ALL_REMOTE_FEATURES BT_OP(BT_OGF_LE, 0x0088) /* 0x2088 */
```

相关声明：[BT_HCI_OP_LE_READ_ALL_REMOTE_FEATURES](#a6e9bed35ad3f4f3e4c5ef5dddb2f98c2)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a034d4a4fd8f7d6d324efa820d0b627d1"></a>

```c
#define BT_HCI_TX_TEST_POWER_MIN -0x7F
```

相关声明：[BT_HCI_TX_TEST_POWER_MIN](#a034d4a4fd8f7d6d324efa820d0b627d1)。

<a id="r_a925dda1fdce843e0bbcdd4acff696440"></a>

```c
#define BT_HCI_TX_TEST_POWER_MAX 0x14
```

相关声明：[BT_HCI_TX_TEST_POWER_MAX](#a925dda1fdce843e0bbcdd4acff696440)。

<a id="r_a5d0fc1dbb127ba0a383e4e56bb503334"></a>

```c
#define BT_HCI_TX_TEST_POWER_MIN_SET 0x7E
```

相关声明：[BT_HCI_TX_TEST_POWER_MIN_SET](#a5d0fc1dbb127ba0a383e4e56bb503334)。

<a id="r_a2e9caac5d12f8df1ce69a54f603500ee"></a>

```c
#define BT_HCI_TX_TEST_POWER_MAX_SET 0x7F
```

相关声明：[BT_HCI_TX_TEST_POWER_MAX_SET](#a2e9caac5d12f8df1ce69a54f603500ee)。

<a id="r_a84e0338551dd8256a821d960bf745208"></a>

```c
#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x0089) /* 0x2089 */
```

相关声明：[BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES](#a84e0338551dd8256a821d960bf745208)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_aac9dd21ae34a16f4cfb5a51abe14f024"></a>

```c
#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2 BT_OP(BT_OGF_LE, 0x00A5) /* 0x20A5 */
```

相关声明：[BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2](#aac9dd21ae34a16f4cfb5a51abe14f024)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

HCI 低功耗蓝牙读取本地支持能力（LE Read Local Supported Capabilities，v2）操作码。

<a id="r_a00b4acee1dd74405ef0a9dfcef4133f1"></a>

```c
#define BT_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2_SUPPORTED(cmd)
```

相关声明：[BT_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2_SUPPORTED](#a00b4acee1dd74405ef0a9dfcef4133f1)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

测试是否支持 LE Read Local Supported Capabilities v2 命令（读取本地支持能力，第 49 八位组的位 2）。

<a id="r_a4f6dd157a555e06cd028a9097fd7b81a"></a>

```c
#define BT_HCI_OP_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x008A) /* 0x208A */
```

相关声明：[BT_HCI_OP_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES](#a4f6dd157a555e06cd028a9097fd7b81a)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_acdbbe0da013fb3b6da5514498c3932dd"></a>

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x008B) /* 0x208B */
```

相关声明：[BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES](#acdbbe0da013fb3b6da5514498c3932dd)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a523daa9b70fb57ae36a4bb9ff158cce8"></a>

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES_V2 BT_OP(BT_OGF_LE, 0x00A6) /* 0x20A6 */
```

相关声明：[BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES_V2](#a523daa9b70fb57ae36a4bb9ff158cce8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

HCI 低功耗蓝牙信道探测写入缓存的远端支持能力（LE CS Write Cached Remote Supported Capabilities，v2）操作码。

<a id="r_a574168efdaa5729aec9699d48f988d77"></a>

```c
#define BT_HCI_OP_LE_CS_SECURITY_ENABLE BT_OP(BT_OGF_LE, 0x008C) /* 0x208C */
```

相关声明：[BT_HCI_OP_LE_CS_SECURITY_ENABLE](#a574168efdaa5729aec9699d48f988d77)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_addb1ab37dc75ab5389d74c6c96629b02"></a>

```c
#define BT_HCI_OP_LE_CS_SET_DEFAULT_SETTINGS BT_OP(BT_OGF_LE, 0x008D) /* 0x208D */
```

相关声明：[BT_HCI_OP_LE_CS_SET_DEFAULT_SETTINGS](#addb1ab37dc75ab5389d74c6c96629b02)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a74aaa5b6b799dad3af6778e23093b230"></a>

```c
#define BT_HCI_OP_LE_CS_INITIATOR_ROLE_MASK BIT(0)
```

相关声明：[BT_HCI_OP_LE_CS_INITIATOR_ROLE_MASK](#a74aaa5b6b799dad3af6778e23093b230)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1beb2f602b3635fee272580f0f2f8719"></a>

```c
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE_MASK BIT(1)
```

相关声明：[BT_HCI_OP_LE_CS_REFLECTOR_ROLE_MASK](#a1beb2f602b3635fee272580f0f2f8719)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a040315a8ac4f80a2c497919a2fd4d7bc"></a>

```c
#define BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER -127
```

相关声明：[BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER](#a040315a8ac4f80a2c497919a2fd4d7bc)。

<a id="r_a29a240b2d3f209b1f5f3d96e380dde08"></a>

```c
#define BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER 20
```

相关声明：[BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER](#a29a240b2d3f209b1f5f3d96e380dde08)。

<a id="r_a7fa26323384443ba9c5e635047b74f51"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_ONE 0x01
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_ONE](#a7fa26323384443ba9c5e635047b74f51)。

<a id="r_aa6d146c85e3148a2afb66023d94c2eeb"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_TWO 0x02
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_TWO](#aa6d146c85e3148a2afb66023d94c2eeb)。

<a id="r_a8721a8f4670a8038d66d42adea061f57"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_THREE 0x03
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_THREE](#a8721a8f4670a8038d66d42adea061f57)。

<a id="r_af0d407f944831f8c85f91fb60f5bc618"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_FOUR 0x04
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_FOUR](#af0d407f944831f8c85f91fb60f5bc618)。

<a id="r_afad5b26b2a6ce125b6198856d20bcdd8"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_REP 0xFE
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_REP](#afad5b26b2a6ce125b6198856d20bcdd8)。

<a id="r_aed2444a40bc79ccf3f383dd961036f5e"></a>

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_NONE 0xFF
```

相关声明：[BT_HCI_OP_LE_CS_ANTENNA_SEL_NONE](#aed2444a40bc79ccf3f383dd961036f5e)。

<a id="r_afa7a0214b145891562f1d2b7b16860ab"></a>

```c
#define BT_HCI_OP_LE_CS_READ_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008E) /* 0x208E */
```

相关声明：[BT_HCI_OP_LE_CS_READ_REMOTE_FAE_TABLE](#afa7a0214b145891562f1d2b7b16860ab)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a44eb5d70628f6522a08b1327588df979"></a>

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008F) /* 0x208F */
```

相关声明：[BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_FAE_TABLE](#a44eb5d70628f6522a08b1327588df979)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a880439089735247c7011862d5b3e090f"></a>

```c
#define BT_HCI_OP_LE_CS_SET_CHANNEL_CLASSIFICATION BT_OP(BT_OGF_LE, 0x0092) /* 0x2092 */
```

相关声明：[BT_HCI_OP_LE_CS_SET_CHANNEL_CLASSIFICATION](#a880439089735247c7011862d5b3e090f)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_ad74850cecd8d8dd8a7878d944abdb411"></a>

```c
#define BT_HCI_OP_LE_CS_SET_PROCEDURE_PARAMETERS BT_OP(BT_OGF_LE, 0x0093) /* 0x2093 */
```

相关声明：[BT_HCI_OP_LE_CS_SET_PROCEDURE_PARAMETERS](#ad74850cecd8d8dd8a7878d944abdb411)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a3a8f1c94f40696f18e18810f736497e3"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_1M 0x01
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURE_PHY_1M](#a3a8f1c94f40696f18e18810f736497e3)。

<a id="r_a016f68a621de8d332f3073df4faf1702"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_2M 0x02
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURE_PHY_2M](#a016f68a621de8d332f3073df4faf1702)。

<a id="r_a2543f9fa20db642fb8b47b949c50af6a"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S8 0x03
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S8](#a2543f9fa20db642fb8b47b949c50af6a)。

<a id="r_a776a14d8e7fdca584475f26b441c8bfb"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S2 0x04
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S2](#a776a14d8e7fdca584475f26b441c8bfb)。

<a id="r_a4eddce6558339caba6a3d16f8fe5d485"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_ENABLE BT_OP(BT_OGF_LE, 0x0094) /* 0x2094 */
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURE_ENABLE](#a4eddce6558339caba6a3d16f8fe5d485)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a3e01bbe3a72c946015a288ee49d3cbdd"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURES_DISABLED 0x00
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURES_DISABLED](#a3e01bbe3a72c946015a288ee49d3cbdd)。

<a id="r_a4a88120ae7e83fd791012c913315d14f"></a>

```c
#define BT_HCI_OP_LE_CS_PROCEDURES_ENABLED 0x01
```

相关声明：[BT_HCI_OP_LE_CS_PROCEDURES_ENABLED](#a4a88120ae7e83fd791012c913315d14f)。

<a id="r_af09601cffd1adf3f8b623868d8f8a3e9"></a>

```c
#define BT_HCI_OP_LE_CS_TEST BT_OP(BT_OGF_LE, 0x0095) /* 0x2095 */
```

相关声明：[BT_HCI_OP_LE_CS_TEST](#af09601cffd1adf3f8b623868d8f8a3e9)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_af1b7924e50ba017e59d697fd8814d491"></a>

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_1 0x1
```

相关声明：[BT_HCI_OP_LE_CS_MAIN_MODE_1](#af1b7924e50ba017e59d697fd8814d491)。

<a id="r_a714152a085bbc317b539d6e973ccffc6"></a>

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_2 0x2
```

相关声明：[BT_HCI_OP_LE_CS_MAIN_MODE_2](#a714152a085bbc317b539d6e973ccffc6)。

<a id="r_a5d2af0ed5e0cc5cf7d9f0baae512ff68"></a>

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_3 0x3
```

相关声明：[BT_HCI_OP_LE_CS_MAIN_MODE_3](#a5d2af0ed5e0cc5cf7d9f0baae512ff68)。

<a id="r_a219243d501bbcb6d62668398cde79fca"></a>

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_1 0x1
```

相关声明：[BT_HCI_OP_LE_CS_SUB_MODE_1](#a219243d501bbcb6d62668398cde79fca)。

<a id="r_ada09c787fca0a1d54bb754635489b51e"></a>

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_2 0x2
```

相关声明：[BT_HCI_OP_LE_CS_SUB_MODE_2](#ada09c787fca0a1d54bb754635489b51e)。

<a id="r_a4b48c199b6b75e9dd62ec36883b40aa4"></a>

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_3 0x3
```

相关声明：[BT_HCI_OP_LE_CS_SUB_MODE_3](#a4b48c199b6b75e9dd62ec36883b40aa4)。

<a id="r_ab3fce1eb448b0ade581e4e12b2d56039"></a>

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_UNUSED 0xFF
```

相关声明：[BT_HCI_OP_LE_CS_SUB_MODE_UNUSED](#ab3fce1eb448b0ade581e4e12b2d56039)。

<a id="r_a4505bedc3b5aae63b80cf53fc516b342"></a>

```c
#define BT_HCI_OP_LE_CS_INITIATOR_ROLE 0x0
```

相关声明：[BT_HCI_OP_LE_CS_INITIATOR_ROLE](#a4505bedc3b5aae63b80cf53fc516b342)。

<a id="r_aeb3715dfcac55a46532f51279e29708c"></a>

```c
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE 0x1
```

相关声明：[BT_HCI_OP_LE_CS_REFLECTOR_ROLE](#aeb3715dfcac55a46532f51279e29708c)。

<a id="r_a759eb7a8e43ee7cf1ea88ddd3e69feb5"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY 0x0
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY](#a759eb7a8e43ee7cf1ea88ddd3e69feb5)。

<a id="r_aa2ae18252a20ef3481d2402f8924cdda"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND 0x1
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND](#aa2ae18252a20ef3481d2402f8924cdda)。

<a id="r_a73cbfe2a942b684ac0b5b50d900fb83f"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND 0x2
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND](#a73cbfe2a942b684ac0b5b50d900fb83f)。

<a id="r_abe4efee7cf9371129f4b5bd650b0d64a"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND 0x3
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND](#abe4efee7cf9371129f4b5bd650b0d64a)。

<a id="r_a77e56fd5302673f6ef295c0cceabdc9f"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND 0x4
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND](#a77e56fd5302673f6ef295c0cceabdc9f)。

<a id="r_aa60f64ff7259fd79fb1da2c063530348"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND 0x5
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND](#aa60f64ff7259fd79fb1da2c063530348)。

<a id="r_a1fe5e94fbd1156c8196c8e1ab9816bac"></a>

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND 0x6
```

相关声明：[BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND](#a1fe5e94fbd1156c8196c8e1ab9816bac)。

<a id="r_a7baf90f5bf691ce6b650677e6c2a9600"></a>

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_1M 0x1
```

相关声明：[BT_HCI_OP_LE_CS_CS_SYNC_1M](#a7baf90f5bf691ce6b650677e6c2a9600)。

<a id="r_ae49d35db87532e06ea685a63eb89177a"></a>

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_2M 0x2
```

相关声明：[BT_HCI_OP_LE_CS_CS_SYNC_2M](#ae49d35db87532e06ea685a63eb89177a)。

<a id="r_ac34716156b071e06eb454f091a63216c"></a>

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT 0x3
```

相关声明：[BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT](#ac34716156b071e06eb454f091a63216c)。

<a id="r_a500597c78a6ada65d1224960bf6a370f"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER 0x7E
```

相关声明：[BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER](#a500597c78a6ada65d1224960bf6a370f)。

<a id="r_a50eb827977c0c596cb357ed62a6e80bd"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER 0x7F
```

相关声明：[BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER](#a50eb827977c0c596cb357ed62a6e80bd)。

<a id="r_a92e1ec21014999f40172fa1812c36575"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_0 0x0
```

相关声明：[BT_HCI_OP_LE_CS_ACI_0](#a92e1ec21014999f40172fa1812c36575)。

<a id="r_a5b082fa5b8ba11a651468cc516d067fe"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_1 0x1
```

相关声明：[BT_HCI_OP_LE_CS_ACI_1](#a5b082fa5b8ba11a651468cc516d067fe)。

<a id="r_ab30a4e55002080394c39fb885eba36e4"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_2 0x2
```

相关声明：[BT_HCI_OP_LE_CS_ACI_2](#ab30a4e55002080394c39fb885eba36e4)。

<a id="r_a76d1452003c0bd3b688765aa2d25047f"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_3 0x3
```

相关声明：[BT_HCI_OP_LE_CS_ACI_3](#a76d1452003c0bd3b688765aa2d25047f)。

<a id="r_af16c4c79e602e6da833b8aa3e0c4bf64"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_4 0x4
```

相关声明：[BT_HCI_OP_LE_CS_ACI_4](#af16c4c79e602e6da833b8aa3e0c4bf64)。

<a id="r_ad980d8f134d940b80dc9b0e3a570ac06"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_5 0x5
```

相关声明：[BT_HCI_OP_LE_CS_ACI_5](#ad980d8f134d940b80dc9b0e3a570ac06)。

<a id="r_a4c7ff3c949023f4544bf50353a0f082b"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_6 0x6
```

相关声明：[BT_HCI_OP_LE_CS_ACI_6](#a4c7ff3c949023f4544bf50353a0f082b)。

<a id="r_acabccf9f5893324dcb6acc0769ab8417"></a>

```c
#define BT_HCI_OP_LE_CS_ACI_7 0x7
```

相关声明：[BT_HCI_OP_LE_CS_ACI_7](#acabccf9f5893324dcb6acc0769ab8417)。

<a id="r_a96b13fb3b363a5436e1b9633f54bb248"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_18 0x0
```

相关声明：[BT_HCI_OP_LE_CS_SNR_18](#a96b13fb3b363a5436e1b9633f54bb248)。

<a id="r_a4b93a8bceafd49d6ca65816924bb4230"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_21 0x1
```

相关声明：[BT_HCI_OP_LE_CS_SNR_21](#a4b93a8bceafd49d6ca65816924bb4230)。

<a id="r_a135a4dc2f191d2a931b4270e00774cb2"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_24 0x2
```

相关声明：[BT_HCI_OP_LE_CS_SNR_24](#a135a4dc2f191d2a931b4270e00774cb2)。

<a id="r_a52eb27d8f726a2ed6859149fcdf2355d"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_27 0x3
```

相关声明：[BT_HCI_OP_LE_CS_SNR_27](#a52eb27d8f726a2ed6859149fcdf2355d)。

<a id="r_a181c2d98b93bd18e9edc11a6f9535331"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_30 0x4
```

相关声明：[BT_HCI_OP_LE_CS_SNR_30](#a181c2d98b93bd18e9edc11a6f9535331)。

<a id="r_a4aa2e02ce5110be3dc68a801bb583372"></a>

```c
#define BT_HCI_OP_LE_CS_SNR_NOT_USED 0xFF
```

相关声明：[BT_HCI_OP_LE_CS_SNR_NOT_USED](#a4aa2e02ce5110be3dc68a801bb583372)。

<a id="r_a0a73e0d46b5ca0e94b4bb00d2f79e89d"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_0_MASK BIT(0)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_0_MASK](#a0a73e0d46b5ca0e94b4bb00d2f79e89d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2a62cbc191abd177cbf5aea27112fb8b"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_2_MASK BIT(2)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_2_MASK](#a2a62cbc191abd177cbf5aea27112fb8b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a560f6f1bddedc60b3a373778bc56b1a7"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_3_MASK BIT(3)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_3_MASK](#a560f6f1bddedc60b3a373778bc56b1a7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a36c2c6debe6bf395853112c68a726d25"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_4_MASK BIT(4)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_4_MASK](#a36c2c6debe6bf395853112c68a726d25)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4aca98e213ba81c999c8495310af9320"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_5_MASK BIT(5)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_5_MASK](#a4aca98e213ba81c999c8495310af9320)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afd7b8b4ec0baf526cc4335d26c380b62"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_6_MASK BIT(6)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_6_MASK](#afd7b8b4ec0baf526cc4335d26c380b62)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a695d2ba272dbdd2681ab9216d00ca43a"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_7_MASK BIT(7)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_7_MASK](#a695d2ba272dbdd2681ab9216d00ca43a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad92a29871be9aff39802fdea4446ef4b"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_8_MASK BIT(8)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_8_MASK](#ad92a29871be9aff39802fdea4446ef4b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a90c77fe0022f016453a8eb174b8fcd63"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_10_MASK BIT(10)
```

相关声明：[BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_10_MASK](#a90c77fe0022f016453a8eb174b8fcd63)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a77d27762b9faa7743a55d822a1839eac"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B 0x0
```

相关声明：[BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B](#a77d27762b9faa7743a55d822a1839eac)。

<a id="r_af17f867204bc7cf99e5d530c39302be0"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C 0x1
```

相关声明：[BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C](#af17f867204bc7cf99e5d530c39302be0)。

<a id="r_acd33fc2eb3f5ebe10cbe4c5060f8336b"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT 0x0
```

相关声明：[BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT](#acd33fc2eb3f5ebe10cbe4c5060f8336b)。

<a id="r_ad09c735ab352d7a546cade296e915e85"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X 0x1
```

相关声明：[BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X](#ad09c735ab352d7a546cade296e915e85)。

<a id="r_a9ed8967faa3ee3824433422709148330"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_NONE 0x0
```

相关声明：[BT_HCI_OP_LE_CS_TEST_TONE_EXT_NONE](#a9ed8967faa3ee3824433422709148330)。

<a id="r_a0513bf5ca6eb9f43a7e8cecaf943c4d7"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_INIT 0x1
```

相关声明：[BT_HCI_OP_LE_CS_TEST_TONE_EXT_INIT](#a0513bf5ca6eb9f43a7e8cecaf943c4d7)。

<a id="r_aa24ae1cf1501de66660051a4a62246df"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REFL 0x2
```

相关声明：[BT_HCI_OP_LE_CS_TEST_TONE_EXT_REFL](#aa24ae1cf1501de66660051a4a62246df)。

<a id="r_ad7a89a9365e20e4cd1e44bdb74ae7ecb"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_BOTH 0x3
```

相关声明：[BT_HCI_OP_LE_CS_TEST_TONE_EXT_BOTH](#ad7a89a9365e20e4cd1e44bdb74ae7ecb)。

<a id="r_a50fba6ab75b37ccf39452211ba05e896"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REPEAT 0x4
```

相关声明：[BT_HCI_OP_LE_CS_TEST_TONE_EXT_REPEAT](#a50fba6ab75b37ccf39452211ba05e896)。

<a id="r_aa4ba4be270035da446389766b795c327"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_00 0x0
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_00](#aa4ba4be270035da446389766b795c327)。

<a id="r_aa0e9e2081d3cbbb60de9b6dcffe77239"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_01 0x1
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_01](#aa0e9e2081d3cbbb60de9b6dcffe77239)。

<a id="r_a762c5efa09e1fba989fdfb0bdcba9b9c"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_02 0x2
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_02](#a762c5efa09e1fba989fdfb0bdcba9b9c)。

<a id="r_a2cc7a5d5d2105b1a428703e274cc5388"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_03 0x3
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_03](#a2cc7a5d5d2105b1a428703e274cc5388)。

<a id="r_a03ffb0ffb8e98b26390575b153471bab"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_04 0x4
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_04](#a03ffb0ffb8e98b26390575b153471bab)。

<a id="r_adbd3820e0ffa5f99e27778217d477010"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_05 0x5
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_05](#adbd3820e0ffa5f99e27778217d477010)。

<a id="r_a70607449d6bd6207783e319e77d63b16"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_06 0x6
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_06](#a70607449d6bd6207783e319e77d63b16)。

<a id="r_acc79a879ea527c2901a8b91dae58d0ed"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_07 0x7
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_07](#acc79a879ea527c2901a8b91dae58d0ed)。

<a id="r_a9dfd88863d649182855edc8c268107d6"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_08 0x8
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_08](#a9dfd88863d649182855edc8c268107d6)。

<a id="r_ae5a27304aa1cefdfb26ae2cbf42532e3"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_09 0x9
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_09](#ae5a27304aa1cefdfb26ae2cbf42532e3)。

<a id="r_a0e9664c52808aa246218f92a4fb55516"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_10 0xA
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_10](#a0e9664c52808aa246218f92a4fb55516)。

<a id="r_a8fbc80d91e4a1ae04c76cda189cd5d83"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_11 0xB
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_11](#a8fbc80d91e4a1ae04c76cda189cd5d83)。

<a id="r_a4c4a44bd33ebf97852e6640b0d510fdd"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_12 0xC
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_12](#a4c4a44bd33ebf97852e6640b0d510fdd)。

<a id="r_a08690b2f762d24c34966b839a6d5e696"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_13 0xD
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_13](#a08690b2f762d24c34966b839a6d5e696)。

<a id="r_ac2cd3ed1583f86af0480b8481cedca1e"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_14 0xE
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_14](#ac2cd3ed1583f86af0480b8481cedca1e)。

<a id="r_ab2b0745d98053775e9bf073e36ce5d78"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_15 0xF
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_15](#ab2b0745d98053775e9bf073e36ce5d78)。

<a id="r_add2c42aa2583b93b0f98ac33ca61ca9d"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_16 0x10
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_16](#add2c42aa2583b93b0f98ac33ca61ca9d)。

<a id="r_a08db476ea6516691baeb9007b553281d"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_17 0x11
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_17](#a08db476ea6516691baeb9007b553281d)。

<a id="r_a9f0bf05cb0aac50e1df43397c3b913bc"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_18 0x12
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_18](#a9f0bf05cb0aac50e1df43397c3b913bc)。

<a id="r_a5df817bdfefc4de0a1309cf71908a105"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_19 0x13
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_19](#a5df817bdfefc4de0a1309cf71908a105)。

<a id="r_ae64e5a409523b94ef1ce315ed49afed0"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_20 0x14
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_20](#ae64e5a409523b94ef1ce315ed49afed0)。

<a id="r_a46f70b5096593956795cc381e33c4aa2"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_21 0x15
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_21](#a46f70b5096593956795cc381e33c4aa2)。

<a id="r_abe9fa4621e9c004421170b0166ea14e1"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_22 0x16
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_22](#abe9fa4621e9c004421170b0166ea14e1)。

<a id="r_afc41ca64d03a7ed8ea82a641a0217436"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_23 0x17
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_23](#afc41ca64d03a7ed8ea82a641a0217436)。

<a id="r_ac9d7cb5a339759b7e0c4ed150a487ca3"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_LOOP 0xFF
```

相关声明：[BT_HCI_OP_LE_CS_TEST_AP_INDEX_LOOP](#ac9d7cb5a339759b7e0c4ed150a487ca3)。

<a id="r_a1f2bfc1afab1928321c01beddb658f01"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT 0xFF
```

相关声明：[BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT](#a1f2bfc1afab1928321c01beddb658f01)。

<a id="r_a45e1ff56f1a6dcc59b784905e4fc6726"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_0011 0x0
```

相关声明：[BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_0011](#a45e1ff56f1a6dcc59b784905e4fc6726)。

<a id="r_a5d3c206a5067ddc5a02a5d5e8c3eb7a3"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_1100 0x1
```

相关声明：[BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_1100](#a5d3c206a5067ddc5a02a5d5e8c3eb7a3)。

<a id="r_a24d2e56f620500905572e786f2523b0e"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_LOOP 0x2
```

相关声明：[BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_LOOP](#a24d2e56f620500905572e786f2523b0e)。

<a id="r_a4f922c5e0662adf8471686dfa9b719ec"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS9 0x00
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS9](#a4f922c5e0662adf8471686dfa9b719ec)。

<a id="r_af20dfb1e245afc06a495179d700f126f"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11110000 0x01
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_11110000](#af20dfb1e245afc06a495179d700f126f)。

<a id="r_ae133ef2939518d660df5322551157d47"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_10101010 0x02
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_10101010](#ae133ef2939518d660df5322551157d47)。

<a id="r_a92bc70a5ad7938a46ac9f2127f1bc2d9"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS15 0x03
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS15](#a92bc70a5ad7938a46ac9f2127f1bc2d9)。

<a id="r_aa94eda86c6ffe85a65267f285dae5cb1"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11111111 0x04
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_11111111](#aa94eda86c6ffe85a65267f285dae5cb1)。

<a id="r_a04a26b8600cac8c82247a7d51122f600"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00000000 0x05
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_00000000](#a04a26b8600cac8c82247a7d51122f600)。

<a id="r_abf19d511680005828add231d64e1e3f0"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00001111 0x06
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_00001111](#abf19d511680005828add231d64e1e3f0)。

<a id="r_a53f0ca5604489a38a1367736a5297b45"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_01010101 0x07
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_01010101](#a53f0ca5604489a38a1367736a5297b45)。

<a id="r_a94007d8250c3524ad0b86745dbb74b3b"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_USER 0x80
```

相关声明：[BT_HCI_OP_LE_CS_TEST_PAYLOAD_USER](#a94007d8250c3524ad0b86745dbb74b3b)。

<a id="r_af26aad0e137782c8f12937b1736d6ada"></a>

```c
#define BT_HCI_OP_LE_CS_CREATE_CONFIG BT_OP(BT_OGF_LE, 0x0090) /* 0x2090 */
```

相关声明：[BT_HCI_OP_LE_CS_CREATE_CONFIG](#af26aad0e137782c8f12937b1736d6ada)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a54116ddaa8338d59b23fb879c185a399"></a>

```c
#define BT_HCI_OP_LE_CS_REMOVE_CONFIG BT_OP(BT_OGF_LE, 0x0091) /* 0x2091 */
```

相关声明：[BT_HCI_OP_LE_CS_REMOVE_CONFIG](#a54116ddaa8338d59b23fb879c185a399)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a4c45c8b2b33ae857c654cc100b5e5550"></a>

```c
#define BT_HCI_OP_LE_CS_TEST_END BT_OP(BT_OGF_LE, 0x0096) /* 0x2096 */
```

相关声明：[BT_HCI_OP_LE_CS_TEST_END](#a4c45c8b2b33ae857c654cc100b5e5550)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a5dc8fa3e7157ca71b48a3cde12115664"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_1M_MASK BIT(0)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_1M_MASK](#a5dc8fa3e7157ca71b48a3cde12115664)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a82ebdbd872d0d2905b2c29d15b1a019d"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_2M_MASK BIT(1)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_2M_MASK](#a82ebdbd872d0d2905b2c29d15b1a019d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5d63134bfa327abae3cf2d7a67980f39"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_CODED_MASK BIT(2)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_CODED_MASK](#a5d63134bfa327abae3cf2d7a67980f39)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1ff1899e87988795cb56cf3ac69fc661"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK BIT(0)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK](#a1ff1899e87988795cb56cf3ac69fc661)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac390cbfa78d9027cbb6b9cda5e11c9c6"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK BIT(1)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK](#ac390cbfa78d9027cbb6b9cda5e11c9c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af7216a6ef4ccc35e081d7b18513af2d2"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK BIT(2)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK](#af7216a6ef4ccc35e081d7b18513af2d2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7f490f8f8ac13199da1c2af10adea5de"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK BIT(3)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK](#a7f490f8f8ac13199da1c2af10adea5de)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1e3128522364b82dc7a3ba05f89b96fc"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK BIT(4)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK](#a1e3128522364b82dc7a3ba05f89b96fc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a076869aba2dc8593b2263c642cdaa148"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST (0)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST](#a076869aba2dc8593b2263c642cdaa148)。

<a id="r_a45ff3a04cd0179ed02576136114ed8c0"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER (1)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER](#a45ff3a04cd0179ed02576136114ed8c0)。

<a id="r_acb1d2b1b3e2e1802b81dbeb82bcc9f12"></a>

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER (2)
```

相关声明：[BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER](#acb1d2b1b3e2e1802b81dbeb82bcc9f12)。

<a id="r_acf8c51fe662c42853f4c023b25bcbd48"></a>

```c
#define BT_HCI_OP_LE_FRAME_SPACE_UPDATE BT_OP(BT_OGF_LE, 0x009D) /* 0x209D */
```

相关声明：[BT_HCI_OP_LE_FRAME_SPACE_UPDATE](#acf8c51fe662c42853f4c023b25bcbd48)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a292c11301eed063f4b9cfec645881a47"></a>

```c
#define BT_HCI_LE_SCI_INTERVAL_MIN_125US (0x0003U)
```

相关声明：[BT_HCI_LE_SCI_INTERVAL_MIN_125US](#a292c11301eed063f4b9cfec645881a47)。

所有限制均依据《蓝牙核心规范》（BT Core Spec）6.2，第 4 卷 E 部分 7.8.154。

<a id="r_a14c9d4eab8b8fe650ea2950d0c3a703f"></a>

```c
#define BT_HCI_LE_SCI_INTERVAL_MAX_125US (0x7D00U)
```

相关声明：[BT_HCI_LE_SCI_INTERVAL_MAX_125US](#a14c9d4eab8b8fe650ea2950d0c3a703f)。

<a id="r_a9d55d12b5d3c37c99730950878075684"></a>

```c
#define BT_HCI_LE_SCI_INTERVAL_MIN_US (375U)
```

相关声明：[BT_HCI_LE_SCI_INTERVAL_MIN_US](#a9d55d12b5d3c37c99730950878075684)。

<a id="r_ad6ccdf8c0658b065218f10581990fef8"></a>

```c
#define BT_HCI_LE_SCI_INTERVAL_MAX_US (4000000U)
```

相关声明：[BT_HCI_LE_SCI_INTERVAL_MAX_US](#ad6ccdf8c0658b065218f10581990fef8)。

<a id="r_a47b99bb33143c6a936af1462ce791313"></a>

```c
#define BT_HCI_LE_SCI_INTERVAL_UNIT_US (125U)
```

相关声明：[BT_HCI_LE_SCI_INTERVAL_UNIT_US](#a47b99bb33143c6a936af1462ce791313)。

<a id="r_aea8e6814082534c65773ceb291d60c49"></a>

```c
#define BT_HCI_LE_SCI_STRIDE_MIN_125US (0x0001U)
```

相关声明：[BT_HCI_LE_SCI_STRIDE_MIN_125US](#aea8e6814082534c65773ceb291d60c49)。

<a id="r_ac5dd60afc8c8bff309090fca1b6875aa"></a>

```c
#define BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US (375U)
```

相关声明：[BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US](#ac5dd60afc8c8bff309090fca1b6875aa)。

<a id="r_ac6ae380e312559c82742975cf5ed742f"></a>

```c
#define BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US (7500U)
```

相关声明：[BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US](#ac6ae380e312559c82742975cf5ed742f)。

<a id="r_acef97af0baeb7f491d66ec1d0b4fff36"></a>

```c
#define BT_HCI_LE_SCI_CE_LEN_MIN_125US (0x0001U)
```

相关声明：[BT_HCI_LE_SCI_CE_LEN_MIN_125US](#acef97af0baeb7f491d66ec1d0b4fff36)。

<a id="r_ab0319b6bf5387c5a4d2d38d789fab6aa"></a>

```c
#define BT_HCI_LE_SCI_CE_LEN_MAX_125US (0x3E7FU)
```

相关声明：[BT_HCI_LE_SCI_CE_LEN_MAX_125US](#ab0319b6bf5387c5a4d2d38d789fab6aa)。

<a id="r_a46425554910f04a93f8819f3aede38c1"></a>

```c
#define BT_HCI_OP_LE_READ_MIN_SUPPORTED_CONN_INTERVAL BT_OP(BT_OGF_LE, 0x00A3) /* 0x20A3 */
```

相关声明：[BT_HCI_OP_LE_READ_MIN_SUPPORTED_CONN_INTERVAL](#a46425554910f04a93f8819f3aede38c1)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0cbe2f1d110c04231e859f18e3a102f8"></a>

```c
#define BT_HCI_OP_LE_SET_DEFAULT_RATE_PARAMETERS BT_OP(BT_OGF_LE, 0x00A2) /* 0x20A2 */
```

相关声明：[BT_HCI_OP_LE_SET_DEFAULT_RATE_PARAMETERS](#a0cbe2f1d110c04231e859f18e3a102f8)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a41d7e2f884f868bcb5805781730e5ab4"></a>

```c
#define BT_HCI_OP_LE_CONNECTION_RATE_REQUEST BT_OP(BT_OGF_LE, 0x00A1) /* 0x20A1 */
```

相关声明：[BT_HCI_OP_LE_CONNECTION_RATE_REQUEST](#a41d7e2f884f868bcb5805781730e5ab4)、[BT_OP](#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_LE](#abb09db6a211185842f039eddb9fadca5)。

<a id="r_a0f44f6e5037d650b9dd0c5f34ba681b5"></a>

```c
#define BT_HCI_EVT_UNKNOWN 0x00
```

相关声明：[BT_HCI_EVT_UNKNOWN](#a0f44f6e5037d650b9dd0c5f34ba681b5)。

<a id="r_a955fe06f3fcab82c3370cb621f0dbca0"></a>

```c
#define BT_HCI_EVT_VENDOR 0xff
```

相关声明：[BT_HCI_EVT_VENDOR](#a955fe06f3fcab82c3370cb621f0dbca0)。

<a id="r_abd8f15d920c0bdb3c68556b4e873f413"></a>

```c
#define BT_HCI_EVT_INQUIRY_COMPLETE 0x01
```

相关声明：[BT_HCI_EVT_INQUIRY_COMPLETE](#abd8f15d920c0bdb3c68556b4e873f413)。

<a id="r_a0dd2162851b4a7afc3d96924f69cceca"></a>

```c
#define BT_HCI_EVT_CONN_COMPLETE 0x03
```

相关声明：[BT_HCI_EVT_CONN_COMPLETE](#a0dd2162851b4a7afc3d96924f69cceca)。

<a id="r_afc473fec33612ffb044d54bad39e8d76"></a>

```c
#define BT_HCI_EVT_CONN_REQUEST 0x04
```

相关声明：[BT_HCI_EVT_CONN_REQUEST](#afc473fec33612ffb044d54bad39e8d76)。

<a id="r_a32e5051a114f8987b49c6957c84d60e2"></a>

```c
#define BT_HCI_EVT_DISCONN_COMPLETE 0x05
```

相关声明：[BT_HCI_EVT_DISCONN_COMPLETE](#a32e5051a114f8987b49c6957c84d60e2)。

<a id="r_acc9c74c8406b84baaf55d9452924aaf9"></a>

```c
#define BT_HCI_EVT_AUTH_COMPLETE 0x06
```

相关声明：[BT_HCI_EVT_AUTH_COMPLETE](#acc9c74c8406b84baaf55d9452924aaf9)。

<a id="r_a1a4be9cf628063db2fb821f67c54ea56"></a>

```c
#define BT_HCI_EVT_REMOTE_NAME_REQ_COMPLETE 0x07
```

相关声明：[BT_HCI_EVT_REMOTE_NAME_REQ_COMPLETE](#a1a4be9cf628063db2fb821f67c54ea56)。

<a id="r_a1828465a27d0a30b0da6dfeb40ff3915"></a>

```c
#define BT_HCI_ENCRYPTION_OFF 0x00
```

相关声明：[BT_HCI_ENCRYPTION_OFF](#a1828465a27d0a30b0da6dfeb40ff3915)。

<a id="r_aa3946f9d506682315e81823121bcd34a"></a>

```c
#define BT_HCI_ENCRYPTION_ON_LE_AES_CCM 0x01
```

相关声明：[BT_HCI_ENCRYPTION_ON_LE_AES_CCM](#aa3946f9d506682315e81823121bcd34a)。

<a id="r_ab4bf0fcc115109a5d5cb12f9bbbf0225"></a>

```c
#define BT_HCI_ENCRYPTION_ON_BR_E0 0x01
```

相关声明：[BT_HCI_ENCRYPTION_ON_BR_E0](#ab4bf0fcc115109a5d5cb12f9bbbf0225)。

<a id="r_a355ff7e0b5a5deea620f04a56e869be2"></a>

```c
#define BT_HCI_ENCRYPTION_ON_BR_AES_CCM 0x02
```

相关声明：[BT_HCI_ENCRYPTION_ON_BR_AES_CCM](#a355ff7e0b5a5deea620f04a56e869be2)。

<a id="r_a8dee2fc366d0371b68b212ff40e6ea7d"></a>

```c
#define BT_HCI_EVT_ENCRYPT_CHANGE 0x08
```

相关声明：[BT_HCI_EVT_ENCRYPT_CHANGE](#a8dee2fc366d0371b68b212ff40e6ea7d)。

<a id="r_acbad340a978d4fc118af826d2c1a81e3"></a>

```c
#define BT_HCI_EVT_REMOTE_FEATURES 0x0b
```

相关声明：[BT_HCI_EVT_REMOTE_FEATURES](#acbad340a978d4fc118af826d2c1a81e3)。

<a id="r_a18f58c80d213d666ee8309cda8eb0a26"></a>

```c
#define BT_HCI_EVT_REMOTE_VERSION_INFO 0x0c
```

相关声明：[BT_HCI_EVT_REMOTE_VERSION_INFO](#a18f58c80d213d666ee8309cda8eb0a26)。

<a id="r_a06f6cf60885ac051cdc9b463fc3b7de7"></a>

```c
#define BT_HCI_EVT_CMD_COMPLETE 0x0e
```

相关声明：[BT_HCI_EVT_CMD_COMPLETE](#a06f6cf60885ac051cdc9b463fc3b7de7)。

<a id="r_a2b35e7484351228243bb3564273c5bff"></a>

```c
#define BT_HCI_EVT_CMD_STATUS 0x0f
```

相关声明：[BT_HCI_EVT_CMD_STATUS](#a2b35e7484351228243bb3564273c5bff)。

<a id="r_a54c3bdd2687d142f925183a46ffc5f8b"></a>

```c
#define BT_HCI_EVT_HARDWARE_ERROR 0x10
```

相关声明：[BT_HCI_EVT_HARDWARE_ERROR](#a54c3bdd2687d142f925183a46ffc5f8b)。

<a id="r_a9508e6faf71a345f7ff3d2cec9d85dde"></a>

```c
#define BT_HCI_EVT_ROLE_CHANGE 0x12
```

相关声明：[BT_HCI_EVT_ROLE_CHANGE](#a9508e6faf71a345f7ff3d2cec9d85dde)。

<a id="r_a883433c60959629a013d34cea21ab88f"></a>

```c
#define BT_HCI_EVT_NUM_COMPLETED_PACKETS 0x13
```

相关声明：[BT_HCI_EVT_NUM_COMPLETED_PACKETS](#a883433c60959629a013d34cea21ab88f)。

<a id="r_a1b6049f2e0fde604d1da02cbb66b7948"></a>

```c
#define BT_ACTIVE_MODE 0x00
```

相关声明：[BT_ACTIVE_MODE](#a1b6049f2e0fde604d1da02cbb66b7948)。

<a id="r_ac2ec12929f29264e2831c7ef986d163e"></a>

```c
#define BT_HOLD_MODE 0x01
```

相关声明：[BT_HOLD_MODE](#ac2ec12929f29264e2831c7ef986d163e)。

<a id="r_a52ac9ae0d0d89e5957e4bfd7dca93fe1"></a>

```c
#define BT_SNIFF_MODE 0x02
```

相关声明：[BT_SNIFF_MODE](#a52ac9ae0d0d89e5957e4bfd7dca93fe1)。

<a id="r_a4fa69f355651302f55064c13af7b18a2"></a>

```c
#define BT_HCI_EVT_MODE_CHANGE 0x14
```

相关声明：[BT_HCI_EVT_MODE_CHANGE](#a4fa69f355651302f55064c13af7b18a2)。

<a id="r_a8c16e0bdecf9eae58bbd884fb48b0fc2"></a>

```c
#define BT_HCI_EVT_PIN_CODE_REQ 0x16
```

相关声明：[BT_HCI_EVT_PIN_CODE_REQ](#a8c16e0bdecf9eae58bbd884fb48b0fc2)。

<a id="r_aab60607637f0e1f8e3cbf9f7292ddc57"></a>

```c
#define BT_HCI_EVT_LINK_KEY_REQ 0x17
```

相关声明：[BT_HCI_EVT_LINK_KEY_REQ](#aab60607637f0e1f8e3cbf9f7292ddc57)。

<a id="r_a7283a42b1220dd6d56c22cd9cb424e7c"></a>

```c
#define BT_LK_COMBINATION 0x00
```

相关声明：[BT_LK_COMBINATION](#a7283a42b1220dd6d56c22cd9cb424e7c)。

<a id="r_a12ffe67b9e4ec01bbe400a6a3cc5b859"></a>

```c
#define BT_LK_LOCAL_UNIT 0x01
```

相关声明：[BT_LK_LOCAL_UNIT](#a12ffe67b9e4ec01bbe400a6a3cc5b859)。

<a id="r_aeb53b797c4fc91a38a459ff5f29d35e1"></a>

```c
#define BT_LK_REMOTE_UNIT 0x02
```

相关声明：[BT_LK_REMOTE_UNIT](#aeb53b797c4fc91a38a459ff5f29d35e1)。

<a id="r_a916e6133d2dadb9aaf5fe42d0c0e1b96"></a>

```c
#define BT_LK_DEBUG_COMBINATION 0x03
```

相关声明：[BT_LK_DEBUG_COMBINATION](#a916e6133d2dadb9aaf5fe42d0c0e1b96)。

<a id="r_adfea495d48088eae78491a14730bef31"></a>

```c
#define BT_LK_UNAUTH_COMBINATION_P192 0x04
```

相关声明：[BT_LK_UNAUTH_COMBINATION_P192](#adfea495d48088eae78491a14730bef31)。

<a id="r_a6630ceb874d343f721931f80ee5fa67e"></a>

```c
#define BT_LK_AUTH_COMBINATION_P192 0x05
```

相关声明：[BT_LK_AUTH_COMBINATION_P192](#a6630ceb874d343f721931f80ee5fa67e)。

<a id="r_a5753841a02ba0c2fa627d9e96bad045d"></a>

```c
#define BT_LK_CHANGED_COMBINATION 0x06
```

相关声明：[BT_LK_CHANGED_COMBINATION](#a5753841a02ba0c2fa627d9e96bad045d)。

<a id="r_ada18ab581a323eafe8754009ef27d05e"></a>

```c
#define BT_LK_UNAUTH_COMBINATION_P256 0x07
```

相关声明：[BT_LK_UNAUTH_COMBINATION_P256](#ada18ab581a323eafe8754009ef27d05e)。

<a id="r_aa941cce486c497afa6d03fec326396b9"></a>

```c
#define BT_LK_AUTH_COMBINATION_P256 0x08
```

相关声明：[BT_LK_AUTH_COMBINATION_P256](#aa941cce486c497afa6d03fec326396b9)。

<a id="r_a15578dd8e9d2b16a28ea0b020ac9112b"></a>

```c
#define BT_HCI_EVT_LINK_KEY_NOTIFY 0x18
```

相关声明：[BT_HCI_EVT_LINK_KEY_NOTIFY](#a15578dd8e9d2b16a28ea0b020ac9112b)。

<a id="r_a44233b934e33c65af90d03ad301e6b9d"></a>

```c
#define BT_OVERFLOW_LINK_SYNCH 0x00
```

相关声明：[BT_OVERFLOW_LINK_SYNCH](#a44233b934e33c65af90d03ad301e6b9d)。

<a id="r_a35831810e3a7e2c5446780b14ef7d9c1"></a>

```c
#define BT_OVERFLOW_LINK_ACL 0x01
```

相关声明：[BT_OVERFLOW_LINK_ACL](#a35831810e3a7e2c5446780b14ef7d9c1)。

<a id="r_ad32010743baef10c635d8b08f21c8641"></a>

```c
#define BT_OVERFLOW_LINK_ISO 0x02
```

相关声明：[BT_OVERFLOW_LINK_ISO](#ad32010743baef10c635d8b08f21c8641)。

<a id="r_ae747b016101bc9e9614163288c5c0d15"></a>

```c
#define BT_HCI_EVT_DATA_BUF_OVERFLOW 0x1a
```

相关声明：[BT_HCI_EVT_DATA_BUF_OVERFLOW](#ae747b016101bc9e9614163288c5c0d15)。

<a id="r_a4dc96c114c545ed23fe926d7ec0967a7"></a>

```c
#define BT_HCI_EVT_CONN_PKT_TYPE_CHANGED 0x1d
```

相关声明：[BT_HCI_EVT_CONN_PKT_TYPE_CHANGED](#a4dc96c114c545ed23fe926d7ec0967a7)。

HCI 连接分组类型已改变事件（Connection Packet Type Changed Event）。

<a id="r_a92243c99484922771d5aca8f98945d29"></a>

```c
#define BT_HCI_EVT_INQUIRY_RESULT_WITH_RSSI 0x22
```

相关声明：[BT_HCI_EVT_INQUIRY_RESULT_WITH_RSSI](#a92243c99484922771d5aca8f98945d29)。

<a id="r_a092a782ea069c98475a6617241321122"></a>

```c
#define BT_HCI_EVT_REMOTE_EXT_FEATURES 0x23
```

相关声明：[BT_HCI_EVT_REMOTE_EXT_FEATURES](#a092a782ea069c98475a6617241321122)。

<a id="r_a0decb07f1b4ae20b23cffc616dd442e4"></a>

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED_V2 0x24
```

相关声明：[BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED_V2](#a0decb07f1b4ae20b23cffc616dd442e4)。

<a id="r_a8d067bf751953fd8a7bb5421bdc94970"></a>

```c
#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT_V2 0x25
```

相关声明：[BT_HCI_EVT_LE_PER_ADVERTISING_REPORT_V2](#a8d067bf751953fd8a7bb5421bdc94970)。

<a id="r_a5379a2a0016a2551ac79736924c7ea86"></a>

```c
#define BT_HCI_EVT_LE_PAST_RECEIVED_V2 0x26
```

相关声明：[BT_HCI_EVT_LE_PAST_RECEIVED_V2](#a5379a2a0016a2551ac79736924c7ea86)。

<a id="r_a4395b8b850e9fd3735c2369798f9c226"></a>

```c
#define BT_HCI_EVT_LE_PER_ADV_SUBEVENT_DATA_REQUEST 0x27
```

相关声明：[BT_HCI_EVT_LE_PER_ADV_SUBEVENT_DATA_REQUEST](#a4395b8b850e9fd3735c2369798f9c226)。

<a id="r_a64e0f465068e72e98904fa6cdc33d3de"></a>

```c
#define BT_HCI_EVT_LE_PER_ADV_RESPONSE_REPORT 0x28
```

相关声明：[BT_HCI_EVT_LE_PER_ADV_RESPONSE_REPORT](#a64e0f465068e72e98904fa6cdc33d3de)。

<a id="r_a60ea5e58028aa09c00d20cfff5c942d5"></a>

```c
#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE_V2 0x29
```

相关声明：[BT_HCI_EVT_LE_ENH_CONN_COMPLETE_V2](#a60ea5e58028aa09c00d20cfff5c942d5)。

<a id="r_ab77f3074a2236afc1ed773775d17befe"></a>

```c
#define BT_HCI_EVT_SYNC_CONN_COMPLETE 0x2c
```

相关声明：[BT_HCI_EVT_SYNC_CONN_COMPLETE](#ab77f3074a2236afc1ed773775d17befe)。

<a id="r_a9b5405de1e07fcefba54b286bd1fdfbe"></a>

```c
#define BT_HCI_EVT_EXTENDED_INQUIRY_RESULT 0x2f
```

相关声明：[BT_HCI_EVT_EXTENDED_INQUIRY_RESULT](#a9b5405de1e07fcefba54b286bd1fdfbe)。

<a id="r_aad28cc20cc111ac39e39011932b9d22e"></a>

```c
#define BT_HCI_EVT_ENCRYPT_KEY_REFRESH_COMPLETE 0x30
```

相关声明：[BT_HCI_EVT_ENCRYPT_KEY_REFRESH_COMPLETE](#aad28cc20cc111ac39e39011932b9d22e)。

<a id="r_a4d69a943660da9c1a6ffedb9b653ce3f"></a>

```c
#define BT_HCI_EVT_IO_CAPA_REQ 0x31
```

相关声明：[BT_HCI_EVT_IO_CAPA_REQ](#a4d69a943660da9c1a6ffedb9b653ce3f)。

<a id="r_a0f5cae40268568e25142eed9e3e5e639"></a>

```c
#define BT_HCI_EVT_IO_CAPA_RESP 0x32
```

相关声明：[BT_HCI_EVT_IO_CAPA_RESP](#a0f5cae40268568e25142eed9e3e5e639)。

<a id="r_a78cdb5848d8a12a8cbea17767b3d02aa"></a>

```c
#define BT_HCI_EVT_USER_CONFIRM_REQ 0x33
```

相关声明：[BT_HCI_EVT_USER_CONFIRM_REQ](#a78cdb5848d8a12a8cbea17767b3d02aa)。

<a id="r_a38a1bce81af39bb28d40e149f9309b69"></a>

```c
#define BT_HCI_EVT_USER_PASSKEY_REQ 0x34
```

相关声明：[BT_HCI_EVT_USER_PASSKEY_REQ](#a38a1bce81af39bb28d40e149f9309b69)。

<a id="r_a7d2ba655c6954f90de04cafafccd727f"></a>

```c
#define BT_HCI_EVT_SSP_COMPLETE 0x36
```

相关声明：[BT_HCI_EVT_SSP_COMPLETE](#a7d2ba655c6954f90de04cafafccd727f)。

<a id="r_a724d43899b16fcb89c235898a21c13b9"></a>

```c
#define BT_HCI_EVT_USER_PASSKEY_NOTIFY 0x3b
```

相关声明：[BT_HCI_EVT_USER_PASSKEY_NOTIFY](#a724d43899b16fcb89c235898a21c13b9)。

<a id="r_ac1d7f9270323d7fa459e60b372cf998b"></a>

```c
#define BT_HCI_EVT_LE_META_EVENT 0x3e
```

相关声明：[BT_HCI_EVT_LE_META_EVENT](#ac1d7f9270323d7fa459e60b372cf998b)。

<a id="r_a589975abd5d9532ba16d15ac21c5e81e"></a>

```c
#define BT_HCI_EVT_AUTH_PAYLOAD_TIMEOUT_EXP 0x57
```

相关声明：[BT_HCI_EVT_AUTH_PAYLOAD_TIMEOUT_EXP](#a589975abd5d9532ba16d15ac21c5e81e)。

<a id="r_a150ea8f2095d8510bde3ebd65d521c29"></a>

```c
#define BT_HCI_ROLE_CENTRAL 0x00
```

相关声明：[BT_HCI_ROLE_CENTRAL](#a150ea8f2095d8510bde3ebd65d521c29)。

<a id="r_a9ca37afd4638ef94cdd55302bd4c99b3"></a>

```c
#define BT_HCI_ROLE_PERIPHERAL 0x01
```

相关声明：[BT_HCI_ROLE_PERIPHERAL](#a9ca37afd4638ef94cdd55302bd4c99b3)。

<a id="r_a2c3c4f81903d1860f21880c7c3cfbaa7"></a>

```c
#define BT_HCI_EVT_LE_CONN_COMPLETE 0x01
```

相关声明：[BT_HCI_EVT_LE_CONN_COMPLETE](#a2c3c4f81903d1860f21880c7c3cfbaa7)。

<a id="r_a56f7acd075e03694d966d949f637946c"></a>

```c
#define BT_HCI_LE_RSSI_NOT_AVAILABLE 0x7F
```

相关声明：[BT_HCI_LE_RSSI_NOT_AVAILABLE](#a56f7acd075e03694d966d949f637946c)。

<a id="r_a1a93b78bdbb29982d989aea5eae5ec19"></a>

```c
#define BT_HCI_EVT_LE_ADVERTISING_REPORT 0x02
```

相关声明：[BT_HCI_EVT_LE_ADVERTISING_REPORT](#a1a93b78bdbb29982d989aea5eae5ec19)。

<a id="r_adcf6bcefe1d8a34f65597730910bab69"></a>

```c
#define BT_HCI_LE_INTERVAL_MIN 0x0006
```

相关声明：[BT_HCI_LE_INTERVAL_MIN](#adcf6bcefe1d8a34f65597730910bab69)。

所有限制均依据《蓝牙核心规范》（BT Core Spec）v5.4，第 4 卷 E 部分。

<a id="r_a23ce5829beb61d9db40fedfce35c368e"></a>

```c
#define BT_HCI_LE_INTERVAL_MAX 0x0c80
```

相关声明：[BT_HCI_LE_INTERVAL_MAX](#a23ce5829beb61d9db40fedfce35c368e)。

<a id="r_a95274b56d9d973f32d2098b433ed1ff7"></a>

```c
#define BT_HCI_LE_PERIPHERAL_LATENCY_MIN (0x0000U)
```

相关声明：[BT_HCI_LE_PERIPHERAL_LATENCY_MIN](#a95274b56d9d973f32d2098b433ed1ff7)。

<a id="r_a9af7ce6ecbd978df6193c4e9c2d8b002"></a>

```c
#define BT_HCI_LE_PERIPHERAL_LATENCY_MAX 0x01f3
```

相关声明：[BT_HCI_LE_PERIPHERAL_LATENCY_MAX](#a9af7ce6ecbd978df6193c4e9c2d8b002)。

<a id="r_a07b822f1a826f4824ec070c4b6822fe2"></a>

```c
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MIN 0x000a
```

相关声明：[BT_HCI_LE_SUPERVISION_TIMEOUT_MIN](#a07b822f1a826f4824ec070c4b6822fe2)。

最小低功耗蓝牙监督超时（LE Supervision Timeout）：10 ms。

<a id="r_a1357a2a7227e86df1c132207ba44d6db"></a>

```c
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MAX 0x0c80
```

相关声明：[BT_HCI_LE_SUPERVISION_TIMEOUT_MAX](#a1357a2a7227e86df1c132207ba44d6db)。

最大低功耗蓝牙监督超时（LE Supervision Timeout）：3200 ms。

<a id="r_a03dc93eec388a17c286d50395c683fcb"></a>

```c
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MIN BT_HCI_LE_SUPERVISION_TIMEOUT_MIN __DEPRECATED_MACRO
```

相关声明：[BT_HCI_LE_SUPERVISON_TIMEOUT_MIN](#a03dc93eec388a17c286d50395c683fcb)、[BT_HCI_LE_SUPERVISION_TIMEOUT_MIN](#a07b822f1a826f4824ec070c4b6822fe2)。

<a id="r_a2564ee96b802cb887f67e3cc38f8f400"></a>

```c
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MAX BT_HCI_LE_SUPERVISION_TIMEOUT_MAX __DEPRECATED_MACRO
```

相关声明：[BT_HCI_LE_SUPERVISON_TIMEOUT_MAX](#a2564ee96b802cb887f67e3cc38f8f400)、[BT_HCI_LE_SUPERVISION_TIMEOUT_MAX](#a1357a2a7227e86df1c132207ba44d6db)。

<a id="r_aba0e61062d66e72b84c55662d00e03af"></a>

```c
#define BT_HCI_LE_INTERVAL_UNIT_US (1250U)
```

相关声明：[BT_HCI_LE_INTERVAL_UNIT_US](#aba0e61062d66e72b84c55662d00e03af)。

<a id="r_aeef912e71549d4b5a0d8b293074a909c"></a>

```c
#define BT_HCI_EVT_LE_CONN_UPDATE_COMPLETE 0x03
```

相关声明：[BT_HCI_EVT_LE_CONN_UPDATE_COMPLETE](#aeef912e71549d4b5a0d8b293074a909c)。

<a id="r_a8b1653caabce8474fba132343aa62f56"></a>

```c
#define BT_HCI_EVT_LE_REMOTE_FEAT_COMPLETE 0x04
```

相关声明：[BT_HCI_EVT_LE_REMOTE_FEAT_COMPLETE](#a8b1653caabce8474fba132343aa62f56)。

<a id="r_a9efb73da285829cde0e4c1ac28a48f1a"></a>

```c
#define BT_HCI_EVT_LE_LTK_REQUEST 0x05
```

相关声明：[BT_HCI_EVT_LE_LTK_REQUEST](#a9efb73da285829cde0e4c1ac28a48f1a)。

<a id="r_a77072c10df87395e7e649307b975fb69"></a>

```c
#define BT_HCI_EVT_LE_CONN_PARAM_REQ 0x06
```

相关声明：[BT_HCI_EVT_LE_CONN_PARAM_REQ](#a77072c10df87395e7e649307b975fb69)。

<a id="r_a064cf9e32616c6f94041d138a5bf4819"></a>

```c
#define BT_HCI_EVT_LE_DATA_LEN_CHANGE 0x07
```

相关声明：[BT_HCI_EVT_LE_DATA_LEN_CHANGE](#a064cf9e32616c6f94041d138a5bf4819)。

<a id="r_abe39909eb984dd6edd1220f9c6744546"></a>

```c
#define BT_HCI_EVT_LE_P256_PUBLIC_KEY_COMPLETE 0x08
```

相关声明：[BT_HCI_EVT_LE_P256_PUBLIC_KEY_COMPLETE](#abe39909eb984dd6edd1220f9c6744546)。

<a id="r_a8ab77f497135e365fb9e895dc2d4d453"></a>

```c
#define BT_HCI_EVT_LE_GENERATE_DHKEY_COMPLETE 0x09
```

相关声明：[BT_HCI_EVT_LE_GENERATE_DHKEY_COMPLETE](#a8ab77f497135e365fb9e895dc2d4d453)。

<a id="r_a292de9ec009a80e23308ead618656b4f"></a>

```c
#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE 0x0a
```

相关声明：[BT_HCI_EVT_LE_ENH_CONN_COMPLETE](#a292de9ec009a80e23308ead618656b4f)。

<a id="r_a417144400fd8d7f5c05e050950c75dab"></a>

```c
#define BT_HCI_EVT_LE_DIRECT_ADV_REPORT 0x0b
```

相关声明：[BT_HCI_EVT_LE_DIRECT_ADV_REPORT](#a417144400fd8d7f5c05e050950c75dab)。

<a id="r_a44f18d799280d47ec09376e7cffd4c40"></a>

```c
#define BT_HCI_EVT_LE_PHY_UPDATE_COMPLETE 0x0c
```

相关声明：[BT_HCI_EVT_LE_PHY_UPDATE_COMPLETE](#a44f18d799280d47ec09376e7cffd4c40)。

<a id="r_ad63fc0c42f0253dfe06b81324a05f505"></a>

```c
#define BT_HCI_EVT_LE_EXT_ADVERTISING_REPORT 0x0d
```

相关声明：[BT_HCI_EVT_LE_EXT_ADVERTISING_REPORT](#ad63fc0c42f0253dfe06b81324a05f505)。

<a id="r_ae448216e385d4e1175b92e112c941140"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_CONN BIT(0)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_CONN](#ae448216e385d4e1175b92e112c941140)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a54673fbd23e05fec88e1f6bca6aa70e9"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN BIT(1)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_SCAN](#a54673fbd23e05fec88e1f6bca6aa70e9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1b5738583447011ee63350787236b3b8"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DIRECT BIT(2)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DIRECT](#a1b5738583447011ee63350787236b3b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a485843f24c09934b1f15d5274b4a56d5"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN_RSP BIT(3)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_SCAN_RSP](#a485843f24c09934b1f15d5274b4a56d5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0879fbea8bf3acbe56e25f3693c81ad6"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_LEGACY BIT(4)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_LEGACY](#a0879fbea8bf3acbe56e25f3693c81ad6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a9557bf3ea41a526fb9d628d2fd3d5bea"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS(ev_type)
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS](#a9557bf3ea41a526fb9d628d2fd3d5bea)。

<a id="r_a85720f3d88c7fa5da9dc9cdffb94ec87"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_COMPLETE 0
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_COMPLETE](#a85720f3d88c7fa5da9dc9cdffb94ec87)。

<a id="r_ab7842a3081c9bf5288275b57337955f2"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_PARTIAL 1
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_PARTIAL](#ab7842a3081c9bf5288275b57337955f2)。

<a id="r_abf119f5606440c075e61abcbfaa683c6"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_INCOMPLETE 2
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_INCOMPLETE](#abf119f5606440c075e61abcbfaa683c6)。

<a id="r_ad9bcda2a43eed7e73112f2ef84cc6183"></a>

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_RX_FAILED 0xFF
```

相关声明：[BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_RX_FAILED](#ad9bcda2a43eed7e73112f2ef84cc6183)。

<a id="r_a4e3752dfde6a1f6ce6c7561b6c19657c"></a>

```c
#define BT_HCI_LE_ADV_EVT_PHY_1M 0x01
```

相关声明：[BT_HCI_LE_ADV_EVT_PHY_1M](#a4e3752dfde6a1f6ce6c7561b6c19657c)。

<a id="r_a0eae639d3066358da815743aa7ba2933"></a>

```c
#define BT_HCI_LE_ADV_EVT_PHY_2M 0x02
```

相关声明：[BT_HCI_LE_ADV_EVT_PHY_2M](#a0eae639d3066358da815743aa7ba2933)。

<a id="r_a51fd268794a726f7d9fa2fb4ce937507"></a>

```c
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S8 0x03
```

相关声明：[BT_HCI_LE_ADV_EVT_PHY_CODED_S8](#a51fd268794a726f7d9fa2fb4ce937507)。

<a id="r_a865ad7eefd0051e7965bd5e391bf852c"></a>

```c
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S2 0x04
```

相关声明：[BT_HCI_LE_ADV_EVT_PHY_CODED_S2](#a865ad7eefd0051e7965bd5e391bf852c)。

<a id="r_a5fcf4bb36d4ebe25706c1b71431eb12f"></a>

```c
#define BT_HCI_LE_EXT_ADV_REPORT_MAX_NUM_REPORTS 0x0a
```

相关声明：[BT_HCI_LE_EXT_ADV_REPORT_MAX_NUM_REPORTS](#a5fcf4bb36d4ebe25706c1b71431eb12f)。

低功耗蓝牙扩展广播报告（LE Extended Advertising Report）中的最大报告数量。

<a id="r_a8c721c9e5df496900f661755aff7cbd6"></a>

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED 0x0e
```

相关声明：[BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED](#a8c721c9e5df496900f661755aff7cbd6)。

<a id="r_a31fc096530a89e63d4967d7ddd85b753"></a>

```c
#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT 0x0f
```

相关声明：[BT_HCI_EVT_LE_PER_ADVERTISING_REPORT](#a31fc096530a89e63d4967d7ddd85b753)。

<a id="r_ab303042eabbeb133e202bdcfbd38666c"></a>

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_LOST 0x10
```

相关声明：[BT_HCI_EVT_LE_PER_ADV_SYNC_LOST](#ab303042eabbeb133e202bdcfbd38666c)。

<a id="r_a7234c851946c6025aa850c9bf28faab0"></a>

```c
#define BT_HCI_EVT_LE_SCAN_TIMEOUT 0x11
```

相关声明：[BT_HCI_EVT_LE_SCAN_TIMEOUT](#a7234c851946c6025aa850c9bf28faab0)。

<a id="r_a398afcbdb732fe76ec01db1393721ab2"></a>

```c
#define BT_HCI_EVT_LE_ADV_SET_TERMINATED 0x12
```

相关声明：[BT_HCI_EVT_LE_ADV_SET_TERMINATED](#a398afcbdb732fe76ec01db1393721ab2)。

<a id="r_a0ebf19a602a02c00793b3de64392e514"></a>

```c
#define BT_HCI_EVT_LE_SCAN_REQ_RECEIVED 0x13
```

相关声明：[BT_HCI_EVT_LE_SCAN_REQ_RECEIVED](#a0ebf19a602a02c00793b3de64392e514)。

<a id="r_ac8dcea08127aa5ce2a870d64fcc843f1"></a>

```c
#define BT_HCI_LE_CHAN_SEL_ALGO_1 0x00
```

相关声明：[BT_HCI_LE_CHAN_SEL_ALGO_1](#ac8dcea08127aa5ce2a870d64fcc843f1)。

<a id="r_a7a4b52643c764233427314732896d353"></a>

```c
#define BT_HCI_LE_CHAN_SEL_ALGO_2 0x01
```

相关声明：[BT_HCI_LE_CHAN_SEL_ALGO_2](#a7a4b52643c764233427314732896d353)。

<a id="r_a4f012a8357e5bb17b5dd04128bd39911"></a>

```c
#define BT_HCI_EVT_LE_CHAN_SEL_ALGO 0x14
```

相关声明：[BT_HCI_EVT_LE_CHAN_SEL_ALGO](#a4f012a8357e5bb17b5dd04128bd39911)。

<a id="r_ac1ce16d42df9eb71860e51a843dbc943"></a>

```c
#define BT_HCI_LE_CTE_CRC_OK 0x0
```

相关声明：[BT_HCI_LE_CTE_CRC_OK](#ac1ce16d42df9eb71860e51a843dbc943)。

<a id="r_a3f787f516c3cc233fc700c08552a4034"></a>

```c
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_TIME 0x1
```

相关声明：[BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_TIME](#a3f787f516c3cc233fc700c08552a4034)。

<a id="r_a478bc1be161e0b1eb05667bc8b6c9ae5"></a>

```c
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_OTHER 0x2
```

相关声明：[BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_OTHER](#a478bc1be161e0b1eb05667bc8b6c9ae5)。

<a id="r_a3bc1e15287e6173d45b7d1e981d6e90e"></a>

```c
#define BT_HCI_LE_CTE_INSUFFICIENT_RESOURCES 0xFF
```

相关声明：[BT_HCI_LE_CTE_INSUFFICIENT_RESOURCES](#a3bc1e15287e6173d45b7d1e981d6e90e)。

<a id="r_a87364c12ecac6b05681469c9450f887e"></a>

```c
#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MIN 0x9
```

相关声明：[B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MIN](#a87364c12ecac6b05681469c9450f887e)。

<a id="r_a9693358ac3b7d9da498ca557fa0d1410"></a>

```c
#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MAX 0x52
```

相关声明：[B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MAX](#a9693358ac3b7d9da498ca557fa0d1410)。

<a id="r_a40156c4680916b289b00b1546e0d5bb0"></a>

```c
#define BT_HCI_LE_CTE_REPORT_NO_VALID_SAMPLE 0x80
```

相关声明：[BT_HCI_LE_CTE_REPORT_NO_VALID_SAMPLE](#a40156c4680916b289b00b1546e0d5bb0)。

<a id="r_a04c4a4567eaad7c592f2181e47768522"></a>

```c
#define BT_HCI_EVT_LE_CONNECTIONLESS_IQ_REPORT 0x15
```

相关声明：[BT_HCI_EVT_LE_CONNECTIONLESS_IQ_REPORT](#a04c4a4567eaad7c592f2181e47768522)。

<a id="r_ace41ae5ec2a8f036aabf83ac94937a8b"></a>

```c
#define BT_HCI_EVT_LE_CONNECTION_IQ_REPORT 0x16
```

相关声明：[BT_HCI_EVT_LE_CONNECTION_IQ_REPORT](#ace41ae5ec2a8f036aabf83ac94937a8b)。

<a id="r_a5e0814f9ca6e7fbc78b0778634ff075d"></a>

```c
#define BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE 0x0
```

相关声明：[BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE](#a5e0814f9ca6e7fbc78b0778634ff075d)。

<a id="r_aacaa203f0c8e23c6ca551df0375410e8"></a>

```c
#define BT_HCI_EVT_LE_CTE_REQUEST_FAILED 0x17
```

相关声明：[BT_HCI_EVT_LE_CTE_REQUEST_FAILED](#aacaa203f0c8e23c6ca551df0375410e8)。

<a id="r_ad61867c0bef6797f7a3b5418c5a4ed5f"></a>

```c
#define BT_HCI_EVT_LE_PAST_RECEIVED 0x18
```

相关声明：[BT_HCI_EVT_LE_PAST_RECEIVED](#ad61867c0bef6797f7a3b5418c5a4ed5f)。

<a id="r_a875de5e9c3675c6bac301dab52733ae1"></a>

```c
#define BT_HCI_LE_CIG_SYNC_DELAY_MIN 0x0000F2U
```

相关声明：[BT_HCI_LE_CIG_SYNC_DELAY_MIN](#a875de5e9c3675c6bac301dab52733ae1)。

7.7.65.25 LE CIS Established 事件所定义的连接等时组（CIG）最小同步延迟（Sync Delay）。

<a id="r_a811e0d38fa730e175efac792e5702ebd"></a>

```c
#define BT_HCI_LE_CIG_SYNC_DELAY_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_CIG_SYNC_DELAY_MAX](#a811e0d38fa730e175efac792e5702ebd)。

7.7.65.25 LE CIS Established 事件所定义的连接等时组（CIG）最大同步延迟（Sync Delay）。

<a id="r_af678f3fb040ad4b115fff082832d28e0"></a>

```c
#define BT_HCI_LE_CIS_SYNC_DELAY_MIN 0x0000F2U
```

相关声明：[BT_HCI_LE_CIS_SYNC_DELAY_MIN](#af678f3fb040ad4b115fff082832d28e0)。

7.7.65.25 LE CIS Established 事件所定义的连接等时流（CIS）最小同步延迟（Sync Delay）。

<a id="r_acb49877cf9c9a0563ac20e7b5541f972"></a>

```c
#define BT_HCI_LE_CIS_SYNC_DELAY_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_CIS_SYNC_DELAY_MAX](#acb49877cf9c9a0563ac20e7b5541f972)。

7.7.65.25 LE CIS Established 事件所定义的连接等时流（CIS）最大同步延迟（Sync Delay）。

<a id="r_a85732b5233b34298a3f979f8e9009907"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MIN 0x0000F2U
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MIN](#a85732b5233b34298a3f979f8e9009907)。

7.7.65.25 LE CIS Established 事件所定义的中央设备到外设（Central to Peripheral）的最小传输延迟（Transport Latency）。

<a id="r_ad6729367096ec3d288b187b5746f17d7"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MAX](#ad6729367096ec3d288b187b5746f17d7)。

7.7.65.25 LE CIS Established 事件所定义的中央设备到外设（Central to Peripheral）的最大传输延迟（Transport Latency）。

<a id="r_a9f10f08358a5caa80b71b7351dbf09bc"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MIN 0x0000F2U
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MIN](#a9f10f08358a5caa80b71b7351dbf09bc)。

7.7.65.25 LE CIS Established 事件所定义的外设到中央设备（Peripheral to Central）的最小传输延迟（Transport Latency）。

<a id="r_a0bce30a784239e713fb38125cd16e2c1"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MAX](#a0bce30a784239e713fb38125cd16e2c1)。

7.7.65.25 LE CIS Established 事件所定义的外设到中央设备（Peripheral to Central）的最大传输延迟（Transport Latency）。

<a id="r_a263d26617702ab43fa8b6717007e1df8"></a>

```c
#define BT_HCI_EVT_LE_CIS_ESTABLISHED 0x19
```

相关声明：[BT_HCI_EVT_LE_CIS_ESTABLISHED](#a263d26617702ab43fa8b6717007e1df8)。

<a id="r_aaa4af1dcdb163a57b0473b43e8107fd7"></a>

```c
#define BT_HCI_EVT_LE_CIS_REQ 0x1a
```

相关声明：[BT_HCI_EVT_LE_CIS_REQ](#aaa4af1dcdb163a57b0473b43e8107fd7)。

<a id="r_ab145283f399f65b5d576d83fe79d173a"></a>

```c
#define BT_HCI_LE_BIG_HANDLE_MIN 0x00U
```

相关声明：[BT_HCI_LE_BIG_HANDLE_MIN](#ab145283f399f65b5d576d83fe79d173a)。

<a id="r_afd311a47bbe6cdfac035c97b0b19b736"></a>

```c
#define BT_HCI_LE_BIG_HANDLE_MAX 0xEFU
```

相关声明：[BT_HCI_LE_BIG_HANDLE_MAX](#afd311a47bbe6cdfac035c97b0b19b736)。

<a id="r_ad6106a99804460b7aa68f52d5e322db1"></a>

```c
#define BT_HCI_LE_BIG_SYNC_DELAY_MIN 0x000030U
```

相关声明：[BT_HCI_LE_BIG_SYNC_DELAY_MIN](#ad6106a99804460b7aa68f52d5e322db1)。

<a id="r_a70d6f103242dcd48f2c118ac82f9d358"></a>

```c
#define BT_HCI_LE_BIG_SYNC_DELAY_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_BIG_SYNC_DELAY_MAX](#a70d6f103242dcd48f2c118ac82f9d358)。

<a id="r_ae24bd2c6c05c7d300d110a522c59fcbc"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MIN 0x000030U
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_BIG_MIN](#ae24bd2c6c05c7d300d110a522c59fcbc)。

<a id="r_ace025b0516289eb493f54ba92292dd22"></a>

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MAX 0x7FFFFFU
```

相关声明：[BT_HCI_LE_TRANSPORT_LATENCY_BIG_MAX](#ace025b0516289eb493f54ba92292dd22)。

<a id="r_aade42399ac596746100849328c551259"></a>

```c
#define BT_HCI_EVT_LE_BIG_COMPLETE 0x1b
```

相关声明：[BT_HCI_EVT_LE_BIG_COMPLETE](#aade42399ac596746100849328c551259)。

<a id="r_ac0a1310793a73afda4c2179749df9985"></a>

```c
#define BT_HCI_EVT_LE_BIG_TERMINATE 0x1c
```

相关声明：[BT_HCI_EVT_LE_BIG_TERMINATE](#ac0a1310793a73afda4c2179749df9985)。

<a id="r_a8d021615f0b1b2077bbec1f1482b85ef"></a>

```c
#define BT_HCI_EVT_LE_BIG_SYNC_ESTABLISHED 0x1d
```

相关声明：[BT_HCI_EVT_LE_BIG_SYNC_ESTABLISHED](#a8d021615f0b1b2077bbec1f1482b85ef)。

<a id="r_a9c79430501848b9e75a21020920a8ca8"></a>

```c
#define BT_HCI_EVT_LE_BIG_SYNC_LOST 0x1e
```

相关声明：[BT_HCI_EVT_LE_BIG_SYNC_LOST](#a9c79430501848b9e75a21020920a8ca8)。

<a id="r_aeb33301a950a9520d7ff706dddb07951"></a>

```c
#define BT_HCI_EVT_LE_REQ_PEER_SCA_COMPLETE 0x1f
```

相关声明：[BT_HCI_EVT_LE_REQ_PEER_SCA_COMPLETE](#aeb33301a950a9520d7ff706dddb07951)。

<a id="r_aff1538e314a97aa4910d4f7066dc4d55"></a>

```c
#define BT_HCI_LE_ZONE_ENTERED_LOW 0x0
```

相关声明：[BT_HCI_LE_ZONE_ENTERED_LOW](#aff1538e314a97aa4910d4f7066dc4d55)。

<a id="r_ab88f3d713f6862c08b73752436ca8b1b"></a>

```c
#define BT_HCI_LE_ZONE_ENTERED_MIDDLE 0x1
```

相关声明：[BT_HCI_LE_ZONE_ENTERED_MIDDLE](#ab88f3d713f6862c08b73752436ca8b1b)。

<a id="r_af7cc15be8165315ee0358ebb517b5e33"></a>

```c
#define BT_HCI_LE_ZONE_ENTERED_HIGH 0x2
```

相关声明：[BT_HCI_LE_ZONE_ENTERED_HIGH](#af7cc15be8165315ee0358ebb517b5e33)。

<a id="r_a0408b7ecb697bd573b2ea7d2c3c93b92"></a>

```c
#define BT_HCI_LE_PATH_LOSS_UNAVAILABLE 0xFF
```

相关声明：[BT_HCI_LE_PATH_LOSS_UNAVAILABLE](#a0408b7ecb697bd573b2ea7d2c3c93b92)。

<a id="r_a3e646ec9a2e0baca5126e58368c97995"></a>

```c
#define BT_HCI_EVT_LE_PATH_LOSS_THRESHOLD 0x20
```

相关声明：[BT_HCI_EVT_LE_PATH_LOSS_THRESHOLD](#a3e646ec9a2e0baca5126e58368c97995)。

<a id="r_a443a5a524ec41bf2ea86eab74dd022dc"></a>

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_LOCAL_CHANGED 0x00
```

相关声明：[BT_HCI_LE_TX_POWER_REPORT_REASON_LOCAL_CHANGED](#a443a5a524ec41bf2ea86eab74dd022dc)。

发射功率报告（Transmit Power Reporting）的原因。

<a id="r_a1fbc1b017b13987a017af7cd90bdf708"></a>

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_REMOTE_CHANGED 0x01
```

相关声明：[BT_HCI_LE_TX_POWER_REPORT_REASON_REMOTE_CHANGED](#a1fbc1b017b13987a017af7cd90bdf708)。

<a id="r_a268761b9eae9c84f74394a6098f15ee8"></a>

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_READ_REMOTE_COMPLETED 0x02
```

相关声明：[BT_HCI_LE_TX_POWER_REPORT_REASON_READ_REMOTE_COMPLETED](#a268761b9eae9c84f74394a6098f15ee8)。

<a id="r_a835280c0bf13ddebf451fef5f08c22d0"></a>

```c
#define BT_HCI_EVT_LE_TRANSMIT_POWER_REPORT 0x21
```

相关声明：[BT_HCI_EVT_LE_TRANSMIT_POWER_REPORT](#a835280c0bf13ddebf451fef5f08c22d0)。

<a id="r_a651e36b5529cb7f289721573434154cd"></a>

```c
#define BT_HCI_EVT_LE_BIGINFO_ADV_REPORT 0x22
```

相关声明：[BT_HCI_EVT_LE_BIGINFO_ADV_REPORT](#a651e36b5529cb7f289721573434154cd)。

<a id="r_a135059b92eba0676689abc78a2f560d3"></a>

```c
#define BT_HCI_LE_SUBRATE_FACTOR_MIN 0x0001
```

相关声明：[BT_HCI_LE_SUBRATE_FACTOR_MIN](#a135059b92eba0676689abc78a2f560d3)。

所有限制均依据《蓝牙核心规范》（BT Core Spec）v5.4，第 4 卷 E 部分。

<a id="r_a33ce951c9eddfcc5556b0168c14b9769"></a>

```c
#define BT_HCI_LE_SUBRATE_FACTOR_MAX 0x01f4
```

相关声明：[BT_HCI_LE_SUBRATE_FACTOR_MAX](#a33ce951c9eddfcc5556b0168c14b9769)。

<a id="r_a6ac68f277aff54739238ffdafb640f85"></a>

```c
#define BT_HCI_LE_CONTINUATION_NUM_MIN (0x0000U)
```

相关声明：[BT_HCI_LE_CONTINUATION_NUM_MIN](#a6ac68f277aff54739238ffdafb640f85)。

<a id="r_aa2b9a667e0b80a4cf4d8cef9cb022ad4"></a>

```c
#define BT_HCI_LE_CONTINUATION_NUM_MAX 0x01f3
```

相关声明：[BT_HCI_LE_CONTINUATION_NUM_MAX](#aa2b9a667e0b80a4cf4d8cef9cb022ad4)。

<a id="r_a2098d628b6ad185cb29106ef69c3627d"></a>

```c
#define BT_HCI_EVT_LE_SUBRATE_CHANGE 0x23
```

相关声明：[BT_HCI_EVT_LE_SUBRATE_CHANGE](#a2098d628b6ad185cb29106ef69c3627d)。

<a id="r_ae5a1301a0fea0ab6c205dab22e39c6c9"></a>

```c
#define BT_HCI_EVT_LE_CIS_ESTABLISHED_V2 0x2a
```

相关声明：[BT_HCI_EVT_LE_CIS_ESTABLISHED_V2](#ae5a1301a0fea0ab6c205dab22e39c6c9)。

<a id="r_af442282c712682dc805d139f7c31c62f"></a>

```c
#define BT_HCI_EVT_LE_READ_ALL_REMOTE_FEAT_COMPLETE 0x2b
```

相关声明：[BT_HCI_EVT_LE_READ_ALL_REMOTE_FEAT_COMPLETE](#af442282c712682dc805d139f7c31c62f)。

<a id="r_a399c04a940168b9767f3126268dd684e"></a>

```c
#define BT_HCI_LE_FEATURE_PAGE_MAX 10
```

相关声明：[BT_HCI_LE_FEATURE_PAGE_MAX](#a399c04a940168b9767f3126268dd684e)。

<a id="r_ad0cf0a98dff26ba6aed21fa79bcd43f1"></a>

```c
#define BT_HCI_LE_BYTES_PER_FEATURE_PAGE 24
```

相关声明：[BT_HCI_LE_BYTES_PER_FEATURE_PAGE](#ad0cf0a98dff26ba6aed21fa79bcd43f1)。

<a id="r_a81b4b9ce53511c62889790a79b0f6a34"></a>

```c
#define BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE 8
```

相关声明：[BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE](#a81b4b9ce53511c62889790a79b0f6a34)。

<a id="r_af457a20ddc90001f8a523a0e3df6a4bd"></a>

```c
#define BT_HCI_LE_CS_INITIATOR_ROLE_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_INITIATOR_ROLE_MASK](#af457a20ddc90001f8a523a0e3df6a4bd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4c42a75a04962264257c690ba80f6126"></a>

```c
#define BT_HCI_LE_CS_REFLECTOR_ROLE_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_REFLECTOR_ROLE_MASK](#a4c42a75a04962264257c690ba80f6126)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a62ab6fbe9acb92c4023f35ae8bb7b14b"></a>

```c
#define BT_HCI_LE_CS_MODES_SUPPORTED_MODE_3_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_MODES_SUPPORTED_MODE_3_MASK](#a62ab6fbe9acb92c4023f35ae8bb7b14b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab7843d7e6463e96bce693b82c3f8cc7d"></a>

```c
#define BT_HCI_LE_CS_RTT_AA_ONLY_N_10NS_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_RTT_AA_ONLY_N_10NS_MASK](#ab7843d7e6463e96bce693b82c3f8cc7d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad701c1822a44a639bf5a576bf291544f"></a>

```c
#define BT_HCI_LE_CS_RTT_SOUNDING_N_10NS_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_RTT_SOUNDING_N_10NS_MASK](#ad701c1822a44a639bf5a576bf291544f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2135776cd2413e80b3ad653405f0ec67"></a>

```c
#define BT_HCI_LE_CS_RTT_RANDOM_PAYLOAD_N_10NS_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_RTT_RANDOM_PAYLOAD_N_10NS_MASK](#a2135776cd2413e80b3ad653405f0ec67)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a903505932b23ae60c59fc4f439f8f3ce"></a>

```c
#define BT_HCI_LE_CS_NADM_SOUNDING_CAPABILITY_PHASE_BASED_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_NADM_SOUNDING_CAPABILITY_PHASE_BASED_MASK](#a903505932b23ae60c59fc4f439f8f3ce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6b64cb407c353d7a143b7483cf16507f"></a>

```c
#define BT_HCI_LE_CS_NADM_RANDOM_CAPABILITY_PHASE_BASED_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_NADM_RANDOM_CAPABILITY_PHASE_BASED_MASK](#a6b64cb407c353d7a143b7483cf16507f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad8742ec8b365df1850b6e5f56c39e655"></a>

```c
#define BT_HCI_LE_CS_SYNC_PHYS_2M_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_SYNC_PHYS_2M_MASK](#ad8742ec8b365df1850b6e5f56c39e655)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aeba1a6050a1ff6ad3864132015063026"></a>

```c
#define BT_HCI_LE_CS_SYNC_PHYS_2M_2BT_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_SYNC_PHYS_2M_2BT_MASK](#aeba1a6050a1ff6ad3864132015063026)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a2241cba5ca0dbeb1ea19797654c97397"></a>

```c
#define BT_HCI_LE_CS_SUBFEATURE_NO_TX_FAE_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_SUBFEATURE_NO_TX_FAE_MASK](#a2241cba5ca0dbeb1ea19797654c97397)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5a7e8927e6086b70177cc04915d16ff8"></a>

```c
#define BT_HCI_LE_CS_SUBFEATURE_CHSEL_ALG_3C_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_SUBFEATURE_CHSEL_ALG_3C_MASK](#a5a7e8927e6086b70177cc04915d16ff8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4bcdc621f0292fd182f47762a2cf16bb"></a>

```c
#define BT_HCI_LE_CS_SUBFEATURE_PBR_FROM_RTT_SOUNDING_SEQ_MASK BIT(3)
```

相关声明：[BT_HCI_LE_CS_SUBFEATURE_PBR_FROM_RTT_SOUNDING_SEQ_MASK](#a4bcdc621f0292fd182f47762a2cf16bb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab14fe72c7edfc6ccf24fd9347240a395"></a>

```c
#define BT_HCI_LE_CS_SUBFEATURE_CS_IPT_REFLECTOR_MASK BIT(4)
```

相关声明：[BT_HCI_LE_CS_SUBFEATURE_CS_IPT_REFLECTOR_MASK](#ab14fe72c7edfc6ccf24fd9347240a395)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

子功能：反射端（Reflector）中的带 IPT 的信道探测（CS with IPT）。

<a id="r_a85f667356dd1e1d9de288776ec13e721"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_10US_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_10US_MASK](#a85f667356dd1e1d9de288776ec13e721)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a331eff3b3e89a073b30c9d334014b2da"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_20US_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_20US_MASK](#a331eff3b3e89a073b30c9d334014b2da)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a62112179c80be4546b29bc39f632f619"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_30US_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_30US_MASK](#a62112179c80be4546b29bc39f632f619)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a57232d7cbd988c6d6d01d2462e90a7f5"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_40US_MASK BIT(3)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_40US_MASK](#a57232d7cbd988c6d6d01d2462e90a7f5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4aa0365eb6bc4f54bbbd3ebc2b717c41"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_50US_MASK BIT(4)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_50US_MASK](#a4aa0365eb6bc4f54bbbd3ebc2b717c41)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a647ea407f97ea754f3f729ac8a9bbb02"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_60US_MASK BIT(5)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_60US_MASK](#a647ea407f97ea754f3f729ac8a9bbb02)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8bd6f366622ed48cea49fc67692349ce"></a>

```c
#define BT_HCI_LE_CS_T_IP1_TIME_80US_MASK BIT(6)
```

相关声明：[BT_HCI_LE_CS_T_IP1_TIME_80US_MASK](#a8bd6f366622ed48cea49fc67692349ce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a46420b559fcc0e584bc604790ae066ae"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_10US_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_10US_MASK](#a46420b559fcc0e584bc604790ae066ae)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5d279467b3b0b239748b23be57fee63b"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_20US_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_20US_MASK](#a5d279467b3b0b239748b23be57fee63b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a95d5e9901c50e579600db0ef160425eb"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_30US_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_30US_MASK](#a95d5e9901c50e579600db0ef160425eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a66b0bca7c0b19f43b6871cdf05e57543"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_40US_MASK BIT(3)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_40US_MASK](#a66b0bca7c0b19f43b6871cdf05e57543)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a875fa244820e7aea6f1d6674e3d7d72a"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_50US_MASK BIT(4)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_50US_MASK](#a875fa244820e7aea6f1d6674e3d7d72a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab73d093bcb50ebdd5630e85677af6223"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_60US_MASK BIT(5)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_60US_MASK](#ab73d093bcb50ebdd5630e85677af6223)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6d6e20505ba9b86bc254bc3419e5bc04"></a>

```c
#define BT_HCI_LE_CS_T_IP2_TIME_80US_MASK BIT(6)
```

相关声明：[BT_HCI_LE_CS_T_IP2_TIME_80US_MASK](#a6d6e20505ba9b86bc254bc3419e5bc04)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac1138ac8f702b4b79bc03c9a7d60207b"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_15US_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_15US_MASK](#ac1138ac8f702b4b79bc03c9a7d60207b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7023db07ddc8f9e9fbfc59283511bafb"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_20US_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_20US_MASK](#a7023db07ddc8f9e9fbfc59283511bafb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a77aea9f93d8bcc5949abddcbda52d919"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_30US_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_30US_MASK](#a77aea9f93d8bcc5949abddcbda52d919)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a93fc4d9abc1964278748d7dacec7d15a"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_40US_MASK BIT(3)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_40US_MASK](#a93fc4d9abc1964278748d7dacec7d15a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a9f45646b734d3d831d307485d2c8c076"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_50US_MASK BIT(4)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_50US_MASK](#a9f45646b734d3d831d307485d2c8c076)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a27771be57984aac0b825b3ff033df070"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_60US_MASK BIT(5)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_60US_MASK](#a27771be57984aac0b825b3ff033df070)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab9c3168510c3e5161c393d7093c3527b"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_80US_MASK BIT(6)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_80US_MASK](#ab9c3168510c3e5161c393d7093c3527b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acc787bc6363f4c885816a677f7c47db7"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_100US_MASK BIT(7)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_100US_MASK](#acc787bc6363f4c885816a677f7c47db7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a40d5f49728ef8204e9b19be3da28a5ae"></a>

```c
#define BT_HCI_LE_CS_T_FCS_TIME_1200US_MASK BIT(8)
```

相关声明：[BT_HCI_LE_CS_T_FCS_TIME_1200US_MASK](#a40d5f49728ef8204e9b19be3da28a5ae)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a46f2a35868d8422878e89f1ddde0e7dc"></a>

```c
#define BT_HCI_LE_CS_T_PM_TIME_10US_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_T_PM_TIME_10US_MASK](#a46f2a35868d8422878e89f1ddde0e7dc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a68e13620f22327e8e132aeb19a7cdaf6"></a>

```c
#define BT_HCI_LE_CS_T_PM_TIME_20US_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_T_PM_TIME_20US_MASK](#a68e13620f22327e8e132aeb19a7cdaf6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a24c56f19fcf03aabb170925555209f33"></a>

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_18DB_MASK BIT(0)
```

相关声明：[BT_HCI_LE_CS_TX_SNR_CAPABILITY_18DB_MASK](#a24c56f19fcf03aabb170925555209f33)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a80fe1748abbd89e1700c239ff450ce07"></a>

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_21DB_MASK BIT(1)
```

相关声明：[BT_HCI_LE_CS_TX_SNR_CAPABILITY_21DB_MASK](#a80fe1748abbd89e1700c239ff450ce07)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acd8cc2c9de0edd52c954b0d70dfa44ac"></a>

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_24DB_MASK BIT(2)
```

相关声明：[BT_HCI_LE_CS_TX_SNR_CAPABILITY_24DB_MASK](#acd8cc2c9de0edd52c954b0d70dfa44ac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1f27b2456c323b90eebfa8e45932d92f"></a>

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_27DB_MASK BIT(3)
```

相关声明：[BT_HCI_LE_CS_TX_SNR_CAPABILITY_27DB_MASK](#a1f27b2456c323b90eebfa8e45932d92f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5045b5b06b3c79c77a4997066f332d13"></a>

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_30DB_MASK BIT(4)
```

相关声明：[BT_HCI_LE_CS_TX_SNR_CAPABILITY_30DB_MASK](#a5045b5b06b3c79c77a4997066f332d13)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_abceb3da0b6d4c858ad35c631acf0516e"></a>

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE 0x2C
```

相关声明：[BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE](#abceb3da0b6d4c858ad35c631acf0516e)。

<a id="r_a654ffdb3fac697916351b12f737425bd"></a>

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 0x38
```

相关声明：[BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2](#a654ffdb3fac697916351b12f737425bd)。

HCI 低功耗蓝牙信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete，v2）。

<a id="r_a319b523766bcc778ba6bfb3784ac49b7"></a>

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE 0x2D
```

相关声明：[BT_HCI_EVT_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE](#a319b523766bcc778ba6bfb3784ac49b7)。

<a id="r_a9c815ae28e424256fc440b426ba69892"></a>

```c
#define BT_HCI_LE_CS_CONFIG_ACTION_REMOVED 0x00
```

相关声明：[BT_HCI_LE_CS_CONFIG_ACTION_REMOVED](#a9c815ae28e424256fc440b426ba69892)。

<a id="r_aa437d198f03b30ddbac6ada679e5e0c6"></a>

```c
#define BT_HCI_LE_CS_CONFIG_ACTION_CREATED 0x01
```

相关声明：[BT_HCI_LE_CS_CONFIG_ACTION_CREATED](#aa437d198f03b30ddbac6ada679e5e0c6)。

<a id="r_ae1e6afca81585dda0f08f85adc3c69a3"></a>

```c
#define BT_HCI_EVT_LE_CS_SECURITY_ENABLE_COMPLETE 0x2E
```

相关声明：[BT_HCI_EVT_LE_CS_SECURITY_ENABLE_COMPLETE](#ae1e6afca81585dda0f08f85adc3c69a3)。

<a id="r_ab0d5abde05c53bc194fe07b8726fb307"></a>

```c
#define BT_HCI_EVT_LE_CS_CONFIG_COMPLETE 0x2F
```

相关声明：[BT_HCI_EVT_LE_CS_CONFIG_COMPLETE](#ab0d5abde05c53bc194fe07b8726fb307)。

<a id="r_aa615aebe1d896ca1a06bf618619d96f7"></a>

```c
#define BT_HCI_LE_CS_TEST_CONN_HANDLE 0x0FFF
```

相关声明：[BT_HCI_LE_CS_TEST_CONN_HANDLE](#aa615aebe1d896ca1a06bf618619d96f7)。

<a id="r_ace872d54fba6d94d62b59a2373c7d0d5"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE 0x0
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE](#ace872d54fba6d94d62b59a2373c7d0d5)。

<a id="r_af057e8492e52d0c8763d4a2e969d949d"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL 0x1
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL](#af057e8492e52d0c8763d4a2e969d949d)。

<a id="r_a821a29dacea9867e4e576f916cf7be3d"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED 0xF
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED](#a821a29dacea9867e4e576f916cf7be3d)。

<a id="r_aee251ce3c46dc0404d880be7d4550fa6"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE 0x0
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE](#aee251ce3c46dc0404d880be7d4550fa6)。

<a id="r_a414d620018a946fcb6c209b21ad6fb00"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_PARTIAL 0x1
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_PARTIAL](#a414d620018a946fcb6c209b21ad6fb00)。

<a id="r_af1907f8ae481a08c674d86e689826f49"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED 0xF
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED](#af1907f8ae481a08c674d86e689826f49)。

<a id="r_a056a67d663cfdc2189b480fc79946c74"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT 0x0
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT](#a056a67d663cfdc2189b480fc79946c74)。

<a id="r_a21eb191c5d99f902c7a244cad685995f"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST](#a21eb191c5d99f902c7a244cad685995f)。

<a id="r_a6dc3f766ce40bbd0ddb7af3cf85677b1"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS 0x2
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS](#a6dc3f766ce40bbd0ddb7af3cf85677b1)。

<a id="r_ae8446a2638bd4009b7dee725bb54c883"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED 0x3
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED](#ae8446a2638bd4009b7dee725bb54c883)。

<a id="r_a1e92177f7be3c6a6be00f97fbfc17dcf"></a>

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED 0xF
```

相关声明：[BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED](#a1e92177f7be3c6a6be00f97fbfc17dcf)。

<a id="r_a095b6061c31229b951b6b96e5d02381f"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT 0x0
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT](#a095b6061c31229b951b6b96e5d02381f)。

<a id="r_a41bbe08db99fb0a2ef77f4f3103f9b6c"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST](#a41bbe08db99fb0a2ef77f4f3103f9b6c)。

<a id="r_ac4817c265c50019d8f74146f7477bf58"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED 0x2
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED](#ac4817c265c50019d8f74146f7477bf58)。

<a id="r_a31cb520a05fe31313bacf8b021da468c"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT 0x3
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT](#a31cb520a05fe31313bacf8b021da468c)。

<a id="r_abfdca3ae615e19c8e24c098ba8349618"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED 0xF
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED](#abfdca3ae615e19c8e24c098ba8349618)。

<a id="r_a6efdde19fbbf06a40d5dc8dee0515af8"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_IGNORED 0x00
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_IGNORED](#a6efdde19fbbf06a40d5dc8dee0515af8)。

<a id="r_ae3e9f6d380a61278a8082f07694bdf43"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_1 0x01
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_1](#ae3e9f6d380a61278a8082f07694bdf43)。

<a id="r_ad6951a0000c3b5cadfbaae94decb153f"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_2 0x02
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_2](#ad6951a0000c3b5cadfbaae94decb153f)。

<a id="r_aaeb365c3f3ea16d760d4943587ea0bd7"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_3 0x03
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_3](#aaeb365c3f3ea16d760d4943587ea0bd7)。

<a id="r_a4cf750ee707ca0b81d4945e4f66798e3"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_4 0x04
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_4](#a4cf750ee707ca0b81d4945e4f66798e3)。

<a id="r_a385a401b373522160b1832b66838e02d"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE 0xC000
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE](#a385a401b373522160b1832b66838e02d)。

<a id="r_a22b108e24f198dfd41b2ad692d448c01"></a>

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_PCT_NOT_AVAILABLE 0xFFFFFFFF
```

相关声明：[BT_HCI_LE_CS_SUBEVENT_RESULT_PCT_NOT_AVAILABLE](#a22b108e24f198dfd41b2ad692d448c01)。

<a id="r_aa4345ca4225d3958968131ba7a5ff950"></a>

```c
#define BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE 0x7F
```

相关声明：[BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE](#aa4345ca4225d3958968131ba7a5ff950)。

<a id="r_af69d92b7c92c8fbeeba8e14838a41f74"></a>

```c
#define BT_HCI_LE_CS_PCT_I_MASK 0x000FFF
```

相关声明：[BT_HCI_LE_CS_PCT_I_MASK](#af69d92b7c92c8fbeeba8e14838a41f74)。

<a id="r_a1720b6024f6156e98cb407d6e06e894e"></a>

```c
#define BT_HCI_LE_CS_PCT_Q_MASK 0xFFF000
```

相关声明：[BT_HCI_LE_CS_PCT_Q_MASK](#a1720b6024f6156e98cb407d6e06e894e)。

<a id="r_adcc92fe105d853cc329bbf4340562835"></a>

```c
#define BT_HCI_LE_CS_TONE_QUALITY_HIGH 0x0
```

相关声明：[BT_HCI_LE_CS_TONE_QUALITY_HIGH](#adcc92fe105d853cc329bbf4340562835)。

<a id="r_af42a419097a2e8ee37d46419cd5e20c3"></a>

```c
#define BT_HCI_LE_CS_TONE_QUALITY_MED 0x1
```

相关声明：[BT_HCI_LE_CS_TONE_QUALITY_MED](#af42a419097a2e8ee37d46419cd5e20c3)。

<a id="r_accc9e73d5fd38c6ab3d108bc3fd039de"></a>

```c
#define BT_HCI_LE_CS_TONE_QUALITY_LOW 0x2
```

相关声明：[BT_HCI_LE_CS_TONE_QUALITY_LOW](#accc9e73d5fd38c6ab3d108bc3fd039de)。

<a id="r_a2b14945754c982ead67ad3b7e615eba9"></a>

```c
#define BT_HCI_LE_CS_TONE_QUALITY_UNAVAILABLE 0x3
```

相关声明：[BT_HCI_LE_CS_TONE_QUALITY_UNAVAILABLE](#a2b14945754c982ead67ad3b7e615eba9)。

<a id="r_a014d9a06d3c571ce06c94a2ebfdbe4e5"></a>

```c
#define BT_HCI_LE_CS_NOT_TONE_EXT_SLOT 0x0
```

相关声明：[BT_HCI_LE_CS_NOT_TONE_EXT_SLOT](#a014d9a06d3c571ce06c94a2ebfdbe4e5)。

<a id="r_a72a59878b1445b037eb633a374de92e8"></a>

```c
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_NOT_EXPECTED 0x1
```

相关声明：[BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_NOT_EXPECTED](#a72a59878b1445b037eb633a374de92e8)。

<a id="r_a932802d089c04b78dd6a541b3ddff1e1"></a>

```c
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_EXPECTED 0x2
```

相关声明：[BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_EXPECTED](#a932802d089c04b78dd6a541b3ddff1e1)。

<a id="r_ad0895b572ba1e3d763dbef69c1541b2c"></a>

```c
#define BT_HCI_LE_CS_TIME_DIFFERENCE_NOT_AVAILABLE ((int16_t)0x8000)
```

相关声明：[BT_HCI_LE_CS_TIME_DIFFERENCE_NOT_AVAILABLE](#ad0895b572ba1e3d763dbef69c1541b2c)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

<a id="r_a54895cd6caacff2dc5aee25e301144a7"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_UNLIKELY 0x00
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_UNLIKELY](#a54895cd6caacff2dc5aee25e301144a7)。

<a id="r_af10362bcbd6b95f8404654d258acdbcb"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_UNLIKELY 0x01
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_UNLIKELY](#af10362bcbd6b95f8404654d258acdbcb)。

<a id="r_acf2d6f7fd7873e12389a2d470241340f"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_UNLIKELY 0x02
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_UNLIKELY](#acf2d6f7fd7873e12389a2d470241340f)。

<a id="r_a73bf7224e934c28a73d5e54a632e0e69"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_POSSIBLE 0x03
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_POSSIBLE](#a73bf7224e934c28a73d5e54a632e0e69)。

<a id="r_a93f1786e8177c89eb9db36a72e367122"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_LIKELY 0x04
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_LIKELY](#a93f1786e8177c89eb9db36a72e367122)。

<a id="r_a0b10dcb24c429d594b17eec494954d74"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_LIKELY 0x05
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_LIKELY](#a0b10dcb24c429d594b17eec494954d74)。

<a id="r_abfedf14c97b27f6cdbbb66f2598734e9"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_LIKELY 0x06
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_LIKELY](#abfedf14c97b27f6cdbbb66f2598734e9)。

<a id="r_a5f7d8e81a83a3b94e18a39b507232823"></a>

```c
#define BT_HCI_LE_CS_PACKET_NADM_UNKNOWN 0xFF
```

相关声明：[BT_HCI_LE_CS_PACKET_NADM_UNKNOWN](#a5f7d8e81a83a3b94e18a39b507232823)。

<a id="r_ab05d15713fb0145b32a5977774b50533"></a>

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_SUCCESSFUL 0x0
```

相关声明：[BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_SUCCESSFUL](#ab05d15713fb0145b32a5977774b50533)。

<a id="r_a7c0e4053873d629e10567937adc033d3"></a>

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_BIT_ERRORS_FOUND 0x1
```

相关声明：[BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_BIT_ERRORS_FOUND](#a7c0e4053873d629e10567937adc033d3)。

<a id="r_af357550f37226be5b2b6491ebad3fd57"></a>

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_AA_NOT_FOUND 0x2
```

相关声明：[BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_AA_NOT_FOUND](#af357550f37226be5b2b6491ebad3fd57)。

<a id="r_a8ce6b3556a9f5b83648b80d90652f00d"></a>

```c
#define BT_HCI_LE_CS_PACKET_RSSI_NOT_AVAILABLE 0x7F
```

相关声明：[BT_HCI_LE_CS_PACKET_RSSI_NOT_AVAILABLE](#a8ce6b3556a9f5b83648b80d90652f00d)。

<a id="r_a56079aad1e8efe328c0bfd4dbad9d953"></a>

```c
#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT 0x31
```

相关声明：[BT_HCI_EVT_LE_CS_SUBEVENT_RESULT](#a56079aad1e8efe328c0bfd4dbad9d953)。

<a id="r_aad00fc66b8bbc4f3e474661cb4122e47"></a>

```c
#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT_CONTINUE 0x32
```

相关声明：[BT_HCI_EVT_LE_CS_SUBEVENT_RESULT_CONTINUE](#aad00fc66b8bbc4f3e474661cb4122e47)。

<a id="r_a7dae3e2125d30c3b344b51aba0df68bf"></a>

```c
#define BT_HCI_EVT_LE_CS_TEST_END_COMPLETE 0x33
```

相关声明：[BT_HCI_EVT_LE_CS_TEST_END_COMPLETE](#a7dae3e2125d30c3b344b51aba0df68bf)。

<a id="r_a276cf3951bb5c4ee0b1deeb78a7b5681"></a>

```c
#define BT_HCI_EVT_LE_CS_PROCEDURE_ENABLE_COMPLETE 0x30
```

相关声明：[BT_HCI_EVT_LE_CS_PROCEDURE_ENABLE_COMPLETE](#a276cf3951bb5c4ee0b1deeb78a7b5681)。

<a id="r_a38b479e428c9154c51f04bc84ddf7279"></a>

```c
#define BT_HCI_EVT_LE_FRAME_SPACE_UPDATE_COMPLETE 0x35
```

相关声明：[BT_HCI_EVT_LE_FRAME_SPACE_UPDATE_COMPLETE](#a38b479e428c9154c51f04bc84ddf7279)。

<a id="r_a6b4187331428ca3abdcce55320e56fe9"></a>

```c
#define BT_HCI_EVT_LE_CONN_RATE_CHANGE 0x37
```

相关声明：[BT_HCI_EVT_LE_CONN_RATE_CHANGE](#a6b4187331428ca3abdcce55320e56fe9)。

<a id="r_a25201544478590f6ee87a829410c612b"></a>

```c
#define BT_EVT_BIT(n)
```

相关声明：[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a79851cd962916f9be81e29ce9797e901"></a>

```c
#define BT_EVT_MASK_INQUIRY_COMPLETE BT_EVT_BIT(0)
```

相关声明：[BT_EVT_MASK_INQUIRY_COMPLETE](#a79851cd962916f9be81e29ce9797e901)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a5a13adda8bf4f015550a043667e0b67d"></a>

```c
#define BT_EVT_MASK_CONN_COMPLETE BT_EVT_BIT(2)
```

相关声明：[BT_EVT_MASK_CONN_COMPLETE](#a5a13adda8bf4f015550a043667e0b67d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad77bbcd4fb8b0e37700492e8a3cccd38"></a>

```c
#define BT_EVT_MASK_CONN_REQUEST BT_EVT_BIT(3)
```

相关声明：[BT_EVT_MASK_CONN_REQUEST](#ad77bbcd4fb8b0e37700492e8a3cccd38)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a5ea9d4fb977c660bc33be93c73817705"></a>

```c
#define BT_EVT_MASK_DISCONN_COMPLETE BT_EVT_BIT(4)
```

相关声明：[BT_EVT_MASK_DISCONN_COMPLETE](#a5ea9d4fb977c660bc33be93c73817705)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad4f80dd3fdf22b23d47785a507aa5a85"></a>

```c
#define BT_EVT_MASK_AUTH_COMPLETE BT_EVT_BIT(5)
```

相关声明：[BT_EVT_MASK_AUTH_COMPLETE](#ad4f80dd3fdf22b23d47785a507aa5a85)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a4433027483d6d63911b59c4fe605ba69"></a>

```c
#define BT_EVT_MASK_REMOTE_NAME_REQ_COMPLETE BT_EVT_BIT(6)
```

相关声明：[BT_EVT_MASK_REMOTE_NAME_REQ_COMPLETE](#a4433027483d6d63911b59c4fe605ba69)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a334c571248a1aad285bb11bc39d2ade8"></a>

```c
#define BT_EVT_MASK_ENCRYPT_CHANGE BT_EVT_BIT(7)
```

相关声明：[BT_EVT_MASK_ENCRYPT_CHANGE](#a334c571248a1aad285bb11bc39d2ade8)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a7ccade60a01e0f8a175b3b11b5e20f6d"></a>

```c
#define BT_EVT_MASK_REMOTE_FEATURES BT_EVT_BIT(10)
```

相关声明：[BT_EVT_MASK_REMOTE_FEATURES](#a7ccade60a01e0f8a175b3b11b5e20f6d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a87331cabdea78ace1577cbf2fa7e3523"></a>

```c
#define BT_EVT_MASK_REMOTE_VERSION_INFO BT_EVT_BIT(11)
```

相关声明：[BT_EVT_MASK_REMOTE_VERSION_INFO](#a87331cabdea78ace1577cbf2fa7e3523)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a079c00e59422034a9f977af7dd20234c"></a>

```c
#define BT_EVT_MASK_HARDWARE_ERROR BT_EVT_BIT(15)
```

相关声明：[BT_EVT_MASK_HARDWARE_ERROR](#a079c00e59422034a9f977af7dd20234c)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a4b4a80b51b2c20bf28fbfac57679a86e"></a>

```c
#define BT_EVT_MASK_ROLE_CHANGE BT_EVT_BIT(17)
```

相关声明：[BT_EVT_MASK_ROLE_CHANGE](#a4b4a80b51b2c20bf28fbfac57679a86e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a17cdf232094d1eaee9b847fb3d096c79"></a>

```c
#define BT_EVT_MASK_MODE_CHANGE BT_EVT_BIT(19)
```

相关声明：[BT_EVT_MASK_MODE_CHANGE](#a17cdf232094d1eaee9b847fb3d096c79)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a9f5612d89848aafb6e9063a55e5cd6b4"></a>

```c
#define BT_EVT_MASK_PIN_CODE_REQ BT_EVT_BIT(21)
```

相关声明：[BT_EVT_MASK_PIN_CODE_REQ](#a9f5612d89848aafb6e9063a55e5cd6b4)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a1e16ab7caf239e804c0c2057e9b49e42"></a>

```c
#define BT_EVT_MASK_LINK_KEY_REQ BT_EVT_BIT(22)
```

相关声明：[BT_EVT_MASK_LINK_KEY_REQ](#a1e16ab7caf239e804c0c2057e9b49e42)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aa20a3ce217a60070826d0b55ebd105be"></a>

```c
#define BT_EVT_MASK_LINK_KEY_NOTIFY BT_EVT_BIT(23)
```

相关声明：[BT_EVT_MASK_LINK_KEY_NOTIFY](#aa20a3ce217a60070826d0b55ebd105be)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a829ea33c603291d331faba58689b0198"></a>

```c
#define BT_EVT_MASK_DATA_BUFFER_OVERFLOW BT_EVT_BIT(25)
```

相关声明：[BT_EVT_MASK_DATA_BUFFER_OVERFLOW](#a829ea33c603291d331faba58689b0198)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ada3fa58cfba4324ae9f3baa7661b6808"></a>

```c
#define BT_EVT_MASK_CONN_PKT_TYPE_CHANGED BT_EVT_BIT(28)
```

相关声明：[BT_EVT_MASK_CONN_PKT_TYPE_CHANGED](#ada3fa58cfba4324ae9f3baa7661b6808)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

连接分组类型已改变事件（Connection Packet Type Changed Event）的事件掩码位（Event Mask Bit）。

<a id="r_aeb5b4cbc01a8cebea5ce8e0090d37261"></a>

```c
#define BT_EVT_MASK_INQUIRY_RESULT_WITH_RSSI BT_EVT_BIT(33)
```

相关声明：[BT_EVT_MASK_INQUIRY_RESULT_WITH_RSSI](#aeb5b4cbc01a8cebea5ce8e0090d37261)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a9d3bbaa1eb1dbe72714b922dcada3347"></a>

```c
#define BT_EVT_MASK_REMOTE_EXT_FEATURES BT_EVT_BIT(34)
```

相关声明：[BT_EVT_MASK_REMOTE_EXT_FEATURES](#a9d3bbaa1eb1dbe72714b922dcada3347)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a4f1a905136cb713c09fb5197dd099ce2"></a>

```c
#define BT_EVT_MASK_SYNC_CONN_COMPLETE BT_EVT_BIT(43)
```

相关声明：[BT_EVT_MASK_SYNC_CONN_COMPLETE](#a4f1a905136cb713c09fb5197dd099ce2)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a9b361fe6314f56fcb016bacb064af815"></a>

```c
#define BT_EVT_MASK_EXTENDED_INQUIRY_RESULT BT_EVT_BIT(46)
```

相关声明：[BT_EVT_MASK_EXTENDED_INQUIRY_RESULT](#a9b361fe6314f56fcb016bacb064af815)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_af8d96cc1cf99a7130d4c181450998cb7"></a>

```c
#define BT_EVT_MASK_ENCRYPT_KEY_REFRESH_COMPLETE BT_EVT_BIT(47)
```

相关声明：[BT_EVT_MASK_ENCRYPT_KEY_REFRESH_COMPLETE](#af8d96cc1cf99a7130d4c181450998cb7)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a845de3735dc3989d3a9d54cf5e55b408"></a>

```c
#define BT_EVT_MASK_IO_CAPA_REQ BT_EVT_BIT(48)
```

相关声明：[BT_EVT_MASK_IO_CAPA_REQ](#a845de3735dc3989d3a9d54cf5e55b408)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a409e33dbe4fdb1dc90050e0b4eab1f86"></a>

```c
#define BT_EVT_MASK_IO_CAPA_RESP BT_EVT_BIT(49)
```

相关声明：[BT_EVT_MASK_IO_CAPA_RESP](#a409e33dbe4fdb1dc90050e0b4eab1f86)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a1c04cc7d04f056e5edfc4ddaa97c657f"></a>

```c
#define BT_EVT_MASK_USER_CONFIRM_REQ BT_EVT_BIT(50)
```

相关声明：[BT_EVT_MASK_USER_CONFIRM_REQ](#a1c04cc7d04f056e5edfc4ddaa97c657f)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_af56d87ffc24c2e4c08db68ab019fd58e"></a>

```c
#define BT_EVT_MASK_USER_PASSKEY_REQ BT_EVT_BIT(51)
```

相关声明：[BT_EVT_MASK_USER_PASSKEY_REQ](#af56d87ffc24c2e4c08db68ab019fd58e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a6a08ace148ea2728614a3bab02c21f65"></a>

```c
#define BT_EVT_MASK_SSP_COMPLETE BT_EVT_BIT(53)
```

相关声明：[BT_EVT_MASK_SSP_COMPLETE](#a6a08ace148ea2728614a3bab02c21f65)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a2eb47347a5685a290087b236d696971e"></a>

```c
#define BT_EVT_MASK_USER_PASSKEY_NOTIFY BT_EVT_BIT(58)
```

相关声明：[BT_EVT_MASK_USER_PASSKEY_NOTIFY](#a2eb47347a5685a290087b236d696971e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a59f89d39350b396f8d0c986e2d477bba"></a>

```c
#define BT_EVT_MASK_LE_META_EVENT BT_EVT_BIT(61)
```

相关声明：[BT_EVT_MASK_LE_META_EVENT](#a59f89d39350b396f8d0c986e2d477bba)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_abe39e63cbdee9bfeac36a1b6a4d40aba"></a>

```c
#define BT_EVT_MASK_NUM_COMPLETE_DATA_BLOCKS BT_EVT_BIT(8)
```

相关声明：[BT_EVT_MASK_NUM_COMPLETE_DATA_BLOCKS](#abe39e63cbdee9bfeac36a1b6a4d40aba)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aff43216feb0c29c6813d198473f34fdc"></a>

```c
#define BT_EVT_MASK_TRIGG_CLOCK_CAPTURE BT_EVT_BIT(14)
```

相关声明：[BT_EVT_MASK_TRIGG_CLOCK_CAPTURE](#aff43216feb0c29c6813d198473f34fdc)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ac078d5b46d7e227726cb7456e2163d3f"></a>

```c
#define BT_EVT_MASK_SYNCH_TRAIN_COMPLETE BT_EVT_BIT(15)
```

相关声明：[BT_EVT_MASK_SYNCH_TRAIN_COMPLETE](#ac078d5b46d7e227726cb7456e2163d3f)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a8901b477ec3584af207b3648b221bb92"></a>

```c
#define BT_EVT_MASK_SYNCH_TRAIN_RX BT_EVT_BIT(16)
```

相关声明：[BT_EVT_MASK_SYNCH_TRAIN_RX](#a8901b477ec3584af207b3648b221bb92)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aa8842138b1146d3581c39062d11a6305"></a>

```c
#define BT_EVT_MASK_CL_PER_BC_RX BT_EVT_BIT(17)
```

相关声明：[BT_EVT_MASK_CL_PER_BC_RX](#aa8842138b1146d3581c39062d11a6305)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_af513eaa35861cfcfefba97e0263e3f5b"></a>

```c
#define BT_EVT_MASK_CL_PER_BC_TIMEOUT BT_EVT_BIT(18)
```

相关声明：[BT_EVT_MASK_CL_PER_BC_TIMEOUT](#af513eaa35861cfcfefba97e0263e3f5b)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a9b82f06f42651c32f4c0db9826002134"></a>

```c
#define BT_EVT_MASK_TRUNC_PAGE_COMPLETE BT_EVT_BIT(19)
```

相关声明：[BT_EVT_MASK_TRUNC_PAGE_COMPLETE](#a9b82f06f42651c32f4c0db9826002134)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad078befa197baac20294dc0d46eff9dd"></a>

```c
#define BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT BT_EVT_BIT(20)
```

相关声明：[BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT](#ad078befa197baac20294dc0d46eff9dd)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a35f42f297b980a050deceb71237883ba"></a>

```c
#define BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE BT_EVT_BIT(21)
```

相关声明：[BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE](#a35f42f297b980a050deceb71237883ba)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ae8106016a80e123016c6d2fc406224d7"></a>

```c
#define BT_EVT_MASK_INQUIRY_RSP_NOT BT_EVT_BIT(22)
```

相关声明：[BT_EVT_MASK_INQUIRY_RSP_NOT](#ae8106016a80e123016c6d2fc406224d7)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a33753df12afb5f7e19be01f9febc5d23"></a>

```c
#define BT_EVT_MASK_AUTH_PAYLOAD_TIMEOUT_EXP BT_EVT_BIT(23)
```

相关声明：[BT_EVT_MASK_AUTH_PAYLOAD_TIMEOUT_EXP](#a33753df12afb5f7e19be01f9febc5d23)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a8bfac36e993c48d12bdeb7c130fdd6dc"></a>

```c
#define BT_EVT_MASK_SAM_STATUS_CHANGE BT_EVT_BIT(24)
```

相关声明：[BT_EVT_MASK_SAM_STATUS_CHANGE](#a8bfac36e993c48d12bdeb7c130fdd6dc)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a59cd7a15e5b562adb6397509463e375c"></a>

```c
#define BT_EVT_MASK_LE_CONN_COMPLETE BT_EVT_BIT(0)
```

相关声明：[BT_EVT_MASK_LE_CONN_COMPLETE](#a59cd7a15e5b562adb6397509463e375c)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a39a55a4c3e71db708e39c8110a2349f7"></a>

```c
#define BT_EVT_MASK_LE_ADVERTISING_REPORT BT_EVT_BIT(1)
```

相关声明：[BT_EVT_MASK_LE_ADVERTISING_REPORT](#a39a55a4c3e71db708e39c8110a2349f7)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab1988671f4017f6434dc0438b2e8b9f6"></a>

```c
#define BT_EVT_MASK_LE_CONN_UPDATE_COMPLETE BT_EVT_BIT(2)
```

相关声明：[BT_EVT_MASK_LE_CONN_UPDATE_COMPLETE](#ab1988671f4017f6434dc0438b2e8b9f6)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_adba1a3a872ee26a41218c9104e9f957b"></a>

```c
#define BT_EVT_MASK_LE_REMOTE_FEAT_COMPLETE BT_EVT_BIT(3)
```

相关声明：[BT_EVT_MASK_LE_REMOTE_FEAT_COMPLETE](#adba1a3a872ee26a41218c9104e9f957b)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab495948af67d01208eff1adb9a33e489"></a>

```c
#define BT_EVT_MASK_LE_LTK_REQUEST BT_EVT_BIT(4)
```

相关声明：[BT_EVT_MASK_LE_LTK_REQUEST](#ab495948af67d01208eff1adb9a33e489)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ac3eeaa0610a6ac6d3b57880042071f2a"></a>

```c
#define BT_EVT_MASK_LE_CONN_PARAM_REQ BT_EVT_BIT(5)
```

相关声明：[BT_EVT_MASK_LE_CONN_PARAM_REQ](#ac3eeaa0610a6ac6d3b57880042071f2a)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a73489ce7067d812e8443e242ee53a5e6"></a>

```c
#define BT_EVT_MASK_LE_DATA_LEN_CHANGE BT_EVT_BIT(6)
```

相关声明：[BT_EVT_MASK_LE_DATA_LEN_CHANGE](#a73489ce7067d812e8443e242ee53a5e6)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a281d70b2b596b918972b59e684b6a476"></a>

```c
#define BT_EVT_MASK_LE_P256_PUBLIC_KEY_COMPLETE BT_EVT_BIT(7)
```

相关声明：[BT_EVT_MASK_LE_P256_PUBLIC_KEY_COMPLETE](#a281d70b2b596b918972b59e684b6a476)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_afbe64037a16680397614ba2db136b452"></a>

```c
#define BT_EVT_MASK_LE_GENERATE_DHKEY_COMPLETE BT_EVT_BIT(8)
```

相关声明：[BT_EVT_MASK_LE_GENERATE_DHKEY_COMPLETE](#afbe64037a16680397614ba2db136b452)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_afb3b477cb835e60c3e77237451ebae5b"></a>

```c
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE BT_EVT_BIT(9)
```

相关声明：[BT_EVT_MASK_LE_ENH_CONN_COMPLETE](#afb3b477cb835e60c3e77237451ebae5b)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a3e84268b1e701ae37c77e95847490222"></a>

```c
#define BT_EVT_MASK_LE_DIRECT_ADV_REPORT BT_EVT_BIT(10)
```

相关声明：[BT_EVT_MASK_LE_DIRECT_ADV_REPORT](#a3e84268b1e701ae37c77e95847490222)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab5f6014468b107486aba04ba698453ed"></a>

```c
#define BT_EVT_MASK_LE_PHY_UPDATE_COMPLETE BT_EVT_BIT(11)
```

相关声明：[BT_EVT_MASK_LE_PHY_UPDATE_COMPLETE](#ab5f6014468b107486aba04ba698453ed)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a1d7fc1a3ea229622560de8cf0bb63a81"></a>

```c
#define BT_EVT_MASK_LE_EXT_ADVERTISING_REPORT BT_EVT_BIT(12)
```

相关声明：[BT_EVT_MASK_LE_EXT_ADVERTISING_REPORT](#a1d7fc1a3ea229622560de8cf0bb63a81)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a96142f5d79029a93a99152ade46fc005"></a>

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED BT_EVT_BIT(13)
```

相关声明：[BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED](#a96142f5d79029a93a99152ade46fc005)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad7fc62afd0e1e3dc040567d91320e18e"></a>

```c
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT BT_EVT_BIT(14)
```

相关声明：[BT_EVT_MASK_LE_PER_ADVERTISING_REPORT](#ad7fc62afd0e1e3dc040567d91320e18e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ae78587797f24987f36c348fe790438b2"></a>

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_LOST BT_EVT_BIT(15)
```

相关声明：[BT_EVT_MASK_LE_PER_ADV_SYNC_LOST](#ae78587797f24987f36c348fe790438b2)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a372f6b8e355972d63e5f9ff45a486e9d"></a>

```c
#define BT_EVT_MASK_LE_SCAN_TIMEOUT BT_EVT_BIT(16)
```

相关声明：[BT_EVT_MASK_LE_SCAN_TIMEOUT](#a372f6b8e355972d63e5f9ff45a486e9d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a11330b1b6847d77d3ba88e1de0aaa36e"></a>

```c
#define BT_EVT_MASK_LE_ADV_SET_TERMINATED BT_EVT_BIT(17)
```

相关声明：[BT_EVT_MASK_LE_ADV_SET_TERMINATED](#a11330b1b6847d77d3ba88e1de0aaa36e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a3f13865e913a1c6afb6d8d05a6d84608"></a>

```c
#define BT_EVT_MASK_LE_SCAN_REQ_RECEIVED BT_EVT_BIT(18)
```

相关声明：[BT_EVT_MASK_LE_SCAN_REQ_RECEIVED](#a3f13865e913a1c6afb6d8d05a6d84608)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_acee0428356c4853fe664709fc1675f02"></a>

```c
#define BT_EVT_MASK_LE_CHAN_SEL_ALGO BT_EVT_BIT(19)
```

相关声明：[BT_EVT_MASK_LE_CHAN_SEL_ALGO](#acee0428356c4853fe664709fc1675f02)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a6ef13decc171530c00f12b0226fa9ed1"></a>

```c
#define BT_EVT_MASK_LE_CONNECTIONLESS_IQ_REPORT BT_EVT_BIT(20)
```

相关声明：[BT_EVT_MASK_LE_CONNECTIONLESS_IQ_REPORT](#a6ef13decc171530c00f12b0226fa9ed1)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a3b2f133db5641414b95bfd953d715ff3"></a>

```c
#define BT_EVT_MASK_LE_CONNECTION_IQ_REPORT BT_EVT_BIT(21)
```

相关声明：[BT_EVT_MASK_LE_CONNECTION_IQ_REPORT](#a3b2f133db5641414b95bfd953d715ff3)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_afbd3991be814ec6462d62fbc4c898ac0"></a>

```c
#define BT_EVT_MASK_LE_CTE_REQUEST_FAILED BT_EVT_BIT(22)
```

相关声明：[BT_EVT_MASK_LE_CTE_REQUEST_FAILED](#afbd3991be814ec6462d62fbc4c898ac0)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a5b2139ce8847bfcdbcd99c3241fb5ea2"></a>

```c
#define BT_EVT_MASK_LE_PAST_RECEIVED BT_EVT_BIT(23)
```

相关声明：[BT_EVT_MASK_LE_PAST_RECEIVED](#a5b2139ce8847bfcdbcd99c3241fb5ea2)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a9e41b4cb965576490fb39f7dc396722f"></a>

```c
#define BT_EVT_MASK_LE_CIS_ESTABLISHED BT_EVT_BIT(24)
```

相关声明：[BT_EVT_MASK_LE_CIS_ESTABLISHED](#a9e41b4cb965576490fb39f7dc396722f)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aa24e9569ace049098a6d822ad7433e26"></a>

```c
#define BT_EVT_MASK_LE_CIS_REQ BT_EVT_BIT(25)
```

相关声明：[BT_EVT_MASK_LE_CIS_REQ](#aa24e9569ace049098a6d822ad7433e26)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a447ff4a3e4dfba390ce9729e45abb410"></a>

```c
#define BT_EVT_MASK_LE_BIG_COMPLETE BT_EVT_BIT(26)
```

相关声明：[BT_EVT_MASK_LE_BIG_COMPLETE](#a447ff4a3e4dfba390ce9729e45abb410)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad4b775d48bfa14c00c78ac1fbb8f2a2a"></a>

```c
#define BT_EVT_MASK_LE_BIG_TERMINATED BT_EVT_BIT(27)
```

相关声明：[BT_EVT_MASK_LE_BIG_TERMINATED](#ad4b775d48bfa14c00c78ac1fbb8f2a2a)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab88b8bcde1d07b5f16c55c4cbf4fd20d"></a>

```c
#define BT_EVT_MASK_LE_BIG_SYNC_ESTABLISHED BT_EVT_BIT(28)
```

相关声明：[BT_EVT_MASK_LE_BIG_SYNC_ESTABLISHED](#ab88b8bcde1d07b5f16c55c4cbf4fd20d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a87abdedde8bd43f845fe604c80612ca0"></a>

```c
#define BT_EVT_MASK_LE_BIG_SYNC_LOST BT_EVT_BIT(29)
```

相关声明：[BT_EVT_MASK_LE_BIG_SYNC_LOST](#a87abdedde8bd43f845fe604c80612ca0)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a01e518d3bb3d4f99c335743362a84080"></a>

```c
#define BT_EVT_MASK_LE_REQ_PEER_SCA_COMPLETE BT_EVT_BIT(30)
```

相关声明：[BT_EVT_MASK_LE_REQ_PEER_SCA_COMPLETE](#a01e518d3bb3d4f99c335743362a84080)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a6aad398435aa48ba67f6917bca2a690e"></a>

```c
#define BT_EVT_MASK_LE_PATH_LOSS_THRESHOLD BT_EVT_BIT(31)
```

相关声明：[BT_EVT_MASK_LE_PATH_LOSS_THRESHOLD](#a6aad398435aa48ba67f6917bca2a690e)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a7f9d3cdf0de067ad408bec600b9a691f"></a>

```c
#define BT_EVT_MASK_LE_TRANSMIT_POWER_REPORTING BT_EVT_BIT(32)
```

相关声明：[BT_EVT_MASK_LE_TRANSMIT_POWER_REPORTING](#a7f9d3cdf0de067ad408bec600b9a691f)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aff9c37de1e55e6a7085b3a521f34d3e0"></a>

```c
#define BT_EVT_MASK_LE_BIGINFO_ADV_REPORT BT_EVT_BIT(33)
```

相关声明：[BT_EVT_MASK_LE_BIGINFO_ADV_REPORT](#aff9c37de1e55e6a7085b3a521f34d3e0)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a8a52784fd872a8ee6f666c31e846411d"></a>

```c
#define BT_EVT_MASK_LE_SUBRATE_CHANGE BT_EVT_BIT(34)
```

相关声明：[BT_EVT_MASK_LE_SUBRATE_CHANGE](#a8a52784fd872a8ee6f666c31e846411d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a92a360ad268c29e1616de1e16748eb44"></a>

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED_V2 BT_EVT_BIT(35)
```

相关声明：[BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED_V2](#a92a360ad268c29e1616de1e16748eb44)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ad78d5a027581dee52c54bb3f5a19b68d"></a>

```c
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT_V2 BT_EVT_BIT(36)
```

相关声明：[BT_EVT_MASK_LE_PER_ADVERTISING_REPORT_V2](#ad78d5a027581dee52c54bb3f5a19b68d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a93aec31c1636fec90b609981736eb2de"></a>

```c
#define BT_EVT_MASK_LE_PAST_RECEIVED_V2 BT_EVT_BIT(37)
```

相关声明：[BT_EVT_MASK_LE_PAST_RECEIVED_V2](#a93aec31c1636fec90b609981736eb2de)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_af0e2c2e66bdac52fbe5e9c91ca26fe49"></a>

```c
#define BT_EVT_MASK_LE_PER_ADV_SUBEVENT_DATA_REQ BT_EVT_BIT(38)
```

相关声明：[BT_EVT_MASK_LE_PER_ADV_SUBEVENT_DATA_REQ](#af0e2c2e66bdac52fbe5e9c91ca26fe49)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab8a9486fedec169e4d44b249f2445acf"></a>

```c
#define BT_EVT_MASK_LE_PER_ADV_RESPONSE_REPORT BT_EVT_BIT(39)
```

相关声明：[BT_EVT_MASK_LE_PER_ADV_RESPONSE_REPORT](#ab8a9486fedec169e4d44b249f2445acf)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a8b40a701334d25741a6e17ffd86576ad"></a>

```c
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE_V2 BT_EVT_BIT(40)
```

相关声明：[BT_EVT_MASK_LE_ENH_CONN_COMPLETE_V2](#a8b40a701334d25741a6e17ffd86576ad)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a1b02618f1fbfb3a710fd413f205da9a6"></a>

```c
#define BT_EVT_MASK_LE_CIS_ESTABLISHED_V2 BT_EVT_BIT(41)
```

相关声明：[BT_EVT_MASK_LE_CIS_ESTABLISHED_V2](#a1b02618f1fbfb3a710fd413f205da9a6)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a53be462853189607e7733d1131df556f"></a>

```c
#define BT_EVT_MASK_LE_READ_ALL_REMOTE_FEAT_COMPLETE BT_EVT_BIT(42)
```

相关声明：[BT_EVT_MASK_LE_READ_ALL_REMOTE_FEAT_COMPLETE](#a53be462853189607e7733d1131df556f)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a97d1b704b1638fb85fa4da6f6d31e209"></a>

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE BT_EVT_BIT(43)
```

相关声明：[BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE](#a97d1b704b1638fb85fa4da6f6d31e209)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a406cdb92d8c6524aca8971425bab7baa"></a>

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE BT_EVT_BIT(44)
```

相关声明：[BT_EVT_MASK_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE](#a406cdb92d8c6524aca8971425bab7baa)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a07b9cc5a2fcc73d56590a034977cf3a0"></a>

```c
#define BT_EVT_MASK_LE_CS_SECURITY_ENABLE_COMPLETE BT_EVT_BIT(45)
```

相关声明：[BT_EVT_MASK_LE_CS_SECURITY_ENABLE_COMPLETE](#a07b9cc5a2fcc73d56590a034977cf3a0)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_abe6f94ab4bae0d34f23e27c0948e3a21"></a>

```c
#define BT_EVT_MASK_LE_CS_CONFIG_COMPLETE BT_EVT_BIT(46)
```

相关声明：[BT_EVT_MASK_LE_CS_CONFIG_COMPLETE](#abe6f94ab4bae0d34f23e27c0948e3a21)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_affbe9c98cf94e50673a2a59c8fb68256"></a>

```c
#define BT_EVT_MASK_LE_CS_PROCEDURE_ENABLE_COMPLETE BT_EVT_BIT(47)
```

相关声明：[BT_EVT_MASK_LE_CS_PROCEDURE_ENABLE_COMPLETE](#affbe9c98cf94e50673a2a59c8fb68256)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a040ef537fe66f923dc3c344fee023002"></a>

```c
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT BT_EVT_BIT(48)
```

相关声明：[BT_EVT_MASK_LE_CS_SUBEVENT_RESULT](#a040ef537fe66f923dc3c344fee023002)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a226c276713e3cf16108e4a66fad6db79"></a>

```c
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT_CONTINUE BT_EVT_BIT(49)
```

相关声明：[BT_EVT_MASK_LE_CS_SUBEVENT_RESULT_CONTINUE](#a226c276713e3cf16108e4a66fad6db79)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_a8a6ec9510323355aa003cb8be519be7d"></a>

```c
#define BT_EVT_MASK_LE_CS_TEST_END_COMPLETE BT_EVT_BIT(50)
```

相关声明：[BT_EVT_MASK_LE_CS_TEST_END_COMPLETE](#a8a6ec9510323355aa003cb8be519be7d)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ab92e0f5db4474e451285314f90b05e59"></a>

```c
#define BT_EVT_MASK_LE_FRAME_SPACE_UPDATE_COMPLETE BT_EVT_BIT(52)
```

相关声明：[BT_EVT_MASK_LE_FRAME_SPACE_UPDATE_COMPLETE](#ab92e0f5db4474e451285314f90b05e59)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_ae912b6f8f2d8a3057cc8327106098475"></a>

```c
#define BT_EVT_MASK_LE_CONN_RATE_CHANGE BT_EVT_BIT(54)
```

相关声明：[BT_EVT_MASK_LE_CONN_RATE_CHANGE](#ae912b6f8f2d8a3057cc8327106098475)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

<a id="r_aa311f47eecf45fa72cc0b07bb839c4db"></a>

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 BT_EVT_BIT(55)
```

相关声明：[BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2](#aa311f47eecf45fa72cc0b07bb839c4db)、[BT_EVT_BIT](#a25201544478590f6ee87a829410c612b)。

低功耗蓝牙信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete，v2）的事件掩码。

<a id="r_a27c890210eded48f159073cccef8582a"></a>

```c
#define BT_HCI_ERR_SUCCESS 0x00
```

相关声明：[BT_HCI_ERR_SUCCESS](#a27c890210eded48f159073cccef8582a)。

HCI 错误码（Error Codes），依据《蓝牙核心规范》（BT Core Spec）v5.4，第 1 卷 F 部分。

<a id="r_a376012d3b8f7814870e3f03f6cbabb89"></a>

```c
#define BT_HCI_ERR_UNKNOWN_CMD 0x01
```

相关声明：[BT_HCI_ERR_UNKNOWN_CMD](#a376012d3b8f7814870e3f03f6cbabb89)。

<a id="r_afd68afeb0296e3af363d7d60eaf4e9a1"></a>

```c
#define BT_HCI_ERR_UNKNOWN_CONN_ID 0x02
```

相关声明：[BT_HCI_ERR_UNKNOWN_CONN_ID](#afd68afeb0296e3af363d7d60eaf4e9a1)。

<a id="r_a5dfcb0d206b98be7eacdc67547bb8a2c"></a>

```c
#define BT_HCI_ERR_HW_FAILURE 0x03
```

相关声明：[BT_HCI_ERR_HW_FAILURE](#a5dfcb0d206b98be7eacdc67547bb8a2c)。

<a id="r_a1e89c8eb63dee6bd720ef9354c867519"></a>

```c
#define BT_HCI_ERR_PAGE_TIMEOUT 0x04
```

相关声明：[BT_HCI_ERR_PAGE_TIMEOUT](#a1e89c8eb63dee6bd720ef9354c867519)。

<a id="r_a070d51dd0de3288f9811f90a558c889b"></a>

```c
#define BT_HCI_ERR_AUTH_FAIL 0x05
```

相关声明：[BT_HCI_ERR_AUTH_FAIL](#a070d51dd0de3288f9811f90a558c889b)。

<a id="r_a39f129aefe81c2d06f70552ace008a15"></a>

```c
#define BT_HCI_ERR_PIN_OR_KEY_MISSING 0x06
```

相关声明：[BT_HCI_ERR_PIN_OR_KEY_MISSING](#a39f129aefe81c2d06f70552ace008a15)。

<a id="r_ac54f84b29901185822f6bad2edf86b61"></a>

```c
#define BT_HCI_ERR_MEM_CAPACITY_EXCEEDED 0x07
```

相关声明：[BT_HCI_ERR_MEM_CAPACITY_EXCEEDED](#ac54f84b29901185822f6bad2edf86b61)。

<a id="r_ab702caf5cd73431cc9aede8891f74610"></a>

```c
#define BT_HCI_ERR_CONN_TIMEOUT 0x08
```

相关声明：[BT_HCI_ERR_CONN_TIMEOUT](#ab702caf5cd73431cc9aede8891f74610)。

<a id="r_a490798f4f1e226e66475f0fb84cfbcd5"></a>

```c
#define BT_HCI_ERR_CONN_LIMIT_EXCEEDED 0x09
```

相关声明：[BT_HCI_ERR_CONN_LIMIT_EXCEEDED](#a490798f4f1e226e66475f0fb84cfbcd5)。

<a id="r_a56a3d3d9d7798334b29c02214a2e73bf"></a>

```c
#define BT_HCI_ERR_SYNC_CONN_LIMIT_EXCEEDED 0x0a
```

相关声明：[BT_HCI_ERR_SYNC_CONN_LIMIT_EXCEEDED](#a56a3d3d9d7798334b29c02214a2e73bf)。

<a id="r_abcf4cd921e304758cc969a83445d70ec"></a>

```c
#define BT_HCI_ERR_CONN_ALREADY_EXISTS 0x0b
```

相关声明：[BT_HCI_ERR_CONN_ALREADY_EXISTS](#abcf4cd921e304758cc969a83445d70ec)。

<a id="r_a5ee9f2e9625d732e84e5ef593bb2a3f9"></a>

```c
#define BT_HCI_ERR_CMD_DISALLOWED 0x0c
```

相关声明：[BT_HCI_ERR_CMD_DISALLOWED](#a5ee9f2e9625d732e84e5ef593bb2a3f9)。

<a id="r_a0efddbffb31b93158b10a3f678f94f4e"></a>

```c
#define BT_HCI_ERR_INSUFFICIENT_RESOURCES 0x0d
```

相关声明：[BT_HCI_ERR_INSUFFICIENT_RESOURCES](#a0efddbffb31b93158b10a3f678f94f4e)。

<a id="r_a08d4bdfc189bccbdb97a51b0089e77a0"></a>

```c
#define BT_HCI_ERR_INSUFFICIENT_SECURITY 0x0e
```

相关声明：[BT_HCI_ERR_INSUFFICIENT_SECURITY](#a08d4bdfc189bccbdb97a51b0089e77a0)。

<a id="r_a366f85b3bcb3f578b2572149c69b7fc0"></a>

```c
#define BT_HCI_ERR_BD_ADDR_UNACCEPTABLE 0x0f
```

相关声明：[BT_HCI_ERR_BD_ADDR_UNACCEPTABLE](#a366f85b3bcb3f578b2572149c69b7fc0)。

<a id="r_ae4682cbd7a9b9dedd25926efe029c0d7"></a>

```c
#define BT_HCI_ERR_CONN_ACCEPT_TIMEOUT 0x10
```

相关声明：[BT_HCI_ERR_CONN_ACCEPT_TIMEOUT](#ae4682cbd7a9b9dedd25926efe029c0d7)。

<a id="r_af73db17855859676827bad84e2ccbabe"></a>

```c
#define BT_HCI_ERR_UNSUPP_FEATURE_PARAM_VAL 0x11
```

相关声明：[BT_HCI_ERR_UNSUPP_FEATURE_PARAM_VAL](#af73db17855859676827bad84e2ccbabe)。

<a id="r_afc76c774f5e71423eb9fea910d1860e9"></a>

```c
#define BT_HCI_ERR_INVALID_PARAM 0x12
```

相关声明：[BT_HCI_ERR_INVALID_PARAM](#afc76c774f5e71423eb9fea910d1860e9)。

<a id="r_ac0e3b44027180d7a2dedb59395c4b111"></a>

```c
#define BT_HCI_ERR_REMOTE_USER_TERM_CONN 0x13
```

相关声明：[BT_HCI_ERR_REMOTE_USER_TERM_CONN](#ac0e3b44027180d7a2dedb59395c4b111)。

<a id="r_a5eeadfb220c24b2e7f5ce3fd21e5d46a"></a>

```c
#define BT_HCI_ERR_REMOTE_LOW_RESOURCES 0x14
```

相关声明：[BT_HCI_ERR_REMOTE_LOW_RESOURCES](#a5eeadfb220c24b2e7f5ce3fd21e5d46a)。

<a id="r_a083f1fc52300f7e47c2f8d4e50551851"></a>

```c
#define BT_HCI_ERR_REMOTE_POWER_OFF 0x15
```

相关声明：[BT_HCI_ERR_REMOTE_POWER_OFF](#a083f1fc52300f7e47c2f8d4e50551851)。

<a id="r_a0f07b75be216456e9370485dca0da992"></a>

```c
#define BT_HCI_ERR_LOCALHOST_TERM_CONN 0x16
```

相关声明：[BT_HCI_ERR_LOCALHOST_TERM_CONN](#a0f07b75be216456e9370485dca0da992)。

<a id="r_a11d42e0347cc9d1d50ccd45c2e9a39f6"></a>

```c
#define BT_HCI_ERR_REPEATED_ATTEMPTS 0x17
```

相关声明：[BT_HCI_ERR_REPEATED_ATTEMPTS](#a11d42e0347cc9d1d50ccd45c2e9a39f6)。

<a id="r_a60823c337c91aa95348dcae250a83977"></a>

```c
#define BT_HCI_ERR_PAIRING_NOT_ALLOWED 0x18
```

相关声明：[BT_HCI_ERR_PAIRING_NOT_ALLOWED](#a60823c337c91aa95348dcae250a83977)。

<a id="r_a0f81b5c19358982bd33c527239200b08"></a>

```c
#define BT_HCI_ERR_UNKNOWN_LMP_PDU 0x19
```

相关声明：[BT_HCI_ERR_UNKNOWN_LMP_PDU](#a0f81b5c19358982bd33c527239200b08)。

<a id="r_a516751f02bd497a020783f69bcf71453"></a>

```c
#define BT_HCI_ERR_UNSUPP_REMOTE_FEATURE 0x1a
```

相关声明：[BT_HCI_ERR_UNSUPP_REMOTE_FEATURE](#a516751f02bd497a020783f69bcf71453)。

<a id="r_a5e28f04c454361508bc791c6ce292bc2"></a>

```c
#define BT_HCI_ERR_SCO_OFFSET_REJECTED 0x1b
```

相关声明：[BT_HCI_ERR_SCO_OFFSET_REJECTED](#a5e28f04c454361508bc791c6ce292bc2)。

<a id="r_a5093c6357fcefd1ccdcbdf9a99f18e7c"></a>

```c
#define BT_HCI_ERR_SCO_INTERVAL_REJECTED 0x1c
```

相关声明：[BT_HCI_ERR_SCO_INTERVAL_REJECTED](#a5093c6357fcefd1ccdcbdf9a99f18e7c)。

<a id="r_ad8f77a43360e8ab2e6c71a103e14c951"></a>

```c
#define BT_HCI_ERR_SCO_AIR_MODE_REJECTED 0x1d
```

相关声明：[BT_HCI_ERR_SCO_AIR_MODE_REJECTED](#ad8f77a43360e8ab2e6c71a103e14c951)。

<a id="r_a943fe81109d82983018b558b9274f9a3"></a>

```c
#define BT_HCI_ERR_INVALID_LL_PARAM 0x1e
```

相关声明：[BT_HCI_ERR_INVALID_LL_PARAM](#a943fe81109d82983018b558b9274f9a3)。

<a id="r_ab3833bbb70b6a2e57870d8243f528b90"></a>

```c
#define BT_HCI_ERR_UNSPECIFIED 0x1f
```

相关声明：[BT_HCI_ERR_UNSPECIFIED](#ab3833bbb70b6a2e57870d8243f528b90)。

<a id="r_af1fa61561b6a91d08f81e9c19cbe89f7"></a>

```c
#define BT_HCI_ERR_UNSUPP_LL_PARAM_VAL 0x20
```

相关声明：[BT_HCI_ERR_UNSUPP_LL_PARAM_VAL](#af1fa61561b6a91d08f81e9c19cbe89f7)。

<a id="r_a070d016f54e7f5f0a7ca6d8c8218505f"></a>

```c
#define BT_HCI_ERR_ROLE_CHANGE_NOT_ALLOWED 0x21
```

相关声明：[BT_HCI_ERR_ROLE_CHANGE_NOT_ALLOWED](#a070d016f54e7f5f0a7ca6d8c8218505f)。

<a id="r_a6317763780d9c81e6752d5a2c8ce3172"></a>

```c
#define BT_HCI_ERR_LL_RESP_TIMEOUT 0x22
```

相关声明：[BT_HCI_ERR_LL_RESP_TIMEOUT](#a6317763780d9c81e6752d5a2c8ce3172)。

<a id="r_a0e280074290680d62ad4721384bb603e"></a>

```c
#define BT_HCI_ERR_LL_PROC_COLLISION 0x23
```

相关声明：[BT_HCI_ERR_LL_PROC_COLLISION](#a0e280074290680d62ad4721384bb603e)。

<a id="r_a47c02d44d40d785db6fee28c88d3c5b4"></a>

```c
#define BT_HCI_ERR_LMP_PDU_NOT_ALLOWED 0x24
```

相关声明：[BT_HCI_ERR_LMP_PDU_NOT_ALLOWED](#a47c02d44d40d785db6fee28c88d3c5b4)。

<a id="r_aeb5499a707e1c41cbd9db882cfdf0677"></a>

```c
#define BT_HCI_ERR_ENC_MODE_NOT_ACCEPTABLE 0x25
```

相关声明：[BT_HCI_ERR_ENC_MODE_NOT_ACCEPTABLE](#aeb5499a707e1c41cbd9db882cfdf0677)。

<a id="r_aee97132db4398e2db0a6e115ca20b9b4"></a>

```c
#define BT_HCI_ERR_LINK_KEY_CANNOT_BE_CHANGED 0x26
```

相关声明：[BT_HCI_ERR_LINK_KEY_CANNOT_BE_CHANGED](#aee97132db4398e2db0a6e115ca20b9b4)。

<a id="r_a0e02fd84d7a355f42fe006c756936d78"></a>

```c
#define BT_HCI_ERR_REQUESTED_QOS_NOT_SUPPORTED 0x27
```

相关声明：[BT_HCI_ERR_REQUESTED_QOS_NOT_SUPPORTED](#a0e02fd84d7a355f42fe006c756936d78)。

<a id="r_a2d336db995ab250f94de66da952c642c"></a>

```c
#define BT_HCI_ERR_INSTANT_PASSED 0x28
```

相关声明：[BT_HCI_ERR_INSTANT_PASSED](#a2d336db995ab250f94de66da952c642c)。

<a id="r_a059c7d5619823eddf2c541b40a6464cb"></a>

```c
#define BT_HCI_ERR_PAIRING_NOT_SUPPORTED 0x29
```

相关声明：[BT_HCI_ERR_PAIRING_NOT_SUPPORTED](#a059c7d5619823eddf2c541b40a6464cb)。

不支持使用单元密钥配对（Pairing with Unit Key Not Supported）。

<a id="r_a3b461d65baa95f8f984b212264dc5072"></a>

```c
#define BT_HCI_ERR_DIFF_TRANS_COLLISION 0x2a
```

相关声明：[BT_HCI_ERR_DIFF_TRANS_COLLISION](#a3b461d65baa95f8f984b212264dc5072)。

<a id="r_a37c2fdc6b32b4a2cb70d5c17dfbe262b"></a>

```c
#define BT_HCI_ERR_QOS_UNACCEPTABLE_PARAM 0x2c
```

相关声明：[BT_HCI_ERR_QOS_UNACCEPTABLE_PARAM](#a37c2fdc6b32b4a2cb70d5c17dfbe262b)。

<a id="r_a88363d1eb1c0d13dc8138af8edc76abc"></a>

```c
#define BT_HCI_ERR_QOS_REJECTED 0x2d
```

相关声明：[BT_HCI_ERR_QOS_REJECTED](#a88363d1eb1c0d13dc8138af8edc76abc)。

<a id="r_a3b9fc13a3e3ecc9f0f4431487c0301b5"></a>

```c
#define BT_HCI_ERR_CHAN_ASSESS_NOT_SUPPORTED 0x2e
```

相关声明：[BT_HCI_ERR_CHAN_ASSESS_NOT_SUPPORTED](#a3b9fc13a3e3ecc9f0f4431487c0301b5)。

<a id="r_a334efee11bd7086e0611c8f628d65abb"></a>

```c
#define BT_HCI_ERR_INSUFF_SECURITY 0x2f
```

相关声明：[BT_HCI_ERR_INSUFF_SECURITY](#a334efee11bd7086e0611c8f628d65abb)。

<a id="r_a29c763a2e70820fae7e2e825d22f4991"></a>

```c
#define BT_HCI_ERR_PARAM_OUT_OF_MANDATORY_RANGE 0x30
```

相关声明：[BT_HCI_ERR_PARAM_OUT_OF_MANDATORY_RANGE](#a29c763a2e70820fae7e2e825d22f4991)。

<a id="r_ac9c9a68e696e038d7b05af89e3a0c7b6"></a>

```c
#define BT_HCI_ERR_ROLE_SWITCH_PENDING 0x32
```

相关声明：[BT_HCI_ERR_ROLE_SWITCH_PENDING](#ac9c9a68e696e038d7b05af89e3a0c7b6)。

<a id="r_ac6244ca7123879ef039c2c5486d50d41"></a>

```c
#define BT_HCI_ERR_RESERVED_SLOT_VIOLATION 0x34
```

相关声明：[BT_HCI_ERR_RESERVED_SLOT_VIOLATION](#ac6244ca7123879ef039c2c5486d50d41)。

<a id="r_ab40a919a2d87376f2aca6d2ea3f55758"></a>

```c
#define BT_HCI_ERR_ROLE_SWITCH_FAILED 0x35
```

相关声明：[BT_HCI_ERR_ROLE_SWITCH_FAILED](#ab40a919a2d87376f2aca6d2ea3f55758)。

<a id="r_a1b7094ad185ed22542f370ab1101c1ae"></a>

```c
#define BT_HCI_ERR_EXT_INQ_RESP_TOO_LARGE 0x36
```

相关声明：[BT_HCI_ERR_EXT_INQ_RESP_TOO_LARGE](#a1b7094ad185ed22542f370ab1101c1ae)。

<a id="r_afd8840ad198dfdb666bf24851a478c70"></a>

```c
#define BT_HCI_ERR_SIMPLE_PAIR_NOT_SUPP_BY_HOST 0x37
```

相关声明：[BT_HCI_ERR_SIMPLE_PAIR_NOT_SUPP_BY_HOST](#afd8840ad198dfdb666bf24851a478c70)。

<a id="r_a107d85e39fec3146d6b017deb047571b"></a>

```c
#define BT_HCI_ERR_HOST_BUSY_PAIRING 0x38
```

相关声明：[BT_HCI_ERR_HOST_BUSY_PAIRING](#a107d85e39fec3146d6b017deb047571b)。

<a id="r_a1adf558f8f606612ca96bdbbb55e0e78"></a>

```c
#define BT_HCI_ERR_CONN_REJECTED_DUE_TO_NO_CHAN 0x39
```

相关声明：[BT_HCI_ERR_CONN_REJECTED_DUE_TO_NO_CHAN](#a1adf558f8f606612ca96bdbbb55e0e78)。

<a id="r_a33167856fe838b833fe42d92c3eac4eb"></a>

```c
#define BT_HCI_ERR_CONTROLLER_BUSY 0x3a
```

相关声明：[BT_HCI_ERR_CONTROLLER_BUSY](#a33167856fe838b833fe42d92c3eac4eb)。

<a id="r_a712e214942c0d151597ce04e9d0df453"></a>

```c
#define BT_HCI_ERR_UNACCEPT_CONN_PARAM 0x3b
```

相关声明：[BT_HCI_ERR_UNACCEPT_CONN_PARAM](#a712e214942c0d151597ce04e9d0df453)。

<a id="r_abfa408d8366ff3cae1cd35fffcda30c0"></a>

```c
#define BT_HCI_ERR_ADV_TIMEOUT 0x3c
```

相关声明：[BT_HCI_ERR_ADV_TIMEOUT](#abfa408d8366ff3cae1cd35fffcda30c0)。

<a id="r_a71dd49b1b5dc51ad7db8da9aecf9ff06"></a>

```c
#define BT_HCI_ERR_TERM_DUE_TO_MIC_FAIL 0x3d
```

相关声明：[BT_HCI_ERR_TERM_DUE_TO_MIC_FAIL](#a71dd49b1b5dc51ad7db8da9aecf9ff06)。

<a id="r_ac6c44be2e737d7a10b5c886c69d6b1a5"></a>

```c
#define BT_HCI_ERR_CONN_FAIL_TO_ESTAB 0x3e
```

相关声明：[BT_HCI_ERR_CONN_FAIL_TO_ESTAB](#ac6c44be2e737d7a10b5c886c69d6b1a5)。

<a id="r_af0b9f71a874ca2c3587256c7f665e9fa"></a>

```c
#define BT_HCI_ERR_MAC_CONN_FAILED 0x3f
```

相关声明：[BT_HCI_ERR_MAC_CONN_FAILED](#af0b9f71a874ca2c3587256c7f665e9fa)。

<a id="r_a6e9a4db5962d79b5a7f43a4c2919c9e9"></a>

```c
#define BT_HCI_ERR_CLOCK_ADJUST_REJECTED 0x40
```

相关声明：[BT_HCI_ERR_CLOCK_ADJUST_REJECTED](#a6e9a4db5962d79b5a7f43a4c2919c9e9)。

<a id="r_a9e7483e2d7f46981e9d1fcdbb8a7515c"></a>

```c
#define BT_HCI_ERR_SUBMAP_NOT_DEFINED 0x41
```

相关声明：[BT_HCI_ERR_SUBMAP_NOT_DEFINED](#a9e7483e2d7f46981e9d1fcdbb8a7515c)。

<a id="r_a7646bc91f5dbb28c5eeda7e1828f2e30"></a>

```c
#define BT_HCI_ERR_UNKNOWN_ADV_IDENTIFIER 0x42
```

相关声明：[BT_HCI_ERR_UNKNOWN_ADV_IDENTIFIER](#a7646bc91f5dbb28c5eeda7e1828f2e30)。

<a id="r_a86b092455cfd220d48af2bea04900b5b"></a>

```c
#define BT_HCI_ERR_LIMIT_REACHED 0x43
```

相关声明：[BT_HCI_ERR_LIMIT_REACHED](#a86b092455cfd220d48af2bea04900b5b)。

<a id="r_a85433a7b3bcac0a507d7f6376a084142"></a>

```c
#define BT_HCI_ERR_OP_CANCELLED_BY_HOST 0x44
```

相关声明：[BT_HCI_ERR_OP_CANCELLED_BY_HOST](#a85433a7b3bcac0a507d7f6376a084142)。

<a id="r_ab63f7d0c79aaa57abf59aa18e112345f"></a>

```c
#define BT_HCI_ERR_PACKET_TOO_LONG 0x45
```

相关声明：[BT_HCI_ERR_PACKET_TOO_LONG](#ab63f7d0c79aaa57abf59aa18e112345f)。

<a id="r_a9c62f8f73470a3157a60f8d6d56b22a4"></a>

```c
#define BT_HCI_ERR_TOO_LATE 0x46
```

相关声明：[BT_HCI_ERR_TOO_LATE](#a9c62f8f73470a3157a60f8d6d56b22a4)。

<a id="r_a8dcf345b1fea1364f490f40963992cd6"></a>

```c
#define BT_HCI_ERR_TOO_EARLY 0x47
```

相关声明：[BT_HCI_ERR_TOO_EARLY](#a8dcf345b1fea1364f490f40963992cd6)。

## 5.3\_详细说明（Detailed Documentation）

<a id="a9693358ac3b7d9da498ca557fa0d1410"></a>

### `B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MAX`

```c
#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MAX 0x52
```

<a id="a87364c12ecac6b05681469c9450f887e"></a>

### `B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MIN`

```c
#define B_HCI_LE_CTE_REPORT_SAMPLE_COUNT_MIN 0x9
```

<a id="a2f9e6232229ae1bed3d835b5f6531a76"></a>

### `BT_ACL_BROADCAST`

```c
#define BT_ACL_BROADCAST 0x01
```

<a id="ad6f24425a0818730d2377e159698922b"></a>

### `BT_ACL_COMPLETE`

```c
#define BT_ACL_COMPLETE 0x03
```

<a id="a0bfb8a0bac96eb223eb8229c1dff9e7d"></a>

### `BT_ACL_CONT`

```c
#define BT_ACL_CONT 0x01
```

<a id="a499f8647747fd6b7b82d9b3280b4b048"></a>

### `bt_acl_flags`

```c
#define bt_acl_flags ( h)
```

展开值（Value）：

```c
((h) >> 12)
```

<a id="a55cfcca3e0a6a7401e57e7430421093e"></a>

### `bt_acl_flags_bc`

```c
#define bt_acl_flags_bc ( f)
```

展开值（Value）：

```c
((f) >> 2)
```

<a id="ae358e74ce455f11bb134700ec80fe07b"></a>

### `bt_acl_flags_pb`

```c
#define bt_acl_flags_pb ( f)
```

展开值（Value）：

```c
((f) & BIT_MASK(2))
```

<a id="a500341d3485843d85dc034ce6f8a908c"></a>

### `bt_acl_handle`

```c
#define bt_acl_handle ( h)
```

展开值（Value）：

```c
((h) & BT_ACL_HANDLE_MASK)
```

<a id="a28a9f26ba563e2687856aff39b044039"></a>

### `BT_ACL_HANDLE_MASK`

```c
#define BT_ACL_HANDLE_MASK BIT_MASK(12)
```

<a id="aa08e6239d84ce55153baa41f46814363"></a>

### `bt_acl_handle_pack`

```c
#define bt_acl_handle_pack ( h, f )
```

展开值（Value）：

```c
((h) | ((f) << 12))
```

<a id="a343e6550f9a24a59c5a08efd2dab16bb"></a>

### `BT_ACL_POINT_TO_POINT`

```c
#define BT_ACL_POINT_TO_POINT 0x00
```

<a id="a49c9728293c37e718c009ad973f6d43e"></a>

### `BT_ACL_START`

```c
#define BT_ACL_START 0x02
```

<a id="ae8c5ddd450d47b45a310bc979207ebff"></a>

### `BT_ACL_START_NO_FLUSH`

```c
#define BT_ACL_START_NO_FLUSH 0x00
```

<a id="a1b6049f2e0fde604d1da02cbb66b7948"></a>

### `BT_ACTIVE_MODE`

```c
#define BT_ACTIVE_MODE 0x00
```

<a id="a19b4c20d243de28462b686088e2971a3"></a>

### `BT_BREDR_SCAN_DISABLED`

```c
#define BT_BREDR_SCAN_DISABLED 0x00
```

<a id="a2f75eaee67bbb6c0211f3146d881278f"></a>

### `BT_BREDR_SCAN_INQUIRY`

```c
#define BT_BREDR_SCAN_INQUIRY 0x01
```

<a id="a006d877a26f4e8dd0689b1324107a843"></a>

### `BT_BREDR_SCAN_PAGE`

```c
#define BT_BREDR_SCAN_PAGE 0x02
```

<a id="ae3aaad5ae408cb8c72a29ff7a8817c21"></a>

### `BT_CMD_LE_STATES`

```c
#define BT_CMD_LE_STATES ( cmd)
```

展开值（Value）：

```c
BT_CMD_TEST(cmd, 28, 3)
```

<a id="a7d5bc35e597d03fbc65084b39771cf0b"></a>

### `BT_CMD_TEST`

```c
#define BT_CMD_TEST ( cmd, octet, bit )
```

展开值（Value）：

```c
(cmd[octet] & BIT(bit))
```

<a id="a4c274cd6947d37bf4f895ca0002c4f63"></a>

### `BT_ENC_KEY_SIZE_MAX`

```c
#define BT_ENC_KEY_SIZE_MAX 0x10
```

<a id="a90a6c0c50f915c347b75ac3ca46996ac"></a>

### `BT_ENC_KEY_SIZE_MIN`

```c
#define BT_ENC_KEY_SIZE_MIN 0x07
```

<a id="a25201544478590f6ee87a829410c612b"></a>

### `BT_EVT_BIT`

```c
#define BT_EVT_BIT ( n)
```

展开值（Value）：

```c
(1ULL << (n))
```

<a id="ad4f80dd3fdf22b23d47785a507aa5a85"></a>

### `BT_EVT_MASK_AUTH_COMPLETE`

```c
#define BT_EVT_MASK_AUTH_COMPLETE BT_EVT_BIT(5)
```

<a id="a33753df12afb5f7e19be01f9febc5d23"></a>

### `BT_EVT_MASK_AUTH_PAYLOAD_TIMEOUT_EXP`

```c
#define BT_EVT_MASK_AUTH_PAYLOAD_TIMEOUT_EXP BT_EVT_BIT(23)
```

<a id="a35f42f297b980a050deceb71237883ba"></a>

### `BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE`

```c
#define BT_EVT_MASK_CL_PER_BC_CH_MAP_CHANGE BT_EVT_BIT(21)
```

<a id="aa8842138b1146d3581c39062d11a6305"></a>

### `BT_EVT_MASK_CL_PER_BC_RX`

```c
#define BT_EVT_MASK_CL_PER_BC_RX BT_EVT_BIT(17)
```

<a id="af513eaa35861cfcfefba97e0263e3f5b"></a>

### `BT_EVT_MASK_CL_PER_BC_TIMEOUT`

```c
#define BT_EVT_MASK_CL_PER_BC_TIMEOUT BT_EVT_BIT(18)
```

<a id="a5a13adda8bf4f015550a043667e0b67d"></a>

### `BT_EVT_MASK_CONN_COMPLETE`

```c
#define BT_EVT_MASK_CONN_COMPLETE BT_EVT_BIT(2)
```

<a id="ada3fa58cfba4324ae9f3baa7661b6808"></a>

### `BT_EVT_MASK_CONN_PKT_TYPE_CHANGED`

```c
#define BT_EVT_MASK_CONN_PKT_TYPE_CHANGED BT_EVT_BIT(28)
```

连接分组类型已改变事件（Connection Packet Type Changed Event）的事件掩码位（Event Mask Bit）。

<a id="ad77bbcd4fb8b0e37700492e8a3cccd38"></a>

### `BT_EVT_MASK_CONN_REQUEST`

```c
#define BT_EVT_MASK_CONN_REQUEST BT_EVT_BIT(3)
```

<a id="a829ea33c603291d331faba58689b0198"></a>

### `BT_EVT_MASK_DATA_BUFFER_OVERFLOW`

```c
#define BT_EVT_MASK_DATA_BUFFER_OVERFLOW BT_EVT_BIT(25)
```

<a id="a5ea9d4fb977c660bc33be93c73817705"></a>

### `BT_EVT_MASK_DISCONN_COMPLETE`

```c
#define BT_EVT_MASK_DISCONN_COMPLETE BT_EVT_BIT(4)
```

<a id="a334c571248a1aad285bb11bc39d2ade8"></a>

### `BT_EVT_MASK_ENCRYPT_CHANGE`

```c
#define BT_EVT_MASK_ENCRYPT_CHANGE BT_EVT_BIT(7)
```

<a id="af8d96cc1cf99a7130d4c181450998cb7"></a>

### `BT_EVT_MASK_ENCRYPT_KEY_REFRESH_COMPLETE`

```c
#define BT_EVT_MASK_ENCRYPT_KEY_REFRESH_COMPLETE BT_EVT_BIT(47)
```

<a id="a9b361fe6314f56fcb016bacb064af815"></a>

### `BT_EVT_MASK_EXTENDED_INQUIRY_RESULT`

```c
#define BT_EVT_MASK_EXTENDED_INQUIRY_RESULT BT_EVT_BIT(46)
```

<a id="a079c00e59422034a9f977af7dd20234c"></a>

### `BT_EVT_MASK_HARDWARE_ERROR`

```c
#define BT_EVT_MASK_HARDWARE_ERROR BT_EVT_BIT(15)
```

<a id="a79851cd962916f9be81e29ce9797e901"></a>

### `BT_EVT_MASK_INQUIRY_COMPLETE`

```c
#define BT_EVT_MASK_INQUIRY_COMPLETE BT_EVT_BIT(0)
```

<a id="aeb5b4cbc01a8cebea5ce8e0090d37261"></a>

### `BT_EVT_MASK_INQUIRY_RESULT_WITH_RSSI`

```c
#define BT_EVT_MASK_INQUIRY_RESULT_WITH_RSSI BT_EVT_BIT(33)
```

<a id="ae8106016a80e123016c6d2fc406224d7"></a>

### `BT_EVT_MASK_INQUIRY_RSP_NOT`

```c
#define BT_EVT_MASK_INQUIRY_RSP_NOT BT_EVT_BIT(22)
```

<a id="a845de3735dc3989d3a9d54cf5e55b408"></a>

### `BT_EVT_MASK_IO_CAPA_REQ`

```c
#define BT_EVT_MASK_IO_CAPA_REQ BT_EVT_BIT(48)
```

<a id="a409e33dbe4fdb1dc90050e0b4eab1f86"></a>

### `BT_EVT_MASK_IO_CAPA_RESP`

```c
#define BT_EVT_MASK_IO_CAPA_RESP BT_EVT_BIT(49)
```

<a id="a11330b1b6847d77d3ba88e1de0aaa36e"></a>

### `BT_EVT_MASK_LE_ADV_SET_TERMINATED`

```c
#define BT_EVT_MASK_LE_ADV_SET_TERMINATED BT_EVT_BIT(17)
```

<a id="a39a55a4c3e71db708e39c8110a2349f7"></a>

### `BT_EVT_MASK_LE_ADVERTISING_REPORT`

```c
#define BT_EVT_MASK_LE_ADVERTISING_REPORT BT_EVT_BIT(1)
```

<a id="a447ff4a3e4dfba390ce9729e45abb410"></a>

### `BT_EVT_MASK_LE_BIG_COMPLETE`

```c
#define BT_EVT_MASK_LE_BIG_COMPLETE BT_EVT_BIT(26)
```

<a id="ab88b8bcde1d07b5f16c55c4cbf4fd20d"></a>

### `BT_EVT_MASK_LE_BIG_SYNC_ESTABLISHED`

```c
#define BT_EVT_MASK_LE_BIG_SYNC_ESTABLISHED BT_EVT_BIT(28)
```

<a id="a87abdedde8bd43f845fe604c80612ca0"></a>

### `BT_EVT_MASK_LE_BIG_SYNC_LOST`

```c
#define BT_EVT_MASK_LE_BIG_SYNC_LOST BT_EVT_BIT(29)
```

<a id="ad4b775d48bfa14c00c78ac1fbb8f2a2a"></a>

### `BT_EVT_MASK_LE_BIG_TERMINATED`

```c
#define BT_EVT_MASK_LE_BIG_TERMINATED BT_EVT_BIT(27)
```

<a id="aff9c37de1e55e6a7085b3a521f34d3e0"></a>

### `BT_EVT_MASK_LE_BIGINFO_ADV_REPORT`

```c
#define BT_EVT_MASK_LE_BIGINFO_ADV_REPORT BT_EVT_BIT(33)
```

<a id="acee0428356c4853fe664709fc1675f02"></a>

### `BT_EVT_MASK_LE_CHAN_SEL_ALGO`

```c
#define BT_EVT_MASK_LE_CHAN_SEL_ALGO BT_EVT_BIT(19)
```

<a id="a9e41b4cb965576490fb39f7dc396722f"></a>

### `BT_EVT_MASK_LE_CIS_ESTABLISHED`

```c
#define BT_EVT_MASK_LE_CIS_ESTABLISHED BT_EVT_BIT(24)
```

<a id="a1b02618f1fbfb3a710fd413f205da9a6"></a>

### `BT_EVT_MASK_LE_CIS_ESTABLISHED_V2`

```c
#define BT_EVT_MASK_LE_CIS_ESTABLISHED_V2 BT_EVT_BIT(41)
```

<a id="aa24e9569ace049098a6d822ad7433e26"></a>

### `BT_EVT_MASK_LE_CIS_REQ`

```c
#define BT_EVT_MASK_LE_CIS_REQ BT_EVT_BIT(25)
```

<a id="a59cd7a15e5b562adb6397509463e375c"></a>

### `BT_EVT_MASK_LE_CONN_COMPLETE`

```c
#define BT_EVT_MASK_LE_CONN_COMPLETE BT_EVT_BIT(0)
```

<a id="ac3eeaa0610a6ac6d3b57880042071f2a"></a>

### `BT_EVT_MASK_LE_CONN_PARAM_REQ`

```c
#define BT_EVT_MASK_LE_CONN_PARAM_REQ BT_EVT_BIT(5)
```

<a id="ae912b6f8f2d8a3057cc8327106098475"></a>

### `BT_EVT_MASK_LE_CONN_RATE_CHANGE`

```c
#define BT_EVT_MASK_LE_CONN_RATE_CHANGE BT_EVT_BIT(54)
```

<a id="ab1988671f4017f6434dc0438b2e8b9f6"></a>

### `BT_EVT_MASK_LE_CONN_UPDATE_COMPLETE`

```c
#define BT_EVT_MASK_LE_CONN_UPDATE_COMPLETE BT_EVT_BIT(2)
```

<a id="a3b2f133db5641414b95bfd953d715ff3"></a>

### `BT_EVT_MASK_LE_CONNECTION_IQ_REPORT`

```c
#define BT_EVT_MASK_LE_CONNECTION_IQ_REPORT BT_EVT_BIT(21)
```

<a id="a6ef13decc171530c00f12b0226fa9ed1"></a>

### `BT_EVT_MASK_LE_CONNECTIONLESS_IQ_REPORT`

```c
#define BT_EVT_MASK_LE_CONNECTIONLESS_IQ_REPORT BT_EVT_BIT(20)
```

<a id="abe6f94ab4bae0d34f23e27c0948e3a21"></a>

### `BT_EVT_MASK_LE_CS_CONFIG_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_CONFIG_COMPLETE BT_EVT_BIT(46)
```

<a id="affbe9c98cf94e50673a2a59c8fb68256"></a>

### `BT_EVT_MASK_LE_CS_PROCEDURE_ENABLE_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_PROCEDURE_ENABLE_COMPLETE BT_EVT_BIT(47)
```

<a id="a406cdb92d8c6524aca8971425bab7baa"></a>

### `BT_EVT_MASK_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE BT_EVT_BIT(44)
```

<a id="a97d1b704b1638fb85fa4da6f6d31e209"></a>

### `BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE BT_EVT_BIT(43)
```

<a id="aa311f47eecf45fa72cc0b07bb839c4db"></a>

### `BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2`

```c
#define BT_EVT_MASK_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 BT_EVT_BIT(55)
```

低功耗蓝牙信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete，v2）的事件掩码。

<a id="a07b9cc5a2fcc73d56590a034977cf3a0"></a>

### `BT_EVT_MASK_LE_CS_SECURITY_ENABLE_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_SECURITY_ENABLE_COMPLETE BT_EVT_BIT(45)
```

<a id="a040ef537fe66f923dc3c344fee023002"></a>

### `BT_EVT_MASK_LE_CS_SUBEVENT_RESULT`

```c
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT BT_EVT_BIT(48)
```

<a id="a226c276713e3cf16108e4a66fad6db79"></a>

### `BT_EVT_MASK_LE_CS_SUBEVENT_RESULT_CONTINUE`

```c
#define BT_EVT_MASK_LE_CS_SUBEVENT_RESULT_CONTINUE BT_EVT_BIT(49)
```

<a id="a8a6ec9510323355aa003cb8be519be7d"></a>

### `BT_EVT_MASK_LE_CS_TEST_END_COMPLETE`

```c
#define BT_EVT_MASK_LE_CS_TEST_END_COMPLETE BT_EVT_BIT(50)
```

<a id="afbd3991be814ec6462d62fbc4c898ac0"></a>

### `BT_EVT_MASK_LE_CTE_REQUEST_FAILED`

```c
#define BT_EVT_MASK_LE_CTE_REQUEST_FAILED BT_EVT_BIT(22)
```

<a id="a73489ce7067d812e8443e242ee53a5e6"></a>

### `BT_EVT_MASK_LE_DATA_LEN_CHANGE`

```c
#define BT_EVT_MASK_LE_DATA_LEN_CHANGE BT_EVT_BIT(6)
```

<a id="a3e84268b1e701ae37c77e95847490222"></a>

### `BT_EVT_MASK_LE_DIRECT_ADV_REPORT`

```c
#define BT_EVT_MASK_LE_DIRECT_ADV_REPORT BT_EVT_BIT(10)
```

<a id="afb3b477cb835e60c3e77237451ebae5b"></a>

### `BT_EVT_MASK_LE_ENH_CONN_COMPLETE`

```c
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE BT_EVT_BIT(9)
```

<a id="a8b40a701334d25741a6e17ffd86576ad"></a>

### `BT_EVT_MASK_LE_ENH_CONN_COMPLETE_V2`

```c
#define BT_EVT_MASK_LE_ENH_CONN_COMPLETE_V2 BT_EVT_BIT(40)
```

<a id="a1d7fc1a3ea229622560de8cf0bb63a81"></a>

### `BT_EVT_MASK_LE_EXT_ADVERTISING_REPORT`

```c
#define BT_EVT_MASK_LE_EXT_ADVERTISING_REPORT BT_EVT_BIT(12)
```

<a id="ab92e0f5db4474e451285314f90b05e59"></a>

### `BT_EVT_MASK_LE_FRAME_SPACE_UPDATE_COMPLETE`

```c
#define BT_EVT_MASK_LE_FRAME_SPACE_UPDATE_COMPLETE BT_EVT_BIT(52)
```

<a id="afbe64037a16680397614ba2db136b452"></a>

### `BT_EVT_MASK_LE_GENERATE_DHKEY_COMPLETE`

```c
#define BT_EVT_MASK_LE_GENERATE_DHKEY_COMPLETE BT_EVT_BIT(8)
```

<a id="ab495948af67d01208eff1adb9a33e489"></a>

### `BT_EVT_MASK_LE_LTK_REQUEST`

```c
#define BT_EVT_MASK_LE_LTK_REQUEST BT_EVT_BIT(4)
```

<a id="a59f89d39350b396f8d0c986e2d477bba"></a>

### `BT_EVT_MASK_LE_META_EVENT`

```c
#define BT_EVT_MASK_LE_META_EVENT BT_EVT_BIT(61)
```

<a id="a281d70b2b596b918972b59e684b6a476"></a>

### `BT_EVT_MASK_LE_P256_PUBLIC_KEY_COMPLETE`

```c
#define BT_EVT_MASK_LE_P256_PUBLIC_KEY_COMPLETE BT_EVT_BIT(7)
```

<a id="a5b2139ce8847bfcdbcd99c3241fb5ea2"></a>

### `BT_EVT_MASK_LE_PAST_RECEIVED`

```c
#define BT_EVT_MASK_LE_PAST_RECEIVED BT_EVT_BIT(23)
```

<a id="a93aec31c1636fec90b609981736eb2de"></a>

### `BT_EVT_MASK_LE_PAST_RECEIVED_V2`

```c
#define BT_EVT_MASK_LE_PAST_RECEIVED_V2 BT_EVT_BIT(37)
```

<a id="a6aad398435aa48ba67f6917bca2a690e"></a>

### `BT_EVT_MASK_LE_PATH_LOSS_THRESHOLD`

```c
#define BT_EVT_MASK_LE_PATH_LOSS_THRESHOLD BT_EVT_BIT(31)
```

<a id="ab8a9486fedec169e4d44b249f2445acf"></a>

### `BT_EVT_MASK_LE_PER_ADV_RESPONSE_REPORT`

```c
#define BT_EVT_MASK_LE_PER_ADV_RESPONSE_REPORT BT_EVT_BIT(39)
```

<a id="af0e2c2e66bdac52fbe5e9c91ca26fe49"></a>

### `BT_EVT_MASK_LE_PER_ADV_SUBEVENT_DATA_REQ`

```c
#define BT_EVT_MASK_LE_PER_ADV_SUBEVENT_DATA_REQ BT_EVT_BIT(38)
```

<a id="a96142f5d79029a93a99152ade46fc005"></a>

### `BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED`

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED BT_EVT_BIT(13)
```

<a id="a92a360ad268c29e1616de1e16748eb44"></a>

### `BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED_V2`

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_ESTABLISHED_V2 BT_EVT_BIT(35)
```

<a id="ae78587797f24987f36c348fe790438b2"></a>

### `BT_EVT_MASK_LE_PER_ADV_SYNC_LOST`

```c
#define BT_EVT_MASK_LE_PER_ADV_SYNC_LOST BT_EVT_BIT(15)
```

<a id="ad7fc62afd0e1e3dc040567d91320e18e"></a>

### `BT_EVT_MASK_LE_PER_ADVERTISING_REPORT`

```c
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT BT_EVT_BIT(14)
```

<a id="ad78d5a027581dee52c54bb3f5a19b68d"></a>

### `BT_EVT_MASK_LE_PER_ADVERTISING_REPORT_V2`

```c
#define BT_EVT_MASK_LE_PER_ADVERTISING_REPORT_V2 BT_EVT_BIT(36)
```

<a id="ab5f6014468b107486aba04ba698453ed"></a>

### `BT_EVT_MASK_LE_PHY_UPDATE_COMPLETE`

```c
#define BT_EVT_MASK_LE_PHY_UPDATE_COMPLETE BT_EVT_BIT(11)
```

<a id="a53be462853189607e7733d1131df556f"></a>

### `BT_EVT_MASK_LE_READ_ALL_REMOTE_FEAT_COMPLETE`

```c
#define BT_EVT_MASK_LE_READ_ALL_REMOTE_FEAT_COMPLETE BT_EVT_BIT(42)
```

<a id="adba1a3a872ee26a41218c9104e9f957b"></a>

### `BT_EVT_MASK_LE_REMOTE_FEAT_COMPLETE`

```c
#define BT_EVT_MASK_LE_REMOTE_FEAT_COMPLETE BT_EVT_BIT(3)
```

<a id="a01e518d3bb3d4f99c335743362a84080"></a>

### `BT_EVT_MASK_LE_REQ_PEER_SCA_COMPLETE`

```c
#define BT_EVT_MASK_LE_REQ_PEER_SCA_COMPLETE BT_EVT_BIT(30)
```

<a id="a3f13865e913a1c6afb6d8d05a6d84608"></a>

### `BT_EVT_MASK_LE_SCAN_REQ_RECEIVED`

```c
#define BT_EVT_MASK_LE_SCAN_REQ_RECEIVED BT_EVT_BIT(18)
```

<a id="a372f6b8e355972d63e5f9ff45a486e9d"></a>

### `BT_EVT_MASK_LE_SCAN_TIMEOUT`

```c
#define BT_EVT_MASK_LE_SCAN_TIMEOUT BT_EVT_BIT(16)
```

<a id="a8a52784fd872a8ee6f666c31e846411d"></a>

### `BT_EVT_MASK_LE_SUBRATE_CHANGE`

```c
#define BT_EVT_MASK_LE_SUBRATE_CHANGE BT_EVT_BIT(34)
```

<a id="a7f9d3cdf0de067ad408bec600b9a691f"></a>

### `BT_EVT_MASK_LE_TRANSMIT_POWER_REPORTING`

```c
#define BT_EVT_MASK_LE_TRANSMIT_POWER_REPORTING BT_EVT_BIT(32)
```

<a id="aa20a3ce217a60070826d0b55ebd105be"></a>

### `BT_EVT_MASK_LINK_KEY_NOTIFY`

```c
#define BT_EVT_MASK_LINK_KEY_NOTIFY BT_EVT_BIT(23)
```

<a id="a1e16ab7caf239e804c0c2057e9b49e42"></a>

### `BT_EVT_MASK_LINK_KEY_REQ`

```c
#define BT_EVT_MASK_LINK_KEY_REQ BT_EVT_BIT(22)
```

<a id="a17cdf232094d1eaee9b847fb3d096c79"></a>

### `BT_EVT_MASK_MODE_CHANGE`

```c
#define BT_EVT_MASK_MODE_CHANGE BT_EVT_BIT(19)
```

<a id="abe39e63cbdee9bfeac36a1b6a4d40aba"></a>

### `BT_EVT_MASK_NUM_COMPLETE_DATA_BLOCKS`

```c
#define BT_EVT_MASK_NUM_COMPLETE_DATA_BLOCKS BT_EVT_BIT(8)
```

<a id="ad078befa197baac20294dc0d46eff9dd"></a>

### `BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT`

```c
#define BT_EVT_MASK_PER_PAGE_RSP_TIMEOUT BT_EVT_BIT(20)
```

<a id="a9f5612d89848aafb6e9063a55e5cd6b4"></a>

### `BT_EVT_MASK_PIN_CODE_REQ`

```c
#define BT_EVT_MASK_PIN_CODE_REQ BT_EVT_BIT(21)
```

<a id="a9d3bbaa1eb1dbe72714b922dcada3347"></a>

### `BT_EVT_MASK_REMOTE_EXT_FEATURES`

```c
#define BT_EVT_MASK_REMOTE_EXT_FEATURES BT_EVT_BIT(34)
```

<a id="a7ccade60a01e0f8a175b3b11b5e20f6d"></a>

### `BT_EVT_MASK_REMOTE_FEATURES`

```c
#define BT_EVT_MASK_REMOTE_FEATURES BT_EVT_BIT(10)
```

<a id="a4433027483d6d63911b59c4fe605ba69"></a>

### `BT_EVT_MASK_REMOTE_NAME_REQ_COMPLETE`

```c
#define BT_EVT_MASK_REMOTE_NAME_REQ_COMPLETE BT_EVT_BIT(6)
```

<a id="a87331cabdea78ace1577cbf2fa7e3523"></a>

### `BT_EVT_MASK_REMOTE_VERSION_INFO`

```c
#define BT_EVT_MASK_REMOTE_VERSION_INFO BT_EVT_BIT(11)
```

<a id="a4b4a80b51b2c20bf28fbfac57679a86e"></a>

### `BT_EVT_MASK_ROLE_CHANGE`

```c
#define BT_EVT_MASK_ROLE_CHANGE BT_EVT_BIT(17)
```

<a id="a8bfac36e993c48d12bdeb7c130fdd6dc"></a>

### `BT_EVT_MASK_SAM_STATUS_CHANGE`

```c
#define BT_EVT_MASK_SAM_STATUS_CHANGE BT_EVT_BIT(24)
```

<a id="a6a08ace148ea2728614a3bab02c21f65"></a>

### `BT_EVT_MASK_SSP_COMPLETE`

```c
#define BT_EVT_MASK_SSP_COMPLETE BT_EVT_BIT(53)
```

<a id="a4f1a905136cb713c09fb5197dd099ce2"></a>

### `BT_EVT_MASK_SYNC_CONN_COMPLETE`

```c
#define BT_EVT_MASK_SYNC_CONN_COMPLETE BT_EVT_BIT(43)
```

<a id="ac078d5b46d7e227726cb7456e2163d3f"></a>

### `BT_EVT_MASK_SYNCH_TRAIN_COMPLETE`

```c
#define BT_EVT_MASK_SYNCH_TRAIN_COMPLETE BT_EVT_BIT(15)
```

<a id="a8901b477ec3584af207b3648b221bb92"></a>

### `BT_EVT_MASK_SYNCH_TRAIN_RX`

```c
#define BT_EVT_MASK_SYNCH_TRAIN_RX BT_EVT_BIT(16)
```

<a id="aff43216feb0c29c6813d198473f34fdc"></a>

### `BT_EVT_MASK_TRIGG_CLOCK_CAPTURE`

```c
#define BT_EVT_MASK_TRIGG_CLOCK_CAPTURE BT_EVT_BIT(14)
```

<a id="a9b82f06f42651c32f4c0db9826002134"></a>

### `BT_EVT_MASK_TRUNC_PAGE_COMPLETE`

```c
#define BT_EVT_MASK_TRUNC_PAGE_COMPLETE BT_EVT_BIT(19)
```

<a id="a1c04cc7d04f056e5edfc4ddaa97c657f"></a>

### `BT_EVT_MASK_USER_CONFIRM_REQ`

```c
#define BT_EVT_MASK_USER_CONFIRM_REQ BT_EVT_BIT(50)
```

<a id="a2eb47347a5685a290087b236d696971e"></a>

### `BT_EVT_MASK_USER_PASSKEY_NOTIFY`

```c
#define BT_EVT_MASK_USER_PASSKEY_NOTIFY BT_EVT_BIT(58)
```

<a id="af56d87ffc24c2e4c08db68ab019fd58e"></a>

### `BT_EVT_MASK_USER_PASSKEY_REQ`

```c
#define BT_EVT_MASK_USER_PASSKEY_REQ BT_EVT_BIT(51)
```

<a id="a8dbbf37965a9d0ddab5a07f88d7cd7ca"></a>

### `BT_FEAT_2EV3_PKT`

```c
#define BT_FEAT_2EV3_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 5, 5)
```

<a id="a00aec89aa4d1504934e85ec79462b346"></a>

### `BT_FEAT_3EV3_PKT`

```c
#define BT_FEAT_3EV3_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 5, 6)
```

<a id="a5219ff658b46cf28104a99f089854444"></a>

### `BT_FEAT_3SLOT_PKT`

```c
#define BT_FEAT_3SLOT_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 5, 7)
```

<a id="a5508c481ff6b8fd46f2f2c077aaa90c9"></a>

### `BT_FEAT_BREDR`

```c
#define BT_FEAT_BREDR ( feat)
```

展开值（Value）：

```c
!BT_FEAT_TEST(feat, 0, 4, 5)
```

<a id="ad154d0649e8e90c1102b74cae8327fa7"></a>

### `BT_FEAT_EV4_PKT`

```c
#define BT_FEAT_EV4_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 4, 0)
```

<a id="a0a6b9afb4673dc852e1a4d8e867003c9"></a>

### `BT_FEAT_EV5_PKT`

```c
#define BT_FEAT_EV5_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 4, 1)
```

<a id="ac26ebac4f1641d5ff4484f74579852d7"></a>

### `BT_FEAT_EXT_FEATURES`

```c
#define BT_FEAT_EXT_FEATURES ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 7, 7)
```

<a id="af011519b6fb0477ac7f87e5dc98daed0"></a>

### `BT_FEAT_HOST_SSP`

```c
#define BT_FEAT_HOST_SSP ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 1, 0, 0)
```

<a id="ad59c138e945d7f27d3befc286b679e03"></a>

### `BT_FEAT_HV2_PKT`

```c
#define BT_FEAT_HV2_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 1, 4)
```

<a id="aed6f11d60161c919b4d2b7eb13f46e47"></a>

### `BT_FEAT_HV3_PKT`

```c
#define BT_FEAT_HV3_PKT ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 1, 5)
```

<a id="a8b1df8d6b9e0dfcaa13635588cc3bfe3"></a>

### `BT_FEAT_LE`

```c
#define BT_FEAT_LE ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 4, 6)
```

<a id="af10735230c38d2b5a0baf5377212e827"></a>

### `BT_FEAT_LE_ADV_CODING_SEL`

```c
#define BT_FEAT_LE_ADV_CODING_SEL ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ADV_CODING_SEL)
```

<a id="aecf06a32c61c783305ad3817f9e5a596"></a>

### `BT_FEAT_LE_ADV_CODING_SEL_HOST`

```c
#define BT_FEAT_LE_ADV_CODING_SEL_HOST ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST)
```

<a id="a1c3c0e6a213b71e680ca24738047f09a"></a>

### `BT_FEAT_LE_ANT_SWITCH_RX_AOA`

```c
#define BT_FEAT_LE_ANT_SWITCH_RX_AOA ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA)
```

<a id="ae503f9186d39fbea2347036c891fc8bf"></a>

### `BT_FEAT_LE_ANT_SWITCH_TX_AOD`

```c
#define BT_FEAT_LE_ANT_SWITCH_TX_AOD ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD)
```

<a id="a46b2f535c74178c8cc9359a7b1d2e140"></a>

### `BT_FEAT_LE_BIS`

```c
#define BT_FEAT_LE_BIS ( feat)
```

展开值（Value）：

```c
(BT_FEAT_LE_ISO_BROADCASTER(feat) | \
BT_FEAT_LE_SYNC_RECEIVER(feat))
```

<a id="abb7763cc16340d23bc7d687e60badcc0"></a>

### `BT_FEAT_LE_CHANNEL_CLASSIFICATION`

```c
#define BT_FEAT_LE_CHANNEL_CLASSIFICATION ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION)
```

<a id="a7b13b55fd2cfb4d756d3591215b47b7e"></a>

### `BT_FEAT_LE_CHANNEL_SOUNDING`

```c
#define BT_FEAT_LE_CHANNEL_SOUNDING ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CHANNEL_SOUNDING)
```

<a id="aff2b8ca285698906deecfeff7447a74a"></a>

### `BT_FEAT_LE_CHANNEL_SOUNDING_HOST`

```c
#define BT_FEAT_LE_CHANNEL_SOUNDING_HOST ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST)
```

<a id="abe5a1ddbede473f583106e3500dccdb1"></a>

### `BT_FEAT_LE_CIS`

```c
#define BT_FEAT_LE_CIS ( feat)
```

展开值（Value）：

```c
(BT_FEAT_LE_CIS_CENTRAL(feat) | \
BT_FEAT_LE_CIS_PERIPHERAL(feat))
```

<a id="adce7c3804a224e7b7317728fa27d4945"></a>

### `BT_FEAT_LE_CIS_CENTRAL`

```c
#define BT_FEAT_LE_CIS_CENTRAL ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CIS_CENTRAL)
```

<a id="a8a6860b285b3b4401021ba16f59404ce"></a>

### `BT_FEAT_LE_CIS_PERIPHERAL`

```c
#define BT_FEAT_LE_CIS_PERIPHERAL ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CIS_PERIPHERAL)
```

<a id="a554c027fb3946de6f861ea267968ba17"></a>

### `BT_FEAT_LE_CONN_PARAM_REQ_PROC`

```c
#define BT_FEAT_LE_CONN_PARAM_REQ_PROC ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONN_PARAM_REQ)
```

<a id="a75bf595ba1e16deeeedb45a55f470620"></a>

### `BT_FEAT_LE_CONN_SUBRATING`

```c
#define BT_FEAT_LE_CONN_SUBRATING ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONN_SUBRATING)
```

<a id="a37adeecbf4c200cf8b060344718e7949"></a>

### `BT_FEAT_LE_CONN_SUBRATING_HOST_SUPP`

```c
#define BT_FEAT_LE_CONN_SUBRATING_HOST_SUPP ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP)
```

<a id="a51316a5b67950e7644dfb71c4c6baa96"></a>

### `BT_FEAT_LE_CONNECTION_CTE_REQ`

```c
#define BT_FEAT_LE_CONNECTION_CTE_REQ ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONN_CTE_REQ)
```

<a id="a0cdc67a1345969d3504380fce94a4cda"></a>

### `BT_FEAT_LE_CONNECTION_CTE_RESP`

```c
#define BT_FEAT_LE_CONNECTION_CTE_RESP ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONN_CTE_RESP)
```

<a id="aeb0639a8e5cbc904d7f5c02d72375913"></a>

### `BT_FEAT_LE_CONNECTIONLESS_CTE_RX`

```c
#define BT_FEAT_LE_CONNECTIONLESS_CTE_RX ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX)
```

<a id="a81e30f5630750ce4f805748fbe14b456"></a>

### `BT_FEAT_LE_CONNECTIONLESS_CTE_TX`

```c
#define BT_FEAT_LE_CONNECTIONLESS_CTE_TX ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX)
```

<a id="a62e7d152cd9dfabf5b1420945099ecb6"></a>

### `BT_FEAT_LE_DLE`

```c
#define BT_FEAT_LE_DLE ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_DLE)
```

<a id="a51464aacf5bbcbfb873fa6c757bbcd79"></a>

### `BT_FEAT_LE_ENCR`

```c
#define BT_FEAT_LE_ENCR ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ENC)
```

<a id="a8bce94a732d28ce74ad2663e01da09b2"></a>

### `BT_FEAT_LE_EXT_ADV`

```c
#define BT_FEAT_LE_EXT_ADV ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_EXT_ADV)
```

<a id="a5d479d919db4920b7a53c054e4ae7a19"></a>

### `BT_FEAT_LE_EXT_PER_ADV`

```c
#define BT_FEAT_LE_EXT_PER_ADV ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PER_ADV)
```

<a id="ad55c1593a92a868fff376b0d2d2154ad"></a>

### `BT_FEAT_LE_EXT_SCAN`

```c
#define BT_FEAT_LE_EXT_SCAN ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_EXT_SCAN)
```

测试是否支持扩展扫描器过滤策略（Extended Scanner Filter Policies）功能。

<a id="a3d00c2d2897c0a994a136811d9e48f94"></a>

### `BT_FEAT_LE_EXTENDED_FEAT_SET`

```c
#define BT_FEAT_LE_EXTENDED_FEAT_SET ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_EXTENDED_FEAT_SET)
```

<a id="aad2c245d9c1663da7a7ce91deaa1f252"></a>

### `BT_FEAT_LE_FRAME_SPACE_UPDATE_SET`

```c
#define BT_FEAT_LE_FRAME_SPACE_UPDATE_SET ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE)
```

<a id="a7b1b490bf00af8b0bf8ecbf4ef4aaba3"></a>

### `BT_FEAT_LE_ISO`

```c
#define BT_FEAT_LE_ISO ( feat)
```

展开值（Value）：

```c
(BT_FEAT_LE_CIS(feat) | \
BT_FEAT_LE_BIS(feat))
```

<a id="a1c6fd06877a5606ae33aedc45a71f853"></a>

### `BT_FEAT_LE_ISO_BROADCASTER`

```c
#define BT_FEAT_LE_ISO_BROADCASTER ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ISO_BROADCASTER)
```

<a id="a0b24b74715fbf84c2da2dd2cbbb34605"></a>

### `BT_FEAT_LE_ISO_CHANNELS`

```c
#define BT_FEAT_LE_ISO_CHANNELS ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_ISO_CHANNELS)
```

<a id="a7a88046c26b3603a2bb8b0f2ee158b5f"></a>

### `BT_FEAT_LE_PAST_RECV`

```c
#define BT_FEAT_LE_PAST_RECV ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PAST_RECV)
```

<a id="a9e68dcf290273a4a140645c187cd7aee"></a>

### `BT_FEAT_LE_PAST_SEND`

```c
#define BT_FEAT_LE_PAST_SEND ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PAST_SEND)
```

<a id="a8d771bd34d22853f117dbbd41ef4afe5"></a>

### `BT_FEAT_LE_PATH_LOSS_MONITOR`

```c
#define BT_FEAT_LE_PATH_LOSS_MONITOR ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PATH_LOSS_MONITOR)
```

<a id="ac5d15de2be03bc837afdb33905ea40be"></a>

### `BT_FEAT_LE_PAWR_ADVERTISER`

```c
#define BT_FEAT_LE_PAWR_ADVERTISER ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PAWR_ADVERTISER)
```

<a id="a3ee6277e0e4db5e925912e8cb89269fa"></a>

### `BT_FEAT_LE_PAWR_SCANNER`

```c
#define BT_FEAT_LE_PAWR_SCANNER ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PAWR_SCANNER)
```

<a id="a6213deacc8582f14546b23331d41c3a3"></a>

### `BT_FEAT_LE_PER_ADV_ADI_SUPP`

```c
#define BT_FEAT_LE_PER_ADV_ADI_SUPP ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP)
```

<a id="a132b2561dcd4140458fb612b6e0d8b25"></a>

### `BT_FEAT_LE_PER_INIT_FEAT_XCHG`

```c
#define BT_FEAT_LE_PER_INIT_FEAT_XCHG ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG)
```

<a id="aaf11993f4938bb4894cdd317f9386fa3"></a>

### `BT_FEAT_LE_PHY_2M`

```c
#define BT_FEAT_LE_PHY_2M ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PHY_2M)
```

<a id="abb89a0bebe4046ae310b01dd27e02c99"></a>

### `BT_FEAT_LE_PHY_CODED`

```c
#define BT_FEAT_LE_PHY_CODED ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PHY_CODED)
```

<a id="a0b2781f29085a5807d0b2235c32f5173"></a>

### `BT_FEAT_LE_PRIVACY`

```c
#define BT_FEAT_LE_PRIVACY ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PRIVACY)
```

<a id="a342ce6074faa59b507cf179868e612ba"></a>

### `BT_FEAT_LE_PWR_CHG_IND`

```c
#define BT_FEAT_LE_PWR_CHG_IND ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PWR_CHG_IND)
```

<a id="a8ab0d3ca572861bb1c40191766481799"></a>

### `BT_FEAT_LE_PWR_CTRL_REQ`

```c
#define BT_FEAT_LE_PWR_CTRL_REQ ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_PWR_CTRL_REQ)
```

<a id="adf4303d47abfab3bd23080c545b77ef7"></a>

### `BT_FEAT_LE_RX_CTE`

```c
#define BT_FEAT_LE_RX_CTE ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_RX_CTE)
```

<a id="a44f515be8315ee7dded3e3aa5c47a31c"></a>

### `BT_FEAT_LE_SHORTER_CONN_INTERVALS`

```c
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS)
```

<a id="ac968c22e86f5b45fa10d109d47a1de33"></a>

### `BT_FEAT_LE_SHORTER_CONN_INTERVALS_HOST_SUPP`

```c
#define BT_FEAT_LE_SHORTER_CONN_INTERVALS_HOST_SUPP ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP)
```

<a id="af33c8331e204eeee2a7a02e2ad46c7a2"></a>

### `BT_FEAT_LE_SYNC_RECEIVER`

```c
#define BT_FEAT_LE_SYNC_RECEIVER ( feat)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(feat, \
BT_LE_FEAT_BIT_SYNC_RECEIVER)
```

<a id="a7622a2fc0a65f82a827ab3cc84e4e7c5"></a>

### `BT_FEAT_LMP_ESCO_CAPABLE`

```c
#define BT_FEAT_LMP_ESCO_CAPABLE ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 3, 7)
```

<a id="a24f24640d9f52adb15336a1b17122346"></a>

### `BT_FEAT_LMP_SCO_CAPABLE`

```c
#define BT_FEAT_LMP_SCO_CAPABLE ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 0, 1, 3)
```

<a id="a9ecf892ec94af8cbfd2e6c99310b1fa2"></a>

### `BT_FEAT_SC`

```c
#define BT_FEAT_SC ( feat)
```

展开值（Value）：

```c
BT_FEAT_TEST(feat, 2, 1, 0)
```

<a id="a41e5b49e645ed511340a61f843f6b238"></a>

### `BT_FEAT_TEST`

```c
#define BT_FEAT_TEST ( feat, page, octet, bit )
```

展开值（Value）：

```c
((feat[page][octet] & BIT(bit)) != 0)
```

<a id="afee2289cd70b50f888518fd0b6b3f559"></a>

### `BT_HCI_ACL`

```c
#define BT_HCI_ACL 0x01
```

<a id="a7418d845532d6b077a9695454fa65bc5"></a>

### `BT_HCI_ACL_HDR_SIZE`

```c
#define BT_HCI_ACL_HDR_SIZE 4
```

<a id="acc6b2545c83736d1b538e6c81d1f095c"></a>

### `BT_HCI_ACL_PKT_TYPE_BR_MASK`

```c
#define BT_HCI_ACL_PKT_TYPE_BR_MASK
```

展开值（Value）：

```c
(BT_HCI_ACL_PKT_TYPE_DM1 | BT_HCI_ACL_PKT_TYPE_DH1 | \
 BT_HCI_ACL_PKT_TYPE_DM3 | BT_HCI_ACL_PKT_TYPE_DH3 | \
 BT_HCI_ACL_PKT_TYPE_DM5 | BT_HCI_ACL_PKT_TYPE_DH5)
```

所有基本速率（Basic Rate，BR）ACL 分组类型的位掩码（Bitmask）。

<a id="ac0fe269d4e2d7f3794456f9a65e68113"></a>

### `BT_HCI_ACL_PKT_TYPE_DH1`

```c
#define BT_HCI_ACL_PKT_TYPE_DH1 BIT(4)
```

可以使用 `DH1`。

<a id="a972f90f9bfbf7b53d4f71f04d4c82ed5"></a>

### `BT_HCI_ACL_PKT_TYPE_DH3`

```c
#define BT_HCI_ACL_PKT_TYPE_DH3 BIT(11)
```

可以使用 `DH3`。

<a id="af4f275468c7d3266107587793a6be7c6"></a>

### `BT_HCI_ACL_PKT_TYPE_DH5`

```c
#define BT_HCI_ACL_PKT_TYPE_DH5 BIT(15)
```

可以使用 `DH5`。

<a id="aa677b6c5357585d36d81f0ea831e7568"></a>

### `BT_HCI_ACL_PKT_TYPE_DM1`

```c
#define BT_HCI_ACL_PKT_TYPE_DM1 BIT(3)
```

可以使用 `DM1`。

<a id="a72b4b642556556b959d6f9eda2a70770"></a>

### `BT_HCI_ACL_PKT_TYPE_DM3`

```c
#define BT_HCI_ACL_PKT_TYPE_DM3 BIT(10)
```

可以使用 `DM3`。

<a id="a23f80a9369c84786bff1330a4b07c3e7"></a>

### `BT_HCI_ACL_PKT_TYPE_DM5`

```c
#define BT_HCI_ACL_PKT_TYPE_DM5 BIT(14)
```

可以使用 `DM5`。

<a id="ad7f6d9b786df4e2c8bca9b47bd5f6390"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_2DH1`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH1 BIT(1)
```

不得使用 `2-DH1`。

<a id="adfc95ea6f5e2cc80af74138b27fae4b6"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_2DH3`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH3 BIT(8)
```

不得使用 `2-DH3`。

<a id="ac75dba319c7875bbac25a3018bda5802"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_2DH5`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_2DH5 BIT(12)
```

不得使用 `2-DH5`。

<a id="a37863121200c9fbcbc9b61748909c796"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_3DH1`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH1 BIT(2)
```

不得使用 `3-DH1`。

<a id="abc26caf516ecfc413820e6bf0991010b"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_3DH3`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH3 BIT(9)
```

不得使用 `3-DH3`。

<a id="a09023927fff243b8d2cc4c5223b42dca"></a>

### `BT_HCI_ACL_PKT_TYPE_NO_3DH5`

```c
#define BT_HCI_ACL_PKT_TYPE_NO_3DH5 BIT(13)
```

不得使用 `3-DH5`。

<a id="a017742ee92c9ed7b80b41f339394f1e4"></a>

### `BT_HCI_ADDR_RES_DISABLE`

```c
#define BT_HCI_ADDR_RES_DISABLE 0x00
```

<a id="a61e677658b5a730b13869ebc0dbbffbe"></a>

### `BT_HCI_ADDR_RES_ENABLE`

```c
#define BT_HCI_ADDR_RES_ENABLE 0x01
```

<a id="afaecb8d6be1b1c0ce98db7edd8bad343"></a>

### `BT_HCI_ADV_DIRECT_IND`

```c
#define BT_HCI_ADV_DIRECT_IND 0x01
```

<a id="a67c1c0c5349b2de661030138185d7b0d"></a>

### `BT_HCI_ADV_DIRECT_IND_LOW_DUTY`

```c
#define BT_HCI_ADV_DIRECT_IND_LOW_DUTY 0x04
```

<a id="aa85640ad3a1aa78cf862a5d8b2567fa1"></a>

### `BT_HCI_ADV_HANDLE_INVALID`

```c
#define BT_HCI_ADV_HANDLE_INVALID 0xff
```

<a id="a338499e51470b8910e9f663be8f55db5"></a>

### `BT_HCI_ADV_IND`

```c
#define BT_HCI_ADV_IND 0x00
```

<a id="a48e13ce185bf9612455c49484ff80bb9"></a>

### `BT_HCI_ADV_NONCONN_IND`

```c
#define BT_HCI_ADV_NONCONN_IND 0x03
```

<a id="ae94df1ac3bc14f42be1207531872104a"></a>

### `BT_HCI_ADV_SCAN_IND`

```c
#define BT_HCI_ADV_SCAN_IND 0x02
```

<a id="afb3e678c87b81f9348749f1c5721ce26"></a>

### `BT_HCI_ADV_SCAN_RSP`

```c
#define BT_HCI_ADV_SCAN_RSP 0x04
```

<a id="acdf2b6de1459a7492415a8987ad9a896"></a>

### `BT_HCI_CMD_HDR_SIZE`

```c
#define BT_HCI_CMD_HDR_SIZE 3
```

<a id="a89eeffc2f46c776ecdb5eea81cb1f47a"></a>

### `BT_HCI_CODEC_TRANSPORT_MASK_BREDR_ACL`

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_ACL BIT(0)
```

<a id="ab50b70f27bd9beb4da6fe8d4b91398c1"></a>

### `BT_HCI_CODEC_TRANSPORT_MASK_BREDR_SCO`

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_BREDR_SCO BIT(1)
```

<a id="a7d90fc1df2260a4067c3eb4ab169c406"></a>

### `BT_HCI_CODEC_TRANSPORT_MASK_LE_BIS`

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_BIS BIT(3)
```

<a id="a38dd1118554de13f3f6f2853900212c5"></a>

### `BT_HCI_CODEC_TRANSPORT_MASK_LE_CIS`

```c
#define BT_HCI_CODEC_TRANSPORT_MASK_LE_CIS BIT(2)
```

<a id="a36f18d10467a580e9864eb8629b8ce01"></a>

### `BT_HCI_CODING_FORMAT_ALAW_LOG`

```c
#define BT_HCI_CODING_FORMAT_ALAW_LOG 0x01
```

<a id="a80dc369e54038df30f44ca4c13ee14d6"></a>

### `BT_HCI_CODING_FORMAT_CVSD`

```c
#define BT_HCI_CODING_FORMAT_CVSD 0x02
```

<a id="a405e22871772b5155f99774178e4093d"></a>

### `BT_HCI_CODING_FORMAT_G729A`

```c
#define BT_HCI_CODING_FORMAT_G729A 0x07
```

<a id="a1fa62d6f28ef56ebe9c18d5ab86fbf8e"></a>

### `BT_HCI_CODING_FORMAT_LC3`

```c
#define BT_HCI_CODING_FORMAT_LC3 0x06
```

<a id="a2630de3f8cc3ccc3d81f0f2fa4084587"></a>

### `BT_HCI_CODING_FORMAT_LINEAR_PCM`

```c
#define BT_HCI_CODING_FORMAT_LINEAR_PCM 0x04
```

<a id="a9178f80b7783c9cffb4574667d3033af"></a>

### `BT_HCI_CODING_FORMAT_MSBC`

```c
#define BT_HCI_CODING_FORMAT_MSBC 0x05
```

<a id="ad93af498e2265c180a01055eca2a4de0"></a>

### `BT_HCI_CODING_FORMAT_TRANSPARENT`

```c
#define BT_HCI_CODING_FORMAT_TRANSPARENT 0x03
```

<a id="a4f4939e7fa43ab73861f64d25b6549d8"></a>

### `BT_HCI_CODING_FORMAT_ULAW_LOG`

```c
#define BT_HCI_CODING_FORMAT_ULAW_LOG 0x00
```

<a id="a46839c453b81e80fb8e578f89dc31864"></a>

### `BT_HCI_CODING_FORMAT_VS`

```c
#define BT_HCI_CODING_FORMAT_VS 0xFF
```

<a id="a5e0814f9ca6e7fbc78b0778634ff075d"></a>

### `BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE`

```c
#define BT_HCI_CTE_REQ_STATUS_RSP_WITHOUT_CTE 0x0
```

<a id="a252ef06a33818e117fc7f8146413cbd0"></a>

### `BT_HCI_CTL_TO_HOST_FLOW_DISABLE`

```c
#define BT_HCI_CTL_TO_HOST_FLOW_DISABLE 0x00
```

<a id="a4231ce6514091008191d5843b2c0b452"></a>

### `BT_HCI_CTL_TO_HOST_FLOW_ENABLE`

```c
#define BT_HCI_CTL_TO_HOST_FLOW_ENABLE 0x01
```

<a id="af8d89c712a3d27f9b6f92a31bea2a8c3"></a>

### `BT_HCI_DATAPATH_DIR_CTLR_TO_HOST`

```c
#define BT_HCI_DATAPATH_DIR_CTLR_TO_HOST 0x01
```

<a id="a0f74c19fabbcb3088e1a819d33a05a1c"></a>

### `BT_HCI_DATAPATH_DIR_HOST_TO_CTLR`

```c
#define BT_HCI_DATAPATH_DIR_HOST_TO_CTLR 0x00
```

<a id="a5f748cb264265b9fc12f146ba47fa14c"></a>

### `BT_HCI_DATAPATH_ID_HCI`

```c
#define BT_HCI_DATAPATH_ID_HCI 0x00
```

<a id="a0382b1713c7b2a774a8f004b6d1bc33f"></a>

### `BT_HCI_DATAPATH_ID_VS`

```c
#define BT_HCI_DATAPATH_ID_VS 0x01
```

<a id="abf755f2839b36a3ac3431bff04193b2f"></a>

### `BT_HCI_DATAPATH_ID_VS_END`

```c
#define BT_HCI_DATAPATH_ID_VS_END 0xfe
```

<a id="aae1149095ff44d1b749e8b4b4d4aa32f"></a>

### `BT_HCI_DEDICATED_BONDING`

```c
#define BT_HCI_DEDICATED_BONDING 0x02
```

<a id="aa1361f09852be86296cf91896d8f0853"></a>

### `BT_HCI_DEDICATED_BONDING_MITM`

```c
#define BT_HCI_DEDICATED_BONDING_MITM 0x03
```

<a id="a08260407c93741e254a4427ba42c274d"></a>

### `BT_HCI_EIR_MAX_DATA_LEN`

```c
#define BT_HCI_EIR_MAX_DATA_LEN 240
```

扩展查询响应（Extended Inquiry Response）数据的最大长度。

<a id="ae4271fbdb039750aceac7c0712d4f3db"></a>

### `BT_HCI_ENCRYPTION_KEY_SIZE_MAX`

```c
#define BT_HCI_ENCRYPTION_KEY_SIZE_MAX 16
```

<a id="ab4eedd90a583b3893c77f51aee16e3c0"></a>

### `BT_HCI_ENCRYPTION_KEY_SIZE_MIN`

```c
#define BT_HCI_ENCRYPTION_KEY_SIZE_MIN 7
```

<a id="a1828465a27d0a30b0da6dfeb40ff3915"></a>

### `BT_HCI_ENCRYPTION_OFF`

```c
#define BT_HCI_ENCRYPTION_OFF 0x00
```

<a id="a355ff7e0b5a5deea620f04a56e869be2"></a>

### `BT_HCI_ENCRYPTION_ON_BR_AES_CCM`

```c
#define BT_HCI_ENCRYPTION_ON_BR_AES_CCM 0x02
```

<a id="ab4bf0fcc115109a5d5cb12f9bbbf0225"></a>

### `BT_HCI_ENCRYPTION_ON_BR_E0`

```c
#define BT_HCI_ENCRYPTION_ON_BR_E0 0x01
```

<a id="aa3946f9d506682315e81823121bcd34a"></a>

### `BT_HCI_ENCRYPTION_ON_LE_AES_CCM`

```c
#define BT_HCI_ENCRYPTION_ON_LE_AES_CCM 0x01
```

<a id="abfa408d8366ff3cae1cd35fffcda30c0"></a>

### `BT_HCI_ERR_ADV_TIMEOUT`

```c
#define BT_HCI_ERR_ADV_TIMEOUT 0x3c
```

<a id="a070d51dd0de3288f9811f90a558c889b"></a>

### `BT_HCI_ERR_AUTH_FAIL`

```c
#define BT_HCI_ERR_AUTH_FAIL 0x05
```

<a id="a366f85b3bcb3f578b2572149c69b7fc0"></a>

### `BT_HCI_ERR_BD_ADDR_UNACCEPTABLE`

```c
#define BT_HCI_ERR_BD_ADDR_UNACCEPTABLE 0x0f
```

<a id="a3b9fc13a3e3ecc9f0f4431487c0301b5"></a>

### `BT_HCI_ERR_CHAN_ASSESS_NOT_SUPPORTED`

```c
#define BT_HCI_ERR_CHAN_ASSESS_NOT_SUPPORTED 0x2e
```

<a id="a6e9a4db5962d79b5a7f43a4c2919c9e9"></a>

### `BT_HCI_ERR_CLOCK_ADJUST_REJECTED`

```c
#define BT_HCI_ERR_CLOCK_ADJUST_REJECTED 0x40
```

<a id="a5ee9f2e9625d732e84e5ef593bb2a3f9"></a>

### `BT_HCI_ERR_CMD_DISALLOWED`

```c
#define BT_HCI_ERR_CMD_DISALLOWED 0x0c
```

<a id="ae4682cbd7a9b9dedd25926efe029c0d7"></a>

### `BT_HCI_ERR_CONN_ACCEPT_TIMEOUT`

```c
#define BT_HCI_ERR_CONN_ACCEPT_TIMEOUT 0x10
```

<a id="abcf4cd921e304758cc969a83445d70ec"></a>

### `BT_HCI_ERR_CONN_ALREADY_EXISTS`

```c
#define BT_HCI_ERR_CONN_ALREADY_EXISTS 0x0b
```

<a id="ac6c44be2e737d7a10b5c886c69d6b1a5"></a>

### `BT_HCI_ERR_CONN_FAIL_TO_ESTAB`

```c
#define BT_HCI_ERR_CONN_FAIL_TO_ESTAB 0x3e
```

<a id="a490798f4f1e226e66475f0fb84cfbcd5"></a>

### `BT_HCI_ERR_CONN_LIMIT_EXCEEDED`

```c
#define BT_HCI_ERR_CONN_LIMIT_EXCEEDED 0x09
```

<a id="a1adf558f8f606612ca96bdbbb55e0e78"></a>

### `BT_HCI_ERR_CONN_REJECTED_DUE_TO_NO_CHAN`

```c
#define BT_HCI_ERR_CONN_REJECTED_DUE_TO_NO_CHAN 0x39
```

<a id="ab702caf5cd73431cc9aede8891f74610"></a>

### `BT_HCI_ERR_CONN_TIMEOUT`

```c
#define BT_HCI_ERR_CONN_TIMEOUT 0x08
```

<a id="a33167856fe838b833fe42d92c3eac4eb"></a>

### `BT_HCI_ERR_CONTROLLER_BUSY`

```c
#define BT_HCI_ERR_CONTROLLER_BUSY 0x3a
```

<a id="a3b461d65baa95f8f984b212264dc5072"></a>

### `BT_HCI_ERR_DIFF_TRANS_COLLISION`

```c
#define BT_HCI_ERR_DIFF_TRANS_COLLISION 0x2a
```

<a id="aeb5499a707e1c41cbd9db882cfdf0677"></a>

### `BT_HCI_ERR_ENC_MODE_NOT_ACCEPTABLE`

```c
#define BT_HCI_ERR_ENC_MODE_NOT_ACCEPTABLE 0x25
```

<a id="a1b7094ad185ed22542f370ab1101c1ae"></a>

### `BT_HCI_ERR_EXT_INQ_RESP_TOO_LARGE`

```c
#define BT_HCI_ERR_EXT_INQ_RESP_TOO_LARGE 0x36
```

<a id="a107d85e39fec3146d6b017deb047571b"></a>

### `BT_HCI_ERR_HOST_BUSY_PAIRING`

```c
#define BT_HCI_ERR_HOST_BUSY_PAIRING 0x38
```

<a id="a5dfcb0d206b98be7eacdc67547bb8a2c"></a>

### `BT_HCI_ERR_HW_FAILURE`

```c
#define BT_HCI_ERR_HW_FAILURE 0x03
```

<a id="a2d336db995ab250f94de66da952c642c"></a>

### `BT_HCI_ERR_INSTANT_PASSED`

```c
#define BT_HCI_ERR_INSTANT_PASSED 0x28
```

<a id="a334efee11bd7086e0611c8f628d65abb"></a>

### `BT_HCI_ERR_INSUFF_SECURITY`

```c
#define BT_HCI_ERR_INSUFF_SECURITY 0x2f
```

<a id="a0efddbffb31b93158b10a3f678f94f4e"></a>

### `BT_HCI_ERR_INSUFFICIENT_RESOURCES`

```c
#define BT_HCI_ERR_INSUFFICIENT_RESOURCES 0x0d
```

<a id="a08d4bdfc189bccbdb97a51b0089e77a0"></a>

### `BT_HCI_ERR_INSUFFICIENT_SECURITY`

```c
#define BT_HCI_ERR_INSUFFICIENT_SECURITY 0x0e
```

<a id="a943fe81109d82983018b558b9274f9a3"></a>

### `BT_HCI_ERR_INVALID_LL_PARAM`

```c
#define BT_HCI_ERR_INVALID_LL_PARAM 0x1e
```

<a id="afc76c774f5e71423eb9fea910d1860e9"></a>

### `BT_HCI_ERR_INVALID_PARAM`

```c
#define BT_HCI_ERR_INVALID_PARAM 0x12
```

<a id="a86b092455cfd220d48af2bea04900b5b"></a>

### `BT_HCI_ERR_LIMIT_REACHED`

```c
#define BT_HCI_ERR_LIMIT_REACHED 0x43
```

<a id="aee97132db4398e2db0a6e115ca20b9b4"></a>

### `BT_HCI_ERR_LINK_KEY_CANNOT_BE_CHANGED`

```c
#define BT_HCI_ERR_LINK_KEY_CANNOT_BE_CHANGED 0x26
```

<a id="a0e280074290680d62ad4721384bb603e"></a>

### `BT_HCI_ERR_LL_PROC_COLLISION`

```c
#define BT_HCI_ERR_LL_PROC_COLLISION 0x23
```

<a id="a6317763780d9c81e6752d5a2c8ce3172"></a>

### `BT_HCI_ERR_LL_RESP_TIMEOUT`

```c
#define BT_HCI_ERR_LL_RESP_TIMEOUT 0x22
```

<a id="a47c02d44d40d785db6fee28c88d3c5b4"></a>

### `BT_HCI_ERR_LMP_PDU_NOT_ALLOWED`

```c
#define BT_HCI_ERR_LMP_PDU_NOT_ALLOWED 0x24
```

<a id="a0f07b75be216456e9370485dca0da992"></a>

### `BT_HCI_ERR_LOCALHOST_TERM_CONN`

```c
#define BT_HCI_ERR_LOCALHOST_TERM_CONN 0x16
```

<a id="af0b9f71a874ca2c3587256c7f665e9fa"></a>

### `BT_HCI_ERR_MAC_CONN_FAILED`

```c
#define BT_HCI_ERR_MAC_CONN_FAILED 0x3f
```

<a id="ac54f84b29901185822f6bad2edf86b61"></a>

### `BT_HCI_ERR_MEM_CAPACITY_EXCEEDED`

```c
#define BT_HCI_ERR_MEM_CAPACITY_EXCEEDED 0x07
```

<a id="a85433a7b3bcac0a507d7f6376a084142"></a>

### `BT_HCI_ERR_OP_CANCELLED_BY_HOST`

```c
#define BT_HCI_ERR_OP_CANCELLED_BY_HOST 0x44
```

<a id="ab63f7d0c79aaa57abf59aa18e112345f"></a>

### `BT_HCI_ERR_PACKET_TOO_LONG`

```c
#define BT_HCI_ERR_PACKET_TOO_LONG 0x45
```

<a id="a1e89c8eb63dee6bd720ef9354c867519"></a>

### `BT_HCI_ERR_PAGE_TIMEOUT`

```c
#define BT_HCI_ERR_PAGE_TIMEOUT 0x04
```

<a id="a60823c337c91aa95348dcae250a83977"></a>

### `BT_HCI_ERR_PAIRING_NOT_ALLOWED`

```c
#define BT_HCI_ERR_PAIRING_NOT_ALLOWED 0x18
```

<a id="a059c7d5619823eddf2c541b40a6464cb"></a>

### `BT_HCI_ERR_PAIRING_NOT_SUPPORTED`

```c
#define BT_HCI_ERR_PAIRING_NOT_SUPPORTED 0x29
```

不支持使用单元密钥配对（Pairing with Unit Key Not Supported）。

此错误仅对基本速率／增强数据速率（BR/EDR）有效。

<a id="a29c763a2e70820fae7e2e825d22f4991"></a>

### `BT_HCI_ERR_PARAM_OUT_OF_MANDATORY_RANGE`

```c
#define BT_HCI_ERR_PARAM_OUT_OF_MANDATORY_RANGE 0x30
```

<a id="a39f129aefe81c2d06f70552ace008a15"></a>

### `BT_HCI_ERR_PIN_OR_KEY_MISSING`

```c
#define BT_HCI_ERR_PIN_OR_KEY_MISSING 0x06
```

<a id="a88363d1eb1c0d13dc8138af8edc76abc"></a>

### `BT_HCI_ERR_QOS_REJECTED`

```c
#define BT_HCI_ERR_QOS_REJECTED 0x2d
```

<a id="a37c2fdc6b32b4a2cb70d5c17dfbe262b"></a>

### `BT_HCI_ERR_QOS_UNACCEPTABLE_PARAM`

```c
#define BT_HCI_ERR_QOS_UNACCEPTABLE_PARAM 0x2c
```

<a id="a5eeadfb220c24b2e7f5ce3fd21e5d46a"></a>

### `BT_HCI_ERR_REMOTE_LOW_RESOURCES`

```c
#define BT_HCI_ERR_REMOTE_LOW_RESOURCES 0x14
```

<a id="a083f1fc52300f7e47c2f8d4e50551851"></a>

### `BT_HCI_ERR_REMOTE_POWER_OFF`

```c
#define BT_HCI_ERR_REMOTE_POWER_OFF 0x15
```

<a id="ac0e3b44027180d7a2dedb59395c4b111"></a>

### `BT_HCI_ERR_REMOTE_USER_TERM_CONN`

```c
#define BT_HCI_ERR_REMOTE_USER_TERM_CONN 0x13
```

<a id="a11d42e0347cc9d1d50ccd45c2e9a39f6"></a>

### `BT_HCI_ERR_REPEATED_ATTEMPTS`

```c
#define BT_HCI_ERR_REPEATED_ATTEMPTS 0x17
```

<a id="a0e02fd84d7a355f42fe006c756936d78"></a>

### `BT_HCI_ERR_REQUESTED_QOS_NOT_SUPPORTED`

```c
#define BT_HCI_ERR_REQUESTED_QOS_NOT_SUPPORTED 0x27
```

<a id="ac6244ca7123879ef039c2c5486d50d41"></a>

### `BT_HCI_ERR_RESERVED_SLOT_VIOLATION`

```c
#define BT_HCI_ERR_RESERVED_SLOT_VIOLATION 0x34
```

<a id="a070d016f54e7f5f0a7ca6d8c8218505f"></a>

### `BT_HCI_ERR_ROLE_CHANGE_NOT_ALLOWED`

```c
#define BT_HCI_ERR_ROLE_CHANGE_NOT_ALLOWED 0x21
```

<a id="ab40a919a2d87376f2aca6d2ea3f55758"></a>

### `BT_HCI_ERR_ROLE_SWITCH_FAILED`

```c
#define BT_HCI_ERR_ROLE_SWITCH_FAILED 0x35
```

<a id="ac9c9a68e696e038d7b05af89e3a0c7b6"></a>

### `BT_HCI_ERR_ROLE_SWITCH_PENDING`

```c
#define BT_HCI_ERR_ROLE_SWITCH_PENDING 0x32
```

<a id="ad8f77a43360e8ab2e6c71a103e14c951"></a>

### `BT_HCI_ERR_SCO_AIR_MODE_REJECTED`

```c
#define BT_HCI_ERR_SCO_AIR_MODE_REJECTED 0x1d
```

<a id="a5093c6357fcefd1ccdcbdf9a99f18e7c"></a>

### `BT_HCI_ERR_SCO_INTERVAL_REJECTED`

```c
#define BT_HCI_ERR_SCO_INTERVAL_REJECTED 0x1c
```

<a id="a5e28f04c454361508bc791c6ce292bc2"></a>

### `BT_HCI_ERR_SCO_OFFSET_REJECTED`

```c
#define BT_HCI_ERR_SCO_OFFSET_REJECTED 0x1b
```

<a id="afd8840ad198dfdb666bf24851a478c70"></a>

### `BT_HCI_ERR_SIMPLE_PAIR_NOT_SUPP_BY_HOST`

```c
#define BT_HCI_ERR_SIMPLE_PAIR_NOT_SUPP_BY_HOST 0x37
```

<a id="a9e7483e2d7f46981e9d1fcdbb8a7515c"></a>

### `BT_HCI_ERR_SUBMAP_NOT_DEFINED`

```c
#define BT_HCI_ERR_SUBMAP_NOT_DEFINED 0x41
```

<a id="a27c890210eded48f159073cccef8582a"></a>

### `BT_HCI_ERR_SUCCESS`

```c
#define BT_HCI_ERR_SUCCESS 0x00
```

HCI 错误码（Error Codes），依据《蓝牙核心规范》（BT Core Spec）v5.4，第 1 卷 F 部分。

<a id="a56a3d3d9d7798334b29c02214a2e73bf"></a>

### `BT_HCI_ERR_SYNC_CONN_LIMIT_EXCEEDED`

```c
#define BT_HCI_ERR_SYNC_CONN_LIMIT_EXCEEDED 0x0a
```

<a id="a71dd49b1b5dc51ad7db8da9aecf9ff06"></a>

### `BT_HCI_ERR_TERM_DUE_TO_MIC_FAIL`

```c
#define BT_HCI_ERR_TERM_DUE_TO_MIC_FAIL 0x3d
```

<a id="a8dcf345b1fea1364f490f40963992cd6"></a>

### `BT_HCI_ERR_TOO_EARLY`

```c
#define BT_HCI_ERR_TOO_EARLY 0x47
```

<a id="a9c62f8f73470a3157a60f8d6d56b22a4"></a>

### `BT_HCI_ERR_TOO_LATE`

```c
#define BT_HCI_ERR_TOO_LATE 0x46
```

<a id="a712e214942c0d151597ce04e9d0df453"></a>

### `BT_HCI_ERR_UNACCEPT_CONN_PARAM`

```c
#define BT_HCI_ERR_UNACCEPT_CONN_PARAM 0x3b
```

<a id="a7646bc91f5dbb28c5eeda7e1828f2e30"></a>

### `BT_HCI_ERR_UNKNOWN_ADV_IDENTIFIER`

```c
#define BT_HCI_ERR_UNKNOWN_ADV_IDENTIFIER 0x42
```

<a id="a376012d3b8f7814870e3f03f6cbabb89"></a>

### `BT_HCI_ERR_UNKNOWN_CMD`

```c
#define BT_HCI_ERR_UNKNOWN_CMD 0x01
```

<a id="afd68afeb0296e3af363d7d60eaf4e9a1"></a>

### `BT_HCI_ERR_UNKNOWN_CONN_ID`

```c
#define BT_HCI_ERR_UNKNOWN_CONN_ID 0x02
```

<a id="a0f81b5c19358982bd33c527239200b08"></a>

### `BT_HCI_ERR_UNKNOWN_LMP_PDU`

```c
#define BT_HCI_ERR_UNKNOWN_LMP_PDU 0x19
```

<a id="ab3833bbb70b6a2e57870d8243f528b90"></a>

### `BT_HCI_ERR_UNSPECIFIED`

```c
#define BT_HCI_ERR_UNSPECIFIED 0x1f
```

<a id="af73db17855859676827bad84e2ccbabe"></a>

### `BT_HCI_ERR_UNSUPP_FEATURE_PARAM_VAL`

```c
#define BT_HCI_ERR_UNSUPP_FEATURE_PARAM_VAL 0x11
```

<a id="af1fa61561b6a91d08f81e9c19cbe89f7"></a>

### `BT_HCI_ERR_UNSUPP_LL_PARAM_VAL`

```c
#define BT_HCI_ERR_UNSUPP_LL_PARAM_VAL 0x20
```

<a id="a516751f02bd497a020783f69bcf71453"></a>

### `BT_HCI_ERR_UNSUPP_REMOTE_FEATURE`

```c
#define BT_HCI_ERR_UNSUPP_REMOTE_FEATURE 0x1a
```

<a id="a4c57b051b336788e503a8521bb5ada80"></a>

### `BT_HCI_ESCO`

```c
#define BT_HCI_ESCO 0x02
```

<a id="acc9c74c8406b84baaf55d9452924aaf9"></a>

### `BT_HCI_EVT_AUTH_COMPLETE`

```c
#define BT_HCI_EVT_AUTH_COMPLETE 0x06
```

<a id="a589975abd5d9532ba16d15ac21c5e81e"></a>

### `BT_HCI_EVT_AUTH_PAYLOAD_TIMEOUT_EXP`

```c
#define BT_HCI_EVT_AUTH_PAYLOAD_TIMEOUT_EXP 0x57
```

<a id="a06f6cf60885ac051cdc9b463fc3b7de7"></a>

### `BT_HCI_EVT_CMD_COMPLETE`

```c
#define BT_HCI_EVT_CMD_COMPLETE 0x0e
```

<a id="a2b35e7484351228243bb3564273c5bff"></a>

### `BT_HCI_EVT_CMD_STATUS`

```c
#define BT_HCI_EVT_CMD_STATUS 0x0f
```

<a id="a0dd2162851b4a7afc3d96924f69cceca"></a>

### `BT_HCI_EVT_CONN_COMPLETE`

```c
#define BT_HCI_EVT_CONN_COMPLETE 0x03
```

<a id="a4dc96c114c545ed23fe926d7ec0967a7"></a>

### `BT_HCI_EVT_CONN_PKT_TYPE_CHANGED`

```c
#define BT_HCI_EVT_CONN_PKT_TYPE_CHANGED 0x1d
```

HCI 连接分组类型已改变事件（Connection Packet Type Changed Event）。

<a id="afc473fec33612ffb044d54bad39e8d76"></a>

### `BT_HCI_EVT_CONN_REQUEST`

```c
#define BT_HCI_EVT_CONN_REQUEST 0x04
```

<a id="ae747b016101bc9e9614163288c5c0d15"></a>

### `BT_HCI_EVT_DATA_BUF_OVERFLOW`

```c
#define BT_HCI_EVT_DATA_BUF_OVERFLOW 0x1a
```

<a id="a32e5051a114f8987b49c6957c84d60e2"></a>

### `BT_HCI_EVT_DISCONN_COMPLETE`

```c
#define BT_HCI_EVT_DISCONN_COMPLETE 0x05
```

<a id="a8dee2fc366d0371b68b212ff40e6ea7d"></a>

### `BT_HCI_EVT_ENCRYPT_CHANGE`

```c
#define BT_HCI_EVT_ENCRYPT_CHANGE 0x08
```

<a id="aad28cc20cc111ac39e39011932b9d22e"></a>

### `BT_HCI_EVT_ENCRYPT_KEY_REFRESH_COMPLETE`

```c
#define BT_HCI_EVT_ENCRYPT_KEY_REFRESH_COMPLETE 0x30
```

<a id="a9b5405de1e07fcefba54b286bd1fdfbe"></a>

### `BT_HCI_EVT_EXTENDED_INQUIRY_RESULT`

```c
#define BT_HCI_EVT_EXTENDED_INQUIRY_RESULT 0x2f
```

<a id="a54c3bdd2687d142f925183a46ffc5f8b"></a>

### `BT_HCI_EVT_HARDWARE_ERROR`

```c
#define BT_HCI_EVT_HARDWARE_ERROR 0x10
```

<a id="a0edb7e700cfa557e7fb8ec44f5eea961"></a>

### `BT_HCI_EVT_HDR_SIZE`

```c
#define BT_HCI_EVT_HDR_SIZE 2
```

<a id="abd8f15d920c0bdb3c68556b4e873f413"></a>

### `BT_HCI_EVT_INQUIRY_COMPLETE`

```c
#define BT_HCI_EVT_INQUIRY_COMPLETE 0x01
```

<a id="a92243c99484922771d5aca8f98945d29"></a>

### `BT_HCI_EVT_INQUIRY_RESULT_WITH_RSSI`

```c
#define BT_HCI_EVT_INQUIRY_RESULT_WITH_RSSI 0x22
```

<a id="a4d69a943660da9c1a6ffedb9b653ce3f"></a>

### `BT_HCI_EVT_IO_CAPA_REQ`

```c
#define BT_HCI_EVT_IO_CAPA_REQ 0x31
```

<a id="a0f5cae40268568e25142eed9e3e5e639"></a>

### `BT_HCI_EVT_IO_CAPA_RESP`

```c
#define BT_HCI_EVT_IO_CAPA_RESP 0x32
```

<a id="a398afcbdb732fe76ec01db1393721ab2"></a>

### `BT_HCI_EVT_LE_ADV_SET_TERMINATED`

```c
#define BT_HCI_EVT_LE_ADV_SET_TERMINATED 0x12
```

<a id="a1a93b78bdbb29982d989aea5eae5ec19"></a>

### `BT_HCI_EVT_LE_ADVERTISING_REPORT`

```c
#define BT_HCI_EVT_LE_ADVERTISING_REPORT 0x02
```

<a id="aade42399ac596746100849328c551259"></a>

### `BT_HCI_EVT_LE_BIG_COMPLETE`

```c
#define BT_HCI_EVT_LE_BIG_COMPLETE 0x1b
```

<a id="a8d021615f0b1b2077bbec1f1482b85ef"></a>

### `BT_HCI_EVT_LE_BIG_SYNC_ESTABLISHED`

```c
#define BT_HCI_EVT_LE_BIG_SYNC_ESTABLISHED 0x1d
```

<a id="a9c79430501848b9e75a21020920a8ca8"></a>

### `BT_HCI_EVT_LE_BIG_SYNC_LOST`

```c
#define BT_HCI_EVT_LE_BIG_SYNC_LOST 0x1e
```

<a id="ac0a1310793a73afda4c2179749df9985"></a>

### `BT_HCI_EVT_LE_BIG_TERMINATE`

```c
#define BT_HCI_EVT_LE_BIG_TERMINATE 0x1c
```

<a id="a651e36b5529cb7f289721573434154cd"></a>

### `BT_HCI_EVT_LE_BIGINFO_ADV_REPORT`

```c
#define BT_HCI_EVT_LE_BIGINFO_ADV_REPORT 0x22
```

<a id="a4f012a8357e5bb17b5dd04128bd39911"></a>

### `BT_HCI_EVT_LE_CHAN_SEL_ALGO`

```c
#define BT_HCI_EVT_LE_CHAN_SEL_ALGO 0x14
```

<a id="a263d26617702ab43fa8b6717007e1df8"></a>

### `BT_HCI_EVT_LE_CIS_ESTABLISHED`

```c
#define BT_HCI_EVT_LE_CIS_ESTABLISHED 0x19
```

<a id="ae5a1301a0fea0ab6c205dab22e39c6c9"></a>

### `BT_HCI_EVT_LE_CIS_ESTABLISHED_V2`

```c
#define BT_HCI_EVT_LE_CIS_ESTABLISHED_V2 0x2a
```

<a id="aaa4af1dcdb163a57b0473b43e8107fd7"></a>

### `BT_HCI_EVT_LE_CIS_REQ`

```c
#define BT_HCI_EVT_LE_CIS_REQ 0x1a
```

<a id="a2c3c4f81903d1860f21880c7c3cfbaa7"></a>

### `BT_HCI_EVT_LE_CONN_COMPLETE`

```c
#define BT_HCI_EVT_LE_CONN_COMPLETE 0x01
```

<a id="a77072c10df87395e7e649307b975fb69"></a>

### `BT_HCI_EVT_LE_CONN_PARAM_REQ`

```c
#define BT_HCI_EVT_LE_CONN_PARAM_REQ 0x06
```

<a id="a6b4187331428ca3abdcce55320e56fe9"></a>

### `BT_HCI_EVT_LE_CONN_RATE_CHANGE`

```c
#define BT_HCI_EVT_LE_CONN_RATE_CHANGE 0x37
```

<a id="aeef912e71549d4b5a0d8b293074a909c"></a>

### `BT_HCI_EVT_LE_CONN_UPDATE_COMPLETE`

```c
#define BT_HCI_EVT_LE_CONN_UPDATE_COMPLETE 0x03
```

<a id="ace41ae5ec2a8f036aabf83ac94937a8b"></a>

### `BT_HCI_EVT_LE_CONNECTION_IQ_REPORT`

```c
#define BT_HCI_EVT_LE_CONNECTION_IQ_REPORT 0x16
```

<a id="a04c4a4567eaad7c592f2181e47768522"></a>

### `BT_HCI_EVT_LE_CONNECTIONLESS_IQ_REPORT`

```c
#define BT_HCI_EVT_LE_CONNECTIONLESS_IQ_REPORT 0x15
```

<a id="ab0d5abde05c53bc194fe07b8726fb307"></a>

### `BT_HCI_EVT_LE_CS_CONFIG_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_CONFIG_COMPLETE 0x2F
```

<a id="a276cf3951bb5c4ee0b1deeb78a7b5681"></a>

### `BT_HCI_EVT_LE_CS_PROCEDURE_ENABLE_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_PROCEDURE_ENABLE_COMPLETE 0x30
```

<a id="a319b523766bcc778ba6bfb3784ac49b7"></a>

### `BT_HCI_EVT_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_FAE_TABLE_COMPLETE 0x2D
```

<a id="abceb3da0b6d4c858ad35c631acf0516e"></a>

### `BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE 0x2C
```

<a id="a654ffdb3fac697916351b12f737425bd"></a>

### `BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2`

```c
#define BT_HCI_EVT_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES_COMPLETE_V2 0x38
```

HCI 低功耗蓝牙信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete，v2）。

<a id="ae1e6afca81585dda0f08f85adc3c69a3"></a>

### `BT_HCI_EVT_LE_CS_SECURITY_ENABLE_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_SECURITY_ENABLE_COMPLETE 0x2E
```

<a id="a56079aad1e8efe328c0bfd4dbad9d953"></a>

### `BT_HCI_EVT_LE_CS_SUBEVENT_RESULT`

```c
#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT 0x31
```

<a id="aad00fc66b8bbc4f3e474661cb4122e47"></a>

### `BT_HCI_EVT_LE_CS_SUBEVENT_RESULT_CONTINUE`

```c
#define BT_HCI_EVT_LE_CS_SUBEVENT_RESULT_CONTINUE 0x32
```

<a id="a7dae3e2125d30c3b344b51aba0df68bf"></a>

### `BT_HCI_EVT_LE_CS_TEST_END_COMPLETE`

```c
#define BT_HCI_EVT_LE_CS_TEST_END_COMPLETE 0x33
```

<a id="aacaa203f0c8e23c6ca551df0375410e8"></a>

### `BT_HCI_EVT_LE_CTE_REQUEST_FAILED`

```c
#define BT_HCI_EVT_LE_CTE_REQUEST_FAILED 0x17
```

<a id="a064cf9e32616c6f94041d138a5bf4819"></a>

### `BT_HCI_EVT_LE_DATA_LEN_CHANGE`

```c
#define BT_HCI_EVT_LE_DATA_LEN_CHANGE 0x07
```

<a id="a417144400fd8d7f5c05e050950c75dab"></a>

### `BT_HCI_EVT_LE_DIRECT_ADV_REPORT`

```c
#define BT_HCI_EVT_LE_DIRECT_ADV_REPORT 0x0b
```

<a id="a292de9ec009a80e23308ead618656b4f"></a>

### `BT_HCI_EVT_LE_ENH_CONN_COMPLETE`

```c
#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE 0x0a
```

<a id="a60ea5e58028aa09c00d20cfff5c942d5"></a>

### `BT_HCI_EVT_LE_ENH_CONN_COMPLETE_V2`

```c
#define BT_HCI_EVT_LE_ENH_CONN_COMPLETE_V2 0x29
```

<a id="ad63fc0c42f0253dfe06b81324a05f505"></a>

### `BT_HCI_EVT_LE_EXT_ADVERTISING_REPORT`

```c
#define BT_HCI_EVT_LE_EXT_ADVERTISING_REPORT 0x0d
```

<a id="a38b479e428c9154c51f04bc84ddf7279"></a>

### `BT_HCI_EVT_LE_FRAME_SPACE_UPDATE_COMPLETE`

```c
#define BT_HCI_EVT_LE_FRAME_SPACE_UPDATE_COMPLETE 0x35
```

<a id="a8ab77f497135e365fb9e895dc2d4d453"></a>

### `BT_HCI_EVT_LE_GENERATE_DHKEY_COMPLETE`

```c
#define BT_HCI_EVT_LE_GENERATE_DHKEY_COMPLETE 0x09
```

<a id="a9efb73da285829cde0e4c1ac28a48f1a"></a>

### `BT_HCI_EVT_LE_LTK_REQUEST`

```c
#define BT_HCI_EVT_LE_LTK_REQUEST 0x05
```

<a id="ac1d7f9270323d7fa459e60b372cf998b"></a>

### `BT_HCI_EVT_LE_META_EVENT`

```c
#define BT_HCI_EVT_LE_META_EVENT 0x3e
```

<a id="abe39909eb984dd6edd1220f9c6744546"></a>

### `BT_HCI_EVT_LE_P256_PUBLIC_KEY_COMPLETE`

```c
#define BT_HCI_EVT_LE_P256_PUBLIC_KEY_COMPLETE 0x08
```

<a id="ad61867c0bef6797f7a3b5418c5a4ed5f"></a>

### `BT_HCI_EVT_LE_PAST_RECEIVED`

```c
#define BT_HCI_EVT_LE_PAST_RECEIVED 0x18
```

<a id="a5379a2a0016a2551ac79736924c7ea86"></a>

### `BT_HCI_EVT_LE_PAST_RECEIVED_V2`

```c
#define BT_HCI_EVT_LE_PAST_RECEIVED_V2 0x26
```

<a id="a3e646ec9a2e0baca5126e58368c97995"></a>

### `BT_HCI_EVT_LE_PATH_LOSS_THRESHOLD`

```c
#define BT_HCI_EVT_LE_PATH_LOSS_THRESHOLD 0x20
```

<a id="a64e0f465068e72e98904fa6cdc33d3de"></a>

### `BT_HCI_EVT_LE_PER_ADV_RESPONSE_REPORT`

```c
#define BT_HCI_EVT_LE_PER_ADV_RESPONSE_REPORT 0x28
```

<a id="a4395b8b850e9fd3735c2369798f9c226"></a>

### `BT_HCI_EVT_LE_PER_ADV_SUBEVENT_DATA_REQUEST`

```c
#define BT_HCI_EVT_LE_PER_ADV_SUBEVENT_DATA_REQUEST 0x27
```

<a id="a8c721c9e5df496900f661755aff7cbd6"></a>

### `BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED`

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED 0x0e
```

<a id="a0decb07f1b4ae20b23cffc616dd442e4"></a>

### `BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED_V2`

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_ESTABLISHED_V2 0x24
```

<a id="ab303042eabbeb133e202bdcfbd38666c"></a>

### `BT_HCI_EVT_LE_PER_ADV_SYNC_LOST`

```c
#define BT_HCI_EVT_LE_PER_ADV_SYNC_LOST 0x10
```

<a id="a31fc096530a89e63d4967d7ddd85b753"></a>

### `BT_HCI_EVT_LE_PER_ADVERTISING_REPORT`

```c
#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT 0x0f
```

<a id="a8d067bf751953fd8a7bb5421bdc94970"></a>

### `BT_HCI_EVT_LE_PER_ADVERTISING_REPORT_V2`

```c
#define BT_HCI_EVT_LE_PER_ADVERTISING_REPORT_V2 0x25
```

<a id="a44f18d799280d47ec09376e7cffd4c40"></a>

### `BT_HCI_EVT_LE_PHY_UPDATE_COMPLETE`

```c
#define BT_HCI_EVT_LE_PHY_UPDATE_COMPLETE 0x0c
```

<a id="af442282c712682dc805d139f7c31c62f"></a>

### `BT_HCI_EVT_LE_READ_ALL_REMOTE_FEAT_COMPLETE`

```c
#define BT_HCI_EVT_LE_READ_ALL_REMOTE_FEAT_COMPLETE 0x2b
```

<a id="a8b1653caabce8474fba132343aa62f56"></a>

### `BT_HCI_EVT_LE_REMOTE_FEAT_COMPLETE`

```c
#define BT_HCI_EVT_LE_REMOTE_FEAT_COMPLETE 0x04
```

<a id="aeb33301a950a9520d7ff706dddb07951"></a>

### `BT_HCI_EVT_LE_REQ_PEER_SCA_COMPLETE`

```c
#define BT_HCI_EVT_LE_REQ_PEER_SCA_COMPLETE 0x1f
```

<a id="a0ebf19a602a02c00793b3de64392e514"></a>

### `BT_HCI_EVT_LE_SCAN_REQ_RECEIVED`

```c
#define BT_HCI_EVT_LE_SCAN_REQ_RECEIVED 0x13
```

<a id="a7234c851946c6025aa850c9bf28faab0"></a>

### `BT_HCI_EVT_LE_SCAN_TIMEOUT`

```c
#define BT_HCI_EVT_LE_SCAN_TIMEOUT 0x11
```

<a id="a2098d628b6ad185cb29106ef69c3627d"></a>

### `BT_HCI_EVT_LE_SUBRATE_CHANGE`

```c
#define BT_HCI_EVT_LE_SUBRATE_CHANGE 0x23
```

<a id="a835280c0bf13ddebf451fef5f08c22d0"></a>

### `BT_HCI_EVT_LE_TRANSMIT_POWER_REPORT`

```c
#define BT_HCI_EVT_LE_TRANSMIT_POWER_REPORT 0x21
```

<a id="a15578dd8e9d2b16a28ea0b020ac9112b"></a>

### `BT_HCI_EVT_LINK_KEY_NOTIFY`

```c
#define BT_HCI_EVT_LINK_KEY_NOTIFY 0x18
```

<a id="aab60607637f0e1f8e3cbf9f7292ddc57"></a>

### `BT_HCI_EVT_LINK_KEY_REQ`

```c
#define BT_HCI_EVT_LINK_KEY_REQ 0x17
```

<a id="a4fa69f355651302f55064c13af7b18a2"></a>

### `BT_HCI_EVT_MODE_CHANGE`

```c
#define BT_HCI_EVT_MODE_CHANGE 0x14
```

<a id="a883433c60959629a013d34cea21ab88f"></a>

### `BT_HCI_EVT_NUM_COMPLETED_PACKETS`

```c
#define BT_HCI_EVT_NUM_COMPLETED_PACKETS 0x13
```

<a id="a8c16e0bdecf9eae58bbd884fb48b0fc2"></a>

### `BT_HCI_EVT_PIN_CODE_REQ`

```c
#define BT_HCI_EVT_PIN_CODE_REQ 0x16
```

<a id="a092a782ea069c98475a6617241321122"></a>

### `BT_HCI_EVT_REMOTE_EXT_FEATURES`

```c
#define BT_HCI_EVT_REMOTE_EXT_FEATURES 0x23
```

<a id="acbad340a978d4fc118af826d2c1a81e3"></a>

### `BT_HCI_EVT_REMOTE_FEATURES`

```c
#define BT_HCI_EVT_REMOTE_FEATURES 0x0b
```

<a id="a1a4be9cf628063db2fb821f67c54ea56"></a>

### `BT_HCI_EVT_REMOTE_NAME_REQ_COMPLETE`

```c
#define BT_HCI_EVT_REMOTE_NAME_REQ_COMPLETE 0x07
```

<a id="a18f58c80d213d666ee8309cda8eb0a26"></a>

### `BT_HCI_EVT_REMOTE_VERSION_INFO`

```c
#define BT_HCI_EVT_REMOTE_VERSION_INFO 0x0c
```

<a id="a9508e6faf71a345f7ff3d2cec9d85dde"></a>

### `BT_HCI_EVT_ROLE_CHANGE`

```c
#define BT_HCI_EVT_ROLE_CHANGE 0x12
```

<a id="a7d2ba655c6954f90de04cafafccd727f"></a>

### `BT_HCI_EVT_SSP_COMPLETE`

```c
#define BT_HCI_EVT_SSP_COMPLETE 0x36
```

<a id="ab77f3074a2236afc1ed773775d17befe"></a>

### `BT_HCI_EVT_SYNC_CONN_COMPLETE`

```c
#define BT_HCI_EVT_SYNC_CONN_COMPLETE 0x2c
```

<a id="a0f44f6e5037d650b9dd0c5f34ba681b5"></a>

### `BT_HCI_EVT_UNKNOWN`

```c
#define BT_HCI_EVT_UNKNOWN 0x00
```

<a id="a78cdb5848d8a12a8cbea17767b3d02aa"></a>

### `BT_HCI_EVT_USER_CONFIRM_REQ`

```c
#define BT_HCI_EVT_USER_CONFIRM_REQ 0x33
```

<a id="a724d43899b16fcb89c235898a21c13b9"></a>

### `BT_HCI_EVT_USER_PASSKEY_NOTIFY`

```c
#define BT_HCI_EVT_USER_PASSKEY_NOTIFY 0x3b
```

<a id="a38a1bce81af39bb28d40e149f9309b69"></a>

### `BT_HCI_EVT_USER_PASSKEY_REQ`

```c
#define BT_HCI_EVT_USER_PASSKEY_REQ 0x34
```

<a id="a955fe06f3fcab82c3370cb621f0dbca0"></a>

### `BT_HCI_EVT_VENDOR`

```c
#define BT_HCI_EVT_VENDOR 0xff
```

<a id="ad777455cbcdfe02dd297dee5510e63b4"></a>

### `BT_HCI_GENERAL_BONDING`

```c
#define BT_HCI_GENERAL_BONDING 0x04
```

<a id="a5b30ffdf3753d0a2a6c8ab025d32acef"></a>

### `BT_HCI_GENERAL_BONDING_MITM`

```c
#define BT_HCI_GENERAL_BONDING_MITM 0x05
```

<a id="a17386452bbd60c85959296b6539232bd"></a>

### `BT_HCI_H4_ACL`

```c
#define BT_HCI_H4_ACL 0x02 /* HCI ACL Data packet */
```

<a id="a524788ee4d21fe9a4625c35e1756bfe9"></a>

### `BT_HCI_H4_CMD`

```c
#define BT_HCI_H4_CMD 0x01 /* HCI Command packet */
```

<a id="a783053bc2846063e50755f1590e81ba8"></a>

### `BT_HCI_H4_EVT`

```c
#define BT_HCI_H4_EVT 0x04 /* HCI Event packet */
```

<a id="af5e6a53cc7d9619f4ac2ea5bd3256149"></a>

### `BT_HCI_H4_ISO`

```c
#define BT_HCI_H4_ISO 0x05 /* HCI ISO Data packet */
```

<a id="a2a578399cd3a1ed875ba2c8a49b8129b"></a>

### `BT_HCI_H4_NONE`

```c
#define BT_HCI_H4_NONE 0x00 /* None of the known packet types */
```

<a id="a9e1c93f187ed5864cebefccea1b3faa2"></a>

### `BT_HCI_H4_SCO`

```c
#define BT_HCI_H4_SCO 0x03 /* HCI Synchronous Data packet */
```

<a id="a18b5fef3eb5b947ce328e17c1e7db02d"></a>

### `BT_HCI_ISO_CIG_ID_MAX`

```c
#define BT_HCI_ISO_CIG_ID_MAX 0xFE
```

<a id="a26c78a4b760b97682269e66dfe6f99df"></a>

### `BT_HCI_ISO_CIS_COUNT_MAX`

```c
#define BT_HCI_ISO_CIS_COUNT_MAX 0x1F
```

<a id="a11e614cc72adb58bda2a2bdd5f4b36ef"></a>

### `BT_HCI_ISO_CIS_ID_VALID_MAX`

```c
#define BT_HCI_ISO_CIS_ID_VALID_MAX 0xEF
```

<a id="aaf4b4fc224c8b5cfdca663250eb29350"></a>

### `BT_HCI_ISO_FRAMING_VALID_MASK`

```c
#define BT_HCI_ISO_FRAMING_VALID_MASK 0x01
```

<a id="a75c1f5e8a44b034004ecfebdb75ee4be"></a>

### `BT_HCI_ISO_HDR_SIZE`

```c
#define BT_HCI_ISO_HDR_SIZE 4
```

<a id="aaadbec2cc6adc2bb14d7117396023d06"></a>

### `BT_HCI_ISO_INTERVAL_MAX`

```c
#define BT_HCI_ISO_INTERVAL_MAX 0x0C80
```

<a id="a9d5e85ae1380fa85bae9d7e5e67aa0ae"></a>

### `BT_HCI_ISO_INTERVAL_MIN`

```c
#define BT_HCI_ISO_INTERVAL_MIN 0x0004
```

<a id="a9f3e990cadf1be179fcbac3f8ef74efe"></a>

### `BT_HCI_ISO_MAX_SDU_VALID_MASK`

```c
#define BT_HCI_ISO_MAX_SDU_VALID_MASK 0x0FFF
```

<a id="a9794f59f8d28879753b39bd504cf55be"></a>

### `BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MAX`

```c
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MAX 0x0FA0
```

<a id="a8d044df1bfab8381b7e334597b303588"></a>

### `BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MIN`

```c
#define BT_HCI_ISO_MAX_TRANSPORT_LATENCY_MIN 0x0005
```

<a id="aecaa88e04025e575c9bcda093f027400"></a>

### `BT_HCI_ISO_PACKING_VALID_MASK`

```c
#define BT_HCI_ISO_PACKING_VALID_MASK 0x01
```

<a id="ae055ed9714ca23bebd48bb399af04d83"></a>

### `BT_HCI_ISO_PHY_VALID_MASK`

```c
#define BT_HCI_ISO_PHY_VALID_MASK 0x07
```

<a id="a94b93cd856353f24afee5e4022cdbdb9"></a>

### `BT_HCI_ISO_SDU_HDR_SIZE`

```c
#define BT_HCI_ISO_SDU_HDR_SIZE 4
```

<a id="aa75800427e808756fc7c6d30da57de37"></a>

### `BT_HCI_ISO_SDU_INTERVAL_MAX`

```c
#define BT_HCI_ISO_SDU_INTERVAL_MAX 0x0FFFFF
```

<a id="a12e9af0e72013649da8afc7aa70a4e9c"></a>

### `BT_HCI_ISO_SDU_INTERVAL_MIN`

```c
#define BT_HCI_ISO_SDU_INTERVAL_MIN 0x0000FF
```

<a id="a22db454317bc89afe092ab9127888441"></a>

### `BT_HCI_ISO_SDU_TS_HDR_SIZE`

```c
#define BT_HCI_ISO_SDU_TS_HDR_SIZE 8
```

<a id="af5c0bf9fd20df7b4a4cdb7ce18fdc7fc"></a>

### `BT_HCI_ISO_TEST_MAX_SIZE_SDU`

```c
#define BT_HCI_ISO_TEST_MAX_SIZE_SDU 2
```

<a id="aed9e2581c74218e023100d63201721af"></a>

### `BT_HCI_ISO_TEST_VARIABLE_SIZE_SDU`

```c
#define BT_HCI_ISO_TEST_VARIABLE_SIZE_SDU 1
```

<a id="aa857bdd2e81c923ab540761986074557"></a>

### `BT_HCI_ISO_TEST_ZERO_SIZE_SDU`

```c
#define BT_HCI_ISO_TEST_ZERO_SIZE_SDU 0
```

<a id="a49f62e83dd51d17efd77c89337fdd537"></a>

### `BT_HCI_ISO_WORST_CASE_SCA_VALID_MASK`

```c
#define BT_HCI_ISO_WORST_CASE_SCA_VALID_MASK 0x07
```

<a id="a04a69a823bac190d0ac16f3c21481bde"></a>

### `BT_HCI_LE_1US_AOA_RX`

```c
#define BT_HCI_LE_1US_AOA_RX BIT(2)
```

<a id="a70edcf0bd7e63454996ef5d925e91bbf"></a>

### `BT_HCI_LE_1US_AOD_RX`

```c
#define BT_HCI_LE_1US_AOD_RX BIT(1)
```

<a id="a41aac54cd90cfc58990ce93124ce7077"></a>

### `BT_HCI_LE_1US_AOD_TX`

```c
#define BT_HCI_LE_1US_AOD_TX BIT(0)
```

<a id="ae8361a3ca39019757304034c32391b47"></a>

### `BT_HCI_LE_ADV_DISABLE`

```c
#define BT_HCI_LE_ADV_DISABLE 0x00
```

<a id="a6b8140956fbf85bd5aab2f1974b673f9"></a>

### `BT_HCI_LE_ADV_ENABLE`

```c
#define BT_HCI_LE_ADV_ENABLE 0x01
```

<a id="a4e3752dfde6a1f6ce6c7561b6c19657c"></a>

### `BT_HCI_LE_ADV_EVT_PHY_1M`

```c
#define BT_HCI_LE_ADV_EVT_PHY_1M 0x01
```

<a id="a0eae639d3066358da815743aa7ba2933"></a>

### `BT_HCI_LE_ADV_EVT_PHY_2M`

```c
#define BT_HCI_LE_ADV_EVT_PHY_2M 0x02
```

<a id="a865ad7eefd0051e7965bd5e391bf852c"></a>

### `BT_HCI_LE_ADV_EVT_PHY_CODED_S2`

```c
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S2 0x04
```

<a id="a51fd268794a726f7d9fa2fb4ce937507"></a>

### `BT_HCI_LE_ADV_EVT_PHY_CODED_S8`

```c
#define BT_HCI_LE_ADV_EVT_PHY_CODED_S8 0x03
```

<a id="ae448216e385d4e1175b92e112c941140"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_CONN`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_CONN BIT(0)
```

<a id="a9557bf3ea41a526fb9d628d2fd3d5bea"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS ( ev_type)
```

展开值（Value）：

```c
(((ev_type) >> 5) & 0x03)
```

<a id="a85720f3d88c7fa5da9dc9cdffb94ec87"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_COMPLETE`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_COMPLETE 0
```

<a id="abf119f5606440c075e61abcbfaa683c6"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_INCOMPLETE`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_INCOMPLETE 2
```

<a id="ab7842a3081c9bf5288275b57337955f2"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_PARTIAL`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_PARTIAL 1
```

<a id="ad9bcda2a43eed7e73112f2ef84cc6183"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_RX_FAILED`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DATA_STATUS_RX_FAILED 0xFF
```

<a id="a1b5738583447011ee63350787236b3b8"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_DIRECT`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_DIRECT BIT(2)
```

<a id="a0879fbea8bf3acbe56e25f3693c81ad6"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_LEGACY`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_LEGACY BIT(4)
```

<a id="a54673fbd23e05fec88e1f6bca6aa70e9"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_SCAN`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN BIT(1)
```

<a id="a485843f24c09934b1f15d5274b4a56d5"></a>

### `BT_HCI_LE_ADV_EVT_TYPE_SCAN_RSP`

```c
#define BT_HCI_LE_ADV_EVT_TYPE_SCAN_RSP BIT(3)
```

<a id="a12d97417fa11a07b0af5370b595e9a17"></a>

### `BT_HCI_LE_ADV_HANDLE_MAX`

```c
#define BT_HCI_LE_ADV_HANDLE_MAX 0xEF
```

<a id="a2ba70856f1e7fe8c6e7990ac9cdf5aaa"></a>

### `BT_HCI_LE_ADV_PHY_OPTION_NO_REQUIRED`

```c
#define BT_HCI_LE_ADV_PHY_OPTION_NO_REQUIRED 0x00
```

<a id="ac707220fea6b3fc077b8b85267ed0030"></a>

### `BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S2`

```c
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S2 0x03
```

<a id="aab845a49577d93974b468187c948beff"></a>

### `BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S8`

```c
#define BT_HCI_LE_ADV_PHY_OPTION_REQUIRE_S8 0x04
```

<a id="a21c60f21a4de9136accc32b0a8a0325c"></a>

### `BT_HCI_LE_ADV_PROP_ANON`

```c
#define BT_HCI_LE_ADV_PROP_ANON BIT(5)
```

<a id="ac9597c1c284e23578352a23bd66c9fad"></a>

### `BT_HCI_LE_ADV_PROP_CONN`

```c
#define BT_HCI_LE_ADV_PROP_CONN BIT(0)
```

<a id="acd154c93af2dc866cfe8bcf8e370dd3d"></a>

### `BT_HCI_LE_ADV_PROP_DIRECT`

```c
#define BT_HCI_LE_ADV_PROP_DIRECT BIT(2)
```

<a id="a0fb43dd85c3671420029027cbfbf8c11"></a>

### `BT_HCI_LE_ADV_PROP_HI_DC_CONN`

```c
#define BT_HCI_LE_ADV_PROP_HI_DC_CONN BIT(3)
```

<a id="a936310de47af573e0d1d5d9401097ba1"></a>

### `BT_HCI_LE_ADV_PROP_LEGACY`

```c
#define BT_HCI_LE_ADV_PROP_LEGACY BIT(4)
```

<a id="ab886c4c7f33adf396ca3e09d0f38995d"></a>

### `BT_HCI_LE_ADV_PROP_SCAN`

```c
#define BT_HCI_LE_ADV_PROP_SCAN BIT(1)
```

<a id="abd14685442f2fe315a095516464fc92d"></a>

### `BT_HCI_LE_ADV_PROP_TX_POWER`

```c
#define BT_HCI_LE_ADV_PROP_TX_POWER BIT(6)
```

<a id="aa1f4b7ba3b48ea6bd7b8a34a7b831a25"></a>

### `BT_HCI_LE_ADV_SCAN_REQ_DISABLE`

```c
#define BT_HCI_LE_ADV_SCAN_REQ_DISABLE 0
```

<a id="a39fa8033dcf14aa43dfad7cabc1cb429"></a>

### `BT_HCI_LE_ADV_SCAN_REQ_ENABLE`

```c
#define BT_HCI_LE_ADV_SCAN_REQ_ENABLE 1
```

<a id="aa3bfec7459966cf805afcf5186d53103"></a>

### `BT_HCI_LE_ADV_TX_POWER_MAX`

```c
#define BT_HCI_LE_ADV_TX_POWER_MAX 20
```

最大广播发射功率（Advertising TX Power），单位为 dBm；参见《核心规范》第 4 卷 E 部分 7.8.53。

<a id="aa4ce6784e6ee46069fd109dc1869e716"></a>

### `BT_HCI_LE_ADV_TX_POWER_MIN`

```c
#define BT_HCI_LE_ADV_TX_POWER_MIN -127
```

最小广播发射功率（Advertising TX Power），单位为 dBm；参见《核心规范》第 4 卷 E 部分 7.8.53。

<a id="a7f4fcc517033a4743ded39503b35ce29"></a>

### `BT_HCI_LE_ADV_TX_POWER_NO_PREF`

```c
#define BT_HCI_LE_ADV_TX_POWER_NO_PREF 0x7F
```

广播发射功率（Advertising TX Power）：无偏好，由控制器选择。

<a id="a1410330e31701a140eb8c0c73c943972"></a>

### `BT_HCI_LE_ANTENNA_SWITCHING_SLOT_1US`

```c
#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_1US 0x1
```

<a id="afa70fe0b1b9e277bfcb6bf7d6fc03564"></a>

### `BT_HCI_LE_ANTENNA_SWITCHING_SLOT_2US`

```c
#define BT_HCI_LE_ANTENNA_SWITCHING_SLOT_2US 0x2
```

<a id="a9b3306f29525c50cd8bd501f7391e518"></a>

### `BT_HCI_LE_AOA_CTE`

```c
#define BT_HCI_LE_AOA_CTE 0x0
```

<a id="ac80b68b1ca4f55a8a44b6bf0dfa7bfb3"></a>

### `BT_HCI_LE_AOA_CTE_RSP`

```c
#define BT_HCI_LE_AOA_CTE_RSP BIT(0)
```

<a id="a8569e960c44660eb41cdccbe5aeb6ead"></a>

### `BT_HCI_LE_AOD_CTE_1US`

```c
#define BT_HCI_LE_AOD_CTE_1US 0x1
```

<a id="a970732caa95f5742fc18c91efbc7095b"></a>

### `BT_HCI_LE_AOD_CTE_2US`

```c
#define BT_HCI_LE_AOD_CTE_2US 0x2
```

<a id="a124137512b0f87a67fff694359d629d0"></a>

### `BT_HCI_LE_AOD_CTE_RSP_1US`

```c
#define BT_HCI_LE_AOD_CTE_RSP_1US BIT(1)
```

<a id="a5c1dd462d05e4a5615f80402f892ecbc"></a>

### `BT_HCI_LE_AOD_CTE_RSP_2US`

```c
#define BT_HCI_LE_AOD_CTE_RSP_2US BIT(2)
```

<a id="afd311a47bbe6cdfac035c97b0b19b736"></a>

### `BT_HCI_LE_BIG_HANDLE_MAX`

```c
#define BT_HCI_LE_BIG_HANDLE_MAX 0xEFU
```

<a id="ab145283f399f65b5d576d83fe79d173a"></a>

### `BT_HCI_LE_BIG_HANDLE_MIN`

```c
#define BT_HCI_LE_BIG_HANDLE_MIN 0x00U
```

<a id="a70d6f103242dcd48f2c118ac82f9d358"></a>

### `BT_HCI_LE_BIG_SYNC_DELAY_MAX`

```c
#define BT_HCI_LE_BIG_SYNC_DELAY_MAX 0x7FFFFFU
```

<a id="ad6106a99804460b7aa68f52d5e322db1"></a>

### `BT_HCI_LE_BIG_SYNC_DELAY_MIN`

```c
#define BT_HCI_LE_BIG_SYNC_DELAY_MIN 0x000030U
```

<a id="a81b4b9ce53511c62889790a79b0f6a34"></a>

### `BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE`

```c
#define BT_HCI_LE_BYTES_PAGE_0_FEATURE_PAGE 8
```

<a id="ad0cf0a98dff26ba6aed21fa79bcd43f1"></a>

### `BT_HCI_LE_BYTES_PER_FEATURE_PAGE`

```c
#define BT_HCI_LE_BYTES_PER_FEATURE_PAGE 24
```

<a id="ac8dcea08127aa5ce2a870d64fcc843f1"></a>

### `BT_HCI_LE_CHAN_SEL_ALGO_1`

```c
#define BT_HCI_LE_CHAN_SEL_ALGO_1 0x00
```

<a id="a7a4b52643c764233427314732896d353"></a>

### `BT_HCI_LE_CHAN_SEL_ALGO_2`

```c
#define BT_HCI_LE_CHAN_SEL_ALGO_2 0x01
```

<a id="a811e0d38fa730e175efac792e5702ebd"></a>

### `BT_HCI_LE_CIG_SYNC_DELAY_MAX`

```c
#define BT_HCI_LE_CIG_SYNC_DELAY_MAX 0x7FFFFFU
```

7.7.65.25 LE CIS Established 事件所定义的连接等时组（CIG）最大同步延迟（Sync Delay）。

<a id="a875de5e9c3675c6bac301dab52733ae1"></a>

### `BT_HCI_LE_CIG_SYNC_DELAY_MIN`

```c
#define BT_HCI_LE_CIG_SYNC_DELAY_MIN 0x0000F2U
```

7.7.65.25 LE CIS Established 事件所定义的连接等时组（CIG）最小同步延迟（Sync Delay）。

<a id="acb49877cf9c9a0563ac20e7b5541f972"></a>

### `BT_HCI_LE_CIS_SYNC_DELAY_MAX`

```c
#define BT_HCI_LE_CIS_SYNC_DELAY_MAX 0x7FFFFFU
```

7.7.65.25 LE CIS Established 事件所定义的连接等时流（CIS）最大同步延迟（Sync Delay）。

<a id="af678f3fb040ad4b115fff082832d28e0"></a>

### `BT_HCI_LE_CIS_SYNC_DELAY_MIN`

```c
#define BT_HCI_LE_CIS_SYNC_DELAY_MIN 0x0000F2U
```

7.7.65.25 LE CIS Established 事件所定义的连接等时流（CIS）最小同步延迟（Sync Delay）。

<a id="aa2b9a667e0b80a4cf4d8cef9cb022ad4"></a>

### `BT_HCI_LE_CONTINUATION_NUM_MAX`

```c
#define BT_HCI_LE_CONTINUATION_NUM_MAX 0x01f3
```

<a id="a6ac68f277aff54739238ffdafb640f85"></a>

### `BT_HCI_LE_CONTINUATION_NUM_MIN`

```c
#define BT_HCI_LE_CONTINUATION_NUM_MIN (0x0000U)
```

<a id="ac04c2c0020d2972d6df169f39c421c08"></a>

### `BT_HCI_LE_CREATE_CONN_FP_FILTER`

```c
#define BT_HCI_LE_CREATE_CONN_FP_FILTER 0x01
```

<a id="ae1bd495a90fd902614014e7e1e2f1239"></a>

### `BT_HCI_LE_CREATE_CONN_FP_NO_FILTER`

```c
#define BT_HCI_LE_CREATE_CONN_FP_NO_FILTER 0x00
```

<a id="aa437d198f03b30ddbac6ada679e5e0c6"></a>

### `BT_HCI_LE_CS_CONFIG_ACTION_CREATED`

```c
#define BT_HCI_LE_CS_CONFIG_ACTION_CREATED 0x01
```

<a id="a9c815ae28e424256fc440b426ba69892"></a>

### `BT_HCI_LE_CS_CONFIG_ACTION_REMOVED`

```c
#define BT_HCI_LE_CS_CONFIG_ACTION_REMOVED 0x00
```

<a id="af457a20ddc90001f8a523a0e3df6a4bd"></a>

### `BT_HCI_LE_CS_INITIATOR_ROLE_MASK`

```c
#define BT_HCI_LE_CS_INITIATOR_ROLE_MASK BIT(0)
```

<a id="a62ab6fbe9acb92c4023f35ae8bb7b14b"></a>

### `BT_HCI_LE_CS_MODES_SUPPORTED_MODE_3_MASK`

```c
#define BT_HCI_LE_CS_MODES_SUPPORTED_MODE_3_MASK BIT(0)
```

<a id="a6b64cb407c353d7a143b7483cf16507f"></a>

### `BT_HCI_LE_CS_NADM_RANDOM_CAPABILITY_PHASE_BASED_MASK`

```c
#define BT_HCI_LE_CS_NADM_RANDOM_CAPABILITY_PHASE_BASED_MASK BIT(0)
```

<a id="a903505932b23ae60c59fc4f439f8f3ce"></a>

### `BT_HCI_LE_CS_NADM_SOUNDING_CAPABILITY_PHASE_BASED_MASK`

```c
#define BT_HCI_LE_CS_NADM_SOUNDING_CAPABILITY_PHASE_BASED_MASK BIT(0)
```

<a id="a014d9a06d3c571ce06c94a2ebfdbe4e5"></a>

### `BT_HCI_LE_CS_NOT_TONE_EXT_SLOT`

```c
#define BT_HCI_LE_CS_NOT_TONE_EXT_SLOT 0x0
```

<a id="abfedf14c97b27f6cdbbb66f2598734e9"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_LIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_LIKELY 0x06
```

<a id="a54895cd6caacff2dc5aee25e301144a7"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_UNLIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_EXT_UNLIKELY 0x00
```

<a id="a93f1786e8177c89eb9db36a72e367122"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_LIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_LIKELY 0x04
```

<a id="a73bf7224e934c28a73d5e54a632e0e69"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_POSSIBLE`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_POSSIBLE 0x03
```

<a id="acf2d6f7fd7873e12389a2d470241340f"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_UNLIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_UNLIKELY 0x02
```

<a id="a0b10dcb24c429d594b17eec494954d74"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_LIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_LIKELY 0x05
```

<a id="af10362bcbd6b95f8404654d258acdbcb"></a>

### `BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_UNLIKELY`

```c
#define BT_HCI_LE_CS_PACKET_NADM_ATTACK_VERY_UNLIKELY 0x01
```

<a id="a5f7d8e81a83a3b94e18a39b507232823"></a>

### `BT_HCI_LE_CS_PACKET_NADM_UNKNOWN`

```c
#define BT_HCI_LE_CS_PACKET_NADM_UNKNOWN 0xFF
```

<a id="af357550f37226be5b2b6491ebad3fd57"></a>

### `BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_AA_NOT_FOUND`

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_AA_NOT_FOUND 0x2
```

<a id="a7c0e4053873d629e10567937adc033d3"></a>

### `BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_BIT_ERRORS_FOUND`

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_BIT_ERRORS_FOUND 0x1
```

<a id="ab05d15713fb0145b32a5977774b50533"></a>

### `BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_SUCCESSFUL`

```c
#define BT_HCI_LE_CS_PACKET_QUALITY_AA_CHECK_SUCCESSFUL 0x0
```

<a id="a8ce6b3556a9f5b83648b80d90652f00d"></a>

### `BT_HCI_LE_CS_PACKET_RSSI_NOT_AVAILABLE`

```c
#define BT_HCI_LE_CS_PACKET_RSSI_NOT_AVAILABLE 0x7F
```

<a id="af69d92b7c92c8fbeeba8e14838a41f74"></a>

### `BT_HCI_LE_CS_PCT_I_MASK`

```c
#define BT_HCI_LE_CS_PCT_I_MASK 0x000FFF
```

<a id="a1720b6024f6156e98cb407d6e06e894e"></a>

### `BT_HCI_LE_CS_PCT_Q_MASK`

```c
#define BT_HCI_LE_CS_PCT_Q_MASK 0xFFF000
```

<a id="ae8446a2638bd4009b7dee725bb54c883"></a>

### `BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED`

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_CHMAP_INSTANT_PASSED 0x3
```

<a id="a21eb191c5d99f902c7a244cad685995f"></a>

### `BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST`

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
```

<a id="a056a67d663cfdc2189b480fc79946c74"></a>

### `BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT`

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_NO_ABORT 0x0
```

<a id="a6dc3f766ce40bbd0ddb7af3cf85677b1"></a>

### `BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS`

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_TOO_FEW_CHANNELS 0x2
```

<a id="a1e92177f7be3c6a6be00f97fbfc17dcf"></a>

### `BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED`

```c
#define BT_HCI_LE_CS_PROCEDURE_ABORT_REASON_UNSPECIFIED 0xF
```

<a id="a821a29dacea9867e4e576f916cf7be3d"></a>

### `BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED`

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_ABORTED 0xF
```

<a id="ace872d54fba6d94d62b59a2373c7d0d5"></a>

### `BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE`

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_COMPLETE 0x0
```

<a id="af057e8492e52d0c8763d4a2e969d949d"></a>

### `BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL`

```c
#define BT_HCI_LE_CS_PROCEDURE_DONE_STATUS_PARTIAL 0x1
```

<a id="aa4345ca4225d3958968131ba7a5ff950"></a>

### `BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE`

```c
#define BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE 0x7F
```

<a id="a4c42a75a04962264257c690ba80f6126"></a>

### `BT_HCI_LE_CS_REFLECTOR_ROLE_MASK`

```c
#define BT_HCI_LE_CS_REFLECTOR_ROLE_MASK BIT(1)
```

<a id="ab7843d7e6463e96bce693b82c3f8cc7d"></a>

### `BT_HCI_LE_CS_RTT_AA_ONLY_N_10NS_MASK`

```c
#define BT_HCI_LE_CS_RTT_AA_ONLY_N_10NS_MASK BIT(0)
```

<a id="a2135776cd2413e80b3ad653405f0ec67"></a>

### `BT_HCI_LE_CS_RTT_RANDOM_PAYLOAD_N_10NS_MASK`

```c
#define BT_HCI_LE_CS_RTT_RANDOM_PAYLOAD_N_10NS_MASK BIT(2)
```

<a id="ad701c1822a44a639bf5a576bf291544f"></a>

### `BT_HCI_LE_CS_RTT_SOUNDING_N_10NS_MASK`

```c
#define BT_HCI_LE_CS_RTT_SOUNDING_N_10NS_MASK BIT(1)
```

<a id="a41bbe08db99fb0a2ef77f4f3103f9b6c"></a>

### `BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST`

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_LOCAL_HOST_OR_REMOTE_REQUEST 0x1
```

<a id="a095b6061c31229b951b6b96e5d02381f"></a>

### `BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT`

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_ABORT 0x0
```

<a id="ac4817c265c50019d8f74146f7477bf58"></a>

### `BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED`

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_NO_CS_SYNC_RECEIVED 0x2
```

<a id="a31cb520a05fe31313bacf8b021da468c"></a>

### `BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT`

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_SCHED_CONFLICT 0x3
```

<a id="abfdca3ae615e19c8e24c098ba8349618"></a>

### `BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED`

```c
#define BT_HCI_LE_CS_SUBEVENT_ABORT_REASON_UNSPECIFIED 0xF
```

<a id="af1907f8ae481a08c674d86e689826f49"></a>

### `BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED`

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_ABORTED 0xF
```

<a id="aee251ce3c46dc0404d880be7d4550fa6"></a>

### `BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE`

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_COMPLETE 0x0
```

<a id="a414d620018a946fcb6c209b21ad6fb00"></a>

### `BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_PARTIAL`

```c
#define BT_HCI_LE_CS_SUBEVENT_DONE_STATUS_PARTIAL 0x1
```

<a id="a385a401b373522160b1832b66838e02d"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE 0xC000
```

<a id="ae3e9f6d380a61278a8082f07694bdf43"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_1`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_1 0x01
```

<a id="ad6951a0000c3b5cadfbaae94decb153f"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_2`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_2 0x02
```

<a id="aaeb365c3f3ea16d760d4943587ea0bd7"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_3`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_3 0x03
```

<a id="a4cf750ee707ca0b81d4945e4f66798e3"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_4`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_4 0x04
```

<a id="a6efdde19fbbf06a40d5dc8dee0515af8"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_IGNORED`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_N_AP_IGNORED 0x00
```

<a id="a22b108e24f198dfd41b2ad692d448c01"></a>

### `BT_HCI_LE_CS_SUBEVENT_RESULT_PCT_NOT_AVAILABLE`

```c
#define BT_HCI_LE_CS_SUBEVENT_RESULT_PCT_NOT_AVAILABLE 0xFFFFFFFF
```

<a id="a5a7e8927e6086b70177cc04915d16ff8"></a>

### `BT_HCI_LE_CS_SUBFEATURE_CHSEL_ALG_3C_MASK`

```c
#define BT_HCI_LE_CS_SUBFEATURE_CHSEL_ALG_3C_MASK BIT(2)
```

<a id="ab14fe72c7edfc6ccf24fd9347240a395"></a>

### `BT_HCI_LE_CS_SUBFEATURE_CS_IPT_REFLECTOR_MASK`

```c
#define BT_HCI_LE_CS_SUBFEATURE_CS_IPT_REFLECTOR_MASK BIT(4)
```

子功能：反射端（Reflector）中的带 IPT 的信道探测（CS with IPT）。

<a id="a2241cba5ca0dbeb1ea19797654c97397"></a>

### `BT_HCI_LE_CS_SUBFEATURE_NO_TX_FAE_MASK`

```c
#define BT_HCI_LE_CS_SUBFEATURE_NO_TX_FAE_MASK BIT(1)
```

<a id="a4bcdc621f0292fd182f47762a2cf16bb"></a>

### `BT_HCI_LE_CS_SUBFEATURE_PBR_FROM_RTT_SOUNDING_SEQ_MASK`

```c
#define BT_HCI_LE_CS_SUBFEATURE_PBR_FROM_RTT_SOUNDING_SEQ_MASK BIT(3)
```

<a id="aeba1a6050a1ff6ad3864132015063026"></a>

### `BT_HCI_LE_CS_SYNC_PHYS_2M_2BT_MASK`

```c
#define BT_HCI_LE_CS_SYNC_PHYS_2M_2BT_MASK BIT(2)
```

<a id="ad8742ec8b365df1850b6e5f56c39e655"></a>

### `BT_HCI_LE_CS_SYNC_PHYS_2M_MASK`

```c
#define BT_HCI_LE_CS_SYNC_PHYS_2M_MASK BIT(1)
```

<a id="acc787bc6363f4c885816a677f7c47db7"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_100US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_100US_MASK BIT(7)
```

<a id="a40d5f49728ef8204e9b19be3da28a5ae"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_1200US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_1200US_MASK BIT(8)
```

<a id="ac1138ac8f702b4b79bc03c9a7d60207b"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_15US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_15US_MASK BIT(0)
```

<a id="a7023db07ddc8f9e9fbfc59283511bafb"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_20US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_20US_MASK BIT(1)
```

<a id="a77aea9f93d8bcc5949abddcbda52d919"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_30US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_30US_MASK BIT(2)
```

<a id="a93fc4d9abc1964278748d7dacec7d15a"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_40US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_40US_MASK BIT(3)
```

<a id="a9f45646b734d3d831d307485d2c8c076"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_50US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_50US_MASK BIT(4)
```

<a id="a27771be57984aac0b825b3ff033df070"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_60US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_60US_MASK BIT(5)
```

<a id="ab9c3168510c3e5161c393d7093c3527b"></a>

### `BT_HCI_LE_CS_T_FCS_TIME_80US_MASK`

```c
#define BT_HCI_LE_CS_T_FCS_TIME_80US_MASK BIT(6)
```

<a id="a85f667356dd1e1d9de288776ec13e721"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_10US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_10US_MASK BIT(0)
```

<a id="a331eff3b3e89a073b30c9d334014b2da"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_20US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_20US_MASK BIT(1)
```

<a id="a62112179c80be4546b29bc39f632f619"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_30US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_30US_MASK BIT(2)
```

<a id="a57232d7cbd988c6d6d01d2462e90a7f5"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_40US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_40US_MASK BIT(3)
```

<a id="a4aa0365eb6bc4f54bbbd3ebc2b717c41"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_50US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_50US_MASK BIT(4)
```

<a id="a647ea407f97ea754f3f729ac8a9bbb02"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_60US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_60US_MASK BIT(5)
```

<a id="a8bd6f366622ed48cea49fc67692349ce"></a>

### `BT_HCI_LE_CS_T_IP1_TIME_80US_MASK`

```c
#define BT_HCI_LE_CS_T_IP1_TIME_80US_MASK BIT(6)
```

<a id="a46420b559fcc0e584bc604790ae066ae"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_10US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_10US_MASK BIT(0)
```

<a id="a5d279467b3b0b239748b23be57fee63b"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_20US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_20US_MASK BIT(1)
```

<a id="a95d5e9901c50e579600db0ef160425eb"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_30US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_30US_MASK BIT(2)
```

<a id="a66b0bca7c0b19f43b6871cdf05e57543"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_40US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_40US_MASK BIT(3)
```

<a id="a875fa244820e7aea6f1d6674e3d7d72a"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_50US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_50US_MASK BIT(4)
```

<a id="ab73d093bcb50ebdd5630e85677af6223"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_60US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_60US_MASK BIT(5)
```

<a id="a6d6e20505ba9b86bc254bc3419e5bc04"></a>

### `BT_HCI_LE_CS_T_IP2_TIME_80US_MASK`

```c
#define BT_HCI_LE_CS_T_IP2_TIME_80US_MASK BIT(6)
```

<a id="a46f2a35868d8422878e89f1ddde0e7dc"></a>

### `BT_HCI_LE_CS_T_PM_TIME_10US_MASK`

```c
#define BT_HCI_LE_CS_T_PM_TIME_10US_MASK BIT(0)
```

<a id="a68e13620f22327e8e132aeb19a7cdaf6"></a>

### `BT_HCI_LE_CS_T_PM_TIME_20US_MASK`

```c
#define BT_HCI_LE_CS_T_PM_TIME_20US_MASK BIT(1)
```

<a id="aa615aebe1d896ca1a06bf618619d96f7"></a>

### `BT_HCI_LE_CS_TEST_CONN_HANDLE`

```c
#define BT_HCI_LE_CS_TEST_CONN_HANDLE 0x0FFF
```

<a id="ad0895b572ba1e3d763dbef69c1541b2c"></a>

### `BT_HCI_LE_CS_TIME_DIFFERENCE_NOT_AVAILABLE`

```c
#define BT_HCI_LE_CS_TIME_DIFFERENCE_NOT_AVAILABLE ((int16_t)0x8000)
```

<a id="a932802d089c04b78dd6a541b3ddff1e1"></a>

### `BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_EXPECTED`

```c
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_EXPECTED 0x2
```

<a id="a72a59878b1445b037eb633a374de92e8"></a>

### `BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_NOT_EXPECTED`

```c
#define BT_HCI_LE_CS_TONE_EXT_SLOT_EXT_NOT_EXPECTED 0x1
```

<a id="adcc92fe105d853cc329bbf4340562835"></a>

### `BT_HCI_LE_CS_TONE_QUALITY_HIGH`

```c
#define BT_HCI_LE_CS_TONE_QUALITY_HIGH 0x0
```

<a id="accc9e73d5fd38c6ab3d108bc3fd039de"></a>

### `BT_HCI_LE_CS_TONE_QUALITY_LOW`

```c
#define BT_HCI_LE_CS_TONE_QUALITY_LOW 0x2
```

<a id="af42a419097a2e8ee37d46419cd5e20c3"></a>

### `BT_HCI_LE_CS_TONE_QUALITY_MED`

```c
#define BT_HCI_LE_CS_TONE_QUALITY_MED 0x1
```

<a id="a2b14945754c982ead67ad3b7e615eba9"></a>

### `BT_HCI_LE_CS_TONE_QUALITY_UNAVAILABLE`

```c
#define BT_HCI_LE_CS_TONE_QUALITY_UNAVAILABLE 0x3
```

<a id="a24c56f19fcf03aabb170925555209f33"></a>

### `BT_HCI_LE_CS_TX_SNR_CAPABILITY_18DB_MASK`

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_18DB_MASK BIT(0)
```

<a id="a80fe1748abbd89e1700c239ff450ce07"></a>

### `BT_HCI_LE_CS_TX_SNR_CAPABILITY_21DB_MASK`

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_21DB_MASK BIT(1)
```

<a id="acd8cc2c9de0edd52c954b0d70dfa44ac"></a>

### `BT_HCI_LE_CS_TX_SNR_CAPABILITY_24DB_MASK`

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_24DB_MASK BIT(2)
```

<a id="a1f27b2456c323b90eebfa8e45932d92f"></a>

### `BT_HCI_LE_CS_TX_SNR_CAPABILITY_27DB_MASK`

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_27DB_MASK BIT(3)
```

<a id="a5045b5b06b3c79c77a4997066f332d13"></a>

### `BT_HCI_LE_CS_TX_SNR_CAPABILITY_30DB_MASK`

```c
#define BT_HCI_LE_CS_TX_SNR_CAPABILITY_30DB_MASK BIT(4)
```

<a id="a442df4f693ae5bb75d1d8f54fe204bda"></a>

### `BT_HCI_LE_CTE_COUNT_MAX`

```c
#define BT_HCI_LE_CTE_COUNT_MAX 0x10
```

<a id="aec2a77fadbb6bf24267d659a84b7c9a9"></a>

### `BT_HCI_LE_CTE_COUNT_MIN`

```c
#define BT_HCI_LE_CTE_COUNT_MIN 0x1
```

<a id="a478bc1be161e0b1eb05667bc8b6c9ae5"></a>

### `BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_OTHER`

```c
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_OTHER 0x2
```

<a id="a3f787f516c3cc233fc700c08552a4034"></a>

### `BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_TIME`

```c
#define BT_HCI_LE_CTE_CRC_ERR_CTE_BASED_TIME 0x1
```

<a id="ac1ce16d42df9eb71860e51a843dbc943"></a>

### `BT_HCI_LE_CTE_CRC_OK`

```c
#define BT_HCI_LE_CTE_CRC_OK 0x0
```

<a id="a3bc1e15287e6173d45b7d1e981d6e90e"></a>

### `BT_HCI_LE_CTE_INSUFFICIENT_RESOURCES`

```c
#define BT_HCI_LE_CTE_INSUFFICIENT_RESOURCES 0xFF
```

<a id="acdfe03ade99fa88779b68e435aea23e3"></a>

### `BT_HCI_LE_CTE_LEN_MAX`

```c
#define BT_HCI_LE_CTE_LEN_MAX 0x14
```

<a id="a80376d34b4d701d5f6092aa101ce0e6c"></a>

### `BT_HCI_LE_CTE_LEN_MIN`

```c
#define BT_HCI_LE_CTE_LEN_MIN 0x2
```

<a id="a40156c4680916b289b00b1546e0d5bb0"></a>

### `BT_HCI_LE_CTE_REPORT_NO_VALID_SAMPLE`

```c
#define BT_HCI_LE_CTE_REPORT_NO_VALID_SAMPLE 0x80
```

<a id="a4d9626f1b9f0601708b3c38386b5f85c"></a>

### `BT_HCI_LE_EXT_ADV_FRAG_DISABLED`

```c
#define BT_HCI_LE_EXT_ADV_FRAG_DISABLED 0x01
```

<a id="aa1dbb6b62c021501320865ac77b5d6da"></a>

### `BT_HCI_LE_EXT_ADV_FRAG_ENABLED`

```c
#define BT_HCI_LE_EXT_ADV_FRAG_ENABLED 0x00
```

<a id="a3b3f91c046b0656d489c228d75c8b3ff"></a>

### `BT_HCI_LE_EXT_ADV_FRAG_MAX_LEN`

```c
#define BT_HCI_LE_EXT_ADV_FRAG_MAX_LEN 251
```

<a id="a5394a0dbcd3856ffb8c63440d352120b"></a>

### `BT_HCI_LE_EXT_ADV_OP_COMPLETE_DATA`

```c
#define BT_HCI_LE_EXT_ADV_OP_COMPLETE_DATA 0x03
```

<a id="a65b3ae46e1164815cda1325e55df4091"></a>

### `BT_HCI_LE_EXT_ADV_OP_FIRST_FRAG`

```c
#define BT_HCI_LE_EXT_ADV_OP_FIRST_FRAG 0x01
```

<a id="a68c62ac99c4198dbadf6563e40ce33cb"></a>

### `BT_HCI_LE_EXT_ADV_OP_INTERM_FRAG`

```c
#define BT_HCI_LE_EXT_ADV_OP_INTERM_FRAG 0x00
```

<a id="aade6b8cac66aee356c857fcfae17ce65"></a>

### `BT_HCI_LE_EXT_ADV_OP_LAST_FRAG`

```c
#define BT_HCI_LE_EXT_ADV_OP_LAST_FRAG 0x02
```

<a id="a2860ae578d2332a1c76c7bfaa0714e08"></a>

### `BT_HCI_LE_EXT_ADV_OP_UNCHANGED_DATA`

```c
#define BT_HCI_LE_EXT_ADV_OP_UNCHANGED_DATA 0x04
```

<a id="a5fcf4bb36d4ebe25706c1b71431eb12f"></a>

### `BT_HCI_LE_EXT_ADV_REPORT_MAX_NUM_REPORTS`

```c
#define BT_HCI_LE_EXT_ADV_REPORT_MAX_NUM_REPORTS 0x0a
```

低功耗蓝牙扩展广播报告（LE Extended Advertising Report）中的最大报告数量。

<a id="a973c2e0fc4cb22d58c47865b9e76b940"></a>

### `BT_HCI_LE_EXT_ADV_SID_INVALID`

```c
#define BT_HCI_LE_EXT_ADV_SID_INVALID 0xFF
```

<a id="ae9ba6da1a01dacc52c6a1a2c84d16948"></a>

### `BT_HCI_LE_EXT_SCAN_FILTER_DUP_ENABLE_RESET`

```c
#define BT_HCI_LE_EXT_SCAN_FILTER_DUP_ENABLE_RESET 0x02
```

<a id="a0ef6a16a2b042b3e7623210fc5fcd1a0"></a>

### `BT_HCI_LE_EXT_SCAN_PHY_1M`

```c
#define BT_HCI_LE_EXT_SCAN_PHY_1M BIT(0)
```

<a id="ad0f0fe21e4e9136e09e0a443a7253759"></a>

### `BT_HCI_LE_EXT_SCAN_PHY_2M`

```c
#define BT_HCI_LE_EXT_SCAN_PHY_2M BIT(1)
```

<a id="ae15b1ae9e35d060b3a9619d293a7d9ac"></a>

### `BT_HCI_LE_EXT_SCAN_PHY_CODED`

```c
#define BT_HCI_LE_EXT_SCAN_PHY_CODED BIT(2)
```

<a id="a399c04a940168b9767f3126268dd684e"></a>

### `BT_HCI_LE_FEATURE_PAGE_MAX`

```c
#define BT_HCI_LE_FEATURE_PAGE_MAX 10
```

<a id="a45ff3a04cd0179ed02576136114ed8c0"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_CONTROLLER (1)
```

<a id="a076869aba2dc8593b2263c642cdaa148"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_LOCAL_HOST (0)
```

<a id="acb1d2b1b3e2e1802b81dbeb82bcc9f12"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_INITIATOR_PEER (2)
```

<a id="a5dc8fa3e7157ca71b48a3cde12115664"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_1M_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_1M_MASK BIT(0)
```

<a id="a82ebdbd872d0d2905b2c29d15b1a019d"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_2M_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_2M_MASK BIT(1)
```

<a id="a5d63134bfa327abae3cf2d7a67980f39"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_CODED_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_CODED_MASK BIT(2)
```

<a id="a1ff1899e87988795cb56cf3ac69fc661"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_CP_MASK BIT(0)
```

<a id="ac390cbfa78d9027cbb6b9cda5e11c9c6"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_ACL_PC_MASK BIT(1)
```

<a id="a7f490f8f8ac13199da1c2af10adea5de"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_IFS_CIS_MASK BIT(3)
```

<a id="af7216a6ef4ccc35e081d7b18513af2d2"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MCES_MASK BIT(2)
```

<a id="a1e3128522364b82dc7a3ba05f89b96fc"></a>

### `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK`

```c
#define BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_MSS_CIS_MASK BIT(4)
```

<a id="a23ce5829beb61d9db40fedfce35c368e"></a>

### `BT_HCI_LE_INTERVAL_MAX`

```c
#define BT_HCI_LE_INTERVAL_MAX 0x0c80
```

<a id="adcf6bcefe1d8a34f65597730910bab69"></a>

### `BT_HCI_LE_INTERVAL_MIN`

```c
#define BT_HCI_LE_INTERVAL_MIN 0x0006
```

所有限制均依据《蓝牙核心规范》（BT Core Spec）v5.4，第 4 卷 E 部分。

<a id="aba0e61062d66e72b84c55662d00e03af"></a>

### `BT_HCI_LE_INTERVAL_UNIT_US`

```c
#define BT_HCI_LE_INTERVAL_UNIT_US (1250U)
```

<a id="a71f16c552b14042c00e98ea20c1e03c4"></a>

### `BT_HCI_LE_KEY_TYPE_DEBUG`

```c
#define BT_HCI_LE_KEY_TYPE_DEBUG 0x01
```

<a id="ac85ab1283cd175fc575ebd98b52b3335"></a>

### `BT_HCI_LE_KEY_TYPE_GENERATED`

```c
#define BT_HCI_LE_KEY_TYPE_GENERATED 0x00
```

<a id="af54ba281111d90f3edb77c0abf9c57b1"></a>

### `BT_HCI_LE_MAX_CTE_LEN_MAX`

```c
#define BT_HCI_LE_MAX_CTE_LEN_MAX 0x14
```

<a id="adee7271e25e6d66ba434502ab56674c3"></a>

### `BT_HCI_LE_MAX_CTE_LEN_MIN`

```c
#define BT_HCI_LE_MAX_CTE_LEN_MIN 0x2
```

<a id="a72d22456f1eb112a75b91faa40e3b776"></a>

### `BT_HCI_LE_MAX_RX_OCTETS_MAX`

```c
#define BT_HCI_LE_MAX_RX_OCTETS_MAX 0x00FB
```

<a id="a6c192a213459f5cc7898faa8aa0f5f42"></a>

### `BT_HCI_LE_MAX_RX_OCTETS_MIN`

```c
#define BT_HCI_LE_MAX_RX_OCTETS_MIN 0x001B
```

<a id="ad4c16d0e80cb6dc2b6fd65e72e331173"></a>

### `BT_HCI_LE_MAX_RX_TIME_MAX`

```c
#define BT_HCI_LE_MAX_RX_TIME_MAX 0x4290
```

<a id="a6666cbeff0cb43fa4c820ba92311fc11"></a>

### `BT_HCI_LE_MAX_RX_TIME_MIN`

```c
#define BT_HCI_LE_MAX_RX_TIME_MIN 0x0148
```

<a id="a647de996dd2e75a8242e6459abd565f6"></a>

### `BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MAX`

```c
#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MAX 0x4B
```

<a id="a327330c5b69e8ec56dd18fcc3fdf0622"></a>

### `BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MIN`

```c
#define BT_HCI_LE_MAX_SWITCH_PATTERN_LEN_MIN 0x2
```

<a id="aec6c2a321f9700572fe8cf84d8bed238"></a>

### `BT_HCI_LE_MAX_TX_OCTETS_MAX`

```c
#define BT_HCI_LE_MAX_TX_OCTETS_MAX 0x00FB
```

<a id="a6c731f3c0644818489c146eeca9e3ea8"></a>

### `BT_HCI_LE_MAX_TX_OCTETS_MIN`

```c
#define BT_HCI_LE_MAX_TX_OCTETS_MIN 0x001B
```

<a id="aae4ce04bdfd0ad339c87eb18616d8a8a"></a>

### `BT_HCI_LE_MAX_TX_TIME_MAX`

```c
#define BT_HCI_LE_MAX_TX_TIME_MAX 0x4290
```

<a id="ac7c6251a5342a591ff4c413820125f94"></a>

### `BT_HCI_LE_MAX_TX_TIME_MIN`

```c
#define BT_HCI_LE_MAX_TX_TIME_MIN 0x0148
```

<a id="ac6ae380e312559c82742975cf5ed742f"></a>

### `BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US`

```c
#define BT_HCI_LE_MIN_SUPP_CONN_INT_MAX_US (7500U)
```

<a id="ac5dd60afc8c8bff309090fca1b6875aa"></a>

### `BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US`

```c
#define BT_HCI_LE_MIN_SUPP_CONN_INT_MIN_US (375U)
```

<a id="a423acd131760a1ab7b0671c45c9214ca"></a>

### `BT_HCI_LE_MOD_INDEX_STABLE`

```c
#define BT_HCI_LE_MOD_INDEX_STABLE 0x01
```

<a id="a631e672ab64e36a983d4d3aae789b237"></a>

### `BT_HCI_LE_MOD_INDEX_STANDARD`

```c
#define BT_HCI_LE_MOD_INDEX_STANDARD 0x00
```

<a id="aeee9fd73771de54542f7ff24f95eceba"></a>

### `BT_HCI_LE_NO_CTE`

```c
#define BT_HCI_LE_NO_CTE 0xFF
```

<a id="ad9ff685b2854b877e0cdd1ae93272ddf"></a>

### `BT_HCI_LE_NUM_ANT_MAX`

```c
#define BT_HCI_LE_NUM_ANT_MAX 0x4B
```

<a id="a112d3fb3d3ec663278aa4463fedbd89b"></a>

### `BT_HCI_LE_NUM_ANT_MIN`

```c
#define BT_HCI_LE_NUM_ANT_MIN 0x1
```

<a id="a3a3937965aeb187b6fb18da3b7731ed7"></a>

### `BT_HCI_LE_PAST_CTE_TYPE_NO_AOA`

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOA BIT(0)
```

<a id="a440aca4bf97bc6b583284ae6c8037a53"></a>

### `BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_1US`

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_1US BIT(1)
```

<a id="ae2d9be5e54595cb5a426ae8909cdee1c"></a>

### `BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_2US`

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_AOD_2US BIT(2)
```

<a id="af3d8cf0fb8af60c057ba8c24abaf3897"></a>

### `BT_HCI_LE_PAST_CTE_TYPE_NO_CTE`

```c
#define BT_HCI_LE_PAST_CTE_TYPE_NO_CTE BIT(3)
```

<a id="a6fca2634e0e5b0dd5d86b18666ed38e4"></a>

### `BT_HCI_LE_PAST_CTE_TYPE_ONLY_CTE`

```c
#define BT_HCI_LE_PAST_CTE_TYPE_ONLY_CTE BIT(4)
```

<a id="ac7233f9c34f5e33d765b68b55ebc9b9e"></a>

### `BT_HCI_LE_PAST_MODE_NO_REPORTS`

```c
#define BT_HCI_LE_PAST_MODE_NO_REPORTS 0x01
```

<a id="a65ff1c4a937422000f6f1eadea28ccba"></a>

### `BT_HCI_LE_PAST_MODE_NO_SYNC`

```c
#define BT_HCI_LE_PAST_MODE_NO_SYNC 0x00
```

<a id="aaeac19606d3d5e7d0906b38e2c4b4c69"></a>

### `BT_HCI_LE_PAST_MODE_SYNC`

```c
#define BT_HCI_LE_PAST_MODE_SYNC 0x02
```

<a id="ab0232a2abc2b7c86b19ae89298ef8c4b"></a>

### `BT_HCI_LE_PAST_MODE_SYNC_FILTER_DUPLICATES`

```c
#define BT_HCI_LE_PAST_MODE_SYNC_FILTER_DUPLICATES 0x03
```

<a id="a9faae90b3adfcbcdf7da19c631e68a69"></a>

### `BT_HCI_LE_PATH_LOSS_REPORTING_DISABLE`

```c
#define BT_HCI_LE_PATH_LOSS_REPORTING_DISABLE 0x00
```

<a id="ab2e698e4ebbb45d9e3db0663ae5e4657"></a>

### `BT_HCI_LE_PATH_LOSS_REPORTING_ENABLE`

```c
#define BT_HCI_LE_PATH_LOSS_REPORTING_ENABLE 0x01
```

<a id="a0408b7ecb697bd573b2ea7d2c3c93b92"></a>

### `BT_HCI_LE_PATH_LOSS_UNAVAILABLE`

```c
#define BT_HCI_LE_PATH_LOSS_UNAVAILABLE 0xFF
```

<a id="a4c884821e7136f6f68bc4d92b394381a"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS 5
```

<a id="a6ad9e08bcef788c32481756f76df6a43"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_INVALID_VALUE`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_INVALID_VALUE (~BIT_MASK(BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ALLOWED_BITS))
```

<a id="a64c7e74877c8ca638217a09d503e742b"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOA`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOA BIT(0)
```

<a id="ad349244f13388a7437651e5c3909bcb9"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_1US`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_1US BIT(1)
```

<a id="aae32740df5a3096a9b17b9c06e6cc3e9"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_2US`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_AOD_2US BIT(2)
```

<a id="a5532c8ee93198eb831c12b182e13a534"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_CTE`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_CTE BIT(3)
```

<a id="abb3c8fcfc0b48cf6dbebff206a2a9a48"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_FILTERING`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_NO_FILTERING 0
```

<a id="aa3b526ab2ed1aeaab0e26a5390b3dcea"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ONLY_CTE`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_CTE_TYPE_ONLY_CTE BIT(4)
```

<a id="a29c5cf397f94af42bdea484fa95a2a78"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_FILTER_DUPLICATE`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_FILTER_DUPLICATE BIT(2)
```

<a id="a44f11af392e3188e699d8f987cb2f6d6"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_REPORTS_DISABLED`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_REPORTS_DISABLED BIT(1)
```

<a id="a490bb7d8cf236e49c60771a95d258247"></a>

### `BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_USE_LIST`

```c
#define BT_HCI_LE_PER_ADV_CREATE_SYNC_FP_USE_LIST BIT(0)
```

<a id="a7b3cd7870ba4af2ff483a831d2700466"></a>

### `BT_HCI_LE_PER_ADV_FRAG_MAX_LEN`

```c
#define BT_HCI_LE_PER_ADV_FRAG_MAX_LEN 252
```

<a id="a2f2216a88cf77ccac1c9a2f6c5820746"></a>

### `BT_HCI_LE_PER_ADV_INTERVAL_MAX`

```c
#define BT_HCI_LE_PER_ADV_INTERVAL_MAX 0xFFFF
```

<a id="a04f870ac03c1baca22ab5d984354f3bf"></a>

### `BT_HCI_LE_PER_ADV_INTERVAL_MIN`

```c
#define BT_HCI_LE_PER_ADV_INTERVAL_MIN 0x0006
```

<a id="ada39c45c3c1c7576d4d9794dad115e61"></a>

### `BT_HCI_LE_PER_ADV_OP_COMPLETE_DATA`

```c
#define BT_HCI_LE_PER_ADV_OP_COMPLETE_DATA 0x03
```

<a id="a8aeb4c76ec769879fc4796fc2919c459"></a>

### `BT_HCI_LE_PER_ADV_OP_FIRST_FRAG`

```c
#define BT_HCI_LE_PER_ADV_OP_FIRST_FRAG 0x01
```

<a id="aa18edf54edfb8d0fcaca5941e8e5e493"></a>

### `BT_HCI_LE_PER_ADV_OP_INTERM_FRAG`

```c
#define BT_HCI_LE_PER_ADV_OP_INTERM_FRAG 0x00
```

<a id="a7f2314472ccb051e87d1bb2f9b3fded8"></a>

### `BT_HCI_LE_PER_ADV_OP_LAST_FRAG`

```c
#define BT_HCI_LE_PER_ADV_OP_LAST_FRAG 0x02
```

<a id="a9af7ce6ecbd978df6193c4e9c2d8b002"></a>

### `BT_HCI_LE_PERIPHERAL_LATENCY_MAX`

```c
#define BT_HCI_LE_PERIPHERAL_LATENCY_MAX 0x01f3
```

<a id="a95274b56d9d973f32d2098b433ed1ff7"></a>

### `BT_HCI_LE_PERIPHERAL_LATENCY_MIN`

```c
#define BT_HCI_LE_PERIPHERAL_LATENCY_MIN (0x0000U)
```

<a id="a833ae32a3a5ffefbe57c7aa9cdf2e5a9"></a>

### `BT_HCI_LE_PHY_1M`

```c
#define BT_HCI_LE_PHY_1M 0x01
```

<a id="a727a1780d5f3754a78dea0476c2b97bb"></a>

### `BT_HCI_LE_PHY_2M`

```c
#define BT_HCI_LE_PHY_2M 0x02
```

<a id="ac5173dfe471fe4d1aad0f7d79904e46a"></a>

### `BT_HCI_LE_PHY_CODED`

```c
#define BT_HCI_LE_PHY_CODED 0x03
```

<a id="a61909ce217268c8cc6274f16d3db8484"></a>

### `BT_HCI_LE_PHY_CODED_ANY`

```c
#define BT_HCI_LE_PHY_CODED_ANY 0x00
```

<a id="a54bf26868903f0178b0f9f70111ea6b7"></a>

### `BT_HCI_LE_PHY_CODED_S2`

```c
#define BT_HCI_LE_PHY_CODED_S2 0x01
```

<a id="abe28c39a93e86d9ad5e6f0c08b09ef9c"></a>

### `BT_HCI_LE_PHY_CODED_S8`

```c
#define BT_HCI_LE_PHY_CODED_S8 0x02
```

<a id="a8101f257838639b46dcd0d50a92bba0c"></a>

### `BT_HCI_LE_PHY_PREFER_1M`

```c
#define BT_HCI_LE_PHY_PREFER_1M BIT(0)
```

<a id="ae89ffa7723482ced707f8a57febce629"></a>

### `BT_HCI_LE_PHY_PREFER_2M`

```c
#define BT_HCI_LE_PHY_PREFER_2M BIT(1)
```

<a id="ab33fde130c9fdb99559b15455e827a7a"></a>

### `BT_HCI_LE_PHY_PREFER_CODED`

```c
#define BT_HCI_LE_PHY_PREFER_CODED BIT(2)
```

<a id="a0fb6efaf47f2d676eb51b3fb99d0a691"></a>

### `BT_HCI_LE_PHY_RX_ANY`

```c
#define BT_HCI_LE_PHY_RX_ANY BIT(1)
```

<a id="a7656d3400ccb540e8bd066cf1232c38e"></a>

### `BT_HCI_LE_PHY_TX_ANY`

```c
#define BT_HCI_LE_PHY_TX_ANY BIT(0)
```

<a id="a5b394658223fd700fa152c4deb2f956e"></a>

### `BT_HCI_LE_PRIM_ADV_INTERVAL_MAX`

```c
#define BT_HCI_LE_PRIM_ADV_INTERVAL_MAX 0xFFFFFF
```

<a id="a1599475c6673d4fa0e00d16024df9a3b"></a>

### `BT_HCI_LE_PRIM_ADV_INTERVAL_MIN`

```c
#define BT_HCI_LE_PRIM_ADV_INTERVAL_MIN 0x000020
```

<a id="ae61d38e84e0d58be45ffaf521abad2f6"></a>

### `BT_HCI_LE_PRIVACY_MODE_DEVICE`

```c
#define BT_HCI_LE_PRIVACY_MODE_DEVICE 0x01
```

<a id="a423b143e474548458b8bcce59029f722"></a>

### `BT_HCI_LE_PRIVACY_MODE_NETWORK`

```c
#define BT_HCI_LE_PRIVACY_MODE_NETWORK 0x00
```

<a id="a56f7acd075e03694d966d949f637946c"></a>

### `BT_HCI_LE_RSSI_NOT_AVAILABLE`

```c
#define BT_HCI_LE_RSSI_NOT_AVAILABLE 0x7F
```

<a id="a27c179b4c8e85f840b41c4765613c99b"></a>

### `BT_HCI_LE_RX_PHY_1M`

```c
#define BT_HCI_LE_RX_PHY_1M 0x01
```

<a id="ac1db92b615a94b30e587a87d3637ad47"></a>

### `BT_HCI_LE_RX_PHY_2M`

```c
#define BT_HCI_LE_RX_PHY_2M 0x02
```

<a id="a689bc0f95a315c18ee4efbc556d31d60"></a>

### `BT_HCI_LE_RX_PHY_CODED`

```c
#define BT_HCI_LE_RX_PHY_CODED 0x03
```

<a id="a85450acad700f8cef375d34235752650"></a>

### `BT_HCI_LE_SAMPLE_CTE_ALL`

```c
#define BT_HCI_LE_SAMPLE_CTE_ALL 0x0
```

<a id="a0c8888c4dfed6ab4c0f07a37ca3b2278"></a>

### `BT_HCI_LE_SAMPLE_CTE_COUNT_MAX`

```c
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MAX 0x10
```

<a id="afd22fac7ff6d5006015159ffc978798a"></a>

### `BT_HCI_LE_SAMPLE_CTE_COUNT_MIN`

```c
#define BT_HCI_LE_SAMPLE_CTE_COUNT_MIN 0x1
```

<a id="ac13c2e39ac1e13cf5cd2cfa248a6f316"></a>

### `BT_HCI_LE_SCAN_ACTIVE`

```c
#define BT_HCI_LE_SCAN_ACTIVE 0x01
```

<a id="a152712b517c9ee0452555408d14bbfa7"></a>

### `BT_HCI_LE_SCAN_DISABLE`

```c
#define BT_HCI_LE_SCAN_DISABLE 0x00
```

<a id="a6859aeda42fe72b75d5cc1896b7e6afd"></a>

### `BT_HCI_LE_SCAN_ENABLE`

```c
#define BT_HCI_LE_SCAN_ENABLE 0x01
```

<a id="a6fb35a340e8eecd7bc2602ed010aa6c1"></a>

### `BT_HCI_LE_SCAN_FILTER_DUP_DISABLE`

```c
#define BT_HCI_LE_SCAN_FILTER_DUP_DISABLE 0x00
```

<a id="a4c9503d4a13f78a1dc44e087af922793"></a>

### `BT_HCI_LE_SCAN_FILTER_DUP_ENABLE`

```c
#define BT_HCI_LE_SCAN_FILTER_DUP_ENABLE 0x01
```

<a id="ac6f3763ab47d20efee1af16d8d019bf3"></a>

### `BT_HCI_LE_SCAN_FP_BASIC_FILTER`

```c
#define BT_HCI_LE_SCAN_FP_BASIC_FILTER 0x01
```

<a id="a278ccd7cfefd1a46f6de843b722f583a"></a>

### `BT_HCI_LE_SCAN_FP_BASIC_NO_FILTER`

```c
#define BT_HCI_LE_SCAN_FP_BASIC_NO_FILTER 0x00
```

<a id="a45846e02e2630608b14f62f9b9020f9d"></a>

### `BT_HCI_LE_SCAN_FP_EXT_FILTER`

```c
#define BT_HCI_LE_SCAN_FP_EXT_FILTER 0x03
```

<a id="aed7fa63104bbc551bc0dbfa21e38744a"></a>

### `BT_HCI_LE_SCAN_FP_EXT_NO_FILTER`

```c
#define BT_HCI_LE_SCAN_FP_EXT_NO_FILTER 0x02
```

<a id="a2274aacde21083e9633fe59fbff0df87"></a>

### `BT_HCI_LE_SCAN_PASSIVE`

```c
#define BT_HCI_LE_SCAN_PASSIVE 0x00
```

<a id="ab0319b6bf5387c5a4d2d38d789fab6aa"></a>

### `BT_HCI_LE_SCI_CE_LEN_MAX_125US`

```c
#define BT_HCI_LE_SCI_CE_LEN_MAX_125US (0x3E7FU)
```

<a id="acef97af0baeb7f491d66ec1d0b4fff36"></a>

### `BT_HCI_LE_SCI_CE_LEN_MIN_125US`

```c
#define BT_HCI_LE_SCI_CE_LEN_MIN_125US (0x0001U)
```

<a id="a14c9d4eab8b8fe650ea2950d0c3a703f"></a>

### `BT_HCI_LE_SCI_INTERVAL_MAX_125US`

```c
#define BT_HCI_LE_SCI_INTERVAL_MAX_125US (0x7D00U)
```

<a id="ad6ccdf8c0658b065218f10581990fef8"></a>

### `BT_HCI_LE_SCI_INTERVAL_MAX_US`

```c
#define BT_HCI_LE_SCI_INTERVAL_MAX_US (4000000U)
```

<a id="a292c11301eed063f4b9cfec645881a47"></a>

### `BT_HCI_LE_SCI_INTERVAL_MIN_125US`

```c
#define BT_HCI_LE_SCI_INTERVAL_MIN_125US (0x0003U)
```

所有限制均依据《蓝牙核心规范》（BT Core Spec）6.2，第 4 卷 E 部分 7.8.154。

<a id="a9d55d12b5d3c37c99730950878075684"></a>

### `BT_HCI_LE_SCI_INTERVAL_MIN_US`

```c
#define BT_HCI_LE_SCI_INTERVAL_MIN_US (375U)
```

<a id="a47b99bb33143c6a936af1462ce791313"></a>

### `BT_HCI_LE_SCI_INTERVAL_UNIT_US`

```c
#define BT_HCI_LE_SCI_INTERVAL_UNIT_US (125U)
```

<a id="aea8e6814082534c65773ceb291d60c49"></a>

### `BT_HCI_LE_SCI_STRIDE_MIN_125US`

```c
#define BT_HCI_LE_SCI_STRIDE_MIN_125US (0x0001U)
```

<a id="aaf9b76b276b5cf7e02bb5e3b0a12ecf6"></a>

### `BT_HCI_LE_SET_PER_ADV_ENABLE_ADI`

```c
#define BT_HCI_LE_SET_PER_ADV_ENABLE_ADI BIT(1)
```

<a id="a1c03932d8c1e2c5436eaf45be093b4d4"></a>

### `BT_HCI_LE_SET_PER_ADV_ENABLE_ENABLE`

```c
#define BT_HCI_LE_SET_PER_ADV_ENABLE_ENABLE BIT(0)
```

<a id="a1aaaffb3044bfd824aa6744867da0a97"></a>

### `BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_ENABLE`

```c
#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_ENABLE BIT(0)
```

<a id="a08fe0a16e8c1b3eb6b23869b37739f2d"></a>

### `BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_FILTER_DUPLICATE`

```c
#define BT_HCI_LE_SET_PER_ADV_RECV_ENABLE_FILTER_DUPLICATE BIT(1)
```

<a id="a33ce951c9eddfcc5556b0168c14b9769"></a>

### `BT_HCI_LE_SUBRATE_FACTOR_MAX`

```c
#define BT_HCI_LE_SUBRATE_FACTOR_MAX 0x01f4
```

<a id="a135059b92eba0676689abc78a2f560d3"></a>

### `BT_HCI_LE_SUBRATE_FACTOR_MIN`

```c
#define BT_HCI_LE_SUBRATE_FACTOR_MIN 0x0001
```

所有限制均依据《蓝牙核心规范》（BT Core Spec）v5.4，第 4 卷 E 部分。

<a id="a1357a2a7227e86df1c132207ba44d6db"></a>

### `BT_HCI_LE_SUPERVISION_TIMEOUT_MAX`

```c
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MAX 0x0c80
```

最大低功耗蓝牙监督超时（LE Supervision Timeout）：3200 ms。

<a id="a07b822f1a826f4824ec070c4b6822fe2"></a>

### `BT_HCI_LE_SUPERVISION_TIMEOUT_MIN`

```c
#define BT_HCI_LE_SUPERVISION_TIMEOUT_MIN 0x000a
```

最小低功耗蓝牙监督超时（LE Supervision Timeout）：10 ms。

<a id="a2564ee96b802cb887f67e3cc38f8f400"></a>

### `BT_HCI_LE_SUPERVISON_TIMEOUT_MAX`

```c
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MAX BT_HCI_LE_SUPERVISION_TIMEOUT_MAX __DEPRECATED_MACRO
```

<a id="a03dc93eec388a17c286d50395c683fcb"></a>

### `BT_HCI_LE_SUPERVISON_TIMEOUT_MIN`

```c
#define BT_HCI_LE_SUPERVISON_TIMEOUT_MIN BT_HCI_LE_SUPERVISION_TIMEOUT_MIN __DEPRECATED_MACRO
```

<a id="ad6bdc84c282a4e35ded32687cba94e9f"></a>

### `BT_HCI_LE_SWITCH_PATTERN_LEN_MAX`

```c
#define BT_HCI_LE_SWITCH_PATTERN_LEN_MAX 0x4B
```

<a id="ad74e54836996fc3d02fbb245f9c72b5a"></a>

### `BT_HCI_LE_SWITCH_PATTERN_LEN_MIN`

```c
#define BT_HCI_LE_SWITCH_PATTERN_LEN_MIN 0x2
```

<a id="a6764be57300c8dac30a058ebf8387159"></a>

### `BT_HCI_LE_TEST_CTE_DISABLED`

```c
#define BT_HCI_LE_TEST_CTE_DISABLED 0x00
```

<a id="a1f45696f06d7bc3f4cc8393bd6967286"></a>

### `BT_HCI_LE_TEST_CTE_TYPE_ANY`

```c
#define BT_HCI_LE_TEST_CTE_TYPE_ANY 0x00
```

<a id="ac4ac180578ed3f662d91c43b5c6b6b53"></a>

### `BT_HCI_LE_TEST_SLOT_DURATION_ANY`

```c
#define BT_HCI_LE_TEST_SLOT_DURATION_ANY 0x00
```

<a id="aef669f8887a165b4948eb651c91968c1"></a>

### `BT_HCI_LE_TEST_SWITCH_PATTERN_LEN_ANY`

```c
#define BT_HCI_LE_TEST_SWITCH_PATTERN_LEN_ANY 0x00
```

<a id="ace025b0516289eb493f54ba92292dd22"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_BIG_MAX`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MAX 0x7FFFFFU
```

<a id="ae24bd2c6c05c7d300d110a522c59fcbc"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_BIG_MIN`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_BIG_MIN 0x000030U
```

<a id="ad6729367096ec3d288b187b5746f17d7"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MAX`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MAX 0x7FFFFFU
```

7.7.65.25 LE CIS Established 事件所定义的中央设备到外设（Central to Peripheral）的最大传输延迟（Transport Latency）。

<a id="a85732b5233b34298a3f979f8e9009907"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MIN`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_C_TO_P_MIN 0x0000F2U
```

7.7.65.25 LE CIS Established 事件所定义的中央设备到外设（Central to Peripheral）的最小传输延迟（Transport Latency）。

<a id="a0bce30a784239e713fb38125cd16e2c1"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MAX`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MAX 0x7FFFFFU
```

7.7.65.25 LE CIS Established 事件所定义的外设到中央设备（Peripheral to Central）的最大传输延迟（Transport Latency）。

<a id="a9f10f08358a5caa80b71b7351dbf09bc"></a>

### `BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MIN`

```c
#define BT_HCI_LE_TRANSPORT_LATENCY_P_TO_C_MIN 0x0000F2U
```

7.7.65.25 LE CIS Established 事件所定义的外设到中央设备（Peripheral to Central）的最小传输延迟（Transport Latency）。

<a id="a0cb0c8d33e23ff6e59241c88b9e5adee"></a>

### `BT_HCI_LE_TX_PHY_1M`

```c
#define BT_HCI_LE_TX_PHY_1M 0x01
```

<a id="a7de4598ca06439f89772f0e72306ac3c"></a>

### `BT_HCI_LE_TX_PHY_2M`

```c
#define BT_HCI_LE_TX_PHY_2M 0x02
```

<a id="a599195b97f069412e112df470bf2b536"></a>

### `BT_HCI_LE_TX_PHY_CODED_S2`

```c
#define BT_HCI_LE_TX_PHY_CODED_S2 0x04
```

<a id="a01d96d9e7bb61db9b3cd31d161b0abf4"></a>

### `BT_HCI_LE_TX_PHY_CODED_S8`

```c
#define BT_HCI_LE_TX_PHY_CODED_S8 0x03
```

<a id="a740a01412d6fad277362634e1854f54b"></a>

### `BT_HCI_LE_TX_POWER_PHY_1M`

```c
#define BT_HCI_LE_TX_POWER_PHY_1M 0x01
```

<a id="aa3eadebe7675de492b01ec117f72d808"></a>

### `BT_HCI_LE_TX_POWER_PHY_2M`

```c
#define BT_HCI_LE_TX_POWER_PHY_2M 0x02
```

<a id="ab2bed6683929c37a3d087dba88309e45"></a>

### `BT_HCI_LE_TX_POWER_PHY_CODED_S2`

```c
#define BT_HCI_LE_TX_POWER_PHY_CODED_S2 0x04
```

<a id="a66f2c7c03e65392c3477faddc14d9787"></a>

### `BT_HCI_LE_TX_POWER_PHY_CODED_S8`

```c
#define BT_HCI_LE_TX_POWER_PHY_CODED_S8 0x03
```

<a id="a46bac5521c33da56df1d06ed7c472a06"></a>

### `BT_HCI_LE_TX_POWER_REPORT_DISABLE`

```c
#define BT_HCI_LE_TX_POWER_REPORT_DISABLE 0x00
```

<a id="a31f7372543b6dec580fe464ec011d752"></a>

### `BT_HCI_LE_TX_POWER_REPORT_ENABLE`

```c
#define BT_HCI_LE_TX_POWER_REPORT_ENABLE 0x01
```

<a id="a443a5a524ec41bf2ea86eab74dd022dc"></a>

### `BT_HCI_LE_TX_POWER_REPORT_REASON_LOCAL_CHANGED`

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_LOCAL_CHANGED 0x00
```

发射功率报告（Transmit Power Reporting）的原因。

<a id="a268761b9eae9c84f74394a6098f15ee8"></a>

### `BT_HCI_LE_TX_POWER_REPORT_REASON_READ_REMOTE_COMPLETED`

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_READ_REMOTE_COMPLETED 0x02
```

<a id="a1fbc1b017b13987a017af7cd90bdf708"></a>

### `BT_HCI_LE_TX_POWER_REPORT_REASON_REMOTE_CHANGED`

```c
#define BT_HCI_LE_TX_POWER_REPORT_REASON_REMOTE_CHANGED 0x01
```

<a id="af7cc15be8165315ee0358ebb517b5e33"></a>

### `BT_HCI_LE_ZONE_ENTERED_HIGH`

```c
#define BT_HCI_LE_ZONE_ENTERED_HIGH 0x2
```

<a id="aff1538e314a97aa4910d4f7066dc4d55"></a>

### `BT_HCI_LE_ZONE_ENTERED_LOW`

```c
#define BT_HCI_LE_ZONE_ENTERED_LOW 0x0
```

<a id="ab88f3d713f6862c08b73752436ca8b1b"></a>

### `BT_HCI_LE_ZONE_ENTERED_MIDDLE`

```c
#define BT_HCI_LE_ZONE_ENTERED_MIDDLE 0x1
```

<a id="ac4681f15de605e921431b8cc673619ac"></a>

### `BT_HCI_LINK_POLICY_SETTINGS_ENABLE_HOLD_MODE`

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_HOLD_MODE BIT(1)
```

<a id="a7fd831ad60e792a93724b6588e99574b"></a>

### `BT_HCI_LINK_POLICY_SETTINGS_ENABLE_ROLE_SWITCH`

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_ROLE_SWITCH BIT(0)
```

<a id="afdbc756af5184efa28affc7f3c3aed97"></a>

### `BT_HCI_LINK_POLICY_SETTINGS_ENABLE_SNIFF_SWITCH`

```c
#define BT_HCI_LINK_POLICY_SETTINGS_ENABLE_SNIFF_SWITCH BIT(2)
```

<a id="a73dfca6788b272380e6920d2907bf43f"></a>

### `BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_ACL`

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_ACL 0x00
```

<a id="ad10d8c5ffd49cb183731a9ba97c0e058"></a>

### `BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_SCO`

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_BREDR_SCO 0x01
```

<a id="a560cb22e5f39c144e3d477eea5c32beb"></a>

### `BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_BIS`

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_BIS 0x03
```

<a id="a5e53f28cedf59f18ce8d494f16933b3c"></a>

### `BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_CIS`

```c
#define BT_HCI_LOGICAL_TRANSPORT_TYPE_LE_CIS 0x02
```

<a id="ac886a10eed1313f6114fcfc3810a34f0"></a>

### `BT_HCI_NO_BONDING`

```c
#define BT_HCI_NO_BONDING 0x00
```

<a id="a89c6d0d285c1c99c51c96d282fe593b9"></a>

### `BT_HCI_NO_BONDING_MITM`

```c
#define BT_HCI_NO_BONDING_MITM 0x01
```

<a id="af45bed44788b16be1b172c56c33eea34"></a>

### `BT_HCI_OP_ACCEPT_CONN_REQ`

```c
#define BT_HCI_OP_ACCEPT_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x0009) /* 0x0409 */
```

<a id="a97976c13fe03d346313bc19489d45360"></a>

### `BT_HCI_OP_ACCEPT_SYNC_CONN_REQ`

```c
#define BT_HCI_OP_ACCEPT_SYNC_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x0029) /* 0x0429 */
```

<a id="a4c24e505f9c799275fc2f35619b7df97"></a>

### `BT_HCI_OP_AUTH_REQUESTED`

```c
#define BT_HCI_OP_AUTH_REQUESTED BT_OP(BT_OGF_LINK_CTRL, 0x0011) /* 0x0411 */
```

<a id="a8291666923a96840b1c15898d6013d66"></a>

### `BT_HCI_OP_CHANGE_CONN_PACKET_TYPE`

```c
#define BT_HCI_OP_CHANGE_CONN_PACKET_TYPE BT_OP(BT_OGF_LINK_CTRL, 0x000f) /* 0x040f */
```

HCI 更改连接分组类型（Change Connection Packet Type）操作码（Opcode）。

<a id="a2f95e881ffcda381d8d8ad7ba8705e7d"></a>

### `BT_HCI_OP_CLEAR_ADV_SETS`

```c
#define BT_HCI_OP_CLEAR_ADV_SETS BT_OP(BT_OGF_LE, 0x003d) /* 0x203d */
```

<a id="abc80a803d0e540541bcd889772e59940"></a>

### `BT_HCI_OP_CONFIGURE_DATA_PATH`

```c
#define BT_HCI_OP_CONFIGURE_DATA_PATH BT_OP(BT_OGF_BASEBAND, 0x0083) /* 0x0c83 */
```

<a id="addfd3dec2a69e7e5e2634c4fe63769f2"></a>

### `BT_HCI_OP_CONNECT`

```c
#define BT_HCI_OP_CONNECT BT_OP(BT_OGF_LINK_CTRL, 0x0005) /* 0x0405 */
```

<a id="ac50eb14115129bcc8c47016a6479149d"></a>

### `BT_HCI_OP_CONNECT_CANCEL`

```c
#define BT_HCI_OP_CONNECT_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x0008) /* 0x0408 */
```

<a id="ab3d8612855550e52a0887e231371fbc2"></a>

### `BT_HCI_OP_DISCONNECT`

```c
#define BT_HCI_OP_DISCONNECT BT_OP(BT_OGF_LINK_CTRL, 0x0006) /* 0x0406 */
```

<a id="a93951610963235f4ebd86e82c86a52a3"></a>

### `BT_HCI_OP_EXIT_SNIFF_MODE`

```c
#define BT_HCI_OP_EXIT_SNIFF_MODE BT_OP(BT_OGF_LINK_POLICY, 0x0004) /* 0x0804 */
```

<a id="a2e05f146890ad81be27dca91250bf69d"></a>

### `BT_HCI_OP_HOST_BUFFER_SIZE`

```c
#define BT_HCI_OP_HOST_BUFFER_SIZE BT_OP(BT_OGF_BASEBAND, 0x0033) /* 0x0c33 */
```

<a id="a6c7afa8e3b324714bc5f8dce9702604d"></a>

### `BT_HCI_OP_HOST_NUM_COMPLETED_PACKETS`

```c
#define BT_HCI_OP_HOST_NUM_COMPLETED_PACKETS BT_OP(BT_OGF_BASEBAND, 0x0035) /* 0x0c35 */
```

<a id="adce48ff5cdde5f4f8ab5bc960717581a"></a>

### `BT_HCI_OP_INQUIRY`

```c
#define BT_HCI_OP_INQUIRY BT_OP(BT_OGF_LINK_CTRL, 0x0001) /* 0x0401 */
```

<a id="ae2d4e5e9cbf056bff03a668e74523442"></a>

### `BT_HCI_OP_INQUIRY_CANCEL`

```c
#define BT_HCI_OP_INQUIRY_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x0002) /* 0x0402 */
```

<a id="a75d9a0acb6522dd0ae290572c4255540"></a>

### `BT_HCI_OP_IO_CAPABILITY_NEG_REPLY`

```c
#define BT_HCI_OP_IO_CAPABILITY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x0034) /* 0x0434 */
```

<a id="a343a3c5c594dd25483fedf38c304a09a"></a>

### `BT_HCI_OP_IO_CAPABILITY_REPLY`

```c
#define BT_HCI_OP_IO_CAPABILITY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002b) /* 0x042b */
```

<a id="ade7635c85588941a2e628639be06ce7b"></a>

### `BT_HCI_OP_LE_ACCEPT_CIS`

```c
#define BT_HCI_OP_LE_ACCEPT_CIS BT_OP(BT_OGF_LE, 0x0066) /* 0x2066 */
```

<a id="a103c6fada57c61fc3f994f8902f4123c"></a>

### `BT_HCI_OP_LE_ADD_DEV_TO_FAL`

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_FAL BT_OP(BT_OGF_LE, 0x0011) /* 0x2011 */
```

<a id="a393378ba85552bb5f41475a863ca649f"></a>

### `BT_HCI_OP_LE_ADD_DEV_TO_PER_ADV_LIST`

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0047) /* 0x2047 */
```

<a id="a735c643e8afa27c4e7f7be9bfb09676a"></a>

### `BT_HCI_OP_LE_ADD_DEV_TO_RL`

```c
#define BT_HCI_OP_LE_ADD_DEV_TO_RL BT_OP(BT_OGF_LE, 0x0027) /* 0x2027 */
```

<a id="a47af328ede7f14e3d78c81de609af1c9"></a>

### `BT_HCI_OP_LE_BIG_CREATE_SYNC`

```c
#define BT_HCI_OP_LE_BIG_CREATE_SYNC BT_OP(BT_OGF_LE, 0x006b) /* 0x206b */
```

<a id="aa7576f4ab30ec7985b4afd08a08800d2"></a>

### `BT_HCI_OP_LE_BIG_TERMINATE_SYNC`

```c
#define BT_HCI_OP_LE_BIG_TERMINATE_SYNC BT_OP(BT_OGF_LE, 0x006c) /* 0x206c */
```

<a id="a592ce45c74bdabf1b25954b8021a50bb"></a>

### `BT_HCI_OP_LE_CLEAR_FAL`

```c
#define BT_HCI_OP_LE_CLEAR_FAL BT_OP(BT_OGF_LE, 0x0010) /* 0x2010 */
```

<a id="affcd4a54d0b26d7b07e39157f17167b4"></a>

### `BT_HCI_OP_LE_CLEAR_PER_ADV_LIST`

```c
#define BT_HCI_OP_LE_CLEAR_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0049) /* 0x2049 */
```

<a id="a5efab85a3beac1fe3fc5a5294a2b1079"></a>

### `BT_HCI_OP_LE_CLEAR_RL`

```c
#define BT_HCI_OP_LE_CLEAR_RL BT_OP(BT_OGF_LE, 0x0029) /* 0x2029 */
```

<a id="ae488ce598705cf60b78da985015bb42b"></a>

### `BT_HCI_OP_LE_CONN_CTE_REQ_ENABLE`

```c
#define BT_HCI_OP_LE_CONN_CTE_REQ_ENABLE BT_OP(BT_OGF_LE, 0x0056) /* 0x2056 */
```

<a id="a150b54d69fb6fe9175336fadb7d81bb8"></a>

### `BT_HCI_OP_LE_CONN_CTE_RSP_ENABLE`

```c
#define BT_HCI_OP_LE_CONN_CTE_RSP_ENABLE BT_OP(BT_OGF_LE, 0x0057) /* 0x2057 */
```

<a id="a1fbca6b816791f1967278224f37782c1"></a>

### `BT_HCI_OP_LE_CONN_PARAM_REQ_NEG_REPLY`

```c
#define BT_HCI_OP_LE_CONN_PARAM_REQ_NEG_REPLY BT_OP(BT_OGF_LE, 0x0021) /* 0x2021 */
```

<a id="a8b824639d31fa9f579e73cf1f1344c85"></a>

### `BT_HCI_OP_LE_CONN_PARAM_REQ_REPLY`

```c
#define BT_HCI_OP_LE_CONN_PARAM_REQ_REPLY BT_OP(BT_OGF_LE, 0x0020) /* 0x2020 */
```

<a id="ac0c308b64ed89c9b7326982ef04ba6d3"></a>

### `BT_HCI_OP_LE_CONN_UPDATE`

```c
#define BT_HCI_OP_LE_CONN_UPDATE BT_OP(BT_OGF_LE, 0x0013) /* 0x2013 */
```

<a id="a41d7e2f884f868bcb5805781730e5ab4"></a>

### `BT_HCI_OP_LE_CONNECTION_RATE_REQUEST`

```c
#define BT_HCI_OP_LE_CONNECTION_RATE_REQUEST BT_OP(BT_OGF_LE, 0x00A1) /* 0x20A1 */
```

<a id="a2a57bb6089e3a064e62119188b555ba9"></a>

### `BT_HCI_OP_LE_CREATE_BIG`

```c
#define BT_HCI_OP_LE_CREATE_BIG BT_OP(BT_OGF_LE, 0x0068) /* 0x2068 */
```

<a id="ad0f1ae4be3f5bb90ef967d88dcaaf353"></a>

### `BT_HCI_OP_LE_CREATE_BIG_TEST`

```c
#define BT_HCI_OP_LE_CREATE_BIG_TEST BT_OP(BT_OGF_LE, 0x0069) /* 0x2069 */
```

<a id="a63c9af35a55d9b1ed1b253d057657608"></a>

### `BT_HCI_OP_LE_CREATE_CIS`

```c
#define BT_HCI_OP_LE_CREATE_CIS BT_OP(BT_OGF_LE, 0x0064) /* 0x2064 */
```

<a id="aadde6f016c942c7907afddf7b6c94304"></a>

### `BT_HCI_OP_LE_CREATE_CONN`

```c
#define BT_HCI_OP_LE_CREATE_CONN BT_OP(BT_OGF_LE, 0x000d) /* 0x200d */
```

<a id="acacd0832cddc00702da74b4a36e5c825"></a>

### `BT_HCI_OP_LE_CREATE_CONN_CANCEL`

```c
#define BT_HCI_OP_LE_CREATE_CONN_CANCEL BT_OP(BT_OGF_LE, 0x000e) /* 0x200e */
```

<a id="a92e1ec21014999f40172fa1812c36575"></a>

### `BT_HCI_OP_LE_CS_ACI_0`

```c
#define BT_HCI_OP_LE_CS_ACI_0 0x0
```

<a id="a5b082fa5b8ba11a651468cc516d067fe"></a>

### `BT_HCI_OP_LE_CS_ACI_1`

```c
#define BT_HCI_OP_LE_CS_ACI_1 0x1
```

<a id="ab30a4e55002080394c39fb885eba36e4"></a>

### `BT_HCI_OP_LE_CS_ACI_2`

```c
#define BT_HCI_OP_LE_CS_ACI_2 0x2
```

<a id="a76d1452003c0bd3b688765aa2d25047f"></a>

### `BT_HCI_OP_LE_CS_ACI_3`

```c
#define BT_HCI_OP_LE_CS_ACI_3 0x3
```

<a id="af16c4c79e602e6da833b8aa3e0c4bf64"></a>

### `BT_HCI_OP_LE_CS_ACI_4`

```c
#define BT_HCI_OP_LE_CS_ACI_4 0x4
```

<a id="ad980d8f134d940b80dc9b0e3a570ac06"></a>

### `BT_HCI_OP_LE_CS_ACI_5`

```c
#define BT_HCI_OP_LE_CS_ACI_5 0x5
```

<a id="a4c7ff3c949023f4544bf50353a0f082b"></a>

### `BT_HCI_OP_LE_CS_ACI_6`

```c
#define BT_HCI_OP_LE_CS_ACI_6 0x6
```

<a id="acabccf9f5893324dcb6acc0769ab8417"></a>

### `BT_HCI_OP_LE_CS_ACI_7`

```c
#define BT_HCI_OP_LE_CS_ACI_7 0x7
```

<a id="af0d407f944831f8c85f91fb60f5bc618"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_FOUR`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_FOUR 0x04
```

<a id="aed2444a40bc79ccf3f383dd961036f5e"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_NONE`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_NONE 0xFF
```

<a id="a7fa26323384443ba9c5e635047b74f51"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_ONE`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_ONE 0x01
```

<a id="afad5b26b2a6ce125b6198856d20bcdd8"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_REP`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_REP 0xFE
```

<a id="a8721a8f4670a8038d66d42adea061f57"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_THREE`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_THREE 0x03
```

<a id="aa6d146c85e3148a2afb66023d94c2eeb"></a>

### `BT_HCI_OP_LE_CS_ANTENNA_SEL_TWO`

```c
#define BT_HCI_OP_LE_CS_ANTENNA_SEL_TWO 0x02
```

<a id="af26aad0e137782c8f12937b1736d6ada"></a>

### `BT_HCI_OP_LE_CS_CREATE_CONFIG`

```c
#define BT_HCI_OP_LE_CS_CREATE_CONFIG BT_OP(BT_OGF_LE, 0x0090) /* 0x2090 */
```

<a id="a7baf90f5bf691ce6b650677e6c2a9600"></a>

### `BT_HCI_OP_LE_CS_CS_SYNC_1M`

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_1M 0x1
```

<a id="ae49d35db87532e06ea685a63eb89177a"></a>

### `BT_HCI_OP_LE_CS_CS_SYNC_2M`

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_2M 0x2
```

<a id="ac34716156b071e06eb454f091a63216c"></a>

### `BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT`

```c
#define BT_HCI_OP_LE_CS_CS_SYNC_2M_2BT 0x3
```

<a id="a4505bedc3b5aae63b80cf53fc516b342"></a>

### `BT_HCI_OP_LE_CS_INITIATOR_ROLE`

```c
#define BT_HCI_OP_LE_CS_INITIATOR_ROLE 0x0
```

<a id="a74aaa5b6b799dad3af6778e23093b230"></a>

### `BT_HCI_OP_LE_CS_INITIATOR_ROLE_MASK`

```c
#define BT_HCI_OP_LE_CS_INITIATOR_ROLE_MASK BIT(0)
```

<a id="af1b7924e50ba017e59d697fd8814d491"></a>

### `BT_HCI_OP_LE_CS_MAIN_MODE_1`

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_1 0x1
```

<a id="a714152a085bbc317b539d6e973ccffc6"></a>

### `BT_HCI_OP_LE_CS_MAIN_MODE_2`

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_2 0x2
```

<a id="a5d2af0ed5e0cc5cf7d9f0baae512ff68"></a>

### `BT_HCI_OP_LE_CS_MAIN_MODE_3`

```c
#define BT_HCI_OP_LE_CS_MAIN_MODE_3 0x3
```

<a id="a29a240b2d3f209b1f5f3d96e380dde08"></a>

### `BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER`

```c
#define BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER 20
```

<a id="a040315a8ac4f80a2c497919a2fd4d7bc"></a>

### `BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER`

```c
#define BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER -127
```

<a id="a4eddce6558339caba6a3d16f8fe5d485"></a>

### `BT_HCI_OP_LE_CS_PROCEDURE_ENABLE`

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_ENABLE BT_OP(BT_OGF_LE, 0x0094) /* 0x2094 */
```

<a id="a3a8f1c94f40696f18e18810f736497e3"></a>

### `BT_HCI_OP_LE_CS_PROCEDURE_PHY_1M`

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_1M 0x01
```

<a id="a016f68a621de8d332f3073df4faf1702"></a>

### `BT_HCI_OP_LE_CS_PROCEDURE_PHY_2M`

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_2M 0x02
```

<a id="a776a14d8e7fdca584475f26b441c8bfb"></a>

### `BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S2`

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S2 0x04
```

<a id="a2543f9fa20db642fb8b47b949c50af6a"></a>

### `BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S8`

```c
#define BT_HCI_OP_LE_CS_PROCEDURE_PHY_CODED_S8 0x03
```

<a id="a3e01bbe3a72c946015a288ee49d3cbdd"></a>

### `BT_HCI_OP_LE_CS_PROCEDURES_DISABLED`

```c
#define BT_HCI_OP_LE_CS_PROCEDURES_DISABLED 0x00
```

<a id="a4a88120ae7e83fd791012c913315d14f"></a>

### `BT_HCI_OP_LE_CS_PROCEDURES_ENABLED`

```c
#define BT_HCI_OP_LE_CS_PROCEDURES_ENABLED 0x01
```

<a id="a84e0338551dd8256a821d960bf745208"></a>

### `BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES`

```c
#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x0089) /* 0x2089 */
```

<a id="aac9dd21ae34a16f4cfb5a51abe14f024"></a>

### `BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2`

```c
#define BT_HCI_OP_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2 BT_OP(BT_OGF_LE, 0x00A5) /* 0x20A5 */
```

HCI 低功耗蓝牙读取本地支持能力（LE Read Local Supported Capabilities，v2）操作码。

<a id="afa7a0214b145891562f1d2b7b16860ab"></a>

### `BT_HCI_OP_LE_CS_READ_REMOTE_FAE_TABLE`

```c
#define BT_HCI_OP_LE_CS_READ_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008E) /* 0x208E */
```

<a id="a4f6dd157a555e06cd028a9097fd7b81a"></a>

### `BT_HCI_OP_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES`

```c
#define BT_HCI_OP_LE_CS_READ_REMOTE_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x008A) /* 0x208A */
```

<a id="aeb3715dfcac55a46532f51279e29708c"></a>

### `BT_HCI_OP_LE_CS_REFLECTOR_ROLE`

```c
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE 0x1
```

<a id="a1beb2f602b3635fee272580f0f2f8719"></a>

### `BT_HCI_OP_LE_CS_REFLECTOR_ROLE_MASK`

```c
#define BT_HCI_OP_LE_CS_REFLECTOR_ROLE_MASK BIT(1)
```

<a id="a54116ddaa8338d59b23fb879c185a399"></a>

### `BT_HCI_OP_LE_CS_REMOVE_CONFIG`

```c
#define BT_HCI_OP_LE_CS_REMOVE_CONFIG BT_OP(BT_OGF_LE, 0x0091) /* 0x2091 */
```

<a id="a1fe5e94fbd1156c8196c8e1ab9816bac"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_128BIT_RAND 0x6
```

<a id="abe4efee7cf9371129f4b5bd650b0d64a"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_RAND 0x3
```

<a id="aa2ae18252a20ef3481d2402f8924cdda"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_32BIT_SOUND 0x1
```

<a id="a77e56fd5302673f6ef295c0cceabdc9f"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_64BIT_RAND 0x4
```

<a id="aa60f64ff7259fd79fb1da2c063530348"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_RAND 0x5
```

<a id="a73cbfe2a942b684ac0b5b50d900fb83f"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_96BIT_SOUND 0x2
```

<a id="a759eb7a8e43ee7cf1ea88ddd3e69feb5"></a>

### `BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY`

```c
#define BT_HCI_OP_LE_CS_RTT_TYPE_AA_ONLY 0x0
```

<a id="a574168efdaa5729aec9699d48f988d77"></a>

### `BT_HCI_OP_LE_CS_SECURITY_ENABLE`

```c
#define BT_HCI_OP_LE_CS_SECURITY_ENABLE BT_OP(BT_OGF_LE, 0x008C) /* 0x208C */
```

<a id="a880439089735247c7011862d5b3e090f"></a>

### `BT_HCI_OP_LE_CS_SET_CHANNEL_CLASSIFICATION`

```c
#define BT_HCI_OP_LE_CS_SET_CHANNEL_CLASSIFICATION BT_OP(BT_OGF_LE, 0x0092) /* 0x2092 */
```

<a id="addb1ab37dc75ab5389d74c6c96629b02"></a>

### `BT_HCI_OP_LE_CS_SET_DEFAULT_SETTINGS`

```c
#define BT_HCI_OP_LE_CS_SET_DEFAULT_SETTINGS BT_OP(BT_OGF_LE, 0x008D) /* 0x208D */
```

<a id="ad74850cecd8d8dd8a7878d944abdb411"></a>

### `BT_HCI_OP_LE_CS_SET_PROCEDURE_PARAMETERS`

```c
#define BT_HCI_OP_LE_CS_SET_PROCEDURE_PARAMETERS BT_OP(BT_OGF_LE, 0x0093) /* 0x2093 */
```

<a id="a96b13fb3b363a5436e1b9633f54bb248"></a>

### `BT_HCI_OP_LE_CS_SNR_18`

```c
#define BT_HCI_OP_LE_CS_SNR_18 0x0
```

<a id="a4b93a8bceafd49d6ca65816924bb4230"></a>

### `BT_HCI_OP_LE_CS_SNR_21`

```c
#define BT_HCI_OP_LE_CS_SNR_21 0x1
```

<a id="a135a4dc2f191d2a931b4270e00774cb2"></a>

### `BT_HCI_OP_LE_CS_SNR_24`

```c
#define BT_HCI_OP_LE_CS_SNR_24 0x2
```

<a id="a52eb27d8f726a2ed6859149fcdf2355d"></a>

### `BT_HCI_OP_LE_CS_SNR_27`

```c
#define BT_HCI_OP_LE_CS_SNR_27 0x3
```

<a id="a181c2d98b93bd18e9edc11a6f9535331"></a>

### `BT_HCI_OP_LE_CS_SNR_30`

```c
#define BT_HCI_OP_LE_CS_SNR_30 0x4
```

<a id="a4aa2e02ce5110be3dc68a801bb583372"></a>

### `BT_HCI_OP_LE_CS_SNR_NOT_USED`

```c
#define BT_HCI_OP_LE_CS_SNR_NOT_USED 0xFF
```

<a id="a219243d501bbcb6d62668398cde79fca"></a>

### `BT_HCI_OP_LE_CS_SUB_MODE_1`

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_1 0x1
```

<a id="ada09c787fca0a1d54bb754635489b51e"></a>

### `BT_HCI_OP_LE_CS_SUB_MODE_2`

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_2 0x2
```

<a id="a4b48c199b6b75e9dd62ec36883b40aa4"></a>

### `BT_HCI_OP_LE_CS_SUB_MODE_3`

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_3 0x3
```

<a id="ab3fce1eb448b0ade581e4e12b2d56039"></a>

### `BT_HCI_OP_LE_CS_SUB_MODE_UNUSED`

```c
#define BT_HCI_OP_LE_CS_SUB_MODE_UNUSED 0xFF
```

<a id="af09601cffd1adf3f8b623868d8f8a3e9"></a>

### `BT_HCI_OP_LE_CS_TEST`

```c
#define BT_HCI_OP_LE_CS_TEST BT_OP(BT_OGF_LE, 0x0095) /* 0x2095 */
```

<a id="aa4ba4be270035da446389766b795c327"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_00`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_00 0x0
```

<a id="aa0e9e2081d3cbbb60de9b6dcffe77239"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_01`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_01 0x1
```

<a id="a762c5efa09e1fba989fdfb0bdcba9b9c"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_02`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_02 0x2
```

<a id="a2cc7a5d5d2105b1a428703e274cc5388"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_03`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_03 0x3
```

<a id="a03ffb0ffb8e98b26390575b153471bab"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_04`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_04 0x4
```

<a id="adbd3820e0ffa5f99e27778217d477010"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_05`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_05 0x5
```

<a id="a70607449d6bd6207783e319e77d63b16"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_06`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_06 0x6
```

<a id="acc79a879ea527c2901a8b91dae58d0ed"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_07`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_07 0x7
```

<a id="a9dfd88863d649182855edc8c268107d6"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_08`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_08 0x8
```

<a id="ae5a27304aa1cefdfb26ae2cbf42532e3"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_09`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_09 0x9
```

<a id="a0e9664c52808aa246218f92a4fb55516"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_10`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_10 0xA
```

<a id="a8fbc80d91e4a1ae04c76cda189cd5d83"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_11`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_11 0xB
```

<a id="a4c4a44bd33ebf97852e6640b0d510fdd"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_12`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_12 0xC
```

<a id="a08690b2f762d24c34966b839a6d5e696"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_13`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_13 0xD
```

<a id="ac2cd3ed1583f86af0480b8481cedca1e"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_14`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_14 0xE
```

<a id="ab2b0745d98053775e9bf073e36ce5d78"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_15`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_15 0xF
```

<a id="add2c42aa2583b93b0f98ac33ca61ca9d"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_16`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_16 0x10
```

<a id="a08db476ea6516691baeb9007b553281d"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_17`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_17 0x11
```

<a id="a9f0bf05cb0aac50e1df43397c3b913bc"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_18`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_18 0x12
```

<a id="a5df817bdfefc4de0a1309cf71908a105"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_19`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_19 0x13
```

<a id="ae64e5a409523b94ef1ce315ed49afed0"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_20`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_20 0x14
```

<a id="a46f70b5096593956795cc381e33c4aa2"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_21`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_21 0x15
```

<a id="abe9fa4621e9c004421170b0166ea14e1"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_22`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_22 0x16
```

<a id="afc41ca64d03a7ed8ea82a641a0217436"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_23`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_23 0x17
```

<a id="ac9d7cb5a339759b7e0c4ed150a487ca3"></a>

### `BT_HCI_OP_LE_CS_TEST_AP_INDEX_LOOP`

```c
#define BT_HCI_OP_LE_CS_TEST_AP_INDEX_LOOP 0xFF
```

<a id="acd33fc2eb3f5ebe10cbe4c5060f8336b"></a>

### `BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT`

```c
#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_HAT 0x0
```

<a id="ad09c735ab352d7a546cade296e915e85"></a>

### `BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X`

```c
#define BT_HCI_OP_LE_CS_TEST_CH3C_SHAPE_X 0x1
```

<a id="a77d27762b9faa7743a55d822a1839eac"></a>

### `BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B`

```c
#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3B 0x0
```

<a id="af17f867204bc7cf99e5d530c39302be0"></a>

### `BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C`

```c
#define BT_HCI_OP_LE_CS_TEST_CHSEL_TYPE_3C 0x1
```

<a id="a4c45c8b2b33ae857c654cc100b5e5550"></a>

### `BT_HCI_OP_LE_CS_TEST_END`

```c
#define BT_HCI_OP_LE_CS_TEST_END BT_OP(BT_OGF_LE, 0x0096) /* 0x2096 */
```

<a id="a50eb827977c0c596cb357ed62a6e80bd"></a>

### `BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER`

```c
#define BT_HCI_OP_LE_CS_TEST_MAXIMIZE_TX_POWER 0x7F
```

<a id="a500597c78a6ada65d1224960bf6a370f"></a>

### `BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER`

```c
#define BT_HCI_OP_LE_CS_TEST_MINIMIZE_TX_POWER 0x7E
```

<a id="a0a73e0d46b5ca0e94b4bb00d2f79e89d"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_0_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_0_MASK BIT(0)
```

<a id="a90c77fe0022f016453a8eb174b8fcd63"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_10_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_10_MASK BIT(10)
```

<a id="a2a62cbc191abd177cbf5aea27112fb8b"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_2_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_2_MASK BIT(2)
```

<a id="a560f6f1bddedc60b3a373778bc56b1a7"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_3_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_3_MASK BIT(3)
```

<a id="a36c2c6debe6bf395853112c68a726d25"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_4_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_4_MASK BIT(4)
```

<a id="a4aca98e213ba81c999c8495310af9320"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_5_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_5_MASK BIT(5)
```

<a id="afd7b8b4ec0baf526cc4335d26c380b62"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_6_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_6_MASK BIT(6)
```

<a id="a695d2ba272dbdd2681ab9216d00ca43a"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_7_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_7_MASK BIT(7)
```

<a id="ad92a29871be9aff39802fdea4446ef4b"></a>

### `BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_8_MASK`

```c
#define BT_HCI_OP_LE_CS_TEST_OVERRIDE_CONFIG_8_MASK BIT(8)
```

<a id="a04a26b8600cac8c82247a7d51122f600"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_00000000`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00000000 0x05
```

<a id="abf19d511680005828add231d64e1e3f0"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_00001111`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_00001111 0x06
```

<a id="a53f0ca5604489a38a1367736a5297b45"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_01010101`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_01010101 0x07
```

<a id="ae133ef2939518d660df5322551157d47"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_10101010`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_10101010 0x02
```

<a id="af20dfb1e245afc06a495179d700f126f"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_11110000`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11110000 0x01
```

<a id="aa94eda86c6ffe85a65267f285dae5cb1"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_11111111`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_11111111 0x04
```

<a id="a92bc70a5ad7938a46ac9f2127f1bc2d9"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS15`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS15 0x03
```

<a id="a4f922c5e0662adf8471686dfa9b719ec"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS9`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_PRBS9 0x00
```

<a id="a94007d8250c3524ad0b86745dbb74b3b"></a>

### `BT_HCI_OP_LE_CS_TEST_PAYLOAD_USER`

```c
#define BT_HCI_OP_LE_CS_TEST_PAYLOAD_USER 0x80
```

<a id="a1f2bfc1afab1928321c01beddb658f01"></a>

### `BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT`

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_2_POSITION_NOT_PRESENT 0xFF
```

<a id="a45e1ff56f1a6dcc59b784905e4fc6726"></a>

### `BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_0011`

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_0011 0x0
```

<a id="a5d3c206a5067ddc5a02a5d5e8c3eb7a3"></a>

### `BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_1100`

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_1100 0x1
```

<a id="a24d2e56f620500905572e786f2523b0e"></a>

### `BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_LOOP`

```c
#define BT_HCI_OP_LE_CS_TEST_SS_MARKER_VAL_LOOP 0x2
```

<a id="ad7a89a9365e20e4cd1e44bdb74ae7ecb"></a>

### `BT_HCI_OP_LE_CS_TEST_TONE_EXT_BOTH`

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_BOTH 0x3
```

<a id="a0513bf5ca6eb9f43a7e8cecaf943c4d7"></a>

### `BT_HCI_OP_LE_CS_TEST_TONE_EXT_INIT`

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_INIT 0x1
```

<a id="a9ed8967faa3ee3824433422709148330"></a>

### `BT_HCI_OP_LE_CS_TEST_TONE_EXT_NONE`

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_NONE 0x0
```

<a id="aa24ae1cf1501de66660051a4a62246df"></a>

### `BT_HCI_OP_LE_CS_TEST_TONE_EXT_REFL`

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REFL 0x2
```

<a id="a50fba6ab75b37ccf39452211ba05e896"></a>

### `BT_HCI_OP_LE_CS_TEST_TONE_EXT_REPEAT`

```c
#define BT_HCI_OP_LE_CS_TEST_TONE_EXT_REPEAT 0x4
```

<a id="a44eb5d70628f6522a08b1327588df979"></a>

### `BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_FAE_TABLE`

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_FAE_TABLE BT_OP(BT_OGF_LE, 0x008F) /* 0x208F */
```

<a id="acdbbe0da013fb3b6da5514498c3932dd"></a>

### `BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES`

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES BT_OP(BT_OGF_LE, 0x008B) /* 0x208B */
```

<a id="a523daa9b70fb57ae36a4bb9ff158cce8"></a>

### `BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES_V2`

```c
#define BT_HCI_OP_LE_CS_WRITE_CACHED_REMOTE_SUPPORTED_CAPABILITIES_V2 BT_OP(BT_OGF_LE, 0x00A6) /* 0x20A6 */
```

HCI 低功耗蓝牙信道探测写入缓存的远端支持能力（LE CS Write Cached Remote Supported Capabilities，v2）操作码。

<a id="a650fe2941ffe238b16fd99ed5e78b25a"></a>

### `BT_HCI_OP_LE_DEFAULT_PAST_PARAM`

```c
#define BT_HCI_OP_LE_DEFAULT_PAST_PARAM BT_OP(BT_OGF_LE, 0x005d) /* 0x205d */
```

<a id="a99fdd1dbff627a2f627e7d9eced68326"></a>

### `BT_HCI_OP_LE_ENCRYPT`

```c
#define BT_HCI_OP_LE_ENCRYPT BT_OP(BT_OGF_LE, 0x0017) /* 0x2017 */
```

<a id="aebd5487b500c54a47a926bb1daa56f5e"></a>

### `BT_HCI_OP_LE_ENH_READ_TX_POWER_LEVEL`

```c
#define BT_HCI_OP_LE_ENH_READ_TX_POWER_LEVEL BT_OP(BT_OGF_LE, 0x0076) /* 0x2076 */
```

<a id="a51c3637712a8701ae7fee16806f677df"></a>

### `BT_HCI_OP_LE_ENH_RX_TEST`

```c
#define BT_HCI_OP_LE_ENH_RX_TEST BT_OP(BT_OGF_LE, 0x0033) /* 0x2033 */
```

<a id="a903b1ce0bfe7df7de86bae5fb143e88f"></a>

### `BT_HCI_OP_LE_ENH_TX_TEST`

```c
#define BT_HCI_OP_LE_ENH_TX_TEST BT_OP(BT_OGF_LE, 0x0034) /* 0x2034 */
```

<a id="ac498c9cd93b664b5bd2e58982d36d7ad"></a>

### `BT_HCI_OP_LE_EXT_CREATE_CONN`

```c
#define BT_HCI_OP_LE_EXT_CREATE_CONN BT_OP(BT_OGF_LE, 0x0043) /* 0x2043 */
```

<a id="a1b6bc4da843ed8d04e0b9571465ffd12"></a>

### `BT_HCI_OP_LE_EXT_CREATE_CONN_V2`

```c
#define BT_HCI_OP_LE_EXT_CREATE_CONN_V2 BT_OP(BT_OGF_LE, 0x0085) /* 0x2085 */
```

<a id="acf8c51fe662c42853f4c023b25bcbd48"></a>

### `BT_HCI_OP_LE_FRAME_SPACE_UPDATE`

```c
#define BT_HCI_OP_LE_FRAME_SPACE_UPDATE BT_OP(BT_OGF_LE, 0x009D) /* 0x209D */
```

<a id="af2625fcbc0f29199f1a95dc9fe0f929d"></a>

### `BT_HCI_OP_LE_GENERATE_DHKEY`

```c
#define BT_HCI_OP_LE_GENERATE_DHKEY BT_OP(BT_OGF_LE, 0x0026) /* 0x2026 */
```

<a id="aa7bf82632c6df22096210de18902a465"></a>

### `BT_HCI_OP_LE_GENERATE_DHKEY_V2`

```c
#define BT_HCI_OP_LE_GENERATE_DHKEY_V2 BT_OP(BT_OGF_LE, 0x005e) /* 0x205e */
```

<a id="a2b988ffc8ffd10ce1dfde377afa699e1"></a>

### `BT_HCI_OP_LE_ISO_READ_TEST_COUNTERS`

```c
#define BT_HCI_OP_LE_ISO_READ_TEST_COUNTERS BT_OP(BT_OGF_LE, 0x0072) /* 0x2072 */
```

<a id="a467736569f030fbb433000e712f1b08e"></a>

### `BT_HCI_OP_LE_ISO_RECEIVE_TEST`

```c
#define BT_HCI_OP_LE_ISO_RECEIVE_TEST BT_OP(BT_OGF_LE, 0x0071) /* 0x2071 */
```

<a id="a86436e6b0cb17de95b438f192bbff1d2"></a>

### `BT_HCI_OP_LE_ISO_TEST_END`

```c
#define BT_HCI_OP_LE_ISO_TEST_END BT_OP(BT_OGF_LE, 0x0073) /* 0x2073 */
```

<a id="a740f1964df5bdb675906c87ad8ee0cef"></a>

### `BT_HCI_OP_LE_ISO_TRANSMIT_TEST`

```c
#define BT_HCI_OP_LE_ISO_TRANSMIT_TEST BT_OP(BT_OGF_LE, 0x0070) /* 0x2070 */
```

<a id="ae04bd3c7ff17142f2b47e24accdf6a20"></a>

### `BT_HCI_OP_LE_LTK_REQ_NEG_REPLY`

```c
#define BT_HCI_OP_LE_LTK_REQ_NEG_REPLY BT_OP(BT_OGF_LE, 0x001b) /* 0x201b */
```

<a id="a92050425248585bd1c3873e8593db362"></a>

### `BT_HCI_OP_LE_LTK_REQ_REPLY`

```c
#define BT_HCI_OP_LE_LTK_REQ_REPLY BT_OP(BT_OGF_LE, 0x001a) /* 0x201a */
```

<a id="ab1ff230560c1f7712e23a22eb44f0e69"></a>

### `BT_HCI_OP_LE_P256_PUBLIC_KEY`

```c
#define BT_HCI_OP_LE_P256_PUBLIC_KEY BT_OP(BT_OGF_LE, 0x0025) /* 0x2025 */
```

<a id="a177ec628eac4a7d535cfe6c07123cb34"></a>

### `BT_HCI_OP_LE_PAST_PARAM`

```c
#define BT_HCI_OP_LE_PAST_PARAM BT_OP(BT_OGF_LE, 0x005c) /* 0x205c */
```

<a id="a589c2da26ce325d5cb45726c772cf7ab"></a>

### `BT_HCI_OP_LE_PER_ADV_CREATE_SYNC`

```c
#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC BT_OP(BT_OGF_LE, 0x0044) /* 0x2044 */
```

<a id="a3803042099104029f5b49536cb769e6c"></a>

### `BT_HCI_OP_LE_PER_ADV_CREATE_SYNC_CANCEL`

```c
#define BT_HCI_OP_LE_PER_ADV_CREATE_SYNC_CANCEL BT_OP(BT_OGF_LE, 0x0045) /* 0x2045 */
```

<a id="ab7d661097af4cc612ac6631b18bbc7e3"></a>

### `BT_HCI_OP_LE_PER_ADV_SET_INFO_TRANSFER`

```c
#define BT_HCI_OP_LE_PER_ADV_SET_INFO_TRANSFER BT_OP(BT_OGF_LE, 0x005b) /* 0x205b */
```

<a id="aa1d0bc8ccc0e1e8835938f8e8d87b7f1"></a>

### `BT_HCI_OP_LE_PER_ADV_SYNC_TRANSFER`

```c
#define BT_HCI_OP_LE_PER_ADV_SYNC_TRANSFER BT_OP(BT_OGF_LE, 0x005a) /* 0x205a */
```

<a id="a57b7b3cab371b4dd230343dfbc5a5e98"></a>

### `BT_HCI_OP_LE_PER_ADV_TERMINATE_SYNC`

```c
#define BT_HCI_OP_LE_PER_ADV_TERMINATE_SYNC BT_OP(BT_OGF_LE, 0x0046) /* 0x2046 */
```

<a id="ac3af817deaf472dbb2a825fd57b67f42"></a>

### `BT_HCI_OP_LE_RAND`

```c
#define BT_HCI_OP_LE_RAND BT_OP(BT_OGF_LE, 0x0018) /* 0x2018 */
```

<a id="afd47d6bbfd4688383aaa6b5014cf0019"></a>

### `BT_HCI_OP_LE_READ_ADV_CHAN_TX_POWER`

```c
#define BT_HCI_OP_LE_READ_ADV_CHAN_TX_POWER BT_OP(BT_OGF_LE, 0x0007) /* 0x2007 */
```

<a id="a8633ee5d0e774f7936252177d6c2ac74"></a>

### `BT_HCI_OP_LE_READ_ALL_LOCAL_SUPPORTED_FEATURES`

```c
#define BT_HCI_OP_LE_READ_ALL_LOCAL_SUPPORTED_FEATURES BT_OP(BT_OGF_LE, 0x0087) /* 0x2087 */
```

<a id="a6e9bed35ad3f4f3e4c5ef5dddb2f98c2"></a>

### `BT_HCI_OP_LE_READ_ALL_REMOTE_FEATURES`

```c
#define BT_HCI_OP_LE_READ_ALL_REMOTE_FEATURES BT_OP(BT_OGF_LE, 0x0088) /* 0x2088 */
```

<a id="aff3ea5f19135609d5553cacec0d700a6"></a>

### `BT_HCI_OP_LE_READ_ANT_INFO`

```c
#define BT_HCI_OP_LE_READ_ANT_INFO BT_OP(BT_OGF_LE, 0x0058) /* 0x2058 */
```

<a id="a965e30fec3f9b5956bd2ea38e57b8b00"></a>

### `BT_HCI_OP_LE_READ_BUFFER_SIZE`

```c
#define BT_HCI_OP_LE_READ_BUFFER_SIZE BT_OP(BT_OGF_LE, 0x0002) /* 0x2002 */
```

<a id="aa7e78541d152c21e101fab5a094c972f"></a>

### `BT_HCI_OP_LE_READ_BUFFER_SIZE_V2`

```c
#define BT_HCI_OP_LE_READ_BUFFER_SIZE_V2 BT_OP(BT_OGF_LE, 0x0060) /* 0x2060 */
```

<a id="a9040e4b5e719d53cc324faa280a670a4"></a>

### `BT_HCI_OP_LE_READ_CHAN_MAP`

```c
#define BT_HCI_OP_LE_READ_CHAN_MAP BT_OP(BT_OGF_LE, 0x0015) /* 0x2015 */
```

<a id="aa58d9ce08e0f1d4a3e5a2f2b1733a6d2"></a>

### `BT_HCI_OP_LE_READ_DEFAULT_DATA_LEN`

```c
#define BT_HCI_OP_LE_READ_DEFAULT_DATA_LEN BT_OP(BT_OGF_LE, 0x0023) /* 0x2023 */
```

<a id="aeeba2e21bd5e33abbd48fa18f5e252f3"></a>

### `BT_HCI_OP_LE_READ_FAL_SIZE`

```c
#define BT_HCI_OP_LE_READ_FAL_SIZE BT_OP(BT_OGF_LE, 0x000f) /* 0x200f */
```

<a id="acd6367a62d2c80d9f2e796d7b6ab1417"></a>

### `BT_HCI_OP_LE_READ_ISO_LINK_QUALITY`

```c
#define BT_HCI_OP_LE_READ_ISO_LINK_QUALITY BT_OP(BT_OGF_LE, 0x0075) /* 0x2075 */
```

<a id="acb7f49f17a60a4e29270c8719b7aeeed"></a>

### `BT_HCI_OP_LE_READ_ISO_TX_SYNC`

```c
#define BT_HCI_OP_LE_READ_ISO_TX_SYNC BT_OP(BT_OGF_LE, 0x0061) /* 0x2061 */
```

<a id="ae4e1d6098793b91ee0e4974886b98336"></a>

### `BT_HCI_OP_LE_READ_LOCAL_FEATURES`

```c
#define BT_HCI_OP_LE_READ_LOCAL_FEATURES BT_OP(BT_OGF_LE, 0x0003) /* 0x2003 */
```

<a id="af8ec9d3b6889a8530bc5977b8594fea6"></a>

### `BT_HCI_OP_LE_READ_LOCAL_RPA`

```c
#define BT_HCI_OP_LE_READ_LOCAL_RPA BT_OP(BT_OGF_LE, 0x002c) /* 0x202c */
```

<a id="a0246ea11fada7570bf59e73250b49b95"></a>

### `BT_HCI_OP_LE_READ_MAX_ADV_DATA_LEN`

```c
#define BT_HCI_OP_LE_READ_MAX_ADV_DATA_LEN BT_OP(BT_OGF_LE, 0x003a) /* 0x203a */
```

<a id="aafb5872650d77d9f4c6ae43038ef2bf1"></a>

### `BT_HCI_OP_LE_READ_MAX_DATA_LEN`

```c
#define BT_HCI_OP_LE_READ_MAX_DATA_LEN BT_OP(BT_OGF_LE, 0x002f) /* 0x202f */
```

<a id="a46425554910f04a93f8819f3aede38c1"></a>

### `BT_HCI_OP_LE_READ_MIN_SUPPORTED_CONN_INTERVAL`

```c
#define BT_HCI_OP_LE_READ_MIN_SUPPORTED_CONN_INTERVAL BT_OP(BT_OGF_LE, 0x00A3) /* 0x20A3 */
```

<a id="a8d2a855322d0aa454ed00e1458cf9a38"></a>

### `BT_HCI_OP_LE_READ_NUM_ADV_SETS`

```c
#define BT_HCI_OP_LE_READ_NUM_ADV_SETS BT_OP(BT_OGF_LE, 0x003b) /* 0x203b */
```

<a id="a6c605e63bd1633f3423a915cf4db00e8"></a>

### `BT_HCI_OP_LE_READ_PEER_RPA`

```c
#define BT_HCI_OP_LE_READ_PEER_RPA BT_OP(BT_OGF_LE, 0x002b) /* 0x202b */
```

<a id="a3e2fd45c015809e131ac6b3f6a9c72fc"></a>

### `BT_HCI_OP_LE_READ_PER_ADV_LIST_SIZE`

```c
#define BT_HCI_OP_LE_READ_PER_ADV_LIST_SIZE BT_OP(BT_OGF_LE, 0x004a) /* 0x204a */
```

<a id="ad2e063f4522a64ceeb36c1d95835e74e"></a>

### `BT_HCI_OP_LE_READ_PHY`

```c
#define BT_HCI_OP_LE_READ_PHY BT_OP(BT_OGF_LE, 0x0030) /* 0x2030 */
```

<a id="ac8d5165a3a5d190b8e2d31feb79a17c9"></a>

### `BT_HCI_OP_LE_READ_REMOTE_FEATURES`

```c
#define BT_HCI_OP_LE_READ_REMOTE_FEATURES BT_OP(BT_OGF_LE, 0x0016) /* 0x2016 */
```

<a id="ac5bc187df83f28a48ba1f87f84aed54a"></a>

### `BT_HCI_OP_LE_READ_REMOTE_TX_POWER_LEVEL`

```c
#define BT_HCI_OP_LE_READ_REMOTE_TX_POWER_LEVEL BT_OP(BT_OGF_LE, 0x0077) /* 0x2077 */
```

<a id="a6c454d3276f7eaae542b13becad6482c"></a>

### `BT_HCI_OP_LE_READ_RF_PATH_COMP`

```c
#define BT_HCI_OP_LE_READ_RF_PATH_COMP BT_OP(BT_OGF_LE, 0x004c) /* 0x204c */
```

<a id="a45b38708e807c784bd734ba1f69c7f86"></a>

### `BT_HCI_OP_LE_READ_RL_SIZE`

```c
#define BT_HCI_OP_LE_READ_RL_SIZE BT_OP(BT_OGF_LE, 0x002a) /* 0x202a */
```

<a id="a286869ebde03594d56ecd8bc1aa7c73c"></a>

### `BT_HCI_OP_LE_READ_SUPP_STATES`

```c
#define BT_HCI_OP_LE_READ_SUPP_STATES BT_OP(BT_OGF_LE, 0x001c) /* 0x201c */
```

<a id="a77d132306109474465575369db342dbd"></a>

### `BT_HCI_OP_LE_READ_TX_POWER`

```c
#define BT_HCI_OP_LE_READ_TX_POWER BT_OP(BT_OGF_LE, 0x004b) /* 0x204b */
```

<a id="a6c58ebc2082de8c2c3aafd9ee77dfd11"></a>

### `BT_HCI_OP_LE_REJECT_CIS`

```c
#define BT_HCI_OP_LE_REJECT_CIS BT_OP(BT_OGF_LE, 0x0067) /* 0x2067 */
```

<a id="aedbb03b04ed567e54642e42ae758538a"></a>

### `BT_HCI_OP_LE_REM_DEV_FROM_FAL`

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_FAL BT_OP(BT_OGF_LE, 0x0012) /* 0x2012 */
```

<a id="a8545e1ede192257a4383eea6b2e932b7"></a>

### `BT_HCI_OP_LE_REM_DEV_FROM_PER_ADV_LIST`

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_PER_ADV_LIST BT_OP(BT_OGF_LE, 0x0048) /* 0x2048 */
```

<a id="ac4c11605a4cd244ec3ffa972295396fa"></a>

### `BT_HCI_OP_LE_REM_DEV_FROM_RL`

```c
#define BT_HCI_OP_LE_REM_DEV_FROM_RL BT_OP(BT_OGF_LE, 0x0028) /* 0x2028 */
```

<a id="ae802afd7081a39f062f65e5c0994a9e4"></a>

### `BT_HCI_OP_LE_REMOVE_ADV_SET`

```c
#define BT_HCI_OP_LE_REMOVE_ADV_SET BT_OP(BT_OGF_LE, 0x003c) /* 0x203c */
```

<a id="ab623f680f2031fc03bd73199ebbf4e4e"></a>

### `BT_HCI_OP_LE_REMOVE_CIG`

```c
#define BT_HCI_OP_LE_REMOVE_CIG BT_OP(BT_OGF_LE, 0x0065) /* 0x2065 */
```

<a id="addec65d76f67f07c029216435cf117c6"></a>

### `BT_HCI_OP_LE_REMOVE_ISO_PATH`

```c
#define BT_HCI_OP_LE_REMOVE_ISO_PATH BT_OP(BT_OGF_LE, 0x006f) /* 0x206f */
```

<a id="a0057468b1638b07f799b62a24cd096d9"></a>

### `BT_HCI_OP_LE_REQ_PEER_SC`

```c
#define BT_HCI_OP_LE_REQ_PEER_SC BT_OP(BT_OGF_LE, 0x006d) /* 0x206d */
```

<a id="abd18c6854a0dc97c451b498816f206e4"></a>

### `BT_HCI_OP_LE_RX_TEST`

```c
#define BT_HCI_OP_LE_RX_TEST BT_OP(BT_OGF_LE, 0x001d) /* 0x201d */
```

<a id="abe1567f7cf83148b3f2214b6e0787da0"></a>

### `BT_HCI_OP_LE_RX_TEST_V3`

```c
#define BT_HCI_OP_LE_RX_TEST_V3 BT_OP(BT_OGF_LE, 0x004f) /* 0x204f */
```

<a id="a183431c86b7eb32b7c00e6b3a000f29e"></a>

### `BT_HCI_OP_LE_SET_ADDR_RES_ENABLE`

```c
#define BT_HCI_OP_LE_SET_ADDR_RES_ENABLE BT_OP(BT_OGF_LE, 0x002d) /* 0x202d */
```

<a id="adb8f5236ac1b5eaa4c82d620c78c45aa"></a>

### `BT_HCI_OP_LE_SET_ADV_DATA`

```c
#define BT_HCI_OP_LE_SET_ADV_DATA BT_OP(BT_OGF_LE, 0x0008) /* 0x2008 */
```

<a id="a5f218883bda0698b5c52fd6a34d5e9f0"></a>

### `BT_HCI_OP_LE_SET_ADV_ENABLE`

```c
#define BT_HCI_OP_LE_SET_ADV_ENABLE BT_OP(BT_OGF_LE, 0x000a) /* 0x200a */
```

<a id="a446b6e7a74800ee657f5ddcf1c198d02"></a>

### `BT_HCI_OP_LE_SET_ADV_PARAM`

```c
#define BT_HCI_OP_LE_SET_ADV_PARAM BT_OP(BT_OGF_LE, 0x0006) /* 0x2006 */
```

<a id="ac96cefff0857a4d19025a2d9dec8333e"></a>

### `BT_HCI_OP_LE_SET_ADV_SET_RANDOM_ADDR`

```c
#define BT_HCI_OP_LE_SET_ADV_SET_RANDOM_ADDR BT_OP(BT_OGF_LE, 0x0035) /* 0x2035 */
```

<a id="a0a4b2732026a6300d4b354eb6d93905d"></a>

### `BT_HCI_OP_LE_SET_CIG_PARAMS`

```c
#define BT_HCI_OP_LE_SET_CIG_PARAMS BT_OP(BT_OGF_LE, 0x0062) /* 0x2062 */
```

<a id="a54df2d12a0c07bab9fb3521dc69ff2f4"></a>

### `BT_HCI_OP_LE_SET_CIG_PARAMS_TEST`

```c
#define BT_HCI_OP_LE_SET_CIG_PARAMS_TEST BT_OP(BT_OGF_LE, 0x0063) /* 0x2063 */
```

<a id="a728b9a505c9a2f719424bd277f7e8765"></a>

### `BT_HCI_OP_LE_SET_CL_CTE_SAMPLING_ENABLE`

```c
#define BT_HCI_OP_LE_SET_CL_CTE_SAMPLING_ENABLE BT_OP(BT_OGF_LE, 0x0053) /* 0x2053 */
```

<a id="a5527fd8badb977f2ef061ba76468ccf3"></a>

### `BT_HCI_OP_LE_SET_CL_CTE_TX_ENABLE`

```c
#define BT_HCI_OP_LE_SET_CL_CTE_TX_ENABLE BT_OP(BT_OGF_LE, 0x0052) /* 0x2052 */
```

<a id="a900509c6e7485b44de09a43555225ce8"></a>

### `BT_HCI_OP_LE_SET_CL_CTE_TX_PARAMS`

```c
#define BT_HCI_OP_LE_SET_CL_CTE_TX_PARAMS BT_OP(BT_OGF_LE, 0x0051) /* 0x2051 */
```

<a id="a8a079c51fc7c37f29afeda663206c59e"></a>

### `BT_HCI_OP_LE_SET_CONN_CTE_RX_PARAMS`

```c
#define BT_HCI_OP_LE_SET_CONN_CTE_RX_PARAMS BT_OP(BT_OGF_LE, 0x0054) /* 0x2054 */
```

<a id="af4110be6e09c80cd7362d9b2580243e7"></a>

### `BT_HCI_OP_LE_SET_CONN_CTE_TX_PARAMS`

```c
#define BT_HCI_OP_LE_SET_CONN_CTE_TX_PARAMS BT_OP(BT_OGF_LE, 0x0055) /* 0x2055 */
```

<a id="a5aeb49334449851866537ea8703f5ab0"></a>

### `BT_HCI_OP_LE_SET_DATA_LEN`

```c
#define BT_HCI_OP_LE_SET_DATA_LEN BT_OP(BT_OGF_LE, 0x0022) /* 0x2022 */
```

<a id="aaa4e3fd27b4157a617a5fb6817bc1881"></a>

### `BT_HCI_OP_LE_SET_DEFAULT_PHY`

```c
#define BT_HCI_OP_LE_SET_DEFAULT_PHY BT_OP(BT_OGF_LE, 0x0031) /* 0x2031 */
```

<a id="a0cbe2f1d110c04231e859f18e3a102f8"></a>

### `BT_HCI_OP_LE_SET_DEFAULT_RATE_PARAMETERS`

```c
#define BT_HCI_OP_LE_SET_DEFAULT_RATE_PARAMETERS BT_OP(BT_OGF_LE, 0x00A2) /* 0x20A2 */
```

<a id="a05c5f2cb7028e3ae831047e53b767836"></a>

### `BT_HCI_OP_LE_SET_DEFAULT_SUBRATE`

```c
#define BT_HCI_OP_LE_SET_DEFAULT_SUBRATE BT_OP(BT_OGF_LE, 0x007D) /* 0x207D */
```

<a id="aa9a3688473bf15c8845f52a3128362f7"></a>

### `BT_HCI_OP_LE_SET_EVENT_MASK`

```c
#define BT_HCI_OP_LE_SET_EVENT_MASK BT_OP(BT_OGF_LE, 0x0001) /* 0x2001 */
```

<a id="a563769ae57bb58be9d7ee8e92019cb99"></a>

### `BT_HCI_OP_LE_SET_EXT_ADV_DATA`

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_DATA BT_OP(BT_OGF_LE, 0x0037) /* 0x2037 */
```

<a id="a99e9573f9bd290fb18f82a327ca55ecd"></a>

### `BT_HCI_OP_LE_SET_EXT_ADV_ENABLE`

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_ENABLE BT_OP(BT_OGF_LE, 0x0039) /* 0x2039 */
```

<a id="a098efdd7908adafd26b8e3f63508c476"></a>

### `BT_HCI_OP_LE_SET_EXT_ADV_PARAM`

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM BT_OP(BT_OGF_LE, 0x0036) /* 0x2036 */
```

<a id="a66ffb876e588d64ce2b2d9091de94806"></a>

### `BT_HCI_OP_LE_SET_EXT_ADV_PARAM_V2`

```c
#define BT_HCI_OP_LE_SET_EXT_ADV_PARAM_V2 BT_OP(BT_OGF_LE, 0x007F) /* 0x207F */
```

<a id="af7a8256887657e482084d4ed3810195b"></a>

### `BT_HCI_OP_LE_SET_EXT_SCAN_ENABLE`

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_ENABLE BT_OP(BT_OGF_LE, 0x0042) /* 0x2042 */
```

<a id="a7b0687c9e1faae997b76ece821338fd7"></a>

### `BT_HCI_OP_LE_SET_EXT_SCAN_PARAM`

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_PARAM BT_OP(BT_OGF_LE, 0x0041) /* 0x2041 */
```

<a id="a586395798b3d827ab17634287862ef54"></a>

### `BT_HCI_OP_LE_SET_EXT_SCAN_RSP_DATA`

```c
#define BT_HCI_OP_LE_SET_EXT_SCAN_RSP_DATA BT_OP(BT_OGF_LE, 0x0038) /* 0x2038 */
```

<a id="a6224aab014342d93bcb16c717cd52421"></a>

### `BT_HCI_OP_LE_SET_HOST_CHAN_CLASSIF`

```c
#define BT_HCI_OP_LE_SET_HOST_CHAN_CLASSIF BT_OP(BT_OGF_LE, 0x0014) /* 0x2014 */
```

<a id="a29555bdcc7b439c2d0311fcb0721dc0b"></a>

### `BT_HCI_OP_LE_SET_HOST_FEATURE`

```c
#define BT_HCI_OP_LE_SET_HOST_FEATURE BT_OP(BT_OGF_LE, 0x0074) /* 0x2074 */
```

<a id="a09c0d554937de38a7b74661a2820237b"></a>

### `BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_ENABLE`

```c
#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_ENABLE BT_OP(BT_OGF_LE, 0x0079) /* 0x2079 */
```

<a id="a48a3e41f8d6598e617d02ebc609911c6"></a>

### `BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_PARAMETERS`

```c
#define BT_HCI_OP_LE_SET_PATH_LOSS_REPORTING_PARAMETERS BT_OP(BT_OGF_LE, 0x0078) /* 0x2078 */
```

<a id="ae6611e7b72b057ac9d4004a1772fe435"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_DATA`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_DATA BT_OP(BT_OGF_LE, 0x003f) /* 0x203f */
```

<a id="a3ae23554c13b099b50b129462e08afe4"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_ENABLE`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_ENABLE BT_OP(BT_OGF_LE, 0x0040) /* 0x2040 */
```

<a id="a3a111d29fd682fa825f4f9c8c358243f"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_PARAM`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_PARAM BT_OP(BT_OGF_LE, 0x003e) /* 0x203e */
```

<a id="a1125bfc15404124bf4bd533520be0f77"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_PARAM_V2`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_PARAM_V2 BT_OP(BT_OGF_LE, 0x0086) /* 0x2086 */
```

<a id="a047efb565b182e90178513dc3db6390f"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_RECV_ENABLE`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_RECV_ENABLE BT_OP(BT_OGF_LE, 0x0059) /* 0x2059 */
```

<a id="a2be1e66c896dca2022c04164fd94da49"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_RESPONSE_DATA`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_RESPONSE_DATA BT_OP(BT_OGF_LE, 0x0083) /* 0x2083 */
```

<a id="a44e729aebc339ada5deb86ad9d350404"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_SUBEVENT_DATA`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_SUBEVENT_DATA BT_OP(BT_OGF_LE, 0x0082) /* 0x2082 */
```

<a id="aea7f44f563c109be1676454412757fab"></a>

### `BT_HCI_OP_LE_SET_PER_ADV_SYNC_SUBEVENT`

```c
#define BT_HCI_OP_LE_SET_PER_ADV_SYNC_SUBEVENT BT_OP(BT_OGF_LE, 0x0084) /* 0x2084 */
```

<a id="a1d21c4ffe4db8caafa374a9138e179fa"></a>

### `BT_HCI_OP_LE_SET_PHY`

```c
#define BT_HCI_OP_LE_SET_PHY BT_OP(BT_OGF_LE, 0x0032) /* 0x2032 */
```

<a id="a7e1fad2d353904bb345f3a1579c98576"></a>

### `BT_HCI_OP_LE_SET_PRIVACY_MODE`

```c
#define BT_HCI_OP_LE_SET_PRIVACY_MODE BT_OP(BT_OGF_LE, 0x004e) /* 0x204e */
```

<a id="af34eced252d01bbc27bd8e19ed4dc80e"></a>

### `BT_HCI_OP_LE_SET_RANDOM_ADDRESS`

```c
#define BT_HCI_OP_LE_SET_RANDOM_ADDRESS BT_OP(BT_OGF_LE, 0x0005) /* 0x2005 */
```

<a id="aeabb8438460e694867d855cf7f8e3b31"></a>

### `BT_HCI_OP_LE_SET_RPA_TIMEOUT`

```c
#define BT_HCI_OP_LE_SET_RPA_TIMEOUT BT_OP(BT_OGF_LE, 0x002e) /* 0x202e */
```

<a id="a894cf6904ec16b11f6d930d72d30fce6"></a>

### `BT_HCI_OP_LE_SET_SCAN_ENABLE`

```c
#define BT_HCI_OP_LE_SET_SCAN_ENABLE BT_OP(BT_OGF_LE, 0x000c) /* 0x200c */
```

<a id="a56db98b00b57fd713f8cedbf34e2f8fa"></a>

### `BT_HCI_OP_LE_SET_SCAN_PARAM`

```c
#define BT_HCI_OP_LE_SET_SCAN_PARAM BT_OP(BT_OGF_LE, 0x000b) /* 0x200b */
```

<a id="a81718bfe6796648eb5831f3cd03049c8"></a>

### `BT_HCI_OP_LE_SET_SCAN_RSP_DATA`

```c
#define BT_HCI_OP_LE_SET_SCAN_RSP_DATA BT_OP(BT_OGF_LE, 0x0009) /* 0x2009 */
```

<a id="aec22a58c052e856558b316b4f94f8561"></a>

### `BT_HCI_OP_LE_SET_TX_POWER_REPORT_ENABLE`

```c
#define BT_HCI_OP_LE_SET_TX_POWER_REPORT_ENABLE BT_OP(BT_OGF_LE, 0x007A) /* 0x207A */
```

<a id="a97de1164704f5d3c517b9c2ff6b0584a"></a>

### `BT_HCI_OP_LE_SETUP_ISO_PATH`

```c
#define BT_HCI_OP_LE_SETUP_ISO_PATH BT_OP(BT_OGF_LE, 0x006e) /* 0x206e */
```

<a id="afececfce5819f1b8555ce47fbde2aa0b"></a>

### `BT_HCI_OP_LE_START_ENCRYPTION`

```c
#define BT_HCI_OP_LE_START_ENCRYPTION BT_OP(BT_OGF_LE, 0x0019) /* 0x2019 */
```

<a id="af6825cfdac02620af56b8c747d1ef308"></a>

### `BT_HCI_OP_LE_SUBRATE_REQUEST`

```c
#define BT_HCI_OP_LE_SUBRATE_REQUEST BT_OP(BT_OGF_LE, 0x007E) /* 0x207E */
```

<a id="acc5e6c17e33cf43f2a68cb93bb09ef20"></a>

### `BT_HCI_OP_LE_TERMINATE_BIG`

```c
#define BT_HCI_OP_LE_TERMINATE_BIG BT_OP(BT_OGF_LE, 0x006a) /* 0x206a */
```

<a id="a7ff8a81ae09ddb0d18f999fe454e41df"></a>

### `BT_HCI_OP_LE_TEST_END`

```c
#define BT_HCI_OP_LE_TEST_END BT_OP(BT_OGF_LE, 0x001f) /* 0x201f */
```

<a id="af5fe87cbe280dcf26ddc21952e84e93e"></a>

### `BT_HCI_OP_LE_TX_TEST`

```c
#define BT_HCI_OP_LE_TX_TEST BT_OP(BT_OGF_LE, 0x001e) /* 0x201e */
```

<a id="ad570a3edcefcf927e5253805e1d3d4e4"></a>

### `BT_HCI_OP_LE_TX_TEST_V3`

```c
#define BT_HCI_OP_LE_TX_TEST_V3 BT_OP(BT_OGF_LE, 0x0050) /* 0x2050 */
```

<a id="a13827b7d7b656ea02c0620ec7b525f65"></a>

### `BT_HCI_OP_LE_TX_TEST_V4`

```c
#define BT_HCI_OP_LE_TX_TEST_V4 BT_OP(BT_OGF_LE, 0x007B) /* 0x207B */
```

<a id="ae344c1ab9af250787b9ed8109ad3cde0"></a>

### `BT_HCI_OP_LE_WRITE_DEFAULT_DATA_LEN`

```c
#define BT_HCI_OP_LE_WRITE_DEFAULT_DATA_LEN BT_OP(BT_OGF_LE, 0x0024) /* 0x2024 */
```

<a id="a2afc45fe32acff87265d36865c8d0b17"></a>

### `BT_HCI_OP_LE_WRITE_LE_HOST_SUPP`

```c
#define BT_HCI_OP_LE_WRITE_LE_HOST_SUPP BT_OP(BT_OGF_BASEBAND, 0x006d) /* 0x0c6d */
```

<a id="a766b66d1fc7df1d8924d060217de9b9b"></a>

### `BT_HCI_OP_LE_WRITE_RF_PATH_COMP`

```c
#define BT_HCI_OP_LE_WRITE_RF_PATH_COMP BT_OP(BT_OGF_LE, 0x004d) /* 0x204d */
```

<a id="a7db25bd8bdbd4351e0dcef1df8dc7077"></a>

### `BT_HCI_OP_LINK_KEY_NEG_REPLY`

```c
#define BT_HCI_OP_LINK_KEY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000c) /* 0x040c */
```

<a id="a7da489e05d679c00f6cbbca0dfaaf136"></a>

### `BT_HCI_OP_LINK_KEY_REPLY`

```c
#define BT_HCI_OP_LINK_KEY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000b) /* 0x040b */
```

<a id="a5833de4cefd59cee9c614163de7e927b"></a>

### `BT_HCI_OP_PIN_CODE_NEG_REPLY`

```c
#define BT_HCI_OP_PIN_CODE_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000e) /* 0x040e */
```

<a id="a7713e5641070ac7fca91e027fc9b8c40"></a>

### `BT_HCI_OP_PIN_CODE_REPLY`

```c
#define BT_HCI_OP_PIN_CODE_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x000d) /* 0x040d */
```

<a id="a0ea6134bcd33e24b068f35d080cdc4e0"></a>

### `BT_HCI_OP_READ_AUTH_PAYLOAD_TIMEOUT`

```c
#define BT_HCI_OP_READ_AUTH_PAYLOAD_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x007b) /* 0x0c7b */
```

<a id="a4ba1bf2078ac12686e2a7727f637f70b"></a>

### `BT_HCI_OP_READ_BD_ADDR`

```c
#define BT_HCI_OP_READ_BD_ADDR BT_OP(BT_OGF_INFO, 0x0009) /* 0x1009 */
```

<a id="acd5d9ecda744969d4692e6ebface2e53"></a>

### `BT_HCI_OP_READ_BUFFER_SIZE`

```c
#define BT_HCI_OP_READ_BUFFER_SIZE BT_OP(BT_OGF_INFO, 0x0005) /* 0x1005 */
```

<a id="aa700370e995f2bfda85b385f70821c10"></a>

### `BT_HCI_OP_READ_CLASS_OF_DEVICE`

```c
#define BT_HCI_OP_READ_CLASS_OF_DEVICE BT_OP(BT_OGF_BASEBAND, 0x0023) /* 0x0c23 */
```

<a id="a4b9e24d16cd92ce6ee1d6444410cfb43"></a>

### `BT_HCI_OP_READ_CODEC_CAPABILITIES`

```c
#define BT_HCI_OP_READ_CODEC_CAPABILITIES BT_OP(BT_OGF_INFO, 0x000e) /* 0x100e */
```

<a id="a8755487f4672f196051cc513894e4603"></a>

### `BT_HCI_OP_READ_CODECS`

```c
#define BT_HCI_OP_READ_CODECS BT_OP(BT_OGF_INFO, 0x000b) /* 0x100b */
```

<a id="acb09b1a94453c1c341decabc029bbc04"></a>

### `BT_HCI_OP_READ_CODECS_V2`

```c
#define BT_HCI_OP_READ_CODECS_V2 BT_OP(BT_OGF_INFO, 0x000d) /* 0x100d */
```

<a id="af302a5e40644307f522154f3803572d0"></a>

### `BT_HCI_OP_READ_CONN_ACCEPT_TIMEOUT`

```c
#define BT_HCI_OP_READ_CONN_ACCEPT_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0015) /* 0x0c15 */
```

<a id="a9a183b26d18453d5daa6de2dcbe4d9a1"></a>

### `BT_HCI_OP_READ_CTLR_DELAY`

```c
#define BT_HCI_OP_READ_CTLR_DELAY BT_OP(BT_OGF_INFO, 0x000f) /* 0x100f */
```

<a id="a0f01d3fc3b2cfb4287691b8f66a7cf71"></a>

### `BT_HCI_OP_READ_DEFAULT_LINK_POLICY_SETTINGS`

```c
#define BT_HCI_OP_READ_DEFAULT_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000e)
```

<a id="adefeb2117010fa2d53937ce513e28a18"></a>

### `BT_HCI_OP_READ_ENCRYPTION_KEY_SIZE`

```c
#define BT_HCI_OP_READ_ENCRYPTION_KEY_SIZE BT_OP(BT_OGF_STATUS, 0x0008) /* 0x1408 */
```

<a id="a37aedd6992f499b53ae16dea98be07d7"></a>

### `BT_HCI_OP_READ_LINK_POLICY_SETTINGS`

```c
#define BT_HCI_OP_READ_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000c)
```

<a id="a47baf48cd68227e3a7261653adc3f577"></a>

### `BT_HCI_OP_READ_LINK_SUPERVISION_TIMEOUT`

```c
#define BT_HCI_OP_READ_LINK_SUPERVISION_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0036) /* 0x0c36 */
```

HCI 读取链路监督超时（Read Link Supervision Timeout）操作码。

<a id="a882f120b35a9baa2f70bc33ef5ced6d3"></a>

### `BT_HCI_OP_READ_LOCAL_EXT_FEATURES`

```c
#define BT_HCI_OP_READ_LOCAL_EXT_FEATURES BT_OP(BT_OGF_INFO, 0x0004) /* 0x1004 */
```

<a id="a8524505dff48ceb41c008c8662da6408"></a>

### `BT_HCI_OP_READ_LOCAL_FEATURES`

```c
#define BT_HCI_OP_READ_LOCAL_FEATURES BT_OP(BT_OGF_INFO, 0x0003) /* 0x1003 */
```

<a id="a195b8faf6d7d3e4f1b528185c73b4d67"></a>

### `BT_HCI_OP_READ_LOCAL_VERSION_INFO`

```c
#define BT_HCI_OP_READ_LOCAL_VERSION_INFO BT_OP(BT_OGF_INFO, 0x0001) /* 0x1001 */
```

<a id="a87f6747b2b5d52a7886a1ec72100d9d0"></a>

### `BT_HCI_OP_READ_REMOTE_EXT_FEATURES`

```c
#define BT_HCI_OP_READ_REMOTE_EXT_FEATURES BT_OP(BT_OGF_LINK_CTRL, 0x001c) /* 0x041c */
```

<a id="ab6282249d4c14412674083007346b005"></a>

### `BT_HCI_OP_READ_REMOTE_FEATURES`

```c
#define BT_HCI_OP_READ_REMOTE_FEATURES BT_OP(BT_OGF_LINK_CTRL, 0x001b) /* 0x041b */
```

<a id="ae723b797305fe7a370b94d8c865e5708"></a>

### `BT_HCI_OP_READ_REMOTE_VERSION_INFO`

```c
#define BT_HCI_OP_READ_REMOTE_VERSION_INFO BT_OP(BT_OGF_LINK_CTRL, 0x001d) /* 0x041d */
```

<a id="a528902591490d9d20a6966a042254b3a"></a>

### `BT_HCI_OP_READ_RSSI`

```c
#define BT_HCI_OP_READ_RSSI BT_OP(BT_OGF_STATUS, 0x0005) /* 0x1405 */
```

<a id="ac0d7533d221db0fa44cfb83135dfcc6a"></a>

### `BT_HCI_OP_READ_SUPPORTED_COMMANDS`

```c
#define BT_HCI_OP_READ_SUPPORTED_COMMANDS BT_OP(BT_OGF_INFO, 0x0002) /* 0x1002 */
```

<a id="aaac00b7d9f9f96d1438643ee054ab21a"></a>

### `BT_HCI_OP_READ_TX_POWER_LEVEL`

```c
#define BT_HCI_OP_READ_TX_POWER_LEVEL BT_OP(BT_OGF_BASEBAND, 0x002d) /* 0x0c2d */
```

<a id="aabb1f800ad4574e0350007af94cd786d"></a>

### `BT_HCI_OP_REJECT_CONN_REQ`

```c
#define BT_HCI_OP_REJECT_CONN_REQ BT_OP(BT_OGF_LINK_CTRL, 0x000a) /* 0x040a */
```

<a id="a76f79f4e14396297cc5db4ca8dba0c4c"></a>

### `BT_HCI_OP_REMOTE_NAME_CANCEL`

```c
#define BT_HCI_OP_REMOTE_NAME_CANCEL BT_OP(BT_OGF_LINK_CTRL, 0x001a) /* 0x041a */
```

<a id="a2e759212d10ecd3a2e975379bf18d374"></a>

### `BT_HCI_OP_REMOTE_NAME_REQUEST`

```c
#define BT_HCI_OP_REMOTE_NAME_REQUEST BT_OP(BT_OGF_LINK_CTRL, 0x0019) /* 0x0419 */
```

<a id="abb515eb4ea9e66503bf1f375af01a6c0"></a>

### `BT_HCI_OP_RESET`

```c
#define BT_HCI_OP_RESET BT_OP(BT_OGF_BASEBAND, 0x0003) /* 0x0c03 */
```

<a id="ac32c04cf6bc9de299f0a307dbeed63f3"></a>

### `BT_HCI_OP_SET_CONN_ENCRYPT`

```c
#define BT_HCI_OP_SET_CONN_ENCRYPT BT_OP(BT_OGF_LINK_CTRL, 0x0013) /* 0x0413 */
```

<a id="abe87fa64cb529d2cfe7ddf4fa045d3b5"></a>

### `BT_HCI_OP_SET_CTL_TO_HOST_FLOW`

```c
#define BT_HCI_OP_SET_CTL_TO_HOST_FLOW BT_OP(BT_OGF_BASEBAND, 0x0031) /* 0x0c31 */
```

<a id="abb9bf6d936310a43c4a88244ad12640d"></a>

### `BT_HCI_OP_SET_EVENT_MASK`

```c
#define BT_HCI_OP_SET_EVENT_MASK BT_OP(BT_OGF_BASEBAND, 0x0001) /* 0x0c01 */
```

<a id="af5d2954950e00dfd5a69fc19db0fe530"></a>

### `BT_HCI_OP_SET_EVENT_MASK_PAGE_2`

```c
#define BT_HCI_OP_SET_EVENT_MASK_PAGE_2 BT_OP(BT_OGF_BASEBAND, 0x0063) /* 0x0c63 */
```

<a id="ac4e12b8f7b89a658da7bbbaf371358e0"></a>

### `BT_HCI_OP_SETUP_SYNC_CONN`

```c
#define BT_HCI_OP_SETUP_SYNC_CONN BT_OP(BT_OGF_LINK_CTRL, 0x0028) /* 0x0428 */
```

<a id="a65cd61abc9ad7854974fd98579ad41fe"></a>

### `BT_HCI_OP_SNIFF_MODE`

```c
#define BT_HCI_OP_SNIFF_MODE BT_OP(BT_OGF_LINK_POLICY, 0x0003) /* 0x0803 */
```

<a id="af646337afbea8522c2617ddb525bdcf1"></a>

### `BT_HCI_OP_SNIFF_SUBRATING`

```c
#define BT_HCI_OP_SNIFF_SUBRATING BT_OP(BT_OGF_LINK_POLICY, 0x0011) /* 0x0811 */
```

HCI Sniff 子速率（Sniff Subrating）命令操作码（Opcode）。

<a id="a58777d073768707b12220b7208aa0dcf"></a>

### `BT_HCI_OP_SWITCH_ROLE`

```c
#define BT_HCI_OP_SWITCH_ROLE BT_OP(BT_OGF_LINK_POLICY, 0x000b)
```

<a id="aecc09326c190d2ab7b89f99375cd39bd"></a>

### `BT_HCI_OP_USER_CONFIRM_NEG_REPLY`

```c
#define BT_HCI_OP_USER_CONFIRM_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002d) /* 0x042d */
```

<a id="ab688441778a4239e1e8f2b2e0b74004f"></a>

### `BT_HCI_OP_USER_CONFIRM_REPLY`

```c
#define BT_HCI_OP_USER_CONFIRM_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002c) /* 0x042c */
```

<a id="a96f9c5c3439d829dfac94cca9ad1f015"></a>

### `BT_HCI_OP_USER_PASSKEY_NEG_REPLY`

```c
#define BT_HCI_OP_USER_PASSKEY_NEG_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002f) /* 0x042f */
```

<a id="ad1fce315b731f9978cd52a8c23994a10"></a>

### `BT_HCI_OP_USER_PASSKEY_REPLY`

```c
#define BT_HCI_OP_USER_PASSKEY_REPLY BT_OP(BT_OGF_LINK_CTRL, 0x002e) /* 0x042e */
```

<a id="ae74450b7b643f947fa2e83a80e0e2fae"></a>

### `BT_HCI_OP_WRITE_AUTH_PAYLOAD_TIMEOUT`

```c
#define BT_HCI_OP_WRITE_AUTH_PAYLOAD_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x007c) /* 0x0c7c */
```

<a id="ace988e19fa62bf61654a329acaf99018"></a>

### `BT_HCI_OP_WRITE_CLASS_OF_DEVICE`

```c
#define BT_HCI_OP_WRITE_CLASS_OF_DEVICE BT_OP(BT_OGF_BASEBAND, 0x0024) /* 0x0c24 */
```

<a id="a6799bd267ef7c19b05ed2dd57baf0393"></a>

### `BT_HCI_OP_WRITE_CONN_ACCEPT_TIMEOUT`

```c
#define BT_HCI_OP_WRITE_CONN_ACCEPT_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0016) /* 0x0c16 */
```

<a id="afd0a0fa1a8959d6390d59bd6d658432d"></a>

### `BT_HCI_OP_WRITE_CURRENT_IAC_LAP`

```c
#define BT_HCI_OP_WRITE_CURRENT_IAC_LAP BT_OP(BT_OGF_BASEBAND, 0x003a) /* 0x0c3a */
```

<a id="a4277a54a2dac31ac87b4f7841f871571"></a>

### `BT_HCI_OP_WRITE_DEFAULT_LINK_POLICY_SETTINGS`

```c
#define BT_HCI_OP_WRITE_DEFAULT_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000f)
```

<a id="af9fce0fe5f15e5888a40d1d6c492fdc7"></a>

### `BT_HCI_OP_WRITE_EXT_INQUIRY_RESPONSE`

```c
#define BT_HCI_OP_WRITE_EXT_INQUIRY_RESPONSE BT_OP(BT_OGF_BASEBAND, 0x0052) /* 0x0c52 */
```

HCI 写入扩展查询响应（Write Extended Inquiry Response）操作码。

<a id="a04985a29d0f131c09aeb9769689b727b"></a>

### `BT_HCI_OP_WRITE_INQUIRY_MODE`

```c
#define BT_HCI_OP_WRITE_INQUIRY_MODE BT_OP(BT_OGF_BASEBAND, 0x0045) /* 0x0c45 */
```

<a id="a808b7afb7e390569f77d43602d894e34"></a>

### `BT_HCI_OP_WRITE_INQUIRY_SCAN_ACTIVITY`

```c
#define BT_HCI_OP_WRITE_INQUIRY_SCAN_ACTIVITY BT_OP(BT_OGF_BASEBAND, 0x001e) /* 0x0c1e */
```

HCI 写入查询扫描活动参数（Write Inquiry Scan Activity）操作码。

<a id="a8a3526f60f1d08f2cb63c2e26fae96b7"></a>

### `BT_HCI_OP_WRITE_INQUIRY_SCAN_TYPE`

```c
#define BT_HCI_OP_WRITE_INQUIRY_SCAN_TYPE BT_OP(BT_OGF_BASEBAND, 0x0043) /* 0x0c43 */
```

HCI 写入查询扫描类型（Write Inquiry Scan Type）操作码。

<a id="a9b47fe0b9a5f34d031e9e45790f0522b"></a>

### `BT_HCI_OP_WRITE_LINK_POLICY_SETTINGS`

```c
#define BT_HCI_OP_WRITE_LINK_POLICY_SETTINGS BT_OP(BT_OGF_LINK_POLICY, 0x000d)
```

<a id="a635b8ed8e93e89203b5ed16dbf5635d1"></a>

### `BT_HCI_OP_WRITE_LINK_SUPERVISION_TIMEOUT`

```c
#define BT_HCI_OP_WRITE_LINK_SUPERVISION_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0037) /* 0x0c37 */
```

HCI 写入链路监督超时（Write Link Supervision Timeout）操作码。

<a id="a9b328487dbeeaa587e6f75011441f340"></a>

### `BT_HCI_OP_WRITE_LOCAL_NAME`

```c
#define BT_HCI_OP_WRITE_LOCAL_NAME BT_OP(BT_OGF_BASEBAND, 0x0013) /* 0x0c13 */
```

<a id="a15a82766a1e11021d89a87e46fac6e91"></a>

### `BT_HCI_OP_WRITE_PAGE_SCAN_ACTIVITY`

```c
#define BT_HCI_OP_WRITE_PAGE_SCAN_ACTIVITY BT_OP(BT_OGF_BASEBAND, 0x001c) /* 0x0c1c */
```

HCI 写入寻呼扫描活动参数（Write Page Scan Activity）操作码。

<a id="a6b9898159d8f0259287704b2414b5511"></a>

### `BT_HCI_OP_WRITE_PAGE_SCAN_TYPE`

```c
#define BT_HCI_OP_WRITE_PAGE_SCAN_TYPE BT_OP(BT_OGF_BASEBAND, 0x0047) /* 0x0c47 */
```

HCI 写入寻呼扫描类型（Write Page Scan Type）操作码。

<a id="a5ef44fe1cca74a2258ffab1edd04acdf"></a>

### `BT_HCI_OP_WRITE_PAGE_TIMEOUT`

```c
#define BT_HCI_OP_WRITE_PAGE_TIMEOUT BT_OP(BT_OGF_BASEBAND, 0x0018) /* 0x0c18 */
```

<a id="a0480dd89b0f851d0a791b97138b01a5b"></a>

### `BT_HCI_OP_WRITE_SC_HOST_SUPP`

```c
#define BT_HCI_OP_WRITE_SC_HOST_SUPP BT_OP(BT_OGF_BASEBAND, 0x007a) /* 0x0c7a */
```

<a id="a0c8b9dc68ec6cd91ec0e9e565701a887"></a>

### `BT_HCI_OP_WRITE_SCAN_ENABLE`

```c
#define BT_HCI_OP_WRITE_SCAN_ENABLE BT_OP(BT_OGF_BASEBAND, 0x001a) /* 0x0c1a */
```

<a id="ac7a73c5e38a2308d56f0dbaaf0a4795b"></a>

### `BT_HCI_OP_WRITE_SSP_MODE`

```c
#define BT_HCI_OP_WRITE_SSP_MODE BT_OP(BT_OGF_BASEBAND, 0x0056) /* 0x0c56 */
```

<a id="a1109fda761e1ef8c6df935cf97fdc646"></a>

### `BT_HCI_OWN_ADDR_PUBLIC`

```c
#define BT_HCI_OWN_ADDR_PUBLIC 0x00
```

<a id="a8693ea59b948960e627d62785515996e"></a>

### `BT_HCI_OWN_ADDR_RANDOM`

```c
#define BT_HCI_OWN_ADDR_RANDOM 0x01
```

<a id="a115907057c92a59a407d261133946b59"></a>

### `BT_HCI_OWN_ADDR_RPA_MASK`

```c
#define BT_HCI_OWN_ADDR_RPA_MASK 0x02
```

<a id="a92a5db1ce46bbf3ddeaab4da76bc6685"></a>

### `BT_HCI_OWN_ADDR_RPA_OR_PUBLIC`

```c
#define BT_HCI_OWN_ADDR_RPA_OR_PUBLIC 0x02
```

<a id="aec05e679e29fde812e9a066e672405b4"></a>

### `BT_HCI_OWN_ADDR_RPA_OR_RANDOM`

```c
#define BT_HCI_OWN_ADDR_RPA_OR_RANDOM 0x03
```

<a id="a98554ced76600577254b4124b27ef8a8"></a>

### `BT_HCI_PAWR_SUBEVENT_MAX`

```c
#define BT_HCI_PAWR_SUBEVENT_MAX 128
```

<a id="a1e6d78149d0990511b2b6dffb617069e"></a>

### `BT_HCI_PEER_ADDR_ANONYMOUS`

```c
#define BT_HCI_PEER_ADDR_ANONYMOUS 0xff
```

<a id="aebc5bd975899f765afe697ab322db114"></a>

### `BT_HCI_PEER_ADDR_RPA_UNRESOLVED`

```c
#define BT_HCI_PEER_ADDR_RPA_UNRESOLVED 0xfe
```

<a id="a0a41f911f5f4b50b571c7f091393c7d8"></a>

### `BT_HCI_REQUEST_CTE_INTERVAL_MAX`

```c
#define BT_HCI_REQUEST_CTE_INTERVAL_MAX 0xFFFF
```

<a id="a13875ad8ac3a77759afdb4b6a76ad3e8"></a>

### `BT_HCI_REQUEST_CTE_INTERVAL_MIN`

```c
#define BT_HCI_REQUEST_CTE_INTERVAL_MIN 0x1
```

<a id="ad9e1fa26a799b8730c17772482da7982"></a>

### `BT_HCI_REQUEST_CTE_ONCE`

```c
#define BT_HCI_REQUEST_CTE_ONCE 0x0
```

<a id="a150ea8f2095d8510bde3ebd65d521c29"></a>

### `BT_HCI_ROLE_CENTRAL`

```c
#define BT_HCI_ROLE_CENTRAL 0x00
```

<a id="a9ca37afd4638ef94cdd55302bd4c99b3"></a>

### `BT_HCI_ROLE_PERIPHERAL`

```c
#define BT_HCI_ROLE_PERIPHERAL 0x01
```

<a id="a5e79467b20a9173726c6be86b091e596"></a>

### `BT_HCI_SCO`

```c
#define BT_HCI_SCO 0x00
```

<a id="acb8daef29a7f5f2d11a169fd10ae0caa"></a>

### `BT_HCI_SCO_HDR_SIZE`

```c
#define BT_HCI_SCO_HDR_SIZE 3
```

<a id="a3efc934c628fb7712b8376d6754bee29"></a>

### `BT_HCI_SCO_MAX_LATENCY_DEFAULT`

```c
#define BT_HCI_SCO_MAX_LATENCY_DEFAULT 0xffff /* do not care about SCO link latency */
```

<a id="a55e5c34e5388ca27dc0780a1e9950e85"></a>

### `BT_HCI_SCO_RETRANS_EFFORT_DEFAULT`

```c
#define BT_HCI_SCO_RETRANS_EFFORT_DEFAULT 0xff /* do not care about SCO retransmission effort */
```

<a id="a4e4a6e6bb2dc713de8cb7c12139583ed"></a>

### `BT_HCI_SYNC_HANDLE_INVALID`

```c
#define BT_HCI_SYNC_HANDLE_INVALID 0xffff
```

<a id="a1fe8c26f174833a4dccbe192df2c6f7d"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_00000000`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_00000000 0x05
```

<a id="a13baca9e4517522c763c25882177a2a7"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_00001111`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_00001111 0x06
```

<a id="a8f660f979b14d91abd9423e718921ebb"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_01010101`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_01010101 0x07
```

<a id="aab044752b89bb4493a509580ae8eaf9b"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_10101010`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_10101010 0x02
```

<a id="a51d26730c8f4c3c8491b33483bdb9494"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_11110000`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_11110000 0x01
```

<a id="a5008205909cecc994b74c8a1cb1f92af"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_11111111`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_11111111 0x04
```

<a id="a0eb4fcbb3ab6c7d4e2ed87d61c5b30f1"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_PRBS15`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_PRBS15 0x03
```

<a id="aa9ce0f2db7b63303a9c61c37d052d7b7"></a>

### `BT_HCI_TEST_PKT_PAYLOAD_PRBS9`

```c
#define BT_HCI_TEST_PKT_PAYLOAD_PRBS9 0x00
```

<a id="a925dda1fdce843e0bbcdd4acff696440"></a>

### `BT_HCI_TX_TEST_POWER_MAX`

```c
#define BT_HCI_TX_TEST_POWER_MAX 0x14
```

<a id="a2e9caac5d12f8df1ce69a54f603500ee"></a>

### `BT_HCI_TX_TEST_POWER_MAX_SET`

```c
#define BT_HCI_TX_TEST_POWER_MAX_SET 0x7F
```

<a id="a034d4a4fd8f7d6d324efa820d0b627d1"></a>

### `BT_HCI_TX_TEST_POWER_MIN`

```c
#define BT_HCI_TX_TEST_POWER_MIN -0x7F
```

<a id="a5d0fc1dbb127ba0a383e4e56bb503334"></a>

### `BT_HCI_TX_TEST_POWER_MIN_SET`

```c
#define BT_HCI_TX_TEST_POWER_MIN_SET 0x7E
```

<a id="a4947ee8a84f7cd81e242ee812b5b8760"></a>

### `BT_HCI_VERSION_1_0B`

```c
#define BT_HCI_VERSION_1_0B 0
```

版本（Version）1.0b。

<a id="a0fac5f104d8ab1539e84a900aafa9e43"></a>

### `BT_HCI_VERSION_1_1`

```c
#define BT_HCI_VERSION_1_1 1
```

版本（Version）1.1。

<a id="afe6fd8249a97d3762fe454bfb7eab021"></a>

### `BT_HCI_VERSION_1_2`

```c
#define BT_HCI_VERSION_1_2 2
```

版本（Version）1.2。

<a id="afc0d24e2ba5e6b992aec81104cbf035e"></a>

### `BT_HCI_VERSION_2_0`

```c
#define BT_HCI_VERSION_2_0 3
```

版本（Version）2.0。

<a id="a98d73e8f548d5ae7eddff91a3e647aae"></a>

### `BT_HCI_VERSION_2_1`

```c
#define BT_HCI_VERSION_2_1 4
```

版本（Version）2.1。

<a id="acaf91cc6895552243c5b85c2fc007db5"></a>

### `BT_HCI_VERSION_3_0`

```c
#define BT_HCI_VERSION_3_0 5
```

版本（Version）3.0。

<a id="aeb77e725323c3f31c90482e676dad08a"></a>

### `BT_HCI_VERSION_4_0`

```c
#define BT_HCI_VERSION_4_0 6
```

版本（Version）4.0。

<a id="a08cca779ede398a551359efccdaf3090"></a>

### `BT_HCI_VERSION_4_1`

```c
#define BT_HCI_VERSION_4_1 7
```

版本（Version）4.1。

<a id="aa398d6e6fcca0b427a2ccd3a0a343835"></a>

### `BT_HCI_VERSION_4_2`

```c
#define BT_HCI_VERSION_4_2 8
```

版本（Version）4.2。

<a id="a9a203a5a633d28c644b30125d437701a"></a>

### `BT_HCI_VERSION_5_0`

```c
#define BT_HCI_VERSION_5_0 9
```

版本（Version）5.0。

<a id="acfa0dbddfde8ee82b114dd34ff75c5bc"></a>

### `BT_HCI_VERSION_5_1`

```c
#define BT_HCI_VERSION_5_1 10
```

版本（Version）5.1。

<a id="aa4828a916c53d97de0541992d0359c09"></a>

### `BT_HCI_VERSION_5_2`

```c
#define BT_HCI_VERSION_5_2 11
```

版本（Version）5.2。

<a id="a37b04f40e68e821a1aac3b785903b379"></a>

### `BT_HCI_VERSION_5_3`

```c
#define BT_HCI_VERSION_5_3 12
```

版本（Version）5.3。

<a id="ae8eadab2b7be415160f145bd63bae367"></a>

### `BT_HCI_VERSION_5_4`

```c
#define BT_HCI_VERSION_5_4 13
```

版本（Version）5.4。

<a id="a66f6fbbc23991a16aa8bcfa2998f025f"></a>

### `BT_HCI_VERSION_6_0`

```c
#define BT_HCI_VERSION_6_0 14
```

版本（Version）6.0。

<a id="a418b3f42ae31a5b4c92905602e54ac4b"></a>

### `BT_HCI_VERSION_6_1`

```c
#define BT_HCI_VERSION_6_1 15
```

版本（Version）6.1。

<a id="a440c203fc4aed922ef9e27ad90c8ad12"></a>

### `BT_HCI_VERSION_6_2`

```c
#define BT_HCI_VERSION_6_2 16
```

版本（Version）6.2。

<a id="ac458d1d93335e0c6562508ab9af48633"></a>

### `BT_HCI_VERSION_6_3`

```c
#define BT_HCI_VERSION_6_3 17
```

版本（Version）6.3。

<a id="aad8fe65b6ce750e45f25af92707f85a2"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ALAW`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ALAW 0x02
```

<a id="abf3f4da1f3de490c997e054bf29cc6e1"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_CVSD`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_CVSD 0x00
```

<a id="af82c969110f65ad886997bfae3adcf3c"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_GET`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_GET ( val)
```

展开值（Value）：

```c
FIELD_GET(BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK, val)
```

<a id="ab8d4ecdf12cf208bb39012b0aa6b2547"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK GENMASK(1, 0)
```

<a id="a6570f5c7ac9cca8c4e27c60244b8cc4d"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP ( val)
```

展开值（Value）：

```c
FIELD_PREP(BT_HCI_VOICE_SETTING_AIR_CODING_FMT_MASK, val)
```

<a id="ae52705d4968245a15c743afd15481702"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_TRANSPARENT`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_TRANSPARENT 0x03
```

<a id="acb33fc93ce1e276775d817972dabd2b1"></a>

### `BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ULAW`

```c
#define BT_HCI_VOICE_SETTING_AIR_CODING_FMT_ULAW 0x01
```

<a id="a08e71787dd6643257e66d34e4ba92b1f"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_ALAW`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_ALAW 0x02
```

<a id="ad347325197bc72cf76cb457d7877ba36"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_GET`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_GET ( val)
```

展开值（Value）：

```c
FIELD_GET(BT_HCI_VOICE_SETTING_CODING_FMT_MASK, val)
```

<a id="ac6a8b4ce3e8ab55739c23cabe10df711"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_LINEAR`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_LINEAR 0x00
```

<a id="a05dce15a404d08bb44ccc73616a90082"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_MASK`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_MASK GENMASK(9, 8)
```

<a id="ae44b949821dbed75ed1df869cfe5a8c2"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_PREP`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_PREP ( val)
```

展开值（Value）：

```c
FIELD_PREP(BT_HCI_VOICE_SETTING_CODING_FMT_MASK, val)
```

<a id="ab4b8b429d8b8c80b35bd0d8b7d9e03db"></a>

### `BT_HCI_VOICE_SETTING_CODING_FMT_ULAW`

```c
#define BT_HCI_VOICE_SETTING_CODING_FMT_ULAW 0x01
```

<a id="af3ed0f4545c38aa48860ae0eac682b40"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_1_COMPLEMENT`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_1_COMPLEMENT 0x00
```

<a id="a370732fa8f51c824c784b084645ce437"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_2_COMPLEMENT`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_2_COMPLEMENT 0x01
```

<a id="abb4e34a3fd47ea87c1c2ba6319fe7327"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_GET`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_GET ( val)
```

展开值（Value）：

```c
FIELD_GET(BT_HCI_VOICE_SETTING_DATA_FMT_MASK, val)
```

<a id="ac7fdeedc1f828f4add126a5f5b12c5d8"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_MASK`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_MASK GENMASK(7, 6)
```

<a id="a6f4d39439872aacfbed3deb5c80b3532"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_PREP`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_PREP ( val)
```

展开值（Value）：

```c
FIELD_PREP(BT_HCI_VOICE_SETTING_DATA_FMT_MASK, val)
```

<a id="a231c5dce10f275a96c5c5fd4afc13484"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_SIGNED`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_SIGNED 0x02
```

<a id="aadb335cd648a5e8942b4572e5623aec2"></a>

### `BT_HCI_VOICE_SETTING_DATA_FMT_UNSIGNED`

```c
#define BT_HCI_VOICE_SETTING_DATA_FMT_UNSIGNED 0x03
```

<a id="a69eba4973cb15e8b50bccb3f787a1b32"></a>

### `BT_HCI_VOICE_SETTING_PCM_BIT_POS_DEFAULT`

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_DEFAULT 0x00
```

<a id="a4f930e86dcbeb4065220b2079245b54f"></a>

### `BT_HCI_VOICE_SETTING_PCM_BIT_POS_GET`

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_GET ( val)
```

展开值（Value）：

```c
FIELD_GET(BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK, val)
```

<a id="a02fbd3478aad48191c1e68337070ff24"></a>

### `BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK`

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK GENMASK(2, 4)
```

<a id="aaa4ab55f0b2c5f7a1f23001d1b452e77"></a>

### `BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP`

```c
#define BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP ( val)
```

展开值（Value）：

```c
FIELD_PREP(BT_HCI_VOICE_SETTING_PCM_BIT_POS_MASK, val)
```

<a id="a1369b9fe7bc657f5a2aec967faad0808"></a>

### `BT_HCI_VOICE_SETTING_SAMPLE_SIZE_16_BITS`

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_16_BITS 0x01
```

<a id="ae0c3ab318909f00633efb3e6961ea663"></a>

### `BT_HCI_VOICE_SETTING_SAMPLE_SIZE_8_BITS`

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_8_BITS 0x00
```

<a id="a054d5329a1c54b197b7a1d72a38e3c7e"></a>

### `BT_HCI_VOICE_SETTING_SAMPLE_SIZE_GET`

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_GET ( val)
```

展开值（Value）：

```c
FIELD_GET(BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK, val)
```

<a id="a94baca9b3db3bff4abbbdddbbb571d0e"></a>

### `BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK`

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK GENMASK(5, 5)
```

<a id="a7a0c75e8086231c6a3af00b0171b2437"></a>

### `BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP`

```c
#define BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP ( val)
```

展开值（Value）：

```c
FIELD_PREP(BT_HCI_VOICE_SETTING_SAMPLE_SIZE_MASK, val)
```

<a id="ad3e5599b38db2c67e4b79396a29aa01f"></a>

### `BT_HCI_VOICE_SETTINGS`

```c
#define BT_HCI_VOICE_SETTINGS ( air_coding_fmt, pcm_bit_pos, sample_size, data_fmt, coding_fmt )
```

展开值（Value）：

```c
(BT_HCI_VOICE_SETTING_AIR_CODING_FMT_PREP(air_coding_fmt) | \
 BT_HCI_VOICE_SETTING_PCM_BIT_POS_PREP(pcm_bit_pos) | \
 BT_HCI_VOICE_SETTING_SAMPLE_SIZE_PREP(sample_size) | \
 BT_HCI_VOICE_SETTING_DATA_FMT_PREP(data_fmt) | \
 BT_HCI_VOICE_SETTING_CODING_FMT_PREP(coding_fmt))
```

<a id="ac2ec12929f29264e2831c7ef986d163e"></a>

### `BT_HOLD_MODE`

```c
#define BT_HOLD_MODE 0x01
```

<a id="ac656a702e4193044a59cac517099e2cf"></a>

### `BT_IO_DISPLAY_ONLY`

```c
#define BT_IO_DISPLAY_ONLY 0x00
```

<a id="a701d4fa8a4ebc07647f70264ad36153e"></a>

### `BT_IO_DISPLAY_YESNO`

```c
#define BT_IO_DISPLAY_YESNO 0x01
```

<a id="a5a2a51ccedf3041c42ecdbd69e8c4a68"></a>

### `BT_IO_KEYBOARD_ONLY`

```c
#define BT_IO_KEYBOARD_ONLY 0x02
```

<a id="ad68c0057160d5dacae12fce949fdaa32"></a>

### `BT_IO_NO_INPUT_OUTPUT`

```c
#define BT_IO_NO_INPUT_OUTPUT 0x03
```

<a id="a06c43e91abee990343ece9c22f5a515e"></a>

### `BT_ISO_CONT`

```c
#define BT_ISO_CONT 0x01
```

<a id="a7149213544fe2ac9e7d3d0fd64ecb271"></a>

### `BT_ISO_DATA_INVALID`

```c
#define BT_ISO_DATA_INVALID 0x01
```

<a id="ae736b21ff7b99c4bb85df1a3f4bee9cd"></a>

### `BT_ISO_DATA_NOP`

```c
#define BT_ISO_DATA_NOP 0x02
```

<a id="a52091a307cca85d8d39fbfe5be6b6179"></a>

### `BT_ISO_DATA_VALID`

```c
#define BT_ISO_DATA_VALID 0x00
```

<a id="ac2da3db69ba73112fff5bf16ef386cb3"></a>

### `BT_ISO_END`

```c
#define BT_ISO_END 0x03
```

<a id="a54e2f7efc0f22287d65bdd560dd7ec78"></a>

### `bt_iso_flags`

```c
#define bt_iso_flags ( h)
```

展开值（Value）：

```c
((h) >> 12)
```

<a id="a7ea328491745f1bde6e2b376c19cc380"></a>

### `bt_iso_flags_pb`

```c
#define bt_iso_flags_pb ( f)
```

展开值（Value）：

```c
((f) & 0x0003)
```

<a id="aed6d45daf19ce7fadc1c8fbcc79c9e8a"></a>

### `bt_iso_flags_ts`

```c
#define bt_iso_flags_ts ( f)
```

展开值（Value）：

```c
(((f) >> 2) & 0x0001)
```

<a id="adcdb9dd367b64a820a040724c1c42c15"></a>

### `bt_iso_handle`

```c
#define bt_iso_handle ( h)
```

展开值（Value）：

```c
((h) & 0x0fff)
```

<a id="ab96b2d1b49a86ee96b2254b624b2e93f"></a>

### `bt_iso_handle_pack`

```c
#define bt_iso_handle_pack ( h, pb, ts )
```

展开值（Value）：

```c
((h) | (bt_iso_pack_flags(pb, ts) << 12))
```

<a id="a128d269790ccf3f8dcdeb51f80697ba0"></a>

### `bt_iso_hdr_len`

```c
#define bt_iso_hdr_len ( h)
```

展开值（Value）：

```c
((h) & BIT_MASK(14))
```

<a id="a9bdbdc6e181731a58ec91d53cdade532"></a>

### `bt_iso_pack_flags`

```c
#define bt_iso_pack_flags ( pb, ts )
```

展开值（Value）：

```c
(((pb) & 0x0003) | (((ts) & 0x0001) << 2))
```

<a id="a6dbade5730a92ea7f85017792939e941"></a>

### `bt_iso_pkt_flags`

```c
#define bt_iso_pkt_flags ( h)
```

展开值（Value）：

```c
((h) >> 14)
```

<a id="a0d540918a423992f5f244febcc82248a"></a>

### `bt_iso_pkt_len`

```c
#define bt_iso_pkt_len ( h)
```

展开值（Value）：

```c
((h) & BIT_MASK(12))
```

<a id="a3683be1ceedbcb97f61483b6fa4344e6"></a>

### `bt_iso_pkt_len_pack`

```c
#define bt_iso_pkt_len_pack ( h, f )
```

展开值（Value）：

```c
(((h) & BIT_MASK(12)) | ((f) << 14))
```

<a id="a1db9801de1c97b2d15cf9d2f0ec2a5f0"></a>

### `BT_ISO_SINGLE`

```c
#define BT_ISO_SINGLE 0x02
```

<a id="a9ef86241b4dfb462ec31c855bce4ee28"></a>

### `BT_ISO_START`

```c
#define BT_ISO_START 0x00
```

<a id="af96bfa8c912e66233f64b7cc1844b82e"></a>

### `BT_LE_ADV_CHAN_MAP_ALL`

```c
#define BT_LE_ADV_CHAN_MAP_ALL 0x07
```

<a id="af9652f7d96b61e7cc9f44f3d923bd962"></a>

### `BT_LE_ADV_CHAN_MAP_CHAN_37`

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_37 0x01
```

<a id="a07c18344ec56b22c8a3e902bc53ba191"></a>

### `BT_LE_ADV_CHAN_MAP_CHAN_38`

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_38 0x02
```

<a id="a14be9af8f16dcdf70aebf251bcfb52f3"></a>

### `BT_LE_ADV_CHAN_MAP_CHAN_39`

```c
#define BT_LE_ADV_CHAN_MAP_CHAN_39 0x04
```

<a id="a980ff7f9bf7154c7866b5e302a1f2a55"></a>

### `BT_LE_ADV_FP_FILTER_BOTH`

```c
#define BT_LE_ADV_FP_FILTER_BOTH 0x03
```

<a id="a5f3d27b78705afc3abff35e353eee9fa"></a>

### `BT_LE_ADV_FP_FILTER_CONN_IND`

```c
#define BT_LE_ADV_FP_FILTER_CONN_IND 0x02
```

<a id="aba027e2aeacea1040c3b45ccaeb23d3c"></a>

### `BT_LE_ADV_FP_FILTER_SCAN_REQ`

```c
#define BT_LE_ADV_FP_FILTER_SCAN_REQ 0x01
```

<a id="abc1615c8d22ab64844c3f3394023c1b4"></a>

### `BT_LE_ADV_FP_NO_FILTER`

```c
#define BT_LE_ADV_FP_NO_FILTER 0x00
```

<a id="a607201e55561cdccf34e18ceac0f23b7"></a>

### `BT_LE_ADV_INTERVAL_DEFAULT`

```c
#define BT_LE_ADV_INTERVAL_DEFAULT 0x0800
```

<a id="a6479fb2c964155cfcdd3cc48c3a45618"></a>

### `BT_LE_ADV_INTERVAL_MAX`

```c
#define BT_LE_ADV_INTERVAL_MAX 0x4000
```

<a id="ac89392b0484164812b77360d15d9984b"></a>

### `BT_LE_ADV_INTERVAL_MIN`

```c
#define BT_LE_ADV_INTERVAL_MIN 0x0020
```

<a id="a00b4acee1dd74405ef0a9dfcef4133f1"></a>

### `BT_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2_SUPPORTED`

```c
#define BT_LE_CS_READ_LOCAL_SUPPORTED_CAPABILITIES_V2_SUPPORTED ( cmd)
```

展开值（Value）：

```c
BT_CMD_TEST(cmd, 49, 2)
```

测试是否支持 LE Read Local Supported Capabilities v2 命令（读取本地支持能力，第 49 八位组的位 2）。

<a id="af698d1a0fa7a384e2fa1231edec00caa"></a>

### `BT_LE_EXT_ADV_INTERVAL_MAX`

```c
#define BT_LE_EXT_ADV_INTERVAL_MAX 0xFFFFFFU
```

最大低功耗蓝牙扩展广播间隔（LE Extended Advertising Interval）：`0xFFFFFF`，以 0.625 ms 为单位。

<a id="a4d920d42e8042c9117f97e334f889f51"></a>

### `BT_LE_FEAT_BIT_ADV_CODING_SEL`

```c
#define BT_LE_FEAT_BIT_ADV_CODING_SEL 40
```

<a id="ad711e7491883e1f1e068fe167cca8a4e"></a>

### `BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST`

```c
#define BT_LE_FEAT_BIT_ADV_CODING_SEL_HOST 41
```

<a id="a480fc67a1c8a2f36410f285ef0ee36e7"></a>

### `BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA`

```c
#define BT_LE_FEAT_BIT_ANT_SWITCH_RX_AOA 22
```

<a id="a41eae1585972ae6792eb1a639c2e3a8e"></a>

### `BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD`

```c
#define BT_LE_FEAT_BIT_ANT_SWITCH_TX_AOD 21
```

<a id="a9120867d6f31465cb5f085b610d5ed70"></a>

### `BT_LE_FEAT_BIT_CHAN_SEL_ALGO_2`

```c
#define BT_LE_FEAT_BIT_CHAN_SEL_ALGO_2 14
```

<a id="af2a4be520b4d8c3eb56231b865738e90"></a>

### `BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION`

```c
#define BT_LE_FEAT_BIT_CHANNEL_CLASSIFICATION 39
```

<a id="ab918084874aace22954aa748333baf6d"></a>

### `BT_LE_FEAT_BIT_CHANNEL_SOUNDING`

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING 46
```

<a id="aa4572a11d78651ce775a010178c6dfa2"></a>

### `BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST`

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_HOST 47
```

<a id="a705bd721edaa581f0046064ca39c2b69"></a>

### `BT_LE_FEAT_BIT_CHANNEL_SOUNDING_TONE_QUAL_IND`

```c
#define BT_LE_FEAT_BIT_CHANNEL_SOUNDING_TONE_QUAL_IND 48
```

<a id="aa98eed376b6d5263621f14c55d776088"></a>

### `BT_LE_FEAT_BIT_CIS_CENTRAL`

```c
#define BT_LE_FEAT_BIT_CIS_CENTRAL 28
```

<a id="a298fde96c2d6376e3333a99f7e03409d"></a>

### `BT_LE_FEAT_BIT_CIS_PERIPHERAL`

```c
#define BT_LE_FEAT_BIT_CIS_PERIPHERAL 29
```

<a id="aed34742e8554b830c3b6c4bf04f0e2db"></a>

### `BT_LE_FEAT_BIT_CONN_CTE_REQ`

```c
#define BT_LE_FEAT_BIT_CONN_CTE_REQ 17
```

<a id="aa5279a2ce26decb5856a6b709d0641c9"></a>

### `BT_LE_FEAT_BIT_CONN_CTE_RESP`

```c
#define BT_LE_FEAT_BIT_CONN_CTE_RESP 18
```

<a id="ab816048bdd6c1e42b0e458abebb76572"></a>

### `BT_LE_FEAT_BIT_CONN_PARAM_REQ`

```c
#define BT_LE_FEAT_BIT_CONN_PARAM_REQ 1
```

<a id="aa45b06a49232372891ceb5e4496d46da"></a>

### `BT_LE_FEAT_BIT_CONN_SUBRATING`

```c
#define BT_LE_FEAT_BIT_CONN_SUBRATING 37
```

<a id="adb884a30bc1a24e3dfb115cef7149c81"></a>

### `BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP`

```c
#define BT_LE_FEAT_BIT_CONN_SUBRATING_HOST_SUPP 38
```

<a id="a6abf01c846a5d637ca98997f6cfc263d"></a>

### `BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX`

```c
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_RX 20
```

<a id="a331e7697a3fdc073abba5dd0ff47346b"></a>

### `BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX`

```c
#define BT_LE_FEAT_BIT_CONNECTIONLESS_CTE_TX 19
```

<a id="a58d4aacb31998717b5943b7314622eb3"></a>

### `BT_LE_FEAT_BIT_DECISION_ADV_FILTER`

```c
#define BT_LE_FEAT_BIT_DECISION_ADV_FILTER 42
```

<a id="ac09127210b281e5ee45fbc134df64aa6"></a>

### `BT_LE_FEAT_BIT_DLE`

```c
#define BT_LE_FEAT_BIT_DLE 5
```

<a id="abd616dd5af5ed3742be9bae400ded848"></a>

### `BT_LE_FEAT_BIT_ENC`

```c
#define BT_LE_FEAT_BIT_ENC 0
```

<a id="ae1a0751e7c380117c4e31741712096a4"></a>

### `BT_LE_FEAT_BIT_EXT_ADV`

```c
#define BT_LE_FEAT_BIT_EXT_ADV 12
```

<a id="ae5644021aff31996c09f6edf3ede197c"></a>

### `BT_LE_FEAT_BIT_EXT_REJ_IND`

```c
#define BT_LE_FEAT_BIT_EXT_REJ_IND 2
```

<a id="a8f1fa8948f79bec50373e0342ab0969a"></a>

### `BT_LE_FEAT_BIT_EXT_SCAN`

```c
#define BT_LE_FEAT_BIT_EXT_SCAN 7
```

<a id="a51fc94e0f2ed1c6fe724c2846756cb31"></a>

### `BT_LE_FEAT_BIT_EXTENDED_FEAT_SET`

```c
#define BT_LE_FEAT_BIT_EXTENDED_FEAT_SET 63
```

<a id="a06c9aa4e8165cfe3e359283f199b450c"></a>

### `BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE`

```c
#define BT_LE_FEAT_BIT_FRAME_SPACE_UPDATE 65
```

<a id="af08a1ffd734d1c211f38d90b4fe72417"></a>

### `BT_LE_FEAT_BIT_ISO_BROADCASTER`

```c
#define BT_LE_FEAT_BIT_ISO_BROADCASTER 30
```

<a id="a0d80ccb33d263abd3b42de1b69cfeeeb"></a>

### `BT_LE_FEAT_BIT_ISO_CHANNELS`

```c
#define BT_LE_FEAT_BIT_ISO_CHANNELS 32
```

<a id="ac8cf36c670ae359ec24e62efb4505758"></a>

### `BT_LE_FEAT_BIT_MIN_USED_CHAN_PROC`

```c
#define BT_LE_FEAT_BIT_MIN_USED_CHAN_PROC 16
```

<a id="a28a862eaf11f8b45237f3b87e4bb15c7"></a>

### `BT_LE_FEAT_BIT_PAST_RECV`

```c
#define BT_LE_FEAT_BIT_PAST_RECV 25
```

<a id="aa05da01a6a9b9ac26423d6fc2661f3db"></a>

### `BT_LE_FEAT_BIT_PAST_SEND`

```c
#define BT_LE_FEAT_BIT_PAST_SEND 24
```

<a id="a434fb43b6b3176393f5d22d3932d69fa"></a>

### `BT_LE_FEAT_BIT_PATH_LOSS_MONITOR`

```c
#define BT_LE_FEAT_BIT_PATH_LOSS_MONITOR 35
```

<a id="af251cb9d905586fd53113f5920038dae"></a>

### `BT_LE_FEAT_BIT_PAWR_ADVERTISER`

```c
#define BT_LE_FEAT_BIT_PAWR_ADVERTISER 43
```

<a id="a00bb51972e0db07be84d4f3dfd007cea"></a>

### `BT_LE_FEAT_BIT_PAWR_SCANNER`

```c
#define BT_LE_FEAT_BIT_PAWR_SCANNER 44
```

<a id="a1ac5bab6d48775b4e63e249b5759a683"></a>

### `BT_LE_FEAT_BIT_PER_ADV`

```c
#define BT_LE_FEAT_BIT_PER_ADV 13
```

<a id="ad5a8221cb25d79b63f1a574699983038"></a>

### `BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP`

```c
#define BT_LE_FEAT_BIT_PER_ADV_ADI_SUPP 36
```

<a id="aeaea6ea6595de9e3283fd6063bf7c579"></a>

### `BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG`

```c
#define BT_LE_FEAT_BIT_PER_INIT_FEAT_XCHG 3
```

<a id="afcbc8d664c8e924b777c06ffb4c17315"></a>

### `BT_LE_FEAT_BIT_PHY_2M`

```c
#define BT_LE_FEAT_BIT_PHY_2M 8
```

<a id="a800686aa45cf336fbd6efc76b3752959"></a>

### `BT_LE_FEAT_BIT_PHY_CODED`

```c
#define BT_LE_FEAT_BIT_PHY_CODED 11
```

<a id="a9b4dc56ef4433b0c0dc74a3d95cf289e"></a>

### `BT_LE_FEAT_BIT_PING`

```c
#define BT_LE_FEAT_BIT_PING 4
```

<a id="a3c4196c04a73aa537baa845e061e9654"></a>

### `BT_LE_FEAT_BIT_PRIVACY`

```c
#define BT_LE_FEAT_BIT_PRIVACY 6
```

<a id="a0138172a0ed78244d8d3ac9d6936cf85"></a>

### `BT_LE_FEAT_BIT_PWR_CHG_IND`

```c
#define BT_LE_FEAT_BIT_PWR_CHG_IND 34
```

<a id="a938f823110f31a3a5d034cbe9b9d26eb"></a>

### `BT_LE_FEAT_BIT_PWR_CLASS_1`

```c
#define BT_LE_FEAT_BIT_PWR_CLASS_1 15
```

<a id="ae58f5260530d1b94608874f5d03d766d"></a>

### `BT_LE_FEAT_BIT_PWR_CTRL_REQ`

```c
#define BT_LE_FEAT_BIT_PWR_CTRL_REQ 33
```

<a id="a6d17dd4238ea471daca22f74e3cc3bcb"></a>

### `BT_LE_FEAT_BIT_REMOTE_PUB_KEY_VALIDATE`

```c
#define BT_LE_FEAT_BIT_REMOTE_PUB_KEY_VALIDATE 27
```

<a id="a9d9449f1935d6522291eca581f3fa9b0"></a>

### `BT_LE_FEAT_BIT_RX_CTE`

```c
#define BT_LE_FEAT_BIT_RX_CTE 23
```

<a id="a829e9d23a16912bad19448a6c4061e3b"></a>

### `BT_LE_FEAT_BIT_SCA_UPDATE`

```c
#define BT_LE_FEAT_BIT_SCA_UPDATE 26
```

<a id="ac00a188cc19a04ff9523fd3a4e044b17"></a>

### `BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS`

```c
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS 72
```

<a id="a670eda9a27a581646c5bc17fc452b466"></a>

### `BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP`

```c
#define BT_LE_FEAT_BIT_SHORTER_CONN_INTERVALS_HOST_SUPP 73
```

<a id="a9430a65ea813861b6890252ed4748f19"></a>

### `BT_LE_FEAT_BIT_SMI_RX`

```c
#define BT_LE_FEAT_BIT_SMI_RX 10
```

<a id="aea19f3c3cdcec054c81c176d5aa5f319"></a>

### `BT_LE_FEAT_BIT_SMI_TX`

```c
#define BT_LE_FEAT_BIT_SMI_TX 9
```

<a id="a2fed771f5611212e48027025e11f7678"></a>

### `BT_LE_FEAT_BIT_SYNC_RECEIVER`

```c
#define BT_LE_FEAT_BIT_SYNC_RECEIVER 31
```

<a id="ace0c3131b0a592ae60d8ef705ff54e7c"></a>

### `BT_LE_FEAT_BIT_UNSEG_FRAMED_MODE`

```c
#define BT_LE_FEAT_BIT_UNSEG_FRAMED_MODE 45
```

<a id="a6bf20989952fed3726bc45873beb896e"></a>

### `BT_LE_FEAT_TEST`

```c
#define BT_LE_FEAT_TEST ( feat, n )
```

展开值（Value）：

```c
(feat[(n) >> 3] & \
BIT((n) & 7))
```

<a id="abff5a0c6d1f3ab8ecf297d4ef29f7940"></a>

### `BT_LE_STATES_PER_CONN_ADV`

```c
#define BT_LE_STATES_PER_CONN_ADV ( states)
```

展开值（Value）：

```c
(states & BIT64_MASK(38))
```

<a id="a9871a7d021f9e0bcfda278c82c3731d7"></a>

### `BT_LE_STATES_SCAN_INIT`

```c
#define BT_LE_STATES_SCAN_INIT ( states)
```

展开值（Value）：

```c
0
```

<a id="a6630ceb874d343f721931f80ee5fa67e"></a>

### `BT_LK_AUTH_COMBINATION_P192`

```c
#define BT_LK_AUTH_COMBINATION_P192 0x05
```

<a id="aa941cce486c497afa6d03fec326396b9"></a>

### `BT_LK_AUTH_COMBINATION_P256`

```c
#define BT_LK_AUTH_COMBINATION_P256 0x08
```

<a id="a5753841a02ba0c2fa627d9e96bad045d"></a>

### `BT_LK_CHANGED_COMBINATION`

```c
#define BT_LK_CHANGED_COMBINATION 0x06
```

<a id="a7283a42b1220dd6d56c22cd9cb424e7c"></a>

### `BT_LK_COMBINATION`

```c
#define BT_LK_COMBINATION 0x00
```

<a id="a916e6133d2dadb9aaf5fe42d0c0e1b96"></a>

### `BT_LK_DEBUG_COMBINATION`

```c
#define BT_LK_DEBUG_COMBINATION 0x03
```

<a id="a12ffe67b9e4ec01bbe400a6a3cc5b859"></a>

### `BT_LK_LOCAL_UNIT`

```c
#define BT_LK_LOCAL_UNIT 0x01
```

<a id="aeb53b797c4fc91a38a459ff5f29d35e1"></a>

### `BT_LK_REMOTE_UNIT`

```c
#define BT_LK_REMOTE_UNIT 0x02
```

<a id="adfea495d48088eae78491a14730bef31"></a>

### `BT_LK_UNAUTH_COMBINATION_P192`

```c
#define BT_LK_UNAUTH_COMBINATION_P192 0x04
```

<a id="ada18ab581a323eafe8754009ef27d05e"></a>

### `BT_LK_UNAUTH_COMBINATION_P256`

```c
#define BT_LK_UNAUTH_COMBINATION_P256 0x07
```

<a id="a47ba0b282416c3e8f4275a38b7780b59"></a>

### `BT_MITM`

```c
#define BT_MITM 0x01
```

<a id="ac267cc5384724efba92df0be57379a89"></a>

### `BT_OCF`

```c
#define BT_OCF ( opcode)
```

展开值（Value）：

```c
((opcode) & BIT_MASK(10))
```

<a id="af3ae81176a4ace13a562262ad53aeae6"></a>

### `BT_OGF`

```c
#define BT_OGF ( opcode)
```

展开值（Value）：

```c
(((opcode) >> 10) & BIT_MASK(6))
```

<a id="a2ac75061b53ef7fe66c8fd1dc4ab8ef4"></a>

### `BT_OGF_BASEBAND`

```c
#define BT_OGF_BASEBAND 0x03
```

<a id="ac7c7348e291360169bf0ca5bb57b3d7e"></a>

### `BT_OGF_INFO`

```c
#define BT_OGF_INFO 0x04
```

<a id="abb09db6a211185842f039eddb9fadca5"></a>

### `BT_OGF_LE`

```c
#define BT_OGF_LE 0x08
```

<a id="abb6c50fe170ffaaaf4a0827058331381"></a>

### `BT_OGF_LINK_CTRL`

```c
#define BT_OGF_LINK_CTRL 0x01
```

<a id="a1ec081ffdef36e4a6b32beafc5bf5b34"></a>

### `BT_OGF_LINK_POLICY`

```c
#define BT_OGF_LINK_POLICY 0x02
```

<a id="a5ce14b9103bd538f3610afd80284157e"></a>

### `BT_OGF_STATUS`

```c
#define BT_OGF_STATUS 0x05
```

<a id="a6b682cb6e4f489ffb67b05280b3dbd65"></a>

### `BT_OGF_VS`

```c
#define BT_OGF_VS 0x3f
```

<a id="a7e006e0f69c498601f2c64a4ce3d8101"></a>

### `BT_OP`

```c
#define BT_OP ( ogf, ocf )
```

展开值（Value）：

```c
((ocf) | ((ogf) << 10))
```

<a id="a1bf4881fa3237f4a5b22e5fdb417762b"></a>

### `BT_OP_NOP`

```c
#define BT_OP_NOP 0x0000
```

<a id="a35831810e3a7e2c5446780b14ef7d9c1"></a>

### `BT_OVERFLOW_LINK_ACL`

```c
#define BT_OVERFLOW_LINK_ACL 0x01
```

<a id="ad32010743baef10c635d8b08f21c8641"></a>

### `BT_OVERFLOW_LINK_ISO`

```c
#define BT_OVERFLOW_LINK_ISO 0x02
```

<a id="a44233b934e33c65af90d03ad301e6b9d"></a>

### `BT_OVERFLOW_LINK_SYNCH`

```c
#define BT_OVERFLOW_LINK_SYNCH 0x00
```

<a id="a591f7071864e66aca2a3e85d63971be3"></a>

### `BT_READ_ALL_LOCAL_FEATURES_SUPPORTED`

```c
#define BT_READ_ALL_LOCAL_FEATURES_SUPPORTED ( supported_commands)
```

展开值（Value）：

```c
BT_CMD_TEST(supported_commands, 47, 2)
```

<a id="a52ac9ae0d0d89e5957e4bfd7dca93fe1"></a>

### `BT_SNIFF_MODE`

```c
#define BT_SNIFF_MODE 0x02
```

<a id="ac1ebc6168b2823aea2af2e2f89ffb6cd"></a>

### `BT_TX_POWER_LEVEL_CURRENT`

```c
#define BT_TX_POWER_LEVEL_CURRENT 0x00
```

<a id="ad835bc44abee2e174f86cd55ac0338e3"></a>

### `BT_TX_POWER_LEVEL_MAX`

```c
#define BT_TX_POWER_LEVEL_MAX 0x01
```

<a id="aa3a50b43beddbd76ae67b71e79a80175"></a>

### `EDR_ESCO_PKT_MASK`

```c
#define EDR_ESCO_PKT_MASK
```

展开值（Value）：

```c
(HCI_PKT_TYPE_ESCO_2EV3 | \
HCI_PKT_TYPE_ESCO_3EV3 | \
HCI_PKT_TYPE_ESCO_2EV5 | \
HCI_PKT_TYPE_ESCO_3EV5)
```

<a id="a8afe2c798b2d9657778f0815e3cb11c8"></a>

### `ESCO_PKT_MASK`

```c
#define ESCO_PKT_MASK
```

展开值（Value）：

```c
(HCI_PKT_TYPE_SCO_HV1 | \
HCI_PKT_TYPE_SCO_HV2 | \
HCI_PKT_TYPE_SCO_HV3 | \
HCI_PKT_TYPE_ESCO_EV3 | \
HCI_PKT_TYPE_ESCO_EV4 | \
HCI_PKT_TYPE_ESCO_EV5)
```

<a id="a1ccc4d6e5cfc560b7e2cb80c4c386607"></a>

### `HCI_PKT_TYPE_ESCO_2EV3`

```c
#define HCI_PKT_TYPE_ESCO_2EV3 0x0040
```

<a id="a1252be2692bcfb7a1256c63c4deed15d"></a>

### `HCI_PKT_TYPE_ESCO_2EV5`

```c
#define HCI_PKT_TYPE_ESCO_2EV5 0x0100
```

<a id="ac5f09e3db1bc4d697ff705802e9ec3a0"></a>

### `HCI_PKT_TYPE_ESCO_3EV3`

```c
#define HCI_PKT_TYPE_ESCO_3EV3 0x0080
```

<a id="aa45e51b1be89505fe599bc7983fcb950"></a>

### `HCI_PKT_TYPE_ESCO_3EV5`

```c
#define HCI_PKT_TYPE_ESCO_3EV5 0x0200
```

<a id="a9530e916a0cf905e2185cd021320bfff"></a>

### `HCI_PKT_TYPE_ESCO_EV3`

```c
#define HCI_PKT_TYPE_ESCO_EV3 0x0008
```

<a id="a3e0b6a1aa3818cb0c36f7883fd361c7e"></a>

### `HCI_PKT_TYPE_ESCO_EV4`

```c
#define HCI_PKT_TYPE_ESCO_EV4 0x0010
```

<a id="a1f7474cb16a495bd81dc1f23d4103f70"></a>

### `HCI_PKT_TYPE_ESCO_EV5`

```c
#define HCI_PKT_TYPE_ESCO_EV5 0x0020
```

<a id="aecb5b3886467c41baf979d01d8bde4a1"></a>

### `HCI_PKT_TYPE_HV1`

```c
#define HCI_PKT_TYPE_HV1 0x0020
```

<a id="ae68633ce74639ec6f06d5ef4feee2d09"></a>

### `HCI_PKT_TYPE_HV2`

```c
#define HCI_PKT_TYPE_HV2 0x0040
```

<a id="aecd04ca27f536a1cb15aacf9ee80aba8"></a>

### `HCI_PKT_TYPE_HV3`

```c
#define HCI_PKT_TYPE_HV3 0x0080
```

<a id="a4b048addd84409867177a97c785c4a73"></a>

### `HCI_PKT_TYPE_SCO_HV1`

```c
#define HCI_PKT_TYPE_SCO_HV1 0x0001
```

<a id="a98f8217b27c0b9b7817c86520da45018"></a>

### `HCI_PKT_TYPE_SCO_HV2`

```c
#define HCI_PKT_TYPE_SCO_HV2 0x0002
```

<a id="af67cdc23b6542e6d8323f14e17c7171d"></a>

### `HCI_PKT_TYPE_SCO_HV3`

```c
#define HCI_PKT_TYPE_SCO_HV3 0x0004
```

<a id="a1ef7929257a087f340f1f421cd8f51ce"></a>

### `SCO_PKT_MASK`

```c
#define SCO_PKT_MASK
```

展开值（Value）：

```c
(HCI_PKT_TYPE_SCO_HV1 | \
HCI_PKT_TYPE_SCO_HV2 | \
HCI_PKT_TYPE_SCO_HV3)
```


## 5.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/addr.h](../api_source_visible_fragment_reference/P001_addr.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [bt_hci_sco_hdr](../bluetooth_hci_model_reference/P436_bt_hci_sco_hdr_结构体.md)
- [bt_hci_evt_hdr](../bluetooth_hci_model_reference/P217_bt_hci_evt_hdr_结构体.md)
- [bt_hci_acl_hdr](../bluetooth_hci_model_reference/P001_bt_hci_acl_hdr_结构体.md)
- [bt_hci_iso_sdu_hdr](../bluetooth_hci_model_reference/P313_bt_hci_iso_sdu_hdr_结构体.md)
- [bt_hci_iso_sdu_ts_hdr](../bluetooth_hci_model_reference/P314_bt_hci_iso_sdu_ts_hdr_结构体.md)
- [bt_hci_iso_hdr](../bluetooth_hci_model_reference/P312_bt_hci_iso_hdr_结构体.md)
- [bt_hci_cmd_hdr](../bluetooth_hci_model_reference/P005_bt_hci_cmd_hdr_结构体.md)
- [bt_hci_op_inquiry](../bluetooth_hci_model_reference/P328_bt_hci_op_inquiry_结构体.md)
- [bt_hci_cp_connect](../bluetooth_hci_model_reference/P013_bt_hci_cp_connect_结构体.md)
- [bt_hci_cp_disconnect](../bluetooth_hci_model_reference/P015_bt_hci_cp_disconnect_结构体.md)
- [bt_hci_cp_connect_cancel](../bluetooth_hci_model_reference/P014_bt_hci_cp_connect_cancel_结构体.md)
- [bt_hci_rp_connect_cancel](../bluetooth_hci_model_reference/P335_bt_hci_rp_connect_cancel_结构体.md)
- [bt_hci_cp_accept_conn_req](../bluetooth_hci_model_reference/P007_bt_hci_cp_accept_conn_req_结构体.md)
- [bt_hci_cp_setup_sync_conn](../bluetooth_hci_model_reference/P168_bt_hci_cp_setup_sync_conn_结构体.md)
- [bt_hci_cp_accept_sync_conn_req](../bluetooth_hci_model_reference/P008_bt_hci_cp_accept_sync_conn_req_结构体.md)
- [bt_hci_cp_reject_conn_req](../bluetooth_hci_model_reference/P161_bt_hci_cp_reject_conn_req_结构体.md)
- [bt_hci_cp_link_key_reply](../bluetooth_hci_model_reference/P140_bt_hci_cp_link_key_reply_结构体.md)
- [bt_hci_cp_link_key_neg_reply](../bluetooth_hci_model_reference/P139_bt_hci_cp_link_key_neg_reply_结构体.md)
- [bt_hci_cp_pin_code_reply](../bluetooth_hci_model_reference/P148_bt_hci_cp_pin_code_reply_结构体.md)
- [bt_hci_rp_pin_code_reply](../bluetooth_hci_model_reference/P400_bt_hci_rp_pin_code_reply_结构体.md)
- [bt_hci_cp_pin_code_neg_reply](../bluetooth_hci_model_reference/P147_bt_hci_cp_pin_code_neg_reply_结构体.md)
- [bt_hci_rp_pin_code_neg_reply](../bluetooth_hci_model_reference/P399_bt_hci_rp_pin_code_neg_reply_结构体.md)
- [bt_hci_cp_change_conn_packet_type](../bluetooth_hci_model_reference/P010_bt_hci_cp_change_conn_packet_type_结构体.md)
- [bt_hci_cp_auth_requested](../bluetooth_hci_model_reference/P009_bt_hci_cp_auth_requested_结构体.md)
- [bt_hci_cp_set_conn_encrypt](../bluetooth_hci_model_reference/P164_bt_hci_cp_set_conn_encrypt_结构体.md)
- [bt_hci_cp_remote_name_request](../bluetooth_hci_model_reference/P163_bt_hci_cp_remote_name_request_结构体.md)
- [bt_hci_cp_remote_name_cancel](../bluetooth_hci_model_reference/P162_bt_hci_cp_remote_name_cancel_结构体.md)
- [bt_hci_rp_remote_name_cancel](../bluetooth_hci_model_reference/P420_bt_hci_rp_remote_name_cancel_结构体.md)
- [bt_hci_cp_read_remote_features](../bluetooth_hci_model_reference/P157_bt_hci_cp_read_remote_features_结构体.md)
- [bt_hci_cp_read_remote_ext_features](../bluetooth_hci_model_reference/P156_bt_hci_cp_read_remote_ext_features_结构体.md)
- [bt_hci_cp_read_remote_version_info](../bluetooth_hci_model_reference/P158_bt_hci_cp_read_remote_version_info_结构体.md)
- [bt_hci_cp_io_capability_reply](../bluetooth_hci_model_reference/P020_bt_hci_cp_io_capability_reply_结构体.md)
- [bt_hci_cp_user_confirm_reply](../bluetooth_hci_model_reference/P172_bt_hci_cp_user_confirm_reply_结构体.md)
- [bt_hci_rp_user_confirm_reply](../bluetooth_hci_model_reference/P422_bt_hci_rp_user_confirm_reply_结构体.md)
- [bt_hci_cp_user_passkey_reply](../bluetooth_hci_model_reference/P174_bt_hci_cp_user_passkey_reply_结构体.md)
- [bt_hci_cp_user_passkey_neg_reply](../bluetooth_hci_model_reference/P173_bt_hci_cp_user_passkey_neg_reply_结构体.md)
- [bt_hci_cp_io_capability_neg_reply](../bluetooth_hci_model_reference/P019_bt_hci_cp_io_capability_neg_reply_结构体.md)
- [bt_hci_cp_switch_role](../bluetooth_hci_model_reference/P171_bt_hci_cp_switch_role_结构体.md)
- [bt_hci_cp_read_link_policy_settings](../bluetooth_hci_model_reference/P153_bt_hci_cp_read_link_policy_settings_结构体.md)
- [bt_hci_rp_read_link_policy_settings](../bluetooth_hci_model_reference/P412_bt_hci_rp_read_link_policy_settings_结构体.md)
- [bt_hci_cp_write_link_policy_settings](../bluetooth_hci_model_reference/P194_bt_hci_cp_write_link_policy_settings_结构体.md)
- [bt_hci_rp_read_default_link_policy_settings](../bluetooth_hci_model_reference/P410_bt_hci_rp_read_default_link_policy_settings_结构体.md)
- [bt_hci_cp_write_default_link_policy_settings](../bluetooth_hci_model_reference/P188_bt_hci_cp_write_default_link_policy_settings_结构体.md)
- [bt_hci_cp_sniff_mode](../bluetooth_hci_model_reference/P169_bt_hci_cp_sniff_mode_结构体.md)
- [bt_hci_cp_exit_sniff_mode](../bluetooth_hci_model_reference/P016_bt_hci_cp_exit_sniff_mode_结构体.md)
- [bt_hci_cp_sniff_subrating](../bluetooth_hci_model_reference/P170_bt_hci_cp_sniff_subrating_结构体.md)
- [bt_hci_rp_sniff_subrating](../bluetooth_hci_model_reference/P421_bt_hci_rp_sniff_subrating_结构体.md)
- [bt_hci_cp_set_event_mask](../bluetooth_hci_model_reference/P166_bt_hci_cp_set_event_mask_结构体.md)
- [bt_hci_write_local_name](../bluetooth_hci_model_reference/P450_bt_hci_write_local_name_结构体.md)
- [bt_hci_rp_read_conn_accept_timeout](../bluetooth_hci_model_reference/P408_bt_hci_rp_read_conn_accept_timeout_结构体.md)
- [bt_hci_cp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P186_bt_hci_cp_write_conn_accept_timeout_结构体.md)
- [bt_hci_rp_write_conn_accept_timeout](../bluetooth_hci_model_reference/P435_bt_hci_rp_write_conn_accept_timeout_结构体.md)
- [bt_hci_cp_write_page_scan_activity](../bluetooth_hci_model_reference/P196_bt_hci_cp_write_page_scan_activity_结构体.md)
- [bt_hci_cp_write_inquiry_scan_activity](../bluetooth_hci_model_reference/P191_bt_hci_cp_write_inquiry_scan_activity_结构体.md)
- [bt_hci_rp_read_class_of_device](../bluetooth_hci_model_reference/P404_bt_hci_rp_read_class_of_device_结构体.md)
- [bt_hci_cp_write_class_of_device](../bluetooth_hci_model_reference/P185_bt_hci_cp_write_class_of_device_结构体.md)
- [bt_hci_cp_read_tx_power_level](../bluetooth_hci_model_reference/P160_bt_hci_cp_read_tx_power_level_结构体.md)
- [bt_hci_rp_read_tx_power_level](../bluetooth_hci_model_reference/P419_bt_hci_rp_read_tx_power_level_结构体.md)
- [bt_hci_cp_le_read_tx_power_level](../bluetooth_hci_model_reference/P069_bt_hci_cp_le_read_tx_power_level_结构体.md)
- [bt_hci_rp_le_read_tx_power_level](../bluetooth_hci_model_reference/P377_bt_hci_rp_le_read_tx_power_level_结构体.md)
- [bt_hci_cp_le_set_tx_power_report_enable](../bluetooth_hci_model_reference/P125_bt_hci_cp_le_set_tx_power_report_enable_结构体.md)
- [bt_hci_cp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P107_bt_hci_cp_le_set_path_loss_reporting_parameters_结构体.md)
- [bt_hci_rp_le_set_path_loss_reporting_parameters](../bluetooth_hci_model_reference/P390_bt_hci_rp_le_set_path_loss_reporting_parameters_结构体.md)
- [bt_hci_cp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P106_bt_hci_cp_le_set_path_loss_reporting_enable_结构体.md)
- [bt_hci_rp_le_set_path_loss_reporting_enable](../bluetooth_hci_model_reference/P389_bt_hci_rp_le_set_path_loss_reporting_enable_结构体.md)
- [bt_hci_cp_le_set_default_subrate](../bluetooth_hci_model_reference/P095_bt_hci_cp_le_set_default_subrate_结构体.md)
- [bt_hci_cp_le_subrate_request](../bluetooth_hci_model_reference/P128_bt_hci_cp_le_subrate_request_结构体.md)
- [bt_hci_cp_set_ctl_to_host_flow](../bluetooth_hci_model_reference/P165_bt_hci_cp_set_ctl_to_host_flow_结构体.md)
- [bt_hci_cp_host_buffer_size](../bluetooth_hci_model_reference/P017_bt_hci_cp_host_buffer_size_结构体.md)
- [bt_hci_handle_count](../bluetooth_hci_model_reference/P310_bt_hci_handle_count_结构体.md)
- [bt_hci_cp_host_num_completed_packets](../bluetooth_hci_model_reference/P018_bt_hci_cp_host_num_completed_packets_结构体.md)
- [bt_hci_cp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P154_bt_hci_cp_read_link_supervision_timeout_结构体.md)
- [bt_hci_rp_read_link_supervision_timeout](../bluetooth_hci_model_reference/P413_bt_hci_rp_read_link_supervision_timeout_结构体.md)
- [bt_hci_cp_write_link_supervision_timeout](../bluetooth_hci_model_reference/P195_bt_hci_cp_write_link_supervision_timeout_结构体.md)
- [bt_hci_iac_lap](../bluetooth_hci_model_reference/P311_bt_hci_iac_lap_结构体.md)
- [bt_hci_cp_write_current_iac_lap](../bluetooth_hci_model_reference/P187_bt_hci_cp_write_current_iac_lap_结构体.md)
- [bt_hci_cp_write_inquiry_scan_type](../bluetooth_hci_model_reference/P192_bt_hci_cp_write_inquiry_scan_type_结构体.md)
- [bt_hci_cp_write_inquiry_mode](../bluetooth_hci_model_reference/P190_bt_hci_cp_write_inquiry_mode_结构体.md)
- [bt_hci_cp_write_page_scan_type](../bluetooth_hci_model_reference/P197_bt_hci_cp_write_page_scan_type_结构体.md)
- [bt_hci_cp_write_ext_inquiry_response](../bluetooth_hci_model_reference/P189_bt_hci_cp_write_ext_inquiry_response_结构体.md)
- [bt_hci_cp_write_ssp_mode](../bluetooth_hci_model_reference/P199_bt_hci_cp_write_ssp_mode_结构体.md)
- [bt_hci_cp_set_event_mask_page_2](../bluetooth_hci_model_reference/P167_bt_hci_cp_set_event_mask_page_2_结构体.md)
- [bt_hci_cp_write_le_host_supp](../bluetooth_hci_model_reference/P193_bt_hci_cp_write_le_host_supp_结构体.md)
- [bt_hci_cp_write_sc_host_supp](../bluetooth_hci_model_reference/P198_bt_hci_cp_write_sc_host_supp_结构体.md)
- [bt_hci_cp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P149_bt_hci_cp_read_auth_payload_timeout_结构体.md)
- [bt_hci_rp_read_auth_payload_timeout](../bluetooth_hci_model_reference/P401_bt_hci_rp_read_auth_payload_timeout_结构体.md)
- [bt_hci_cp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P184_bt_hci_cp_write_auth_payload_timeout_结构体.md)
- [bt_hci_rp_write_auth_payload_timeout](../bluetooth_hci_model_reference/P434_bt_hci_rp_write_auth_payload_timeout_结构体.md)
- [bt_hci_cp_configure_data_path](../bluetooth_hci_model_reference/P012_bt_hci_cp_configure_data_path_结构体.md)
- [bt_hci_rp_configure_data_path](../bluetooth_hci_model_reference/P334_bt_hci_rp_configure_data_path_结构体.md)
- [bt_hci_rp_read_local_version_info](../bluetooth_hci_model_reference/P416_bt_hci_rp_read_local_version_info_结构体.md)
- [bt_hci_rp_read_supported_commands](../bluetooth_hci_model_reference/P418_bt_hci_rp_read_supported_commands_结构体.md)
- [bt_hci_cp_read_local_ext_features](../bluetooth_hci_model_reference/P155_bt_hci_cp_read_local_ext_features_结构体.md)
- [bt_hci_rp_read_local_ext_features](../bluetooth_hci_model_reference/P414_bt_hci_rp_read_local_ext_features_结构体.md)
- [bt_hci_rp_read_local_features](../bluetooth_hci_model_reference/P415_bt_hci_rp_read_local_features_结构体.md)
- [bt_hci_rp_read_buffer_size](../bluetooth_hci_model_reference/P403_bt_hci_rp_read_buffer_size_结构体.md)
- [bt_hci_rp_read_bd_addr](../bluetooth_hci_model_reference/P402_bt_hci_rp_read_bd_addr_结构体.md)
- [bt_hci_std_codec_info](../bluetooth_hci_model_reference/P438_bt_hci_std_codec_info_结构体.md)
- [bt_hci_std_codecs](../bluetooth_hci_model_reference/P440_bt_hci_std_codecs_结构体.md)
- [bt_hci_vs_codec_info](../bluetooth_hci_model_reference/P443_bt_hci_vs_codec_info_结构体.md)
- [bt_hci_vs_codecs](../bluetooth_hci_model_reference/P445_bt_hci_vs_codecs_结构体.md)
- [bt_hci_rp_read_codecs](../bluetooth_hci_model_reference/P406_bt_hci_rp_read_codecs_结构体.md)
- [bt_hci_std_codec_info_v2](../bluetooth_hci_model_reference/P439_bt_hci_std_codec_info_v2_结构体.md)
- [bt_hci_std_codecs_v2](../bluetooth_hci_model_reference/P441_bt_hci_std_codecs_v2_结构体.md)
- [bt_hci_vs_codec_info_v2](../bluetooth_hci_model_reference/P444_bt_hci_vs_codec_info_v2_结构体.md)
- [bt_hci_vs_codecs_v2](../bluetooth_hci_model_reference/P446_bt_hci_vs_codecs_v2_结构体.md)
- [bt_hci_rp_read_codecs_v2](../bluetooth_hci_model_reference/P407_bt_hci_rp_read_codecs_v2_结构体.md)
- [bt_hci_cp_codec_id](../bluetooth_hci_model_reference/P011_bt_hci_cp_codec_id_结构体.md)
- [bt_hci_cp_read_codec_capabilities](../bluetooth_hci_model_reference/P150_bt_hci_cp_read_codec_capabilities_结构体.md)
- [bt_hci_codec_capability_info](../bluetooth_hci_model_reference/P006_bt_hci_codec_capability_info_结构体.md)
- [bt_hci_rp_read_codec_capabilities](../bluetooth_hci_model_reference/P405_bt_hci_rp_read_codec_capabilities_结构体.md)
- [bt_hci_cp_read_ctlr_delay](../bluetooth_hci_model_reference/P151_bt_hci_cp_read_ctlr_delay_结构体.md)
- [bt_hci_rp_read_ctlr_delay](../bluetooth_hci_model_reference/P409_bt_hci_rp_read_ctlr_delay_结构体.md)
- [bt_hci_cp_read_rssi](../bluetooth_hci_model_reference/P159_bt_hci_cp_read_rssi_结构体.md)
- [bt_hci_rp_read_rssi](../bluetooth_hci_model_reference/P417_bt_hci_rp_read_rssi_结构体.md)
- [bt_hci_cp_read_encryption_key_size](../bluetooth_hci_model_reference/P152_bt_hci_cp_read_encryption_key_size_结构体.md)
- [bt_hci_rp_read_encryption_key_size](../bluetooth_hci_model_reference/P411_bt_hci_rp_read_encryption_key_size_结构体.md)
- [bt_hci_cp_le_set_event_mask](../bluetooth_hci_model_reference/P096_bt_hci_cp_le_set_event_mask_结构体.md)
- [bt_hci_rp_le_read_buffer_size](../bluetooth_hci_model_reference/P354_bt_hci_rp_le_read_buffer_size_结构体.md)
- [bt_hci_rp_le_read_local_features](../bluetooth_hci_model_reference/P362_bt_hci_rp_le_read_local_features_结构体.md)
- [bt_hci_cp_le_set_random_address](../bluetooth_hci_model_reference/P120_bt_hci_cp_le_set_random_address_结构体.md)
- [bt_hci_cp_le_set_adv_param](../bluetooth_hci_model_reference/P084_bt_hci_cp_le_set_adv_param_结构体.md)
- [bt_hci_rp_le_read_chan_tx_power](../bluetooth_hci_model_reference/P357_bt_hci_rp_le_read_chan_tx_power_结构体.md)
- [bt_hci_cp_le_set_adv_data](../bluetooth_hci_model_reference/P082_bt_hci_cp_le_set_adv_data_结构体.md)
- [bt_hci_cp_le_set_scan_rsp_data](../bluetooth_hci_model_reference/P124_bt_hci_cp_le_set_scan_rsp_data_结构体.md)
- [bt_hci_cp_le_set_adv_enable](../bluetooth_hci_model_reference/P083_bt_hci_cp_le_set_adv_enable_结构体.md)
- [bt_hci_cp_le_set_scan_param](../bluetooth_hci_model_reference/P123_bt_hci_cp_le_set_scan_param_结构体.md)
- [bt_hci_cp_le_set_scan_enable](../bluetooth_hci_model_reference/P122_bt_hci_cp_le_set_scan_enable_结构体.md)
- [bt_hci_cp_le_create_conn](../bluetooth_hci_model_reference/P034_bt_hci_cp_le_create_conn_结构体.md)
- [bt_hci_rp_le_read_fal_size](../bluetooth_hci_model_reference/P359_bt_hci_rp_le_read_fal_size_结构体.md)
- [bt_hci_cp_le_add_dev_to_fal](../bluetooth_hci_model_reference/P022_bt_hci_cp_le_add_dev_to_fal_结构体.md)
- [bt_hci_cp_le_rem_dev_from_fal](../bluetooth_hci_model_reference/P071_bt_hci_cp_le_rem_dev_from_fal_结构体.md)
- [hci_cp_le_conn_update](../network_service_model_reference/P022_hci_cp_le_conn_update_结构体.md)
- [bt_hci_cp_le_set_host_chan_classif](../bluetooth_hci_model_reference/P104_bt_hci_cp_le_set_host_chan_classif_结构体.md)
- [bt_hci_cp_le_read_chan_map](../bluetooth_hci_model_reference/P059_bt_hci_cp_le_read_chan_map_结构体.md)
- [bt_hci_rp_le_read_chan_map](../bluetooth_hci_model_reference/P356_bt_hci_rp_le_read_chan_map_结构体.md)
- [bt_hci_cp_le_read_remote_features](../bluetooth_hci_model_reference/P066_bt_hci_cp_le_read_remote_features_结构体.md)
- [bt_hci_cp_le_encrypt](../bluetooth_hci_model_reference/P039_bt_hci_cp_le_encrypt_结构体.md)
- [bt_hci_rp_le_encrypt](../bluetooth_hci_model_reference/P342_bt_hci_rp_le_encrypt_结构体.md)
- [bt_hci_rp_le_rand](../bluetooth_hci_model_reference/P351_bt_hci_rp_le_rand_结构体.md)
- [bt_hci_cp_le_start_encryption](../bluetooth_hci_model_reference/P127_bt_hci_cp_le_start_encryption_结构体.md)
- [bt_hci_cp_le_ltk_req_reply](../bluetooth_hci_model_reference/P051_bt_hci_cp_le_ltk_req_reply_结构体.md)
- [bt_hci_rp_le_ltk_req_reply](../bluetooth_hci_model_reference/P347_bt_hci_rp_le_ltk_req_reply_结构体.md)
- [bt_hci_cp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P050_bt_hci_cp_le_ltk_req_neg_reply_结构体.md)
- [bt_hci_rp_le_ltk_req_neg_reply](../bluetooth_hci_model_reference/P346_bt_hci_rp_le_ltk_req_neg_reply_结构体.md)
- [bt_hci_rp_le_read_supp_states](../bluetooth_hci_model_reference/P374_bt_hci_rp_le_read_supp_states_结构体.md)
- [bt_hci_cp_le_rx_test](../bluetooth_hci_model_reference/P078_bt_hci_cp_le_rx_test_结构体.md)
- [bt_hci_cp_le_tx_test](../bluetooth_hci_model_reference/P130_bt_hci_cp_le_tx_test_结构体.md)
- [bt_hci_rp_le_test_end](../bluetooth_hci_model_reference/P392_bt_hci_rp_le_test_end_结构体.md)
- [bt_hci_cp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P030_bt_hci_cp_le_conn_param_req_reply_结构体.md)
- [bt_hci_rp_le_conn_param_req_reply](../bluetooth_hci_model_reference/P340_bt_hci_rp_le_conn_param_req_reply_结构体.md)
- [bt_hci_cp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P029_bt_hci_cp_le_conn_param_req_neg_reply_结构体.md)
- [bt_hci_rp_le_conn_param_req_neg_reply](../bluetooth_hci_model_reference/P339_bt_hci_rp_le_conn_param_req_neg_reply_结构体.md)
- [bt_hci_cp_le_set_data_len](../bluetooth_hci_model_reference/P093_bt_hci_cp_le_set_data_len_结构体.md)
- [bt_hci_rp_le_set_data_len](../bluetooth_hci_model_reference/P386_bt_hci_rp_le_set_data_len_结构体.md)
- [bt_hci_rp_le_read_default_data_len](../bluetooth_hci_model_reference/P358_bt_hci_rp_le_read_default_data_len_结构体.md)
- [bt_hci_cp_le_write_default_data_len](../bluetooth_hci_model_reference/P137_bt_hci_cp_le_write_default_data_len_结构体.md)
- [bt_hci_cp_le_generate_dhkey](../bluetooth_hci_model_reference/P045_bt_hci_cp_le_generate_dhkey_结构体.md)
- [bt_hci_cp_le_generate_dhkey_v2](../bluetooth_hci_model_reference/P046_bt_hci_cp_le_generate_dhkey_v2_结构体.md)
- [bt_hci_cp_le_add_dev_to_rl](../bluetooth_hci_model_reference/P024_bt_hci_cp_le_add_dev_to_rl_结构体.md)
- [bt_hci_cp_le_rem_dev_from_rl](../bluetooth_hci_model_reference/P073_bt_hci_cp_le_rem_dev_from_rl_结构体.md)
- [bt_hci_rp_le_read_rl_size](../bluetooth_hci_model_reference/P373_bt_hci_rp_le_read_rl_size_结构体.md)
- [bt_hci_cp_le_read_peer_rpa](../bluetooth_hci_model_reference/P063_bt_hci_cp_le_read_peer_rpa_结构体.md)
- [bt_hci_rp_le_read_peer_rpa](../bluetooth_hci_model_reference/P369_bt_hci_rp_le_read_peer_rpa_结构体.md)
- [bt_hci_cp_le_read_local_rpa](../bluetooth_hci_model_reference/P062_bt_hci_cp_le_read_local_rpa_结构体.md)
- [bt_hci_rp_le_read_local_rpa](../bluetooth_hci_model_reference/P363_bt_hci_rp_le_read_local_rpa_结构体.md)
- [bt_hci_cp_le_set_addr_res_enable](../bluetooth_hci_model_reference/P081_bt_hci_cp_le_set_addr_res_enable_结构体.md)
- [bt_hci_cp_le_set_rpa_timeout](../bluetooth_hci_model_reference/P121_bt_hci_cp_le_set_rpa_timeout_结构体.md)
- [bt_hci_rp_le_read_max_data_len](../bluetooth_hci_model_reference/P367_bt_hci_rp_le_read_max_data_len_结构体.md)
- [bt_hci_cp_le_read_phy](../bluetooth_hci_model_reference/P064_bt_hci_cp_le_read_phy_结构体.md)
- [bt_hci_rp_le_read_phy](../bluetooth_hci_model_reference/P371_bt_hci_rp_le_read_phy_结构体.md)
- [bt_hci_cp_le_set_default_phy](../bluetooth_hci_model_reference/P094_bt_hci_cp_le_set_default_phy_结构体.md)
- [bt_hci_cp_le_set_phy](../bluetooth_hci_model_reference/P117_bt_hci_cp_le_set_phy_结构体.md)
- [bt_hci_cp_le_enh_rx_test](../bluetooth_hci_model_reference/P040_bt_hci_cp_le_enh_rx_test_结构体.md)
- [bt_hci_cp_le_enh_tx_test](../bluetooth_hci_model_reference/P041_bt_hci_cp_le_enh_tx_test_结构体.md)
- [bt_hci_cp_le_set_adv_set_random_addr](../bluetooth_hci_model_reference/P085_bt_hci_cp_le_set_adv_set_random_addr_结构体.md)
- [bt_hci_cp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P099_bt_hci_cp_le_set_ext_adv_param_结构体.md)
- [bt_hci_rp_le_set_ext_adv_param](../bluetooth_hci_model_reference/P387_bt_hci_rp_le_set_ext_adv_param_结构体.md)
- [bt_hci_cp_le_set_ext_adv_param_v2](../bluetooth_hci_model_reference/P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md)
- [bt_hci_cp_le_set_ext_adv_data](../bluetooth_hci_model_reference/P097_bt_hci_cp_le_set_ext_adv_data_结构体.md)
- [bt_hci_cp_le_set_ext_scan_rsp_data](../bluetooth_hci_model_reference/P103_bt_hci_cp_le_set_ext_scan_rsp_data_结构体.md)
- [bt_hci_ext_adv_set](../bluetooth_hci_model_reference/P307_bt_hci_ext_adv_set_结构体.md)
- [bt_hci_cp_le_set_ext_adv_enable](../bluetooth_hci_model_reference/P098_bt_hci_cp_le_set_ext_adv_enable_结构体.md)
- [bt_hci_rp_le_read_max_adv_data_len](../bluetooth_hci_model_reference/P366_bt_hci_rp_le_read_max_adv_data_len_结构体.md)
- [bt_hci_rp_le_read_num_adv_sets](../bluetooth_hci_model_reference/P368_bt_hci_rp_le_read_num_adv_sets_结构体.md)
- [bt_hci_cp_le_remove_adv_set](../bluetooth_hci_model_reference/P074_bt_hci_cp_le_remove_adv_set_结构体.md)
- [bt_hci_cp_le_set_per_adv_param](../bluetooth_hci_model_reference/P114_bt_hci_cp_le_set_per_adv_param_结构体.md)
- [bt_hci_cp_le_set_per_adv_data](../bluetooth_hci_model_reference/P112_bt_hci_cp_le_set_per_adv_data_结构体.md)
- [bt_hci_cp_le_set_per_adv_enable](../bluetooth_hci_model_reference/P113_bt_hci_cp_le_set_per_adv_enable_结构体.md)
- [bt_hci_ext_scan_phy](../bluetooth_hci_model_reference/P309_bt_hci_ext_scan_phy_结构体.md)
- [bt_hci_cp_le_set_ext_scan_param](../bluetooth_hci_model_reference/P102_bt_hci_cp_le_set_ext_scan_param_结构体.md)
- [bt_hci_cp_le_set_ext_scan_enable](../bluetooth_hci_model_reference/P101_bt_hci_cp_le_set_ext_scan_enable_结构体.md)
- [bt_hci_ext_conn_phy](../bluetooth_hci_model_reference/P308_bt_hci_ext_conn_phy_结构体.md)
- [bt_hci_cp_le_ext_create_conn](../bluetooth_hci_model_reference/P042_bt_hci_cp_le_ext_create_conn_结构体.md)
- [bt_hci_cp_le_ext_create_conn_v2](../bluetooth_hci_model_reference/P043_bt_hci_cp_le_ext_create_conn_v2_结构体.md)
- [bt_hci_cp_le_set_pawr_subevent_data_element](../bluetooth_hci_model_reference/P110_bt_hci_cp_le_set_pawr_subevent_data_element_结构体.md)
- [bt_hci_cp_le_set_pawr_subevent_data](../bluetooth_hci_model_reference/P109_bt_hci_cp_le_set_pawr_subevent_data_结构体.md)
- [bt_hci_cp_le_set_pawr_response_data](../bluetooth_hci_model_reference/P108_bt_hci_cp_le_set_pawr_response_data_结构体.md)
- [bt_hci_cp_le_set_pawr_sync_subevent](../bluetooth_hci_model_reference/P111_bt_hci_cp_le_set_pawr_sync_subevent_结构体.md)
- [bt_hci_cp_le_set_per_adv_param_v2](../bluetooth_hci_model_reference/P115_bt_hci_cp_le_set_per_adv_param_v2_结构体.md)
- [bt_hci_cp_le_per_adv_create_sync](../bluetooth_hci_model_reference/P053_bt_hci_cp_le_per_adv_create_sync_结构体.md)
- [bt_hci_cp_le_per_adv_terminate_sync](../bluetooth_hci_model_reference/P056_bt_hci_cp_le_per_adv_terminate_sync_结构体.md)
- [bt_hci_cp_le_add_dev_to_per_adv_list](../bluetooth_hci_model_reference/P023_bt_hci_cp_le_add_dev_to_per_adv_list_结构体.md)
- [bt_hci_cp_le_rem_dev_from_per_adv_list](../bluetooth_hci_model_reference/P072_bt_hci_cp_le_rem_dev_from_per_adv_list_结构体.md)
- [bt_hci_rp_le_read_per_adv_list_size](../bluetooth_hci_model_reference/P370_bt_hci_rp_le_read_per_adv_list_size_结构体.md)
- [bt_hci_rp_le_read_tx_power](../bluetooth_hci_model_reference/P376_bt_hci_rp_le_read_tx_power_结构体.md)
- [bt_hci_rp_le_read_rf_path_comp](../bluetooth_hci_model_reference/P372_bt_hci_rp_le_read_rf_path_comp_结构体.md)
- [bt_hci_cp_le_write_rf_path_comp](../bluetooth_hci_model_reference/P138_bt_hci_cp_le_write_rf_path_comp_结构体.md)
- [bt_hci_cp_le_set_privacy_mode](../bluetooth_hci_model_reference/P118_bt_hci_cp_le_set_privacy_mode_结构体.md)
- [bt_hci_cp_le_rx_test_v3](../bluetooth_hci_model_reference/P079_bt_hci_cp_le_rx_test_v3_结构体.md)
- [bt_hci_cp_le_tx_test_v3](../bluetooth_hci_model_reference/P131_bt_hci_cp_le_tx_test_v3_结构体.md)
- [bt_hci_cp_le_set_cl_cte_tx_params](../bluetooth_hci_model_reference/P090_bt_hci_cp_le_set_cl_cte_tx_params_结构体.md)
- [bt_hci_cp_le_set_cl_cte_tx_enable](../bluetooth_hci_model_reference/P089_bt_hci_cp_le_set_cl_cte_tx_enable_结构体.md)
- [bt_hci_cp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P088_bt_hci_cp_le_set_cl_cte_sampling_enable_结构体.md)
- [bt_hci_rp_le_set_cl_cte_sampling_enable](../bluetooth_hci_model_reference/P383_bt_hci_rp_le_set_cl_cte_sampling_enable_结构体.md)
- [bt_hci_cp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P091_bt_hci_cp_le_set_conn_cte_rx_params_结构体.md)
- [bt_hci_rp_le_set_conn_cte_rx_params](../bluetooth_hci_model_reference/P384_bt_hci_rp_le_set_conn_cte_rx_params_结构体.md)
- [bt_hci_cp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P092_bt_hci_cp_le_set_conn_cte_tx_params_结构体.md)
- [bt_hci_rp_le_set_conn_cte_tx_params](../bluetooth_hci_model_reference/P385_bt_hci_rp_le_set_conn_cte_tx_params_结构体.md)
- [bt_hci_cp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P027_bt_hci_cp_le_conn_cte_req_enable_结构体.md)
- [bt_hci_rp_le_conn_cte_req_enable](../bluetooth_hci_model_reference/P337_bt_hci_rp_le_conn_cte_req_enable_结构体.md)
- [bt_hci_cp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P028_bt_hci_cp_le_conn_cte_rsp_enable_结构体.md)
- [bt_hci_rp_le_conn_cte_rsp_enable](../bluetooth_hci_model_reference/P338_bt_hci_rp_le_conn_cte_rsp_enable_结构体.md)
- [bt_hci_rp_le_read_ant_info](../bluetooth_hci_model_reference/P353_bt_hci_rp_le_read_ant_info_结构体.md)
- [bt_hci_cp_le_set_per_adv_recv_enable](../bluetooth_hci_model_reference/P116_bt_hci_cp_le_set_per_adv_recv_enable_结构体.md)
- [bt_hci_cp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P055_bt_hci_cp_le_per_adv_sync_transfer_结构体.md)
- [bt_hci_rp_le_per_adv_sync_transfer](../bluetooth_hci_model_reference/P350_bt_hci_rp_le_per_adv_sync_transfer_结构体.md)
- [bt_hci_cp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P054_bt_hci_cp_le_per_adv_set_info_transfer_结构体.md)
- [bt_hci_rp_le_per_adv_set_info_transfer](../bluetooth_hci_model_reference/P349_bt_hci_rp_le_per_adv_set_info_transfer_结构体.md)
- [bt_hci_cp_le_past_param](../bluetooth_hci_model_reference/P052_bt_hci_cp_le_past_param_结构体.md)
- [bt_hci_rp_le_past_param](../bluetooth_hci_model_reference/P348_bt_hci_rp_le_past_param_结构体.md)
- [bt_hci_cp_le_default_past_param](../bluetooth_hci_model_reference/P038_bt_hci_cp_le_default_past_param_结构体.md)
- [bt_hci_rp_le_default_past_param](../bluetooth_hci_model_reference/P341_bt_hci_rp_le_default_past_param_结构体.md)
- [bt_hci_rp_le_read_buffer_size_v2](../bluetooth_hci_model_reference/P355_bt_hci_rp_le_read_buffer_size_v2_结构体.md)
- [bt_hci_cp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P061_bt_hci_cp_le_read_iso_tx_sync_结构体.md)
- [bt_hci_rp_le_read_iso_tx_sync](../bluetooth_hci_model_reference/P361_bt_hci_rp_le_read_iso_tx_sync_结构体.md)
- [bt_hci_cis_params](../bluetooth_hci_model_reference/P003_bt_hci_cis_params_结构体.md)
- [bt_hci_cp_le_set_cig_params](../bluetooth_hci_model_reference/P086_bt_hci_cp_le_set_cig_params_结构体.md)
- [bt_hci_rp_le_set_cig_params](../bluetooth_hci_model_reference/P381_bt_hci_rp_le_set_cig_params_结构体.md)
- [bt_hci_cis_params_test](../bluetooth_hci_model_reference/P004_bt_hci_cis_params_test_结构体.md)
- [bt_hci_cp_le_set_cig_params_test](../bluetooth_hci_model_reference/P087_bt_hci_cp_le_set_cig_params_test_结构体.md)
- [bt_hci_rp_le_set_cig_params_test](../bluetooth_hci_model_reference/P382_bt_hci_rp_le_set_cig_params_test_结构体.md)
- [bt_hci_cis](../bluetooth_hci_model_reference/P002_bt_hci_cis_结构体.md)
- [bt_hci_cp_le_create_cis](../bluetooth_hci_model_reference/P033_bt_hci_cp_le_create_cis_结构体.md)
- [bt_hci_cp_le_remove_cig](../bluetooth_hci_model_reference/P075_bt_hci_cp_le_remove_cig_结构体.md)
- [bt_hci_rp_le_remove_cig](../bluetooth_hci_model_reference/P379_bt_hci_rp_le_remove_cig_结构体.md)
- [bt_hci_cp_le_accept_cis](../bluetooth_hci_model_reference/P021_bt_hci_cp_le_accept_cis_结构体.md)
- [bt_hci_cp_le_reject_cis](../bluetooth_hci_model_reference/P070_bt_hci_cp_le_reject_cis_结构体.md)
- [bt_hci_rp_le_reject_cis](../bluetooth_hci_model_reference/P378_bt_hci_rp_le_reject_cis_结构体.md)
- [bt_hci_cp_le_create_big](../bluetooth_hci_model_reference/P031_bt_hci_cp_le_create_big_结构体.md)
- [bt_hci_cp_le_create_big_test](../bluetooth_hci_model_reference/P032_bt_hci_cp_le_create_big_test_结构体.md)
- [bt_hci_cp_le_terminate_big](../bluetooth_hci_model_reference/P129_bt_hci_cp_le_terminate_big_结构体.md)
- [bt_hci_cp_le_big_create_sync](../bluetooth_hci_model_reference/P025_bt_hci_cp_le_big_create_sync_结构体.md)
- [bt_hci_cp_le_big_terminate_sync](../bluetooth_hci_model_reference/P026_bt_hci_cp_le_big_terminate_sync_结构体.md)
- [bt_hci_rp_le_big_terminate_sync](../bluetooth_hci_model_reference/P336_bt_hci_rp_le_big_terminate_sync_结构体.md)
- [bt_hci_cp_le_req_peer_sca](../bluetooth_hci_model_reference/P077_bt_hci_cp_le_req_peer_sca_结构体.md)
- [bt_hci_cp_le_setup_iso_path](../bluetooth_hci_model_reference/P126_bt_hci_cp_le_setup_iso_path_结构体.md)
- [bt_hci_rp_le_setup_iso_path](../bluetooth_hci_model_reference/P391_bt_hci_rp_le_setup_iso_path_结构体.md)
- [bt_hci_cp_le_remove_iso_path](../bluetooth_hci_model_reference/P076_bt_hci_cp_le_remove_iso_path_结构体.md)
- [bt_hci_rp_le_remove_iso_path](../bluetooth_hci_model_reference/P380_bt_hci_rp_le_remove_iso_path_结构体.md)
- [bt_hci_cp_le_iso_transmit_test](../bluetooth_hci_model_reference/P049_bt_hci_cp_le_iso_transmit_test_结构体.md)
- [bt_hci_rp_le_iso_transmit_test](../bluetooth_hci_model_reference/P345_bt_hci_rp_le_iso_transmit_test_结构体.md)
- [bt_hci_cp_le_iso_receive_test](../bluetooth_hci_model_reference/P047_bt_hci_cp_le_iso_receive_test_结构体.md)
- [bt_hci_rp_le_iso_receive_test](../bluetooth_hci_model_reference/P343_bt_hci_rp_le_iso_receive_test_结构体.md)
- [bt_hci_cp_le_read_test_counters](../bluetooth_hci_model_reference/P068_bt_hci_cp_le_read_test_counters_结构体.md)
- [bt_hci_rp_le_read_test_counters](../bluetooth_hci_model_reference/P375_bt_hci_rp_le_read_test_counters_结构体.md)
- [bt_hci_cp_le_iso_test_end](../bluetooth_hci_model_reference/P048_bt_hci_cp_le_iso_test_end_结构体.md)
- [bt_hci_rp_le_iso_test_end](../bluetooth_hci_model_reference/P344_bt_hci_rp_le_iso_test_end_结构体.md)
- [bt_hci_cp_le_set_host_feature](../bluetooth_hci_model_reference/P105_bt_hci_cp_le_set_host_feature_结构体.md)
- [bt_hci_rp_le_set_host_feature](../bluetooth_hci_model_reference/P388_bt_hci_rp_le_set_host_feature_结构体.md)
- [bt_hci_cp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P060_bt_hci_cp_le_read_iso_link_quality_结构体.md)
- [bt_hci_rp_le_read_iso_link_quality](../bluetooth_hci_model_reference/P360_bt_hci_rp_le_read_iso_link_quality_结构体.md)
- [bt_hci_cp_le_tx_test_v4](../bluetooth_hci_model_reference/P132_bt_hci_cp_le_tx_test_v4_结构体.md)
- [bt_hci_rp_le_read_all_local_supported_features](../bluetooth_hci_model_reference/P352_bt_hci_rp_le_read_all_local_supported_features_结构体.md)
- [bt_hci_cp_le_read_all_remote_features](../bluetooth_hci_model_reference/P058_bt_hci_cp_le_read_all_remote_features_结构体.md)
- [bt_hci_cp_le_tx_test_v4_tx_power](../bluetooth_hci_model_reference/P133_bt_hci_cp_le_tx_test_v4_tx_power_结构体.md)
- [bt_hci_rp_le_read_local_supported_capabilities](../bluetooth_hci_model_reference/P364_bt_hci_rp_le_read_local_supported_capabilities_结构体.md)
- [bt_hci_rp_le_read_local_supported_capabilities_v2](../bluetooth_hci_model_reference/P365_bt_hci_rp_le_read_local_supported_capabilities_v2_结构体.md)
- [bt_hci_cp_le_read_remote_supported_capabilities](../bluetooth_hci_model_reference/P067_bt_hci_cp_le_read_remote_supported_capabilities_结构体.md)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities](../bluetooth_hci_model_reference/P135_bt_hci_cp_le_write_cached_remote_supported_capabilities_结构体.md)
- [bt_hci_cp_le_write_cached_remote_supported_capabilities_v2](../bluetooth_hci_model_reference/P136_bt_hci_cp_le_write_cached_remote_supported_capabilities_v2_结构体.md)
- [bt_hci_cp_le_security_enable](../bluetooth_hci_model_reference/P080_bt_hci_cp_le_security_enable_结构体.md)
- [bt_hci_cp_le_cs_set_default_settings](../bluetooth_hci_model_reference/P037_bt_hci_cp_le_cs_set_default_settings_结构体.md)
- [bt_hci_cp_le_read_remote_fae_table](../bluetooth_hci_model_reference/P065_bt_hci_cp_le_read_remote_fae_table_结构体.md)
- [bt_hci_cp_le_write_cached_remote_fae_table](../bluetooth_hci_model_reference/P134_bt_hci_cp_le_write_cached_remote_fae_table_结构体.md)
- [bt_hci_cp_le_set_procedure_parameters](../bluetooth_hci_model_reference/P119_bt_hci_cp_le_set_procedure_parameters_结构体.md)
- [bt_hci_cp_le_procedure_enable](../bluetooth_hci_model_reference/P057_bt_hci_cp_le_procedure_enable_结构体.md)
- [bt_hci_op_le_cs_test](../bluetooth_hci_model_reference/P330_bt_hci_op_le_cs_test_结构体.md)
- [bt_hci_cp_le_cs_create_config](../bluetooth_hci_model_reference/P035_bt_hci_cp_le_cs_create_config_结构体.md)
- [bt_hci_cp_le_cs_remove_config](../bluetooth_hci_model_reference/P036_bt_hci_cp_le_cs_remove_config_结构体.md)
- [bt_hci_cp_le_frame_space_update](../bluetooth_hci_model_reference/P044_bt_hci_cp_le_frame_space_update_结构体.md)
- [bt_hci_le_read_min_supported_conn_interval_group](../bluetooth_hci_model_reference/P325_bt_hci_le_read_min_supported_conn_interval_group_结构体.md)
- [bt_hci_op_le_read_min_supported_conn_interval](../bluetooth_hci_model_reference/P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md)
- [bt_hci_op_le_set_default_rate_parameters](../bluetooth_hci_model_reference/P332_bt_hci_op_le_set_default_rate_parameters_结构体.md)
- [bt_hci_op_le_connection_rate_request](../bluetooth_hci_model_reference/P329_bt_hci_op_le_connection_rate_request_结构体.md)
- [bt_hci_evt_inquiry_complete](../bluetooth_hci_model_reference/P218_bt_hci_evt_inquiry_complete_结构体.md)
- [bt_hci_evt_conn_complete](../bluetooth_hci_model_reference/P208_bt_hci_evt_conn_complete_结构体.md)
- [bt_hci_evt_conn_request](../bluetooth_hci_model_reference/P210_bt_hci_evt_conn_request_结构体.md)
- [bt_hci_evt_disconn_complete](../bluetooth_hci_model_reference/P212_bt_hci_evt_disconn_complete_结构体.md)
- [bt_hci_evt_auth_complete](../bluetooth_hci_model_reference/P203_bt_hci_evt_auth_complete_结构体.md)
- [bt_hci_evt_remote_name_req_complete](../bluetooth_hci_model_reference/P292_bt_hci_evt_remote_name_req_complete_结构体.md)
- [bt_hci_evt_encrypt_change](../bluetooth_hci_model_reference/P213_bt_hci_evt_encrypt_change_结构体.md)
- [bt_hci_evt_remote_features](../bluetooth_hci_model_reference/P291_bt_hci_evt_remote_features_结构体.md)
- [bt_hci_evt_remote_version_info](../bluetooth_hci_model_reference/P293_bt_hci_evt_remote_version_info_结构体.md)
- [bt_hci_evt_cmd_complete](../bluetooth_hci_model_reference/P206_bt_hci_evt_cmd_complete_结构体.md)
- [bt_hci_evt_cc_status](../bluetooth_hci_model_reference/P205_bt_hci_evt_cc_status_结构体.md)
- [bt_hci_evt_cmd_status](../bluetooth_hci_model_reference/P207_bt_hci_evt_cmd_status_结构体.md)
- [bt_hci_evt_hardware_error](../bluetooth_hci_model_reference/P216_bt_hci_evt_hardware_error_结构体.md)
- [bt_hci_evt_role_change](../bluetooth_hci_model_reference/P294_bt_hci_evt_role_change_结构体.md)
- [bt_hci_evt_num_completed_packets](../bluetooth_hci_model_reference/P288_bt_hci_evt_num_completed_packets_结构体.md)
- [bt_hci_evt_mode_change](../bluetooth_hci_model_reference/P287_bt_hci_evt_mode_change_结构体.md)
- [bt_hci_evt_pin_code_req](../bluetooth_hci_model_reference/P289_bt_hci_evt_pin_code_req_结构体.md)
- [bt_hci_evt_link_key_req](../bluetooth_hci_model_reference/P282_bt_hci_evt_link_key_req_结构体.md)
- [bt_hci_evt_link_key_notify](../bluetooth_hci_model_reference/P281_bt_hci_evt_link_key_notify_结构体.md)
- [bt_hci_evt_data_buf_overflow](../bluetooth_hci_model_reference/P211_bt_hci_evt_data_buf_overflow_结构体.md)
- [bt_hci_evt_conn_pkt_type_changed](../bluetooth_hci_model_reference/P209_bt_hci_evt_conn_pkt_type_changed_结构体.md)
- [bt_hci_evt_inquiry_result_with_rssi](../bluetooth_hci_model_reference/P219_bt_hci_evt_inquiry_result_with_rssi_结构体.md)
- [bt_hci_evt_remote_ext_features](../bluetooth_hci_model_reference/P290_bt_hci_evt_remote_ext_features_结构体.md)
- [bt_hci_evt_le_per_adv_sync_established_v2](../bluetooth_hci_model_reference/P270_bt_hci_evt_le_per_adv_sync_established_v2_结构体.md)
- [bt_hci_evt_le_per_advertising_report_v2](../bluetooth_hci_model_reference/P273_bt_hci_evt_le_per_advertising_report_v2_结构体.md)
- [bt_hci_evt_le_past_received_v2](../bluetooth_hci_model_reference/P264_bt_hci_evt_le_past_received_v2_结构体.md)
- [bt_hci_evt_le_per_adv_subevent_data_request](../bluetooth_hci_model_reference/P268_bt_hci_evt_le_per_adv_subevent_data_request_结构体.md)
- [bt_hci_evt_le_per_adv_response](../bluetooth_hci_model_reference/P266_bt_hci_evt_le_per_adv_response_结构体.md)
- [bt_hci_evt_le_per_adv_response_report](../bluetooth_hci_model_reference/P267_bt_hci_evt_le_per_adv_response_report_结构体.md)
- [bt_hci_evt_le_enh_conn_complete_v2](../bluetooth_hci_model_reference/P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md)
- [bt_hci_evt_sync_conn_complete](../bluetooth_hci_model_reference/P296_bt_hci_evt_sync_conn_complete_结构体.md)
- [bt_hci_evt_extended_inquiry_result](../bluetooth_hci_model_reference/P215_bt_hci_evt_extended_inquiry_result_结构体.md)
- [bt_hci_evt_encrypt_key_refresh_complete](../bluetooth_hci_model_reference/P214_bt_hci_evt_encrypt_key_refresh_complete_结构体.md)
- [bt_hci_evt_io_capa_req](../bluetooth_hci_model_reference/P220_bt_hci_evt_io_capa_req_结构体.md)
- [bt_hci_evt_io_capa_resp](../bluetooth_hci_model_reference/P221_bt_hci_evt_io_capa_resp_结构体.md)
- [bt_hci_evt_user_confirm_req](../bluetooth_hci_model_reference/P297_bt_hci_evt_user_confirm_req_结构体.md)
- [bt_hci_evt_user_passkey_req](../bluetooth_hci_model_reference/P299_bt_hci_evt_user_passkey_req_结构体.md)
- [bt_hci_evt_ssp_complete](../bluetooth_hci_model_reference/P295_bt_hci_evt_ssp_complete_结构体.md)
- [bt_hci_evt_user_passkey_notify](../bluetooth_hci_model_reference/P298_bt_hci_evt_user_passkey_notify_结构体.md)
- [bt_hci_evt_le_meta_event](../bluetooth_hci_model_reference/P261_bt_hci_evt_le_meta_event_结构体.md)
- [bt_hci_evt_auth_payload_timeout_exp](../bluetooth_hci_model_reference/P204_bt_hci_evt_auth_payload_timeout_exp_结构体.md)
- [bt_hci_evt_le_conn_complete](../bluetooth_hci_model_reference/P234_bt_hci_evt_le_conn_complete_结构体.md)
- [bt_hci_evt_le_advertising_info](../bluetooth_hci_model_reference/P223_bt_hci_evt_le_advertising_info_结构体.md)
- [bt_hci_evt_le_advertising_report](../bluetooth_hci_model_reference/P224_bt_hci_evt_le_advertising_report_结构体.md)
- [bt_hci_evt_le_conn_update_complete](../bluetooth_hci_model_reference/P237_bt_hci_evt_le_conn_update_complete_结构体.md)
- [bt_hci_evt_le_remote_feat_complete](../bluetooth_hci_model_reference/P276_bt_hci_evt_le_remote_feat_complete_结构体.md)
- [bt_hci_evt_le_ltk_request](../bluetooth_hci_model_reference/P260_bt_hci_evt_le_ltk_request_结构体.md)
- [bt_hci_evt_le_conn_param_req](../bluetooth_hci_model_reference/P235_bt_hci_evt_le_conn_param_req_结构体.md)
- [bt_hci_evt_le_data_len_change](../bluetooth_hci_model_reference/P251_bt_hci_evt_le_data_len_change_结构体.md)
- [bt_hci_evt_le_p256_public_key_complete](../bluetooth_hci_model_reference/P262_bt_hci_evt_le_p256_public_key_complete_结构体.md)
- [bt_hci_evt_le_generate_dhkey_complete](../bluetooth_hci_model_reference/P259_bt_hci_evt_le_generate_dhkey_complete_结构体.md)
- [bt_hci_evt_le_enh_conn_complete](../bluetooth_hci_model_reference/P254_bt_hci_evt_le_enh_conn_complete_结构体.md)
- [bt_hci_evt_le_direct_adv_info](../bluetooth_hci_model_reference/P252_bt_hci_evt_le_direct_adv_info_结构体.md)
- [bt_hci_evt_le_direct_adv_report](../bluetooth_hci_model_reference/P253_bt_hci_evt_le_direct_adv_report_结构体.md)
- [bt_hci_evt_le_phy_update_complete](../bluetooth_hci_model_reference/P274_bt_hci_evt_le_phy_update_complete_结构体.md)
- [bt_hci_evt_le_ext_advertising_info](../bluetooth_hci_model_reference/P256_bt_hci_evt_le_ext_advertising_info_结构体.md)
- [bt_hci_evt_le_ext_advertising_report](../bluetooth_hci_model_reference/P257_bt_hci_evt_le_ext_advertising_report_结构体.md)
- [bt_hci_evt_le_per_adv_sync_established](../bluetooth_hci_model_reference/P269_bt_hci_evt_le_per_adv_sync_established_结构体.md)
- [bt_hci_evt_le_per_advertising_report](../bluetooth_hci_model_reference/P272_bt_hci_evt_le_per_advertising_report_结构体.md)
- [bt_hci_evt_le_per_adv_sync_lost](../bluetooth_hci_model_reference/P271_bt_hci_evt_le_per_adv_sync_lost_结构体.md)
- [bt_hci_evt_le_adv_set_terminated](../bluetooth_hci_model_reference/P222_bt_hci_evt_le_adv_set_terminated_结构体.md)
- [bt_hci_evt_le_scan_req_received](../bluetooth_hci_model_reference/P278_bt_hci_evt_le_scan_req_received_结构体.md)
- [bt_hci_evt_le_chan_sel_algo](../bluetooth_hci_model_reference/P230_bt_hci_evt_le_chan_sel_algo_结构体.md)
- [bt_hci_le_iq_sample](../bluetooth_hci_model_reference/P323_bt_hci_le_iq_sample_结构体.md)
- [bt_hci_evt_le_connectionless_iq_report](../bluetooth_hci_model_reference/P239_bt_hci_evt_le_connectionless_iq_report_结构体.md)
- [bt_hci_evt_le_connection_iq_report](../bluetooth_hci_model_reference/P238_bt_hci_evt_le_connection_iq_report_结构体.md)
- [bt_hci_evt_le_cte_req_failed](../bluetooth_hci_model_reference/P250_bt_hci_evt_le_cte_req_failed_结构体.md)
- [bt_hci_evt_le_past_received](../bluetooth_hci_model_reference/P263_bt_hci_evt_le_past_received_结构体.md)
- [bt_hci_evt_le_cis_established](../bluetooth_hci_model_reference/P231_bt_hci_evt_le_cis_established_结构体.md)
- [bt_hci_evt_le_cis_req](../bluetooth_hci_model_reference/P233_bt_hci_evt_le_cis_req_结构体.md)
- [bt_hci_evt_le_big_complete](../bluetooth_hci_model_reference/P225_bt_hci_evt_le_big_complete_结构体.md)
- [bt_hci_evt_le_big_terminate](../bluetooth_hci_model_reference/P228_bt_hci_evt_le_big_terminate_结构体.md)
- [bt_hci_evt_le_big_sync_established](../bluetooth_hci_model_reference/P226_bt_hci_evt_le_big_sync_established_结构体.md)
- [bt_hci_evt_le_big_sync_lost](../bluetooth_hci_model_reference/P227_bt_hci_evt_le_big_sync_lost_结构体.md)
- [bt_hci_evt_le_req_peer_sca_complete](../bluetooth_hci_model_reference/P277_bt_hci_evt_le_req_peer_sca_complete_结构体.md)
- [bt_hci_evt_le_path_loss_threshold](../bluetooth_hci_model_reference/P265_bt_hci_evt_le_path_loss_threshold_结构体.md)
- [bt_hci_evt_le_transmit_power_report](../bluetooth_hci_model_reference/P280_bt_hci_evt_le_transmit_power_report_结构体.md)
- [bt_hci_evt_le_biginfo_adv_report](../bluetooth_hci_model_reference/P229_bt_hci_evt_le_biginfo_adv_report_结构体.md)
- [bt_hci_evt_le_subrate_change](../bluetooth_hci_model_reference/P279_bt_hci_evt_le_subrate_change_结构体.md)
- [bt_hci_evt_le_cis_established_v2](../bluetooth_hci_model_reference/P232_bt_hci_evt_le_cis_established_v2_结构体.md)
- [bt_hci_evt_le_read_all_remote_feat_complete](../bluetooth_hci_model_reference/P275_bt_hci_evt_le_read_all_remote_feat_complete_结构体.md)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete](../bluetooth_hci_model_reference/P243_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_结构体.md)
- [bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2](../bluetooth_hci_model_reference/P244_bt_hci_evt_le_cs_read_remote_supported_capabilities_complete_v2_结构体.md)
- [bt_hci_evt_le_cs_read_remote_fae_table_complete](../bluetooth_hci_model_reference/P242_bt_hci_evt_le_cs_read_remote_fae_table_complete_结构体.md)
- [bt_hci_evt_le_cs_security_enable_complete](../bluetooth_hci_model_reference/P245_bt_hci_evt_le_cs_security_enable_complete_结构体.md)
- [bt_hci_evt_le_cs_config_complete](../bluetooth_hci_model_reference/P240_bt_hci_evt_le_cs_config_complete_结构体.md)
- [bt_hci_le_cs_step_data_mode_0_initiator](../bluetooth_hci_model_reference/P315_bt_hci_le_cs_step_data_mode_0_initiator_结构体.md)
- [bt_hci_le_cs_step_data_mode_0_reflector](../bluetooth_hci_model_reference/P316_bt_hci_le_cs_step_data_mode_0_reflector_结构体.md)
- [bt_hci_le_cs_step_data_mode_1](../bluetooth_hci_model_reference/P317_bt_hci_le_cs_step_data_mode_1_结构体.md)
- [bt_hci_le_cs_step_data_mode_1_ss_rtt](../bluetooth_hci_model_reference/P318_bt_hci_le_cs_step_data_mode_1_ss_rtt_结构体.md)
- [bt_hci_le_cs_step_data_tone_info](../bluetooth_hci_model_reference/P322_bt_hci_le_cs_step_data_tone_info_结构体.md)
- [bt_hci_le_cs_step_data_mode_2](../bluetooth_hci_model_reference/P319_bt_hci_le_cs_step_data_mode_2_结构体.md)
- [bt_hci_le_cs_step_data_mode_3](../bluetooth_hci_model_reference/P320_bt_hci_le_cs_step_data_mode_3_结构体.md)
- [bt_hci_le_cs_step_data_mode_3_ss_rtt](../bluetooth_hci_model_reference/P321_bt_hci_le_cs_step_data_mode_3_ss_rtt_结构体.md)
- [bt_hci_evt_le_cs_subevent_result_step](../bluetooth_hci_model_reference/P248_bt_hci_evt_le_cs_subevent_result_step_结构体.md)
- [bt_hci_evt_le_cs_subevent_result](../bluetooth_hci_model_reference/P246_bt_hci_evt_le_cs_subevent_result_结构体.md)
- [bt_hci_evt_le_cs_subevent_result_continue](../bluetooth_hci_model_reference/P247_bt_hci_evt_le_cs_subevent_result_continue_结构体.md)
- [bt_hci_evt_le_cs_test_end_complete](../bluetooth_hci_model_reference/P249_bt_hci_evt_le_cs_test_end_complete_结构体.md)
- [bt_hci_evt_le_cs_procedure_enable_complete](../bluetooth_hci_model_reference/P241_bt_hci_evt_le_cs_procedure_enable_complete_结构体.md)
- [bt_hci_evt_le_frame_space_update_complete](../bluetooth_hci_model_reference/P258_bt_hci_evt_le_frame_space_update_complete_结构体.md)
- [bt_hci_evt_le_conn_rate_change](../bluetooth_hci_model_reference/P236_bt_hci_evt_le_conn_rate_change_结构体.md)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)
- [FIELD_PREP](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="ahci__types_8h_html_a28a9f26ba563e2687856aff39b044039"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="ahci__types_8h_html_a7d5bc35e597d03fbc65084b39771cf0b"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ahci__types_8h_html_a41e5b49e645ed511340a61f843f6b238"></a>
<a id="ahci__types_8h_html_a4d920d42e8042c9117f97e334f889f51"></a>
<a id="ahci__types_8h_html_a6bf20989952fed3726bc45873beb896e"></a>
<a id="ahci__types_8h_html_ad711e7491883e1f1e068fe167cca8a4e"></a>
<a id="ahci__types_8h_html_a480fc67a1c8a2f36410f285ef0ee36e7"></a>
<a id="ahci__types_8h_html_a41eae1585972ae6792eb1a639c2e3a8e"></a>
<a id="ahci__types_8h_html_a1c6fd06877a5606ae33aedc45a71f853"></a>
<a id="ahci__types_8h_html_af2a4be520b4d8c3eb56231b865738e90"></a>
<a id="ahci__types_8h_html_ab918084874aace22954aa748333baf6d"></a>
<a id="ahci__types_8h_html_aa4572a11d78651ce775a010178c6dfa2"></a>
<a id="ahci__types_8h_html_adce7c3804a224e7b7317728fa27d4945"></a>
<a id="ahci__types_8h_html_aa98eed376b6d5263621f14c55d776088"></a>
<a id="ahci__types_8h_html_a298fde96c2d6376e3333a99f7e03409d"></a>
<a id="ahci__types_8h_html_ab816048bdd6c1e42b0e458abebb76572"></a>
<a id="ahci__types_8h_html_aa45b06a49232372891ceb5e4496d46da"></a>
<a id="ahci__types_8h_html_adb884a30bc1a24e3dfb115cef7149c81"></a>
<a id="ahci__types_8h_html_aed34742e8554b830c3b6c4bf04f0e2db"></a>
<a id="ahci__types_8h_html_aa5279a2ce26decb5856a6b709d0641c9"></a>
<a id="ahci__types_8h_html_a6abf01c846a5d637ca98997f6cfc263d"></a>
<a id="ahci__types_8h_html_a331e7697a3fdc073abba5dd0ff47346b"></a>
<a id="ahci__types_8h_html_ac09127210b281e5ee45fbc134df64aa6"></a>
<a id="ahci__types_8h_html_abd616dd5af5ed3742be9bae400ded848"></a>
<a id="ahci__types_8h_html_ae1a0751e7c380117c4e31741712096a4"></a>
<a id="ahci__types_8h_html_a1ac5bab6d48775b4e63e249b5759a683"></a>
<a id="ahci__types_8h_html_a8f1fa8948f79bec50373e0342ab0969a"></a>
<a id="ahci__types_8h_html_a51fc94e0f2ed1c6fe724c2846756cb31"></a>
<a id="ahci__types_8h_html_a06c9aa4e8165cfe3e359283f199b450c"></a>
<a id="ahci__types_8h_html_abe5a1ddbede473f583106e3500dccdb1"></a>
<a id="ahci__types_8h_html_af08a1ffd734d1c211f38d90b4fe72417"></a>
<a id="ahci__types_8h_html_a0d80ccb33d263abd3b42de1b69cfeeeb"></a>
<a id="ahci__types_8h_html_a28a862eaf11f8b45237f3b87e4bb15c7"></a>
<a id="ahci__types_8h_html_aa05da01a6a9b9ac26423d6fc2661f3db"></a>
<a id="ahci__types_8h_html_a434fb43b6b3176393f5d22d3932d69fa"></a>
<a id="ahci__types_8h_html_af251cb9d905586fd53113f5920038dae"></a>
<a id="ahci__types_8h_html_a00bb51972e0db07be84d4f3dfd007cea"></a>
<a id="ahci__types_8h_html_ad5a8221cb25d79b63f1a574699983038"></a>
<a id="ahci__types_8h_html_aeaea6ea6595de9e3283fd6063bf7c579"></a>
<a id="ahci__types_8h_html_afcbc8d664c8e924b777c06ffb4c17315"></a>
<a id="ahci__types_8h_html_a800686aa45cf336fbd6efc76b3752959"></a>
<a id="ahci__types_8h_html_a3c4196c04a73aa537baa845e061e9654"></a>
<a id="ahci__types_8h_html_a0138172a0ed78244d8d3ac9d6936cf85"></a>
<a id="ahci__types_8h_html_ae58f5260530d1b94608874f5d03d766d"></a>
<a id="ahci__types_8h_html_a9d9449f1935d6522291eca581f3fa9b0"></a>
<a id="ahci__types_8h_html_ac00a188cc19a04ff9523fd3a4e044b17"></a>
<a id="ahci__types_8h_html_a670eda9a27a581646c5bc17fc452b466"></a>
<a id="ahci__types_8h_html_a2fed771f5611212e48027025e11f7678"></a>
<a id="ahci__types_8h_html_a23f80a9369c84786bff1330a4b07c3e7"></a>
<a id="ahci__types_8h_html_a72b4b642556556b959d6f9eda2a70770"></a>
<a id="ahci__types_8h_html_a972f90f9bfbf7b53d4f71f04d4c82ed5"></a>
<a id="ahci__types_8h_html_aa677b6c5357585d36d81f0ea831e7568"></a>
<a id="ahci__types_8h_html_ac0fe269d4e2d7f3794456f9a65e68113"></a>
<a id="ahci__types_8h_html_af4f275468c7d3266107587793a6be7c6"></a>
<a id="ahci__types_8h_html_ab8d4ecdf12cf208bb39012b0aa6b2547"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="ahci__types_8h_html_a05dce15a404d08bb44ccc73616a90082"></a>
<a id="ahci__types_8h_html_ac7fdeedc1f828f4add126a5f5b12c5d8"></a>
<a id="ahci__types_8h_html_a02fbd3478aad48191c1e68337070ff24"></a>
<a id="ahci__types_8h_html_a94baca9b3db3bff4abbbdddbbb571d0e"></a>
<a id="ahci__types_8h_html_a6570f5c7ac9cca8c4e27c60244b8cc4d"></a>
<a id="ahci__types_8h_html_a9bdbdc6e181731a58ec91d53cdade532"></a>
<a id="agroup__sys-util_html_ga1a138896caafcb2429a6483ea7412d12"></a>
<a id="ahci__types_8h_html_a1252be2692bcfb7a1256c63c4deed15d"></a>
<a id="ahci__types_8h_html_a1ccc4d6e5cfc560b7e2cb80c4c386607"></a>
<a id="ahci__types_8h_html_aa45e51b1be89505fe599bc7983fcb950"></a>
<a id="ahci__types_8h_html_ac5f09e3db1bc4d697ff705802e9ec3a0"></a>
<a id="ahci__types_8h_html_a1f7474cb16a495bd81dc1f23d4103f70"></a>
<a id="ahci__types_8h_html_a3e0b6a1aa3818cb0c36f7883fd361c7e"></a>
<a id="ahci__types_8h_html_a4b048addd84409867177a97c785c4a73"></a>
<a id="ahci__types_8h_html_a9530e916a0cf905e2185cd021320bfff"></a>
<a id="ahci__types_8h_html_a98f8217b27c0b9b7817c86520da45018"></a>
<a id="ahci__types_8h_html_af67cdc23b6542e6d8323f14e17c7171d"></a>

---

[上一章](P004_zephyr__bluetooth__mesh__cfg_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__bluetooth__iso.h_文件参考.md)
