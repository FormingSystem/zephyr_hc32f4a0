---
id: learning.zephyr-docs.api-file-runtime-reference.page-17
title: zephyr__bluetooth__hci_vs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_bluetooth\_\_hci\_vs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fversion_5Finfo"></a>

```c
struct bt_hci_rp_vs_read_version_info
```

相关声明：[bt_hci_rp_vs_read_version_info](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fsupported_5Fcommands"></a>

```c
struct bt_hci_rp_vs_read_supported_commands
```

相关声明：[bt_hci_rp_vs_read_supported_commands](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fsupported_5Ffeatures"></a>

```c
struct bt_hci_rp_vs_read_supported_features
```

相关声明：[bt_hci_rp_vs_read_supported_features](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fset_5Fevent_5Fmask"></a>

```c
struct bt_hci_cp_vs_set_event_mask
```

相关声明：[bt_hci_cp_vs_set_event_mask](../bluetooth_hci_model_reference/P177_bt_hci_cp_vs_set_event_mask_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Freset"></a>

```c
struct bt_hci_cp_vs_reset
```

相关声明：[bt_hci_cp_vs_reset](../bluetooth_hci_model_reference/P176_bt_hci_cp_vs_reset_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fwrite_5Fbd_5Faddr"></a>

```c
struct bt_hci_cp_vs_write_bd_addr
```

相关声明：[bt_hci_cp_vs_write_bd_addr](../bluetooth_hci_model_reference/P182_bt_hci_cp_vs_write_bd_addr_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fset_5Ftrace_5Fenable"></a>

```c
struct bt_hci_cp_vs_set_trace_enable
```

相关声明：[bt_hci_cp_vs_set_trace_enable](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fbuild_5Finfo"></a>

```c
struct bt_hci_rp_vs_read_build_info
```

相关声明：[bt_hci_rp_vs_read_build_info](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fstatic_5Faddr"></a>

```c
struct bt_hci_vs_static_addr
```

相关声明：[bt_hci_vs_static_addr](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fstatic_5Faddrs"></a>

```c
struct bt_hci_rp_vs_read_static_addrs
```

相关声明：[bt_hci_rp_vs_read_static_addrs](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fkey_5Fhierarchy_5Froots"></a>

```c
struct bt_hci_rp_vs_read_key_hierarchy_roots
```

相关声明：[bt_hci_rp_vs_read_key_hierarchy_roots](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fchip_5Ftemp"></a>

```c
struct bt_hci_rp_vs_read_chip_temp
```

相关声明：[bt_hci_rp_vs_read_chip_temp](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Fcmd"></a>

```c
struct bt_hci_vs_cmd
```

相关声明：[bt_hci_vs_cmd](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fhost_5Fstack_5Fcmds"></a>

```c
struct bt_hci_rp_vs_read_host_stack_cmds
```

相关声明：[bt_hci_rp_vs_read_host_stack_cmds](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fset_5Fscan_5Freq_5Freports"></a>

```c
struct bt_hci_cp_vs_set_scan_req_reports
```

相关声明：[bt_hci_cp_vs_set_scan_req_reports](../bluetooth_hci_model_reference/P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fwrite_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_cp_vs_write_tx_power_level
```

相关声明：[bt_hci_cp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fwrite_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_rp_vs_write_tx_power_level
```

相关声明：[bt_hci_rp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_cp_vs_read_tx_power_level
```

相关声明：[bt_hci_cp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Ftx_5Fpower_5Flevel"></a>

```c
struct bt_hci_rp_vs_read_tx_power_level
```

相关声明：[bt_hci_rp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fvs_5Fread_5Fusb_5Ftransport_5Fmode"></a>

```c
struct bt_hci_rp_vs_read_usb_transport_mode
```

相关声明：[bt_hci_rp_vs_read_usb_transport_mode](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fset_5Fusb_5Ftransport_5Fmode"></a>

```c
struct bt_hci_cp_vs_set_usb_transport_mode
```

相关声明：[bt_hci_cp_vs_set_usb_transport_mode](../bluetooth_hci_model_reference/P181_bt_hci_cp_vs_set_usb_transport_mode_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fvs_5Fset_5Fmin_5Fnum_5Fused_5Fchans"></a>

```c
struct bt_hci_cp_vs_set_min_num_used_chans
```

相关声明：[bt_hci_cp_vs_set_min_num_used_chans](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs"></a>

```c
struct bt_hci_evt_vs
```

相关声明：[bt_hci_evt_vs](../bluetooth_hci_model_reference/P300_bt_hci_evt_vs_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Ffatal_5Ferror_5Fcpu_5Fdata_5Fcortex_5Fm"></a>

```c
struct bt_hci_vs_fatal_error_cpu_data_cortex_m
```

相关声明：[bt_hci_vs_fatal_error_cpu_data_cortex_m](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md)。

<a id="r_bt_5Fhci_5Fvs_5Ffatal_5Ferror_5Fstack_5Fframe"></a>

```c
struct bt_hci_vs_fatal_error_stack_frame
```

相关声明：[bt_hci_vs_fatal_error_stack_frame](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Ffatal_5Ferror_5Ftrace_5Fdata"></a>

```c
struct bt_hci_evt_vs_fatal_error_trace_data
```

相关声明：[bt_hci_evt_vs_fatal_error_trace_data](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Ffatal_5Ferror"></a>

```c
struct bt_hci_evt_vs_fatal_error
```

相关声明：[bt_hci_evt_vs_fatal_error](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Ftrace_5Finfo"></a>

```c
struct bt_hci_evt_vs_trace_info
```

相关声明：[bt_hci_evt_vs_trace_info](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Fscan_5Freq_5Frx"></a>

```c
struct bt_hci_evt_vs_scan_req_rx
```

相关声明：[bt_hci_evt_vs_scan_req_rx](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md)。

<a id="r_bt_5Fhci_5Fle_5Fiq_5Fsample16"></a>

```c
struct bt_hci_le_iq_sample16
```

相关声明：[bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Fle_5Fconnectionless_5Fiq_5Freport"></a>

```c
struct bt_hci_evt_vs_le_connectionless_iq_report
```

相关声明：[bt_hci_evt_vs_le_connectionless_iq_report](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fvs_5Fle_5Fconnection_5Fiq_5Freport"></a>

```c
struct bt_hci_evt_vs_le_connection_iq_report
```

相关声明：[bt_hci_evt_vs_le_connection_iq_report](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh"></a>

```c
struct bt_hci_cp_mesh
```

相关声明：[bt_hci_cp_mesh](../bluetooth_hci_model_reference/P141_bt_hci_cp_mesh_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fget_5Fopts"></a>

```c
struct bt_hci_rp_mesh_get_opts
```

相关声明：[bt_hci_rp_mesh_get_opts](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md)。

<a id="r_bt_5Fhci_5Fmesh_5Fpattern"></a>

```c
struct bt_hci_mesh_pattern
```

相关声明：[bt_hci_mesh_pattern](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh_5Fset_5Fscan_5Ffilter"></a>

```c
struct bt_hci_cp_mesh_set_scan_filter
```

相关声明：[bt_hci_cp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fset_5Fscan_5Ffilter"></a>

```c
struct bt_hci_rp_mesh_set_scan_filter
```

相关声明：[bt_hci_rp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh_5Fadvertise"></a>

```c
struct bt_hci_cp_mesh_advertise
```

相关声明：[bt_hci_cp_mesh_advertise](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fadvertise"></a>

```c
struct bt_hci_rp_mesh_advertise
```

相关声明：[bt_hci_rp_mesh_advertise](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh_5Fadvertise_5Ftimed"></a>

```c
struct bt_hci_cp_mesh_advertise_timed
```

相关声明：[bt_hci_cp_mesh_advertise_timed](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fadvertise_5Ftimed"></a>

```c
struct bt_hci_rp_mesh_advertise_timed
```

相关声明：[bt_hci_rp_mesh_advertise_timed](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh_5Fadvertise_5Fcancel"></a>

```c
struct bt_hci_cp_mesh_advertise_cancel
```

相关声明：[bt_hci_cp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P143_bt_hci_cp_mesh_advertise_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fadvertise_5Fcancel"></a>

```c
struct bt_hci_rp_mesh_advertise_cancel
```

相关声明：[bt_hci_rp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md)。

<a id="r_bt_5Fhci_5Fcp_5Fmesh_5Fset_5Fscanning"></a>

```c
struct bt_hci_cp_mesh_set_scanning
```

相关声明：[bt_hci_cp_mesh_set_scanning](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md)。

<a id="r_bt_5Fhci_5Frp_5Fmesh_5Fset_5Fscanning"></a>

```c
struct bt_hci_rp_mesh_set_scanning
```

相关声明：[bt_hci_rp_mesh_set_scanning](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fmesh"></a>

```c
struct bt_hci_evt_mesh
```

相关声明：[bt_hci_evt_mesh](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fmesh_5Fadv_5Fcomplete"></a>

```c
struct bt_hci_evt_mesh_adv_complete
```

相关声明：[bt_hci_evt_mesh_adv_complete](../bluetooth_hci_model_reference/P284_bt_hci_evt_mesh_adv_complete_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fmesh_5Fscan_5Freport"></a>

```c
struct bt_hci_evt_mesh_scan_report
```

相关声明：[bt_hci_evt_mesh_scan_report](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md)。

<a id="r_bt_5Fhci_5Fevt_5Fmesh_5Fscanning_5Freport"></a>

```c
struct bt_hci_evt_mesh_scanning_report
```

相关声明：[bt_hci_evt_mesh_scanning_report](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_a98cda5172947a82dfee334a5db41b0bb"></a>

```c
#define BT_VS_CMD_BIT_VERSION 0
```

相关声明：[BT_VS_CMD_BIT_VERSION](#a98cda5172947a82dfee334a5db41b0bb)。

<a id="r_a2eec9eff49fc0d8f4e4f746dd7498478"></a>

```c
#define BT_VS_CMD_BIT_SUP_CMD 1
```

相关声明：[BT_VS_CMD_BIT_SUP_CMD](#a2eec9eff49fc0d8f4e4f746dd7498478)。

<a id="r_a418e0fd9c322671c1124835752b25678"></a>

```c
#define BT_VS_CMD_BIT_SUP_FEAT 2
```

相关声明：[BT_VS_CMD_BIT_SUP_FEAT](#a418e0fd9c322671c1124835752b25678)。

<a id="r_ab1b627847e323e94949b53665e47f20f"></a>

```c
#define BT_VS_CMD_BIT_SET_EVT_MASK 3
```

相关声明：[BT_VS_CMD_BIT_SET_EVT_MASK](#ab1b627847e323e94949b53665e47f20f)。

<a id="r_a020ca307df4c66bcd4c4f6da42d22e40"></a>

```c
#define BT_VS_CMD_BIT_RESET 4
```

相关声明：[BT_VS_CMD_BIT_RESET](#a020ca307df4c66bcd4c4f6da42d22e40)。

<a id="r_ac8fa0f7e3d5b802f1797c77d988bc172"></a>

```c
#define BT_VS_CMD_BIT_WRITE_BDADDR 5
```

相关声明：[BT_VS_CMD_BIT_WRITE_BDADDR](#ac8fa0f7e3d5b802f1797c77d988bc172)。

<a id="r_ad57ee37a93208d3127e5ba36933b0d36"></a>

```c
#define BT_VS_CMD_BIT_SET_TRACE_ENABLE 6
```

相关声明：[BT_VS_CMD_BIT_SET_TRACE_ENABLE](#ad57ee37a93208d3127e5ba36933b0d36)。

<a id="r_aaae2460cf69b0ad51aedf57c72d42103"></a>

```c
#define BT_VS_CMD_BIT_READ_BUILD_INFO 7
```

相关声明：[BT_VS_CMD_BIT_READ_BUILD_INFO](#aaae2460cf69b0ad51aedf57c72d42103)。

<a id="r_a27e19ec90e057244db7f632887a46ec1"></a>

```c
#define BT_VS_CMD_BIT_READ_STATIC_ADDRS 8
```

相关声明：[BT_VS_CMD_BIT_READ_STATIC_ADDRS](#a27e19ec90e057244db7f632887a46ec1)。

<a id="r_aa8b39f4ac968cf0cdb18073de1aa1ad5"></a>

```c
#define BT_VS_CMD_BIT_READ_KEY_ROOTS 9
```

相关声明：[BT_VS_CMD_BIT_READ_KEY_ROOTS](#aa8b39f4ac968cf0cdb18073de1aa1ad5)。

<a id="r_a96cee049fdf09d1e22aa2204a080c956"></a>

```c
#define BT_VS_CMD_BIT_READ_CHIP_TEMP 10
```

相关声明：[BT_VS_CMD_BIT_READ_CHIP_TEMP](#a96cee049fdf09d1e22aa2204a080c956)。

<a id="r_a072226e7bfd637f71a03971e18d795e5"></a>

```c
#define BT_VS_CMD_BIT_READ_HOST_STACK_CMD 11
```

相关声明：[BT_VS_CMD_BIT_READ_HOST_STACK_CMD](#a072226e7bfd637f71a03971e18d795e5)。

<a id="r_ac16322768bdd4688b2cefb4ea7b8c26f"></a>

```c
#define BT_VS_CMD_BIT_SET_SCAN_REP_ENABLE 12
```

相关声明：[BT_VS_CMD_BIT_SET_SCAN_REP_ENABLE](#ac16322768bdd4688b2cefb4ea7b8c26f)。

<a id="r_a3f720e278e3aeefd11e9682d683e448b"></a>

```c
#define BT_VS_CMD_BIT_WRITE_TX_POWER 13
```

相关声明：[BT_VS_CMD_BIT_WRITE_TX_POWER](#a3f720e278e3aeefd11e9682d683e448b)。

<a id="r_a9af8f8bde7f33db3f32aa2aa5bda4012"></a>

```c
#define BT_VS_CMD_BIT_READ_TX_POWER 14
```

相关声明：[BT_VS_CMD_BIT_READ_TX_POWER](#a9af8f8bde7f33db3f32aa2aa5bda4012)。

<a id="r_a6f43e26c34622d9b9b2cf0a6ba53a393"></a>

```c
#define BT_VS_CMD_SUP_FEAT(cmd)
```

相关声明：[BT_VS_CMD_SUP_FEAT](#a6f43e26c34622d9b9b2cf0a6ba53a393)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

<a id="r_af94dd47fba70aa74257db8f711a855dc"></a>

```c
#define BT_VS_CMD_WRITE_BD_ADDR(cmd)
```

相关声明：[BT_VS_CMD_WRITE_BD_ADDR](#af94dd47fba70aa74257db8f711a855dc)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

检查是否支持主机控制器接口厂商特定命令（HCI VS Command）`BT_VS_CMD_BIT_WRITE_BDADDR`。

<a id="r_af5ef90c96d5798cef8ad32f8d6094d53"></a>

```c
#define BT_VS_CMD_READ_STATIC_ADDRS(cmd)
```

相关声明：[BT_VS_CMD_READ_STATIC_ADDRS](#af5ef90c96d5798cef8ad32f8d6094d53)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

<a id="r_aa81a670c17714854306b0044e9fb6392"></a>

```c
#define BT_VS_CMD_READ_KEY_ROOTS(cmd)
```

相关声明：[BT_VS_CMD_READ_KEY_ROOTS](#aa81a670c17714854306b0044e9fb6392)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

<a id="r_a35bf58cbe551d8e3e56fa687828a5ee7"></a>

```c
#define BT_HCI_VS_HW_PLAT_INTEL 0x0001
```

相关声明：[BT_HCI_VS_HW_PLAT_INTEL](#a35bf58cbe551d8e3e56fa687828a5ee7)。

<a id="r_a533362f9e60a77ce5c787d26241a2200"></a>

```c
#define BT_HCI_VS_HW_PLAT_NORDIC 0x0002
```

相关声明：[BT_HCI_VS_HW_PLAT_NORDIC](#a533362f9e60a77ce5c787d26241a2200)。

<a id="r_a0813745772dc53d5eb8d78ca016e0b3c"></a>

```c
#define BT_HCI_VS_HW_PLAT_NXP 0x0003
```

相关声明：[BT_HCI_VS_HW_PLAT_NXP](#a0813745772dc53d5eb8d78ca016e0b3c)。

<a id="r_a30a49f1ddcd9fecb5020d5aa968f49ae"></a>

```c
#define BT_HCI_VS_HW_PLAT_ESPRESSIF 0x0004
```

相关声明：[BT_HCI_VS_HW_PLAT_ESPRESSIF](#a30a49f1ddcd9fecb5020d5aa968f49ae)。

<a id="r_aef40f22484598bcd15885f1cf27a3a7e"></a>

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF51X 0x0001
```

相关声明：[BT_HCI_VS_HW_VAR_NORDIC_NRF51X](#aef40f22484598bcd15885f1cf27a3a7e)。

<a id="r_a990c9b5feb8fa1756d2270127a8909f9"></a>

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF52X 0x0002
```

相关声明：[BT_HCI_VS_HW_VAR_NORDIC_NRF52X](#a990c9b5feb8fa1756d2270127a8909f9)。

<a id="r_a040e6267e8b8cd77db9668f018d9cc83"></a>

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF53X 0x0003
```

相关声明：[BT_HCI_VS_HW_VAR_NORDIC_NRF53X](#a040e6267e8b8cd77db9668f018d9cc83)。

<a id="r_af6d066382f1d824b14d32b2d67f5d353"></a>

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54HX 0x0004
```

相关声明：[BT_HCI_VS_HW_VAR_NORDIC_NRF54HX](#af6d066382f1d824b14d32b2d67f5d353)。

<a id="r_ab88e2f4a0810421cbe017c8c709ace7e"></a>

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54LX 0x0005
```

相关声明：[BT_HCI_VS_HW_VAR_NORDIC_NRF54LX](#ab88e2f4a0810421cbe017c8c709ace7e)。

<a id="r_a5ebfdba9153d1b621c8fda49855229f1"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32 0x0001
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32](#a5ebfdba9153d1b621c8fda49855229f1)。

<a id="r_ad14df70f0f8072d6d6e2808e8ce17a5d"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32S3 0x0002
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32S3](#ad14df70f0f8072d6d6e2808e8ce17a5d)。

<a id="r_ac51b4d7403418958588b73948d9af89e"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32C2 0x0003
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32C2](#ac51b4d7403418958588b73948d9af89e)。

<a id="r_aa48cce481695b93e87b43a723b398a8b"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32C3 0x0004
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32C3](#aa48cce481695b93e87b43a723b398a8b)。

<a id="r_a7404be7bf8919f4301826952b99f6fb8"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32C6 0x0005
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32C6](#a7404be7bf8919f4301826952b99f6fb8)。

<a id="r_a13541361ae8b94189aa1891f7aedf9a1"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32H2 0x0006
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32H2](#a13541361ae8b94189aa1891f7aedf9a1)。

<a id="r_a08f15311c3594c4372644423c37ac6e3"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32C5 0x0007
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32C5](#a08f15311c3594c4372644423c37ac6e3)。

ESP32-C5 硬件变体（Hardware Variant）。

<a id="r_a12238c1f8404d435ad63201808ff934b"></a>

```c
#define BT_HCI_VS_HW_VAR_ESP32C61 0x0008
```

相关声明：[BT_HCI_VS_HW_VAR_ESP32C61](#a12238c1f8404d435ad63201808ff934b)。

ESP32-C61 硬件变体（Hardware Variant）。

<a id="r_ac7e92cbb6a56d20b641be9304372a457"></a>

```c
#define BT_HCI_VS_FW_VAR_STANDARD_CTLR 0x0000
```

相关声明：[BT_HCI_VS_FW_VAR_STANDARD_CTLR](#ac7e92cbb6a56d20b641be9304372a457)。

<a id="r_aa41b3f0e21f47343262aca3648c1f02d"></a>

```c
#define BT_HCI_VS_FW_VAR_VS_CTLR 0x0001
```

相关声明：[BT_HCI_VS_FW_VAR_VS_CTLR](#aa41b3f0e21f47343262aca3648c1f02d)。

<a id="r_a6514cac9da9792697b18a2bf7906aaae"></a>

```c
#define BT_HCI_VS_FW_VAR_FW_LOADER 0x0002
```

相关声明：[BT_HCI_VS_FW_VAR_FW_LOADER](#a6514cac9da9792697b18a2bf7906aaae)。

<a id="r_a551e878d9131dfc94f9a2ac304661e87"></a>

```c
#define BT_HCI_VS_FW_VAR_RESCUE_IMG 0x0003
```

相关声明：[BT_HCI_VS_FW_VAR_RESCUE_IMG](#a551e878d9131dfc94f9a2ac304661e87)。

<a id="r_a7877a1d36a2370abd622eef05cf25795"></a>

```c
#define BT_HCI_OP_VS_READ_VERSION_INFO BT_OP(BT_OGF_VS, 0x0001)
```

相关声明：[BT_HCI_OP_VS_READ_VERSION_INFO](#a7877a1d36a2370abd622eef05cf25795)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_aeb5ac33d62cbd0c1db44a387fe99520c"></a>

```c
#define BT_HCI_OP_VS_READ_SUPPORTED_COMMANDS BT_OP(BT_OGF_VS, 0x0002)
```

相关声明：[BT_HCI_OP_VS_READ_SUPPORTED_COMMANDS](#aeb5ac33d62cbd0c1db44a387fe99520c)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a77537f2ac77e6f4b25b840726899bb8d"></a>

```c
#define BT_HCI_OP_VS_READ_SUPPORTED_FEATURES BT_OP(BT_OGF_VS, 0x0003)
```

相关声明：[BT_HCI_OP_VS_READ_SUPPORTED_FEATURES](#a77537f2ac77e6f4b25b840726899bb8d)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a3d99ba16d2510f12c9b8a7fd7cd6e5e9"></a>

```c
#define BT_HCI_OP_VS_SET_EVENT_MASK BT_OP(BT_OGF_VS, 0x0004)
```

相关声明：[BT_HCI_OP_VS_SET_EVENT_MASK](#a3d99ba16d2510f12c9b8a7fd7cd6e5e9)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a2c47a3d7d4b69e33b5caf5e69ae80abf"></a>

```c
#define BT_HCI_VS_RESET_SOFT 0x00
```

相关声明：[BT_HCI_VS_RESET_SOFT](#a2c47a3d7d4b69e33b5caf5e69ae80abf)。

<a id="r_a50933b6556620154780af3c54ee987a5"></a>

```c
#define BT_HCI_VS_RESET_HARD 0x01
```

相关声明：[BT_HCI_VS_RESET_HARD](#a50933b6556620154780af3c54ee987a5)。

<a id="r_ad3e609f9713edcc0fd5a23fa6042df6d"></a>

```c
#define BT_HCI_OP_VS_RESET BT_OP(BT_OGF_VS, 0x0005)
```

相关声明：[BT_HCI_OP_VS_RESET](#ad3e609f9713edcc0fd5a23fa6042df6d)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a81e2e5d7a5c4def4b86ab7074551c5bf"></a>

```c
#define BT_HCI_OP_VS_WRITE_BD_ADDR BT_OP(BT_OGF_VS, 0x0006)
```

相关声明：[BT_HCI_OP_VS_WRITE_BD_ADDR](#a81e2e5d7a5c4def4b86ab7074551c5bf)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_afd977fec9cc90cc3e3f304dbb181fac4"></a>

```c
#define BT_HCI_VS_TRACE_DISABLED 0x00
```

相关声明：[BT_HCI_VS_TRACE_DISABLED](#afd977fec9cc90cc3e3f304dbb181fac4)。

<a id="r_a22c18b5e3fc458394ef9d20595ff5019"></a>

```c
#define BT_HCI_VS_TRACE_ENABLED 0x01
```

相关声明：[BT_HCI_VS_TRACE_ENABLED](#a22c18b5e3fc458394ef9d20595ff5019)。

<a id="r_a3851c5deb79a1530e448a8cfa0eed2ed"></a>

```c
#define BT_HCI_VS_TRACE_HCI_EVTS 0x00
```

相关声明：[BT_HCI_VS_TRACE_HCI_EVTS](#a3851c5deb79a1530e448a8cfa0eed2ed)。

<a id="r_a72f7e148fe28d21381870f57b30b87e1"></a>

```c
#define BT_HCI_VS_TRACE_VDC 0x01
```

相关声明：[BT_HCI_VS_TRACE_VDC](#a72f7e148fe28d21381870f57b30b87e1)。

<a id="r_a285f127f83f4c241372aa7258b4cad70"></a>

```c
#define BT_HCI_OP_VS_SET_TRACE_ENABLE BT_OP(BT_OGF_VS, 0x0007)
```

相关声明：[BT_HCI_OP_VS_SET_TRACE_ENABLE](#a285f127f83f4c241372aa7258b4cad70)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a6a4f182f0aeeb80e59474f785adda864"></a>

```c
#define BT_HCI_OP_VS_READ_BUILD_INFO BT_OP(BT_OGF_VS, 0x0008)
```

相关声明：[BT_HCI_OP_VS_READ_BUILD_INFO](#a6a4f182f0aeeb80e59474f785adda864)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a0306297daa39e9b73c0953b56ac0fb16"></a>

```c
#define BT_HCI_OP_VS_READ_STATIC_ADDRS BT_OP(BT_OGF_VS, 0x0009)
```

相关声明：[BT_HCI_OP_VS_READ_STATIC_ADDRS](#a0306297daa39e9b73c0953b56ac0fb16)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a11cb133e491f6ed0e796f2cb6cd07731"></a>

```c
#define BT_HCI_OP_VS_READ_KEY_HIERARCHY_ROOTS BT_OP(BT_OGF_VS, 0x000a)
```

相关声明：[BT_HCI_OP_VS_READ_KEY_HIERARCHY_ROOTS](#a11cb133e491f6ed0e796f2cb6cd07731)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_aabf7e4c3ac3b35f22787ad9a448b8220"></a>

```c
#define BT_HCI_OP_VS_READ_CHIP_TEMP BT_OP(BT_OGF_VS, 0x000b)
```

相关声明：[BT_HCI_OP_VS_READ_CHIP_TEMP](#aabf7e4c3ac3b35f22787ad9a448b8220)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a8f9f21d0b193bfdd1e4d1a98b4a96f04"></a>

```c
#define BT_HCI_VS_VID_ANDROID 0x0001
```

相关声明：[BT_HCI_VS_VID_ANDROID](#a8f9f21d0b193bfdd1e4d1a98b4a96f04)。

<a id="r_ab028da372f594f1e698335c3f083bd7f"></a>

```c
#define BT_HCI_VS_VID_MICROSOFT 0x0002
```

相关声明：[BT_HCI_VS_VID_MICROSOFT](#ab028da372f594f1e698335c3f083bd7f)。

<a id="r_a33eb32eabc404d0a73a0b75523210778"></a>

```c
#define BT_HCI_OP_VS_READ_HOST_STACK_CMDS BT_OP(BT_OGF_VS, 0x000c)
```

相关声明：[BT_HCI_OP_VS_READ_HOST_STACK_CMDS](#a33eb32eabc404d0a73a0b75523210778)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a4025336d067b79bead25b45de0ed33cf"></a>

```c
#define BT_HCI_VS_SCAN_REQ_REPORTS_DISABLED 0x00
```

相关声明：[BT_HCI_VS_SCAN_REQ_REPORTS_DISABLED](#a4025336d067b79bead25b45de0ed33cf)。

<a id="r_a7be2294229731b3a004788a739d6f616"></a>

```c
#define BT_HCI_VS_SCAN_REQ_REPORTS_ENABLED 0x01
```

相关声明：[BT_HCI_VS_SCAN_REQ_REPORTS_ENABLED](#a7be2294229731b3a004788a739d6f616)。

<a id="r_ac1e36447ba26e70b4a95073e200cc549"></a>

```c
#define BT_HCI_OP_VS_SET_SCAN_REQ_REPORTS BT_OP(BT_OGF_VS, 0x000d)
```

相关声明：[BT_HCI_OP_VS_SET_SCAN_REQ_REPORTS](#ac1e36447ba26e70b4a95073e200cc549)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a1f0308641bb308088c49ca241d1293a8"></a>

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_ADV 0x00
```

相关声明：[BT_HCI_VS_LL_HANDLE_TYPE_ADV](#a1f0308641bb308088c49ca241d1293a8)。

<a id="r_a36e1663258f24c7f5ea8235efcb8b1f6"></a>

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_SCAN 0x01
```

相关声明：[BT_HCI_VS_LL_HANDLE_TYPE_SCAN](#a36e1663258f24c7f5ea8235efcb8b1f6)。

<a id="r_a9ae772dcf1042953552a44c41d41f3e9"></a>

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_CONN 0x02
```

相关声明：[BT_HCI_VS_LL_HANDLE_TYPE_CONN](#a9ae772dcf1042953552a44c41d41f3e9)。

<a id="r_a17d4ed99163918297a67a4c00de38728"></a>

```c
#define BT_HCI_VS_LL_TX_POWER_LEVEL_NO_PREF 0x7F
```

相关声明：[BT_HCI_VS_LL_TX_POWER_LEVEL_NO_PREF](#a17d4ed99163918297a67a4c00de38728)。

<a id="r_a29b5fda3541bfd8d69db72e46688d180"></a>

```c
#define BT_HCI_OP_VS_WRITE_TX_POWER_LEVEL BT_OP(BT_OGF_VS, 0x000e)
```

相关声明：[BT_HCI_OP_VS_WRITE_TX_POWER_LEVEL](#a29b5fda3541bfd8d69db72e46688d180)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_ad18fb75b6b25758cec63ea30ada16394"></a>

```c
#define BT_HCI_OP_VS_READ_TX_POWER_LEVEL BT_OP(BT_OGF_VS, 0x000f)
```

相关声明：[BT_HCI_OP_VS_READ_TX_POWER_LEVEL](#ad18fb75b6b25758cec63ea30ada16394)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_ae51d60b72e66a4eae8e5d608e0ab339b"></a>

```c
#define BT_HCI_OP_VS_READ_USB_TRANSPORT_MODE BT_OP(BT_OGF_VS, 0x0010)
```

相关声明：[BT_HCI_OP_VS_READ_USB_TRANSPORT_MODE](#ae51d60b72e66a4eae8e5d608e0ab339b)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a86badb7e68535ef6d741e03c63811578"></a>

```c
#define BT_HCI_VS_USB_H2_MODE 0x00
```

相关声明：[BT_HCI_VS_USB_H2_MODE](#a86badb7e68535ef6d741e03c63811578)。

<a id="r_a758ccb4c0f666df106f550af15025e02"></a>

```c
#define BT_HCI_VS_USB_H4_MODE 0x01
```

相关声明：[BT_HCI_VS_USB_H4_MODE](#a758ccb4c0f666df106f550af15025e02)。

<a id="r_adcf0e45c997c88301a5f4ba9240eb071"></a>

```c
#define BT_HCI_OP_VS_SET_USB_TRANSPORT_MODE BT_OP(BT_OGF_VS, 0x0011)
```

相关声明：[BT_HCI_OP_VS_SET_USB_TRANSPORT_MODE](#adcf0e45c997c88301a5f4ba9240eb071)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a6c499204a11f76fe28cc88df665f4af0"></a>

```c
#define BT_HCI_OP_VS_SET_MIN_NUM_USED_CHANS BT_OP(BT_OGF_VS, 0x0012)
```

相关声明：[BT_HCI_OP_VS_SET_MIN_NUM_USED_CHANS](#a6c499204a11f76fe28cc88df665f4af0)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a20356ed318eead6aab20ef19b6d7c0df"></a>

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_STACK_FRAME 0x01
```

相关声明：[BT_HCI_EVT_VS_ERROR_DATA_TYPE_STACK_FRAME](#a20356ed318eead6aab20ef19b6d7c0df)。

<a id="r_ae9900729ac120c6fb68314b1e0984516"></a>

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_CTRL_ASSERT 0x02
```

相关声明：[BT_HCI_EVT_VS_ERROR_DATA_TYPE_CTRL_ASSERT](#ae9900729ac120c6fb68314b1e0984516)。

<a id="r_a7ed9dbedd215a7ed4b040b6486d49b98"></a>

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_TRACE 0x03
```

相关声明：[BT_HCI_EVT_VS_ERROR_DATA_TYPE_TRACE](#a7ed9dbedd215a7ed4b040b6486d49b98)。

<a id="r_a36a880f6a4f53465f38f70387b52b006"></a>

```c
#define BT_HCI_EVT_VS_ERROR_CPU_TYPE_CORTEX_M 0x01
```

相关声明：[BT_HCI_EVT_VS_ERROR_CPU_TYPE_CORTEX_M](#a36a880f6a4f53465f38f70387b52b006)。

<a id="r_aa56a360e3cdf72fc87216685179edd41"></a>

```c
#define BT_HCI_VS_TRACE_LMP_TX 0x01
```

相关声明：[BT_HCI_VS_TRACE_LMP_TX](#aa56a360e3cdf72fc87216685179edd41)。

<a id="r_aa27a4038be1c6e9cfb756e78d9b07df9"></a>

```c
#define BT_HCI_VS_TRACE_LMP_RX 0x02
```

相关声明：[BT_HCI_VS_TRACE_LMP_RX](#aa27a4038be1c6e9cfb756e78d9b07df9)。

<a id="r_a4a212cd52bdd9343bdab8d27ae5d650e"></a>

```c
#define BT_HCI_VS_TRACE_LLCP_TX 0x03
```

相关声明：[BT_HCI_VS_TRACE_LLCP_TX](#a4a212cd52bdd9343bdab8d27ae5d650e)。

<a id="r_a2c69ab6f964ed5cd95419a9771363b64"></a>

```c
#define BT_HCI_VS_TRACE_LLCP_RX 0x04
```

相关声明：[BT_HCI_VS_TRACE_LLCP_RX](#a2c69ab6f964ed5cd95419a9771363b64)。

<a id="r_affed427819b721735e31fbcc52f40b5f"></a>

```c
#define BT_HCI_VS_TRACE_LE_CONN_IND 0x05
```

相关声明：[BT_HCI_VS_TRACE_LE_CONN_IND](#affed427819b721735e31fbcc52f40b5f)。

<a id="r_a43dd9ebf0a175aa0bc244f99df278344"></a>

```c
#define BT_HCI_EVT_VS_TRACE_INFO 0x03
```

相关声明：[BT_HCI_EVT_VS_TRACE_INFO](#a43dd9ebf0a175aa0bc244f99df278344)。

<a id="r_ac4fae4567bb2ba2866ed24ccfc328f63"></a>

```c
#define BT_HCI_EVT_VS_SCAN_REQ_RX 0x04
```

相关声明：[BT_HCI_EVT_VS_SCAN_REQ_RX](#ac4fae4567bb2ba2866ed24ccfc328f63)。

<a id="r_a8b0ced9392cbf33794100794f964d53f"></a>

```c
#define BT_HCI_EVT_VS_LE_CONNECTIONLESS_IQ_REPORT 0x5
```

相关声明：[BT_HCI_EVT_VS_LE_CONNECTIONLESS_IQ_REPORT](#a8b0ced9392cbf33794100794f964d53f)。

<a id="r_a71d87ba67638aca600ebbe615a0d4122"></a>

```c
#define BT_HCI_VS_LE_CTE_REPORT_NO_VALID_SAMPLE 0x8000
```

相关声明：[BT_HCI_VS_LE_CTE_REPORT_NO_VALID_SAMPLE](#a71d87ba67638aca600ebbe615a0d4122)。

<a id="r_a6066be0390be7f611e0e3f4bfab030df"></a>

```c
#define BT_HCI_EVT_VS_LE_CONNECTION_IQ_REPORT 0x6
```

相关声明：[BT_HCI_EVT_VS_LE_CONNECTION_IQ_REPORT](#a6066be0390be7f611e0e3f4bfab030df)。

<a id="r_a365da8f1041d55948caa4bf60ea349bd"></a>

```c
#define BT_EVT_MASK_VS_FATAL_ERROR BT_EVT_BIT(1)
```

相关声明：[BT_EVT_MASK_VS_FATAL_ERROR](#a365da8f1041d55948caa4bf60ea349bd)、[BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)。

<a id="r_aae4f865bf37b8933de070e16ea3047ec"></a>

```c
#define BT_EVT_MASK_VS_TRACE_INFO BT_EVT_BIT(2)
```

相关声明：[BT_EVT_MASK_VS_TRACE_INFO](#aae4f865bf37b8933de070e16ea3047ec)、[BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)。

<a id="r_a9b4fcdd0de4197b3eb1ac65602e30408"></a>

```c
#define BT_EVT_MASK_VS_SCAN_REQ_RX BT_EVT_BIT(3)
```

相关声明：[BT_EVT_MASK_VS_SCAN_REQ_RX](#a9b4fcdd0de4197b3eb1ac65602e30408)、[BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)。

<a id="r_a74d2cf07f64f35318ec4ba24fd570dff"></a>

```c
#define BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT BT_EVT_BIT(4)
```

相关声明：[BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT](#a74d2cf07f64f35318ec4ba24fd570dff)、[BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)。

<a id="r_a3971e9541300e12abb4ff36679d9b1f1"></a>

```c
#define BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT BT_EVT_BIT(5)
```

相关声明：[BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT](#a3971e9541300e12abb4ff36679d9b1f1)、[BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)。

<a id="r_a2f8e8f0070bde0e62019c71cc343fbe6"></a>

```c
#define DEFAULT_VS_EVT_MASK
```

相关声明：[DEFAULT_VS_EVT_MASK](#a2f8e8f0070bde0e62019c71cc343fbe6)。

<a id="r_aeb5fdec34a0dfbf5d56a1aa42ba53318"></a>

```c
#define BT_HCI_MESH_REVISION 0x01
```

相关声明：[BT_HCI_MESH_REVISION](#aeb5fdec34a0dfbf5d56a1aa42ba53318)。

<a id="r_ad03814f2ae0c377234c5a340388b6ad1"></a>

```c
#define BT_HCI_OP_VS_MESH BT_OP(BT_OGF_VS, 0x0042)
```

相关声明：[BT_HCI_OP_VS_MESH](#ad03814f2ae0c377234c5a340388b6ad1)、[BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)、[BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)。

<a id="r_a4817a57b69eda704a5a85198aa734792"></a>

```c
#define BT_HCI_MESH_EVT_PREFIX 0xF0
```

相关声明：[BT_HCI_MESH_EVT_PREFIX](#a4817a57b69eda704a5a85198aa734792)。

<a id="r_af4cbb4f987c728312a0d00bea62db1c6"></a>

```c
#define BT_HCI_OC_MESH_GET_OPTS 0x00
```

相关声明：[BT_HCI_OC_MESH_GET_OPTS](#af4cbb4f987c728312a0d00bea62db1c6)。

<a id="r_aa31c2257092c0fdce4865ad5af1031ad"></a>

```c
#define BT_HCI_MESH_PATTERN_LEN_MAX 0x0f
```

相关声明：[BT_HCI_MESH_PATTERN_LEN_MAX](#aa31c2257092c0fdce4865ad5af1031ad)。

<a id="r_af22f7e03d43595b10ebb6b2cfbe26540"></a>

```c
#define BT_HCI_OC_MESH_SET_SCAN_FILTER 0x01
```

相关声明：[BT_HCI_OC_MESH_SET_SCAN_FILTER](#af22f7e03d43595b10ebb6b2cfbe26540)。

<a id="r_ac73a04914ed07491fde6d463d111a9e2"></a>

```c
#define BT_HCI_OC_MESH_ADVERTISE 0x02
```

相关声明：[BT_HCI_OC_MESH_ADVERTISE](#ac73a04914ed07491fde6d463d111a9e2)。

<a id="r_a9f894b55f3db9df8bb2f710eb736ef1a"></a>

```c
#define BT_HCI_OC_MESH_ADVERTISE_TIMED 0x03
```

相关声明：[BT_HCI_OC_MESH_ADVERTISE_TIMED](#a9f894b55f3db9df8bb2f710eb736ef1a)。

<a id="r_a02491eb40b1874b4fdfb9eac5c3520c0"></a>

```c
#define BT_HCI_OC_MESH_ADVERTISE_CANCEL 0x04
```

相关声明：[BT_HCI_OC_MESH_ADVERTISE_CANCEL](#a02491eb40b1874b4fdfb9eac5c3520c0)。

<a id="r_a4225e58654df90330fe007a8e99f4bdb"></a>

```c
#define BT_HCI_OC_MESH_SET_SCANNING 0x05
```

相关声明：[BT_HCI_OC_MESH_SET_SCANNING](#a4225e58654df90330fe007a8e99f4bdb)。

<a id="r_af6e0159b30b73f3bbe8f5df7cdad8ef6"></a>

```c
#define BT_HCI_EVT_MESH_ADV_COMPLETE 0x00
```

相关声明：[BT_HCI_EVT_MESH_ADV_COMPLETE](#af6e0159b30b73f3bbe8f5df7cdad8ef6)。

<a id="r_a77e3ea0a8f95449a11e4119c30313fe9"></a>

```c
#define BT_HCI_EVT_MESH_SCANNING_REPORT 0x01
```

相关声明：[BT_HCI_EVT_MESH_SCANNING_REPORT](#a77e3ea0a8f95449a11e4119c30313fe9)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_aa90c2106bbb977f1ea8532212ff01b4d"></a>

```c
struct net_buf * hci_vs_err_stack_frame (unsigned int reason, const struct arch_esf *esf)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[hci_vs_err_stack_frame](#aa90c2106bbb977f1ea8532212ff01b4d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a9a91c493cc947492d5a172a15abe9a4e"></a>

```c
struct net_buf * hci_vs_err_trace (const char *file, uint32_t line, uint64_t pc)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[hci_vs_err_trace](#a9a91c493cc947492d5a172a15abe9a4e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

<a id="r_afc9ea0e4f2260bf59336f2c66532d9b1"></a>

```c
struct net_buf * hci_vs_err_assert (const char *file, uint32_t line)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[hci_vs_err_assert](#afc9ea0e4f2260bf59336f2c66532d9b1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

## 17.4\_详细说明（Detailed Documentation）

<a id="a365da8f1041d55948caa4bf60ea349bd"></a>

### `BT_EVT_MASK_VS_FATAL_ERROR`

```c
#define BT_EVT_MASK_VS_FATAL_ERROR BT_EVT_BIT(1)
```

<a id="a3971e9541300e12abb4ff36679d9b1f1"></a>

### `BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT`

```c
#define BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT BT_EVT_BIT(5)
```

<a id="a74d2cf07f64f35318ec4ba24fd570dff"></a>

### `BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT`

```c
#define BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT BT_EVT_BIT(4)
```

<a id="a9b4fcdd0de4197b3eb1ac65602e30408"></a>

### `BT_EVT_MASK_VS_SCAN_REQ_RX`

```c
#define BT_EVT_MASK_VS_SCAN_REQ_RX BT_EVT_BIT(3)
```

<a id="aae4f865bf37b8933de070e16ea3047ec"></a>

### `BT_EVT_MASK_VS_TRACE_INFO`

```c
#define BT_EVT_MASK_VS_TRACE_INFO BT_EVT_BIT(2)
```

<a id="af6e0159b30b73f3bbe8f5df7cdad8ef6"></a>

### `BT_HCI_EVT_MESH_ADV_COMPLETE`

```c
#define BT_HCI_EVT_MESH_ADV_COMPLETE 0x00
```

<a id="a77e3ea0a8f95449a11e4119c30313fe9"></a>

### `BT_HCI_EVT_MESH_SCANNING_REPORT`

```c
#define BT_HCI_EVT_MESH_SCANNING_REPORT 0x01
```

<a id="a36a880f6a4f53465f38f70387b52b006"></a>

### `BT_HCI_EVT_VS_ERROR_CPU_TYPE_CORTEX_M`

```c
#define BT_HCI_EVT_VS_ERROR_CPU_TYPE_CORTEX_M 0x01
```

<a id="ae9900729ac120c6fb68314b1e0984516"></a>

### `BT_HCI_EVT_VS_ERROR_DATA_TYPE_CTRL_ASSERT`

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_CTRL_ASSERT 0x02
```

<a id="a20356ed318eead6aab20ef19b6d7c0df"></a>

### `BT_HCI_EVT_VS_ERROR_DATA_TYPE_STACK_FRAME`

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_STACK_FRAME 0x01
```

<a id="a7ed9dbedd215a7ed4b040b6486d49b98"></a>

### `BT_HCI_EVT_VS_ERROR_DATA_TYPE_TRACE`

```c
#define BT_HCI_EVT_VS_ERROR_DATA_TYPE_TRACE 0x03
```

<a id="a6066be0390be7f611e0e3f4bfab030df"></a>

### `BT_HCI_EVT_VS_LE_CONNECTION_IQ_REPORT`

```c
#define BT_HCI_EVT_VS_LE_CONNECTION_IQ_REPORT 0x6
```

<a id="a8b0ced9392cbf33794100794f964d53f"></a>

### `BT_HCI_EVT_VS_LE_CONNECTIONLESS_IQ_REPORT`

```c
#define BT_HCI_EVT_VS_LE_CONNECTIONLESS_IQ_REPORT 0x5
```

<a id="ac4fae4567bb2ba2866ed24ccfc328f63"></a>

### `BT_HCI_EVT_VS_SCAN_REQ_RX`

```c
#define BT_HCI_EVT_VS_SCAN_REQ_RX 0x04
```

<a id="a43dd9ebf0a175aa0bc244f99df278344"></a>

### `BT_HCI_EVT_VS_TRACE_INFO`

```c
#define BT_HCI_EVT_VS_TRACE_INFO 0x03
```

<a id="a4817a57b69eda704a5a85198aa734792"></a>

### `BT_HCI_MESH_EVT_PREFIX`

```c
#define BT_HCI_MESH_EVT_PREFIX 0xF0
```

<a id="aa31c2257092c0fdce4865ad5af1031ad"></a>

### `BT_HCI_MESH_PATTERN_LEN_MAX`

```c
#define BT_HCI_MESH_PATTERN_LEN_MAX 0x0f
```

<a id="aeb5fdec34a0dfbf5d56a1aa42ba53318"></a>

### `BT_HCI_MESH_REVISION`

```c
#define BT_HCI_MESH_REVISION 0x01
```

<a id="ac73a04914ed07491fde6d463d111a9e2"></a>

### `BT_HCI_OC_MESH_ADVERTISE`

```c
#define BT_HCI_OC_MESH_ADVERTISE 0x02
```

<a id="a02491eb40b1874b4fdfb9eac5c3520c0"></a>

### `BT_HCI_OC_MESH_ADVERTISE_CANCEL`

```c
#define BT_HCI_OC_MESH_ADVERTISE_CANCEL 0x04
```

<a id="a9f894b55f3db9df8bb2f710eb736ef1a"></a>

### `BT_HCI_OC_MESH_ADVERTISE_TIMED`

```c
#define BT_HCI_OC_MESH_ADVERTISE_TIMED 0x03
```

<a id="af4cbb4f987c728312a0d00bea62db1c6"></a>

### `BT_HCI_OC_MESH_GET_OPTS`

```c
#define BT_HCI_OC_MESH_GET_OPTS 0x00
```

<a id="af22f7e03d43595b10ebb6b2cfbe26540"></a>

### `BT_HCI_OC_MESH_SET_SCAN_FILTER`

```c
#define BT_HCI_OC_MESH_SET_SCAN_FILTER 0x01
```

<a id="a4225e58654df90330fe007a8e99f4bdb"></a>

### `BT_HCI_OC_MESH_SET_SCANNING`

```c
#define BT_HCI_OC_MESH_SET_SCANNING 0x05
```

<a id="ad03814f2ae0c377234c5a340388b6ad1"></a>

### `BT_HCI_OP_VS_MESH`

```c
#define BT_HCI_OP_VS_MESH BT_OP(BT_OGF_VS, 0x0042)
```

<a id="a6a4f182f0aeeb80e59474f785adda864"></a>

### `BT_HCI_OP_VS_READ_BUILD_INFO`

```c
#define BT_HCI_OP_VS_READ_BUILD_INFO BT_OP(BT_OGF_VS, 0x0008)
```

<a id="aabf7e4c3ac3b35f22787ad9a448b8220"></a>

### `BT_HCI_OP_VS_READ_CHIP_TEMP`

```c
#define BT_HCI_OP_VS_READ_CHIP_TEMP BT_OP(BT_OGF_VS, 0x000b)
```

<a id="a33eb32eabc404d0a73a0b75523210778"></a>

### `BT_HCI_OP_VS_READ_HOST_STACK_CMDS`

```c
#define BT_HCI_OP_VS_READ_HOST_STACK_CMDS BT_OP(BT_OGF_VS, 0x000c)
```

<a id="a11cb133e491f6ed0e796f2cb6cd07731"></a>

### `BT_HCI_OP_VS_READ_KEY_HIERARCHY_ROOTS`

```c
#define BT_HCI_OP_VS_READ_KEY_HIERARCHY_ROOTS BT_OP(BT_OGF_VS, 0x000a)
```

<a id="a0306297daa39e9b73c0953b56ac0fb16"></a>

### `BT_HCI_OP_VS_READ_STATIC_ADDRS`

```c
#define BT_HCI_OP_VS_READ_STATIC_ADDRS BT_OP(BT_OGF_VS, 0x0009)
```

<a id="aeb5ac33d62cbd0c1db44a387fe99520c"></a>

### `BT_HCI_OP_VS_READ_SUPPORTED_COMMANDS`

```c
#define BT_HCI_OP_VS_READ_SUPPORTED_COMMANDS BT_OP(BT_OGF_VS, 0x0002)
```

<a id="a77537f2ac77e6f4b25b840726899bb8d"></a>

### `BT_HCI_OP_VS_READ_SUPPORTED_FEATURES`

```c
#define BT_HCI_OP_VS_READ_SUPPORTED_FEATURES BT_OP(BT_OGF_VS, 0x0003)
```

<a id="ad18fb75b6b25758cec63ea30ada16394"></a>

### `BT_HCI_OP_VS_READ_TX_POWER_LEVEL`

```c
#define BT_HCI_OP_VS_READ_TX_POWER_LEVEL BT_OP(BT_OGF_VS, 0x000f)
```

<a id="ae51d60b72e66a4eae8e5d608e0ab339b"></a>

### `BT_HCI_OP_VS_READ_USB_TRANSPORT_MODE`

```c
#define BT_HCI_OP_VS_READ_USB_TRANSPORT_MODE BT_OP(BT_OGF_VS, 0x0010)
```

<a id="a7877a1d36a2370abd622eef05cf25795"></a>

### `BT_HCI_OP_VS_READ_VERSION_INFO`

```c
#define BT_HCI_OP_VS_READ_VERSION_INFO BT_OP(BT_OGF_VS, 0x0001)
```

<a id="ad3e609f9713edcc0fd5a23fa6042df6d"></a>

### `BT_HCI_OP_VS_RESET`

```c
#define BT_HCI_OP_VS_RESET BT_OP(BT_OGF_VS, 0x0005)
```

<a id="a3d99ba16d2510f12c9b8a7fd7cd6e5e9"></a>

### `BT_HCI_OP_VS_SET_EVENT_MASK`

```c
#define BT_HCI_OP_VS_SET_EVENT_MASK BT_OP(BT_OGF_VS, 0x0004)
```

<a id="a6c499204a11f76fe28cc88df665f4af0"></a>

### `BT_HCI_OP_VS_SET_MIN_NUM_USED_CHANS`

```c
#define BT_HCI_OP_VS_SET_MIN_NUM_USED_CHANS BT_OP(BT_OGF_VS, 0x0012)
```

<a id="ac1e36447ba26e70b4a95073e200cc549"></a>

### `BT_HCI_OP_VS_SET_SCAN_REQ_REPORTS`

```c
#define BT_HCI_OP_VS_SET_SCAN_REQ_REPORTS BT_OP(BT_OGF_VS, 0x000d)
```

<a id="a285f127f83f4c241372aa7258b4cad70"></a>

### `BT_HCI_OP_VS_SET_TRACE_ENABLE`

```c
#define BT_HCI_OP_VS_SET_TRACE_ENABLE BT_OP(BT_OGF_VS, 0x0007)
```

<a id="adcf0e45c997c88301a5f4ba9240eb071"></a>

### `BT_HCI_OP_VS_SET_USB_TRANSPORT_MODE`

```c
#define BT_HCI_OP_VS_SET_USB_TRANSPORT_MODE BT_OP(BT_OGF_VS, 0x0011)
```

<a id="a81e2e5d7a5c4def4b86ab7074551c5bf"></a>

### `BT_HCI_OP_VS_WRITE_BD_ADDR`

```c
#define BT_HCI_OP_VS_WRITE_BD_ADDR BT_OP(BT_OGF_VS, 0x0006)
```

<a id="a29b5fda3541bfd8d69db72e46688d180"></a>

### `BT_HCI_OP_VS_WRITE_TX_POWER_LEVEL`

```c
#define BT_HCI_OP_VS_WRITE_TX_POWER_LEVEL BT_OP(BT_OGF_VS, 0x000e)
```

<a id="a6514cac9da9792697b18a2bf7906aaae"></a>

### `BT_HCI_VS_FW_VAR_FW_LOADER`

```c
#define BT_HCI_VS_FW_VAR_FW_LOADER 0x0002
```

<a id="a551e878d9131dfc94f9a2ac304661e87"></a>

### `BT_HCI_VS_FW_VAR_RESCUE_IMG`

```c
#define BT_HCI_VS_FW_VAR_RESCUE_IMG 0x0003
```

<a id="ac7e92cbb6a56d20b641be9304372a457"></a>

### `BT_HCI_VS_FW_VAR_STANDARD_CTLR`

```c
#define BT_HCI_VS_FW_VAR_STANDARD_CTLR 0x0000
```

<a id="aa41b3f0e21f47343262aca3648c1f02d"></a>

### `BT_HCI_VS_FW_VAR_VS_CTLR`

```c
#define BT_HCI_VS_FW_VAR_VS_CTLR 0x0001
```

<a id="a30a49f1ddcd9fecb5020d5aa968f49ae"></a>

### `BT_HCI_VS_HW_PLAT_ESPRESSIF`

```c
#define BT_HCI_VS_HW_PLAT_ESPRESSIF 0x0004
```

<a id="a35bf58cbe551d8e3e56fa687828a5ee7"></a>

### `BT_HCI_VS_HW_PLAT_INTEL`

```c
#define BT_HCI_VS_HW_PLAT_INTEL 0x0001
```

<a id="a533362f9e60a77ce5c787d26241a2200"></a>

### `BT_HCI_VS_HW_PLAT_NORDIC`

```c
#define BT_HCI_VS_HW_PLAT_NORDIC 0x0002
```

<a id="a0813745772dc53d5eb8d78ca016e0b3c"></a>

### `BT_HCI_VS_HW_PLAT_NXP`

```c
#define BT_HCI_VS_HW_PLAT_NXP 0x0003
```

<a id="a5ebfdba9153d1b621c8fda49855229f1"></a>

### `BT_HCI_VS_HW_VAR_ESP32`

```c
#define BT_HCI_VS_HW_VAR_ESP32 0x0001
```

<a id="ac51b4d7403418958588b73948d9af89e"></a>

### `BT_HCI_VS_HW_VAR_ESP32C2`

```c
#define BT_HCI_VS_HW_VAR_ESP32C2 0x0003
```

<a id="aa48cce481695b93e87b43a723b398a8b"></a>

### `BT_HCI_VS_HW_VAR_ESP32C3`

```c
#define BT_HCI_VS_HW_VAR_ESP32C3 0x0004
```

<a id="a08f15311c3594c4372644423c37ac6e3"></a>

### `BT_HCI_VS_HW_VAR_ESP32C5`

```c
#define BT_HCI_VS_HW_VAR_ESP32C5 0x0007
```

ESP32-C5 硬件变体（Hardware Variant）。

<a id="a7404be7bf8919f4301826952b99f6fb8"></a>

### `BT_HCI_VS_HW_VAR_ESP32C6`

```c
#define BT_HCI_VS_HW_VAR_ESP32C6 0x0005
```

<a id="a12238c1f8404d435ad63201808ff934b"></a>

### `BT_HCI_VS_HW_VAR_ESP32C61`

```c
#define BT_HCI_VS_HW_VAR_ESP32C61 0x0008
```

ESP32-C61 硬件变体（Hardware Variant）。

<a id="a13541361ae8b94189aa1891f7aedf9a1"></a>

### `BT_HCI_VS_HW_VAR_ESP32H2`

```c
#define BT_HCI_VS_HW_VAR_ESP32H2 0x0006
```

<a id="ad14df70f0f8072d6d6e2808e8ce17a5d"></a>

### `BT_HCI_VS_HW_VAR_ESP32S3`

```c
#define BT_HCI_VS_HW_VAR_ESP32S3 0x0002
```

<a id="aef40f22484598bcd15885f1cf27a3a7e"></a>

### `BT_HCI_VS_HW_VAR_NORDIC_NRF51X`

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF51X 0x0001
```

<a id="a990c9b5feb8fa1756d2270127a8909f9"></a>

### `BT_HCI_VS_HW_VAR_NORDIC_NRF52X`

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF52X 0x0002
```

<a id="a040e6267e8b8cd77db9668f018d9cc83"></a>

### `BT_HCI_VS_HW_VAR_NORDIC_NRF53X`

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF53X 0x0003
```

<a id="af6d066382f1d824b14d32b2d67f5d353"></a>

### `BT_HCI_VS_HW_VAR_NORDIC_NRF54HX`

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54HX 0x0004
```

<a id="ab88e2f4a0810421cbe017c8c709ace7e"></a>

### `BT_HCI_VS_HW_VAR_NORDIC_NRF54LX`

```c
#define BT_HCI_VS_HW_VAR_NORDIC_NRF54LX 0x0005
```

<a id="a71d87ba67638aca600ebbe615a0d4122"></a>

### `BT_HCI_VS_LE_CTE_REPORT_NO_VALID_SAMPLE`

```c
#define BT_HCI_VS_LE_CTE_REPORT_NO_VALID_SAMPLE 0x8000
```

<a id="a1f0308641bb308088c49ca241d1293a8"></a>

### `BT_HCI_VS_LL_HANDLE_TYPE_ADV`

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_ADV 0x00
```

<a id="a9ae772dcf1042953552a44c41d41f3e9"></a>

### `BT_HCI_VS_LL_HANDLE_TYPE_CONN`

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_CONN 0x02
```

<a id="a36e1663258f24c7f5ea8235efcb8b1f6"></a>

### `BT_HCI_VS_LL_HANDLE_TYPE_SCAN`

```c
#define BT_HCI_VS_LL_HANDLE_TYPE_SCAN 0x01
```

<a id="a17d4ed99163918297a67a4c00de38728"></a>

### `BT_HCI_VS_LL_TX_POWER_LEVEL_NO_PREF`

```c
#define BT_HCI_VS_LL_TX_POWER_LEVEL_NO_PREF 0x7F
```

<a id="a50933b6556620154780af3c54ee987a5"></a>

### `BT_HCI_VS_RESET_HARD`

```c
#define BT_HCI_VS_RESET_HARD 0x01
```

<a id="a2c47a3d7d4b69e33b5caf5e69ae80abf"></a>

### `BT_HCI_VS_RESET_SOFT`

```c
#define BT_HCI_VS_RESET_SOFT 0x00
```

<a id="a4025336d067b79bead25b45de0ed33cf"></a>

### `BT_HCI_VS_SCAN_REQ_REPORTS_DISABLED`

```c
#define BT_HCI_VS_SCAN_REQ_REPORTS_DISABLED 0x00
```

<a id="a7be2294229731b3a004788a739d6f616"></a>

### `BT_HCI_VS_SCAN_REQ_REPORTS_ENABLED`

```c
#define BT_HCI_VS_SCAN_REQ_REPORTS_ENABLED 0x01
```

<a id="afd977fec9cc90cc3e3f304dbb181fac4"></a>

### `BT_HCI_VS_TRACE_DISABLED`

```c
#define BT_HCI_VS_TRACE_DISABLED 0x00
```

<a id="a22c18b5e3fc458394ef9d20595ff5019"></a>

### `BT_HCI_VS_TRACE_ENABLED`

```c
#define BT_HCI_VS_TRACE_ENABLED 0x01
```

<a id="a3851c5deb79a1530e448a8cfa0eed2ed"></a>

### `BT_HCI_VS_TRACE_HCI_EVTS`

```c
#define BT_HCI_VS_TRACE_HCI_EVTS 0x00
```

<a id="affed427819b721735e31fbcc52f40b5f"></a>

### `BT_HCI_VS_TRACE_LE_CONN_IND`

```c
#define BT_HCI_VS_TRACE_LE_CONN_IND 0x05
```

<a id="a2c69ab6f964ed5cd95419a9771363b64"></a>

### `BT_HCI_VS_TRACE_LLCP_RX`

```c
#define BT_HCI_VS_TRACE_LLCP_RX 0x04
```

<a id="a4a212cd52bdd9343bdab8d27ae5d650e"></a>

### `BT_HCI_VS_TRACE_LLCP_TX`

```c
#define BT_HCI_VS_TRACE_LLCP_TX 0x03
```

<a id="aa27a4038be1c6e9cfb756e78d9b07df9"></a>

### `BT_HCI_VS_TRACE_LMP_RX`

```c
#define BT_HCI_VS_TRACE_LMP_RX 0x02
```

<a id="aa56a360e3cdf72fc87216685179edd41"></a>

### `BT_HCI_VS_TRACE_LMP_TX`

```c
#define BT_HCI_VS_TRACE_LMP_TX 0x01
```

<a id="a72f7e148fe28d21381870f57b30b87e1"></a>

### `BT_HCI_VS_TRACE_VDC`

```c
#define BT_HCI_VS_TRACE_VDC 0x01
```

<a id="a86badb7e68535ef6d741e03c63811578"></a>

### `BT_HCI_VS_USB_H2_MODE`

```c
#define BT_HCI_VS_USB_H2_MODE 0x00
```

<a id="a758ccb4c0f666df106f550af15025e02"></a>

### `BT_HCI_VS_USB_H4_MODE`

```c
#define BT_HCI_VS_USB_H4_MODE 0x01
```

<a id="a8f9f21d0b193bfdd1e4d1a98b4a96f04"></a>

### `BT_HCI_VS_VID_ANDROID`

```c
#define BT_HCI_VS_VID_ANDROID 0x0001
```

<a id="ab028da372f594f1e698335c3f083bd7f"></a>

### `BT_HCI_VS_VID_MICROSOFT`

```c
#define BT_HCI_VS_VID_MICROSOFT 0x0002
```

<a id="aaae2460cf69b0ad51aedf57c72d42103"></a>

### `BT_VS_CMD_BIT_READ_BUILD_INFO`

```c
#define BT_VS_CMD_BIT_READ_BUILD_INFO 7
```

<a id="a96cee049fdf09d1e22aa2204a080c956"></a>

### `BT_VS_CMD_BIT_READ_CHIP_TEMP`

```c
#define BT_VS_CMD_BIT_READ_CHIP_TEMP 10
```

<a id="a072226e7bfd637f71a03971e18d795e5"></a>

### `BT_VS_CMD_BIT_READ_HOST_STACK_CMD`

```c
#define BT_VS_CMD_BIT_READ_HOST_STACK_CMD 11
```

<a id="aa8b39f4ac968cf0cdb18073de1aa1ad5"></a>

### `BT_VS_CMD_BIT_READ_KEY_ROOTS`

```c
#define BT_VS_CMD_BIT_READ_KEY_ROOTS 9
```

<a id="a27e19ec90e057244db7f632887a46ec1"></a>

### `BT_VS_CMD_BIT_READ_STATIC_ADDRS`

```c
#define BT_VS_CMD_BIT_READ_STATIC_ADDRS 8
```

<a id="a9af8f8bde7f33db3f32aa2aa5bda4012"></a>

### `BT_VS_CMD_BIT_READ_TX_POWER`

```c
#define BT_VS_CMD_BIT_READ_TX_POWER 14
```

<a id="a020ca307df4c66bcd4c4f6da42d22e40"></a>

### `BT_VS_CMD_BIT_RESET`

```c
#define BT_VS_CMD_BIT_RESET 4
```

<a id="ab1b627847e323e94949b53665e47f20f"></a>

### `BT_VS_CMD_BIT_SET_EVT_MASK`

```c
#define BT_VS_CMD_BIT_SET_EVT_MASK 3
```

<a id="ac16322768bdd4688b2cefb4ea7b8c26f"></a>

### `BT_VS_CMD_BIT_SET_SCAN_REP_ENABLE`

```c
#define BT_VS_CMD_BIT_SET_SCAN_REP_ENABLE 12
```

<a id="ad57ee37a93208d3127e5ba36933b0d36"></a>

### `BT_VS_CMD_BIT_SET_TRACE_ENABLE`

```c
#define BT_VS_CMD_BIT_SET_TRACE_ENABLE 6
```

<a id="a2eec9eff49fc0d8f4e4f746dd7498478"></a>

### `BT_VS_CMD_BIT_SUP_CMD`

```c
#define BT_VS_CMD_BIT_SUP_CMD 1
```

<a id="a418e0fd9c322671c1124835752b25678"></a>

### `BT_VS_CMD_BIT_SUP_FEAT`

```c
#define BT_VS_CMD_BIT_SUP_FEAT 2
```

<a id="a98cda5172947a82dfee334a5db41b0bb"></a>

### `BT_VS_CMD_BIT_VERSION`

```c
#define BT_VS_CMD_BIT_VERSION 0
```

<a id="ac8fa0f7e3d5b802f1797c77d988bc172"></a>

### `BT_VS_CMD_BIT_WRITE_BDADDR`

```c
#define BT_VS_CMD_BIT_WRITE_BDADDR 5
```

<a id="a3f720e278e3aeefd11e9682d683e448b"></a>

### `BT_VS_CMD_BIT_WRITE_TX_POWER`

```c
#define BT_VS_CMD_BIT_WRITE_TX_POWER 13
```

<a id="aa81a670c17714854306b0044e9fb6392"></a>

### `BT_VS_CMD_READ_KEY_ROOTS`

```c
#define BT_VS_CMD_READ_KEY_ROOTS ( cmd)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(cmd, \
BT_VS_CMD_BIT_READ_KEY_ROOTS)
```

<a id="af5ef90c96d5798cef8ad32f8d6094d53"></a>

### `BT_VS_CMD_READ_STATIC_ADDRS`

```c
#define BT_VS_CMD_READ_STATIC_ADDRS ( cmd)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(cmd, \
BT_VS_CMD_BIT_READ_STATIC_ADDRS)
```

<a id="a6f43e26c34622d9b9b2cf0a6ba53a393"></a>

### `BT_VS_CMD_SUP_FEAT`

```c
#define BT_VS_CMD_SUP_FEAT ( cmd)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(cmd, \
BT_VS_CMD_BIT_SUP_FEAT)
```

<a id="af94dd47fba70aa74257db8f711a855dc"></a>

### `BT_VS_CMD_WRITE_BD_ADDR`

```c
#define BT_VS_CMD_WRITE_BD_ADDR ( cmd)
```

展开值（Value）：

```c
BT_LE_FEAT_TEST(cmd, \
BT_VS_CMD_BIT_WRITE_BDADDR)
```

检查是否支持主机控制器接口厂商特定命令（HCI VS Command）`BT_VS_CMD_BIT_WRITE_BDADDR`。

<a id="a2f8e8f0070bde0e62019c71cc343fbe6"></a>

### `DEFAULT_VS_EVT_MASK`

```c
#define DEFAULT_VS_EVT_MASK
```

展开值（Value）：

```c
BT_EVT_MASK_VS_FATAL_ERROR | BT_EVT_MASK_VS_TRACE_INFO | BT_EVT_MASK_VS_SCAN_REQ_RX |      \
        BT_EVT_MASK_VS_LE_CONNECTIONLESS_IQ_REPORT |                                       \
        BT_EVT_MASK_VS_LE_CONNECTION_IQ_REPORT
```

<a id="afc9ea0e4f2260bf59336f2c66532d9b1"></a>

### `hci_vs_err_assert()`

```c
struct net_buf * hci_vs_err_assert ( const char * file, uint32_t line )
```

<a id="aa90c2106bbb977f1ea8532212ff01b4d"></a>

### `hci_vs_err_stack_frame()`

```c
struct net_buf * hci_vs_err_stack_frame ( unsigned int reason, const struct arch_esf * esf )
```

<a id="a9a91c493cc947492d5a172a15abe9a4e"></a>

### `hci_vs_err_trace()`

```c
struct net_buf * hci_vs_err_trace ( const char * file, uint32_t line, uint64_t pc )
```


## 17.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h_source.html)
- [zephyr/bluetooth/hci.h](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [bt_hci_rp_vs_read_version_info](../bluetooth_hci_model_reference/P432_bt_hci_rp_vs_read_version_info_结构体.md)
- [bt_hci_rp_vs_read_supported_commands](../bluetooth_hci_model_reference/P428_bt_hci_rp_vs_read_supported_commands_结构体.md)
- [bt_hci_rp_vs_read_supported_features](../bluetooth_hci_model_reference/P429_bt_hci_rp_vs_read_supported_features_结构体.md)
- [bt_hci_cp_vs_set_event_mask](../bluetooth_hci_model_reference/P177_bt_hci_cp_vs_set_event_mask_结构体.md)
- [bt_hci_cp_vs_reset](../bluetooth_hci_model_reference/P176_bt_hci_cp_vs_reset_结构体.md)
- [bt_hci_cp_vs_write_bd_addr](../bluetooth_hci_model_reference/P182_bt_hci_cp_vs_write_bd_addr_结构体.md)
- [bt_hci_cp_vs_set_trace_enable](../bluetooth_hci_model_reference/P180_bt_hci_cp_vs_set_trace_enable_结构体.md)
- [bt_hci_rp_vs_read_build_info](../bluetooth_hci_model_reference/P423_bt_hci_rp_vs_read_build_info_结构体.md)
- [bt_hci_vs_static_addr](../bluetooth_hci_model_reference/P449_bt_hci_vs_static_addr_结构体.md)
- [bt_hci_rp_vs_read_static_addrs](../bluetooth_hci_model_reference/P427_bt_hci_rp_vs_read_static_addrs_结构体.md)
- [bt_hci_rp_vs_read_key_hierarchy_roots](../bluetooth_hci_model_reference/P426_bt_hci_rp_vs_read_key_hierarchy_roots_结构体.md)
- [bt_hci_rp_vs_read_chip_temp](../bluetooth_hci_model_reference/P424_bt_hci_rp_vs_read_chip_temp_结构体.md)
- [bt_hci_vs_cmd](../bluetooth_hci_model_reference/P442_bt_hci_vs_cmd_结构体.md)
- [bt_hci_rp_vs_read_host_stack_cmds](../bluetooth_hci_model_reference/P425_bt_hci_rp_vs_read_host_stack_cmds_结构体.md)
- [bt_hci_cp_vs_set_scan_req_reports](../bluetooth_hci_model_reference/P179_bt_hci_cp_vs_set_scan_req_reports_结构体.md)
- [bt_hci_cp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P183_bt_hci_cp_vs_write_tx_power_level_结构体.md)
- [bt_hci_rp_vs_write_tx_power_level](../bluetooth_hci_model_reference/P433_bt_hci_rp_vs_write_tx_power_level_结构体.md)
- [bt_hci_cp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P175_bt_hci_cp_vs_read_tx_power_level_结构体.md)
- [bt_hci_rp_vs_read_tx_power_level](../bluetooth_hci_model_reference/P430_bt_hci_rp_vs_read_tx_power_level_结构体.md)
- [bt_hci_rp_vs_read_usb_transport_mode](../bluetooth_hci_model_reference/P431_bt_hci_rp_vs_read_usb_transport_mode_结构体.md)
- [bt_hci_cp_vs_set_usb_transport_mode](../bluetooth_hci_model_reference/P181_bt_hci_cp_vs_set_usb_transport_mode_结构体.md)
- [bt_hci_cp_vs_set_min_num_used_chans](../bluetooth_hci_model_reference/P178_bt_hci_cp_vs_set_min_num_used_chans_结构体.md)
- [bt_hci_evt_vs](../bluetooth_hci_model_reference/P300_bt_hci_evt_vs_结构体.md)
- [bt_hci_vs_fatal_error_cpu_data_cortex_m](../bluetooth_hci_model_reference/P447_bt_hci_vs_fatal_error_cpu_data_cortex_m_结构体.md)
- [bt_hci_vs_fatal_error_stack_frame](../bluetooth_hci_model_reference/P448_bt_hci_vs_fatal_error_stack_frame_结构体.md)
- [bt_hci_evt_vs_fatal_error_trace_data](../bluetooth_hci_model_reference/P302_bt_hci_evt_vs_fatal_error_trace_data_结构体.md)
- [bt_hci_evt_vs_fatal_error](../bluetooth_hci_model_reference/P301_bt_hci_evt_vs_fatal_error_结构体.md)
- [bt_hci_evt_vs_trace_info](../bluetooth_hci_model_reference/P306_bt_hci_evt_vs_trace_info_结构体.md)
- [bt_hci_evt_vs_scan_req_rx](../bluetooth_hci_model_reference/P305_bt_hci_evt_vs_scan_req_rx_结构体.md)
- [bt_hci_le_iq_sample16](../bluetooth_hci_model_reference/P324_bt_hci_le_iq_sample16_结构体.md)
- [bt_hci_evt_vs_le_connectionless_iq_report](../bluetooth_hci_model_reference/P304_bt_hci_evt_vs_le_connectionless_iq_report_结构体.md)
- [bt_hci_evt_vs_le_connection_iq_report](../bluetooth_hci_model_reference/P303_bt_hci_evt_vs_le_connection_iq_report_结构体.md)
- [bt_hci_cp_mesh](../bluetooth_hci_model_reference/P141_bt_hci_cp_mesh_结构体.md)
- [bt_hci_rp_mesh_get_opts](../bluetooth_hci_model_reference/P396_bt_hci_rp_mesh_get_opts_结构体.md)
- [bt_hci_mesh_pattern](../bluetooth_hci_model_reference/P327_bt_hci_mesh_pattern_结构体.md)
- [bt_hci_cp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P145_bt_hci_cp_mesh_set_scan_filter_结构体.md)
- [bt_hci_rp_mesh_set_scan_filter](../bluetooth_hci_model_reference/P397_bt_hci_rp_mesh_set_scan_filter_结构体.md)
- [bt_hci_cp_mesh_advertise](../bluetooth_hci_model_reference/P142_bt_hci_cp_mesh_advertise_结构体.md)
- [bt_hci_rp_mesh_advertise](../bluetooth_hci_model_reference/P393_bt_hci_rp_mesh_advertise_结构体.md)
- [bt_hci_cp_mesh_advertise_timed](../bluetooth_hci_model_reference/P144_bt_hci_cp_mesh_advertise_timed_结构体.md)
- [bt_hci_rp_mesh_advertise_timed](../bluetooth_hci_model_reference/P395_bt_hci_rp_mesh_advertise_timed_结构体.md)
- [bt_hci_cp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P143_bt_hci_cp_mesh_advertise_cancel_结构体.md)
- [bt_hci_rp_mesh_advertise_cancel](../bluetooth_hci_model_reference/P394_bt_hci_rp_mesh_advertise_cancel_结构体.md)
- [bt_hci_cp_mesh_set_scanning](../bluetooth_hci_model_reference/P146_bt_hci_cp_mesh_set_scanning_结构体.md)
- [bt_hci_rp_mesh_set_scanning](../bluetooth_hci_model_reference/P398_bt_hci_rp_mesh_set_scanning_结构体.md)
- [bt_hci_evt_mesh](../bluetooth_hci_model_reference/P283_bt_hci_evt_mesh_结构体.md)
- [bt_hci_evt_mesh_adv_complete](../bluetooth_hci_model_reference/P284_bt_hci_evt_mesh_adv_complete_结构体.md)
- [bt_hci_evt_mesh_scan_report](../bluetooth_hci_model_reference/P285_bt_hci_evt_mesh_scan_report_结构体.md)
- [bt_hci_evt_mesh_scanning_report](../bluetooth_hci_model_reference/P286_bt_hci_evt_mesh_scanning_report_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [BT_OP](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7e006e0f69c498601f2c64a4ce3d8101)
- [BT_OGF_VS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6b682cb6e4f489ffb67b05280b3dbd65)
- [BT_EVT_BIT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a25201544478590f6ee87a829410c612b)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [BT_LE_FEAT_TEST](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a6bf20989952fed3726bc45873beb896e)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="ahci__types_8h_html_a6bf20989952fed3726bc45873beb896e"></a>
<a id="ahci__vs_8h_html_aa8b39f4ac968cf0cdb18073de1aa1ad5"></a>
<a id="ahci__vs_8h_html_a27e19ec90e057244db7f632887a46ec1"></a>
<a id="ahci__vs_8h_html_a418e0fd9c322671c1124835752b25678"></a>
<a id="ahci__vs_8h_html_ac8fa0f7e3d5b802f1797c77d988bc172"></a>
<a id="ahci__vs_8h_html_a365da8f1041d55948caa4bf60ea349bd"></a>
<a id="ahci__vs_8h_html_a3971e9541300e12abb4ff36679d9b1f1"></a>
<a id="ahci__vs_8h_html_a74d2cf07f64f35318ec4ba24fd570dff"></a>
<a id="ahci__vs_8h_html_a9b4fcdd0de4197b3eb1ac65602e30408"></a>
<a id="ahci__vs_8h_html_aae4f865bf37b8933de070e16ea3047ec"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_zephyr__drivers__gpio__gpio_nrf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__net__hdlc_rcp_if__hdlc_rcp_if.h_文件参考.md)
