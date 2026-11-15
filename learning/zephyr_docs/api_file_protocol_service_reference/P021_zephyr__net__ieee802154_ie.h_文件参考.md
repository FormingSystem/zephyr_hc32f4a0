---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-21
title: zephyr__net__ieee802154_ie.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_net\_\_ieee802154\_ie.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__ie_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IEEE 802.15.4 MAC信息元素（Information Element，IE）的相关类型和辅助接口。

<a id="details"></a>

```c
#include <zephyr/net_buf.h>
#include <zephyr/sys/byteorder.h>
```

查看此文件的源码。

IEEE 802.15.4 MAC 信息元素（Information Element，IE）相关类型和辅助接口。本文件不应由应用包含，只包含 IEEE 802.15.4 驱动和二层（L2）需要共同可见的 IE 支持类型部分，即头部 IE（Header IE）的表示、解析与生成相关内容。本文件所有规范引用均指 IEEE 802.15.4-2020。**注意（Note）：**本文件中直接表示 IEEE 802.15.4 帧组成部分的全部结构体和属性均采用小端序（Little Endian），参见第 4 节，尤其是 4.3 节。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_ieee802154_5Fheader_5Fie_5Fvendor_5Fspecific"></a>

```c
struct ieee802154_header_ie_vendor_specific
```

相关声明：[ieee802154_header_ie_vendor_specific](../network_core_model_reference/P031_ieee802154_header_ie_vendor_specific_结构体.md)。

厂商专用头部信息元素（Vendor Specific Header IE），见第7.4.2.3节。

<a id="r_ieee802154_5Fheader_5Fie_5Fcsl_5Ffull"></a>

```c
struct ieee802154_header_ie_csl_full
```

相关声明：[ieee802154_header_ie_csl_full](../network_core_model_reference/P024_ieee802154_header_ie_csl_full_结构体.md)。

完整的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="r_ieee802154_5Fheader_5Fie_5Fcsl_5Freduced"></a>

```c
struct ieee802154_header_ie_csl_reduced
```

相关声明：[ieee802154_header_ie_csl_reduced](../network_core_model_reference/P025_ieee802154_header_ie_csl_reduced_结构体.md)。

精简的协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="r_ieee802154_5Fheader_5Fie_5Fcsl"></a>

```c
struct ieee802154_header_ie_csl
```

相关声明：[ieee802154_header_ie_csl](../network_core_model_reference/P023_ieee802154_header_ie_csl_结构体.md)。

通用协调采样监听信息元素（CSL IE），见第7.4.2.3节。

<a id="r_ieee802154_5Fheader_5Fie_5Frit"></a>

```c
struct ieee802154_header_ie_rit
```

相关声明：[ieee802154_header_ie_rit](../network_core_model_reference/P029_ieee802154_header_ie_rit_结构体.md)。

接收方发起传输信息元素（RIT IE），见第7.4.2.4节。

<a id="r_ieee802154_5Fheader_5Fie_5Frendezvous_5Ftime_5Ffull"></a>

```c
struct ieee802154_header_ie_rendezvous_time_full
```

相关声明：[ieee802154_header_ie_rendezvous_time_full](../network_core_model_reference/P027_ieee802154_header_ie_rendezvous_time_full_结构体.md)。

完整的会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节；macCslInterval非零。

<a id="r_ieee802154_5Fheader_5Fie_5Frendezvous_5Ftime_5Freduced"></a>

```c
struct ieee802154_header_ie_rendezvous_time_reduced
```

相关声明：[ieee802154_header_ie_rendezvous_time_reduced](../network_core_model_reference/P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md)。

精简的会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节；macCslInterval为零。

<a id="r_ieee802154_5Fheader_5Fie_5Frendezvous_5Ftime"></a>

```c
struct ieee802154_header_ie_rendezvous_time
```

相关声明：[ieee802154_header_ie_rendezvous_time](../network_core_model_reference/P026_ieee802154_header_ie_rendezvous_time_结构体.md)。

会合时间信息元素（Rendezvous Time IE），见第7.4.2.6节。

<a id="r_ieee802154_5Fheader_5Fie_5Ftime_5Fcorrection"></a>

```c
struct ieee802154_header_ie_time_correction
```

相关声明：[ieee802154_header_ie_time_correction](../network_core_model_reference/P030_ieee802154_header_ie_time_correction_结构体.md)。

时间校正信息元素（Time Correction IE），见第7.4.2.7节。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 21.2\_IEEE 802.15.4 第 7.4.2 节：MAC 头部信息元素（Header Information Elements）

<a id="r_ga4f66344126179e2c98a17f19f6db516b"></a>

```c
#define IEEE802154_HEADER_IE_HEADER_LENGTH sizeof(uint16_t)
```

相关声明：[IEEE802154_HEADER_IE_HEADER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga4f66344126179e2c98a17f19f6db516b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

头部 IE（Header IE）的头部长度，为 2 字节。

<a id="r_gafc449a0c9d4ce8f128fd716b2a537f68"></a>

```c
#define IEEE802154_DEFINE_HEADER_IE_VENDOR_SPECIFIC(_vendor_oui, _vendor_specific_info, _vendor_specific_info_len)
```

相关声明：[IEEE802154_DEFINE_HEADER_IE_VENDOR_SPECIFIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gafc449a0c9d4ce8f128fd716b2a537f68)。

定义厂商专用头部 IE（Vendor-specific Header IE），参见 7.4.2.3 节。

<a id="r_ga382debc13f36ee16e0c015a2c2555c8f"></a>

```c
#define IEEE802154_DEFINE_HEADER_IE_CSL_REDUCED(_csl_phase, _csl_period)
```

相关声明：[IEEE802154_DEFINE_HEADER_IE_CSL_REDUCED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga382debc13f36ee16e0c015a2c2555c8f)。

定义精简 CSL IE（Reduced CSL IE），参见 7.4.2.3 节。

<a id="r_ga3392a33334814ae63e212491ea90ae74"></a>

```c
#define IEEE802154_DEFINE_HEADER_IE_CSL_FULL(_csl_phase, _csl_period, _csl_rendezvous_time)
```

相关声明：[IEEE802154_DEFINE_HEADER_IE_CSL_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3392a33334814ae63e212491ea90ae74)。

定义完整 CSL IE（Full CSL IE），参见 7.4.2.3 节。

<a id="r_gac2549865f529b5aff1653c80ceda9650"></a>

```c
#define IEEE802154_DEFINE_HEADER_IE_TIME_CORRECTION(_ack, _time_correction_us)
```

相关声明：[IEEE802154_DEFINE_HEADER_IE_TIME_CORRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gac2549865f529b5aff1653c80ceda9650)。

定义时间校正 IE（Time Correction IE），参见 7.4.2.7 节。

<a id="r_gaaaf32be17c41497c8d3be48292ad1374"></a>

```c
#define IEEE802154_TIME_CORRECTION_HEADER_IE_LEN (IEEE802154_HEADER_IE_HEADER_LENGTH + sizeof(struct ieee802154_header_ie_time_correction))
```

相关声明：[IEEE802154_TIME_CORRECTION_HEADER_IE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaaaf32be17c41497c8d3be48292ad1374)、[IEEE802154_HEADER_IE_HEADER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga4f66344126179e2c98a17f19f6db516b)、[ieee802154_header_ie_time_correction](../network_core_model_reference/P030_ieee802154_header_ie_time_correction_结构体.md)。

“时间校正”（Time Correction）头部 IE 的字节长度。

<a id="r_gae16b5d403da141b0f9d9279817703677"></a>

```c
#define IEEE802154_HEADER_TERMINATION_1_HEADER_IE_LEN IEEE802154_HEADER_IE_HEADER_LENGTH
```

相关声明：[IEEE802154_HEADER_TERMINATION_1_HEADER_IE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gae16b5d403da141b0f9d9279817703677)、[IEEE802154_HEADER_IE_HEADER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga4f66344126179e2c98a17f19f6db516b)。

“头部终止 1”（Header Termination 1）头部 IE 的字节长度。

<a id="r_ga207e3aa0454f9e4173c809cfe7ff32cd"></a>

```c
enum ieee802154_ie_type { IEEE802154_IE_TYPE_HEADER = 0x0 , IEEE802154_IE_TYPE_PAYLOAD }
```

相关声明：[ieee802154_ie_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga207e3aa0454f9e4173c809cfe7ff32cd)、[IEEE802154_IE_TYPE_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a)、[IEEE802154_IE_TYPE_PAYLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7)。

信息元素类型（Information Element Types）。

<a id="r_ga0de396c2c2c781ff85b94ebf577f15ce"></a>

```c
enum ieee802154_header_ie_element_id { IEEE802154_HEADER_IE_ELEMENT_ID_VENDOR_SPECIFIC_IE = 0x00 , IEEE802154_HEADER_IE_ELEMENT_ID_CSL_IE = 0x1a , IEEE802154_HEADER_IE_ELEMENT_ID_RIT_IE = 0x1b , IEEE802154_HEADER_IE_ELEMENT_ID_RENDEZVOUS_TIME_IE = 0x1d , IEEE802154_HEADER_IE_ELEMENT_ID_TIME_CORRECTION_IE = 0x1e , IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_1 = 0x7e , IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_2 = 0x7f }
```

相关声明：[ieee802154_header_ie_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga0de396c2c2c781ff85b94ebf577f15ce)、[IEEE802154_HEADER_IE_ELEMENT_ID_VENDOR_SPECIFIC_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14)、[IEEE802154_HEADER_IE_ELEMENT_ID_CSL_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb)、[IEEE802154_HEADER_IE_ELEMENT_ID_RIT_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021)、[IEEE802154_HEADER_IE_ELEMENT_ID_RENDEZVOUS_TIME_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e)、[IEEE802154_HEADER_IE_ELEMENT_ID_TIME_CORRECTION_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330)、[IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3)、[IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941)。

头部信息元素 ID（Header Information Element IDs）。

<a id="r_gaaae70f7d15135b2e77369cef3c61ba62"></a>

```c
static int16_t ieee802154_header_ie_get_time_correction_us (struct ieee802154_header_ie_time_correction *ie)
```

相关声明：[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[ieee802154_header_ie_get_time_correction_us](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaaae70f7d15135b2e77369cef3c61ba62)、[ieee802154_header_ie_time_correction](../network_core_model_reference/P030_ieee802154_header_ie_time_correction_结构体.md)。

从时间校正 IE（Time Correction IE）获取以微秒为单位的时间校正值，参见 7.4.2.7 节。

<a id="r_gaef81648e58dc4fbdfd942a1d856952fa"></a>

```c
static void ieee802154_header_ie_set_element_id (struct ieee802154_header_ie *ie, uint8_t element_id)
```

相关声明：[ieee802154_header_ie_set_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaef81648e58dc4fbdfd942a1d856952fa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置头部 IE（Header IE）的元素 ID。

<a id="r_gaec7f06d8bf0b44c3350d1d07a65c6cb4"></a>

```c
static uint8_t ieee802154_header_ie_get_element_id (struct ieee802154_header_ie *ie)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ieee802154_header_ie_get_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaec7f06d8bf0b44c3350d1d07a65c6cb4)。

获取头部 IE（Header IE）的元素 ID。


## 21.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P002_系统字节序头文件源码.md)
- [查看此文件的源码。](../api_source_network_reference/P009_ieee802154_ie.h_源码浏览.md)
- [ieee802154_header_ie_vendor_specific](../network_core_model_reference/P031_ieee802154_header_ie_vendor_specific_结构体.md)
- [ieee802154_header_ie_csl_full](../network_core_model_reference/P024_ieee802154_header_ie_csl_full_结构体.md)
- [ieee802154_header_ie_csl_reduced](../network_core_model_reference/P025_ieee802154_header_ie_csl_reduced_结构体.md)
- [ieee802154_header_ie_csl](../network_core_model_reference/P023_ieee802154_header_ie_csl_结构体.md)
- [ieee802154_header_ie_rit](../network_core_model_reference/P029_ieee802154_header_ie_rit_结构体.md)
- [ieee802154_header_ie_rendezvous_time_full](../network_core_model_reference/P027_ieee802154_header_ie_rendezvous_time_full_结构体.md)
- [ieee802154_header_ie_rendezvous_time_reduced](../network_core_model_reference/P028_ieee802154_header_ie_rendezvous_time_reduced_结构体.md)
- [ieee802154_header_ie_rendezvous_time](../network_core_model_reference/P026_ieee802154_header_ie_rendezvous_time_结构体.md)
- [ieee802154_header_ie_time_correction](../network_core_model_reference/P030_ieee802154_header_ie_time_correction_结构体.md)
- [IEEE802154_HEADER_IE_HEADER_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga4f66344126179e2c98a17f19f6db516b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [IEEE802154_DEFINE_HEADER_IE_VENDOR_SPECIFIC](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gafc449a0c9d4ce8f128fd716b2a537f68)
- [IEEE802154_DEFINE_HEADER_IE_CSL_REDUCED](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga382debc13f36ee16e0c015a2c2555c8f)
- [IEEE802154_DEFINE_HEADER_IE_CSL_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga3392a33334814ae63e212491ea90ae74)
- [IEEE802154_DEFINE_HEADER_IE_TIME_CORRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gac2549865f529b5aff1653c80ceda9650)
- [IEEE802154_TIME_CORRECTION_HEADER_IE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaaaf32be17c41497c8d3be48292ad1374)
- [IEEE802154_HEADER_TERMINATION_1_HEADER_IE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gae16b5d403da141b0f9d9279817703677)
- [ieee802154_ie_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga207e3aa0454f9e4173c809cfe7ff32cd)
- [IEEE802154_IE_TYPE_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga207e3aa0454f9e4173c809cfe7ff32cda6891d992dc8d592ed8bd95cf836cab1a)
- [IEEE802154_IE_TYPE_PAYLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga207e3aa0454f9e4173c809cfe7ff32cda87905298e0b0920f9da8053129471af7)
- [ieee802154_header_ie_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#ga0de396c2c2c781ff85b94ebf577f15ce)
- [IEEE802154_HEADER_IE_ELEMENT_ID_VENDOR_SPECIFIC_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceaf02726c8c317ee15e92c1d43b4392c14)
- [IEEE802154_HEADER_IE_ELEMENT_ID_CSL_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea69e4548081815bd45ea68c52d1b66efb)
- [IEEE802154_HEADER_IE_ELEMENT_ID_RIT_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceaffc141c8eebdc4b39df6d7b314b8e021)
- [IEEE802154_HEADER_IE_ELEMENT_ID_RENDEZVOUS_TIME_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea12b16ed83f7b7fb952b86c151af65e5e)
- [IEEE802154_HEADER_IE_ELEMENT_ID_TIME_CORRECTION_IE](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea3f050528506d59ba26a100e42a182330)
- [IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15cea5034cb0963de1fd64a9018937cfeaec3)
- [IEEE802154_HEADER_IE_ELEMENT_ID_HEADER_TERMINATION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gga0de396c2c2c781ff85b94ebf577f15ceabd8d5a5fe12f978ace7eb5a089df6941)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [ieee802154_header_ie_get_time_correction_us](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaaae70f7d15135b2e77369cef3c61ba62)
- [ieee802154_header_ie_set_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaef81648e58dc4fbdfd942a1d856952fa)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_header_ie_get_element_id](https://docs.zephyrproject.org/latest/doxygen/html/group__ieee802154__driver.html#gaec7f06d8bf0b44c3350d1d07a65c6cb4)

<a id="header-details"></a>

---

[上一章](P020_zephyr__net__icmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__interrupt_controller__intc_renesas_rx_grp_int.h_文件参考.md)
