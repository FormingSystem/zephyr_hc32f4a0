---
id: learning.zephyr-docs.device-power-control-model-reference.page-94
title: tcpc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtcpc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_tcpc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtcpc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：USB Type-C端口控制器（Port Controller）驱动操作。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：USB Type-C 端口控制器（Port Controller，TCPC）驱动操作。这是每个 USB Type-C 端口控制器驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_ae4cf25f8c0c5f0020c0d57b9dc6bdb4c"></a>

```c
tcpc_api_init_t init
```

相关声明：[tcpc_api_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae28524287fdb5504883afb66003d035c)、[init](#ae4cf25f8c0c5f0020c0d57b9dc6bdb4c)。

`REQ`：初始化 TCPC。

<a id="r_af483dc0041006ad9bb717ffc4b570978"></a>

```c
tcpc_api_get_cc_t get_cc
```

相关声明：[tcpc_api_get_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga39981c9b68e280de660ca15e137ffbd0)、[get_cc](#af483dc0041006ad9bb717ffc4b570978)。

`OPT`：读取配置通道（Configuration Channel，CC）线的状态。

<a id="r_a3ef2690b032843d0d8e3ca3c675428cf"></a>

```c
tcpc_api_select_rp_value_t select_rp_value
```

相关声明：[tcpc_api_select_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae749f76083de380e2edd602dc0e30402)、[select_rp_value](#a3ef2690b032843d0d8e3ca3c675428cf)。

`OPT`：设置作为供电方（Source）运行时使用的 CC 上拉电阻值。

<a id="r_a49f69dcc86e944e7d922bcadab949194"></a>

```c
tcpc_api_get_rp_value_t get_rp_value
```

相关声明：[tcpc_api_get_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad1db9d036dd666846065bbf35ea22177)、[get_rp_value](#a49f69dcc86e944e7d922bcadab949194)。

`OPT`：获取作为供电方（Source）运行时使用的 CC 上拉电阻值。

<a id="r_a6938fec4089908809cbd101095a5c4f8"></a>

```c
tcpc_api_set_cc_t set_cc
```

相关声明：[tcpc_api_set_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac524dbe59d67fb5bdfad78bc1a4d64c9)、[set_cc](#a6938fec4089908809cbd101095a5c4f8)。

`REQ`：设置 CC 上拉/下拉电阻，并将角色设为供电方（Source）或受电方（Sink）。

<a id="r_af04de5dd092efeb32a23e21cda5033c0"></a>

```c
tcpc_api_set_vconn_discharge_cb_t set_vconn_discharge_cb
```

相关声明：[tcpc_api_set_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad8d3e1b467e6ee4fb58dcfed16117737)、[set_vconn_discharge_cb](#af04de5dd092efeb32a23e21cda5033c0)。

`REQ`：设置能够启用 VCONN 或对其放电的回调。当 TCPC 无法执行这些操作，或系统配置为不使用 TCPC 的 VCONN 控制能力时，使用此回调。

<a id="r_a022918a3098b5b2cbba9d660f8f05a0a"></a>

```c
tcpc_api_set_vconn_cb_t set_vconn_cb
```

相关声明：[tcpc_api_set_vconn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga26217be69c8bc7ea24e6cabe489445da)、[set_vconn_cb](#a022918a3098b5b2cbba9d660f8f05a0a)。

`REQ`：设置能够启用或禁用 VCONN 的回调。当 TCPC 无法执行这些操作，或系统配置为不使用 TCPC 的 VCONN 控制能力时，使用此回调。

<a id="r_adc8f34eefe17f59953bba2029fcaa4bc"></a>

```c
tcpc_api_vconn_discharge_t vconn_discharge
```

相关声明：[tcpc_api_vconn_discharge_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab503f46443ce870dd0baeebf8dd48e8f)、[vconn_discharge](#adc8f34eefe17f59953bba2029fcaa4bc)。

`OPT`：对 VCONN 放电。

<a id="r_a536fbd074107f6a2b65e553f8acd1d0b"></a>

```c
tcpc_api_set_vconn_t set_vconn
```

相关声明：[tcpc_api_set_vconn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaf8d6f41fdd6fe99a1b629d361556966d)、[set_vconn](#a536fbd074107f6a2b65e553f8acd1d0b)。

`OPT`：启用或禁用 VCONN。

<a id="r_ae5c9719810866d0fcc03f329c84b3a58"></a>

```c
tcpc_api_set_roles_t set_roles
```

相关声明：[tcpc_api_set_roles_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gadc6b26855f37fe94391f294c7f63d5bd)、[set_roles](#ae5c9719810866d0fcc03f329c84b3a58)。

`OPT`：设置 USB 供电协商（Power Delivery，PD）消息头中的电源角色和数据角色（Power/Data Role）。

<a id="r_a385a741aa402403637e3f2f3f7c4c456"></a>

```c
tcpc_api_get_rx_pending_msg_t get_rx_pending_msg
```

相关声明：[tcpc_api_get_rx_pending_msg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab0828b95c31b6d6523ca471dd68ec065)、[get_rx_pending_msg](#a385a741aa402403637e3f2f3f7c4c456)。

`REQ`：从 TCPC 获取 PD 消息。

<a id="r_ac79a47b9a94fb4481bc9ecdba86b898d"></a>

```c
tcpc_api_set_rx_enable_t set_rx_enable
```

相关声明：[tcpc_api_set_rx_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga7cd4aae87502bf5ebb1939edceea81f3)、[set_rx_enable](#ac79a47b9a94fb4481bc9ecdba86b898d)。

`OPT`：启用 `SOP*` 类型消息的接收。

<a id="r_a0239a44cb7c1977ad96423e0c11f3ad6"></a>

```c
tcpc_api_set_cc_polarity_t set_cc_polarity
```

相关声明：[tcpc_api_set_cc_polarity_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa791f068d25e28abbd7d45071a5016be)、[set_cc_polarity](#a0239a44cb7c1977ad96423e0c11f3ad6)。

`REQ`：设置 CC 线的极性（Polarity）。

<a id="r_aaa0956282b1b9cf3e41dc45a9f31e073"></a>

```c
tcpc_api_transmit_data_t transmit_data
```

相关声明：[tcpc_api_transmit_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab1f1d2db116913e4c0e451f57fb76d2c)、[transmit_data](#aaa0956282b1b9cf3e41dc45a9f31e073)。

`OPT`：发送 PD 消息。

<a id="r_a212ac07d41716e76742a3db2aea2301c"></a>

```c
tcpc_api_dump_std_reg_t dump_std_reg
```

相关声明：[tcpc_api_dump_std_reg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga99bb0b6056fb353fe15fc2d717f1a724)、[dump_std_reg](#a212ac07d41716e76742a3db2aea2301c)。

`OPT`：转储一组 TCPC 寄存器。

<a id="r_adc65471e8ae2b106575b25d5c30653dd"></a>

```c
tcpc_api_mask_status_register_t mask_status_register
```

相关声明：[tcpc_api_mask_status_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa309db76ccb877d1cd9797d34bc55900)、[mask_status_register](#adc65471e8ae2b106575b25d5c30653dd)。

`OPT`：设置 TCPC 状态寄存器的掩码。

<a id="r_aaa2b59daf061965dc6ed6cb7a42b684f"></a>

```c
tcpc_api_set_debug_accessory_t set_debug_accessory
```

相关声明：[tcpc_api_set_debug_accessory_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga238a927c4602269c48325d06d0f72215)、[set_debug_accessory](#aaa2b59daf061965dc6ed6cb7a42b684f)。

`OPT`：手动控制 TCPC 的调试附件（DebugAccessory）控制功能。

<a id="r_a85c30801d61470a3bf41c27117a847ee"></a>

```c
tcpc_api_set_debug_detach_t set_debug_detach
```

相关声明：[tcpc_api_set_debug_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga483cbf6d74b5a892d8d241ccc8f6060e)、[set_debug_detach](#a85c30801d61470a3bf41c27117a847ee)。

`OPT`：断开调试连接。

<a id="r_a3ca4d4e9ff4658ae2c805cc0a7613b8a"></a>

```c
tcpc_api_set_drp_toggle_t set_drp_toggle
```

相关声明：[tcpc_api_set_drp_toggle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga56db121a729ffbb9173fe03fe867add1)、[set_drp_toggle](#a3ca4d4e9ff4658ae2c805cc0a7613b8a)。

`OPT`：启用 TCPC 自动双角色切换（Auto dual role toggle）。

<a id="r_a6f8756d7b4f4d6e2beea20b3e5176bcd"></a>

```c
tcpc_api_get_snk_ctrl_t get_snk_ctrl
```

相关声明：[tcpc_api_get_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gabafb00fd478d682be7d33379b2c2487e)、[get_snk_ctrl](#a6f8756d7b4f4d6e2beea20b3e5176bcd)。

`OPT`：查询 TCPC 当前的受电（Sinking）状态。

<a id="r_aca835517376e241345d05bf66119cb6c"></a>

```c
tcpc_api_set_snk_ctrl_t set_snk_ctrl
```

相关声明：[tcpc_api_set_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaaed7c7d360c5eb455d84164fc4ee2d1d)、[set_snk_ctrl](#aca835517376e241345d05bf66119cb6c)。

`OPT`：设置 TCPC 的 VBUS 受电状态。

<a id="r_a895901166eeedac50b48918b436ee6bc"></a>

```c
tcpc_api_get_src_ctrl_t get_src_ctrl
```

相关声明：[tcpc_api_get_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga2da6efeb17079086b4dc7ac52d2e60e7)、[get_src_ctrl](#a895901166eeedac50b48918b436ee6bc)。

`OPT`：查询 TCPC 当前的供电（Sourcing）状态。

<a id="r_a70571ced311498d1065b94d81cbf5d4e"></a>

```c
tcpc_api_set_src_ctrl_t set_src_ctrl
```

相关声明：[tcpc_api_set_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga8863bafbd43a21204b990aa74d710285)、[set_src_ctrl](#a70571ced311498d1065b94d81cbf5d4e)。

`OPT`：设置 TCPC 的 VBUS 供电状态。

<a id="r_a72ac506119d63dc10be9b497fe479e6f"></a>

```c
tcpc_api_get_chip_info_t get_chip_info
```

相关声明：[tcpc_api_get_chip_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac6f9724f73200ca20f1aa0a519928e50)、[get_chip_info](#a72ac506119d63dc10be9b497fe479e6f)。

`OPT`：获取 TCPC 固件版本。

<a id="r_a3bfecb52f9ed73b2a1eb081914197f01"></a>

```c
tcpc_api_set_low_power_mode_t set_low_power_mode
```

相关声明：[tcpc_api_set_low_power_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae3339cd538cf4025f9f6e0959647e430)、[set_low_power_mode](#a3bfecb52f9ed73b2a1eb081914197f01)。

`OPT`：指示 TCPC 进入或退出低功耗模式（Low power mode）。

<a id="r_aa1b59f3aa1ccc8684445f119d4ea75aa"></a>

```c
tcpc_api_sop_prime_enable_t sop_prime_enable
```

相关声明：[tcpc_api_sop_prime_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga232b5d184f585aab94eb22daaf06c86b)、[sop_prime_enable](#aa1b59f3aa1ccc8684445f119d4ea75aa)。

`OPT`：启用 `SOP'`（SOP Prime）消息接收，并可选启用 `SOP''`（SOP Double Prime）消息接收。

<a id="r_ab5ef4ec81c532dc054b53058b199a7e0"></a>

```c
tcpc_api_set_bist_test_mode_t set_bist_test_mode
```

相关声明：[tcpc_api_set_bist_test_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaea02443c9aeb62583903291908a660cd)、[set_bist_test_mode](#ab5ef4ec81c532dc054b53058b199a7e0)。

`OPT`：控制 TCPC 的内建自测试（BIST）模式。

<a id="r_a8cc43981c1047cc92dbed8843e6f72f0"></a>

```c
tcpc_api_set_alert_handler_cb_t set_alert_handler_cb
```

相关声明：[tcpc_api_set_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga511cdf626c88790199edbd2fd578a833)、[set_alert_handler_cb](#a8cc43981c1047cc92dbed8843e6f72f0)。

`REQ`：设置告警函数（Alert function），在告警位触发中断时调用。

<a id="r_a485a6e3409a73015fc479ada7c5170b0"></a>

```c
tcpc_api_dead_battery_enabled_t dead_battery_enabled
```

相关声明：[tcpc_api_dead_battery_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga0dfa332e501412fb407ef2490a042e11)、[dead_battery_enabled](#a485a6e3409a73015fc479ada7c5170b0)。

`OPT`：查询 TCPC 是否施加 USB-C 电池耗尽状态端接（Dead battery terminations）。

## 94.2\_详细说明（Detailed Documentation）

<a id="a485a6e3409a73015fc479ada7c5170b0"></a>

### `dead_battery_enabled`

```c
tcpc_api_dead_battery_enabled_t tcpc_driver_api::dead_battery_enabled
```

`OPT`：查询 TCPC 是否施加 USB-C 电池耗尽状态端接（Dead battery terminations）。

<a id="a212ac07d41716e76742a3db2aea2301c"></a>

### `dump_std_reg`

```c
tcpc_api_dump_std_reg_t tcpc_driver_api::dump_std_reg
```

`OPT`：转储一组 TCPC 寄存器。

<a id="af483dc0041006ad9bb717ffc4b570978"></a>

### `get_cc`

```c
tcpc_api_get_cc_t tcpc_driver_api::get_cc
```

`OPT`：读取配置通道（Configuration Channel，CC）线的状态。

<a id="a72ac506119d63dc10be9b497fe479e6f"></a>

### `get_chip_info`

```c
tcpc_api_get_chip_info_t tcpc_driver_api::get_chip_info
```

`OPT`：获取 TCPC 固件版本。

<a id="a49f69dcc86e944e7d922bcadab949194"></a>

### `get_rp_value`

```c
tcpc_api_get_rp_value_t tcpc_driver_api::get_rp_value
```

`OPT`：获取作为供电方（Source）运行时使用的 CC 上拉电阻值。

<a id="a385a741aa402403637e3f2f3f7c4c456"></a>

### `get_rx_pending_msg`

```c
tcpc_api_get_rx_pending_msg_t tcpc_driver_api::get_rx_pending_msg
```

`REQ`：从 TCPC 获取 PD 消息。

<a id="a6f8756d7b4f4d6e2beea20b3e5176bcd"></a>

### `get_snk_ctrl`

```c
tcpc_api_get_snk_ctrl_t tcpc_driver_api::get_snk_ctrl
```

`OPT`：查询 TCPC 当前的受电（Sinking）状态。

<a id="a895901166eeedac50b48918b436ee6bc"></a>

### `get_src_ctrl`

```c
tcpc_api_get_src_ctrl_t tcpc_driver_api::get_src_ctrl
```

`OPT`：查询 TCPC 当前的供电（Sourcing）状态。

<a id="ae4cf25f8c0c5f0020c0d57b9dc6bdb4c"></a>

### `init`

```c
tcpc_api_init_t tcpc_driver_api::init
```

`REQ`：初始化 TCPC。

<a id="adc65471e8ae2b106575b25d5c30653dd"></a>

### `mask_status_register`

```c
tcpc_api_mask_status_register_t tcpc_driver_api::mask_status_register
```

`OPT`：设置 TCPC 状态寄存器的掩码。

<a id="a3ef2690b032843d0d8e3ca3c675428cf"></a>

### `select_rp_value`

```c
tcpc_api_select_rp_value_t tcpc_driver_api::select_rp_value
```

`OPT`：设置作为供电方（Source）运行时使用的 CC 上拉电阻值。

<a id="a8cc43981c1047cc92dbed8843e6f72f0"></a>

### `set_alert_handler_cb`

```c
tcpc_api_set_alert_handler_cb_t tcpc_driver_api::set_alert_handler_cb
```

`REQ`：设置告警函数（Alert function），在告警位触发中断时调用。

<a id="ab5ef4ec81c532dc054b53058b199a7e0"></a>

### `set_bist_test_mode`

```c
tcpc_api_set_bist_test_mode_t tcpc_driver_api::set_bist_test_mode
```

`OPT`：控制 TCPC 的内建自测试（BIST）模式。

<a id="a6938fec4089908809cbd101095a5c4f8"></a>

### `set_cc`

```c
tcpc_api_set_cc_t tcpc_driver_api::set_cc
```

`REQ`：设置 CC 上拉/下拉电阻，并将角色设为供电方（Source）或受电方（Sink）。

<a id="a0239a44cb7c1977ad96423e0c11f3ad6"></a>

### `set_cc_polarity`

```c
tcpc_api_set_cc_polarity_t tcpc_driver_api::set_cc_polarity
```

`REQ`：设置 CC 线的极性（Polarity）。

<a id="aaa2b59daf061965dc6ed6cb7a42b684f"></a>

### `set_debug_accessory`

```c
tcpc_api_set_debug_accessory_t tcpc_driver_api::set_debug_accessory
```

`OPT`：手动控制 TCPC 的调试附件（DebugAccessory）控制功能。

<a id="a85c30801d61470a3bf41c27117a847ee"></a>

### `set_debug_detach`

```c
tcpc_api_set_debug_detach_t tcpc_driver_api::set_debug_detach
```

`OPT`：断开调试连接。

<a id="a3ca4d4e9ff4658ae2c805cc0a7613b8a"></a>

### `set_drp_toggle`

```c
tcpc_api_set_drp_toggle_t tcpc_driver_api::set_drp_toggle
```

`OPT`：启用 TCPC 自动双角色切换（Auto dual role toggle）。

<a id="a3bfecb52f9ed73b2a1eb081914197f01"></a>

### `set_low_power_mode`

```c
tcpc_api_set_low_power_mode_t tcpc_driver_api::set_low_power_mode
```

`OPT`：指示 TCPC 进入或退出低功耗模式（Low power mode）。

<a id="ae5c9719810866d0fcc03f329c84b3a58"></a>

### `set_roles`

```c
tcpc_api_set_roles_t tcpc_driver_api::set_roles
```

`OPT`：设置 USB 供电协商（Power Delivery，PD）消息头中的电源角色和数据角色（Power/Data Role）。

<a id="ac79a47b9a94fb4481bc9ecdba86b898d"></a>

### `set_rx_enable`

```c
tcpc_api_set_rx_enable_t tcpc_driver_api::set_rx_enable
```

`OPT`：启用 `SOP*` 类型消息的接收。

<a id="aca835517376e241345d05bf66119cb6c"></a>

### `set_snk_ctrl`

```c
tcpc_api_set_snk_ctrl_t tcpc_driver_api::set_snk_ctrl
```

`OPT`：设置 TCPC 的 VBUS 受电状态。

<a id="a70571ced311498d1065b94d81cbf5d4e"></a>

### `set_src_ctrl`

```c
tcpc_api_set_src_ctrl_t tcpc_driver_api::set_src_ctrl
```

`OPT`：设置 TCPC 的 VBUS 供电状态。

<a id="a536fbd074107f6a2b65e553f8acd1d0b"></a>

### `set_vconn`

```c
tcpc_api_set_vconn_t tcpc_driver_api::set_vconn
```

`OPT`：启用或禁用 VCONN。

<a id="a022918a3098b5b2cbba9d660f8f05a0a"></a>

### `set_vconn_cb`

```c
tcpc_api_set_vconn_cb_t tcpc_driver_api::set_vconn_cb
```

`REQ`：设置能够启用或禁用 VCONN 的回调。当 TCPC 无法执行这些操作，或系统配置为不使用 TCPC 的 VCONN 控制能力时，使用此回调。

<a id="af04de5dd092efeb32a23e21cda5033c0"></a>

### `set_vconn_discharge_cb`

```c
tcpc_api_set_vconn_discharge_cb_t tcpc_driver_api::set_vconn_discharge_cb
```

`REQ`：设置能够启用 VCONN 或对其放电的回调。当 TCPC 无法执行这些操作，或系统配置为不使用 TCPC 的 VCONN 控制能力时，使用此回调。

<a id="aa1b59f3aa1ccc8684445f119d4ea75aa"></a>

### `sop_prime_enable`

```c
tcpc_api_sop_prime_enable_t tcpc_driver_api::sop_prime_enable
```

`OPT`：启用 `SOP'`（SOP Prime）消息接收，并可选启用 `SOP''`（SOP Double Prime）消息接收。

<a id="aaa0956282b1b9cf3e41dc45a9f31e073"></a>

### `transmit_data`

```c
tcpc_api_transmit_data_t tcpc_driver_api::transmit_data
```

`OPT`：发送 PD 消息。

<a id="adc8f34eefe17f59953bba2029fcaa4bc"></a>

### `vconn_discharge`

```c
tcpc_api_vconn_discharge_t tcpc_driver_api::vconn_discharge
```

`OPT`：对 VCONN 放电。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_tcpc.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_tcpc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h_source.html)
- [tcpc_api_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae28524287fdb5504883afb66003d035c)
- [tcpc_api_get_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga39981c9b68e280de660ca15e137ffbd0)
- [tcpc_api_select_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae749f76083de380e2edd602dc0e30402)
- [tcpc_api_get_rp_value_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad1db9d036dd666846065bbf35ea22177)
- [tcpc_api_set_cc_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac524dbe59d67fb5bdfad78bc1a4d64c9)
- [tcpc_api_set_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gad8d3e1b467e6ee4fb58dcfed16117737)
- [tcpc_api_set_vconn_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga26217be69c8bc7ea24e6cabe489445da)
- [tcpc_api_vconn_discharge_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab503f46443ce870dd0baeebf8dd48e8f)
- [tcpc_api_set_vconn_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaf8d6f41fdd6fe99a1b629d361556966d)
- [tcpc_api_set_roles_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gadc6b26855f37fe94391f294c7f63d5bd)
- [tcpc_api_get_rx_pending_msg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab0828b95c31b6d6523ca471dd68ec065)
- [tcpc_api_set_rx_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga7cd4aae87502bf5ebb1939edceea81f3)
- [tcpc_api_set_cc_polarity_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa791f068d25e28abbd7d45071a5016be)
- [tcpc_api_transmit_data_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gab1f1d2db116913e4c0e451f57fb76d2c)
- [tcpc_api_dump_std_reg_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga99bb0b6056fb353fe15fc2d717f1a724)
- [tcpc_api_mask_status_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaa309db76ccb877d1cd9797d34bc55900)
- [tcpc_api_set_debug_accessory_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga238a927c4602269c48325d06d0f72215)
- [tcpc_api_set_debug_detach_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga483cbf6d74b5a892d8d241ccc8f6060e)
- [tcpc_api_set_drp_toggle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga56db121a729ffbb9173fe03fe867add1)
- [tcpc_api_get_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gabafb00fd478d682be7d33379b2c2487e)
- [tcpc_api_set_snk_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaaed7c7d360c5eb455d84164fc4ee2d1d)
- [tcpc_api_get_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga2da6efeb17079086b4dc7ac52d2e60e7)
- [tcpc_api_set_src_ctrl_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga8863bafbd43a21204b990aa74d710285)
- [tcpc_api_get_chip_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gac6f9724f73200ca20f1aa0a519928e50)
- [tcpc_api_set_low_power_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gae3339cd538cf4025f9f6e0959647e430)
- [tcpc_api_sop_prime_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga232b5d184f585aab94eb22daaf06c86b)
- [tcpc_api_set_bist_test_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#gaea02443c9aeb62583903291908a660cd)
- [tcpc_api_set_alert_handler_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga511cdf626c88790199edbd2fd578a833)
- [tcpc_api_dead_battery_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api__backend.html#ga0dfa332e501412fb407ef2490a042e11)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_tcpc_chip_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_tcpci_reg_dump_map_结构体.md)
