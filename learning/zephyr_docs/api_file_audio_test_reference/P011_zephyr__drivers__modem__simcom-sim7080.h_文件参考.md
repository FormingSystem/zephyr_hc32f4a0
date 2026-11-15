---
id: learning.zephyr-docs.api-file-audio-test-reference.page-11
title: zephyr__drivers__modem__simcom-sim7080.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_modem\_\_simcom-sim7080.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Simcom SIM7080调制解调器（Modem）的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stdbool.h>
#include <stdint.h>
#include <time.h>
```

查看此文件的源码。

芯讯通 SIM7080 调制解调器（Simcom SIM7080 Modem）公共 API 头文件。Copyright (C) 2021 metraTec GmbH SPDX-License-Identifier: Apache-2.0

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_sim7080_5Fgnss_5Fdata"></a>

```c
struct sim7080_gnss_data
```

相关声明：[sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)。

Sim7080全球导航卫星系统（GNSS）的数据结构。

<a id="r_sim7080_5Fsms"></a>

```c
struct sim7080_sms
```

相关声明：[sim7080_sms](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md)。

短消息（SMS）的缓冲区结构。

<a id="r_sim7080_5Fsms_5Fbuffer"></a>

```c
struct sim7080_sms_buffer
```

相关声明：[sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)。

短消息（SMS）读取操作的缓冲区结构。

<a id="r_sim7080_5Fue_5Fsys_5Finfo_5Fgsm"></a>

```c
struct sim7080_ue_sys_info_gsm
```

相关声明：[sim7080_ue_sys_info_gsm](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md)。

Sim7080用户设备（UE）的GSM系统信息结构。

<a id="r_sim7080_5Fue_5Fsys_5Finfo_5Flte"></a>

```c
struct sim7080_ue_sys_info_lte
```

相关声明：[sim7080_ue_sys_info_lte](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md)。

Sim7080用户设备（UE）的LTE系统信息结构。

<a id="r_sim7080_5Fue_5Fsys_5Finfo"></a>

```c
struct sim7080_ue_sys_info
```

相关声明：[sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)。

Sim7080用户设备（UE）的系统信息结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gace6ac2be37e58af15aeda674923c8201"></a>

```c
#define SIM7080_GNSS_DATA_UTC_LEN 20
```

相关声明：[SIM7080_GNSS_DATA_UTC_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gace6ac2be37e58af15aeda674923c8201)。

全球导航卫星系统（GNSS）协调世界时（UTC）数据的最大长度。

<a id="r_gab64ab50adf37f68e036db2901dd839a7"></a>

```c
#define SIM7080_SMS_MAX_LEN 160
```

相关声明：[SIM7080_SMS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gab64ab50adf37f68e036db2901dd839a7)。

短信最大长度（Maximum SMS Length）。

<a id="r_ga43d7e807a3f3a51a63ad86055d8d7af2"></a>

```c
#define SIM7080_UE_SYS_INFO_BAND_SIZE 32
```

相关声明：[SIM7080_UE_SYS_INFO_BAND_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga43d7e807a3f3a51a63ad86055d8d7af2)。

用户设备系统信息频段字段的最大大小（Maximum UE System Information Band Size）。

<a id="r_ga2dcf6cd30aa9b07c331ec742d730e8ad"></a>

```c
#define SIM7080_DNS_MAX_RECOUNT 10
```

相关声明：[SIM7080_DNS_MAX_RECOUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga2dcf6cd30aa9b07c331ec742d730e8ad)。

域名系统（DNS）的最大重试次数。

<a id="r_ga9779d47638672294335d8024ddac9b7c"></a>

```c
#define SIM7080_DNS_MAX_TIMEOUT_MS 60000
```

相关声明：[SIM7080_DNS_MAX_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga9779d47638672294335d8024ddac9b7c)。

DNS 查询的最大超时（Maximum Timeout），单位为毫秒。

<a id="r_ga57f77bbd01cddc0363b74b7ab457abda"></a>

```c
#define SIM7080_LTE_CHANNEL_MASK_NB1 0x7BEFFU
```

相关声明：[SIM7080_LTE_CHANNEL_MASK_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga57f77bbd01cddc0363b74b7ab457abda)。

窄带物联网（NB-IoT）信道掩码（Channel Mask）。

<a id="r_gac0abf584f86b5aafa913c1cd9f7287fc"></a>

```c
#define SIM7080_LTE_CHANNEL_MASK_M1 0x5FFFFU
```

相关声明：[SIM7080_LTE_CHANNEL_MASK_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gac0abf584f86b5aafa913c1cd9f7287fc)。

CAT-M1 信道掩码（Channel Mask）。

<a id="r_ga13010dfff50442f49737060838f906c0"></a>

```c
#define SIM7080_NUM_LTE_CHANNELS 19U
```

相关声明：[SIM7080_NUM_LTE_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga13010dfff50442f49737060838f906c0)。

调制解调器支持的 LTE 信道数量（Number of Channels）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ga5d90415d319a9939f03752ff38a7c25a"></a>

```c
enum sim7080_state { SIM7080_STATE_INIT = 0 , SIM7080_STATE_IDLE , SIM7080_STATE_NETWORKING , SIM7080_STATE_GNSS , SIM7080_STATE_OFF }
```

相关声明：[sim7080_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga5d90415d319a9939f03752ff38a7c25a)、[SIM7080_STATE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c)、[SIM7080_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a)、[SIM7080_STATE_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8)、[SIM7080_STATE_GNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0)、[SIM7080_STATE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b)。

SIM7080 调制解调器状态（Modem State）。

<a id="r_ga02721f95826487567017ebf780dff635"></a>

```c
enum sim7080_rat { SIM7080_RAT_LTE_NB1 , SIM7080_RAT_LTE_M1 , SIM7080_RAT_LTE_AUTO , SIM7080_RAT_GSM }
```

相关声明：[sim7080_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga02721f95826487567017ebf780dff635)、[SIM7080_RAT_LTE_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671)、[SIM7080_RAT_LTE_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6)、[SIM7080_RAT_LTE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36)、[SIM7080_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3)。

调制解调器无线接入技术（Radio Access Technology）。

<a id="r_gafefcd23a6ce4c292b1cfc2bbcfa98784"></a>

```c
enum sim7080_lte_chan { SIM7080_LTE_CHAN_B1 = BIT(0) , SIM7080_LTE_CHAN_B2 = BIT(1) , SIM7080_LTE_CHAN_B3 = BIT(2) , SIM7080_LTE_CHAN_B4 = BIT(3) , SIM7080_LTE_CHAN_B5 = BIT(4) , SIM7080_LTE_CHAN_B8 = BIT(5) , SIM7080_LTE_CHAN_B12 = BIT(6) , SIM7080_LTE_CHAN_B13 = BIT(7) , SIM7080_LTE_CHAN_B14 = BIT(8) , SIM7080_LTE_CHAN_B18 = BIT(9) , SIM7080_LTE_CHAN_B19 = BIT(10) , SIM7080_LTE_CHAN_B20 = BIT(11) , SIM7080_LTE_CHAN_B25 = BIT(12) , SIM7080_LTE_CHAN_B26 = BIT(13) , SIM7080_LTE_CHAN_B27 = BIT(14) , SIM7080_LTE_CHAN_B28 = BIT(15) , SIM7080_LTE_CHAN_B66 = BIT(16) , SIM7080_LTE_CHAN_B71 = BIT(17) , SIM7080_LTE_CHAN_B85 = BIT(18) }
```

相关声明：[sim7080_lte_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafefcd23a6ce4c292b1cfc2bbcfa98784)、[SIM7080_LTE_CHAN_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24)、[SIM7080_LTE_CHAN_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c)、[SIM7080_LTE_CHAN_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a)、[SIM7080_LTE_CHAN_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67)、[SIM7080_LTE_CHAN_B5](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9)、[SIM7080_LTE_CHAN_B8](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050)、[SIM7080_LTE_CHAN_B12](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c)、[SIM7080_LTE_CHAN_B13](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a)、[SIM7080_LTE_CHAN_B14](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e)、[SIM7080_LTE_CHAN_B18](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666)、[SIM7080_LTE_CHAN_B19](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e)、[SIM7080_LTE_CHAN_B20](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465)、[SIM7080_LTE_CHAN_B25](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0)、[SIM7080_LTE_CHAN_B26](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70)、[SIM7080_LTE_CHAN_B27](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528)、[SIM7080_LTE_CHAN_B28](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749)、[SIM7080_LTE_CHAN_B66](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e)、[SIM7080_LTE_CHAN_B71](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9)、[SIM7080_LTE_CHAN_B85](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831)。

支持的 LTE 信道（Channels）。

<a id="r_ga04f3c0bce4f7d2b35762dc92f0aa20eb"></a>

```c
enum sim7080_sms_stat { SIM7080_SMS_STAT_REC_UNREAD = 0 , SIM7080_SMS_STAT_REC_READ , SIM7080_SMS_STAT_STO_UNSENT , SIM7080_SMS_STAT_STO_SENT , SIM7080_SMS_STAT_ALL }
```

相关声明：[sim7080_sms_stat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga04f3c0bce4f7d2b35762dc92f0aa20eb)、[SIM7080_SMS_STAT_REC_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86)、[SIM7080_SMS_STAT_REC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165)、[SIM7080_SMS_STAT_STO_UNSENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669)、[SIM7080_SMS_STAT_STO_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5)、[SIM7080_SMS_STAT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)。

存储中的短信可能状态（SMS States）。

<a id="r_ga48afa6e777af6010488fbf726f467e63"></a>

```c
enum sim7080_ftp_rc { SIM7080_FTP_RC_OK = 0 , SIM7080_FTP_RC_FINISHED , SIM7080_FTP_RC_ERROR }
```

相关声明：[sim7080_ftp_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga48afa6e777af6010488fbf726f467e63)、[SIM7080_FTP_RC_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda)、[SIM7080_FTP_RC_FINISHED](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241)、[SIM7080_FTP_RC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce)。

可能的文件传输协议返回码（FTP Return Codes）。

<a id="r_ga25a5a23ca32dbd4bc7991274d3d1ce04"></a>

```c
enum sim7080_ue_sys_mode { SIM7080_UE_SYS_MODE_NO_SERVICE , SIM7080_UE_SYS_MODE_GSM , SIM7080_UE_SYS_MODE_LTE_CAT_M1 , SIM7080_UE_SYS_MODE_LTE_NB_IOT }
```

相关声明：[sim7080_ue_sys_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25a5a23ca32dbd4bc7991274d3d1ce04)、[SIM7080_UE_SYS_MODE_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c)、[SIM7080_UE_SYS_MODE_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14)、[SIM7080_UE_SYS_MODE_LTE_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2)、[SIM7080_UE_SYS_MODE_LTE_NB_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00)。

用户设备系统模式（UE System Mode）。

<a id="r_gaeda25db4347c7fcfbee69e8d6edace64"></a>

```c
enum sim7080_ue_op_mode { SIM7080_UE_OP_MODE_ONLINE , SIM7080_UE_OP_MODE_OFFLINE , SIM7080_UE_OP_MODE_FACTORY_TEST_MODE , SIM7080_UE_OP_MODE_RESET , SIM7080_UE_OP_MODE_LOW_POWER_MODE }
```

相关声明：[sim7080_ue_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaeda25db4347c7fcfbee69e8d6edace64)、[SIM7080_UE_OP_MODE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5)、[SIM7080_UE_OP_MODE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000)、[SIM7080_UE_OP_MODE_FACTORY_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c)、[SIM7080_UE_OP_MODE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff)、[SIM7080_UE_OP_MODE_LOW_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14)。

用户设备工作模式（UE Operating Mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_ga1e082cf652a5b34efdf50b30fe55f631"></a>

```c
enum sim7080_state mdm_sim7080_get_state (void)
```

相关声明：[sim7080_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga5d90415d319a9939f03752ff38a7c25a)、[mdm_sim7080_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga1e082cf652a5b34efdf50b30fe55f631)。

获取调制解调器当前状态（Modem State）。

<a id="r_ga93395c2713539db360cdcf0170075ea1"></a>

```c
int mdm_sim7080_power_on (void)
```

相关声明：[mdm_sim7080_power_on](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga93395c2713539db360cdcf0170075ea1)。

开启 SIM7080 电源（Power On）。

<a id="r_ga35c2b87170079e5700021969d01d7f8b"></a>

```c
int mdm_sim7080_power_off (void)
```

相关声明：[mdm_sim7080_power_off](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga35c2b87170079e5700021969d01d7f8b)。

关闭 SIM7080 电源（Power Off）。

<a id="r_ga454c0078f17532f8e77bb036f9c0d707"></a>

```c
void mdm_sim7080_force_reset (void)
```

相关声明：[mdm_sim7080_force_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga454c0078f17532f8e77bb036f9c0d707)。

通过将 pwrkey 拉动并保持 15 秒，强制复位调制解调器（Force Reset）。

<a id="r_gad857dd548490d40e6b9082c0b72e8d2b"></a>

```c
int mdm_sim7080_start_network (void)
```

相关声明：[mdm_sim7080_start_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad857dd548490d40e6b9082c0b72e8d2b)。

激活调制解调器的网络工作模式（Network Operation Mode）。

<a id="r_gaa07958866afaf9b9cc65517abf65d08c"></a>

```c
int mdm_sim7080_stop_network (void)
```

相关声明：[mdm_sim7080_stop_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa07958866afaf9b9cc65517abf65d08c)。

停止调制解调器的网络工作模式（Networking Operation Mode）。

<a id="r_ga6106a7d04282af2130471d26f6080ed4"></a>

```c
int mdm_sim7080_start_gnss (void)
```

相关声明：[mdm_sim7080_start_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6106a7d04282af2130471d26f6080ed4)。

以全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

<a id="r_ga7dc8062da9814bdee91b1e88092eee4b"></a>

```c
int mdm_sim7080_start_gnss_xtra (void)
```

相关声明：[mdm_sim7080_start_gnss_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga7dc8062da9814bdee91b1e88092eee4b)。

以带 XTRA 功能的全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

<a id="r_ga617c649ba2524884d8bf11c91bd2c492"></a>

```c
int mdm_sim7080_stop_gnss (void)
```

相关声明：[mdm_sim7080_stop_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga617c649ba2524884d8bf11c91bd2c492)。

停止调制解调器的 GNSS 工作模式（Operation Mode）。

<a id="r_gad84438b511f6fed71668273470294420"></a>

```c
int mdm_sim7080_download_xtra (uint8_t server_id, const char *f_name)
```

相关声明：[mdm_sim7080_download_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad84438b511f6fed71668273470294420)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

下载用于辅助 GNSS（Assisted GNSS）的 XTRA 文件。

<a id="r_ga25692018fd26087e093b666a5884726c"></a>

```c
int mdm_sim7080_query_xtra_validity (int16_t *diff_h, int16_t *duration_h, struct tm *inject)
```

相关声明：[mdm_sim7080_query_xtra_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25692018fd26087e093b666a5884726c)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

查询 XTRA 文件的有效性（Validity）。

<a id="r_gacce71e254dd7854052678319227c3f5b"></a>

```c
int mdm_sim7080_query_gnss (struct sim7080_gnss_data *data)
```

相关声明：[mdm_sim7080_query_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gacce71e254dd7854052678319227c3f5b)、[sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)。

从调制解调器查询 GNSS 位置（Position）。

<a id="r_ga79837aee512ae6f2fed52f3162e39868"></a>

```c
const char * mdm_sim7080_get_manufacturer (void)
```

相关声明：[mdm_sim7080_get_manufacturer](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga79837aee512ae6f2fed52f3162e39868)。

获取 SIM7080 的制造商（Manufacturer）。

<a id="r_ga557ec2729649fd92c5588f6dd0a04f15"></a>

```c
const char * mdm_sim7080_get_model (void)
```

相关声明：[mdm_sim7080_get_model](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga557ec2729649fd92c5588f6dd0a04f15)。

获取 SIM7080 的型号信息（Model Information）。

<a id="r_ga9759bf93bc2e8e15869858853a9499de"></a>

```c
const char * mdm_sim7080_get_revision (void)
```

相关声明：[mdm_sim7080_get_revision](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga9759bf93bc2e8e15869858853a9499de)。

获取 SIM7080 的修订版本（Revision）。

<a id="r_ga26d1291993cdcd44982c95bad2dd7b4f"></a>

```c
const char * mdm_sim7080_get_imei (void)
```

相关声明：[mdm_sim7080_get_imei](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga26d1291993cdcd44982c95bad2dd7b4f)。

获取 SIM7080 的国际移动设备识别码（IMEI）。

<a id="r_gad7e8d5c7cecb9b6150ad1148c81cf3ab"></a>

```c
const char * mdm_sim7080_get_iccid (void)
```

相关声明：[mdm_sim7080_get_iccid](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad7e8d5c7cecb9b6150ad1148c81cf3ab)。

获取 SIM7080 的集成电路卡识别码（ICCID）。

<a id="r_gaacf368bc85d27d49709bde170a0db2ec"></a>

```c
int mdm_sim7080_read_sms (struct sim7080_sms_buffer *buffer)
```

相关声明：[mdm_sim7080_read_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaacf368bc85d27d49709bde170a0db2ec)、[sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)。

从 SIM 模块读取短信（SMS）。

<a id="r_gae7137523b94c96d4816e4c19cb48313c"></a>

```c
int mdm_sim7080_delete_sms (uint16_t index)
```

相关声明：[mdm_sim7080_delete_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gae7137523b94c96d4816e4c19cb48313c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除给定索引处的短信（SMS）。

<a id="r_ga6cea6acdf6f02868a9f97c10b909a097"></a>

```c
int mdm_sim7080_set_gpio (int gpio, int level)
```

相关声明：[mdm_sim7080_set_gpio](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6cea6acdf6f02868a9f97c10b909a097)。

设置模块某个 GPIO 引脚的电平（Level）。

<a id="r_ga53a7c0d347cfacf0d7fadaf073fbff6c"></a>

```c
int mdm_sim7080_ftp_get_start (const char *server, const char *user, const char *passwd, const char *file, const char *path)
```

相关声明：[mdm_sim7080_ftp_get_start](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga53a7c0d347cfacf0d7fadaf073fbff6c)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)。

启动 FTP 下载会话（FTP Get Session）。

<a id="r_ga74f00c0b99f71f7340740fb199db58a5"></a>

```c
int mdm_sim7080_ftp_get_read (char *dst, size_t *size)
```

相关声明：[mdm_sim7080_ftp_get_read](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga74f00c0b99f71f7340740fb199db58a5)。

从 FTP 下载会话（FTP Get Session）读取数据。

<a id="r_ga313d94f1005e562f6646867813d97fb2"></a>

```c
int mdm_sim7080_get_battery_charge (uint8_t *bcs, uint8_t *bcl, uint16_t *voltage)
```

相关声明：[mdm_sim7080_get_battery_charge](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga313d94f1005e562f6646867813d97fb2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取电压（Voltage）、充电状态（Charge Status）及电池连接电平（Battery Connection Level）。

<a id="r_ga2895183848c33177c5b788e08382ba09"></a>

```c
int mdm_sim7080_get_ue_sys_info (struct sim7080_ue_sys_info *info)
```

相关声明：[mdm_sim7080_get_ue_sys_info](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga2895183848c33177c5b788e08382ba09)、[sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)。

读取用户设备系统信息（UE System Information）。

<a id="r_ga71b0423009ee53ea6d2f4497820e775c"></a>

```c
int mdm_sim7080_get_local_time (struct tm *t)
```

相关声明：[mdm_sim7080_get_local_time](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga71b0423009ee53ea6d2f4497820e775c)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取调制解调器的本地时间（Local Time）。

<a id="r_ga017a7dc143628ff5ff5646c7be6d4579"></a>

```c
int mdm_sim7080_dns_set_lookup_params (uint8_t recount, uint16_t timeout)
```

相关声明：[mdm_sim7080_dns_set_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga017a7dc143628ff5ff5646c7be6d4579)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 DNS 查询参数（Query Lookup Parameters）。

<a id="r_ga83acdbbe8cde8d73eec066f7e6829941"></a>

```c
void mdm_sim7080_dns_get_lookup_params (uint8_t *recount, uint16_t *timeout)
```

相关声明：[mdm_sim7080_dns_get_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga83acdbbe8cde8d73eec066f7e6829941)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 DNS 查询参数（Query Lookup Parameters）。

<a id="r_gafe348fd71a838e6d3628e4025e859ba6"></a>

```c
void mdm_sim7080_get_rat (enum sim7080_rat *rat)
```

相关声明：[mdm_sim7080_get_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafe348fd71a838e6d3628e4025e859ba6)、[sim7080_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga02721f95826487567017ebf780dff635)。

获取当前选定的无线技术（Radio Technology）。

<a id="r_gaa33f561bff0c1a0c8fe484ae226fe421"></a>

```c
int mdm_sim7080_set_rat (enum sim7080_rat rat)
```

相关声明：[mdm_sim7080_set_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa33f561bff0c1a0c8fe484ae226fe421)、[sim7080_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga02721f95826487567017ebf780dff635)。

设置无线技术（Radio Technology）。

<a id="r_ga810526ebd0e2bec22c1dac87b5425d5d"></a>

```c
void mdm_sim7080_get_lte_bands (uint32_t *nb1, uint32_t *m1)
```

相关声明：[mdm_sim7080_get_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga810526ebd0e2bec22c1dac87b5425d5d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取当前使用的 LTE 频段（Bands）。

<a id="r_ga4a4fbc695dc92fdf57cb7faf1f104f42"></a>

```c
int mdm_sim7080_set_lte_bands (uint32_t nb1, uint32_t m1)
```

相关声明：[mdm_sim7080_set_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga4a4fbc695dc92fdf57cb7faf1f104f42)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置要使用的 LTE 频段（Bands）。


## 11.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P786_simcom-sim7080.h_源码浏览.md)
- [sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)
- [sim7080_sms](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md)
- [sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)
- [sim7080_ue_sys_info_gsm](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md)
- [sim7080_ue_sys_info_lte](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md)
- [sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)
- [SIM7080_GNSS_DATA_UTC_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gace6ac2be37e58af15aeda674923c8201)
- [SIM7080_SMS_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gab64ab50adf37f68e036db2901dd839a7)
- [SIM7080_UE_SYS_INFO_BAND_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga43d7e807a3f3a51a63ad86055d8d7af2)
- [SIM7080_DNS_MAX_RECOUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga2dcf6cd30aa9b07c331ec742d730e8ad)
- [SIM7080_DNS_MAX_TIMEOUT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga9779d47638672294335d8024ddac9b7c)
- [SIM7080_LTE_CHANNEL_MASK_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga57f77bbd01cddc0363b74b7ab457abda)
- [SIM7080_LTE_CHANNEL_MASK_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gac0abf584f86b5aafa913c1cd9f7287fc)
- [SIM7080_NUM_LTE_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga13010dfff50442f49737060838f906c0)
- [sim7080_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga5d90415d319a9939f03752ff38a7c25a)
- [SIM7080_STATE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c)
- [SIM7080_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a)
- [SIM7080_STATE_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8)
- [SIM7080_STATE_GNSS](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0)
- [SIM7080_STATE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b)
- [sim7080_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga02721f95826487567017ebf780dff635)
- [SIM7080_RAT_LTE_NB1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671)
- [SIM7080_RAT_LTE_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6)
- [SIM7080_RAT_LTE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36)
- [SIM7080_RAT_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3)
- [sim7080_lte_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafefcd23a6ce4c292b1cfc2bbcfa98784)
- [SIM7080_LTE_CHAN_B1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24)
- [SIM7080_LTE_CHAN_B2](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c)
- [SIM7080_LTE_CHAN_B3](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a)
- [SIM7080_LTE_CHAN_B4](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67)
- [SIM7080_LTE_CHAN_B5](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9)
- [SIM7080_LTE_CHAN_B8](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050)
- [SIM7080_LTE_CHAN_B12](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c)
- [SIM7080_LTE_CHAN_B13](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a)
- [SIM7080_LTE_CHAN_B14](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e)
- [SIM7080_LTE_CHAN_B18](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666)
- [SIM7080_LTE_CHAN_B19](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e)
- [SIM7080_LTE_CHAN_B20](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465)
- [SIM7080_LTE_CHAN_B25](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0)
- [SIM7080_LTE_CHAN_B26](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70)
- [SIM7080_LTE_CHAN_B27](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528)
- [SIM7080_LTE_CHAN_B28](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749)
- [SIM7080_LTE_CHAN_B66](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e)
- [SIM7080_LTE_CHAN_B71](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9)
- [SIM7080_LTE_CHAN_B85](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831)
- [sim7080_sms_stat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga04f3c0bce4f7d2b35762dc92f0aa20eb)
- [SIM7080_SMS_STAT_REC_UNREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86)
- [SIM7080_SMS_STAT_REC_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165)
- [SIM7080_SMS_STAT_STO_UNSENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669)
- [SIM7080_SMS_STAT_STO_SENT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5)
- [SIM7080_SMS_STAT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)
- [sim7080_ftp_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga48afa6e777af6010488fbf726f467e63)
- [SIM7080_FTP_RC_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda)
- [SIM7080_FTP_RC_FINISHED](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241)
- [SIM7080_FTP_RC_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce)
- [sim7080_ue_sys_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25a5a23ca32dbd4bc7991274d3d1ce04)
- [SIM7080_UE_SYS_MODE_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c)
- [SIM7080_UE_SYS_MODE_GSM](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14)
- [SIM7080_UE_SYS_MODE_LTE_CAT_M1](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2)
- [SIM7080_UE_SYS_MODE_LTE_NB_IOT](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00)
- [sim7080_ue_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaeda25db4347c7fcfbee69e8d6edace64)
- [SIM7080_UE_OP_MODE_ONLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5)
- [SIM7080_UE_OP_MODE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000)
- [SIM7080_UE_OP_MODE_FACTORY_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c)
- [SIM7080_UE_OP_MODE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff)
- [SIM7080_UE_OP_MODE_LOW_POWER_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14)
- [mdm_sim7080_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga1e082cf652a5b34efdf50b30fe55f631)
- [mdm_sim7080_power_on](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga93395c2713539db360cdcf0170075ea1)
- [mdm_sim7080_power_off](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga35c2b87170079e5700021969d01d7f8b)
- [mdm_sim7080_force_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga454c0078f17532f8e77bb036f9c0d707)
- [mdm_sim7080_start_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad857dd548490d40e6b9082c0b72e8d2b)
- [mdm_sim7080_stop_network](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa07958866afaf9b9cc65517abf65d08c)
- [mdm_sim7080_start_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6106a7d04282af2130471d26f6080ed4)
- [mdm_sim7080_start_gnss_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga7dc8062da9814bdee91b1e88092eee4b)
- [mdm_sim7080_stop_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga617c649ba2524884d8bf11c91bd2c492)
- [mdm_sim7080_download_xtra](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad84438b511f6fed71668273470294420)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mdm_sim7080_query_xtra_validity](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25692018fd26087e093b666a5884726c)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [mdm_sim7080_query_gnss](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gacce71e254dd7854052678319227c3f5b)
- [mdm_sim7080_get_manufacturer](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga79837aee512ae6f2fed52f3162e39868)
- [mdm_sim7080_get_model](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga557ec2729649fd92c5588f6dd0a04f15)
- [mdm_sim7080_get_revision](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga9759bf93bc2e8e15869858853a9499de)
- [mdm_sim7080_get_imei](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga26d1291993cdcd44982c95bad2dd7b4f)
- [mdm_sim7080_get_iccid](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gad7e8d5c7cecb9b6150ad1148c81cf3ab)
- [mdm_sim7080_read_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaacf368bc85d27d49709bde170a0db2ec)
- [mdm_sim7080_delete_sms](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gae7137523b94c96d4816e4c19cb48313c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mdm_sim7080_set_gpio](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga6cea6acdf6f02868a9f97c10b909a097)
- [mdm_sim7080_ftp_get_start](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga53a7c0d347cfacf0d7fadaf073fbff6c)
- [passwd](../posix_system_model_reference/P009_passwd_结构体.md)
- [mdm_sim7080_ftp_get_read](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga74f00c0b99f71f7340740fb199db58a5)
- [mdm_sim7080_get_battery_charge](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga313d94f1005e562f6646867813d97fb2)
- [mdm_sim7080_get_ue_sys_info](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga2895183848c33177c5b788e08382ba09)
- [mdm_sim7080_get_local_time](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga71b0423009ee53ea6d2f4497820e775c)
- [mdm_sim7080_dns_set_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga017a7dc143628ff5ff5646c7be6d4579)
- [mdm_sim7080_dns_get_lookup_params](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga83acdbbe8cde8d73eec066f7e6829941)
- [mdm_sim7080_get_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gafe348fd71a838e6d3628e4025e859ba6)
- [mdm_sim7080_set_rat](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaa33f561bff0c1a0c8fe484ae226fe421)
- [mdm_sim7080_get_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga810526ebd0e2bec22c1dac87b5425d5d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mdm_sim7080_set_lte_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga4a4fbc695dc92fdf57cb7faf1f104f42)

<a id="header-details"></a>

---

[上一章](P010_zephyr__dt-bindings__clock__mcux_lpc_syscon_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__dt-bindings__clock__syna_sr100_clock.h_文件参考.md)
