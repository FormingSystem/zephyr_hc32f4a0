---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-14
title: USB Type-C API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_USB Type-C API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB Type-C 线缆和连接器支持。

<a id="details"></a>

USB Type-C 线缆和连接器支持。

<a id="header-groups"></a>
<a id="groups"></a>

## 14.1\_主题（Topics）

<a id="r_usb_5Fpower_5Fdelivery"></a>

相关声明：[USB 电力传输（USB Power Delivery）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html)。

USB 电力传输（USB Power Delivery）

<a id="r_usb_5Ftype_5Fc_5Fport_5Fcontroller_5Fapi"></a>

相关声明：[USB Type-C 端口控制器 API（Port Controller API）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html)。

USB Type-C 端口控制器 API（Port Controller API）

<a id="r_usb_5Ftype_5Fc_5Fpower_5Fpath_5Fcontroller"></a>

相关声明：[USB Type-C 电源路径控制器（Power Path Controller）](../api_buffer_paging_topic_reference/P019_USB Type-C 电源路径控制器（Power Path Controller）.md)。

USB Type-C 电源路径控制器（Power Path Controller）

<a id="r_usbc_5Fvbus_5Fapi"></a>

相关声明：[USB-C 总线电源（VBUS）API](../api_network_time_topic_reference/P026_USB-C 总线电源（VBUS）API.md)。

USB-C 总线电源（VBUS）API

<a id="header-files"></a>
<a id="files"></a>

## 14.2\_文件（Files）

<a id="r_usbc_5Ftc_2Eh"></a>

```c
file usbc_tc.h
```

相关声明：[usbc_tc.h](../api_file_usb_network_reference/P016_zephyr__drivers__usb_c__usbc_tc.h_文件参考.md)。

USB-C驱动使用的USB Type-C线缆与连接器（Cable and Connector）API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.3\_宏定义（Macros）

<a id="r_ga025aeca5768435b245ecb9fe8bfa29c8"></a>

```c
#define TC_V_SINK_DISCONNECT_MIN_MV 800
```

相关声明：[TC_V_SINK_DISCONNECT_MIN_MV](#ga025aeca5768435b245ecb9fe8bfa29c8)。

受电端断开检测（Sink Disconnect Detection）的最小 VBUS 电压。

<a id="r_ga151c5852b9d2ad3f6f7f0869505e854b"></a>

```c
#define TC_V_SINK_DISCONNECT_MAX_MV 3670
```

相关声明：[TC_V_SINK_DISCONNECT_MAX_MV](#ga151c5852b9d2ad3f6f7f0869505e854b)。

受电端断开检测（Sink Disconnect Detection）的最大 VBUS 电压。

<a id="r_gace546c362f92ed1ba0455a5d8006357c"></a>

```c
#define TC_T_VBUS_ON_MAX_MS 275
```

相关声明：[TC_T_VBUS_ON_MAX_MS](#gace546c362f92ed1ba0455a5d8006357c)。

从进入 `Attached.SRC` 状态，到在供电端插座（Source Receptacle）处测得 VBUS 达到最小 `vSafe5V` 阈值的时间。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="r_ga2d6440c7b480ee75ccadf8242e29e7e9"></a>

```c
#define TC_T_VBUS_OFF_MAX_MS 650
```

相关声明：[TC_T_VBUS_OFF_MAX_MS](#ga2d6440c7b480ee75ccadf8242e29e7e9)。

从受电端（Sink）断开，到供电端（Source）撤去 VBUS 并使其达到 `vSafe0V` 的时间，参见 USB 电力传输（USB PD）。

<a id="r_gaf2cbadac415eedae8c4db3dc91f3623b"></a>

```c
#define TC_T_VCONN_ON_MAX_MS 2
```

相关声明：[TC_T_VCONN_ON_MAX_MS](#gaf2cbadac415eedae8c4db3dc91f3623b)。

从供电端（Source）在 `Attached.SRC` 状态下开始提供 VBUS 的时刻起计时。

<a id="r_ga24837587c589d85bc48bed2a6815798d"></a>

```c
#define TC_T_VCONN_ON_PA_MAX_MS 100
```

相关声明：[TC_T_VCONN_ON_PA_MAX_MS](#ga24837587c589d85bc48bed2a6815798d)。

从支持附件（Accessory）的受电端（Sink）进入 `PoweredAccessory` 状态，到受电端提供最小 VCONN 电压的时间，最小电压参见表 4-5。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="r_ga2f347359b4ffc4478338cbbc8a62d4d9"></a>

```c
#define TC_T_VCONN_OFF_MAX_MS 35
```

相关声明：[TC_T_VCONN_OFF_MAX_MS](#ga2f347359b4ffc4478338cbbc8a62d4d9)。

从受电端（Sink）断开，或按指示开始操作，到断开 VCONN 供电的时间。

<a id="r_gaa1291eb2b50b59a9746ffe0658d60258"></a>

```c
#define TC_T_SINK_ADJ_MAX_MS 60
```

相关声明：[TC_T_SINK_ADJ_MAX_MS](#gaa1291eb2b50b59a9746ffe0658d60258)。

USB Type-C 电流通告（Current Advertisement）变化后，受电端（Sink）将其电流消耗调整到指定范围所需的响应时间。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="r_gab042a018fbc99a402ab23371c3d6fe47"></a>

```c
#define TC_T_DRP_MIN_MS 50
```

相关声明：[TC_T_DRP_MIN_MS](#gab042a018fbc99a402ab23371c3d6fe47)。

双角色电源端口（DRP）完成从供电端（Source）到受电端（Sink）再返回的角色通告所需的最小周期。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="r_gaba34e5687c2e12984629a9297f0e7813"></a>

```c
#define TC_T_DRP_MAX_MS 100
```

相关声明：[TC_T_DRP_MAX_MS](#gaba34e5687c2e12984629a9297f0e7813)。

双角色电源端口（DRP）完成从供电端（Source）到受电端（Sink）再返回的角色通告所需的最大周期。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="r_ga06432fe2787e95420b7d1e08ee3e9e42"></a>

```c
#define TC_T_DRP_PW_MIN_MS 15
```

相关声明：[TC_T_DRP_PW_MIN_MS](#ga06432fe2787e95420b7d1e08ee3e9e42)。

双角色电源端口（DRP）应通告供电端（Source）或受电端（Sink）角色的最短时间。

<a id="r_ga7b4ab74daa0edc9cff141679ac05a0c3"></a>

```c
#define TC_T_DRP_PW_MAX_MS 70
```

相关声明：[TC_T_DRP_PW_MAX_MS](#ga7b4ab74daa0edc9cff141679ac05a0c3)。

双角色电源端口（DRP）应通告供电端（Source）或受电端（Sink）角色的最长时间。

<a id="r_ga6ab07167512c79d9587d547902443049"></a>

```c
#define TC_T_DRP_TRANSITION_MIN_MS 0
```

相关声明：[TC_T_DRP_TRANSITION_MIN_MS](#ga6ab07167512c79d9587d547902443049)。

角色确定（Role Resolution）期间，双角色电源端口（DRP）完成供电端（Source）与受电端（Sink）角色切换所需的最短时间。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="r_gae1e9780a30b644a1f15463cba216e385"></a>

```c
#define TC_T_DRP_TRANSITION_MAX_MS 1
```

相关声明：[TC_T_DRP_TRANSITION_MAX_MS](#gae1e9780a30b644a1f15463cba216e385)。

角色确定（Role Resolution）期间，双角色电源端口（DRP）完成供电端（Source）与受电端（Sink）角色切换所需的最长时间。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="r_ga1ee8d43885ebc26a2f4da640d5758188"></a>

```c
#define TC_T_DRP_TRY_MIN_MS 75
```

相关声明：[TC_T_DRP_TRY_MIN_MS](#ga1ee8d43885ebc26a2f4da640d5758188)。

与 `Try.SRC` 状态关联的最短等待时间（Minimum Wait Time）。

<a id="r_ga95cd5ac306f2d27440b980593c759f07"></a>

```c
#define TC_T_DRP_TRY_MAX_MS 150
```

相关声明：[TC_T_DRP_TRY_MAX_MS](#ga95cd5ac306f2d27440b980593c759f07)。

与 `Try.SRC` 状态关联的最长等待时间（Maximum Wait Time）。

<a id="r_gae19a1dc5b950495866359deef2cd6c7c"></a>

```c
#define TC_T_DRP_TRY_WAIT_MIN_MS 400
```

相关声明：[TC_T_DRP_TRY_WAIT_MIN_MS](#gae19a1dc5b950495866359deef2cd6c7c)。

与 `Try.SNK` 状态关联的最短等待时间（Minimum Wait Time）。

<a id="r_ga0eb5b996e1678f3830c38584f84a6268"></a>

```c
#define TC_T_DRP_TRY_WAIT_MAX_MS 800
```

相关声明：[TC_T_DRP_TRY_WAIT_MAX_MS](#ga0eb5b996e1678f3830c38584f84a6268)。

与 `Try.SNK` 状态关联的最长等待时间（Maximum Wait Time）。

<a id="r_ga45be1dbb0a9ad2e9a9b0549f953cb8c2"></a>

```c
#define TC_T_TRY_TIMEOUT_MIN_MS 550
```

相关声明：[TC_T_TRY_TIMEOUT_MIN_MS](#ga45be1dbb0a9ad2e9a9b0549f953cb8c2)。

从 `Try.SRC` 转换到 `TryWait.SNK` 的最小超时时间（Minimum Timeout）。

<a id="r_gae3e98e8acbfb5fa7f398dea64265cb0a"></a>

```c
#define TC_T_TRY_TIMEOUT_MAX_MS 1100
```

相关声明：[TC_T_TRY_TIMEOUT_MAX_MS](#gae3e98e8acbfb5fa7f398dea64265cb0a)。

从 `Try.SRC` 转换到 `TryWait.SNK` 的最大超时时间（Maximum Timeout）。

<a id="r_ga50a154595c40bba3e46751f6f46df848"></a>

```c
#define TC_T_VPD_DETACH_MIN_MS 10
```

相关声明：[TC_T_VPD_DETACH_MIN_MS](#ga50a154595c40bba3e46751f6f46df848)。

撤去 VBUS 后，双角色电源端口（DRP）检测到已连接的支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）已断开所需的最短时间。

<a id="r_ga33b792a38351081f316e6f854710a96e"></a>

```c
#define TC_T_VPD_DETACH_MAX_MS 20
```

相关声明：[TC_T_VPD_DETACH_MAX_MS](#ga33b792a38351081f316e6f854710a96e)。

撤去 VBUS 后，双角色电源端口（DRP）检测到已连接的支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）已断开所需的最长时间。

<a id="r_gae059acba0f01f24cb682ee2c3ded59d9"></a>

```c
#define TC_T_CC_DEBOUNCE_MIN_MS 100
```

相关声明：[TC_T_CC_DEBOUNCE_MIN_MS](#gae059acba0f01f24cb682ee2c3ded59d9)。

端口判定自身已连接（Attached）前应等待的最短时间。参见表 4-31“CC 时序”（CC Timing）。

<a id="r_gac4eb3955701e40ddabf8b2afae68ea8d"></a>

```c
#define TC_T_CC_DEBOUNCE_MAX_MS 200
```

相关声明：[TC_T_CC_DEBOUNCE_MAX_MS](#gac4eb3955701e40ddabf8b2afae68ea8d)。

端口判定自身已连接（Attached）前应等待的最长时间。参见表 4-31“CC 时序”（CC Timing）。

<a id="r_ga46e03b71bd69657786755bd716383fe7"></a>

```c
#define TC_T_PD_DEBOUNCE_MIN_MS 10
```

相关声明：[TC_T_PD_DEBOUNCE_MIN_MS](#ga46e03b71bd69657786755bd716383fe7)。

受电端端口（Sink Port）判定自身已断开前应等待的最短时间；原因是状态定义中所述的 CC 上可能存在 USB PD 信令（Signaling）。

<a id="r_ga4327b09ebf8f27675ac8fc6125ab6bbc"></a>

```c
#define TC_T_PD_DEBOUNCE_MAX_MS 20
```

相关声明：[TC_T_PD_DEBOUNCE_MAX_MS](#ga4327b09ebf8f27675ac8fc6125ab6bbc)。

受电端端口（Sink Port）判定自身已断开前应等待的最长时间；原因是状态定义中所述的 CC 上可能存在 USB PD 信令（Signaling）。

<a id="r_ga21ce86c10d5b0b9e3e7fa08e902d6f77"></a>

```c
#define TC_T_TRY_CC_DEBOUNCE_MIN_MS 10
```

相关声明：[TC_T_TRY_CC_DEBOUNCE_MIN_MS](#ga21ce86c10d5b0b9e3e7fa08e902d6f77)。

在尝试等待过程（Try-wait Process）中，端口判定自身已重新连接（Re-attached）前应等待的最短时间。

<a id="r_ga1b736eb0d37209d95f4e305baaefc1f0"></a>

```c
#define TC_T_TRY_CC_DEBOUNCE_MAX_MS 10
```

相关声明：[TC_T_TRY_CC_DEBOUNCE_MAX_MS](#ga1b736eb0d37209d95f4e305baaefc1f0)。

在尝试等待过程（Try-wait Process）中，端口判定自身已重新连接（Re-attached）前应等待的最长时间。

<a id="r_ga70a063a53fba92977ed35169743368f0"></a>

```c
#define TC_T_ERROR_RECOVERY_SELF_POWERED_MIN_MS 25
```

相关声明：[TC_T_ERROR_RECOVERY_SELF_POWERED_MIN_MS](#ga70a063a53fba92977ed35169743368f0)。

自供电端口（Self-powered Port）必须停留在 `ErrorRecovery` 状态的最短时间。

<a id="r_gaaee37a1ff25fc71a5c66f04b327f9b04"></a>

```c
#define TC_T_ERROR_RECOVERY_SOURCE_MIN_MS 240
```

相关声明：[TC_T_ERROR_RECOVERY_SOURCE_MIN_MS](#gaaee37a1ff25fc71a5c66f04b327f9b04)。

如果供电端（Source）在前一状态中提供 VCONN，则其必须停留在 `ErrorRecovery` 状态的最短时间。

<a id="r_ga22273343713c29c84f7ff95fc34e9573"></a>

```c
#define TC_T_RP_VALUE_CHANGE_MIN_MS 10
```

相关声明：[TC_T_RP_VALUE_CHANGE_MIN_MS](#ga22273343713c29c84f7ff95fc34e9573)。

当 CC 不处于 BMC 空闲状态（BMC Idle），或端口无法检测 BMC 空闲状态时，受电端端口（Sink Port）判定 Rp 已发生变化前应等待的最短时间。

<a id="r_gade24fb4955e80390e4f47b86fbce1874"></a>

```c
#define TC_T_RP_VALUE_CHANGE_MAX_MS 20
```

相关声明：[TC_T_RP_VALUE_CHANGE_MAX_MS](#gade24fb4955e80390e4f47b86fbce1874)。

当 CC 不处于 BMC 空闲状态（BMC Idle），或端口无法检测 BMC 空闲状态时，受电端端口（Sink Port）判定 Rp 已发生变化前应等待的最长时间。

<a id="r_ga767c754753786419f50faa2888859cdb"></a>

```c
#define TC_T_SRC_DISCONNECT_MIN_MS 0
```

相关声明：[TC_T_SRC_DISCONNECT_MIN_MS](#ga767c754753786419f50faa2888859cdb)。

供电端（Source）检测 `SRC.Open` 状态的最短时间。

<a id="r_ga92232c9516031a90da1a6fbd1be03b73"></a>

```c
#define TC_T_SRC_DISCONNECT_MAX_MS 20
```

相关声明：[TC_T_SRC_DISCONNECT_MAX_MS](#ga92232c9516031a90da1a6fbd1be03b73)。

供电端（Source）检测 `SRC.Open` 状态的最长时间。

<a id="r_ga5ccab8bbe9c386d47f705551c3b5f918"></a>

```c
#define TC_T_NO_TOGGLE_CONNECT_MIN_MS 0
```

相关声明：[TC_T_NO_TOGGLE_CONNECT_MIN_MS](#ga5ccab8bbe9c386d47f705551c3b5f918)。

两侧端口伙伴（Port Partner）均未切换角色时，检测到连接的最短时间。

<a id="r_ga7e56e9ff953b5fc425c4304831c19738"></a>

```c
#define TC_T_NO_TOGGLE_CONNECT_MAX_MS 5
```

相关声明：[TC_T_NO_TOGGLE_CONNECT_MAX_MS](#ga7e56e9ff953b5fc425c4304831c19738)。

两侧端口伙伴（Port Partner）均未切换角色时，检测到连接的最长时间。

<a id="r_ga44d9260612a215407d79415b30e63613"></a>

```c
#define TC_T_ONE_PORT_TOGGLE_CONNECT_MIN_MS 0
```

相关声明：[TC_T_ONE_PORT_TOGGLE_CONNECT_MIN_MS](#ga44d9260612a215407d79415b30e63613)。

一侧端口伙伴（Port Partner）切换角色时，检测到连接的最短时间；原文给出的范围为 `0ms … dcSRC.DRP max * tDRP max + 2 * tNoToggleConnect)`。

<a id="r_ga62662057432f68c48dd59be8b28297d4"></a>

```c
#define TC_T_ONE_PORT_TOGGLE_CONNECT_MAX_MS 80
```

相关声明：[TC_T_ONE_PORT_TOGGLE_CONNECT_MAX_MS](#ga62662057432f68c48dd59be8b28297d4)。

一侧端口伙伴（Port Partner）切换角色时，检测到连接的最长时间；原文给出的范围为 `0ms … dcSRC.DRP max * tDRP max + 2 * tNoToggleConnect)`。

<a id="r_ga96c2bf7f24deb8e8a0d327536a0a023e"></a>

```c
#define TC_T_TWO_PORT_TOGGLE_CONNECT_MIN_MS 0
```

相关声明：[TC_T_TWO_PORT_TOGGLE_CONNECT_MIN_MS](#ga96c2bf7f24deb8e8a0d327536a0a023e)。

两侧端口伙伴（Port Partner）均切换角色时，检测到连接的最短时间；范围为 `(0ms … 5 * tDRP max + 2 * tNoToggleConnect)`。

<a id="r_gad911bc40a17b676c8a87d87d51fc0fbf"></a>

```c
#define TC_T_TWO_PORT_TOGGLE_CONNECT_MAX_MS 510
```

相关声明：[TC_T_TWO_PORT_TOGGLE_CONNECT_MAX_MS](#gad911bc40a17b676c8a87d87d51fc0fbf)。

两侧端口伙伴（Port Partner）均切换角色时，检测到连接的最长时间；范围为 `(0ms … 5 * tDRP max + 2 * tNoToggleConnect)`。

<a id="r_gae2ebe887ccb4f9549d130e85b999062e"></a>

```c
#define TC_T_VPDCTDD_MIN_US 30
```

相关声明：[TC_T_VPDCTDD_MIN_US](#gae2ebe887ccb4f9549d130e85b999062e)。

撤去 VBUS 后，支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）检测到充电透传供电端（Charge-Through Source）已从 CC 断开、转换到 `CTUnattached.VPD` 状态，并在主机端口 CC 上重新施加通告 3.0 A 的 Rp 终端电阻所需的最短时间。

<a id="r_ga75223d9754d7ce76e302ee2ed40d11ef"></a>

```c
#define TC_T_VPDCTDD_MAX_MS 5
```

相关声明：[TC_T_VPDCTDD_MAX_MS](#ga75223d9754d7ce76e302ee2ed40d11ef)。

撤去 VBUS 后，支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）检测到充电透传供电端（Charge-Through Source）已从 CC 断开、转换到 `CTUnattached.VPD` 状态，并在主机端口 CC 上重新施加通告 3.0 A 的 Rp 终端电阻所需的最长时间。

<a id="r_ga56ece8323bd0a8e4ce0755e0e9e06f96"></a>

```c
#define TC_T_VPDDISABLE_MIN_MS 25
```

相关声明：[TC_T_VPDDISABLE_MIN_MS](#ga56ece8323bd0a8e4ce0755e0e9e06f96)。

支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）必须停留在 `CTDisabled.VPD` 状态的最短时间。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.4\_枚举（Enumerations）

<a id="r_ga64e32ec2da97f70fd5b96975317cb92c"></a>

```c
enum tc_cc_voltage_state { TC_CC_VOLT_OPEN = 0 , TC_CC_VOLT_RA = 1 , TC_CC_VOLT_RD = 2 , TC_CC_VOLT_RP_DEF = 5 , TC_CC_VOLT_RP_1A5 = 6 , TC_CC_VOLT_RP_3A0 = 7 }
```

相关声明：[tc_cc_voltage_state](#ga64e32ec2da97f70fd5b96975317cb92c)、[TC_CC_VOLT_OPEN](#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05)、[TC_CC_VOLT_RA](#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea)、[TC_CC_VOLT_RD](#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)、[TC_CC_VOLT_RP_DEF](#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)、[TC_CC_VOLT_RP_1A5](#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)、[TC_CC_VOLT_RP_3A0](#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca)。

CC 电压状态（CC Voltage Status）。

<a id="r_ga015455a6c5620dfc96cfb713bbb72161"></a>

```c
enum tc_vbus_level { TC_VBUS_SAFE0V = 0 , TC_VBUS_PRESENT = 1 , TC_VBUS_REMOVED = 2 }
```

相关声明：[tc_vbus_level](#ga015455a6c5620dfc96cfb713bbb72161)、[TC_VBUS_SAFE0V](#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827)、[TC_VBUS_PRESENT](#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5)、[TC_VBUS_REMOVED](#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc)。

VBUS 电压等级（VBUS Level Voltages）。

<a id="r_ga4e0eec97f7c5c97b87eff9561deea2d5"></a>

```c
enum tc_rp_value { TC_RP_USB = 0 , TC_RP_1A5 = 1 , TC_RP_3A0 = 2 , TC_RP_RESERVED = 3 }
```

相关声明：[tc_rp_value](#ga4e0eec97f7c5c97b87eff9561deea2d5)、[TC_RP_USB](#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb)、[TC_RP_1A5](#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28)、[TC_RP_3A0](#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c)、[TC_RP_RESERVED](#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1)。

上拉电阻值（Pull-Up Resistor Values）。

<a id="r_ga0200c820510eb786f3ca30a9b5f7aada"></a>

```c
enum tc_cc_pull { TC_CC_RA = 0 , TC_CC_RP = 1 , TC_CC_RD = 2 , TC_CC_OPEN = 3 , TC_RA_RD = 4 }
```

相关声明：[tc_cc_pull](#ga0200c820510eb786f3ca30a9b5f7aada)、[TC_CC_RA](#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8)、[TC_CC_RP](#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322)、[TC_CC_RD](#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e)、[TC_CC_OPEN](#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8)、[TC_RA_RD](#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e)。

CC 上拉／下拉电阻（CC Pull Resistors）。

<a id="r_ga8707ac194510396d55a40887673b53ca"></a>

```c
enum tc_cable_plug { PD_PLUG_FROM_DFP_UFP = 0 , PD_PLUG_FROM_CABLE_VPD = 1 }
```

相关声明：[tc_cable_plug](#ga8707ac194510396d55a40887673b53ca)、[PD_PLUG_FROM_DFP_UFP](#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3)、[PD_PLUG_FROM_CABLE_VPD](#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed)。

线缆插头（Cable Plug）。

<a id="r_ga7fa5123d0e4404fd9931d162e1152c84"></a>

```c
enum tc_power_role_capability { TC_ROLE_CAP_SINK = 0 , TC_ROLE_CAP_SOURCE = 1 , TC_ROLE_CAP_DRP = 2 }
```

相关声明：[tc_power_role_capability](#ga7fa5123d0e4404fd9931d162e1152c84)、[TC_ROLE_CAP_SINK](#gga7fa5123d0e4404fd9931d162e1152c84a9609834767cb8d6fb809723ed39d95ac)、[TC_ROLE_CAP_SOURCE](#gga7fa5123d0e4404fd9931d162e1152c84a90e2ae7810814497656c8bcd3c930a28)、[TC_ROLE_CAP_DRP](#gga7fa5123d0e4404fd9931d162e1152c84a22e4c04eea5706dbd0c51999c0e2f1cf)。

电力传输电源角色能力（Power Delivery Power Role Capability）。本枚举表示端口已配置的能力（Configured Capability）。

<a id="r_gaa6dda0612045b5f55b9d8ba63d2b9f9d"></a>

```c
enum tc_power_role { TC_ROLE_SINK = 0 , TC_ROLE_SOURCE = 1 }
```

相关声明：[tc_power_role](#gaa6dda0612045b5f55b9d8ba63d2b9f9d)、[TC_ROLE_SINK](#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb)、[TC_ROLE_SOURCE](#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1)。

电力传输电源角色（Power Delivery Power Role）。

<a id="r_ga6b98bbe238e62cfd5531688494a63de2"></a>

```c
enum tc_data_role { TC_ROLE_UFP = 0 , TC_ROLE_DFP = 1 , TC_ROLE_DISCONNECTED = 2 }
```

相关声明：[tc_data_role](#ga6b98bbe238e62cfd5531688494a63de2)、[TC_ROLE_UFP](#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414)、[TC_ROLE_DFP](#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1)、[TC_ROLE_DISCONNECTED](#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058)。

电力传输数据角色（Power Delivery Data Role）。

<a id="r_gac5b4b58840c9b076a869a5816ba100db"></a>

```c
enum tc_cc_polarity { TC_POLARITY_CC1 = 0 , TC_POLARITY_CC2 = 1 }
```

相关声明：[tc_cc_polarity](#gac5b4b58840c9b076a869a5816ba100db)、[TC_POLARITY_CC1](#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2)、[TC_POLARITY_CC2](#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910)。

CC 线路极性（CC Line Polarity）。

<a id="r_ga5bb2cfcf3ab60423048db38103657197"></a>

```c
enum tc_cc_states { TC_CC_NONE = 0 , TC_CC_UFP_NONE = 1 , TC_CC_UFP_AUDIO_ACC = 2 , TC_CC_UFP_DEBUG_ACC = 3 , TC_CC_UFP_ATTACHED = 4 , TC_CC_DFP_ATTACHED = 5 , TC_CC_DFP_DEBUG_ACC = 6 }
```

相关声明：[tc_cc_states](#ga5bb2cfcf3ab60423048db38103657197)、[TC_CC_NONE](#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0)、[TC_CC_UFP_NONE](#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0)、[TC_CC_UFP_AUDIO_ACC](#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea)、[TC_CC_UFP_DEBUG_ACC](#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78)、[TC_CC_UFP_ATTACHED](#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524)、[TC_CC_DFP_ATTACHED](#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba)、[TC_CC_DFP_DEBUG_ACC](#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c)。

根据 CC 线路状态判断的可能端口伙伴连接（Port Partner Connections）。

## 14.5\_详细说明（Detailed Documentation）

<a id="gac4eb3955701e40ddabf8b2afae68ea8d"></a>

### `TC_T_CC_DEBOUNCE_MAX_MS`

```c
#define TC_T_CC_DEBOUNCE_MAX_MS 200
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

端口判定自身已连接（Attached）前应等待的最长时间。参见表 4-31“CC 时序”（CC Timing）。

<a id="gae059acba0f01f24cb682ee2c3ded59d9"></a>

### `TC_T_CC_DEBOUNCE_MIN_MS`

```c
#define TC_T_CC_DEBOUNCE_MIN_MS 100
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

端口判定自身已连接（Attached）前应等待的最短时间。参见表 4-31“CC 时序”（CC Timing）。

<a id="gaba34e5687c2e12984629a9297f0e7813"></a>

### `TC_T_DRP_MAX_MS`

```c
#define TC_T_DRP_MAX_MS 100
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

双角色电源端口（DRP）完成从供电端（Source）到受电端（Sink）再返回的角色通告所需的最大周期。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="gab042a018fbc99a402ab23371c3d6fe47"></a>

### `TC_T_DRP_MIN_MS`

```c
#define TC_T_DRP_MIN_MS 50
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

双角色电源端口（DRP）完成从供电端（Source）到受电端（Sink）再返回的角色通告所需的最小周期。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga7b4ab74daa0edc9cff141679ac05a0c3"></a>

### `TC_T_DRP_PW_MAX_MS`

```c
#define TC_T_DRP_PW_MAX_MS 70
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

双角色电源端口（DRP）应通告供电端（Source）或受电端（Sink）角色的最长时间。

双角色电源端口切换脉宽最大值（DRP Toggle Pulse Width Maximum）：`tDRP max * dcSRC.DRP max`。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga06432fe2787e95420b7d1e08ee3e9e42"></a>

### `TC_T_DRP_PW_MIN_MS`

```c
#define TC_T_DRP_PW_MIN_MS 15
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

双角色电源端口（DRP）应通告供电端（Source）或受电端（Sink）角色的最短时间。

双角色电源端口切换脉宽最小值（DRP Toggle Pulse Width Minimum）：`tDRP min * dcSRC.DRP min`。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="gae1e9780a30b644a1f15463cba216e385"></a>

### `TC_T_DRP_TRANSITION_MAX_MS`

```c
#define TC_T_DRP_TRANSITION_MAX_MS 1
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

角色确定（Role Resolution）期间，双角色电源端口（DRP）完成供电端（Source）与受电端（Sink）角色切换所需的最长时间。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga6ab07167512c79d9587d547902443049"></a>

### `TC_T_DRP_TRANSITION_MIN_MS`

```c
#define TC_T_DRP_TRANSITION_MIN_MS 0
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

角色确定（Role Resolution）期间，双角色电源端口（DRP）完成供电端（Source）与受电端（Sink）角色切换所需的最短时间。参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga95cd5ac306f2d27440b980593c759f07"></a>

### `TC_T_DRP_TRY_MAX_MS`

```c
#define TC_T_DRP_TRY_MAX_MS 150
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

与 `Try.SRC` 状态关联的最长等待时间（Maximum Wait Time）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga1ee8d43885ebc26a2f4da640d5758188"></a>

### `TC_T_DRP_TRY_MIN_MS`

```c
#define TC_T_DRP_TRY_MIN_MS 75
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

与 `Try.SRC` 状态关联的最短等待时间（Minimum Wait Time）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga0eb5b996e1678f3830c38584f84a6268"></a>

### `TC_T_DRP_TRY_WAIT_MAX_MS`

```c
#define TC_T_DRP_TRY_WAIT_MAX_MS 800
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

与 `Try.SNK` 状态关联的最长等待时间（Maximum Wait Time）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="gae19a1dc5b950495866359deef2cd6c7c"></a>

### `TC_T_DRP_TRY_WAIT_MIN_MS`

```c
#define TC_T_DRP_TRY_WAIT_MIN_MS 400
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

与 `Try.SNK` 状态关联的最短等待时间（Minimum Wait Time）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga70a063a53fba92977ed35169743368f0"></a>

### `TC_T_ERROR_RECOVERY_SELF_POWERED_MIN_MS`

```c
#define TC_T_ERROR_RECOVERY_SELF_POWERED_MIN_MS 25
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

自供电端口（Self-powered Port）必须停留在 `ErrorRecovery` 状态的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="gaaee37a1ff25fc71a5c66f04b327f9b04"></a>

### `TC_T_ERROR_RECOVERY_SOURCE_MIN_MS`

```c
#define TC_T_ERROR_RECOVERY_SOURCE_MIN_MS 240
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

如果供电端（Source）在前一状态中提供 VCONN，则其必须停留在 `ErrorRecovery` 状态的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga7e56e9ff953b5fc425c4304831c19738"></a>

### `TC_T_NO_TOGGLE_CONNECT_MAX_MS`

```c
#define TC_T_NO_TOGGLE_CONNECT_MAX_MS 5
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

两侧端口伙伴（Port Partner）均未切换角色时，检测到连接的最长时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga5ccab8bbe9c386d47f705551c3b5f918"></a>

### `TC_T_NO_TOGGLE_CONNECT_MIN_MS`

```c
#define TC_T_NO_TOGGLE_CONNECT_MIN_MS 0
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

两侧端口伙伴（Port Partner）均未切换角色时，检测到连接的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga62662057432f68c48dd59be8b28297d4"></a>

### `TC_T_ONE_PORT_TOGGLE_CONNECT_MAX_MS`

```c
#define TC_T_ONE_PORT_TOGGLE_CONNECT_MAX_MS 80
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

一侧端口伙伴（Port Partner）切换角色时，检测到连接的最长时间；原文给出的范围为 `0ms … dcSRC.DRP max * tDRP max + 2 * tNoToggleConnect)`。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga44d9260612a215407d79415b30e63613"></a>

### `TC_T_ONE_PORT_TOGGLE_CONNECT_MIN_MS`

```c
#define TC_T_ONE_PORT_TOGGLE_CONNECT_MIN_MS 0
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

一侧端口伙伴（Port Partner）切换角色时，检测到连接的最短时间；原文给出的范围为 `0ms … dcSRC.DRP max * tDRP max + 2 * tNoToggleConnect)`。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga4327b09ebf8f27675ac8fc6125ab6bbc"></a>

### `TC_T_PD_DEBOUNCE_MAX_MS`

```c
#define TC_T_PD_DEBOUNCE_MAX_MS 20
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

受电端端口（Sink Port）判定自身已断开前应等待的最长时间；原因是状态定义中所述的 CC 上可能存在 USB PD 信令（Signaling）。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga46e03b71bd69657786755bd716383fe7"></a>

### `TC_T_PD_DEBOUNCE_MIN_MS`

```c
#define TC_T_PD_DEBOUNCE_MIN_MS 10
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

受电端端口（Sink Port）判定自身已断开前应等待的最短时间；原因是状态定义中所述的 CC 上可能存在 USB PD 信令（Signaling）。

参见表 4-31“CC 时序”（CC Timing）。

<a id="gade24fb4955e80390e4f47b86fbce1874"></a>

### `TC_T_RP_VALUE_CHANGE_MAX_MS`

```c
#define TC_T_RP_VALUE_CHANGE_MAX_MS 20
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

当 CC 不处于 BMC 空闲状态（BMC Idle），或端口无法检测 BMC 空闲状态时，受电端端口（Sink Port）判定 Rp 已发生变化前应等待的最长时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga22273343713c29c84f7ff95fc34e9573"></a>

### `TC_T_RP_VALUE_CHANGE_MIN_MS`

```c
#define TC_T_RP_VALUE_CHANGE_MIN_MS 10
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

当 CC 不处于 BMC 空闲状态（BMC Idle），或端口无法检测 BMC 空闲状态时，受电端端口（Sink Port）判定 Rp 已发生变化前应等待的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="gaa1291eb2b50b59a9746ffe0658d60258"></a>

### `TC_T_SINK_ADJ_MAX_MS`

```c
#define TC_T_SINK_ADJ_MAX_MS 60
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

USB Type-C 电流通告（Current Advertisement）变化后，受电端（Sink）将其电流消耗调整到指定范围所需的响应时间。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="ga92232c9516031a90da1a6fbd1be03b73"></a>

### `TC_T_SRC_DISCONNECT_MAX_MS`

```c
#define TC_T_SRC_DISCONNECT_MAX_MS 20
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

供电端（Source）检测 `SRC.Open` 状态的最长时间。

供电端（Source）应在实际可行的范围内尽快检测 `SRC.Open` 状态。参见表 4-31“CC 时序”（CC Timing）。

<a id="ga767c754753786419f50faa2888859cdb"></a>

### `TC_T_SRC_DISCONNECT_MIN_MS`

```c
#define TC_T_SRC_DISCONNECT_MIN_MS 0
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

供电端（Source）检测 `SRC.Open` 状态的最短时间。

供电端（Source）应在实际可行的范围内尽快检测 `SRC.Open` 状态。参见表 4-31“CC 时序”（CC Timing）。

<a id="ga1b736eb0d37209d95f4e305baaefc1f0"></a>

### `TC_T_TRY_CC_DEBOUNCE_MAX_MS`

```c
#define TC_T_TRY_CC_DEBOUNCE_MAX_MS 10
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

在尝试等待过程（Try-wait Process）中，端口判定自身已重新连接（Re-attached）前应等待的最长时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga21ce86c10d5b0b9e3e7fa08e902d6f77"></a>

### `TC_T_TRY_CC_DEBOUNCE_MIN_MS`

```c
#define TC_T_TRY_CC_DEBOUNCE_MIN_MS 10
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

在尝试等待过程（Try-wait Process）中，端口判定自身已重新连接（Re-attached）前应等待的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="gae3e98e8acbfb5fa7f398dea64265cb0a"></a>

### `TC_T_TRY_TIMEOUT_MAX_MS`

```c
#define TC_T_TRY_TIMEOUT_MAX_MS 1100
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从 `Try.SRC` 转换到 `TryWait.SNK` 的最大超时时间（Maximum Timeout）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga45be1dbb0a9ad2e9a9b0549f953cb8c2"></a>

### `TC_T_TRY_TIMEOUT_MIN_MS`

```c
#define TC_T_TRY_TIMEOUT_MIN_MS 550
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从 `Try.SRC` 转换到 `TryWait.SNK` 的最小超时时间（Minimum Timeout）。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="gad911bc40a17b676c8a87d87d51fc0fbf"></a>

### `TC_T_TWO_PORT_TOGGLE_CONNECT_MAX_MS`

```c
#define TC_T_TWO_PORT_TOGGLE_CONNECT_MAX_MS 510
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

两侧端口伙伴（Port Partner）均切换角色时，检测到连接的最长时间；范围为 `(0ms … 5 * tDRP max + 2 * tNoToggleConnect)`。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga96c2bf7f24deb8e8a0d327536a0a023e"></a>

### `TC_T_TWO_PORT_TOGGLE_CONNECT_MIN_MS`

```c
#define TC_T_TWO_PORT_TOGGLE_CONNECT_MIN_MS 0
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

两侧端口伙伴（Port Partner）均切换角色时，检测到连接的最短时间；范围为 `(0ms … 5 * tDRP max + 2 * tNoToggleConnect)`。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga2d6440c7b480ee75ccadf8242e29e7e9"></a>

### `TC_T_VBUS_OFF_MAX_MS`

```c
#define TC_T_VBUS_OFF_MAX_MS 650
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从受电端（Sink）断开，到供电端（Source）撤去 VBUS 并使其达到 `vSafe0V` 的时间，参见 USB 电力传输（USB PD）。

参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="gace546c362f92ed1ba0455a5d8006357c"></a>

### `TC_T_VBUS_ON_MAX_MS`

```c
#define TC_T_VBUS_ON_MAX_MS 275
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从进入 `Attached.SRC` 状态，到在供电端插座（Source Receptacle）处测得 VBUS 达到最小 `vSafe5V` 阈值的时间。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="ga2f347359b4ffc4478338cbbc8a62d4d9"></a>

### `TC_T_VCONN_OFF_MAX_MS`

```c
#define TC_T_VCONN_OFF_MAX_MS 35
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从受电端（Sink）断开，或按指示开始操作，到断开 VCONN 供电的时间。

参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="gaf2cbadac415eedae8c4db3dc91f3623b"></a>

### `TC_T_VCONN_ON_MAX_MS`

```c
#define TC_T_VCONN_ON_MAX_MS 2
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从供电端（Source）在 `Attached.SRC` 状态下开始提供 VBUS 的时刻起计时。

参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="ga24837587c589d85bc48bed2a6815798d"></a>

### `TC_T_VCONN_ON_PA_MAX_MS`

```c
#define TC_T_VCONN_ON_PA_MAX_MS 100
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

从支持附件（Accessory）的受电端（Sink）进入 `PoweredAccessory` 状态，到受电端提供最小 VCONN 电压的时间，最小电压参见表 4-5。参见表 4-29“VBUS 与 VCONN 时序参数”（VBUS and VCONN Timing Parameters）。

<a id="ga33b792a38351081f316e6f854710a96e"></a>

### `TC_T_VPD_DETACH_MAX_MS`

```c
#define TC_T_VPD_DETACH_MAX_MS 20
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

撤去 VBUS 后，双角色电源端口（DRP）检测到已连接的支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）已断开所需的最长时间。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga50a154595c40bba3e46751f6f46df848"></a>

### `TC_T_VPD_DETACH_MIN_MS`

```c
#define TC_T_VPD_DETACH_MIN_MS 10
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

撤去 VBUS 后，双角色电源端口（DRP）检测到已连接的支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）已断开所需的最短时间。

参见表 4-30“DRP 时序参数”（DRP Timing Parameters）。

<a id="ga75223d9754d7ce76e302ee2ed40d11ef"></a>

### `TC_T_VPDCTDD_MAX_MS`

```c
#define TC_T_VPDCTDD_MAX_MS 5
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

撤去 VBUS 后，支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）检测到充电透传供电端（Charge-Through Source）已从 CC 断开、转换到 `CTUnattached.VPD` 状态，并在主机端口 CC 上重新施加通告 3.0 A 的 Rp 终端电阻所需的最长时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="gae2ebe887ccb4f9549d130e85b999062e"></a>

### `TC_T_VPDCTDD_MIN_US`

```c
#define TC_T_VPDCTDD_MIN_US 30
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

撤去 VBUS 后，支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）检测到充电透传供电端（Charge-Through Source）已从 CC 断开、转换到 `CTUnattached.VPD` 状态，并在主机端口 CC 上重新施加通告 3.0 A 的 Rp 终端电阻所需的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga56ece8323bd0a8e4ce0755e0e9e06f96"></a>

### `TC_T_VPDDISABLE_MIN_MS`

```c
#define TC_T_VPDDISABLE_MIN_MS 25
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

支持充电透传的 VCONN 供电 USB 设备（Charge-Through VCONN-Powered USB Device）必须停留在 `CTDisabled.VPD` 状态的最短时间。

参见表 4-31“CC 时序”（CC Timing）。

<a id="ga151c5852b9d2ad3f6f7f0869505e854b"></a>

### `TC_V_SINK_DISCONNECT_MAX_MV`

```c
#define TC_V_SINK_DISCONNECT_MAX_MV 3670
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

受电端断开检测（Sink Disconnect Detection）的最大 VBUS 电压。

参见表 4-3“VBUS 受电端特性”（VBUS Sink Characteristics）。

<a id="ga025aeca5768435b245ecb9fe8bfa29c8"></a>

### `TC_V_SINK_DISCONNECT_MIN_MV`

```c
#define TC_V_SINK_DISCONNECT_MIN_MV 800
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

受电端断开检测（Sink Disconnect Detection）的最小 VBUS 电压。

参见表 4-3“VBUS 受电端特性”（VBUS Sink Characteristics）。

<a id="ga8707ac194510396d55a40887673b53ca"></a>

### `tc_cable_plug`

```c
enum tc_cable_plug
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

线缆插头（Cable Plug）。

参见第 6.2.1.1.7 节“线缆插头”（Cable Plug）。仅适用于 `SOP'` 和 `SOP"`。对于 SOP 数据包，改用 `pd_power_role`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PD_PLUG_FROM_DFP_UFP` | 消息源自下行端口（DFP）或上行端口（UFP）。 |
| `PD_PLUG_FROM_CABLE_VPD` | 消息源自线缆插头（Cable Plug）或 VCONN 供电设备（VPD）。 |

<a id="gac5b4b58840c9b076a869a5816ba100db"></a>

### `tc_cc_polarity`

```c
enum tc_cc_polarity
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

CC 线路极性（CC Line Polarity）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_POLARITY_CC1` | 使用 CC1 输入／输出（I/O）进行电力传输通信（Power Delivery Communication）。 |
| `TC_POLARITY_CC2` | 使用 CC2 输入／输出（I/O）进行电力传输通信（Power Delivery Communication）。 |

<a id="ga0200c820510eb786f3ca30a9b5f7aada"></a>

### `tc_cc_pull`

```c
enum tc_cc_pull
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

CC 上拉／下拉电阻（CC Pull Resistors）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_CC_RA` | Ra 下拉电阻（Pull-Down Resistor）。 |
| `TC_CC_RP` | Rp 上拉电阻（Pull-Up Resistor）。 |
| `TC_CC_RD` | Rd 下拉电阻（Pull-Down Resistor）。 |
| `TC_CC_OPEN` | 无 CC 电阻（CC Resistor）。 |
| `TC_RA_RD` | Ra 和 Rd 下拉电阻（Pull-Down Resistor）。 |

<a id="ga5bb2cfcf3ab60423048db38103657197"></a>

### `tc_cc_states`

```c
enum tc_cc_states
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

根据 CC 线路状态判断的可能端口伙伴连接（Port Partner Connections）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_CC_NONE` | 未接入端口伙伴（Port Partner）。 |
| `TC_CC_UFP_NONE` | 从下行端口（DFP）的视角看：未连接上行端口附件（UFP Accessory）。 |
| `TC_CC_UFP_AUDIO_ACC` | 已连接上行端口音频附件（UFP Audio Accessory）。 |
| `TC_CC_UFP_DEBUG_ACC` | 已连接上行端口调试附件（UFP Debug Accessory）。 |
| `TC_CC_UFP_ATTACHED` | 已接入普通上行端口（Plain UFP）。 |
| `TC_CC_DFP_ATTACHED` | 从上行端口（UFP）的视角看：已接入普通下行端口（Plain DFP）。 |
| `TC_CC_DFP_DEBUG_ACC` | 已连接下行端口调试附件（DFP Debug Accessory）。 |

<a id="ga64e32ec2da97f70fd5b96975317cb92c"></a>

### `tc_cc_voltage_state`

```c
enum tc_cc_voltage_state
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

CC 电压状态（CC Voltage Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_CC_VOLT_OPEN` | 没有端口伙伴连接（Port Partner Connection）。 |
| `TC_CC_VOLT_RA` | 端口伙伴（Port Partner）正在接入 Ra 电阻。 |
| `TC_CC_VOLT_RD` | 端口伙伴（Port Partner）正在接入 Rd 电阻。 |
| `TC_CC_VOLT_RP_DEF` | 端口伙伴（Port Partner）正在接入 Rp 电阻，通告电流为 0.5 A。 |
| `TC_CC_VOLT_RP_1A5` | 端口伙伴（Port Partner）正在接入 Rp 电阻，通告电流为 1.5 A。 |
| `TC_CC_VOLT_RP_3A0` | 端口伙伴（Port Partner）正在接入 Rp 电阻，通告电流为 3.0 A。 |

<a id="ga6b98bbe238e62cfd5531688494a63de2"></a>

### `tc_data_role`

```c
enum tc_data_role
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

电力传输数据角色（Power Delivery Data Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_ROLE_UFP` | 数据角色（Data Role）为上行端口（Upstream Facing Port）。 |
| `TC_ROLE_DFP` | 数据角色（Data Role）为下行端口（Downstream Facing Port）。 |
| `TC_ROLE_DISCONNECTED` | 端口已断开（Disconnected）。 |

<a id="gaa6dda0612045b5f55b9d8ba63d2b9f9d"></a>

### `tc_power_role`

```c
enum tc_power_role
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

电力传输电源角色（Power Delivery Power Role）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_ROLE_SINK` | 电源角色（Power Role）为受电端（Sink）。 |
| `TC_ROLE_SOURCE` | 电源角色（Power Role）为供电端（Source）。 |

<a id="ga7fa5123d0e4404fd9931d162e1152c84"></a>

### `tc_power_role_capability`

```c
enum tc_power_role_capability
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

电力传输电源角色能力（Power Delivery Power Role Capability）。本枚举表示端口已配置的能力（Configured Capability）。

注意（NOTE）：必须与设备树绑定（Devicetree Binding）的 `power-role` 枚举索引一致：`sink` 为 0、`source` 为 1、`dual` 为 2。参见 `dts/bindings/usb-c/usb-c-connector.yaml`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_ROLE_CAP_SINK` | 电源角色能力（Power Role Capability）仅支持受电端（Sink）。 |
| `TC_ROLE_CAP_SOURCE` | 电源角色能力（Power Role Capability）仅支持供电端（Source）。 |
| `TC_ROLE_CAP_DRP` | 电源角色能力（Power Role Capability）支持双角色（DRP），即受电端（Sink）与供电端（Source）。 |

<a id="ga4e0eec97f7c5c97b87eff9561deea2d5"></a>

### `tc_rp_value`

```c
enum tc_rp_value
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

上拉电阻值（Pull-Up Resistor Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_RP_USB` | 对应 900 mA 电流的上拉电阻（Pull-Up Resistor）。 |
| `TC_RP_1A5` | 对应 1.5 A 电流的上拉电阻（Pull-Up Resistor）。 |
| `TC_RP_3A0` | 对应 3.0 A 电流的上拉电阻（Pull-Up Resistor）。 |
| `TC_RP_RESERVED` | 未接入上拉电阻（Pull-Up Resistor）。 |

<a id="ga015455a6c5620dfc96cfb713bbb72161"></a>

### `tc_vbus_level`

```c
enum tc_vbus_level
```

```c
#include <zephyr/drivers/usb_c/usbc_tc.h>
```

VBUS 电压等级（VBUS Level Voltages）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TC_VBUS_SAFE0V` | VBUS 小于 `vSafe0V max`。 |
| `TC_VBUS_PRESENT` | VBUS 至少达到 `vSafe5V min`。 |
| `TC_VBUS_REMOVED` | VBUS 小于 `vSinkDisconnect max`。 |


## 14.6\_原页交叉引用（Cross References）

- [USB 电力传输（USB Power Delivery）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html)
- [USB Type-C 端口控制器 API（Port Controller API）](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html)
- [USB Type-C 电源路径控制器（Power Path Controller）](../api_buffer_paging_topic_reference/P019_USB Type-C 电源路径控制器（Power Path Controller）.md)
- [USB-C 总线电源（VBUS）API](../api_network_time_topic_reference/P026_USB-C 总线电源（VBUS）API.md)
- [usbc_tc.h](../api_file_usb_network_reference/P016_zephyr__drivers__usb_c__usbc_tc.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3"></a>
<a id="gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed"></a>
<a id="ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2"></a>
<a id="ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910"></a>
<a id="gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8"></a>
<a id="gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322"></a>
<a id="gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e"></a>
<a id="gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8"></a>
<a id="gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba"></a>
<a id="gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72"></a>
<a id="gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca"></a>
<a id="gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414"></a>
<a id="gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1"></a>
<a id="gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058"></a>
<a id="ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb"></a>
<a id="ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1"></a>
<a id="gga7fa5123d0e4404fd9931d162e1152c84a9609834767cb8d6fb809723ed39d95ac"></a>
<a id="gga7fa5123d0e4404fd9931d162e1152c84a90e2ae7810814497656c8bcd3c930a28"></a>
<a id="gga7fa5123d0e4404fd9931d162e1152c84a22e4c04eea5706dbd0c51999c0e2f1cf"></a>
<a id="gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb"></a>
<a id="gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28"></a>
<a id="gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c"></a>
<a id="gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1"></a>
<a id="gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827"></a>
<a id="gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5"></a>
<a id="gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc"></a>

---

[上一章](P013_TMAG5273 API主题.md) · [返回大纲](大纲.md)
