---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-10
title: USB Type-C 端口控制器驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_USB Type-C 端口控制器驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 USB Type-C 端口控制器驱动（USB Type-C Port Controller Driver）所需的 API 类型定义（Type Definitions）、回调签名（Callback Signatures）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_tcpc_5Fdriver_5Fapi"></a>

```c
struct tcpc_driver_api
```

相关声明：[tcpc_driver_api](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md)。

驱动操作（Driver Operations）：USB Type-C端口控制器（Port Controller）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_gae28524287fdb5504883afb66003d035c"></a>

```c
typedef int(* tcpc_api_init_t) (const struct device *dev)
```

相关声明：[tcpc_api_init_t](#gae28524287fdb5504883afb66003d035c)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Type-C 端口控制器（TCPC）的回调 API。

<a id="r_ga39981c9b68e280de660ca15e137ffbd0"></a>

```c
typedef int(* tcpc_api_get_cc_t) (const struct device *dev, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

相关声明：[tcpc_api_get_cc_t](#ga39981c9b68e280de660ca15e137ffbd0)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

读取 CC 线路状态（CC Line Status）的回调 API。

<a id="r_gae749f76083de380e2edd602dc0e30402"></a>

```c
typedef int(* tcpc_api_select_rp_value_t) (const struct device *dev, enum tc_rp_value rp)
```

相关声明：[tcpc_api_select_rp_value_t](#gae749f76083de380e2edd602dc0e30402)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

设置供电端 Rp 值（Source Rp Value）的回调 API。

<a id="r_gad1db9d036dd666846065bbf35ea22177"></a>

```c
typedef int(* tcpc_api_get_rp_value_t) (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[tcpc_api_get_rp_value_t](#gad1db9d036dd666846065bbf35ea22177)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取供电端 Rp 值（Source Rp Value）的回调 API。

<a id="r_gac524dbe59d67fb5bdfad78bc1a4d64c9"></a>

```c
typedef int(* tcpc_api_set_cc_t) (const struct device *dev, enum tc_cc_pull pull)
```

相关声明：[tcpc_api_set_cc_t](#gac524dbe59d67fb5bdfad78bc1a4d64c9)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)。

设置 CC 上拉／下拉（CC Pull）及角色（Role）的回调 API。

<a id="r_gad8d3e1b467e6ee4fb58dcfed16117737"></a>

```c
typedef void(* tcpc_api_set_vconn_discharge_cb_t) (const struct device *dev, tcpc_vconn_discharge_cb_t cb, const struct device *usbc_dev)
```

相关声明：[tcpc_api_set_vconn_discharge_cb_t](#gad8d3e1b467e6ee4fb58dcfed16117737)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)。

注册 VCONN 放电应用回调（VCONN Discharge Application Callback）的回调 API。

<a id="r_ga26217be69c8bc7ea24e6cabe489445da"></a>

```c
typedef void(* tcpc_api_set_vconn_cb_t) (const struct device *dev, tcpc_vconn_control_cb_t vconn_cb, const struct device *usbc_dev)
```

相关声明：[tcpc_api_set_vconn_cb_t](#ga26217be69c8bc7ea24e6cabe489445da)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)。

注册 VCONN 控制应用回调（VCONN Control Application Callback）的回调 API。

<a id="r_gab503f46443ce870dd0baeebf8dd48e8f"></a>

```c
typedef int(* tcpc_api_vconn_discharge_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_vconn_discharge_t](#gab503f46443ce870dd0baeebf8dd48e8f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN 放电（VCONN Discharge）的回调 API。

<a id="r_gaf8d6f41fdd6fe99a1b629d361556966d"></a>

```c
typedef int(* tcpc_api_set_vconn_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_vconn_t](#gaf8d6f41fdd6fe99a1b629d361556966d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN 的回调 API。

<a id="r_gadc6b26855f37fe94391f294c7f63d5bd"></a>

```c
typedef int(* tcpc_api_set_roles_t) (const struct device *dev, enum tc_power_role power_role, enum tc_data_role data_role)
```

相关声明：[tcpc_api_set_roles_t](#gadc6b26855f37fe94391f294c7f63d5bd)、[device](../device_reference/P002_设备对象结构.md)、[tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)。

设置 PD 消息头部（PD Message Header）电源角色（Power Role）和数据角色（Data Role）的回调 API。

<a id="r_gab0828b95c31b6d6523ca471dd68ec065"></a>

```c
typedef int(* tcpc_api_get_rx_pending_msg_t) (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_api_get_rx_pending_msg_t](#gab0828b95c31b6d6523ca471dd68ec065)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

获取待处理接收消息（Pending RX Message）或查询接收状态（RX Status）的回调 API。

<a id="r_ga7cd4aae87502bf5ebb1939edceea81f3"></a>

```c
typedef int(* tcpc_api_set_rx_enable_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_rx_enable_t](#ga7cd4aae87502bf5ebb1939edceea81f3)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 SOP* 接收（RX）的回调 API。

<a id="r_gaa791f068d25e28abbd7d45071a5016be"></a>

```c
typedef int(* tcpc_api_set_cc_polarity_t) (const struct device *dev, enum tc_cc_polarity polarity)
```

相关声明：[tcpc_api_set_cc_polarity_t](#gaa791f068d25e28abbd7d45071a5016be)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)。

设置 CC 极性（CC Polarity）的回调 API。

<a id="r_gab1f1d2db116913e4c0e451f57fb76d2c"></a>

```c
typedef int(* tcpc_api_transmit_data_t) (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_api_transmit_data_t](#gab1f1d2db116913e4c0e451f57fb76d2c)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

发送 PD 消息（PD Message）的回调 API。

<a id="r_ga99bb0b6056fb353fe15fc2d717f1a724"></a>

```c
typedef int(* tcpc_api_dump_std_reg_t) (const struct device *dev)
```

相关声明：[tcpc_api_dump_std_reg_t](#ga99bb0b6056fb353fe15fc2d717f1a724)、[device](../device_reference/P002_设备对象结构.md)。

转储标准 TCPC 寄存器（Standard TCPC Registers）的回调 API。

<a id="r_gaa309db76ccb877d1cd9797d34bc55900"></a>

```c
typedef int(* tcpc_api_mask_status_register_t) (const struct device *dev, enum tcpc_status_reg reg, uint32_t mask)
```

相关声明：[tcpc_api_mask_status_register_t](#gaa309db76ccb877d1cd9797d34bc55900)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

屏蔽或取消屏蔽状态寄存器位（Status Register Bits）的回调 API。

<a id="r_ga238a927c4602269c48325d06d0f72215"></a>

```c
typedef int(* tcpc_api_set_debug_accessory_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_debug_accessory_t](#ga238a927c4602269c48325d06d0f72215)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用调试附件控制（Debug Accessory Control）的回调 API。

<a id="r_ga483cbf6d74b5a892d8d241ccc8f6060e"></a>

```c
typedef int(* tcpc_api_set_debug_detach_t) (const struct device *dev)
```

相关声明：[tcpc_api_set_debug_detach_t](#ga483cbf6d74b5a892d8d241ccc8f6060e)、[device](../device_reference/P002_设备对象结构.md)。

从调试连接（Debug Connection）断开的回调 API。

<a id="r_ga56db121a729ffbb9173fe03fe867add1"></a>

```c
typedef int(* tcpc_api_set_drp_toggle_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_drp_toggle_t](#ga56db121a729ffbb9173fe03fe867add1)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用双角色电源端口切换（DRP Toggle）的回调 API。

<a id="r_gabafb00fd478d682be7d33379b2c2487e"></a>

```c
typedef int(* tcpc_api_get_snk_ctrl_t) (const struct device *dev)
```

相关声明：[tcpc_api_get_snk_ctrl_t](#gabafb00fd478d682be7d33379b2c2487e)、[device](../device_reference/P002_设备对象结构.md)。

查询 VBUS 受电控制状态（VBUS Sink Control State）的回调 API。

<a id="r_gaaed7c7d360c5eb455d84164fc4ee2d1d"></a>

```c
typedef int(* tcpc_api_set_snk_ctrl_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_snk_ctrl_t](#gaaed7c7d360c5eb455d84164fc4ee2d1d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VBUS 受电（VBUS Sinking）的回调 API。

<a id="r_ga2da6efeb17079086b4dc7ac52d2e60e7"></a>

```c
typedef int(* tcpc_api_get_src_ctrl_t) (const struct device *dev)
```

相关声明：[tcpc_api_get_src_ctrl_t](#ga2da6efeb17079086b4dc7ac52d2e60e7)、[device](../device_reference/P002_设备对象结构.md)。

查询 VBUS 供电控制状态（VBUS Source Control State）的回调 API。

<a id="r_ga8863bafbd43a21204b990aa74d710285"></a>

```c
typedef int(* tcpc_api_set_src_ctrl_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_src_ctrl_t](#ga8863bafbd43a21204b990aa74d710285)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VBUS 供电（VBUS Sourcing）的回调 API。

<a id="r_gac6f9724f73200ca20f1aa0a519928e50"></a>

```c
typedef int(* tcpc_api_get_chip_info_t) (const struct device *dev, struct tcpc_chip_info *chip_info)
```

相关声明：[tcpc_api_get_chip_info_t](#gac6f9724f73200ca20f1aa0a519928e50)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

读取 TCPC 芯片信息（TCPC Chip Information）的回调 API。

<a id="r_gae3339cd538cf4025f9f6e0959647e430"></a>

```c
typedef int(* tcpc_api_set_low_power_mode_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_low_power_mode_t](#gae3339cd538cf4025f9f6e0959647e430)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

进入或退出低功耗模式（Low Power Mode）的回调 API。

<a id="r_ga232b5d184f585aab94eb22daaf06c86b"></a>

```c
typedef int(* tcpc_api_sop_prime_enable_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_sop_prime_enable_t](#ga232b5d184f585aab94eb22daaf06c86b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 `SOP'`／`SOP''` 接收（Reception）的回调 API。

<a id="r_gaea02443c9aeb62583903291908a660cd"></a>

```c
typedef int(* tcpc_api_set_bist_test_mode_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_bist_test_mode_t](#gaea02443c9aeb62583903291908a660cd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用内建自测试模式（BIST Test Mode）的回调 API。

<a id="r_ga511cdf626c88790199edbd2fd578a833"></a>

```c
typedef int(* tcpc_api_set_alert_handler_cb_t) (const struct device *dev, tcpc_alert_handler_cb_t handler, void *data)
```

相关声明：[tcpc_api_set_alert_handler_cb_t](#ga511cdf626c88790199edbd2fd578a833)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)。

注册警报应用回调（Alert Application Callback）的回调 API。

<a id="r_ga0dfa332e501412fb407ef2490a042e11"></a>

```c
typedef int(* tcpc_api_dead_battery_enabled_t) (const struct device *dev, bool *enabled)
```

相关声明：[tcpc_api_dead_battery_enabled_t](#ga0dfa332e501412fb407ef2490a042e11)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPC 无电池电量配置（Dead Battery Configuration）的回调 API。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga0dfa332e501412fb407ef2490a042e11"></a>

### `tcpc_api_dead_battery_enabled_t`

```c
typedef int(* tcpc_api_dead_battery_enabled_t) (const struct device *dev, bool *enabled)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 TCPC 无电池电量配置（Dead Battery Configuration）的回调 API。

参数说明参见 `tcpc_dead_battery_enabled()`。

<a id="ga99bb0b6056fb353fe15fc2d717f1a724"></a>

### `tcpc_api_dump_std_reg_t`

```c
typedef int(* tcpc_api_dump_std_reg_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

转储标准 TCPC 寄存器（Standard TCPC Registers）的回调 API。

参数说明参见 `tcpc_dump_std_reg()`。

<a id="ga39981c9b68e280de660ca15e137ffbd0"></a>

### `tcpc_api_get_cc_t`

```c
typedef int(* tcpc_api_get_cc_t) (const struct device *dev, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

读取 CC 线路状态（CC Line Status）的回调 API。

参数说明参见 `tcpc_get_cc()`。

<a id="gac6f9724f73200ca20f1aa0a519928e50"></a>

### `tcpc_api_get_chip_info_t`

```c
typedef int(* tcpc_api_get_chip_info_t) (const struct device *dev, struct tcpc_chip_info *chip_info)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

读取 TCPC 芯片信息（TCPC Chip Information）的回调 API。

参数说明参见 `tcpc_get_chip_info()`。

<a id="gad1db9d036dd666846065bbf35ea22177"></a>

### `tcpc_api_get_rp_value_t`

```c
typedef int(* tcpc_api_get_rp_value_t) (const struct device *dev, enum tc_rp_value *rp)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

获取供电端 Rp 值（Source Rp Value）的回调 API。

参数说明参见 `tcpc_get_rp_value()`。

<a id="gab0828b95c31b6d6523ca471dd68ec065"></a>

### `tcpc_api_get_rx_pending_msg_t`

```c
typedef int(* tcpc_api_get_rx_pending_msg_t) (const struct device *dev, struct pd_msg *msg)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

获取待处理接收消息（Pending RX Message）或查询接收状态（RX Status）的回调 API。

参数说明参见 `tcpc_get_rx_pending_msg()`。

<a id="gabafb00fd478d682be7d33379b2c2487e"></a>

### `tcpc_api_get_snk_ctrl_t`

```c
typedef int(* tcpc_api_get_snk_ctrl_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 VBUS 受电控制状态（VBUS Sink Control State）的回调 API。

参数说明参见 `tcpc_get_snk_ctrl()`。

<a id="ga2da6efeb17079086b4dc7ac52d2e60e7"></a>

### `tcpc_api_get_src_ctrl_t`

```c
typedef int(* tcpc_api_get_src_ctrl_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

查询 VBUS 供电控制状态（VBUS Source Control State）的回调 API。

参数说明参见 `tcpc_get_src_ctrl()`。

<a id="gae28524287fdb5504883afb66003d035c"></a>

### `tcpc_api_init_t`

```c
typedef int(* tcpc_api_init_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

初始化 Type-C 端口控制器（TCPC）的回调 API。

参数说明参见 `tcpc_init()`。

<a id="gaa309db76ccb877d1cd9797d34bc55900"></a>

### `tcpc_api_mask_status_register_t`

```c
typedef int(* tcpc_api_mask_status_register_t) (const struct device *dev, enum tcpc_status_reg reg, uint32_t mask)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

屏蔽或取消屏蔽状态寄存器位（Status Register Bits）的回调 API。

参数说明参见 `tcpc_mask_status_register()`。

<a id="gae749f76083de380e2edd602dc0e30402"></a>

### `tcpc_api_select_rp_value_t`

```c
typedef int(* tcpc_api_select_rp_value_t) (const struct device *dev, enum tc_rp_value rp)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置供电端 Rp 值（Source Rp Value）的回调 API。

参数说明参见 `tcpc_select_rp_value()`。

<a id="ga511cdf626c88790199edbd2fd578a833"></a>

### `tcpc_api_set_alert_handler_cb_t`

```c
typedef int(* tcpc_api_set_alert_handler_cb_t) (const struct device *dev, tcpc_alert_handler_cb_t handler, void *data)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

注册警报应用回调（Alert Application Callback）的回调 API。

参数说明参见 `tcpc_set_alert_handler_cb()`。

<a id="gaea02443c9aeb62583903291908a660cd"></a>

### `tcpc_api_set_bist_test_mode_t`

```c
typedef int(* tcpc_api_set_bist_test_mode_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用内建自测试模式（BIST Test Mode）的回调 API。

参数说明参见 `tcpc_set_bist_test_mode()`。

<a id="gaa791f068d25e28abbd7d45071a5016be"></a>

### `tcpc_api_set_cc_polarity_t`

```c
typedef int(* tcpc_api_set_cc_polarity_t) (const struct device *dev, enum tc_cc_polarity polarity)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 CC 极性（CC Polarity）的回调 API。

参数说明参见 `tcpc_set_cc_polarity()`。

<a id="gac524dbe59d67fb5bdfad78bc1a4d64c9"></a>

### `tcpc_api_set_cc_t`

```c
typedef int(* tcpc_api_set_cc_t) (const struct device *dev, enum tc_cc_pull pull)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 CC 上拉／下拉（CC Pull）及角色（Role）的回调 API。

参数说明参见 `tcpc_set_cc()`。

<a id="ga238a927c4602269c48325d06d0f72215"></a>

### `tcpc_api_set_debug_accessory_t`

```c
typedef int(* tcpc_api_set_debug_accessory_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用调试附件控制（Debug Accessory Control）的回调 API。

参数说明参见 `tcpc_set_debug_accessory()`。

<a id="ga483cbf6d74b5a892d8d241ccc8f6060e"></a>

### `tcpc_api_set_debug_detach_t`

```c
typedef int(* tcpc_api_set_debug_detach_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

从调试连接（Debug Connection）断开的回调 API。

参数说明参见 `tcpc_set_debug_detach()`。

<a id="ga56db121a729ffbb9173fe03fe867add1"></a>

### `tcpc_api_set_drp_toggle_t`

```c
typedef int(* tcpc_api_set_drp_toggle_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用双角色电源端口切换（DRP Toggle）的回调 API。

参数说明参见 `tcpc_set_drp_toggle()`。

<a id="gae3339cd538cf4025f9f6e0959647e430"></a>

### `tcpc_api_set_low_power_mode_t`

```c
typedef int(* tcpc_api_set_low_power_mode_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

进入或退出低功耗模式（Low Power Mode）的回调 API。

参数说明参见 `tcpc_set_low_power_mode()`。

<a id="gadc6b26855f37fe94391f294c7f63d5bd"></a>

### `tcpc_api_set_roles_t`

```c
typedef int(* tcpc_api_set_roles_t) (const struct device *dev, enum tc_power_role power_role, enum tc_data_role data_role)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

设置 PD 消息头部（PD Message Header）电源角色（Power Role）和数据角色（Data Role）的回调 API。

参数说明参见 `tcpc_set_roles()`。

<a id="ga7cd4aae87502bf5ebb1939edceea81f3"></a>

### `tcpc_api_set_rx_enable_t`

```c
typedef int(* tcpc_api_set_rx_enable_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 SOP* 接收（RX）的回调 API。

参数说明参见 `tcpc_set_rx_enable()`。

<a id="gaaed7c7d360c5eb455d84164fc4ee2d1d"></a>

### `tcpc_api_set_snk_ctrl_t`

```c
typedef int(* tcpc_api_set_snk_ctrl_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 VBUS 受电（VBUS Sinking）的回调 API。

参数说明参见 `tcpc_set_snk_ctrl()`。

<a id="ga8863bafbd43a21204b990aa74d710285"></a>

### `tcpc_api_set_src_ctrl_t`

```c
typedef int(* tcpc_api_set_src_ctrl_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 VBUS 供电（VBUS Sourcing）的回调 API。

参数说明参见 `tcpc_set_src_ctrl()`。

<a id="ga26217be69c8bc7ea24e6cabe489445da"></a>

### `tcpc_api_set_vconn_cb_t`

```c
typedef void(* tcpc_api_set_vconn_cb_t) (const struct device *dev, tcpc_vconn_control_cb_t vconn_cb, const struct device *usbc_dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

注册 VCONN 控制应用回调（VCONN Control Application Callback）的回调 API。

参数说明参见 `tcpc_set_vconn_cb()`。

<a id="gad8d3e1b467e6ee4fb58dcfed16117737"></a>

### `tcpc_api_set_vconn_discharge_cb_t`

```c
typedef void(* tcpc_api_set_vconn_discharge_cb_t) (const struct device *dev, tcpc_vconn_discharge_cb_t cb, const struct device *usbc_dev)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

注册 VCONN 放电应用回调（VCONN Discharge Application Callback）的回调 API。

参数说明参见 `tcpc_set_vconn_discharge_cb()`。

<a id="gaf8d6f41fdd6fe99a1b629d361556966d"></a>

### `tcpc_api_set_vconn_t`

```c
typedef int(* tcpc_api_set_vconn_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 VCONN 的回调 API。

参数说明参见 `tcpc_set_vconn()`。

<a id="ga232b5d184f585aab94eb22daaf06c86b"></a>

### `tcpc_api_sop_prime_enable_t`

```c
typedef int(* tcpc_api_sop_prime_enable_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 `SOP'`／`SOP''` 接收（Reception）的回调 API。

参数说明参见 `tcpc_sop_prime_enable()`。

<a id="gab1f1d2db116913e4c0e451f57fb76d2c"></a>

### `tcpc_api_transmit_data_t`

```c
typedef int(* tcpc_api_transmit_data_t) (const struct device *dev, struct pd_msg *msg)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

发送 PD 消息（PD Message）的回调 API。

参数说明参见 `tcpc_transmit_data()`。

<a id="gab503f46443ce870dd0baeebf8dd48e8f"></a>

### `tcpc_api_vconn_discharge_t`

```c
typedef int(* tcpc_api_vconn_discharge_t) (const struct device *dev, bool enable)
```

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

启用或禁用 VCONN 放电（VCONN Discharge）的回调 API。

参数说明参见 `tcpc_vconn_discharge()`。


## 10.4\_原页交叉引用（Cross References）

- [tcpc_driver_api](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)
- [tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)
- [tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)
- [zephyr/drivers/usb_c/usbc_tcpc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)
- [tcpc_dead_battery_enabled()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaac29d0958fd377db24f1911cfa03188c)
- [tcpc_dump_std_reg()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91eef7084b523f1991e000f0592b8cbd)
- [tcpc_get_cc()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga66ab7a9f3cd1b80cd5bc8e99040c5627)
- [tcpc_get_chip_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga894d24140f8675b4f48d759c27f52076)
- [tcpc_get_rp_value()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga25a110be90977e768623f3a0c9a222d5)
- [tcpc_get_rx_pending_msg()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga34e4caefb0f660b170f97956ac57b707)
- [tcpc_get_snk_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0c1cd7bc86c89abf5e348987d34e4623)
- [tcpc_get_src_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03c8c6fc6f4c6adefacbc809588e1f85)
- [tcpc_init()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gabc50daa9cc713b1d0e340007e3850ca8)
- [tcpc_mask_status_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0d1868d555e99877e062fb7135d9db8f)
- [tcpc_select_rp_value()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3958eac0cc0b9b2ac782e0cdb235036c)
- [tcpc_set_alert_handler_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga75f0dc246dac576f14c5ac51b45fd489)
- [tcpc_set_bist_test_mode()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaccc728a1f27c59a163a5c0a221ab7c18)
- [tcpc_set_cc_polarity()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga53f0207ecb63011c6dfc3c298a841ed4)
- [tcpc_set_cc()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gac5737d02caa2b9e649b469bcd648440f)
- [tcpc_set_debug_accessory()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga01687aa218b25ba137e994a2a55bce23)
- [tcpc_set_debug_detach()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaaa38e56e6bc8c41e936d8ed70aaa8a23)
- [tcpc_set_drp_toggle()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa06e156bef46ff3f70cc8c302ddf0a4d)
- [tcpc_set_low_power_mode()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga961a4dc393d58dc44ea19a62c943ed48)
- [tcpc_set_roles()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8d30c961335f62faa33aa7d842422da0)
- [tcpc_set_rx_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga905176a77ff127f4df8f6a4f2c61a1b7)
- [tcpc_set_snk_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga7a63d55cbe5de1d89aa76e10df0140ed)
- [tcpc_set_src_ctrl()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8f06b257d1bd0a17eb3042d204b2e6cd)
- [tcpc_set_vconn_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga1f057bcddc5a7757370f2e6de8170128)
- [tcpc_set_vconn_discharge_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga71981a635ad82b9db41d549f29ad5c68)
- [tcpc_set_vconn()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga247f0ea91249753d6f5eefe006617e41)
- [tcpc_sop_prime_enable()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)
- [tcpc_transmit_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8bf8fd202d582a4cc179a0fc4aff35e1)
- [tcpc_vconn_discharge()](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3937d66636a2b22422caf11c48f7628a)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P009_安全Shell（SSH）客户端_服务器的通用API。.md) · [返回大纲](大纲.md) · [下一章](P011_视频格式（Video Formats）.md)
