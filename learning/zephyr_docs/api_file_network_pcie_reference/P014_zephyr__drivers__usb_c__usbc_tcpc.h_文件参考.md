---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-14
title: zephyr__drivers__usb_c__usbc_tcpc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_usb\_c\_\_usbc\_tcpc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C Type-C端口控制器（Port Controller）的设备API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>
#include "usbc_tc.h"
#include "usbc_pd.h"
```

查看此文件的源码。

USB-C Type-C 端口控制器设备 API（USB Type-C Port Controller Device APIs）。本文件包含 USB Type-C 端口控制器的设备 API。所有 Type-C 端口控制器设备驱动均应实现本文件描述的 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_tcpc_5Fchip_5Finfo"></a>

```c
struct tcpc_chip_info
```

相关声明：[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

Type-C端口控制器（TCPC）的芯片信息。

<a id="r_tcpc_5Fdriver_5Fapi"></a>

```c
struct tcpc_driver_api
```

相关声明：[tcpc_driver_api](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md)。

驱动操作（Driver Operations）：USB Type-C端口控制器（Port Controller）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_ga073ad4a46a5ea1f9e5cad45488d672f0"></a>

```c
typedef int(* tcpc_vconn_control_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

相关声明：[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

VCONN 控制回调类型（VCONN Control Callback Type）。

<a id="r_ga4d2b77f6ee685d1bff1117843150e664"></a>

```c
typedef int(* tcpc_vconn_discharge_cb_t) (const struct device *tcpc_dev, const struct device *usbc_dev, enum tc_cc_polarity pol, bool enable)
```

相关声明：[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

VCONN 放电回调类型（VCONN Discharge Callback Type）。

<a id="r_ga5f42fa12f90d34961eeeb67c0dc4f925"></a>

```c
typedef void(* tcpc_alert_handler_cb_t) (const struct device *dev, void *data, enum tcpc_alert alert)
```

相关声明：[tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)。

处理 TCPC 警报事件（TCPC Alert Events）的回调类型（Callback Type）。

<a id="r_gae28524287fdb5504883afb66003d035c"></a>

```c
typedef int(* tcpc_api_init_t) (const struct device *dev)
```

相关声明：[tcpc_api_init_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae28524287fdb5504883afb66003d035c)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Type-C 端口控制器（TCPC）的回调 API。

<a id="r_ga39981c9b68e280de660ca15e137ffbd0"></a>

```c
typedef int(* tcpc_api_get_cc_t) (const struct device *dev, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

相关声明：[tcpc_api_get_cc_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga39981c9b68e280de660ca15e137ffbd0)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

读取 CC 线路状态（CC Line Status）的回调 API。

<a id="r_gae749f76083de380e2edd602dc0e30402"></a>

```c
typedef int(* tcpc_api_select_rp_value_t) (const struct device *dev, enum tc_rp_value rp)
```

相关声明：[tcpc_api_select_rp_value_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae749f76083de380e2edd602dc0e30402)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

设置供电端 Rp 值（Source Rp Value）的回调 API。

<a id="r_gad1db9d036dd666846065bbf35ea22177"></a>

```c
typedef int(* tcpc_api_get_rp_value_t) (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[tcpc_api_get_rp_value_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gad1db9d036dd666846065bbf35ea22177)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取供电端 Rp 值（Source Rp Value）的回调 API。

<a id="r_gac524dbe59d67fb5bdfad78bc1a4d64c9"></a>

```c
typedef int(* tcpc_api_set_cc_t) (const struct device *dev, enum tc_cc_pull pull)
```

相关声明：[tcpc_api_set_cc_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gac524dbe59d67fb5bdfad78bc1a4d64c9)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)。

设置 CC 上拉／下拉（CC Pull）及角色（Role）的回调 API。

<a id="r_gad8d3e1b467e6ee4fb58dcfed16117737"></a>

```c
typedef void(* tcpc_api_set_vconn_discharge_cb_t) (const struct device *dev, tcpc_vconn_discharge_cb_t cb, const struct device *usbc_dev)
```

相关声明：[tcpc_api_set_vconn_discharge_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gad8d3e1b467e6ee4fb58dcfed16117737)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)。

注册 VCONN 放电应用回调（VCONN Discharge Application Callback）的回调 API。

<a id="r_ga26217be69c8bc7ea24e6cabe489445da"></a>

```c
typedef void(* tcpc_api_set_vconn_cb_t) (const struct device *dev, tcpc_vconn_control_cb_t vconn_cb, const struct device *usbc_dev)
```

相关声明：[tcpc_api_set_vconn_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga26217be69c8bc7ea24e6cabe489445da)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)。

注册 VCONN 控制应用回调（VCONN Control Application Callback）的回调 API。

<a id="r_gab503f46443ce870dd0baeebf8dd48e8f"></a>

```c
typedef int(* tcpc_api_vconn_discharge_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_vconn_discharge_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab503f46443ce870dd0baeebf8dd48e8f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN 放电（VCONN Discharge）的回调 API。

<a id="r_gaf8d6f41fdd6fe99a1b629d361556966d"></a>

```c
typedef int(* tcpc_api_set_vconn_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_vconn_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaf8d6f41fdd6fe99a1b629d361556966d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN 的回调 API。

<a id="r_gadc6b26855f37fe94391f294c7f63d5bd"></a>

```c
typedef int(* tcpc_api_set_roles_t) (const struct device *dev, enum tc_power_role power_role, enum tc_data_role data_role)
```

相关声明：[tcpc_api_set_roles_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gadc6b26855f37fe94391f294c7f63d5bd)、[device](../device_reference/P002_设备对象结构.md)、[tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)。

设置 PD 消息头部（PD Message Header）电源角色（Power Role）和数据角色（Data Role）的回调 API。

<a id="r_gab0828b95c31b6d6523ca471dd68ec065"></a>

```c
typedef int(* tcpc_api_get_rx_pending_msg_t) (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_api_get_rx_pending_msg_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab0828b95c31b6d6523ca471dd68ec065)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

获取待处理接收消息（Pending RX Message）或查询接收状态（RX Status）的回调 API。

<a id="r_ga7cd4aae87502bf5ebb1939edceea81f3"></a>

```c
typedef int(* tcpc_api_set_rx_enable_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_rx_enable_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga7cd4aae87502bf5ebb1939edceea81f3)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 SOP* 接收（RX）的回调 API。

<a id="r_gaa791f068d25e28abbd7d45071a5016be"></a>

```c
typedef int(* tcpc_api_set_cc_polarity_t) (const struct device *dev, enum tc_cc_polarity polarity)
```

相关声明：[tcpc_api_set_cc_polarity_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaa791f068d25e28abbd7d45071a5016be)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)。

设置 CC 极性（CC Polarity）的回调 API。

<a id="r_gab1f1d2db116913e4c0e451f57fb76d2c"></a>

```c
typedef int(* tcpc_api_transmit_data_t) (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_api_transmit_data_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab1f1d2db116913e4c0e451f57fb76d2c)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

发送 PD 消息（PD Message）的回调 API。

<a id="r_ga99bb0b6056fb353fe15fc2d717f1a724"></a>

```c
typedef int(* tcpc_api_dump_std_reg_t) (const struct device *dev)
```

相关声明：[tcpc_api_dump_std_reg_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga99bb0b6056fb353fe15fc2d717f1a724)、[device](../device_reference/P002_设备对象结构.md)。

转储标准 TCPC 寄存器（Standard TCPC Registers）的回调 API。

<a id="r_gaa309db76ccb877d1cd9797d34bc55900"></a>

```c
typedef int(* tcpc_api_mask_status_register_t) (const struct device *dev, enum tcpc_status_reg reg, uint32_t mask)
```

相关声明：[tcpc_api_mask_status_register_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaa309db76ccb877d1cd9797d34bc55900)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

屏蔽或取消屏蔽状态寄存器位（Status Register Bits）的回调 API。

<a id="r_ga238a927c4602269c48325d06d0f72215"></a>

```c
typedef int(* tcpc_api_set_debug_accessory_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_debug_accessory_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga238a927c4602269c48325d06d0f72215)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用调试附件控制（Debug Accessory Control）的回调 API。

<a id="r_ga483cbf6d74b5a892d8d241ccc8f6060e"></a>

```c
typedef int(* tcpc_api_set_debug_detach_t) (const struct device *dev)
```

相关声明：[tcpc_api_set_debug_detach_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga483cbf6d74b5a892d8d241ccc8f6060e)、[device](../device_reference/P002_设备对象结构.md)。

从调试连接（Debug Connection）断开的回调 API。

<a id="r_ga56db121a729ffbb9173fe03fe867add1"></a>

```c
typedef int(* tcpc_api_set_drp_toggle_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_drp_toggle_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga56db121a729ffbb9173fe03fe867add1)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用双角色电源端口切换（DRP Toggle）的回调 API。

<a id="r_gabafb00fd478d682be7d33379b2c2487e"></a>

```c
typedef int(* tcpc_api_get_snk_ctrl_t) (const struct device *dev)
```

相关声明：[tcpc_api_get_snk_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gabafb00fd478d682be7d33379b2c2487e)、[device](../device_reference/P002_设备对象结构.md)。

查询 VBUS 受电控制状态（VBUS Sink Control State）的回调 API。

<a id="r_gaaed7c7d360c5eb455d84164fc4ee2d1d"></a>

```c
typedef int(* tcpc_api_set_snk_ctrl_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_snk_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaaed7c7d360c5eb455d84164fc4ee2d1d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VBUS 受电（VBUS Sinking）的回调 API。

<a id="r_ga2da6efeb17079086b4dc7ac52d2e60e7"></a>

```c
typedef int(* tcpc_api_get_src_ctrl_t) (const struct device *dev)
```

相关声明：[tcpc_api_get_src_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga2da6efeb17079086b4dc7ac52d2e60e7)、[device](../device_reference/P002_设备对象结构.md)。

查询 VBUS 供电控制状态（VBUS Source Control State）的回调 API。

<a id="r_ga8863bafbd43a21204b990aa74d710285"></a>

```c
typedef int(* tcpc_api_set_src_ctrl_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_src_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga8863bafbd43a21204b990aa74d710285)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VBUS 供电（VBUS Sourcing）的回调 API。

<a id="r_gac6f9724f73200ca20f1aa0a519928e50"></a>

```c
typedef int(* tcpc_api_get_chip_info_t) (const struct device *dev, struct tcpc_chip_info *chip_info)
```

相关声明：[tcpc_api_get_chip_info_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gac6f9724f73200ca20f1aa0a519928e50)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

读取 TCPC 芯片信息（TCPC Chip Information）的回调 API。

<a id="r_gae3339cd538cf4025f9f6e0959647e430"></a>

```c
typedef int(* tcpc_api_set_low_power_mode_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_low_power_mode_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae3339cd538cf4025f9f6e0959647e430)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

进入或退出低功耗模式（Low Power Mode）的回调 API。

<a id="r_ga232b5d184f585aab94eb22daaf06c86b"></a>

```c
typedef int(* tcpc_api_sop_prime_enable_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_sop_prime_enable_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga232b5d184f585aab94eb22daaf06c86b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 `SOP'`／`SOP''` 接收（Reception）的回调 API。

<a id="r_gaea02443c9aeb62583903291908a660cd"></a>

```c
typedef int(* tcpc_api_set_bist_test_mode_t) (const struct device *dev, bool enable)
```

相关声明：[tcpc_api_set_bist_test_mode_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaea02443c9aeb62583903291908a660cd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用内建自测试模式（BIST Test Mode）的回调 API。

<a id="r_ga511cdf626c88790199edbd2fd578a833"></a>

```c
typedef int(* tcpc_api_set_alert_handler_cb_t) (const struct device *dev, tcpc_alert_handler_cb_t handler, void *data)
```

相关声明：[tcpc_api_set_alert_handler_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga511cdf626c88790199edbd2fd578a833)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)。

注册警报应用回调（Alert Application Callback）的回调 API。

<a id="r_ga0dfa332e501412fb407ef2490a042e11"></a>

```c
typedef int(* tcpc_api_dead_battery_enabled_t) (const struct device *dev, bool *enabled)
```

相关声明：[tcpc_api_dead_battery_enabled_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga0dfa332e501412fb407ef2490a042e11)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPC 无电池电量配置（Dead Battery Configuration）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga4687047910cad0dd970bbd28adcf22ed"></a>

```c
enum tcpc_alert { TCPC_ALERT_CC_STATUS , TCPC_ALERT_POWER_STATUS , TCPC_ALERT_MSG_STATUS , TCPC_ALERT_HARD_RESET_RECEIVED , TCPC_ALERT_TRANSMIT_MSG_FAILED , TCPC_ALERT_TRANSMIT_MSG_DISCARDED , TCPC_ALERT_TRANSMIT_MSG_SUCCESS , TCPC_ALERT_VBUS_ALARM_HI , TCPC_ALERT_VBUS_ALARM_LO , TCPC_ALERT_FAULT_STATUS , TCPC_ALERT_RX_BUFFER_OVERFLOW , TCPC_ALERT_VBUS_SNK_DISCONNECT , TCPC_ALERT_BEGINNING_MSG_STATUS , TCPC_ALERT_EXTENDED_STATUS , TCPC_ALERT_EXTENDED , TCPC_ALERT_VENDOR_DEFINED }
```

相关声明：[tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)、[TCPC_ALERT_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f)、[TCPC_ALERT_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4)、[TCPC_ALERT_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb)、[TCPC_ALERT_HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0)、[TCPC_ALERT_TRANSMIT_MSG_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec)、[TCPC_ALERT_TRANSMIT_MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe)、[TCPC_ALERT_TRANSMIT_MSG_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2)、[TCPC_ALERT_VBUS_ALARM_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66)、[TCPC_ALERT_VBUS_ALARM_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0)、[TCPC_ALERT_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e)、[TCPC_ALERT_RX_BUFFER_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752)、[TCPC_ALERT_VBUS_SNK_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd)、[TCPC_ALERT_BEGINNING_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb)、[TCPC_ALERT_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9)、[TCPC_ALERT_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25)、[TCPC_ALERT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)。

TCPC 警报位（Alert Bits）。

<a id="r_gafd8253dfa6abc80d0717b17271ed8916"></a>

```c
enum tcpc_status_reg { TCPC_ALERT_STATUS , TCPC_CC_STATUS , TCPC_POWER_STATUS , TCPC_FAULT_STATUS , TCPC_EXTENDED_STATUS , TCPC_EXTENDED_ALERT_STATUS , TCPC_VENDOR_DEFINED_STATUS }
```

相关声明：[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[TCPC_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b)、[TCPC_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4)、[TCPC_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f)、[TCPC_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440)、[TCPC_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d)、[TCPC_EXTENDED_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db)、[TCPC_VENDOR_DEFINED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)。

TCPC 状态寄存器（Status Register）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_ga6dfd68915ffe093058f6187b770a2436"></a>

```c
static int tcpc_is_cc_rp (enum tc_cc_voltage_state cc)
```

相关声明：[tcpc_is_cc_rp](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga6dfd68915ffe093058f6187b770a2436)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

返回受电端（Sink）是否在对端检测到 Rp 电阻。

<a id="r_ga0db896e395812603a03548b8faac6791"></a>

```c
static int tcpc_is_cc_open (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_open](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0db896e395812603a03548b8faac6791)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

两条 CC 线路都完全开路（Completely Open）时返回 `true`。

<a id="r_gaa0d2059c3a53df986150141f73b9a98a"></a>

```c
static int tcpc_is_cc_snk_dbg_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_snk_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa0d2059c3a53df986150141f73b9a98a)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

检测到端口伙伴（Port Partner）为受电端调试附件（Sink Debug Accessory）时返回 `true`。

<a id="r_ga03849a7a4fd7f468b18838c443d1ecd8"></a>

```c
static int tcpc_is_cc_src_dbg_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_src_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03849a7a4fd7f468b18838c443d1ecd8)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

检测到端口伙伴（Port Partner）为供电端调试附件（Source Debug Accessory）时返回 `true`。

<a id="r_ga153054be89d5f21148fe3ee750c718ee"></a>

```c
static int tcpc_is_cc_audio_acc (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_audio_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga153054be89d5f21148fe3ee750c718ee)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）为音频附件（Audio Accessory）时返回 `true`。

<a id="r_gab4e9cc812679cf8cb0189f73a28d7cd2"></a>

```c
static int tcpc_is_cc_at_least_one_rd (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_at_least_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab4e9cc812679cf8cb0189f73a28d7cd2)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）至少接入了一个 Rd 电阻时返回 `true`。

<a id="r_ga91c3c40ea82ce5a081918183d8b76c06"></a>

```c
static int tcpc_is_cc_only_one_rd (enum tc_cc_voltage_state cc1, enum tc_cc_voltage_state cc2)
```

相关声明：[tcpc_is_cc_only_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91c3c40ea82ce5a081918183d8b76c06)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

端口伙伴（Port Partner）仅在一条 CC 线路上接入 Rd 电阻时返回 `true`。

<a id="r_gabc50daa9cc713b1d0e340007e3850ca8"></a>

```c
static int tcpc_init (const struct device *dev)
```

相关声明：[tcpc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gabc50daa9cc713b1d0e340007e3850ca8)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Type-C 端口控制器（TCPC）。

<a id="r_ga66ab7a9f3cd1b80cd5bc8e99040c5627"></a>

```c
static int tcpc_get_cc (const struct device *dev, enum tc_cc_voltage_state *cc1, enum tc_cc_voltage_state *cc2)
```

相关声明：[tcpc_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga66ab7a9f3cd1b80cd5bc8e99040c5627)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)、[tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)。

读取 CC 线路状态（CC Line Status）。

<a id="r_ga3958eac0cc0b9b2ac782e0cdb235036c"></a>

```c
static int tcpc_select_rp_value (const struct device *dev, enum tc_rp_value rp)
```

相关声明：[tcpc_select_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3958eac0cc0b9b2ac782e0cdb235036c)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

设置作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

<a id="r_ga25a110be90977e768623f3a0c9a222d5"></a>

```c
static int tcpc_get_rp_value (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[tcpc_get_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga25a110be90977e768623f3a0c9a222d5)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取作为供电端（Source）工作时使用的 CC 上拉电阻值（CC Pull-up Resistor Value）。

<a id="r_gac5737d02caa2b9e649b469bcd648440f"></a>

```c
static int tcpc_set_cc (const struct device *dev, enum tc_cc_pull pull)
```

相关声明：[tcpc_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gac5737d02caa2b9e649b469bcd648440f)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)。

设置 CC 上拉／下拉电阻（CC Pull Resistor），并将角色设为供电端（Source）或受电端（Sink）。

<a id="r_ga1f057bcddc5a7757370f2e6de8170128"></a>

```c
static void tcpc_set_vconn_cb (const struct device *dev, tcpc_vconn_control_cb_t vconn_cb, const struct device *usbc_dev)
```

相关声明：[tcpc_set_vconn_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga1f057bcddc5a7757370f2e6de8170128)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)、[device](../device_reference/P002_设备对象结构.md)。

设置可启用或禁用 VCONN 的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

<a id="r_ga71981a635ad82b9db41d549f29ad5c68"></a>

```c
static void tcpc_set_vconn_discharge_cb (const struct device *dev, tcpc_vconn_discharge_cb_t cb, const struct device *usbc_dev)
```

相关声明：[tcpc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga71981a635ad82b9db41d549f29ad5c68)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)、[device](../device_reference/P002_设备对象结构.md)。

设置可启用 VCONN 或对其放电的回调（Callback），用于 TCPC 无法控制 VCONN，或系统配置为不使用 TCPC 的 VCONN 控制能力的情况。

<a id="r_ga3937d66636a2b22422caf11c48f7628a"></a>

```c
static int tcpc_vconn_discharge (const struct device *dev, bool enable)
```

相关声明：[tcpc_vconn_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3937d66636a2b22422caf11c48f7628a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

对 VCONN 放电（Discharge VCONN）。

<a id="r_ga247f0ea91249753d6f5eefe006617e41"></a>

```c
static int tcpc_set_vconn (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_vconn](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga247f0ea91249753d6f5eefe006617e41)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 VCONN。

<a id="r_ga8d30c961335f62faa33aa7d842422da0"></a>

```c
static int tcpc_set_roles (const struct device *dev, enum tc_power_role power_role, enum tc_data_role data_role)
```

相关声明：[tcpc_set_roles](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8d30c961335f62faa33aa7d842422da0)、[device](../device_reference/P002_设备对象结构.md)、[tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)。

设置 PD 消息头部（PD Message Header）的电源角色（Power Role）和数据角色（Data Role）。

<a id="r_ga34e4caefb0f660b170f97956ac57b707"></a>

```c
static int tcpc_get_rx_pending_msg (const struct device *dev, struct pd_msg *buf)
```

相关声明：[tcpc_get_rx_pending_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga34e4caefb0f660b170f97956ac57b707)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

从 TCPC 获取电力传输消息（Power Delivery Message）。

<a id="r_ga905176a77ff127f4df8f6a4f2c61a1b7"></a>

```c
static int tcpc_set_rx_enable (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga905176a77ff127f4df8f6a4f2c61a1b7)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 SOP* 消息类型的接收（Reception）。

<a id="r_ga53f0207ecb63011c6dfc3c298a841ed4"></a>

```c
static int tcpc_set_cc_polarity (const struct device *dev, enum tc_cc_polarity polarity)
```

相关声明：[tcpc_set_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga53f0207ecb63011c6dfc3c298a841ed4)、[device](../device_reference/P002_设备对象结构.md)、[tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)。

设置 CC 线路极性（CC Line Polarity）。

<a id="r_ga8bf8fd202d582a4cc179a0fc4aff35e1"></a>

```c
static int tcpc_transmit_data (const struct device *dev, struct pd_msg *msg)
```

相关声明：[tcpc_transmit_data](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8bf8fd202d582a4cc179a0fc4aff35e1)、[device](../device_reference/P002_设备对象结构.md)、[pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)。

发送电力传输消息（Power Delivery Message）。

<a id="r_ga91eef7084b523f1991e000f0592b8cbd"></a>

```c
static int tcpc_dump_std_reg (const struct device *dev)
```

相关声明：[tcpc_dump_std_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91eef7084b523f1991e000f0592b8cbd)、[device](../device_reference/P002_设备对象结构.md)。

转储一组 TCPC 寄存器（Registers）。

<a id="r_ga75f0dc246dac576f14c5ac51b45fd489"></a>

```c
static int tcpc_set_alert_handler_cb (const struct device *dev, tcpc_alert_handler_cb_t handler, void *data)
```

相关声明：[tcpc_set_alert_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga75f0dc246dac576f14c5ac51b45fd489)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)。

设置警报函数（Alert Function），由警报位（Alert Bit）触发中断时调用。

<a id="r_ga0d1868d555e99877e062fb7135d9db8f"></a>

```c
static int tcpc_mask_status_register (const struct device *dev, enum tcpc_status_reg reg, uint32_t mask)
```

相关声明：[tcpc_mask_status_register](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0d1868d555e99877e062fb7135d9db8f)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置 TCPC 状态寄存器的掩码（Status Register Mask）。

<a id="r_ga01687aa218b25ba137e994a2a55bce23"></a>

```c
static int tcpc_set_debug_accessory (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_debug_accessory](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga01687aa218b25ba137e994a2a55bce23)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

手动控制 TCPC 调试附件控制功能（DebugAccessory Control）。

<a id="r_gaaa38e56e6bc8c41e936d8ed70aaa8a23"></a>

```c
static int tcpc_set_debug_detach (const struct device *dev)
```

相关声明：[tcpc_set_debug_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaaa38e56e6bc8c41e936d8ed70aaa8a23)、[device](../device_reference/P002_设备对象结构.md)。

从调试连接（Debug Connection）断开。

<a id="r_gaa06e156bef46ff3f70cc8c302ddf0a4d"></a>

```c
static int tcpc_set_drp_toggle (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_drp_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa06e156bef46ff3f70cc8c302ddf0a4d)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 TCPC 自动双角色切换（Auto Dual Role Toggle）。

<a id="r_ga0c1cd7bc86c89abf5e348987d34e4623"></a>

```c
static int tcpc_get_snk_ctrl (const struct device *dev)
```

相关声明：[tcpc_get_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0c1cd7bc86c89abf5e348987d34e4623)、[device](../device_reference/P002_设备对象结构.md)。

查询 TCPC 当前受电状态（Sinking State）。

<a id="r_ga7a63d55cbe5de1d89aa76e10df0140ed"></a>

```c
static int tcpc_set_snk_ctrl (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga7a63d55cbe5de1d89aa76e10df0140ed)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 TCPC 的 VBUS 受电状态（VBUS Sinking State）。

<a id="r_ga03c8c6fc6f4c6adefacbc809588e1f85"></a>

```c
static int tcpc_get_src_ctrl (const struct device *dev)
```

相关声明：[tcpc_get_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03c8c6fc6f4c6adefacbc809588e1f85)、[device](../device_reference/P002_设备对象结构.md)。

查询 TCPC 当前供电状态（Sourcing State）。

<a id="r_ga8f06b257d1bd0a17eb3042d204b2e6cd"></a>

```c
static int tcpc_set_src_ctrl (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8f06b257d1bd0a17eb3042d204b2e6cd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 TCPC 的 VBUS 供电状态（VBUS Sourcing State）。

<a id="r_gaccc728a1f27c59a163a5c0a221ab7c18"></a>

```c
static int tcpc_set_bist_test_mode (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_bist_test_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaccc728a1f27c59a163a5c0a221ab7c18)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制 TCPC 的内建自测试模式（BIST Mode）。

<a id="r_ga894d24140f8675b4f48d759c27f52076"></a>

```c
static int tcpc_get_chip_info (const struct device *dev, struct tcpc_chip_info *chip_info)
```

相关声明：[tcpc_get_chip_info](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga894d24140f8675b4f48d759c27f52076)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)。

获取 TCPC 固件版本（Firmware Version）。

<a id="r_ga961a4dc393d58dc44ea19a62c943ed48"></a>

```c
static int tcpc_set_low_power_mode (const struct device *dev, bool enable)
```

相关声明：[tcpc_set_low_power_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga961a4dc393d58dc44ea19a62c943ed48)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

指示 TCPC 进入或退出低功耗模式（Low Power Mode）。

<a id="r_gab0f1f5d47c1e2b8ee9eb3d7875a0051e"></a>

```c
static int tcpc_sop_prime_enable (const struct device *dev, bool enable)
```

相关声明：[tcpc_sop_prime_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 SOP Prime 消息的接收，并可选择启用 SOP Double Prime 消息的接收。

<a id="r_gaac29d0958fd377db24f1911cfa03188c"></a>

```c
static int tcpc_dead_battery_enabled (const struct device *dev, bool *enabled)
```

相关声明：[tcpc_dead_battery_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaac29d0958fd377db24f1911cfa03188c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

查询 TCPC 是否施加 USB-C 电池耗尽端接（Dead Battery Terminations）。


## 14.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [usbc_tc.h](../api_source_reference/P891_usbc_tc.h_源码浏览.md)
- [usbc_pd.h](../api_source_reference/P890_usbc_pd.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P892_usbc_tcpc.h_源码浏览.md)
- [tcpc_chip_info](../device_power_control_model_reference/P093_tcpc_chip_info_结构体.md)
- [tcpc_driver_api](../device_power_control_model_reference/P094_tcpc_driver_api_结构体.md)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_cc_polarity](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gac5b4b58840c9b076a869a5816ba100db)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [tcpc_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga5f42fa12f90d34961eeeb67c0dc4f925)
- [tcpc_alert](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4687047910cad0dd970bbd28adcf22ed)
- [tcpc_api_init_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae28524287fdb5504883afb66003d035c)
- [tcpc_api_get_cc_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga39981c9b68e280de660ca15e137ffbd0)
- [tc_cc_voltage_state](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga64e32ec2da97f70fd5b96975317cb92c)
- [tcpc_api_select_rp_value_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae749f76083de380e2edd602dc0e30402)
- [tc_rp_value](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [tcpc_api_get_rp_value_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gad1db9d036dd666846065bbf35ea22177)
- [tcpc_api_set_cc_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gac524dbe59d67fb5bdfad78bc1a4d64c9)
- [tc_cc_pull](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga0200c820510eb786f3ca30a9b5f7aada)
- [tcpc_api_set_vconn_discharge_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gad8d3e1b467e6ee4fb58dcfed16117737)
- [tcpc_api_set_vconn_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga26217be69c8bc7ea24e6cabe489445da)
- [tcpc_api_vconn_discharge_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab503f46443ce870dd0baeebf8dd48e8f)
- [tcpc_api_set_vconn_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaf8d6f41fdd6fe99a1b629d361556966d)
- [tcpc_api_set_roles_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gadc6b26855f37fe94391f294c7f63d5bd)
- [tc_power_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [tc_data_role](../api_usb_gnss_topic_reference/P014_USB Type-C API主题.md#ga6b98bbe238e62cfd5531688494a63de2)
- [tcpc_api_get_rx_pending_msg_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab0828b95c31b6d6523ca471dd68ec065)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [tcpc_api_set_rx_enable_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga7cd4aae87502bf5ebb1939edceea81f3)
- [tcpc_api_set_cc_polarity_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaa791f068d25e28abbd7d45071a5016be)
- [tcpc_api_transmit_data_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gab1f1d2db116913e4c0e451f57fb76d2c)
- [tcpc_api_dump_std_reg_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga99bb0b6056fb353fe15fc2d717f1a724)
- [tcpc_api_mask_status_register_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaa309db76ccb877d1cd9797d34bc55900)
- [tcpc_status_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gafd8253dfa6abc80d0717b17271ed8916)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tcpc_api_set_debug_accessory_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga238a927c4602269c48325d06d0f72215)
- [tcpc_api_set_debug_detach_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga483cbf6d74b5a892d8d241ccc8f6060e)
- [tcpc_api_set_drp_toggle_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga56db121a729ffbb9173fe03fe867add1)
- [tcpc_api_get_snk_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gabafb00fd478d682be7d33379b2c2487e)
- [tcpc_api_set_snk_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaaed7c7d360c5eb455d84164fc4ee2d1d)
- [tcpc_api_get_src_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga2da6efeb17079086b4dc7ac52d2e60e7)
- [tcpc_api_set_src_ctrl_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga8863bafbd43a21204b990aa74d710285)
- [tcpc_api_get_chip_info_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gac6f9724f73200ca20f1aa0a519928e50)
- [tcpc_api_set_low_power_mode_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gae3339cd538cf4025f9f6e0959647e430)
- [tcpc_api_sop_prime_enable_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga232b5d184f585aab94eb22daaf06c86b)
- [tcpc_api_set_bist_test_mode_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#gaea02443c9aeb62583903291908a660cd)
- [tcpc_api_set_alert_handler_cb_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga511cdf626c88790199edbd2fd578a833)
- [tcpc_api_dead_battery_enabled_t](../api_flash_connection_topic_reference/P010_USB Type-C 端口控制器驱动后端 API.md#ga0dfa332e501412fb407ef2490a042e11)
- [TCPC_ALERT_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda30b8a2c88cc2309849efa9d478271a3f)
- [TCPC_ALERT_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edabbce6e484dc5373597097a664a6b5af4)
- [TCPC_ALERT_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda57eedbbbb9b1d899e1607e25c2799eeb)
- [TCPC_ALERT_HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda61c51ceb776d0432c657f6c16d5595e0)
- [TCPC_ALERT_TRANSMIT_MSG_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edadff8e9cab783e22eedad2971baae77ec)
- [TCPC_ALERT_TRANSMIT_MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda302c30d41b09b4bf1949ce0c945c71fe)
- [TCPC_ALERT_TRANSMIT_MSG_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda642e2b837d88dc983177546a06d938b2)
- [TCPC_ALERT_VBUS_ALARM_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda64f5af2ef616a1adf90ff3549a114a66)
- [TCPC_ALERT_VBUS_ALARM_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac44bb12fb7bd9de2f49af7d5f72744b0)
- [TCPC_ALERT_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edacd3a5188b6be126dfd00a4676e2a768e)
- [TCPC_ALERT_RX_BUFFER_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edaefb353c046fa8346a4736d02a3003752)
- [TCPC_ALERT_VBUS_SNK_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda8aa0d4566f11e6079f59500ac03929cd)
- [TCPC_ALERT_BEGINNING_MSG_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda449d3f9271aa42feb43e54a1f36114eb)
- [TCPC_ALERT_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda284b478e32999fd923ba3064088274a9)
- [TCPC_ALERT_EXTENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22eda4356cb85ef371e72badad22110172e25)
- [TCPC_ALERT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gga4687047910cad0dd970bbd28adcf22edac5675390dfba5276227ff8d2be783992)
- [TCPC_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a3b639f1629de38eb9c29d6af24f5011b)
- [TCPC_CC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aaf41a51cc8e4c849780af463ea63a0c4)
- [TCPC_POWER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916aa42f110436df796f5cfdadab921aac7f)
- [TCPC_FAULT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a14723bbaaae32413e2399159a6def440)
- [TCPC_EXTENDED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916afe72a3bc04d7f92bd74e754129e99c6d)
- [TCPC_EXTENDED_ALERT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a5e15cc2aae46edf6b7e0f5316b37a9db)
- [TCPC_VENDOR_DEFINED_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ggafd8253dfa6abc80d0717b17271ed8916a45f424f2f0e126085d3e49e0cc4d7c61)
- [tcpc_is_cc_rp](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga6dfd68915ffe093058f6187b770a2436)
- [tcpc_is_cc_open](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0db896e395812603a03548b8faac6791)
- [tcpc_is_cc_snk_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa0d2059c3a53df986150141f73b9a98a)
- [tcpc_is_cc_src_dbg_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03849a7a4fd7f468b18838c443d1ecd8)
- [tcpc_is_cc_audio_acc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga153054be89d5f21148fe3ee750c718ee)
- [tcpc_is_cc_at_least_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab4e9cc812679cf8cb0189f73a28d7cd2)
- [tcpc_is_cc_only_one_rd](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91c3c40ea82ce5a081918183d8b76c06)
- [tcpc_init](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gabc50daa9cc713b1d0e340007e3850ca8)
- [tcpc_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga66ab7a9f3cd1b80cd5bc8e99040c5627)
- [tcpc_select_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3958eac0cc0b9b2ac782e0cdb235036c)
- [tcpc_get_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga25a110be90977e768623f3a0c9a222d5)
- [tcpc_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gac5737d02caa2b9e649b469bcd648440f)
- [tcpc_set_vconn_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga1f057bcddc5a7757370f2e6de8170128)
- [tcpc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga71981a635ad82b9db41d549f29ad5c68)
- [tcpc_vconn_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga3937d66636a2b22422caf11c48f7628a)
- [tcpc_set_vconn](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga247f0ea91249753d6f5eefe006617e41)
- [tcpc_set_roles](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8d30c961335f62faa33aa7d842422da0)
- [tcpc_get_rx_pending_msg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga34e4caefb0f660b170f97956ac57b707)
- [tcpc_set_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga905176a77ff127f4df8f6a4f2c61a1b7)
- [tcpc_set_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga53f0207ecb63011c6dfc3c298a841ed4)
- [tcpc_transmit_data](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8bf8fd202d582a4cc179a0fc4aff35e1)
- [tcpc_dump_std_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga91eef7084b523f1991e000f0592b8cbd)
- [tcpc_set_alert_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga75f0dc246dac576f14c5ac51b45fd489)
- [tcpc_mask_status_register](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0d1868d555e99877e062fb7135d9db8f)
- [tcpc_set_debug_accessory](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga01687aa218b25ba137e994a2a55bce23)
- [tcpc_set_debug_detach](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaaa38e56e6bc8c41e936d8ed70aaa8a23)
- [tcpc_set_drp_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaa06e156bef46ff3f70cc8c302ddf0a4d)
- [tcpc_get_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga0c1cd7bc86c89abf5e348987d34e4623)
- [tcpc_set_snk_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga7a63d55cbe5de1d89aa76e10df0140ed)
- [tcpc_get_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga03c8c6fc6f4c6adefacbc809588e1f85)
- [tcpc_set_src_ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga8f06b257d1bd0a17eb3042d204b2e6cd)
- [tcpc_set_bist_test_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaccc728a1f27c59a163a5c0a221ab7c18)
- [tcpc_get_chip_info](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga894d24140f8675b4f48d759c27f52076)
- [tcpc_set_low_power_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga961a4dc393d58dc44ea19a62c943ed48)
- [tcpc_sop_prime_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gab0f1f5d47c1e2b8ee9eb3d7875a0051e)
- [tcpc_dead_battery_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#gaac29d0958fd377db24f1911cfa03188c)

<a id="header-details"></a>

---

[上一章](P013_zephyr__drivers__usb_c__usbc_pd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__net__wifi.h_文件参考.md)
