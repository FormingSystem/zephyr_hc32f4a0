---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-15
title: SIMCom SIM7080 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_SIMCom SIM7080 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SIMCom SIM7080 蜂窝调制解调器（Cellular modems）。

<a id="details"></a>

SIMCom SIM7080 蜂窝调制解调器（Cellular modems）。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_simcom-sim7080_2Eh"></a>

```c
file simcom-sim7080.h
```

相关声明：[simcom-sim7080.h](../api_file_audio_test_reference/P011_zephyr__drivers__modem__simcom-sim7080.h_文件参考.md)。

Simcom SIM7080调制解调器（Modem）的公共API头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.2\_数据结构（Data Structures）

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

## 15.3\_宏定义（Macros）

<a id="r_gace6ac2be37e58af15aeda674923c8201"></a>

```c
#define SIM7080_GNSS_DATA_UTC_LEN 20
```

相关声明：[SIM7080_GNSS_DATA_UTC_LEN](#gace6ac2be37e58af15aeda674923c8201)。

全球导航卫星系统（GNSS）协调世界时（UTC）数据的最大长度。

<a id="r_gab64ab50adf37f68e036db2901dd839a7"></a>

```c
#define SIM7080_SMS_MAX_LEN 160
```

相关声明：[SIM7080_SMS_MAX_LEN](#gab64ab50adf37f68e036db2901dd839a7)。

短信最大长度（Maximum SMS Length）。

<a id="r_ga43d7e807a3f3a51a63ad86055d8d7af2"></a>

```c
#define SIM7080_UE_SYS_INFO_BAND_SIZE 32
```

相关声明：[SIM7080_UE_SYS_INFO_BAND_SIZE](#ga43d7e807a3f3a51a63ad86055d8d7af2)。

用户设备系统信息频段字段的最大大小（Maximum UE System Information Band Size）。

<a id="r_ga2dcf6cd30aa9b07c331ec742d730e8ad"></a>

```c
#define SIM7080_DNS_MAX_RECOUNT 10
```

相关声明：[SIM7080_DNS_MAX_RECOUNT](#ga2dcf6cd30aa9b07c331ec742d730e8ad)。

域名系统（DNS）的最大重试次数。

<a id="r_ga9779d47638672294335d8024ddac9b7c"></a>

```c
#define SIM7080_DNS_MAX_TIMEOUT_MS 60000
```

相关声明：[SIM7080_DNS_MAX_TIMEOUT_MS](#ga9779d47638672294335d8024ddac9b7c)。

DNS 查询的最大超时（Maximum Timeout），单位为毫秒。

<a id="r_ga57f77bbd01cddc0363b74b7ab457abda"></a>

```c
#define SIM7080_LTE_CHANNEL_MASK_NB1 0x7BEFFU
```

相关声明：[SIM7080_LTE_CHANNEL_MASK_NB1](#ga57f77bbd01cddc0363b74b7ab457abda)。

窄带物联网（NB-IoT）信道掩码（Channel Mask）。

<a id="r_gac0abf584f86b5aafa913c1cd9f7287fc"></a>

```c
#define SIM7080_LTE_CHANNEL_MASK_M1 0x5FFFFU
```

相关声明：[SIM7080_LTE_CHANNEL_MASK_M1](#gac0abf584f86b5aafa913c1cd9f7287fc)。

CAT-M1 信道掩码（Channel Mask）。

<a id="r_ga13010dfff50442f49737060838f906c0"></a>

```c
#define SIM7080_NUM_LTE_CHANNELS 19U
```

相关声明：[SIM7080_NUM_LTE_CHANNELS](#ga13010dfff50442f49737060838f906c0)。

调制解调器支持的 LTE 信道数量（Number of Channels）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_ga5d90415d319a9939f03752ff38a7c25a"></a>

```c
enum sim7080_state { SIM7080_STATE_INIT = 0 , SIM7080_STATE_IDLE , SIM7080_STATE_NETWORKING , SIM7080_STATE_GNSS , SIM7080_STATE_OFF }
```

相关声明：[sim7080_state](#ga5d90415d319a9939f03752ff38a7c25a)、[SIM7080_STATE_INIT](#gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c)、[SIM7080_STATE_IDLE](#gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a)、[SIM7080_STATE_NETWORKING](#gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8)、[SIM7080_STATE_GNSS](#gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0)、[SIM7080_STATE_OFF](#gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b)。

SIM7080 调制解调器状态（Modem State）。

<a id="r_ga02721f95826487567017ebf780dff635"></a>

```c
enum sim7080_rat { SIM7080_RAT_LTE_NB1 , SIM7080_RAT_LTE_M1 , SIM7080_RAT_LTE_AUTO , SIM7080_RAT_GSM }
```

相关声明：[sim7080_rat](#ga02721f95826487567017ebf780dff635)、[SIM7080_RAT_LTE_NB1](#gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671)、[SIM7080_RAT_LTE_M1](#gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6)、[SIM7080_RAT_LTE_AUTO](#gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36)、[SIM7080_RAT_GSM](#gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3)。

调制解调器无线接入技术（Radio Access Technology）。

<a id="r_gafefcd23a6ce4c292b1cfc2bbcfa98784"></a>

```c
enum sim7080_lte_chan { SIM7080_LTE_CHAN_B1 = BIT(0) , SIM7080_LTE_CHAN_B2 = BIT(1) , SIM7080_LTE_CHAN_B3 = BIT(2) , SIM7080_LTE_CHAN_B4 = BIT(3) , SIM7080_LTE_CHAN_B5 = BIT(4) , SIM7080_LTE_CHAN_B8 = BIT(5) , SIM7080_LTE_CHAN_B12 = BIT(6) , SIM7080_LTE_CHAN_B13 = BIT(7) , SIM7080_LTE_CHAN_B14 = BIT(8) , SIM7080_LTE_CHAN_B18 = BIT(9) , SIM7080_LTE_CHAN_B19 = BIT(10) , SIM7080_LTE_CHAN_B20 = BIT(11) , SIM7080_LTE_CHAN_B25 = BIT(12) , SIM7080_LTE_CHAN_B26 = BIT(13) , SIM7080_LTE_CHAN_B27 = BIT(14) , SIM7080_LTE_CHAN_B28 = BIT(15) , SIM7080_LTE_CHAN_B66 = BIT(16) , SIM7080_LTE_CHAN_B71 = BIT(17) , SIM7080_LTE_CHAN_B85 = BIT(18) }
```

相关声明：[sim7080_lte_chan](#gafefcd23a6ce4c292b1cfc2bbcfa98784)、[SIM7080_LTE_CHAN_B1](#ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24)、[SIM7080_LTE_CHAN_B2](#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c)、[SIM7080_LTE_CHAN_B3](#ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a)、[SIM7080_LTE_CHAN_B4](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67)、[SIM7080_LTE_CHAN_B5](#ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9)、[SIM7080_LTE_CHAN_B8](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050)、[SIM7080_LTE_CHAN_B12](#ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c)、[SIM7080_LTE_CHAN_B13](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a)、[SIM7080_LTE_CHAN_B14](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e)、[SIM7080_LTE_CHAN_B18](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666)、[SIM7080_LTE_CHAN_B19](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e)、[SIM7080_LTE_CHAN_B20](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465)、[SIM7080_LTE_CHAN_B25](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0)、[SIM7080_LTE_CHAN_B26](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70)、[SIM7080_LTE_CHAN_B27](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528)、[SIM7080_LTE_CHAN_B28](#ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749)、[SIM7080_LTE_CHAN_B66](#ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e)、[SIM7080_LTE_CHAN_B71](#ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9)、[SIM7080_LTE_CHAN_B85](#ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831)。

支持的 LTE 信道（Channels）。

<a id="r_ga04f3c0bce4f7d2b35762dc92f0aa20eb"></a>

```c
enum sim7080_sms_stat { SIM7080_SMS_STAT_REC_UNREAD = 0 , SIM7080_SMS_STAT_REC_READ , SIM7080_SMS_STAT_STO_UNSENT , SIM7080_SMS_STAT_STO_SENT , SIM7080_SMS_STAT_ALL }
```

相关声明：[sim7080_sms_stat](#ga04f3c0bce4f7d2b35762dc92f0aa20eb)、[SIM7080_SMS_STAT_REC_UNREAD](#gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86)、[SIM7080_SMS_STAT_REC_READ](#gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165)、[SIM7080_SMS_STAT_STO_UNSENT](#gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669)、[SIM7080_SMS_STAT_STO_SENT](#gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5)、[SIM7080_SMS_STAT_ALL](#gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35)。

存储中的短信可能状态（SMS States）。

<a id="r_ga48afa6e777af6010488fbf726f467e63"></a>

```c
enum sim7080_ftp_rc { SIM7080_FTP_RC_OK = 0 , SIM7080_FTP_RC_FINISHED , SIM7080_FTP_RC_ERROR }
```

相关声明：[sim7080_ftp_rc](#ga48afa6e777af6010488fbf726f467e63)、[SIM7080_FTP_RC_OK](#gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda)、[SIM7080_FTP_RC_FINISHED](#gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241)、[SIM7080_FTP_RC_ERROR](#gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce)。

可能的文件传输协议返回码（FTP Return Codes）。

<a id="r_ga25a5a23ca32dbd4bc7991274d3d1ce04"></a>

```c
enum sim7080_ue_sys_mode { SIM7080_UE_SYS_MODE_NO_SERVICE , SIM7080_UE_SYS_MODE_GSM , SIM7080_UE_SYS_MODE_LTE_CAT_M1 , SIM7080_UE_SYS_MODE_LTE_NB_IOT }
```

相关声明：[sim7080_ue_sys_mode](#ga25a5a23ca32dbd4bc7991274d3d1ce04)、[SIM7080_UE_SYS_MODE_NO_SERVICE](#gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c)、[SIM7080_UE_SYS_MODE_GSM](#gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14)、[SIM7080_UE_SYS_MODE_LTE_CAT_M1](#gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2)、[SIM7080_UE_SYS_MODE_LTE_NB_IOT](#gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00)。

用户设备系统模式（UE System Mode）。

<a id="r_gaeda25db4347c7fcfbee69e8d6edace64"></a>

```c
enum sim7080_ue_op_mode { SIM7080_UE_OP_MODE_ONLINE , SIM7080_UE_OP_MODE_OFFLINE , SIM7080_UE_OP_MODE_FACTORY_TEST_MODE , SIM7080_UE_OP_MODE_RESET , SIM7080_UE_OP_MODE_LOW_POWER_MODE }
```

相关声明：[sim7080_ue_op_mode](#gaeda25db4347c7fcfbee69e8d6edace64)、[SIM7080_UE_OP_MODE_ONLINE](#ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5)、[SIM7080_UE_OP_MODE_OFFLINE](#ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000)、[SIM7080_UE_OP_MODE_FACTORY_TEST_MODE](#ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c)、[SIM7080_UE_OP_MODE_RESET](#ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff)、[SIM7080_UE_OP_MODE_LOW_POWER_MODE](#ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14)。

用户设备工作模式（UE Operating Mode）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_ga1e082cf652a5b34efdf50b30fe55f631"></a>

```c
enum sim7080_state mdm_sim7080_get_state (void)
```

相关声明：[sim7080_state](#ga5d90415d319a9939f03752ff38a7c25a)、[mdm_sim7080_get_state](#ga1e082cf652a5b34efdf50b30fe55f631)。

获取调制解调器当前状态（Modem State）。

<a id="r_ga93395c2713539db360cdcf0170075ea1"></a>

```c
int mdm_sim7080_power_on (void)
```

相关声明：[mdm_sim7080_power_on](#ga93395c2713539db360cdcf0170075ea1)。

开启 SIM7080 电源（Power On）。

<a id="r_ga35c2b87170079e5700021969d01d7f8b"></a>

```c
int mdm_sim7080_power_off (void)
```

相关声明：[mdm_sim7080_power_off](#ga35c2b87170079e5700021969d01d7f8b)。

关闭 SIM7080 电源（Power Off）。

<a id="r_ga454c0078f17532f8e77bb036f9c0d707"></a>

```c
void mdm_sim7080_force_reset (void)
```

相关声明：[mdm_sim7080_force_reset](#ga454c0078f17532f8e77bb036f9c0d707)。

通过将 pwrkey 拉动并保持 15 秒，强制复位调制解调器（Force Reset）。

<a id="r_gad857dd548490d40e6b9082c0b72e8d2b"></a>

```c
int mdm_sim7080_start_network (void)
```

相关声明：[mdm_sim7080_start_network](#gad857dd548490d40e6b9082c0b72e8d2b)。

激活调制解调器的网络工作模式（Network Operation Mode）。

<a id="r_gaa07958866afaf9b9cc65517abf65d08c"></a>

```c
int mdm_sim7080_stop_network (void)
```

相关声明：[mdm_sim7080_stop_network](#gaa07958866afaf9b9cc65517abf65d08c)。

停止调制解调器的网络工作模式（Networking Operation Mode）。

<a id="r_ga6106a7d04282af2130471d26f6080ed4"></a>

```c
int mdm_sim7080_start_gnss (void)
```

相关声明：[mdm_sim7080_start_gnss](#ga6106a7d04282af2130471d26f6080ed4)。

以全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

<a id="r_ga7dc8062da9814bdee91b1e88092eee4b"></a>

```c
int mdm_sim7080_start_gnss_xtra (void)
```

相关声明：[mdm_sim7080_start_gnss_xtra](#ga7dc8062da9814bdee91b1e88092eee4b)。

以带 XTRA 功能的全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

<a id="r_ga617c649ba2524884d8bf11c91bd2c492"></a>

```c
int mdm_sim7080_stop_gnss (void)
```

相关声明：[mdm_sim7080_stop_gnss](#ga617c649ba2524884d8bf11c91bd2c492)。

停止调制解调器的 GNSS 工作模式（Operation Mode）。

<a id="r_gad84438b511f6fed71668273470294420"></a>

```c
int mdm_sim7080_download_xtra (uint8_t server_id, const char *f_name)
```

相关声明：[mdm_sim7080_download_xtra](#gad84438b511f6fed71668273470294420)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

下载用于辅助 GNSS（Assisted GNSS）的 XTRA 文件。

<a id="r_ga25692018fd26087e093b666a5884726c"></a>

```c
int mdm_sim7080_query_xtra_validity (int16_t *diff_h, int16_t *duration_h, struct tm *inject)
```

相关声明：[mdm_sim7080_query_xtra_validity](#ga25692018fd26087e093b666a5884726c)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

查询 XTRA 文件的有效性（Validity）。

<a id="r_gacce71e254dd7854052678319227c3f5b"></a>

```c
int mdm_sim7080_query_gnss (struct sim7080_gnss_data *data)
```

相关声明：[mdm_sim7080_query_gnss](#gacce71e254dd7854052678319227c3f5b)、[sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)。

从调制解调器查询 GNSS 位置（Position）。

<a id="r_ga79837aee512ae6f2fed52f3162e39868"></a>

```c
const char * mdm_sim7080_get_manufacturer (void)
```

相关声明：[mdm_sim7080_get_manufacturer](#ga79837aee512ae6f2fed52f3162e39868)。

获取 SIM7080 的制造商（Manufacturer）。

<a id="r_ga557ec2729649fd92c5588f6dd0a04f15"></a>

```c
const char * mdm_sim7080_get_model (void)
```

相关声明：[mdm_sim7080_get_model](#ga557ec2729649fd92c5588f6dd0a04f15)。

获取 SIM7080 的型号信息（Model Information）。

<a id="r_ga9759bf93bc2e8e15869858853a9499de"></a>

```c
const char * mdm_sim7080_get_revision (void)
```

相关声明：[mdm_sim7080_get_revision](#ga9759bf93bc2e8e15869858853a9499de)。

获取 SIM7080 的修订版本（Revision）。

<a id="r_ga26d1291993cdcd44982c95bad2dd7b4f"></a>

```c
const char * mdm_sim7080_get_imei (void)
```

相关声明：[mdm_sim7080_get_imei](#ga26d1291993cdcd44982c95bad2dd7b4f)。

获取 SIM7080 的国际移动设备识别码（IMEI）。

<a id="r_gad7e8d5c7cecb9b6150ad1148c81cf3ab"></a>

```c
const char * mdm_sim7080_get_iccid (void)
```

相关声明：[mdm_sim7080_get_iccid](#gad7e8d5c7cecb9b6150ad1148c81cf3ab)。

获取 SIM7080 的集成电路卡识别码（ICCID）。

<a id="r_gaacf368bc85d27d49709bde170a0db2ec"></a>

```c
int mdm_sim7080_read_sms (struct sim7080_sms_buffer *buffer)
```

相关声明：[mdm_sim7080_read_sms](#gaacf368bc85d27d49709bde170a0db2ec)、[sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)。

从 SIM 模块读取短信（SMS）。

<a id="r_gae7137523b94c96d4816e4c19cb48313c"></a>

```c
int mdm_sim7080_delete_sms (uint16_t index)
```

相关声明：[mdm_sim7080_delete_sms](#gae7137523b94c96d4816e4c19cb48313c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

删除给定索引处的短信（SMS）。

<a id="r_ga6cea6acdf6f02868a9f97c10b909a097"></a>

```c
int mdm_sim7080_set_gpio (int gpio, int level)
```

相关声明：[mdm_sim7080_set_gpio](#ga6cea6acdf6f02868a9f97c10b909a097)。

设置模块某个 GPIO 引脚的电平（Level）。

<a id="r_ga53a7c0d347cfacf0d7fadaf073fbff6c"></a>

```c
int mdm_sim7080_ftp_get_start (const char *server, const char *user, const char *passwd, const char *file, const char *path)
```

相关声明：[mdm_sim7080_ftp_get_start](#ga53a7c0d347cfacf0d7fadaf073fbff6c)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)。

启动 FTP 下载会话（FTP Get Session）。

<a id="r_ga74f00c0b99f71f7340740fb199db58a5"></a>

```c
int mdm_sim7080_ftp_get_read (char *dst, size_t *size)
```

相关声明：[mdm_sim7080_ftp_get_read](#ga74f00c0b99f71f7340740fb199db58a5)。

从 FTP 下载会话（FTP Get Session）读取数据。

<a id="r_ga313d94f1005e562f6646867813d97fb2"></a>

```c
int mdm_sim7080_get_battery_charge (uint8_t *bcs, uint8_t *bcl, uint16_t *voltage)
```

相关声明：[mdm_sim7080_get_battery_charge](#ga313d94f1005e562f6646867813d97fb2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取电压（Voltage）、充电状态（Charge Status）及电池连接电平（Battery Connection Level）。

<a id="r_ga2895183848c33177c5b788e08382ba09"></a>

```c
int mdm_sim7080_get_ue_sys_info (struct sim7080_ue_sys_info *info)
```

相关声明：[mdm_sim7080_get_ue_sys_info](#ga2895183848c33177c5b788e08382ba09)、[sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)。

读取用户设备系统信息（UE System Information）。

<a id="r_ga71b0423009ee53ea6d2f4497820e775c"></a>

```c
int mdm_sim7080_get_local_time (struct tm *t)
```

相关声明：[mdm_sim7080_get_local_time](#ga71b0423009ee53ea6d2f4497820e775c)、[tm](../posix_system_model_reference/P025_tm_结构体.md)。

获取调制解调器的本地时间（Local Time）。

<a id="r_ga017a7dc143628ff5ff5646c7be6d4579"></a>

```c
int mdm_sim7080_dns_set_lookup_params (uint8_t recount, uint16_t timeout)
```

相关声明：[mdm_sim7080_dns_set_lookup_params](#ga017a7dc143628ff5ff5646c7be6d4579)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 DNS 查询参数（Query Lookup Parameters）。

<a id="r_ga83acdbbe8cde8d73eec066f7e6829941"></a>

```c
void mdm_sim7080_dns_get_lookup_params (uint8_t *recount, uint16_t *timeout)
```

相关声明：[mdm_sim7080_dns_get_lookup_params](#ga83acdbbe8cde8d73eec066f7e6829941)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 DNS 查询参数（Query Lookup Parameters）。

<a id="r_gafe348fd71a838e6d3628e4025e859ba6"></a>

```c
void mdm_sim7080_get_rat (enum sim7080_rat *rat)
```

相关声明：[mdm_sim7080_get_rat](#gafe348fd71a838e6d3628e4025e859ba6)、[sim7080_rat](#ga02721f95826487567017ebf780dff635)。

获取当前选定的无线技术（Radio Technology）。

<a id="r_gaa33f561bff0c1a0c8fe484ae226fe421"></a>

```c
int mdm_sim7080_set_rat (enum sim7080_rat rat)
```

相关声明：[mdm_sim7080_set_rat](#gaa33f561bff0c1a0c8fe484ae226fe421)、[sim7080_rat](#ga02721f95826487567017ebf780dff635)。

设置无线技术（Radio Technology）。

<a id="r_ga810526ebd0e2bec22c1dac87b5425d5d"></a>

```c
void mdm_sim7080_get_lte_bands (uint32_t *nb1, uint32_t *m1)
```

相关声明：[mdm_sim7080_get_lte_bands](#ga810526ebd0e2bec22c1dac87b5425d5d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取当前使用的 LTE 频段（Bands）。

<a id="r_ga4a4fbc695dc92fdf57cb7faf1f104f42"></a>

```c
int mdm_sim7080_set_lte_bands (uint32_t nb1, uint32_t m1)
```

相关声明：[mdm_sim7080_set_lte_bands](#ga4a4fbc695dc92fdf57cb7faf1f104f42)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置要使用的 LTE 频段（Bands）。

## 15.6\_详细说明（Detailed Documentation）

<a id="ga2dcf6cd30aa9b07c331ec742d730e8ad"></a>

### `SIM7080_DNS_MAX_RECOUNT`

```c
#define SIM7080_DNS_MAX_RECOUNT 10
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

域名系统（DNS）的最大重试次数。

<a id="ga9779d47638672294335d8024ddac9b7c"></a>

### `SIM7080_DNS_MAX_TIMEOUT_MS`

```c
#define SIM7080_DNS_MAX_TIMEOUT_MS 60000
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

DNS 查询的最大超时（Maximum Timeout），单位为毫秒。

<a id="gace6ac2be37e58af15aeda674923c8201"></a>

### `SIM7080_GNSS_DATA_UTC_LEN`

```c
#define SIM7080_GNSS_DATA_UTC_LEN 20
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

全球导航卫星系统（GNSS）协调世界时（UTC）数据的最大长度。

<a id="gac0abf584f86b5aafa913c1cd9f7287fc"></a>

### `SIM7080_LTE_CHANNEL_MASK_M1`

```c
#define SIM7080_LTE_CHANNEL_MASK_M1 0x5FFFFU
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

CAT-M1 信道掩码（Channel Mask）。

<a id="ga57f77bbd01cddc0363b74b7ab457abda"></a>

### `SIM7080_LTE_CHANNEL_MASK_NB1`

```c
#define SIM7080_LTE_CHANNEL_MASK_NB1 0x7BEFFU
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

窄带物联网（NB-IoT）信道掩码（Channel Mask）。

<a id="ga13010dfff50442f49737060838f906c0"></a>

### `SIM7080_NUM_LTE_CHANNELS`

```c
#define SIM7080_NUM_LTE_CHANNELS 19U
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

调制解调器支持的 LTE 信道数量（Number of Channels）。

<a id="gab64ab50adf37f68e036db2901dd839a7"></a>

### `SIM7080_SMS_MAX_LEN`

```c
#define SIM7080_SMS_MAX_LEN 160
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

短信最大长度（Maximum SMS Length）。

<a id="ga43d7e807a3f3a51a63ad86055d8d7af2"></a>

### `SIM7080_UE_SYS_INFO_BAND_SIZE`

```c
#define SIM7080_UE_SYS_INFO_BAND_SIZE 32
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

用户设备系统信息频段字段的最大大小（Maximum UE System Information Band Size）。

<a id="ga48afa6e777af6010488fbf726f467e63"></a>

### `sim7080_ftp_rc`

```c
enum sim7080_ftp_rc
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

可能的文件传输协议返回码（FTP Return Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_FTP_RC_OK` | 操作正常完成（Operation Finished Correctly）。 |
| `SIM7080_FTP_RC_FINISHED` | 会话结束（Session Finished）。 |
| `SIM7080_FTP_RC_ERROR` | 发生错误（An Error Occurred）。 |

<a id="gafefcd23a6ce4c292b1cfc2bbcfa98784"></a>

### `sim7080_lte_chan`

```c
enum sim7080_lte_chan
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

支持的 LTE 信道（Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_LTE_CHAN_B1` | 长期演进（LTE）频段 1。 |
| `SIM7080_LTE_CHAN_B2` | 长期演进（LTE）频段 2。 |
| `SIM7080_LTE_CHAN_B3` | 长期演进（LTE）频段 3。 |
| `SIM7080_LTE_CHAN_B4` | 长期演进（LTE）频段 4。 |
| `SIM7080_LTE_CHAN_B5` | 长期演进（LTE）频段 5。 |
| `SIM7080_LTE_CHAN_B8` | 长期演进（LTE）频段 8。 |
| `SIM7080_LTE_CHAN_B12` | 长期演进（LTE）频段 12。 |
| `SIM7080_LTE_CHAN_B13` | 长期演进（LTE）频段 13。 |
| `SIM7080_LTE_CHAN_B14` | 长期演进（LTE）频段 14。 |
| `SIM7080_LTE_CHAN_B18` | 长期演进（LTE）频段 18。 |
| `SIM7080_LTE_CHAN_B19` | 长期演进（LTE）频段 19。 |
| `SIM7080_LTE_CHAN_B20` | 长期演进（LTE）频段 20。 |
| `SIM7080_LTE_CHAN_B25` | 长期演进（LTE）频段 25。 |
| `SIM7080_LTE_CHAN_B26` | 长期演进（LTE）频段 26。 |
| `SIM7080_LTE_CHAN_B27` | 长期演进（LTE）频段 27。 |
| `SIM7080_LTE_CHAN_B28` | 长期演进（LTE）频段 28。 |
| `SIM7080_LTE_CHAN_B66` | 长期演进（LTE）频段 66。 |
| `SIM7080_LTE_CHAN_B71` | 长期演进（LTE）频段 71。 |
| `SIM7080_LTE_CHAN_B85` | 长期演进（LTE）频段 85。 |

<a id="ga02721f95826487567017ebf780dff635"></a>

### `sim7080_rat`

```c
enum sim7080_rat
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

调制解调器无线接入技术（Radio Access Technology）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_RAT_LTE_NB1` | 仅窄带物联网（NB-IoT）。 |
| `SIM7080_RAT_LTE_M1` | 仅 LTE 类别 M1（CAT M1）。 |
| `SIM7080_RAT_LTE_AUTO` | 调制解调器自动选择 M1 或 NB1。 |
| `SIM7080_RAT_GSM` | 全球移动通信系统（GSM）。 |

<a id="ga04f3c0bce4f7d2b35762dc92f0aa20eb"></a>

### `sim7080_sms_stat`

```c
enum sim7080_sms_stat
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

存储中的短信可能状态（SMS States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_SMS_STAT_REC_UNREAD` | 消息未读（Message Unread）。 |
| `SIM7080_SMS_STAT_REC_READ` | 消息已读取。 |
| `SIM7080_SMS_STAT_STO_UNSENT` | 消息已存储但未发送（Stored Unsent）。 |
| `SIM7080_SMS_STAT_STO_SENT` | 消息已存储且已发送（Stored Sent）。 |
| `SIM7080_SMS_STAT_ALL` | 状态数量（Status Count）。 |

<a id="ga5d90415d319a9939f03752ff38a7c25a"></a>

### `sim7080_state`

```c
enum sim7080_state
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

SIM7080 调制解调器状态（Modem State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_STATE_INIT` | 调制解调器初始状态（Initial Modem State）。 |
| `SIM7080_STATE_IDLE` | 调制解调器空闲（Modem Idle）。 |
| `SIM7080_STATE_NETWORKING` | 网络已激活（Network Active）。 |
| `SIM7080_STATE_GNSS` | 全球导航卫星系统（GNSS）已激活。 |
| `SIM7080_STATE_OFF` | 调制解调器已关闭（Modem Off）。 |

<a id="gaeda25db4347c7fcfbee69e8d6edace64"></a>

### `sim7080_ue_op_mode`

```c
enum sim7080_ue_op_mode
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

用户设备工作模式（UE Operating Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_UE_OP_MODE_ONLINE` | 在线（Online）。 |
| `SIM7080_UE_OP_MODE_OFFLINE` | 离线（Offline）。 |
| `SIM7080_UE_OP_MODE_FACTORY_TEST_MODE` | 工厂测试模式（Factory Test Mode）。 |
| `SIM7080_UE_OP_MODE_RESET` | 复位（Reset）。 |
| `SIM7080_UE_OP_MODE_LOW_POWER_MODE` | 低功耗模式（Low Power Mode）。 |

<a id="ga25a5a23ca32dbd4bc7991274d3d1ce04"></a>

### `sim7080_ue_sys_mode`

```c
enum sim7080_ue_sys_mode
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

用户设备系统模式（UE System Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SIM7080_UE_SYS_MODE_NO_SERVICE` | 无服务（No Service）。 |
| `SIM7080_UE_SYS_MODE_GSM` | 全球移动通信系统（GSM）。 |
| `SIM7080_UE_SYS_MODE_LTE_CAT_M1` | LTE 类别 M1（CAT M1）。 |
| `SIM7080_UE_SYS_MODE_LTE_NB_IOT` | LTE 窄带物联网（NB-IoT）。 |

<a id="gae7137523b94c96d4816e4c19cb48313c"></a>

### `mdm_sim7080_delete_sms()`

```c
int mdm_sim7080_delete_sms ( uint16_t index)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

删除给定索引处的短信（SMS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 短信（SMS）在存储器中的索引。 |

**返回（Returns）**：返回：成功时为 0，否则返回 -1。

<a id="ga83acdbbe8cde8d73eec066f7e6829941"></a>

### `mdm_sim7080_dns_get_lookup_params()`

```c
void mdm_sim7080_dns_get_lookup_params ( uint8_t * recount, uint16_t * timeout )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 DNS 查询参数（Query Lookup Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `recount` | [out] 每次查询的重试次数（Number of Retries）。 |
| `timeout` | [out] DNS 查询超时时间（Timeout），单位为毫秒。 |

<a id="ga017a7dc143628ff5ff5646c7be6d4579"></a>

### `mdm_sim7080_dns_set_lookup_params()`

```c
int mdm_sim7080_dns_set_lookup_params ( uint8_t recount, uint16_t timeout )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

设置 DNS 查询参数（Query Lookup Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `recount` | 每次查询的重试次数（Number of Retries），最大为 SIM7080_DNS_MAX_RECOUNT。 |
| `timeout` | DNS 查询超时时间（Timeout），单位为毫秒，最大为 SIM7080_DNS_MAX_TIMEOUT_MS。 |

**返回（Returns）**：返回：成功时为 0，否则返回负错误码。

<a id="gad84438b511f6fed71668273470294420"></a>

### `mdm_sim7080_download_xtra()`

```c
int mdm_sim7080_download_xtra ( uint8_t server_id, const char * f_name )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

下载用于辅助 GNSS（Assisted GNSS）的 XTRA 文件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_id` | 用于下载 XTRA 文件的服务器 ID（Server ID）。 |
| `f_name` | 要下载的 XTRA 文件名称（File Name）。 |

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。

<a id="ga454c0078f17532f8e77bb036f9c0d707"></a>

### `mdm_sim7080_force_reset()`

```c
void mdm_sim7080_force_reset ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

通过将 pwrkey 拉动并保持 15 秒，强制复位调制解调器（Force Reset）。

**说明（Note）**：注意：调用此函数后，调制解调器状态可能未定义。强制复位（Force Reset）后应调用 mdm_sim7080_power_on。

<a id="ga74f00c0b99f71f7340740fb199db58a5"></a>

### `mdm_sim7080_ftp_get_read()`

```c
int mdm_sim7080_ftp_get_read ( char * dst, size_t * size )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

从 FTP 下载会话（FTP Get Session）读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 目标缓冲区（Destination Buffer）。 |
| `size` | 初始化为 dst 的大小；随后设置为实际读取的字节数。 |

**返回（Returns）**：返回：遵循 sim7080_ftp_rc。

<a id="ga53a7c0d347cfacf0d7fadaf073fbff6c"></a>

### `mdm_sim7080_ftp_get_start()`

```c
int mdm_sim7080_ftp_get_start ( const char * server, const char * user, const char * passwd, const char * file, const char * path )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

启动 FTP 下载会话（FTP Get Session）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | 文件传输协议服务器地址（FTP Server Address）。 |
| `user` | FTP 服务器的用户名（User Name）。 |
| `passwd` | FTP 用户的密码（Password）。 |
| `file` | 要下载的文件（File）。 |
| `path` | 服务器上的文件路径（File Path）。 |

**返回（Returns）**：返回：已启动会话（Session）时为 0，否则为 -1。

<a id="ga313d94f1005e562f6646867813d97fb2"></a>

### `mdm_sim7080_get_battery_charge()`

```c
int mdm_sim7080_get_battery_charge ( uint8_t * bcs, uint8_t * bcl, uint16_t * voltage )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

读取电压（Voltage）、充电状态（Charge Status）及电池连接电平（Battery Connection Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bcs` | [out] 充电状态（Charge Status）。 |
| `bcl` | [out] 电池连接级别（Battery Connection Level，原文用语）。 |
| `voltage` | [out] 电池电压（Battery Voltage），单位为 mV。 |

**返回（Returns）**：返回：成功时为 0，否则返回负错误码。

<a id="gad7e8d5c7cecb9b6150ad1148c81cf3ab"></a>

### `mdm_sim7080_get_iccid()`

```c
const char * mdm_sim7080_get_iccid ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 SIM7080 的集成电路卡识别码（ICCID）。

<a id="ga26d1291993cdcd44982c95bad2dd7b4f"></a>

### `mdm_sim7080_get_imei()`

```c
const char * mdm_sim7080_get_imei ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 SIM7080 的国际移动设备识别码（IMEI）。

<a id="ga71b0423009ee53ea6d2f4497820e775c"></a>

### `mdm_sim7080_get_local_time()`

```c
int mdm_sim7080_get_local_time ( struct tm * t)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取调制解调器的本地时间（Local Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `t` | 要填写的时间结构体（Time Structure）。 |

**返回（Returns）**：返回：成功时为 0，否则返回负错误码。

**说明（Note）**：注意：时间由网络设置，可能需要一段时间才会有效。

<a id="ga810526ebd0e2bec22c1dac87b5425d5d"></a>

### `mdm_sim7080_get_lte_bands()`

```c
void mdm_sim7080_get_lte_bands ( uint32_t * nb1, uint32_t * m1 )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取当前使用的 LTE 频段（Bands）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb1` | [out] 使用的 NB-IoT 频段（Bands），可以为 NULL。 |
| `m1` | [out] 使用的 CAT-M1 频段（Bands），可以为 NULL。 |

<a id="ga79837aee512ae6f2fed52f3162e39868"></a>

### `mdm_sim7080_get_manufacturer()`

```c
const char * mdm_sim7080_get_manufacturer ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 SIM7080 的制造商（Manufacturer）。

<a id="ga557ec2729649fd92c5588f6dd0a04f15"></a>

### `mdm_sim7080_get_model()`

```c
const char * mdm_sim7080_get_model ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 SIM7080 的型号信息（Model Information）。

<a id="gafe348fd71a838e6d3628e4025e859ba6"></a>

### `mdm_sim7080_get_rat()`

```c
void mdm_sim7080_get_rat ( enum sim7080_rat * rat)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取当前选定的无线技术（Radio Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rat` | [out] 设置为当前无线技术（Current Technology）。 |

<a id="ga9759bf93bc2e8e15869858853a9499de"></a>

### `mdm_sim7080_get_revision()`

```c
const char * mdm_sim7080_get_revision ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取 SIM7080 的修订版本（Revision）。

<a id="ga1e082cf652a5b34efdf50b30fe55f631"></a>

### `mdm_sim7080_get_state()`

```c
enum sim7080_state mdm_sim7080_get_state ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

获取调制解调器当前状态（Modem State）。

返回（Returns）：当前状态（Current State）。

<a id="ga2895183848c33177c5b788e08382ba09"></a>

### `mdm_sim7080_get_ue_sys_info()`

```c
int mdm_sim7080_get_ue_sys_info ( struct sim7080_ue_sys_info * info)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

读取用户设备系统信息（UE System Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `info` | 保存信息的目标缓冲区（Destination Buffer）。 |

**返回（Returns）**：返回：成功时为 0，否则返回负错误码。

<a id="ga35c2b87170079e5700021969d01d7f8b"></a>

### `mdm_sim7080_power_off()`

```c
int mdm_sim7080_power_off ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

关闭 SIM7080 电源（Power Off）。

**返回（Returns）**：返回：成功时为 0，否则返回 -1。

<a id="ga93395c2713539db360cdcf0170075ea1"></a>

### `mdm_sim7080_power_on()`

```c
int mdm_sim7080_power_on ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

开启 SIM7080 电源（Power On）。

**返回（Returns）**：返回：成功时为 0，否则返回 -1。

<a id="gacce71e254dd7854052678319227c3f5b"></a>

### `mdm_sim7080_query_gnss()`

```c
int mdm_sim7080_query_gnss ( struct sim7080_gnss_data * data)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

从调制解调器查询 GNSS 位置（Position）。

**返回（Returns）**：返回：成功时为 0；尚未取得定位结果（Fix）时返回 -EAGAIN；其他情况下返回小于 0 的值。

<a id="ga25692018fd26087e093b666a5884726c"></a>

### `mdm_sim7080_query_xtra_validity()`

```c
int mdm_sim7080_query_xtra_validity ( int16_t * diff_h, int16_t * duration_h, struct tm * inject )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

查询 XTRA 文件的有效性（Validity）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `diff_h` | 本地时间与 XTRA 注入时间（Inject Time）之差，单位为小时。 |
| `duration_h` | XTRA 文件的有效时间（Valid Time），单位为小时。 |
| `inject` | XTRA 文件的注入时间（Injection Time）。 |

<a id="gaacf368bc85d27d49709bde170a0db2ec"></a>

### `mdm_sim7080_read_sms()`

```c
int mdm_sim7080_read_sms ( struct sim7080_sms_buffer * buffer)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

从 SIM 模块读取短信（SMS）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buffer` | 短消息（SMS）的缓冲区结构。 |

**返回（Returns）**：返回：成功时为读取的短信（SMS）数量，否则为 -1。

**说明（Note）**：注意：缓冲区结构体需要按短信缓冲区大小初始化。此函数成功完成后，nsms 设置为读取的短信数量。如果整个结构体已填满，可能需要后续再次读取。

<a id="ga6cea6acdf6f02868a9f97c10b909a097"></a>

### `mdm_sim7080_set_gpio()`

```c
int mdm_sim7080_set_gpio ( int gpio, int level )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

设置模块某个 GPIO 引脚的电平（Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gpio` | GPIO引脚编号。 |
| `level` | GPIO 的新逻辑电平（Logical Level）。 |

**返回（Returns）**：返回：成功时为 0，否则返回 -1。

**说明（Note）**：注意：GPIO 会被隐式配置为输出（Output）。

<a id="ga4a4fbc695dc92fdf57cb7faf1f104f42"></a>

### `mdm_sim7080_set_lte_bands()`

```c
int mdm_sim7080_set_lte_bands ( uint32_t nb1, uint32_t m1 )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

设置要使用的 LTE 频段（Bands）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb1` | 要使用的 NB-IoT 频段（Bands）；0 表示不修改频段。 |
| `m1` | 要使用的 CAT-M1 频段（Bands）；0 表示不修改频段。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 频段选择（Band Selection）不合法。 |

**说明（Note）**：注意：必须在 mdm_sim7080_start_network() 前调用此函数。若网络已激活，修改不会影响当前会话；要应用修改，必须重启网络。可能还需要对调制解调器断电重启（Power Cycle），使其忘记上一次可用配置。NB-IoT 与 CAT-M1 的可用频段不同，参见 SIM7080_LTE_CHANNEL_MASK_NB1 和 SIM7080_LTE_CHANNEL_MASK_M1。

<a id="gaa33f561bff0c1a0c8fe484ae226fe421"></a>

### `mdm_sim7080_set_rat()`

```c
int mdm_sim7080_set_rat ( enum sim7080_rat rat)
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

设置无线技术（Radio Technology）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rat` | 无线技术（Radio Technology）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 选定的无线技术（Technology）不可用。 |

**说明（Note）**：注意：必须在 mdm_sim7080_start_network() 前调用此函数。若网络已激活，修改不会影响当前会话；要应用修改，必须重启网络。可能还需要对调制解调器断电重启（Power Cycle），使其忘记上一次可用配置。

<a id="ga6106a7d04282af2130471d26f6080ed4"></a>

### `mdm_sim7080_start_gnss()`

```c
int mdm_sim7080_start_gnss ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

以全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。

**说明（Note）**：注意：调制解调器必须已启动，此函数才能工作。网络与全球导航卫星系统（GNSS）不能同时使用。

<a id="ga7dc8062da9814bdee91b1e88092eee4b"></a>

### `mdm_sim7080_start_gnss_xtra()`

```c
int mdm_sim7080_start_gnss_xtra ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

以带 XTRA 功能的全球导航卫星系统工作模式（GNSS Operation Mode）启动调制解调器。

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。

**说明（Note）**：注意：调制解调器必须已启动，此函数才能工作。网络与全球导航卫星系统（GNSS）不能同时使用。若启用 XTRA 功能失败，将执行常规冷启动（Cold Start）。

**警告（Warning）**：警告：在某些调制解调器固件版本中，例如 1951B16SIM7080，使用 XTRA 文件时关闭并重新开启 GNSS 功能可能使调制解调器挂起（Hangup）。触发顺序可能为：调用 mdm_sim7080_start_gnss_xtra()，再调用 mdm_sim7080_stop_gnss() 关闭 GNSS，随后再次调用 mdm_sim7080_start_gnss_xtra() 启用 GNSS。此时调制解调器不再响应命令，每次调用调制解调器函数都会超时。必须调用 mdm_sim7080_power_off() 和 mdm_sim7080_power_on()，对整个调制解调器断电重启（Power Cycle）。建议在使用 GNSS 功能前先对调制解调器断电重启，以避免挂起。

<a id="gad857dd548490d40e6b9082c0b72e8d2b"></a>

### `mdm_sim7080_start_network()`

```c
int mdm_sim7080_start_network ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

激活调制解调器的网络工作模式（Network Operation Mode）。

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。

**说明（Note）**：注意：调制解调器必须已启动，此函数才能工作。网络与全球导航卫星系统（GNSS）不能同时使用。

<a id="ga617c649ba2524884d8bf11c91bd2c492"></a>

### `mdm_sim7080_stop_gnss()`

```c
int mdm_sim7080_stop_gnss ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

停止调制解调器的 GNSS 工作模式（Operation Mode）。

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。

<a id="gaa07958866afaf9b9cc65517abf65d08c"></a>

### `mdm_sim7080_stop_network()`

```c
int mdm_sim7080_stop_network ( void )
```

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

停止调制解调器的网络工作模式（Networking Operation Mode）。

**返回（Returns）**：返回：成功时为 0，否则返回小于 0 的值。


## 15.7\_原页交叉引用（Cross References）

- [simcom-sim7080.h](../api_file_audio_test_reference/P011_zephyr__drivers__modem__simcom-sim7080.h_文件参考.md)
- [sim7080_gnss_data](../modem_wireless_model_reference/P065_sim7080_gnss_data_结构体.md)
- [sim7080_sms](../modem_wireless_model_reference/P066_sim7080_sms_结构体.md)
- [sim7080_sms_buffer](../modem_wireless_model_reference/P067_sim7080_sms_buffer_结构体.md)
- [sim7080_ue_sys_info_gsm](../modem_wireless_model_reference/P069_sim7080_ue_sys_info_gsm_结构体.md)
- [sim7080_ue_sys_info_lte](../modem_wireless_model_reference/P070_sim7080_ue_sys_info_lte_结构体.md)
- [sim7080_ue_sys_info](../modem_wireless_model_reference/P068_sim7080_ue_sys_info_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [passwd](../posix_system_model_reference/P009_passwd_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga48afa6e777af6010488fbf726f467e63a6cc1c6e5f12101e8202deddf3667bbda"></a>
<a id="gga48afa6e777af6010488fbf726f467e63a6bc03b17b206166e04ec04a2638dc241"></a>
<a id="gga48afa6e777af6010488fbf726f467e63af744651290c73069148c0726bcdf95ce"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784af1fed81428e04fa1ed1102b754468e24"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784ab951b91a48e106c2bd34503a6408100c"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784abf07653aa5c5c7fc38c6c0e9a530b09a"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a7a65a1af619a8451cd1fe77e18b00e67"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784ab63b58736416d738f381c991b509aba9"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a892159a544473dc0e37ae22bbd1f7050"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784af337a56637a986f63e50c95165d3e28c"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a1d9dc9cfd0704de467f20330ef73337a"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a99777d6c606515e2f1cbdfdbf8c9877e"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a77c5d67140903e0c42292e1b92c23666"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a40e43ece45afd379aa071277f648649e"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a045d79d61b1f995edb75801e3b095465"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a970ee528bb955d0a90e76f09ff0ed5d0"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a5eaf600aed0d8079818929fa3a8f8d70"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a1cd7fc42302f32e4cc82f11b65fad528"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784ae967bd6f2a449b56acc647af6ecb6749"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784afc275bd937ca24a8dcab084205a0fe9e"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784aea11bd338ab8542e5e8083628a5603b9"></a>
<a id="ggafefcd23a6ce4c292b1cfc2bbcfa98784a9ce491762e30d7dc50f77b6a9b8af831"></a>
<a id="gga02721f95826487567017ebf780dff635a7939b7de8fece8cc1021b29394231671"></a>
<a id="gga02721f95826487567017ebf780dff635a1eabca23c4eda124b2ff759978f951e6"></a>
<a id="gga02721f95826487567017ebf780dff635a4338e0ab236bf3858ea88d6a5b1f5d36"></a>
<a id="gga02721f95826487567017ebf780dff635a9deadb1d3ade4641f22d08bd7bd6c3b3"></a>
<a id="gga04f3c0bce4f7d2b35762dc92f0aa20eba60957e1589dd8ce57c45ecc5fa114f86"></a>
<a id="gga04f3c0bce4f7d2b35762dc92f0aa20eba403ca4efe4553c0e4a6d2b2da5be4165"></a>
<a id="gga04f3c0bce4f7d2b35762dc92f0aa20eba770fe2a07f5dbb73221ff48eaedfb669"></a>
<a id="gga04f3c0bce4f7d2b35762dc92f0aa20ebab5c1ccc0cf53a21abc5f4d0145c414c5"></a>
<a id="gga04f3c0bce4f7d2b35762dc92f0aa20eba7afe21ab7bda162b25dc2c7daa127c35"></a>
<a id="gga5d90415d319a9939f03752ff38a7c25aac0bc355a3c8e0a996bb6a7a7f580cb6c"></a>
<a id="gga5d90415d319a9939f03752ff38a7c25aab024ba55594ab204a65f1a34a9b7b56a"></a>
<a id="gga5d90415d319a9939f03752ff38a7c25aa369ac733e64b26f64ec1070bd38c92d8"></a>
<a id="gga5d90415d319a9939f03752ff38a7c25aad90e03decaa89043d355447982133cf0"></a>
<a id="gga5d90415d319a9939f03752ff38a7c25aa3fa46c5fc0fc7d94255ee13280c88f8b"></a>
<a id="ggaeda25db4347c7fcfbee69e8d6edace64a600e1474544a7a78bdcd76204fe435b5"></a>
<a id="ggaeda25db4347c7fcfbee69e8d6edace64a036b486a3039accb70a4f771a66ec000"></a>
<a id="ggaeda25db4347c7fcfbee69e8d6edace64a5dcc819c05e2d77067a6c26c32f1e16c"></a>
<a id="ggaeda25db4347c7fcfbee69e8d6edace64a37a34e81132c5d5615e0692c6c3d10ff"></a>
<a id="ggaeda25db4347c7fcfbee69e8d6edace64aa4cff001bbfd8549d26a427fd4159d14"></a>
<a id="gga25a5a23ca32dbd4bc7991274d3d1ce04a30f4173c0221c5066cdd4d82ba254b8c"></a>
<a id="gga25a5a23ca32dbd4bc7991274d3d1ce04a6cf88dc2ac93074d74c36f59c4469e14"></a>
<a id="gga25a5a23ca32dbd4bc7991274d3d1ce04ab18bd882eec9368c2e65c45fdadc7ff2"></a>
<a id="gga25a5a23ca32dbd4bc7991274d3d1ce04a2279138ee4bbb5ed114fc13c7a058f00"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_TLS 套接字选项（Socket options）.md) · [返回大纲](大纲.md)
