---
id: learning.zephyr-docs.api-source-reference.page-891
title: usbc_tc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第891章\_usbc\_tc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h.html)。

## 891.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00325"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="foldopen00343"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00347"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="foldopen00355"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="foldopen00369"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="foldopen00401"></a>
<a id="l00401"></a>
<a id="l00403"></a>
<a id="l00405"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="foldopen00413"></a>
<a id="l00413"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="foldopen00423"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="foldopen00435"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="foldopen00445"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00452"></a>
<a id="l00454"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00461"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="agroup__usb__type__c_html_ga015455a6c5620dfc96cfb713bbb72161"></a>
<a id="agroup__usb__type__c_html_ga0200c820510eb786f3ca30a9b5f7aada"></a>
<a id="agroup__usb__type__c_html_ga4e0eec97f7c5c97b87eff9561deea2d5"></a>
<a id="agroup__usb__type__c_html_ga5bb2cfcf3ab60423048db38103657197"></a>
<a id="agroup__usb__type__c_html_ga64e32ec2da97f70fd5b96975317cb92c"></a>
<a id="agroup__usb__type__c_html_ga6b98bbe238e62cfd5531688494a63de2"></a>
<a id="agroup__usb__type__c_html_ga7fa5123d0e4404fd9931d162e1152c84"></a>
<a id="agroup__usb__type__c_html_ga8707ac194510396d55a40887673b53ca"></a>
<a id="agroup__usb__type__c_html_gaa6dda0612045b5f55b9d8ba63d2b9f9d"></a>
<a id="agroup__usb__type__c_html_gac5b4b58840c9b076a869a5816ba100db"></a>
<a id="agroup__usb__type__c_html_gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5"></a>
<a id="agroup__usb__type__c_html_gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc"></a>
<a id="agroup__usb__type__c_html_gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827"></a>
<a id="agroup__usb__type__c_html_gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8"></a>
<a id="agroup__usb__type__c_html_gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e"></a>
<a id="agroup__usb__type__c_html_gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322"></a>
<a id="agroup__usb__type__c_html_gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e"></a>
<a id="agroup__usb__type__c_html_gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8"></a>
<a id="agroup__usb__type__c_html_gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28"></a>
<a id="agroup__usb__type__c_html_gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1"></a>
<a id="agroup__usb__type__c_html_gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb"></a>
<a id="agroup__usb__type__c_html_gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba"></a>
<a id="agroup__usb__type__c_html_gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca"></a>
<a id="agroup__usb__type__c_html_gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72"></a>
<a id="agroup__usb__type__c_html_gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058"></a>
<a id="agroup__usb__type__c_html_gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1"></a>
<a id="agroup__usb__type__c_html_gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414"></a>
<a id="agroup__usb__type__c_html_gga7fa5123d0e4404fd9931d162e1152c84a22e4c04eea5706dbd0c51999c0e2f1cf"></a>
<a id="agroup__usb__type__c_html_gga7fa5123d0e4404fd9931d162e1152c84a90e2ae7810814497656c8bcd3c930a28"></a>
<a id="agroup__usb__type__c_html_gga7fa5123d0e4404fd9931d162e1152c84a9609834767cb8d6fb809723ed39d95ac"></a>
<a id="agroup__usb__type__c_html_gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed"></a>
<a id="agroup__usb__type__c_html_gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3"></a>
<a id="agroup__usb__type__c_html_ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb"></a>
<a id="agroup__usb__type__c_html_ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1"></a>
<a id="agroup__usb__type__c_html_ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2"></a>
<a id="agroup__usb__type__c_html_ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>

```c
/*
 * Copyright 2022 The Chromium OS Authors
 * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TC_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TC_H_


#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define TC_V_SINK_DISCONNECT_MIN_MV 800

#define TC_V_SINK_DISCONNECT_MAX_MV 3670

#define TC_T_VBUS_ON_MAX_MS 275

#define TC_T_VBUS_OFF_MAX_MS 650

#define TC_T_VCONN_ON_MAX_MS 2

#define TC_T_VCONN_ON_PA_MAX_MS 100

#define TC_T_VCONN_OFF_MAX_MS 35

#define TC_T_SINK_ADJ_MAX_MS 60

#define TC_T_DRP_MIN_MS 50

#define TC_T_DRP_MAX_MS 100

#define TC_T_DRP_PW_MIN_MS 15

#define TC_T_DRP_PW_MAX_MS 70

#define TC_T_DRP_TRANSITION_MIN_MS 0

#define TC_T_DRP_TRANSITION_MAX_MS 1

#define TC_T_DRP_TRY_MIN_MS 75

#define TC_T_DRP_TRY_MAX_MS 150

#define TC_T_DRP_TRY_WAIT_MIN_MS 400

#define TC_T_DRP_TRY_WAIT_MAX_MS 800

#define TC_T_TRY_TIMEOUT_MIN_MS 550

#define TC_T_TRY_TIMEOUT_MAX_MS 1100

#define TC_T_VPD_DETACH_MIN_MS 10

#define TC_T_VPD_DETACH_MAX_MS 20

#define TC_T_CC_DEBOUNCE_MIN_MS 100

#define TC_T_CC_DEBOUNCE_MAX_MS 200

#define TC_T_PD_DEBOUNCE_MIN_MS 10

#define TC_T_PD_DEBOUNCE_MAX_MS 20

#define TC_T_TRY_CC_DEBOUNCE_MIN_MS 10

#define TC_T_TRY_CC_DEBOUNCE_MAX_MS 10

#define TC_T_ERROR_RECOVERY_SELF_POWERED_MIN_MS 25

#define TC_T_ERROR_RECOVERY_SOURCE_MIN_MS 240

#define TC_T_RP_VALUE_CHANGE_MIN_MS 10

#define TC_T_RP_VALUE_CHANGE_MAX_MS 20

#define TC_T_SRC_DISCONNECT_MIN_MS 0

#define TC_T_SRC_DISCONNECT_MAX_MS 20

#define TC_T_NO_TOGGLE_CONNECT_MIN_MS 0

#define TC_T_NO_TOGGLE_CONNECT_MAX_MS 5

#define TC_T_ONE_PORT_TOGGLE_CONNECT_MIN_MS 0

#define TC_T_ONE_PORT_TOGGLE_CONNECT_MAX_MS 80

#define TC_T_TWO_PORT_TOGGLE_CONNECT_MIN_MS 0

#define TC_T_TWO_PORT_TOGGLE_CONNECT_MAX_MS 510

#define TC_T_VPDCTDD_MIN_US 30

#define TC_T_VPDCTDD_MAX_MS 5

#define TC_T_VPDDISABLE_MIN_MS 25

enum tc_cc_voltage_state {
        TC_CC_VOLT_OPEN         = 0,
        TC_CC_VOLT_RA           = 1,
        TC_CC_VOLT_RD           = 2,
        TC_CC_VOLT_RP_DEF       = 5,
        TC_CC_VOLT_RP_1A5       = 6,
        TC_CC_VOLT_RP_3A0       = 7,
};

enum tc_vbus_level {
        TC_VBUS_SAFE0V  = 0,
        TC_VBUS_PRESENT = 1,
        TC_VBUS_REMOVED = 2
};

enum tc_rp_value {
        TC_RP_USB       = 0,
        TC_RP_1A5       = 1,
        TC_RP_3A0       = 2,
        TC_RP_RESERVED  = 3
};

enum tc_cc_pull {
        TC_CC_RA        = 0,
        TC_CC_RP        = 1,
        TC_CC_RD        = 2,
        TC_CC_OPEN      = 3,
        TC_RA_RD        = 4
};

enum tc_cable_plug {
        PD_PLUG_FROM_DFP_UFP = 0,
        PD_PLUG_FROM_CABLE_VPD = 1
};

enum tc_power_role_capability {
        TC_ROLE_CAP_SINK = 0,
        TC_ROLE_CAP_SOURCE = 1,
        TC_ROLE_CAP_DRP = 2
};

enum tc_power_role {
        TC_ROLE_SINK    = 0,
        TC_ROLE_SOURCE  = 1
};

enum tc_data_role {
        TC_ROLE_UFP             = 0,
        TC_ROLE_DFP             = 1,
        TC_ROLE_DISCONNECTED    = 2
};

enum tc_cc_polarity {
        TC_POLARITY_CC1 = 0,
        TC_POLARITY_CC2 = 1
};

enum tc_cc_states {
        TC_CC_NONE = 0,


        TC_CC_UFP_NONE          = 1,
        TC_CC_UFP_AUDIO_ACC     = 2,
        TC_CC_UFP_DEBUG_ACC     = 3,
        TC_CC_UFP_ATTACHED      = 4,


        TC_CC_DFP_ATTACHED      = 5,
        TC_CC_DFP_DEBUG_ACC     = 6
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TC_H_ */
```

## 891.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The Chromium OS Authors。

版权（Copyright）：© Qualcomm Technologies, Inc. and/or its subsidiaries.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 476 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_TC_H_`。

## 891.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tc_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [tc_cc_voltage_state](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga64e32ec2da97f70fd5b96975317cb92c)
- [TC_CC_VOLT_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca1f4b82ea64d23167df5083fd7550cf05)
- [TC_CC_VOLT_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca17a8d72f4dc6b29e1d4ad35a4f1531ea)
- [TC_CC_VOLT_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca2267bbcda871c265e77228a5fe6342a9)
- [TC_CC_VOLT_RP_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca06bd58eb73aa7f097046e7b88fde0293)
- [TC_CC_VOLT_RP_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca3cc0d3c1ac9775b1b8ba77b87868bc72)
- [TC_CC_VOLT_RP_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga64e32ec2da97f70fd5b96975317cb92ca3965e449dbcc8ca6e87d72cd5a73f0ca)
- [tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)
- [TC_VBUS_SAFE0V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga015455a6c5620dfc96cfb713bbb72161a86bf4c0568d7a7ec89180e8e36c91827)
- [TC_VBUS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga015455a6c5620dfc96cfb713bbb72161a33f8f0dac47bfaffe331553cd42495f5)
- [TC_VBUS_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga015455a6c5620dfc96cfb713bbb72161a84aaa14f5d6dd4b1bf52564af73f24bc)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [TC_RP_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga4e0eec97f7c5c97b87eff9561deea2d5a22d5e50479ca672f0469af9006b4f4bb)
- [TC_RP_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga4e0eec97f7c5c97b87eff9561deea2d5a1c74df7e2b6bbe75d8c61ca4a7202a28)
- [TC_RP_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga4e0eec97f7c5c97b87eff9561deea2d5afa7eda9742f3670a90736a52620cfe3c)
- [TC_RP_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga4e0eec97f7c5c97b87eff9561deea2d5a215508ac427e2cc53478e5f096a400d1)
- [tc_cc_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga0200c820510eb786f3ca30a9b5f7aada)
- [TC_CC_RA](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga0200c820510eb786f3ca30a9b5f7aadaaf52a9f9d10c81fca5b048ad2230cf1e8)
- [TC_CC_RP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga0200c820510eb786f3ca30a9b5f7aadaa7a0a6a716cb42af3a572f43bedc2a322)
- [TC_CC_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga0200c820510eb786f3ca30a9b5f7aadaa60a4e008afce1c9395a0fb6d34767c6e)
- [TC_CC_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga0200c820510eb786f3ca30a9b5f7aadaa4859548c59439c79e3ad080e1fa07fa8)
- [TC_RA_RD](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga0200c820510eb786f3ca30a9b5f7aadaa95c81809d680f28281e9dcaef4fff35e)
- [tc_cable_plug](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga8707ac194510396d55a40887673b53ca)
- [PD_PLUG_FROM_DFP_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga8707ac194510396d55a40887673b53caad1092c45d3fad497dbafe15fd9f1c3b3)
- [PD_PLUG_FROM_CABLE_VPD](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga8707ac194510396d55a40887673b53caa49960a4dee1da0c7330cce2b13c4c0ed)
- [tc_power_role_capability](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga7fa5123d0e4404fd9931d162e1152c84)
- [TC_ROLE_CAP_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga7fa5123d0e4404fd9931d162e1152c84a9609834767cb8d6fb809723ed39d95ac)
- [TC_ROLE_CAP_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga7fa5123d0e4404fd9931d162e1152c84a90e2ae7810814497656c8bcd3c930a28)
- [TC_ROLE_CAP_DRP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga7fa5123d0e4404fd9931d162e1152c84a22e4c04eea5706dbd0c51999c0e2f1cf)
- [tc_power_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gaa6dda0612045b5f55b9d8ba63d2b9f9d)
- [TC_ROLE_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ggaa6dda0612045b5f55b9d8ba63d2b9f9da0023468cf2e977c8372899e6f1a0aafb)
- [TC_ROLE_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ggaa6dda0612045b5f55b9d8ba63d2b9f9da1b8caf27ae76de5ea874b0e52adc4cf1)
- [tc_data_role](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga6b98bbe238e62cfd5531688494a63de2)
- [TC_ROLE_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga6b98bbe238e62cfd5531688494a63de2a9472c4319bf0be6937436e1602c7b414)
- [TC_ROLE_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga6b98bbe238e62cfd5531688494a63de2a812112dccb0c3d8dd555d351a7f5b9e1)
- [TC_ROLE_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga6b98bbe238e62cfd5531688494a63de2a155c3d22f151d83899f46e516e88a058)
- [tc_cc_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gac5b4b58840c9b076a869a5816ba100db)
- [TC_POLARITY_CC1](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ggac5b4b58840c9b076a869a5816ba100dba1ace08cbeb63866305ccfb0c3bf338c2)
- [TC_POLARITY_CC2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ggac5b4b58840c9b076a869a5816ba100dbae3ad03c80e84e32f8974a14e815ed910)
- [tc_cc_states](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga5bb2cfcf3ab60423048db38103657197)
- [TC_CC_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a21cf3890c4a2fa6ee9f137f2b22e51f0)
- [TC_CC_UFP_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a90544a6af90af7722cec8ffe83f752f0)
- [TC_CC_UFP_AUDIO_ACC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a4b841a1438a120652ab78fb3ae2c7dea)
- [TC_CC_UFP_DEBUG_ACC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197aaba130e5d3d999794eb87e2b8a09cf78)
- [TC_CC_UFP_ATTACHED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a0cfcabb4325e4b59213002aaeda75524)
- [TC_CC_DFP_ATTACHED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a950c6ff65a4af5db2f1fdab3383489ba)
- [TC_CC_DFP_DEBUG_ACC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#gga5bb2cfcf3ab60423048db38103657197a8821754209b4cd977b2c97d43957166c)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P890_usbc_pd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P892_usbc_tcpc.h_源码浏览.md)
