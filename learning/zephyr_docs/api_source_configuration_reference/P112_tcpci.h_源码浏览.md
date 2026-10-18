---
id: learning.zephyr-docs.api-source-configuration-reference.page-112
title: tcpci.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_tcpci.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html)。

## 112.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00315"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00324"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00361"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00378"></a>
<a id="l00380"></a>
<a id="l00382"></a>
<a id="l00384"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="foldopen00401"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00410"></a>
<a id="foldopen00412"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00417"></a>
<a id="l00419"></a>
<a id="l00421"></a>
<a id="l00423"></a>
<a id="l00425"></a>
<a id="l00427"></a>
<a id="l00429"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00438"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00460"></a>
<a id="l00462"></a>
<a id="l00464"></a>
<a id="l00470"></a>
<a id="l00475"></a>
<a id="l00477"></a>
<a id="foldopen00479"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="foldopen00490"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00503"></a>
<a id="l00505"></a>
<a id="l00507"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00516"></a>
<a id="l00518"></a>
<a id="l00520"></a>
<a id="l00522"></a>
<a id="l00524"></a>
<a id="l00526"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00535"></a>
<a id="l00537"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00556"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00577"></a>
<a id="l00579"></a>
<a id="l00581"></a>
<a id="l00583"></a>
<a id="l00585"></a>
<a id="l00587"></a>
<a id="l00589"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00595"></a>
<a id="l00597"></a>
<a id="l00599"></a>
<a id="l00601"></a>
<a id="foldopen00606"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00612"></a>
<a id="l00620"></a>
<a id="l00622"></a>
<a id="l00624"></a>
<a id="l00626"></a>
<a id="l00628"></a>
<a id="l00630"></a>
<a id="l00632"></a>
<a id="l00634"></a>
<a id="l00636"></a>
<a id="foldopen00638"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00651"></a>
<a id="l00653"></a>
<a id="l00655"></a>
<a id="l00657"></a>
<a id="l00659"></a>
<a id="l00661"></a>
<a id="l00663"></a>
<a id="l00665"></a>
<a id="l00667"></a>
<a id="l00669"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="foldopen00691"></a>
<a id="l00691"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="foldopen00699"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00704"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00715"></a>
<a id="l00716"></a>
<a id="l00718"></a>
<a id="l00725"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00732"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00744"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00761"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00775"></a>
<a id="l00777"></a>
<a id="l00779"></a>
<a id="l00781"></a>
<a id="l00783"></a>
<a id="l00785"></a>
<a id="l00787"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>

```c
/*
 * Copyright 2024 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_USB_C_TCPCI_H_
#define ZEPHYR_INCLUDE_USB_C_TCPCI_H_


#define TCPC_REG_VENDOR_ID 0x0

#define TCPC_REG_PRODUCT_ID 0x2

#define TCPC_REG_BCD_DEV 0x4

#define TCPC_REG_TC_REV            0x6
#define TCPC_REG_TC_REV_MAJOR_MASK GENMASK(7, 4)
#define TCPC_REG_TC_REV_MAJOR(reg) (((reg) & TCPC_REG_TC_REV_MAJOR_MASK) >> 4)
#define TCPC_REG_TC_REV_MINOR_MASK GENMASK(3, 0)
#define TCPC_REG_TC_REV_MINOR(reg) ((reg) & TCPC_REG_TC_REV_MINOR_MASK)

#define TCPC_REG_PD_REV                0x8
#define TCPC_REG_PD_REV_REV_MAJOR_MASK GENMASK(15, 12)
#define TCPC_REG_PD_REV_REV_MAJOR(reg) (((reg) & TCPC_REG_PD_REV_REV_MAJOR_MASK) >> 12)
#define TCPC_REG_PD_REV_REV_MINOR_MASK GENMASK(11, 8)
#define TCPC_REG_PD_REV_REV_MINOR(reg) (((reg) & TCPC_REG_PD_REV_REV_MINOR_MASK) >> 8)
#define TCPC_REG_PD_REV_VER_MAJOR_MASK GENMASK(7, 4)
#define TCPC_REG_PD_REV_VER_MAJOR(reg) (((reg) & TCPC_REG_PD_REV_VER_MAJOR_MASK) >> 4)
#define TCPC_REG_PD_REV_VER_MINOR_MASK GENMASK(3, 0)
#define TCPC_REG_PD_REV_VER_MINOR(reg) ((reg) & TCPC_REG_PD_REV_VER_MINOR_MASK)

#define TCPC_REG_PD_INT_REV                0xa
#define TCPC_REG_PD_INT_REV_REV_MAJOR_MASK GENMASK(15, 12)
#define TCPC_REG_PD_INT_REV_REV_MAJOR(reg) (((reg) & TCPC_REG_PD_INT_REV_REV_MAJOR_MASK) >> 12)
#define TCPC_REG_PD_INT_REV_REV_MINOR_MASK GENMASK(11, 8)
#define TCPC_REG_PD_INT_REV_REV_MINOR(reg) (((reg) & TCPC_REG_PD_INT_REV_REV_MINOR_MASK) >> 8)
#define TCPC_REG_PD_INT_REV_VER_MAJOR_MASK GENMASK(7, 4)
#define TCPC_REG_PD_INT_REV_VER_MAJOR(reg) (((reg) & TCPC_REG_PD_INT_REV_VER_MAJOR_MASK) >> 4)
#define TCPC_REG_PD_INT_REV_VER_MINOR_MASK GENMASK(3, 0)
#define TCPC_REG_PD_INT_REV_VER_MINOR(reg) ((reg) & TCPC_REG_PD_INT_REV_VER_MINOR_MASK)

#define TCPC_REG_ALERT              0x10
#define TCPC_REG_ALERT_NONE         0x0000
#define TCPC_REG_ALERT_MASK_ALL     0xffff
#define TCPC_REG_ALERT_VENDOR_DEF   BIT(15)
#define TCPC_REG_ALERT_ALERT_EXT    BIT(14)
#define TCPC_REG_ALERT_EXT_STATUS   BIT(13)
#define TCPC_REG_ALERT_RX_BEGINNING BIT(12)
#define TCPC_REG_ALERT_VBUS_DISCNCT BIT(11)
#define TCPC_REG_ALERT_RX_BUF_OVF   BIT(10)
#define TCPC_REG_ALERT_FAULT        BIT(9)
#define TCPC_REG_ALERT_V_ALARM_LO   BIT(8)
#define TCPC_REG_ALERT_V_ALARM_HI   BIT(7)
#define TCPC_REG_ALERT_TX_SUCCESS   BIT(6)
#define TCPC_REG_ALERT_TX_DISCARDED BIT(5)
#define TCPC_REG_ALERT_TX_FAILED    BIT(4)
#define TCPC_REG_ALERT_RX_HARD_RST  BIT(3)
#define TCPC_REG_ALERT_RX_STATUS    BIT(2)
#define TCPC_REG_ALERT_POWER_STATUS BIT(1)
#define TCPC_REG_ALERT_CC_STATUS    BIT(0)
#define TCPC_REG_ALERT_TX_COMPLETE                                                                 \
        (TCPC_REG_ALERT_TX_SUCCESS | TCPC_REG_ALERT_TX_DISCARDED | TCPC_REG_ALERT_TX_FAILED)

#define TCPC_REG_ALERT_MASK 0x12

#define TCPC_REG_POWER_STATUS_MASK 0x14

#define TCPC_REG_FAULT_STATUS_MASK 0x15

#define TCPC_REG_EXT_STATUS_MASK 0x16

#define TCPC_REG_ALERT_EXT_MASK 0x17

#define TCPC_REG_CONFIG_STD_OUTPUT                   0x18
#define TCPC_REG_CONFIG_STD_OUTPUT_HIGH_Z            BIT(7)
#define TCPC_REG_CONFIG_STD_OUTPUT_DBG_ACC_CONN_N    BIT(6)
#define TCPC_REG_CONFIG_STD_OUTPUT_AUDIO_CONN_N      BIT(5)
#define TCPC_REG_CONFIG_STD_OUTPUT_ACTIVE_CABLE      BIT(4)
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_MASK          (3 << 2)
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_NONE          (0 << 2)
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB           (1 << 2)
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_DP            (2 << 2)
#define TCPC_REG_CONFIG_STD_OUTPUT_MUX_USB_DP        (3 << 2)
#define TCPC_REG_CONFIG_STD_OUTPUT_CONN_PRESENT      BIT(1)
#define TCPC_REG_CONFIG_STD_OUTPUT_CONNECTOR_FLIPPED BIT(0)

#define TCPC_REG_TCPC_CTRL                           0x19
#define TCPC_REG_TCPC_CTRL_SMBUS_PEC                 BIT(7)
#define TCPC_REG_TCPC_CTRL_EN_LOOK4CONNECTION_ALERT  BIT(6)
#define TCPC_REG_TCPC_CTRL_WATCHDOG_TIMER            BIT(5)
#define TCPC_REG_TCPC_CTRL_DEBUG_ACC_CONTROL         BIT(4)
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_MASK        GENMASK(3, 2)
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_DISABLED    0
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_ALWAYS   (2 << 2)
#define TCPC_REG_TCPC_CTRL_CLOCK_STRETCH_EN_NO_ALERT (3 << 2)
#define TCPC_REG_TCPC_CTRL_BIST_TEST_MODE            BIT(1)
#define TCPC_REG_TCPC_CTRL_PLUG_ORIENTATION          BIT(0)

#define TCPC_REG_ROLE_CTRL          0x1a
#define TCPC_REG_ROLE_CTRL_DRP_MASK BIT(6)
#define TCPC_REG_ROLE_CTRL_RP_MASK  GENMASK(5, 4)
#define TCPC_REG_ROLE_CTRL_CC2_MASK GENMASK(3, 2)
#define TCPC_REG_ROLE_CTRL_CC1_MASK GENMASK(1, 0)
#define TCPC_REG_ROLE_CTRL_SET(drp, rp, cc1, cc2)                                                  \
        ((((drp) << 6) & TCPC_REG_ROLE_CTRL_DRP_MASK) |                                            \
         (((rp) << 4) & TCPC_REG_ROLE_CTRL_RP_MASK) |                                              \
         (((cc2) << 2) & TCPC_REG_ROLE_CTRL_CC2_MASK) | ((cc1) & TCPC_REG_ROLE_CTRL_CC1_MASK))

#define TCPC_REG_ROLE_CTRL_DRP(reg) (((reg) & TCPC_REG_ROLE_CTRL_DRP_MASK) >> 6)
#define TCPC_REG_ROLE_CTRL_RP(reg)  (((reg) & TCPC_REG_ROLE_CTRL_RP_MASK) >> 4)
#define TCPC_REG_ROLE_CTRL_CC2(reg) (((reg) & TCPC_REG_ROLE_CTRL_CC2_MASK) >> 2)
#define TCPC_REG_ROLE_CTRL_CC1(reg) ((reg) & TCPC_REG_ROLE_CTRL_CC1_MASK)

#define TCPC_REG_FAULT_CTRL                      0x1b
#define TCPC_REG_FAULT_CTRL_VBUS_FORCE_OFF       BIT(4)
#define TCPC_REG_FAULT_CTRL_VBUS_DISCHARGE_FAULT BIT(3)
#define TCPC_REG_FAULT_CTRL_VBUS_OCP_FAULT_DIS   BIT(2)
#define TCPC_REG_FAULT_CTRL_VBUS_OVP_FAULT_DIS   BIT(1)
#define TCPC_REG_FAULT_CTRL_VCONN_OCP_FAULT_DIS  BIT(0)

#define TCPC_REG_POWER_CTRL                           0x1c
#define TCPC_REG_POWER_CTRL_FRS_ENABLE                BIT(7)
#define TCPC_REG_POWER_CTRL_VBUS_VOL_MONITOR_DIS      BIT(6)
#define TCPC_REG_POWER_CTRL_VOLT_ALARM_DIS            BIT(5)
#define TCPC_REG_POWER_CTRL_AUTO_DISCHARGE_DISCONNECT BIT(4)
#define TCPC_REG_POWER_CTRL_BLEED_DISCHARGE           BIT(3)
#define TCPC_REG_POWER_CTRL_FORCE_DISCHARGE           BIT(2)
#define TCPC_REG_POWER_CTRL_VCONN_SUPP                BIT(1)
#define TCPC_REG_POWER_CTRL_VCONN_EN                  BIT(0)

#define TCPC_REG_CC_STATUS                 0x1d
#define TCPC_REG_CC_STATUS_LOOK4CONNECTION BIT(5)
#define TCPC_REG_CC_STATUS_CONNECT_RESULT  BIT(4)
#define TCPC_REG_CC_STATUS_CC2_STATE_MASK  GENMASK(3, 2)
#define TCPC_REG_CC_STATUS_CC2_STATE(reg)  (((reg) & TCPC_REG_CC_STATUS_CC2_STATE_MASK) >> 2)
#define TCPC_REG_CC_STATUS_CC1_STATE_MASK  GENMASK(1, 0)
#define TCPC_REG_CC_STATUS_CC1_STATE(reg)  ((reg) & TCPC_REG_CC_STATUS_CC1_STATE_MASK)

#define TCPC_REG_POWER_STATUS               0x1e
#define TCPC_REG_POWER_STATUS_DEBUG_ACC_CON BIT(7)
#define TCPC_REG_POWER_STATUS_UNINIT        BIT(6)
#define TCPC_REG_POWER_STATUS_SOURCING_HV   BIT(5)
#define TCPC_REG_POWER_STATUS_SOURCING_VBUS BIT(4)
#define TCPC_REG_POWER_STATUS_VBUS_DET      BIT(3)
#define TCPC_REG_POWER_STATUS_VBUS_PRES     BIT(2)
#define TCPC_REG_POWER_STATUS_VCONN_PRES    BIT(1)
#define TCPC_REG_POWER_STATUS_SINKING_VBUS  BIT(0)

#define TCPC_REG_FAULT_STATUS                      0x1f
#define TCPC_REG_FAULT_STATUS_ALL_REGS_RESET       BIT(7)
#define TCPC_REG_FAULT_STATUS_FORCE_OFF_VBUS       BIT(6)
#define TCPC_REG_FAULT_STATUS_AUTO_DISCHARGE_FAIL  BIT(5)
#define TCPC_REG_FAULT_STATUS_FORCE_DISCHARGE_FAIL BIT(4)
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_CURRENT    BIT(3)
#define TCPC_REG_FAULT_STATUS_VBUS_OVER_VOLTAGE    BIT(2)
#define TCPC_REG_FAULT_STATUS_VCONN_OVER_CURRENT   BIT(1)
#define TCPC_REG_FAULT_STATUS_I2C_INTERFACE_ERR    BIT(0)

#define TCPC_REG_EXT_STATUS        0x20
#define TCPC_REG_EXT_STATUS_SAFE0V BIT(0)

#define TCPC_REG_ALERT_EXT               0x21
#define TCPC_REG_ALERT_EXT_TIMER_EXPIRED BIT(2)
#define TCPC_REG_ALERT_EXT_SRC_FRS       BIT(1)
#define TCPC_REG_ALERT_EXT_SNK_FRS       BIT(0)

#define TCPC_REG_COMMAND                     0x23
#define TCPC_REG_COMMAND_WAKE_I2C            0x11
#define TCPC_REG_COMMAND_DISABLE_VBUS_DETECT 0x22
#define TCPC_REG_COMMAND_ENABLE_VBUS_DETECT  0x33
#define TCPC_REG_COMMAND_SNK_CTRL_LOW        0x44
#define TCPC_REG_COMMAND_SNK_CTRL_HIGH       0x55
#define TCPC_REG_COMMAND_SRC_CTRL_LOW        0x66
#define TCPC_REG_COMMAND_SRC_CTRL_DEF        0x77
#define TCPC_REG_COMMAND_SRC_CTRL_HV         0x88
#define TCPC_REG_COMMAND_LOOK4CONNECTION     0x99
#define TCPC_REG_COMMAND_RX_ONE_MORE         0xAA
#define TCPC_REG_COMMAND_SEND_FRS_SIGNAL     0xCC
#define TCPC_REG_COMMAND_RESET_TRANSMIT_BUF  0xDD
#define TCPC_REG_COMMAND_RESET_RECEIVE_BUF   0xEE
#define TCPC_REG_COMMAND_I2CIDLE             0xFF

#define TCPC_REG_DEV_CAP_1                                 0x24
#define TCPC_REG_DEV_CAP_1_VBUS_NONDEFAULT_TARGET          BIT(15)
#define TCPC_REG_DEV_CAP_1_VBUS_OCP_REPORTING              BIT(14)
#define TCPC_REG_DEV_CAP_1_VBUS_OVP_REPORTING              BIT(13)
#define TCPC_REG_DEV_CAP_1_BLEED_DISCHARGE                 BIT(12)
#define TCPC_REG_DEV_CAP_1_FORCE_DISCHARGE                 BIT(11)
#define TCPC_REG_DEV_CAP_1_VBUS_MEASURE_ALARM_CAPABLE      BIT(10)
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK               GENMASK(9, 8)
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR(reg)               \
        (((reg) & TCPC_REG_DEV_CAP_1_SRC_RESISTOR_MASK) >> 8)

#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_DEF             0
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_1P5_DEF         1
#define TCPC_REG_DEV_CAP_1_SRC_RESISTOR_RP_3P0_1P5_DEF     2
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK                 GENMASK(7, 5)
#define TCPC_REG_DEV_CAP_1_POWER_ROLE(reg)                 \
        (((reg) & TCPC_REG_DEV_CAP_1_POWER_ROLE_MASK) >> 5)

#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_OR_SNK           0
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC                  1
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK                  2
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SNK_ACC              3
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_DRP                  4
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP_ADPT_CBL 5
#define TCPC_REG_DEV_CAP_1_POWER_ROLE_SRC_SNK_DRP          6
#define TCPC_REG_DEV_CAP_1_ALL_SOP_STAR_MSGS_SUPPORTED     BIT(4)
#define TCPC_REG_DEV_CAP_1_SOURCE_VCONN                    BIT(3)
#define TCPC_REG_DEV_CAP_1_SINK_VBUS                       BIT(2)
#define TCPC_REG_DEV_CAP_1_SOURCE_HV_VBUS                  BIT(1)
#define TCPC_REG_DEV_CAP_1_SOURCE_VBUS                     BIT(0)

#define TCPC_REG_DEV_CAP_2                         0x26
#define TCPC_REG_DEV_CAP_2_CAP_3_SUPPORTED         BIT(15)
#define TCPC_REG_DEV_CAP_2_MSG_DISABLE_DISCONNECT  BIT(14)
#define TCPC_REG_DEV_CAP_2_GENERIC_TIMER           BIT(13)
#define TCPC_REG_DEV_CAP_2_LONG_MSG                BIT(12)
#define TCPC_REG_DEV_CAP_2_SMBUS_PEC               BIT(11)
#define TCPC_REG_DEV_CAP_2_SRC_FRS                 BIT(10)
#define TCPC_REG_DEV_CAP_2_SNK_FRS                 BIT(9)
#define TCPC_REG_DEV_CAP_2_WATCHDOG_TIMER          BIT(8)
#define TCPC_REG_DEV_CAP_2_SNK_DISC_DET            BIT(7)
#define TCPC_REG_DEV_CAP_2_STOP_DISCHARGE_THRESH   BIT(6)
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK GENMASK(5, 4)
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM(reg)                                                 \
        (((reg) & TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_MASK) >> 4)

#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_25MV    0
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_50MV    1
#define TCPC_REG_DEV_CAP_2_VBUS_VOLTAGE_ALARM_100MV   2
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK GENMASK(3, 1)
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED(reg)                                              \
        (((reg) & TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_MASK) >> 1)

#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_0W     0
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_1_5W     1
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_2_0W     2
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_3_0W     3
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_4_0W     4
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_5_0W     5
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_6_0W     6
#define TCPC_REG_DEV_CAP_2_VCONN_POWER_SUPPORTED_EXTERNAL 7
#define TCPC_REG_DEV_CAP_2_VCONN_OVC_FAULT                BIT(0)

#define TCPC_REG_STD_INPUT_CAP                0x28
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK   GENMASK(4, 3)
#define TCPC_REG_STD_INPUT_CAP_SRC_FRS(reg)   (((reg) & TCPC_REG_STD_INPUT_CAP_SRC_FRS_MASK) >> 3)
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_NONE   0
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_INPUT  1
#define TCPC_REG_STD_INTPU_CAP_SRC_FRS_BOTH   2
#define TCPC_REG_STD_INPUT_CAP_EXT_OVP        BIT(2)
#define TCPC_REG_STD_INPUT_CAP_EXT_OCP        BIT(1)
#define TCPC_REG_STD_INPUT_CAP_FORCE_OFF_VBUS BIT(0)

#define TCPC_REG_STD_OUTPUT_CAP                  0x29
#define TCPC_REG_STD_OUTPUT_CAP_SNK_DISC_DET     BIT(7)
#define TCPC_REG_STD_OUTPUT_CAP_DBG_ACCESSORY    BIT(6)
#define TCPC_REG_STD_OUTPUT_CAP_VBUS_PRESENT_MON BIT(5)
#define TCPC_REG_STD_OUTPUT_CAP_AUDIO_ACCESSORY  BIT(4)
#define TCPC_REG_STD_OUTPUT_CAP_ACTIVE_CABLE     BIT(3)
#define TCPC_REG_STD_OUTPUT_CAP_MUX_CFG_CTRL     BIT(2)
#define TCPC_REG_STD_OUTPUT_CAP_CONN_PRESENT     BIT(1)
#define TCPC_REG_STD_OUTPUT_CAP_CONN_ORIENTATION BIT(0)

#define TCPC_REG_CONFIG_EXT_1                0x2A
#define TCPC_REG_CONFIG_EXT_1_FRS_SNK_DIR    BIT(1)
#define TCPC_REG_CONFIG_EXT_1_STD_IN_SRC_FRS BIT(0)

#define TCPC_REG_GENERIC_TIMER 0x2c

#define TCPC_REG_MSG_HDR_INFO                 0x2e
#define TCPC_REG_MSG_HDR_INFO_CABLE_PLUG      BIT(4)
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK  BIT(3)
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE(reg)  (((reg) & TCPC_REG_MSG_HDR_INFO_DATA_ROLE_MASK) >> 3)
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_UFP   0
#define TCPC_REG_MSG_HDR_INFO_DATA_ROLE_DFP   1
#define TCPC_REG_MSG_HDR_INFO_PD_REV_MASK     GENMASK(2, 1)
#define TCPC_REG_MSG_HDR_INFO_PD_REV(reg)     (((reg) & TCPC_REG_MSG_HDR_INFO_PD_REV_MASK) >> 1)
#define TCPC_REG_MSG_HDR_INFO_PD_REV_1_0      0
#define TCPC_REG_MSG_HDR_INFO_PD_REV_2_0      1
#define TCPC_REG_MSG_HDR_INFO_PD_REV_3_0      2
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK BIT(0)
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE(reg) ((reg) & TCPC_REG_MSG_HDR_INFO_POWER_ROLE_MASK)
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SNK  0
#define TCPC_REG_MSG_HDR_INFO_POWER_ROLE_SRC  1
#define TCPC_REG_MSG_HDR_INFO_SET(pd_rev_type, drole, prole)                                       \
        ((drole) << 3 | (pd_rev_type << 1) | (prole))

#define TCPC_REG_MSG_HDR_INFO_ROLES_MASK (TCPC_REG_MSG_HDR_INFO_SET(3, 1, 1))

#define TCPC_REG_RX_DETECT                        0x2f
#define TCPC_REG_RX_DETECT_MSG_DISABLE_DISCONNECT BIT(7)
#define TCPC_REG_RX_DETECT_CABLE_RST              BIT(6)
#define TCPC_REG_RX_DETECT_HRST                   BIT(5)
#define TCPC_REG_RX_DETECT_SOPPP_DBG              BIT(4)
#define TCPC_REG_RX_DETECT_SOPP_DBG               BIT(3)
#define TCPC_REG_RX_DETECT_SOPPP                  BIT(2)
#define TCPC_REG_RX_DETECT_SOPP                   BIT(1)
#define TCPC_REG_RX_DETECT_SOP                    BIT(0)
#define TCPC_REG_RX_DETECT_SOP_HRST_MASK          (TCPC_REG_RX_DETECT_SOP | TCPC_REG_RX_DETECT_HRST)
#define TCPC_REG_RX_DETECT_SOP_SOPP_SOPPP_HRST_MASK                                                \
        (TCPC_REG_RX_DETECT_SOP | TCPC_REG_RX_DETECT_SOPP | TCPC_REG_RX_DETECT_SOPPP |             \
         TCPC_REG_RX_DETECT_HRST)

#define TCPC_REG_RX_BUFFER 0x30

#define TCPC_REG_TRANSMIT                               0x50
#define TCPC_REG_TRANSMIT_SET_WITH_RETRY(retries, type) ((retries) << 4 | (type))
#define TCPC_REG_TRANSMIT_SET_WITHOUT_RETRY(type)       (type)
#define TCPC_REG_TRANSMIT_TYPE_SOP                      0
#define TCPC_REG_TRANSMIT_TYPE_SOPP                     1
#define TCPC_REG_TRANSMIT_TYPE_SOPPP                    2
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_P                3
#define TCPC_REG_TRANSMIT_TYPE_SOP_DBG_PP               4
#define TCPC_REG_TRANSMIT_TYPE_HRST                     5
#define TCPC_REG_TRANSMIT_TYPE_CABLE_RST                6
#define TCPC_REG_TRANSMIT_TYPE_BIST                     7

#define TCPC_REG_TX_BUFFER 0x51

#define TCPC_REG_VBUS_VOLTAGE                   0x70
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK  GENMASK(9, 0)
#define TCPC_REG_VBUS_VOLTAGE_MEASUREMENT(reg)  ((reg) & TCPC_REG_VBUS_VOLTAGE_MEASUREMENT_MASK)
#define TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK GENMASK(11, 10)
#define TCPC_REG_VBUS_VOLTAGE_SCALE(reg)                                                           \
        (1 << (((reg) & TCPC_REG_VBUS_VOLTAGE_SCALE_FACTOR_MASK) >> 10))

#define TCPC_REG_VBUS_VOLTAGE_LSB 25
#define TCPC_REG_VBUS_VOLTAGE_VBUS(x)                                                              \
        (TCPC_REG_VBUS_VOLTAGE_SCALE(x) * TCPC_REG_VBUS_VOLTAGE_MEASUREMENT(x) *                   \
         TCPC_REG_VBUS_VOLTAGE_LSB)

#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH         0x72
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_LSB     25
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_MASK    GENMASK(11, 0)
#define TCPC_REG_VBUS_SINK_DISCONNECT_THRESH_DEFAULT 0x008C /* 3.5 V */

#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH         0x74
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_LSB     25
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_MASK    GENMASK(11, 0)
#define TCPC_REG_VBUS_STOP_DISCHARGE_THRESH_DEFAULT 0x0020 /* 0.8 V */

#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG      0x76
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_LSB  25
#define TCPC_REG_VBUS_VOLTAGE_ALARM_HI_CFG_MASK GENMASK(11, 0)

#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG      0x78
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_LSB  25
#define TCPC_REG_VBUS_VOLTAGE_ALARM_LO_CFG_MASK GENMASK(11, 0)

#define TCPC_REG_VBUS_NONDEFAULT_TARGET     0x7a
#define TCPC_REG_VBUS_NONDEFAULT_TARGET_LSB 20

#define TCPC_REG_DEV_CAP_3               0x7c
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK GENMASK(2, 0)
#define TCPC_REG_DEV_CAP_3_VBUS_MAX(reg) ((reg) & TCPC_REG_DEV_CAP_3_VBUS_MAX_MASK)
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_5V   0
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_9V   1
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_15V  2
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_20V  3
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_28V  4
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_36V  5
#define TCPC_REG_DEV_CAP_3_VBUS_MAX_48V  6

#endif /* ZEPHYR_INCLUDE_USB_C_TCPCI_H_ */
```

## 112.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 715 行

3.5 V。

### 注释 3：原第 729 行

0.8 V。

### 注释 4：原第 791 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_C_TCPCI_H_`。

## 112.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tcpci_8h.html)

---

[上一章](P111_stm32g0_b1x_c1x_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P113_test_asm_inline_gcc.h_源码浏览.md)
