---
id: learning.zephyr-docs.api-file-supplement-reference.page-71
title: zephyr__modem__ubx__protocol.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_zephyr\_\_modem\_\_ubx\_\_protocol.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/modem/ubx/checksum.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 71.1\_数据结构（Data Structures）

<a id="r_ubx_5Fframe"></a>

```c
struct ubx_frame
```

相关声明：[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。

<a id="r_ubx_5Fframe_5Fmatch"></a>

```c
struct ubx_frame_match
```

相关声明：[ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)。

<a id="r_ubx_5Fnav_5Fpvt"></a>

```c
struct ubx_nav_pvt
```

相关声明：[ubx_nav_pvt](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md)。

<a id="r_ubx_5Fnav_5Fsat"></a>

```c
struct ubx_nav_sat
```

相关声明：[ubx_nav_sat](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md)。

<a id="r_ubx_5Fnav_5Fsat_3A_3Aubx_5Fnav_5Fsat_5Finfo"></a>

```c
struct ubx_nav_sat::ubx_nav_sat_info
```

相关声明：[ubx_nav_sat::ubx_nav_sat_info](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)。

<a id="r_ubx_5Fack"></a>

```c
struct ubx_ack
```

相关声明：[ubx_ack](../sensor_navigation_model_reference/P056_ubx_ack_结构体.md)。

<a id="r_ubx_5Fmon_5Fgnss"></a>

```c
struct ubx_mon_gnss
```

相关声明：[ubx_mon_gnss](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md)。

<a id="r_ubx_5Fcfg_5Fprt"></a>

```c
struct ubx_cfg_prt
```

相关声明：[ubx_cfg_prt](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md)。

<a id="r_ubx_5Fcfg_5Fnav5"></a>

```c
struct ubx_cfg_nav5
```

相关声明：[ubx_cfg_nav5](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md)。

<a id="r_ubx_5Fcfg_5Frst"></a>

```c
struct ubx_cfg_rst
```

相关声明：[ubx_cfg_rst](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md)。

<a id="r_ubx_5Fcfg_5Frate"></a>

```c
struct ubx_cfg_rate
```

相关声明：[ubx_cfg_rate](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md)。

<a id="r_ubx_5Fcfg_5Fval_5Fhdr"></a>

```c
struct ubx_cfg_val_hdr
```

相关声明：[ubx_cfg_val_hdr](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md)。

<a id="r_ubx_5Fcfg_5Fval_5Fu8"></a>

```c
struct ubx_cfg_val_u8
```

相关声明：[ubx_cfg_val_u8](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md)。

<a id="r_ubx_5Fcfg_5Fval_5Fu16"></a>

```c
struct ubx_cfg_val_u16
```

相关声明：[ubx_cfg_val_u16](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md)。

<a id="r_ubx_5Fcfg_5Fval_5Fu32"></a>

```c
struct ubx_cfg_val_u32
```

相关声明：[ubx_cfg_val_u32](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md)。

<a id="r_ubx_5Fcfg_5Fmsg_5Frate"></a>

```c
struct ubx_cfg_msg_rate
```

相关声明：[ubx_cfg_msg_rate](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md)。

<a id="r_ubx_5Fmon_5Fver"></a>

```c
struct ubx_mon_ver
```

相关声明：[ubx_mon_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 71.2\_宏定义（Macros）

<a id="r_a1342f8e944fcd9f45fe94eef9bda307c"></a>

```c
#define UBX_FRAME_HEADER_SZ 6
```

相关声明：[UBX_FRAME_HEADER_SZ](#a1342f8e944fcd9f45fe94eef9bda307c)。

<a id="r_aa0392f4a081c1077b4f235a757431aee"></a>

```c
#define UBX_FRAME_FOOTER_SZ 2
```

相关声明：[UBX_FRAME_FOOTER_SZ](#aa0392f4a081c1077b4f235a757431aee)。

<a id="r_a8e1aded66fd229f071c9d5e060a001a6"></a>

```c
#define UBX_FRAME_SZ_WITHOUT_PAYLOAD (UBX_FRAME_HEADER_SZ + UBX_FRAME_FOOTER_SZ)
```

相关声明：[UBX_FRAME_SZ_WITHOUT_PAYLOAD](#a8e1aded66fd229f071c9d5e060a001a6)、[UBX_FRAME_HEADER_SZ](#a1342f8e944fcd9f45fe94eef9bda307c)、[UBX_FRAME_FOOTER_SZ](#aa0392f4a081c1077b4f235a757431aee)。

<a id="r_a4c64b9118da471baa6a7a88ee345bf66"></a>

```c
#define UBX_FRAME_SZ(payload_size)
```

相关声明：[UBX_FRAME_SZ](#a4c64b9118da471baa6a7a88ee345bf66)。

<a id="r_a1693f3584605a0197076cba71c79b0df"></a>

```c
#define UBX_PREAMBLE_SYNC_CHAR_1 0xB5
```

相关声明：[UBX_PREAMBLE_SYNC_CHAR_1](#a1693f3584605a0197076cba71c79b0df)。

<a id="r_ad8d6229db563db619d4f0a9f225fb640"></a>

```c
#define UBX_PREAMBLE_SYNC_CHAR_2 0x62
```

相关声明：[UBX_PREAMBLE_SYNC_CHAR_2](#ad8d6229db563db619d4f0a9f225fb640)。

<a id="r_a1b417ed30e090d3399f96c87dfe842c4"></a>

```c
#define UBX_FRAME_PREAMBLE_SYNC_CHAR_1_IDX 0
```

相关声明：[UBX_FRAME_PREAMBLE_SYNC_CHAR_1_IDX](#a1b417ed30e090d3399f96c87dfe842c4)。

<a id="r_af940bf4cc68adff5b8b187dcf1e93735"></a>

```c
#define UBX_FRAME_PREAMBLE_SYNC_CHAR_2_IDX 1
```

相关声明：[UBX_FRAME_PREAMBLE_SYNC_CHAR_2_IDX](#af940bf4cc68adff5b8b187dcf1e93735)。

<a id="r_a2c667ef9bb2d12effb251f4df6827c73"></a>

```c
#define UBX_FRAME_MSG_CLASS_IDX 2
```

相关声明：[UBX_FRAME_MSG_CLASS_IDX](#a2c667ef9bb2d12effb251f4df6827c73)。

<a id="r_a9c66cd27732153c56d0872339bc3deae"></a>

```c
#define UBX_PAYLOAD_SZ_MAX 512
```

相关声明：[UBX_PAYLOAD_SZ_MAX](#a9c66cd27732153c56d0872339bc3deae)。

<a id="r_a1cab11988642144cfcc6c7309f5806d0"></a>

```c
#define UBX_FRAME_SZ_MAX UBX_FRAME_SZ(UBX_PAYLOAD_SZ_MAX)
```

相关声明：[UBX_FRAME_SZ_MAX](#a1cab11988642144cfcc6c7309f5806d0)、[UBX_FRAME_SZ](#a4c64b9118da471baa6a7a88ee345bf66)、[UBX_PAYLOAD_SZ_MAX](#a9c66cd27732153c56d0872339bc3deae)。

<a id="r_ae9c98287cbaf17e7fc1beaedc1679fa4"></a>

```c
#define UBX_NAV_PVT_VALID_DATE BIT(0)
```

相关声明：[UBX_NAV_PVT_VALID_DATE](#ae9c98287cbaf17e7fc1beaedc1679fa4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a583269f4c0ea39e43671fd9267b129af"></a>

```c
#define UBX_NAV_PVT_VALID_TIME BIT(1)
```

相关声明：[UBX_NAV_PVT_VALID_TIME](#a583269f4c0ea39e43671fd9267b129af)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4ea40193fa60a75bf5ede5586da92931"></a>

```c
#define UBX_NAV_PVT_VALID_UTC_TOD BIT(2)
```

相关声明：[UBX_NAV_PVT_VALID_UTC_TOD](#a4ea40193fa60a75bf5ede5586da92931)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1f067fe87ff51b4b59e7bfce2c4b9880"></a>

```c
#define UBX_NAV_PVT_VALID_MAGN BIT(3)
```

相关声明：[UBX_NAV_PVT_VALID_MAGN](#a1f067fe87ff51b4b59e7bfce2c4b9880)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af79a6a074065fb7d792109b4d99ba32f"></a>

```c
#define UBX_NAV_PVT_FLAGS_GNSS_FIX_OK BIT(0)
```

相关声明：[UBX_NAV_PVT_FLAGS_GNSS_FIX_OK](#af79a6a074065fb7d792109b4d99ba32f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6318967f82a82af78715635fc7592ce6"></a>

```c
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FLOATING BIT(6)
```

相关声明：[UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FLOATING](#a6318967f82a82af78715635fc7592ce6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a395c3edfbf84edc09f7af09d0a8b48c0"></a>

```c
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FIXED BIT(7)
```

相关声明：[UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FIXED](#a395c3edfbf84edc09f7af09d0a8b48c0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac348d618c31a5ae7b243243267b041c6"></a>

```c
#define UBX_NAV_PVT_FLAGS3_INVALID_LLH BIT(0)
```

相关声明：[UBX_NAV_PVT_FLAGS3_INVALID_LLH](#ac348d618c31a5ae7b243243267b041c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aaaa4b2e1968a45f4c7ee336a45b4164b"></a>

```c
#define UBX_NAV_SAT_FLAGS_SV_USED BIT(3)
```

相关声明：[UBX_NAV_SAT_FLAGS_SV_USED](#aaaa4b2e1968a45f4c7ee336a45b4164b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8c665bbb309e589b8bd88268b802a3eb"></a>

```c
#define UBX_NAV_SAT_FLAGS_RTCM_CORR_USED BIT(17)
```

相关声明：[UBX_NAV_SAT_FLAGS_RTCM_CORR_USED](#a8c665bbb309e589b8bd88268b802a3eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae23528d7cc5a34a48f062a084ae2dbd0"></a>

```c
#define UBX_GNSS_SELECTION_GPS BIT(0)
```

相关声明：[UBX_GNSS_SELECTION_GPS](#ae23528d7cc5a34a48f062a084ae2dbd0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab767685719aa08364b5e77262fae232a"></a>

```c
#define UBX_GNSS_SELECTION_GLONASS BIT(1)
```

相关声明：[UBX_GNSS_SELECTION_GLONASS](#ab767685719aa08364b5e77262fae232a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad57613b25d1716b7ca3e01d37b64a16d"></a>

```c
#define UBX_GNSS_SELECTION_BEIDOU BIT(2)
```

相关声明：[UBX_GNSS_SELECTION_BEIDOU](#ad57613b25d1716b7ca3e01d37b64a16d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa338a732341e0e1560a749123cecd700"></a>

```c
#define UBX_GNSS_SELECTION_GALILEO BIT(3)
```

相关声明：[UBX_GNSS_SELECTION_GALILEO](#aa338a732341e0e1560a749123cecd700)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0eb35bbe06a126aa8aed1738b6dd56c2"></a>

```c
#define UBX_CFG_PRT_MODE_CHAR_LEN(val)
```

相关声明：[UBX_CFG_PRT_MODE_CHAR_LEN](#a0eb35bbe06a126aa8aed1738b6dd56c2)。

<a id="r_abe8dd1db5cf126f76f7a44f4715e9cfa"></a>

```c
#define UBX_CFG_PRT_MODE_PARITY(val)
```

相关声明：[UBX_CFG_PRT_MODE_PARITY](#abe8dd1db5cf126f76f7a44f4715e9cfa)。

<a id="r_a23d980439eed2fe310c8be5107333489"></a>

```c
#define UBX_CFG_PRT_MODE_STOP_BITS(val)
```

相关声明：[UBX_CFG_PRT_MODE_STOP_BITS](#a23d980439eed2fe310c8be5107333489)。

<a id="r_a3f8c1064b9f51778df32e0b713302a2e"></a>

```c
#define UBX_CFG_PRT_PROTO_MASK_UBX BIT(0)
```

相关声明：[UBX_CFG_PRT_PROTO_MASK_UBX](#a3f8c1064b9f51778df32e0b713302a2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a174c408931fd4ca3e6c8128dd540d2dd"></a>

```c
#define UBX_CFG_PRT_PROTO_MASK_NMEA BIT(1)
```

相关声明：[UBX_CFG_PRT_PROTO_MASK_NMEA](#a174c408931fd4ca3e6c8128dd540d2dd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad481e57bb7b8707c468990ad0568d53c"></a>

```c
#define UBX_CFG_PRT_PROTO_MASK_RTCM3 BIT(5)
```

相关声明：[UBX_CFG_PRT_PROTO_MASK_RTCM3](#ad481e57bb7b8707c468990ad0568d53c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_adcfe7daa815d7a1a7dea67642b88ebbf"></a>

```c
#define UBX_CFG_NAV5_APPLY_DYN BIT(0)
```

相关声明：[UBX_CFG_NAV5_APPLY_DYN](#adcfe7daa815d7a1a7dea67642b88ebbf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a93b02f16b10968f47932c502e300c5a6"></a>

```c
#define UBX_CFG_NAV5_APPLY_FIX_MODE BIT(2)
```

相关声明：[UBX_CFG_NAV5_APPLY_FIX_MODE](#a93b02f16b10968f47932c502e300c5a6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad79a0ce05086ada71822ccb9100bc100"></a>

```c
#define UBX_FRAME_DEFINE(_name, _frame)
```

相关声明：[UBX_FRAME_DEFINE](#ad79a0ce05086ada71822ccb9100bc100)。

<a id="r_aca7cb6846e6d01cc84df655f22832987"></a>

```c
#define UBX_FRAME_ARRAY_DEFINE(_name, ...)
```

相关声明：[UBX_FRAME_ARRAY_DEFINE](#aca7cb6846e6d01cc84df655f22832987)。

<a id="r_a8cf6388d5ee4509e36742e30dc640889"></a>

```c
#define UBX_FRAME_ACK_INITIALIZER(_class_id, _msg_id)
```

相关声明：[UBX_FRAME_ACK_INITIALIZER](#a8cf6388d5ee4509e36742e30dc640889)。

<a id="r_a5b5ffd92f5894fc966b1875c7ce4c1a3"></a>

```c
#define UBX_FRAME_NAK_INITIALIZER(_class_id, _msg_id)
```

相关声明：[UBX_FRAME_NAK_INITIALIZER](#a5b5ffd92f5894fc966b1875c7ce4c1a3)。

<a id="r_aed21b263c25f39d499b37dfff38bca39"></a>

```c
#define UBX_FRAME_CFG_RST_INITIALIZER(_start_mode, _reset_mode)
```

相关声明：[UBX_FRAME_CFG_RST_INITIALIZER](#aed21b263c25f39d499b37dfff38bca39)。

<a id="r_a3192675717120efc97a8858605b3f45d"></a>

```c
#define UBX_FRAME_CFG_RATE_INITIALIZER(_meas_rate_ms, _nav_rate, _time_ref)
```

相关声明：[UBX_FRAME_CFG_RATE_INITIALIZER](#a3192675717120efc97a8858605b3f45d)。

<a id="r_af9ce35b33de7f9ebc68d11731beb02f0"></a>

```c
#define UBX_FRAME_CFG_MSG_RATE_INITIALIZER(_class_id, _msg_id, _rate)
```

相关声明：[UBX_FRAME_CFG_MSG_RATE_INITIALIZER](#af9ce35b33de7f9ebc68d11731beb02f0)。

<a id="r_a5b4484d44a25068f960f7f1196cffe89"></a>

```c
#define UBX_FRAME_CFG_VAL_SET_U8_INITIALIZER(_key, _value)
```

相关声明：[UBX_FRAME_CFG_VAL_SET_U8_INITIALIZER](#a5b4484d44a25068f960f7f1196cffe89)。

<a id="r_a66b9664185ed9cfb096df2b375e41f0e"></a>

```c
#define UBX_FRAME_CFG_VAL_SET_U16_INITIALIZER(_key, _value)
```

相关声明：[UBX_FRAME_CFG_VAL_SET_U16_INITIALIZER](#a66b9664185ed9cfb096df2b375e41f0e)。

<a id="r_a997cd3bd57d5cfc6c4f1eeca2bc6ba37"></a>

```c
#define UBX_FRAME_CFG_VAL_SET_U32_INITIALIZER(_key, _value)
```

相关声明：[UBX_FRAME_CFG_VAL_SET_U32_INITIALIZER](#a997cd3bd57d5cfc6c4f1eeca2bc6ba37)。

<a id="r_a1d7a930de22dadce2aae88e64e246dd9"></a>

```c
#define UBX_FRAME_CFG_VAL_GET_INITIALIZER(_key)
```

相关声明：[UBX_FRAME_CFG_VAL_GET_INITIALIZER](#a1d7a930de22dadce2aae88e64e246dd9)。

<a id="r_a4d90346d76d003aeddf16fc665203926"></a>

```c
#define UBX_FRAME_INITIALIZER_PAYLOAD(_class_id, _msg_id, ...)
```

相关声明：[UBX_FRAME_INITIALIZER_PAYLOAD](#a4d90346d76d003aeddf16fc665203926)。

<a id="r_a1cf8842293fe70f3ea22686a55d9beda"></a>

```c
#define UBX_FRAME_GET_INITIALIZER(_class_id, _msg_id)
```

相关声明：[UBX_FRAME_GET_INITIALIZER](#a1cf8842293fe70f3ea22686a55d9beda)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 71.3\_枚举（Enumerations）

<a id="r_ad0dac3b7e7cbf3649aa5b8813e40fc18"></a>

```c
enum ubx_class_id { UBX_CLASS_ID_NAV = 0x01 , UBX_CLASS_ID_RXM = 0x02 , UBX_CLASS_ID_INF = 0x04 , UBX_CLASS_ID_ACK = 0x05 , UBX_CLASS_ID_CFG = 0x06 , UBX_CLASS_ID_UPD = 0x09 , UBX_CLASS_ID_MON = 0x0A , UBX_CLASS_ID_TIM = 0x0D , UBX_CLASS_ID_MGA = 0x13 , UBX_CLASS_ID_LOG = 0x21 , UBX_CLASS_ID_SEC = 0x27 , UBX_CLASS_ID_NMEA_STD = 0xF0 , UBX_CLASS_ID_NMEA_PUBX = 0xF1 }
```

相关声明：[ubx_class_id](#ad0dac3b7e7cbf3649aa5b8813e40fc18)、[UBX_CLASS_ID_NAV](#ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1)、[UBX_CLASS_ID_RXM](#ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321)、[UBX_CLASS_ID_INF](#ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0)、[UBX_CLASS_ID_ACK](#ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b)、[UBX_CLASS_ID_CFG](#ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c)、[UBX_CLASS_ID_UPD](#ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b)、[UBX_CLASS_ID_MON](#ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed)、[UBX_CLASS_ID_TIM](#ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0)、[UBX_CLASS_ID_MGA](#ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f)、[UBX_CLASS_ID_LOG](#ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb)、[UBX_CLASS_ID_SEC](#ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4)、[UBX_CLASS_ID_NMEA_STD](#ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79)、[UBX_CLASS_ID_NMEA_PUBX](#ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895)。

<a id="r_a8a935ea7debb4ac73ea99c98d6ef4d3b"></a>

```c
enum ubx_msg_id_nav { UBX_MSG_ID_NAV_PVT = 0x07 , UBX_MSG_ID_NAV_SAT = 0x35 }
```

相关声明：[ubx_msg_id_nav](#a8a935ea7debb4ac73ea99c98d6ef4d3b)、[UBX_MSG_ID_NAV_PVT](#a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458)、[UBX_MSG_ID_NAV_SAT](#a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae)。

<a id="r_a173b6c1016562da43b8131b8d8f04fef"></a>

```c
enum ubx_nav_fix_type { UBX_NAV_FIX_TYPE_NO_FIX = 0 , UBX_NAV_FIX_TYPE_DR = 1 , UBX_NAV_FIX_TYPE_2D = 2 , UBX_NAV_FIX_TYPE_3D = 3 , UBX_NAV_FIX_TYPE_GNSS_DR_COMBINED = 4 , UBX_NAV_FIX_TYPE_TIME_ONLY = 5 }
```

相关声明：[ubx_nav_fix_type](#a173b6c1016562da43b8131b8d8f04fef)、[UBX_NAV_FIX_TYPE_NO_FIX](#a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498)、[UBX_NAV_FIX_TYPE_DR](#a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e)、[UBX_NAV_FIX_TYPE_2D](#a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651)、[UBX_NAV_FIX_TYPE_3D](#a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43)、[UBX_NAV_FIX_TYPE_GNSS_DR_COMBINED](#a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71)、[UBX_NAV_FIX_TYPE_TIME_ONLY](#a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845)。

<a id="r_a3384ec6c907acb911c4a9c32bcd473ca"></a>

```c
enum ubx_nav_hp_dgnss_mode { UBX_NAV_HP_DGNSS_MODE_RTK_FLOAT = 2 , UBX_NAV_HP_DGNSS_MODE_RTK_FIXED = 3 }
```

相关声明：[ubx_nav_hp_dgnss_mode](#a3384ec6c907acb911c4a9c32bcd473ca)、[UBX_NAV_HP_DGNSS_MODE_RTK_FLOAT](#a3384ec6c907acb911c4a9c32bcd473caaec46850a66dfd2d6bfcb18849a737fdc)、[UBX_NAV_HP_DGNSS_MODE_RTK_FIXED](#a3384ec6c907acb911c4a9c32bcd473caa521219142a95c322e501497ab6262798)。

<a id="r_afbba8ada09d6c6489d52a3b9dc31725f"></a>

```c
enum ubx_nav_sat_health { UBX_NAV_SAT_HEALTH_UNKNOWN = 0 , UBX_NAV_SAT_HEALTH_HEALTHY = 1 , UBX_NAV_SAT_HEALTH_UNHEALTHY = 2 }
```

相关声明：[ubx_nav_sat_health](#afbba8ada09d6c6489d52a3b9dc31725f)、[UBX_NAV_SAT_HEALTH_UNKNOWN](#afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194)、[UBX_NAV_SAT_HEALTH_HEALTHY](#afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e)、[UBX_NAV_SAT_HEALTH_UNHEALTHY](#afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139)。

<a id="r_a6711a33292bf25327950406b96585690"></a>

```c
enum ubx_gnss_id { UBX_GNSS_ID_GPS = 0 , UBX_GNSS_ID_SBAS = 1 , UBX_GNSS_ID_GALILEO = 2 , UBX_GNSS_ID_BEIDOU = 3 , UBX_GNSS_ID_QZSS = 5 , UBX_GNSS_ID_GLONASS = 6 }
```

相关声明：[ubx_gnss_id](#a6711a33292bf25327950406b96585690)、[UBX_GNSS_ID_GPS](#a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9)、[UBX_GNSS_ID_SBAS](#a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b)、[UBX_GNSS_ID_GALILEO](#a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe)、[UBX_GNSS_ID_BEIDOU](#a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7)、[UBX_GNSS_ID_QZSS](#a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103)、[UBX_GNSS_ID_GLONASS](#a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497)。

<a id="r_a260c4adbe9524bd747127a4e3f14bbca"></a>

```c
enum ubx_msg_id_ack { UBX_MSG_ID_ACK = 0x01 , UBX_MSG_ID_NAK = 0x00 }
```

相关声明：[ubx_msg_id_ack](#a260c4adbe9524bd747127a4e3f14bbca)、[UBX_MSG_ID_ACK](#a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511)、[UBX_MSG_ID_NAK](#a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469)。

<a id="r_a3cf04300758f1802e0703428707035d7"></a>

```c
enum ubx_msg_id_cfg { UBX_MSG_ID_CFG_PRT = 0x00 , UBX_MSG_ID_CFG_MSG = 0x01 , UBX_MSG_ID_CFG_RST = 0x04 , UBX_MSG_ID_CFG_RATE = 0x08 , UBX_MSG_ID_CFG_NAV5 = 0x24 , UBX_MSG_ID_CFG_VAL_SET = 0x8A , UBX_MSG_ID_CFG_VAL_GET = 0x8B }
```

相关声明：[ubx_msg_id_cfg](#a3cf04300758f1802e0703428707035d7)、[UBX_MSG_ID_CFG_PRT](#a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9)、[UBX_MSG_ID_CFG_MSG](#a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef)、[UBX_MSG_ID_CFG_RST](#a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453)、[UBX_MSG_ID_CFG_RATE](#a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26)、[UBX_MSG_ID_CFG_NAV5](#a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309)、[UBX_MSG_ID_CFG_VAL_SET](#a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3)、[UBX_MSG_ID_CFG_VAL_GET](#a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c)。

<a id="r_a0d969e434f941cf5af7143cca0cf0fe4"></a>

```c
enum ubx_msg_id_mon { UBX_MSG_ID_MON_VER = 0x04 , UBX_MSG_ID_MON_GNSS = 0x28 }
```

相关声明：[ubx_msg_id_mon](#a0d969e434f941cf5af7143cca0cf0fe4)、[UBX_MSG_ID_MON_VER](#a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0)、[UBX_MSG_ID_MON_GNSS](#a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888)。

<a id="r_adb6a6e16f193bc70840b2dd12dbc9baa"></a>

```c
enum ubx_cfg_port_id { UBX_CFG_PORT_ID_DDC = 0 , UBX_CFG_PORT_ID_UART = 1 , UBX_CFG_PORT_ID_USB = 2 , UBX_CFG_PORT_ID_SPI = 3 }
```

相关声明：[ubx_cfg_port_id](#adb6a6e16f193bc70840b2dd12dbc9baa)、[UBX_CFG_PORT_ID_DDC](#adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19)、[UBX_CFG_PORT_ID_UART](#adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb)、[UBX_CFG_PORT_ID_USB](#adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114)、[UBX_CFG_PORT_ID_SPI](#adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a)。

<a id="r_a887b1fa6af0d6d08cc51ed65de64a78a"></a>

```c
enum ubx_cfg_char_len { UBX_CFG_PRT_PORT_MODE_CHAR_LEN_5 = 0 , UBX_CFG_PRT_PORT_MODE_CHAR_LEN_6 = 1 , UBX_CFG_PRT_PORT_MODE_CHAR_LEN_7 = 2 , UBX_CFG_PRT_PORT_MODE_CHAR_LEN_8 = 3 }
```

相关声明：[ubx_cfg_char_len](#a887b1fa6af0d6d08cc51ed65de64a78a)、[UBX_CFG_PRT_PORT_MODE_CHAR_LEN_5](#a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83)、[UBX_CFG_PRT_PORT_MODE_CHAR_LEN_6](#a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac)、[UBX_CFG_PRT_PORT_MODE_CHAR_LEN_7](#a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca)、[UBX_CFG_PRT_PORT_MODE_CHAR_LEN_8](#a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d)。

<a id="r_a2e5de1479afbcf20caa3300282bb0d1a"></a>

```c
enum ubx_cfg_parity { UBX_CFG_PRT_PORT_MODE_PARITY_EVEN = 0 , UBX_CFG_PRT_PORT_MODE_PARITY_ODD = 1 , UBX_CFG_PRT_PORT_MODE_PARITY_NONE = 4 }
```

相关声明：[ubx_cfg_parity](#a2e5de1479afbcf20caa3300282bb0d1a)、[UBX_CFG_PRT_PORT_MODE_PARITY_EVEN](#a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68)、[UBX_CFG_PRT_PORT_MODE_PARITY_ODD](#a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac)、[UBX_CFG_PRT_PORT_MODE_PARITY_NONE](#a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385)。

<a id="r_a94709ee4f4afe0194790893251ee2b4c"></a>

```c
enum ubx_cfg_stop_bits { UBX_CFG_PRT_PORT_MODE_STOP_BITS_1 = 0 , UBX_CFG_PRT_PORT_MODE_STOP_BITS_1_5 = 1 , UBX_CFG_PRT_PORT_MODE_STOP_BITS_2 = 2 , UBX_CFG_PRT_PORT_MODE_STOP_BITS_0_5 = 3 }
```

相关声明：[ubx_cfg_stop_bits](#a94709ee4f4afe0194790893251ee2b4c)、[UBX_CFG_PRT_PORT_MODE_STOP_BITS_1](#a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9)、[UBX_CFG_PRT_PORT_MODE_STOP_BITS_1_5](#a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1)、[UBX_CFG_PRT_PORT_MODE_STOP_BITS_2](#a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f)、[UBX_CFG_PRT_PORT_MODE_STOP_BITS_0_5](#a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6)。

<a id="r_a9e5e9af7a281e53f2b950089ee66561f"></a>

```c
enum ubx_dyn_model { UBX_DYN_MODEL_PORTABLE = 0 , UBX_DYN_MODEL_STATIONARY = 2 , UBX_DYN_MODEL_PEDESTRIAN = 3 , UBX_DYN_MODEL_AUTOMOTIVE = 4 , UBX_DYN_MODEL_SEA = 5 , UBX_DYN_MODEL_AIRBORNE_1G = 6 , UBX_DYN_MODEL_AIRBORNE_2G = 7 , UBX_DYN_MODEL_AIRBORNE_4G = 8 , UBX_DYN_MODEL_WRIST = 9 , UBX_DYN_MODEL_BIKE = 10 }
```

相关声明：[ubx_dyn_model](#a9e5e9af7a281e53f2b950089ee66561f)、[UBX_DYN_MODEL_PORTABLE](#a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b)、[UBX_DYN_MODEL_STATIONARY](#a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7)、[UBX_DYN_MODEL_PEDESTRIAN](#a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6)、[UBX_DYN_MODEL_AUTOMOTIVE](#a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2)、[UBX_DYN_MODEL_SEA](#a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed)、[UBX_DYN_MODEL_AIRBORNE_1G](#a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476)、[UBX_DYN_MODEL_AIRBORNE_2G](#a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519)、[UBX_DYN_MODEL_AIRBORNE_4G](#a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d)、[UBX_DYN_MODEL_WRIST](#a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2)、[UBX_DYN_MODEL_BIKE](#a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25)。

<a id="r_a342c0d62cf874ccb8b657ce85d91efe0"></a>

```c
enum ubx_fix_mode { UBX_FIX_MODE_2D_ONLY = 1 , UBX_FIX_MODE_3D_ONLY = 2 , UBX_FIX_MODE_AUTO = 3 }
```

相关声明：[ubx_fix_mode](#a342c0d62cf874ccb8b657ce85d91efe0)、[UBX_FIX_MODE_2D_ONLY](#a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff)、[UBX_FIX_MODE_3D_ONLY](#a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6)、[UBX_FIX_MODE_AUTO](#a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617)。

<a id="r_a359b0f88d3769af43c2b1699eb172f23"></a>

```c
enum ubx_utc_standard { UBX_UTC_STANDARD_AUTOMATIC = 0 , UBX_UTC_STANDARD_GPS = 3 , UBX_UTC_STANDARD_GALILEO = 5 , UBX_UTC_STANDARD_GLONASS = 6 , UBX_UTC_STANDARD_BEIDOU = 7 }
```

相关声明：[ubx_utc_standard](#a359b0f88d3769af43c2b1699eb172f23)、[UBX_UTC_STANDARD_AUTOMATIC](#a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5)、[UBX_UTC_STANDARD_GPS](#a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c)、[UBX_UTC_STANDARD_GALILEO](#a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67)、[UBX_UTC_STANDARD_GLONASS](#a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80)、[UBX_UTC_STANDARD_BEIDOU](#a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8)。

<a id="r_a43766ad4c0fd1d31fd547c090e3f39b6"></a>

```c
enum ubx_cfg_rst_start_mode { UBX_CFG_RST_HOT_START = 0x0000 , UBX_CFG_RST_WARM_START = 0x0001 , UBX_CFG_RST_COLD_START = 0xFFFF }
```

相关声明：[ubx_cfg_rst_start_mode](#a43766ad4c0fd1d31fd547c090e3f39b6)、[UBX_CFG_RST_HOT_START](#a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7)、[UBX_CFG_RST_WARM_START](#a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95)、[UBX_CFG_RST_COLD_START](#a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896)。

<a id="r_a5cc2a8f42fd62032afa3cd7687452896"></a>

```c
enum ubx_cfg_rst_mode { UBX_CFG_RST_MODE_HW = 0x00 , UBX_CFG_RST_MODE_SW = 0x01 , UBX_CFG_RST_MODE_GNSS_STOP = 0x08 , UBX_CFG_RST_MODE_GNSS_START = 0x09 }
```

相关声明：[ubx_cfg_rst_mode](#a5cc2a8f42fd62032afa3cd7687452896)、[UBX_CFG_RST_MODE_HW](#a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e)、[UBX_CFG_RST_MODE_SW](#a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342)、[UBX_CFG_RST_MODE_GNSS_STOP](#a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265)、[UBX_CFG_RST_MODE_GNSS_START](#a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b)。

<a id="r_a621d2fae9721b6dc62a71801f3b7952e"></a>

```c
enum ubx_cfg_rate_time_ref { UBX_CFG_RATE_TIME_REF_UTC = 0 , UBX_CFG_RATE_TIME_REF_GPS = 1 , UBX_CFG_RATE_TIME_REF_GLONASS = 2 , UBX_CFG_RATE_TIME_REF_BEIDOU = 3 , UBX_CFG_RATE_TIME_REF_GALILEO = 4 , UBX_CFG_RATE_TIME_REF_NAVIC = 5 }
```

相关声明：[ubx_cfg_rate_time_ref](#a621d2fae9721b6dc62a71801f3b7952e)、[UBX_CFG_RATE_TIME_REF_UTC](#a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea)、[UBX_CFG_RATE_TIME_REF_GPS](#a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e)、[UBX_CFG_RATE_TIME_REF_GLONASS](#a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8)、[UBX_CFG_RATE_TIME_REF_BEIDOU](#a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8)、[UBX_CFG_RATE_TIME_REF_GALILEO](#a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16)、[UBX_CFG_RATE_TIME_REF_NAVIC](#a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce)。

<a id="r_ad7e0ffe55e8dbd97caa5bc089d33540c"></a>

```c
enum ubx_cfg_val_ver { UBX_CFG_VAL_VER_SIMPLE = 0 , UBX_CFG_VAL_VER_TRANSACTION = 1 }
```

相关声明：[ubx_cfg_val_ver](#ad7e0ffe55e8dbd97caa5bc089d33540c)、[UBX_CFG_VAL_VER_SIMPLE](#ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b)、[UBX_CFG_VAL_VER_TRANSACTION](#ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab)。

<a id="r_aa221b68c53f25634d9f2f435f28c1a6c"></a>

```c
enum ubx_msg_id_nmea_std { UBX_MSG_ID_NMEA_STD_DTM = 0x0A , UBX_MSG_ID_NMEA_STD_GBQ = 0x44 , UBX_MSG_ID_NMEA_STD_GBS = 0x09 , UBX_MSG_ID_NMEA_STD_GGA = 0x00 , UBX_MSG_ID_NMEA_STD_GLL = 0x01 , UBX_MSG_ID_NMEA_STD_GLQ = 0x43 , UBX_MSG_ID_NMEA_STD_GNQ = 0x42 , UBX_MSG_ID_NMEA_STD_GNS = 0x0D , UBX_MSG_ID_NMEA_STD_GPQ = 0x40 , UBX_MSG_ID_NMEA_STD_GRS = 0x06 , UBX_MSG_ID_NMEA_STD_GSA = 0x02 , UBX_MSG_ID_NMEA_STD_GST = 0x07 , UBX_MSG_ID_NMEA_STD_GSV = 0x03 , UBX_MSG_ID_NMEA_STD_RMC = 0x04 , UBX_MSG_ID_NMEA_STD_THS = 0x0E , UBX_MSG_ID_NMEA_STD_TXT = 0x41 , UBX_MSG_ID_NMEA_STD_VLW = 0x0F , UBX_MSG_ID_NMEA_STD_VTG = 0x05 , UBX_MSG_ID_NMEA_STD_ZDA = 0x08 }
```

相关声明：[ubx_msg_id_nmea_std](#aa221b68c53f25634d9f2f435f28c1a6c)、[UBX_MSG_ID_NMEA_STD_DTM](#aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad)、[UBX_MSG_ID_NMEA_STD_GBQ](#aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774)、[UBX_MSG_ID_NMEA_STD_GBS](#aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac)、[UBX_MSG_ID_NMEA_STD_GGA](#aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7)、[UBX_MSG_ID_NMEA_STD_GLL](#aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932)、[UBX_MSG_ID_NMEA_STD_GLQ](#aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961)、[UBX_MSG_ID_NMEA_STD_GNQ](#aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77)、[UBX_MSG_ID_NMEA_STD_GNS](#aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191)、[UBX_MSG_ID_NMEA_STD_GPQ](#aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781)、[UBX_MSG_ID_NMEA_STD_GRS](#aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853)、[UBX_MSG_ID_NMEA_STD_GSA](#aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d)、[UBX_MSG_ID_NMEA_STD_GST](#aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6)、[UBX_MSG_ID_NMEA_STD_GSV](#aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03)、[UBX_MSG_ID_NMEA_STD_RMC](#aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3)、[UBX_MSG_ID_NMEA_STD_THS](#aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37)、[UBX_MSG_ID_NMEA_STD_TXT](#aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e)、[UBX_MSG_ID_NMEA_STD_VLW](#aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904)、[UBX_MSG_ID_NMEA_STD_VTG](#aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b)、[UBX_MSG_ID_NMEA_STD_ZDA](#aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27)。

<a id="r_a58dc8b84784731500aa7f55afeb7e582"></a>

```c
enum ubx_msg_id_nmea_pubx { UBX_MSG_ID_NMEA_PUBX_CONFIG = 0x41 , UBX_MSG_ID_NMEA_PUBX_POSITION = 0x00 , UBX_MSG_ID_NMEA_PUBX_RATE = 0x40 , UBX_MSG_ID_NMEA_PUBX_SVSTATUS = 0x03 , UBX_MSG_ID_NMEA_PUBX_TIME = 0x04 }
```

相关声明：[ubx_msg_id_nmea_pubx](#a58dc8b84784731500aa7f55afeb7e582)、[UBX_MSG_ID_NMEA_PUBX_CONFIG](#a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57)、[UBX_MSG_ID_NMEA_PUBX_POSITION](#a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6)、[UBX_MSG_ID_NMEA_PUBX_RATE](#a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667)、[UBX_MSG_ID_NMEA_PUBX_SVSTATUS](#a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a)、[UBX_MSG_ID_NMEA_PUBX_TIME](#a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 71.4\_函数（Functions）

<a id="r_a450f46250ef486af4f933e69ddbb42d2"></a>

```c
static uint16_t ubx_calc_checksum (const struct ubx_frame *frame, size_t len)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[ubx_calc_checksum](#a450f46250ef486af4f933e69ddbb42d2)、[ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)。

<a id="r_acdc0d9b7d25df6aba6bb091e7034f5ba"></a>

```c
static int ubx_frame_encode (uint8_t class, uint8_t id, const uint8_t *payload, size_t payload_len, uint8_t *buf, size_t buf_len)
```

相关声明：[ubx_frame_encode](#acdc0d9b7d25df6aba6bb091e7034f5ba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 71.5\_详细说明（Detailed Documentation）

<a id="adcfe7daa815d7a1a7dea67642b88ebbf"></a>

### `UBX_CFG_NAV5_APPLY_DYN`

```c
#define UBX_CFG_NAV5_APPLY_DYN BIT(0)
```

<a id="a93b02f16b10968f47932c502e300c5a6"></a>

### `UBX_CFG_NAV5_APPLY_FIX_MODE`

```c
#define UBX_CFG_NAV5_APPLY_FIX_MODE BIT(2)
```

<a id="a0eb35bbe06a126aa8aed1738b6dd56c2"></a>

### `UBX_CFG_PRT_MODE_CHAR_LEN`

```c
#define UBX_CFG_PRT_MODE_CHAR_LEN ( val)
```

展开值（Value）：

```c
(((val) & BIT_MASK(2)) << 6)
```

<a id="abe8dd1db5cf126f76f7a44f4715e9cfa"></a>

### `UBX_CFG_PRT_MODE_PARITY`

```c
#define UBX_CFG_PRT_MODE_PARITY ( val)
```

展开值（Value）：

```c
(((val) & BIT_MASK(3)) << 9)
```

<a id="a23d980439eed2fe310c8be5107333489"></a>

### `UBX_CFG_PRT_MODE_STOP_BITS`

```c
#define UBX_CFG_PRT_MODE_STOP_BITS ( val)
```

展开值（Value）：

```c
(((val) & BIT_MASK(2)) << 12)
```

<a id="a174c408931fd4ca3e6c8128dd540d2dd"></a>

### `UBX_CFG_PRT_PROTO_MASK_NMEA`

```c
#define UBX_CFG_PRT_PROTO_MASK_NMEA BIT(1)
```

<a id="ad481e57bb7b8707c468990ad0568d53c"></a>

### `UBX_CFG_PRT_PROTO_MASK_RTCM3`

```c
#define UBX_CFG_PRT_PROTO_MASK_RTCM3 BIT(5)
```

<a id="a3f8c1064b9f51778df32e0b713302a2e"></a>

### `UBX_CFG_PRT_PROTO_MASK_UBX`

```c
#define UBX_CFG_PRT_PROTO_MASK_UBX BIT(0)
```

<a id="a8cf6388d5ee4509e36742e30dc640889"></a>

### `UBX_FRAME_ACK_INITIALIZER`

```c
#define UBX_FRAME_ACK_INITIALIZER ( _class_id, _msg_id )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_ACK, UBX_MSG_ID_ACK, _class_id, _msg_id)
```

<a id="aca7cb6846e6d01cc84df655f22832987"></a>

### `UBX_FRAME_ARRAY_DEFINE`

```c
#define UBX_FRAME_ARRAY_DEFINE ( _name, ... )
```

展开值（Value）：

```c
const struct ubx_frame *_name[] = {__VA_ARGS__};
```

<a id="af9ce35b33de7f9ebc68d11731beb02f0"></a>

### `UBX_FRAME_CFG_MSG_RATE_INITIALIZER`

```c
#define UBX_FRAME_CFG_MSG_RATE_INITIALIZER ( _class_id, _msg_id, _rate )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_MSG,                        \
                              _class_id, _msg_id, _rate)
```

<a id="a3192675717120efc97a8858605b3f45d"></a>

### `UBX_FRAME_CFG_RATE_INITIALIZER`

```c
#define UBX_FRAME_CFG_RATE_INITIALIZER ( _meas_rate_ms, _nav_rate, _time_ref )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_RATE,                       \
                              (_meas_rate_ms & 0xFF), ((_meas_rate_ms >> 8) & 0xFF),       \
                              (_nav_rate & 0xFF), ((_nav_rate >> 8) & 0xFF),               \
                              (_time_ref & 0xFF), ((_time_ref >> 8) & 0xFF))
```

<a id="aed21b263c25f39d499b37dfff38bca39"></a>

### `UBX_FRAME_CFG_RST_INITIALIZER`

```c
#define UBX_FRAME_CFG_RST_INITIALIZER ( _start_mode, _reset_mode )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_RST,                        \
                              (_start_mode & 0xFF), ((_start_mode >> 8) & 0xFF),           \
                               _reset_mode, 0)
```

<a id="a1d7a930de22dadce2aae88e64e246dd9"></a>

### `UBX_FRAME_CFG_VAL_GET_INITIALIZER`

```c
#define UBX_FRAME_CFG_VAL_GET_INITIALIZER ( _key)
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_GET,                    \
                              0x00, 0x00, 0x00, 0x00,                                      \
                              ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                              (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF))
```

<a id="a66b9664185ed9cfb096df2b375e41f0e"></a>

### `UBX_FRAME_CFG_VAL_SET_U16_INITIALIZER`

```c
#define UBX_FRAME_CFG_VAL_SET_U16_INITIALIZER ( _key, _value )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                              0x00, 0x01, 0x00, 0x00,                                      \
                              ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                              (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                              ((_value) & 0xFF), (((_value) >> 8) & 0xFF))
```

<a id="a997cd3bd57d5cfc6c4f1eeca2bc6ba37"></a>

### `UBX_FRAME_CFG_VAL_SET_U32_INITIALIZER`

```c
#define UBX_FRAME_CFG_VAL_SET_U32_INITIALIZER ( _key, _value )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                              0x00, 0x01, 0x00, 0x00,                                      \
                              ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                              (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                              ((_value) & 0xFF), (((_value) >> 8) & 0xFF),                 \
                              (((_value) >> 16) & 0xFF), (((_value) >> 24) & 0xFF))
```

<a id="a5b4484d44a25068f960f7f1196cffe89"></a>

### `UBX_FRAME_CFG_VAL_SET_U8_INITIALIZER`

```c
#define UBX_FRAME_CFG_VAL_SET_U8_INITIALIZER ( _key, _value )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_CFG, UBX_MSG_ID_CFG_VAL_SET,                    \
                              0x00, 0x01, 0x00, 0x00,                                      \
                              ((_key) & 0xFF), (((_key) >> 8) & 0xFF),                     \
                              (((_key) >> 16) & 0xFF), (((_key) >> 24) & 0xFF),            \
                              ((_value) & 0xFF))
```

<a id="ad79a0ce05086ada71822ccb9100bc100"></a>

### `UBX_FRAME_DEFINE`

```c
#define UBX_FRAME_DEFINE ( _name, _frame )
```

展开值（Value）：

```c
const static struct ubx_frame _name = _frame
```

<a id="aa0392f4a081c1077b4f235a757431aee"></a>

### `UBX_FRAME_FOOTER_SZ`

```c
#define UBX_FRAME_FOOTER_SZ 2
```

<a id="a1cf8842293fe70f3ea22686a55d9beda"></a>

### `UBX_FRAME_GET_INITIALIZER`

```c
#define UBX_FRAME_GET_INITIALIZER ( _class_id, _msg_id )
```

展开值（Value）：

```c
{                                                                                          \
        .preamble_sync_char_1 = UBX_PREAMBLE_SYNC_CHAR_1,                                  \
        .preamble_sync_char_2 = UBX_PREAMBLE_SYNC_CHAR_2,                                  \
        .class = _class_id,                                                                \
        .id = _msg_id,                                                                     \
        .payload_size = 0,                                                                 \
        .payload_and_checksum = {                                                          \
                UBX_CSUM(_class_id, _msg_id, 0, 0),                                        \
        },                                                                                 \
}
```

<a id="a1342f8e944fcd9f45fe94eef9bda307c"></a>

### `UBX_FRAME_HEADER_SZ`

```c
#define UBX_FRAME_HEADER_SZ 6
```

<a id="a4d90346d76d003aeddf16fc665203926"></a>

### `UBX_FRAME_INITIALIZER_PAYLOAD`

```c
#define UBX_FRAME_INITIALIZER_PAYLOAD ( _class_id, _msg_id, ... )
```

展开值（Value）：

```c
_UBX_FRAME_INITIALIZER_PAYLOAD(_class_id, _msg_id, __VA_ARGS__)
```

<a id="a2c667ef9bb2d12effb251f4df6827c73"></a>

### `UBX_FRAME_MSG_CLASS_IDX`

```c
#define UBX_FRAME_MSG_CLASS_IDX 2
```

<a id="a5b5ffd92f5894fc966b1875c7ce4c1a3"></a>

### `UBX_FRAME_NAK_INITIALIZER`

```c
#define UBX_FRAME_NAK_INITIALIZER ( _class_id, _msg_id )
```

展开值（Value）：

```c
UBX_FRAME_INITIALIZER_PAYLOAD(UBX_CLASS_ID_ACK, UBX_MSG_ID_NAK, _class_id, _msg_id)
```

<a id="a1b417ed30e090d3399f96c87dfe842c4"></a>

### `UBX_FRAME_PREAMBLE_SYNC_CHAR_1_IDX`

```c
#define UBX_FRAME_PREAMBLE_SYNC_CHAR_1_IDX 0
```

<a id="af940bf4cc68adff5b8b187dcf1e93735"></a>

### `UBX_FRAME_PREAMBLE_SYNC_CHAR_2_IDX`

```c
#define UBX_FRAME_PREAMBLE_SYNC_CHAR_2_IDX 1
```

<a id="a4c64b9118da471baa6a7a88ee345bf66"></a>

### `UBX_FRAME_SZ`

```c
#define UBX_FRAME_SZ ( payload_size)
```

展开值（Value）：

```c
(payload_size + UBX_FRAME_SZ_WITHOUT_PAYLOAD)
```

<a id="a1cab11988642144cfcc6c7309f5806d0"></a>

### `UBX_FRAME_SZ_MAX`

```c
#define UBX_FRAME_SZ_MAX UBX_FRAME_SZ(UBX_PAYLOAD_SZ_MAX)
```

<a id="a8e1aded66fd229f071c9d5e060a001a6"></a>

### `UBX_FRAME_SZ_WITHOUT_PAYLOAD`

```c
#define UBX_FRAME_SZ_WITHOUT_PAYLOAD (UBX_FRAME_HEADER_SZ + UBX_FRAME_FOOTER_SZ)
```

<a id="ad57613b25d1716b7ca3e01d37b64a16d"></a>

### `UBX_GNSS_SELECTION_BEIDOU`

```c
#define UBX_GNSS_SELECTION_BEIDOU BIT(2)
```

<a id="aa338a732341e0e1560a749123cecd700"></a>

### `UBX_GNSS_SELECTION_GALILEO`

```c
#define UBX_GNSS_SELECTION_GALILEO BIT(3)
```

<a id="ab767685719aa08364b5e77262fae232a"></a>

### `UBX_GNSS_SELECTION_GLONASS`

```c
#define UBX_GNSS_SELECTION_GLONASS BIT(1)
```

<a id="ae23528d7cc5a34a48f062a084ae2dbd0"></a>

### `UBX_GNSS_SELECTION_GPS`

```c
#define UBX_GNSS_SELECTION_GPS BIT(0)
```

<a id="ac348d618c31a5ae7b243243267b041c6"></a>

### `UBX_NAV_PVT_FLAGS3_INVALID_LLH`

```c
#define UBX_NAV_PVT_FLAGS3_INVALID_LLH BIT(0)
```

<a id="a395c3edfbf84edc09f7af09d0a8b48c0"></a>

### `UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FIXED`

```c
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FIXED BIT(7)
```

<a id="a6318967f82a82af78715635fc7592ce6"></a>

### `UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FLOATING`

```c
#define UBX_NAV_PVT_FLAGS_GNSS_CARR_SOLN_FLOATING BIT(6)
```

<a id="af79a6a074065fb7d792109b4d99ba32f"></a>

### `UBX_NAV_PVT_FLAGS_GNSS_FIX_OK`

```c
#define UBX_NAV_PVT_FLAGS_GNSS_FIX_OK BIT(0)
```

<a id="ae9c98287cbaf17e7fc1beaedc1679fa4"></a>

### `UBX_NAV_PVT_VALID_DATE`

```c
#define UBX_NAV_PVT_VALID_DATE BIT(0)
```

<a id="a1f067fe87ff51b4b59e7bfce2c4b9880"></a>

### `UBX_NAV_PVT_VALID_MAGN`

```c
#define UBX_NAV_PVT_VALID_MAGN BIT(3)
```

<a id="a583269f4c0ea39e43671fd9267b129af"></a>

### `UBX_NAV_PVT_VALID_TIME`

```c
#define UBX_NAV_PVT_VALID_TIME BIT(1)
```

<a id="a4ea40193fa60a75bf5ede5586da92931"></a>

### `UBX_NAV_PVT_VALID_UTC_TOD`

```c
#define UBX_NAV_PVT_VALID_UTC_TOD BIT(2)
```

<a id="a8c665bbb309e589b8bd88268b802a3eb"></a>

### `UBX_NAV_SAT_FLAGS_RTCM_CORR_USED`

```c
#define UBX_NAV_SAT_FLAGS_RTCM_CORR_USED BIT(17)
```

<a id="aaaa4b2e1968a45f4c7ee336a45b4164b"></a>

### `UBX_NAV_SAT_FLAGS_SV_USED`

```c
#define UBX_NAV_SAT_FLAGS_SV_USED BIT(3)
```

<a id="a9c66cd27732153c56d0872339bc3deae"></a>

### `UBX_PAYLOAD_SZ_MAX`

```c
#define UBX_PAYLOAD_SZ_MAX 512
```

<a id="a1693f3584605a0197076cba71c79b0df"></a>

### `UBX_PREAMBLE_SYNC_CHAR_1`

```c
#define UBX_PREAMBLE_SYNC_CHAR_1 0xB5
```

<a id="ad8d6229db563db619d4f0a9f225fb640"></a>

### `UBX_PREAMBLE_SYNC_CHAR_2`

```c
#define UBX_PREAMBLE_SYNC_CHAR_2 0x62
```

<a id="a887b1fa6af0d6d08cc51ed65de64a78a"></a>

### `ubx_cfg_char_len`

```c
enum ubx_cfg_char_len
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_PRT_PORT_MODE_CHAR_LEN_5` |  |
| `UBX_CFG_PRT_PORT_MODE_CHAR_LEN_6` |  |
| `UBX_CFG_PRT_PORT_MODE_CHAR_LEN_7` |  |
| `UBX_CFG_PRT_PORT_MODE_CHAR_LEN_8` |  |

<a id="a2e5de1479afbcf20caa3300282bb0d1a"></a>

### `ubx_cfg_parity`

```c
enum ubx_cfg_parity
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_PRT_PORT_MODE_PARITY_EVEN` |  |
| `UBX_CFG_PRT_PORT_MODE_PARITY_ODD` |  |
| `UBX_CFG_PRT_PORT_MODE_PARITY_NONE` |  |

<a id="adb6a6e16f193bc70840b2dd12dbc9baa"></a>

### `ubx_cfg_port_id`

```c
enum ubx_cfg_port_id
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_PORT_ID_DDC` |  |
| `UBX_CFG_PORT_ID_UART` |  |
| `UBX_CFG_PORT_ID_USB` |  |
| `UBX_CFG_PORT_ID_SPI` |  |

<a id="a621d2fae9721b6dc62a71801f3b7952e"></a>

### `ubx_cfg_rate_time_ref`

```c
enum ubx_cfg_rate_time_ref
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_RATE_TIME_REF_UTC` |  |
| `UBX_CFG_RATE_TIME_REF_GPS` |  |
| `UBX_CFG_RATE_TIME_REF_GLONASS` |  |
| `UBX_CFG_RATE_TIME_REF_BEIDOU` |  |
| `UBX_CFG_RATE_TIME_REF_GALILEO` |  |
| `UBX_CFG_RATE_TIME_REF_NAVIC` |  |

<a id="a5cc2a8f42fd62032afa3cd7687452896"></a>

### `ubx_cfg_rst_mode`

```c
enum ubx_cfg_rst_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_RST_MODE_HW` |  |
| `UBX_CFG_RST_MODE_SW` |  |
| `UBX_CFG_RST_MODE_GNSS_STOP` |  |
| `UBX_CFG_RST_MODE_GNSS_START` |  |

<a id="a43766ad4c0fd1d31fd547c090e3f39b6"></a>

### `ubx_cfg_rst_start_mode`

```c
enum ubx_cfg_rst_start_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_RST_HOT_START` |  |
| `UBX_CFG_RST_WARM_START` |  |
| `UBX_CFG_RST_COLD_START` |  |

<a id="a94709ee4f4afe0194790893251ee2b4c"></a>

### `ubx_cfg_stop_bits`

```c
enum ubx_cfg_stop_bits
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_PRT_PORT_MODE_STOP_BITS_1` |  |
| `UBX_CFG_PRT_PORT_MODE_STOP_BITS_1_5` |  |
| `UBX_CFG_PRT_PORT_MODE_STOP_BITS_2` |  |
| `UBX_CFG_PRT_PORT_MODE_STOP_BITS_0_5` |  |

<a id="ad7e0ffe55e8dbd97caa5bc089d33540c"></a>

### `ubx_cfg_val_ver`

```c
enum ubx_cfg_val_ver
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CFG_VAL_VER_SIMPLE` |  |
| `UBX_CFG_VAL_VER_TRANSACTION` |  |

<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18"></a>

### `ubx_class_id`

```c
enum ubx_class_id
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_CLASS_ID_NAV` |  |
| `UBX_CLASS_ID_RXM` |  |
| `UBX_CLASS_ID_INF` |  |
| `UBX_CLASS_ID_ACK` |  |
| `UBX_CLASS_ID_CFG` |  |
| `UBX_CLASS_ID_UPD` |  |
| `UBX_CLASS_ID_MON` |  |
| `UBX_CLASS_ID_TIM` |  |
| `UBX_CLASS_ID_MGA` |  |
| `UBX_CLASS_ID_LOG` |  |
| `UBX_CLASS_ID_SEC` |  |
| `UBX_CLASS_ID_NMEA_STD` |  |
| `UBX_CLASS_ID_NMEA_PUBX` |  |

<a id="a9e5e9af7a281e53f2b950089ee66561f"></a>

### `ubx_dyn_model`

```c
enum ubx_dyn_model
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_DYN_MODEL_PORTABLE` |  |
| `UBX_DYN_MODEL_STATIONARY` |  |
| `UBX_DYN_MODEL_PEDESTRIAN` |  |
| `UBX_DYN_MODEL_AUTOMOTIVE` |  |
| `UBX_DYN_MODEL_SEA` |  |
| `UBX_DYN_MODEL_AIRBORNE_1G` |  |
| `UBX_DYN_MODEL_AIRBORNE_2G` |  |
| `UBX_DYN_MODEL_AIRBORNE_4G` |  |
| `UBX_DYN_MODEL_WRIST` |  |
| `UBX_DYN_MODEL_BIKE` |  |

<a id="a342c0d62cf874ccb8b657ce85d91efe0"></a>

### `ubx_fix_mode`

```c
enum ubx_fix_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_FIX_MODE_2D_ONLY` |  |
| `UBX_FIX_MODE_3D_ONLY` |  |
| `UBX_FIX_MODE_AUTO` |  |

<a id="a6711a33292bf25327950406b96585690"></a>

### `ubx_gnss_id`

```c
enum ubx_gnss_id
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_GNSS_ID_GPS` |  |
| `UBX_GNSS_ID_SBAS` |  |
| `UBX_GNSS_ID_GALILEO` |  |
| `UBX_GNSS_ID_BEIDOU` |  |
| `UBX_GNSS_ID_QZSS` |  |
| `UBX_GNSS_ID_GLONASS` |  |

<a id="a260c4adbe9524bd747127a4e3f14bbca"></a>

### `ubx_msg_id_ack`

```c
enum ubx_msg_id_ack
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_ACK` |  |
| `UBX_MSG_ID_NAK` |  |

<a id="a3cf04300758f1802e0703428707035d7"></a>

### `ubx_msg_id_cfg`

```c
enum ubx_msg_id_cfg
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_CFG_PRT` |  |
| `UBX_MSG_ID_CFG_MSG` |  |
| `UBX_MSG_ID_CFG_RST` |  |
| `UBX_MSG_ID_CFG_RATE` |  |
| `UBX_MSG_ID_CFG_NAV5` |  |
| `UBX_MSG_ID_CFG_VAL_SET` |  |
| `UBX_MSG_ID_CFG_VAL_GET` |  |

<a id="a0d969e434f941cf5af7143cca0cf0fe4"></a>

### `ubx_msg_id_mon`

```c
enum ubx_msg_id_mon
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_MON_VER` |  |
| `UBX_MSG_ID_MON_GNSS` |  |

<a id="a8a935ea7debb4ac73ea99c98d6ef4d3b"></a>

### `ubx_msg_id_nav`

```c
enum ubx_msg_id_nav
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_NAV_PVT` |  |
| `UBX_MSG_ID_NAV_SAT` |  |

<a id="a58dc8b84784731500aa7f55afeb7e582"></a>

### `ubx_msg_id_nmea_pubx`

```c
enum ubx_msg_id_nmea_pubx
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_NMEA_PUBX_CONFIG` |  |
| `UBX_MSG_ID_NMEA_PUBX_POSITION` |  |
| `UBX_MSG_ID_NMEA_PUBX_RATE` |  |
| `UBX_MSG_ID_NMEA_PUBX_SVSTATUS` |  |
| `UBX_MSG_ID_NMEA_PUBX_TIME` |  |

<a id="aa221b68c53f25634d9f2f435f28c1a6c"></a>

### `ubx_msg_id_nmea_std`

```c
enum ubx_msg_id_nmea_std
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_MSG_ID_NMEA_STD_DTM` |  |
| `UBX_MSG_ID_NMEA_STD_GBQ` |  |
| `UBX_MSG_ID_NMEA_STD_GBS` |  |
| `UBX_MSG_ID_NMEA_STD_GGA` |  |
| `UBX_MSG_ID_NMEA_STD_GLL` |  |
| `UBX_MSG_ID_NMEA_STD_GLQ` |  |
| `UBX_MSG_ID_NMEA_STD_GNQ` |  |
| `UBX_MSG_ID_NMEA_STD_GNS` |  |
| `UBX_MSG_ID_NMEA_STD_GPQ` |  |
| `UBX_MSG_ID_NMEA_STD_GRS` |  |
| `UBX_MSG_ID_NMEA_STD_GSA` |  |
| `UBX_MSG_ID_NMEA_STD_GST` |  |
| `UBX_MSG_ID_NMEA_STD_GSV` |  |
| `UBX_MSG_ID_NMEA_STD_RMC` |  |
| `UBX_MSG_ID_NMEA_STD_THS` |  |
| `UBX_MSG_ID_NMEA_STD_TXT` |  |
| `UBX_MSG_ID_NMEA_STD_VLW` |  |
| `UBX_MSG_ID_NMEA_STD_VTG` |  |
| `UBX_MSG_ID_NMEA_STD_ZDA` |  |

<a id="a173b6c1016562da43b8131b8d8f04fef"></a>

### `ubx_nav_fix_type`

```c
enum ubx_nav_fix_type
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_NAV_FIX_TYPE_NO_FIX` |  |
| `UBX_NAV_FIX_TYPE_DR` |  |
| `UBX_NAV_FIX_TYPE_2D` |  |
| `UBX_NAV_FIX_TYPE_3D` |  |
| `UBX_NAV_FIX_TYPE_GNSS_DR_COMBINED` |  |
| `UBX_NAV_FIX_TYPE_TIME_ONLY` |  |

<a id="a3384ec6c907acb911c4a9c32bcd473ca"></a>

### `ubx_nav_hp_dgnss_mode`

```c
enum ubx_nav_hp_dgnss_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_NAV_HP_DGNSS_MODE_RTK_FLOAT` |  |
| `UBX_NAV_HP_DGNSS_MODE_RTK_FIXED` |  |

<a id="afbba8ada09d6c6489d52a3b9dc31725f"></a>

### `ubx_nav_sat_health`

```c
enum ubx_nav_sat_health
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_NAV_SAT_HEALTH_UNKNOWN` |  |
| `UBX_NAV_SAT_HEALTH_HEALTHY` |  |
| `UBX_NAV_SAT_HEALTH_UNHEALTHY` |  |

<a id="a359b0f88d3769af43c2b1699eb172f23"></a>

### `ubx_utc_standard`

```c
enum ubx_utc_standard
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UBX_UTC_STANDARD_AUTOMATIC` |  |
| `UBX_UTC_STANDARD_GPS` |  |
| `UBX_UTC_STANDARD_GALILEO` |  |
| `UBX_UTC_STANDARD_GLONASS` |  |
| `UBX_UTC_STANDARD_BEIDOU` |  |

<a id="a450f46250ef486af4f933e69ddbb42d2"></a>

### `ubx_calc_checksum()`

```c
uint16_t ubx_calc_checksum ( const struct ubx_frame * frame, size_t len )
```

声明属性：`inline`、`static`。

预期长度（Expected Length）与实际长度（Actual Length）不匹配会导致帧无效（Invalid Frame）。

<a id="acdc0d9b7d25df6aba6bb091e7034f5ba"></a>

### `ubx_frame_encode()`

```c
int ubx_frame_encode ( uint8_t class, uint8_t id, const uint8_t * payload, size_t payload_len, uint8_t * buf, size_t buf_len )
```

声明属性：`inline`、`static`。


## 71.6\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/modem/ubx/checksum.h](../checksum_reference/P003_UBX校验和头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)
- [ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)
- [ubx_nav_pvt](../sensor_navigation_model_reference/P070_ubx_nav_pvt_结构体.md)
- [ubx_nav_sat](../sensor_navigation_model_reference/P071_ubx_nav_sat_结构体.md)
- [ubx_nav_sat::ubx_nav_sat_info](../sensor_navigation_model_reference/P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)
- [ubx_ack](../sensor_navigation_model_reference/P056_ubx_ack_结构体.md)
- [ubx_mon_gnss](../sensor_navigation_model_reference/P068_ubx_mon_gnss_结构体.md)
- [ubx_cfg_prt](../sensor_navigation_model_reference/P059_ubx_cfg_prt_结构体.md)
- [ubx_cfg_nav5](../sensor_navigation_model_reference/P058_ubx_cfg_nav5_结构体.md)
- [ubx_cfg_rst](../sensor_navigation_model_reference/P061_ubx_cfg_rst_结构体.md)
- [ubx_cfg_rate](../sensor_navigation_model_reference/P060_ubx_cfg_rate_结构体.md)
- [ubx_cfg_val_hdr](../sensor_navigation_model_reference/P062_ubx_cfg_val_hdr_结构体.md)
- [ubx_cfg_val_u8](../sensor_navigation_model_reference/P065_ubx_cfg_val_u8_结构体.md)
- [ubx_cfg_val_u16](../sensor_navigation_model_reference/P063_ubx_cfg_val_u16_结构体.md)
- [ubx_cfg_val_u32](../sensor_navigation_model_reference/P064_ubx_cfg_val_u32_结构体.md)
- [ubx_cfg_msg_rate](../sensor_navigation_model_reference/P057_ubx_cfg_msg_rate_结构体.md)
- [ubx_mon_ver](../sensor_navigation_model_reference/P069_ubx_mon_ver_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="amodem_2ubx_2protocol_8h_html_a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511"></a>
<a id="amodem_2ubx_2protocol_8h_html_a4d90346d76d003aeddf16fc665203926"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b"></a>
<a id="astructubx__frame_html"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c"></a>
<a id="amodem_2ubx_2protocol_8h_html_a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3"></a>
<a id="amodem_2ubx_2protocol_8h_html_a1693f3584605a0197076cba71c79b0df"></a>
<a id="amodem_2ubx_2protocol_8h_html_ad8d6229db563db619d4f0a9f225fb640"></a>
<a id="amodem_2ubx_2protocol_8h_html_a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469"></a>
<a id="amodem_2ubx_2protocol_8h_html_a8e1aded66fd229f071c9d5e060a001a6"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a887b1fa6af0d6d08cc51ed65de64a78aa019364b4a4482098acc0d7821b456b83"></a>
<a id="a887b1fa6af0d6d08cc51ed65de64a78aaeea043882f976e34008f261e1b2ee5ac"></a>
<a id="a887b1fa6af0d6d08cc51ed65de64a78aaeacece1ca309918fa3abe7a02911f5ca"></a>
<a id="a887b1fa6af0d6d08cc51ed65de64a78aae7769c1dd298aabbad37ddaf6260eb4d"></a>
<a id="a2e5de1479afbcf20caa3300282bb0d1aa1ef24c67f4e90f7c6fb011ec433ebb68"></a>
<a id="a2e5de1479afbcf20caa3300282bb0d1aa5db544370f64f19224e9243eae0942ac"></a>
<a id="a2e5de1479afbcf20caa3300282bb0d1aa46b4ba80de7ca4c9d1ea403dd6efb385"></a>
<a id="adb6a6e16f193bc70840b2dd12dbc9baaa5c7c1a24670995305bcb8e98cfd1fa19"></a>
<a id="adb6a6e16f193bc70840b2dd12dbc9baaaccb591a437d0ed7cca8888f41b855efb"></a>
<a id="adb6a6e16f193bc70840b2dd12dbc9baaa3af5f6c24fade976d4ece339e9240114"></a>
<a id="adb6a6e16f193bc70840b2dd12dbc9baaaa0ee1de6e26bb0585f24fddbe3d7ec9a"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952eacc3989fab9e22270c389b0318bbe45ea"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952ea7a2d00bdb7fef5ff7da1d3a682a1b82e"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952ea519dc8f11c80b5a08771fbc36c70fbb8"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952ea30f66599c483f622607f0b13ad0451f8"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952eab7ed326b5da1087afb8d531d97bb9f16"></a>
<a id="a621d2fae9721b6dc62a71801f3b7952ea5be3c906a6c528f65575990041b7e6ce"></a>
<a id="a5cc2a8f42fd62032afa3cd7687452896ac02d28b95ef601af32dc898e35ad252e"></a>
<a id="a5cc2a8f42fd62032afa3cd7687452896a7fd6f4b7557dfa6511dcb6354963d342"></a>
<a id="a5cc2a8f42fd62032afa3cd7687452896a0e9177345e82ad614c1ab4c8b52b9265"></a>
<a id="a5cc2a8f42fd62032afa3cd7687452896aca25f86cc1d85c60b1d67509d0e9506b"></a>
<a id="a43766ad4c0fd1d31fd547c090e3f39b6a67b9cba109cc8f57a38c41b1d521e3c7"></a>
<a id="a43766ad4c0fd1d31fd547c090e3f39b6a1621ed3281429f96fc598d90cc388c95"></a>
<a id="a43766ad4c0fd1d31fd547c090e3f39b6aaef8449ed29d6dd76bdd34157d873896"></a>
<a id="a94709ee4f4afe0194790893251ee2b4caf762dc50babaacd4cbb1ce753a8c0ae9"></a>
<a id="a94709ee4f4afe0194790893251ee2b4ca06c8d5338db83ce4a74a92228f04ffb1"></a>
<a id="a94709ee4f4afe0194790893251ee2b4caea0ef9695c70807a5bdfb1725f31ea3f"></a>
<a id="a94709ee4f4afe0194790893251ee2b4ca461834aa0d5d6ddec370ecd247e330e6"></a>
<a id="ad7e0ffe55e8dbd97caa5bc089d33540ca1fe2554bbbf05c86d3f9b0bc50927c1b"></a>
<a id="ad7e0ffe55e8dbd97caa5bc089d33540caca3b7f2a39ff93b91b8317245e8375ab"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a8f46002e33dddab6782bad93ab3fd8b1"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a5e4eaf66a7356e73b4c6e4949160f321"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a898b493832d06586cf48f9a2545651d0"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18aee43a865c5815ce058261f5f0550fa2b"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18afd0445322777cdb9cb799b43fc8ace1c"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18aba0a811e14f9e87bd47bfbeaad24e11b"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18ac9200dedb25cfa03b80f4336e86db5ed"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a8c700fd2062d8dc51c5e4b28c98c6cf0"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a418aca13d3bd1608869494d26559e52f"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a1e35a224f4809d3a59d0f1570bf382bb"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a760de1a9f06cc6d4832da868d01702c4"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a7e7c3645f46ba3c2e8329ae3a9eeaa79"></a>
<a id="ad0dac3b7e7cbf3649aa5b8813e40fc18a0d9d5044c9df2a6b61b7a46a4f24e895"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa59c3bbc8cb2a44e26920adbe0251375b"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa4f147b313644dba74c95930038201cf7"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa8a2a4bb1bb5b7f69960fdcde374f2ee6"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa736709e926d95754fef9260c596530e2"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa6d89a732b306e21feeaee51cdbcc0bed"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa9bb36ad38aca4f118fe1bdc2f0351476"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa1a39257d816910b26f2323b61a278519"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fae4640365810ae80e8c24507fd7279f3d"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561fa172bc7d2ed80cadb4077ae42233764b2"></a>
<a id="a9e5e9af7a281e53f2b950089ee66561faa062bfc1af7cc119d025dee309ac1d25"></a>
<a id="a342c0d62cf874ccb8b657ce85d91efe0a29354369703a5e54ae7e49edfff886ff"></a>
<a id="a342c0d62cf874ccb8b657ce85d91efe0aa60a16ce7e100e06e0bab9a3922003a6"></a>
<a id="a342c0d62cf874ccb8b657ce85d91efe0a1e324c97e68e6d7ce35feb4ffe2ca617"></a>
<a id="a6711a33292bf25327950406b96585690adca8434b24978430d03939b81d76fbb9"></a>
<a id="a6711a33292bf25327950406b96585690a31a403a2013dc9da3da56366fa95f19b"></a>
<a id="a6711a33292bf25327950406b96585690a931ed807a91dd1f0e6e2cfa013860cbe"></a>
<a id="a6711a33292bf25327950406b96585690ac3f1631647cfd0246be61fc78549a9f7"></a>
<a id="a6711a33292bf25327950406b96585690a2dad67829bb51786024771c0d5a6d103"></a>
<a id="a6711a33292bf25327950406b96585690a4e14cf64a03e9d37af198870b0616497"></a>
<a id="a260c4adbe9524bd747127a4e3f14bbcaa88bba7f61485369188998bc1c18b2511"></a>
<a id="a260c4adbe9524bd747127a4e3f14bbcaacd2316ff6386c7eb2da90de1f4466469"></a>
<a id="a3cf04300758f1802e0703428707035d7a871b880c791ad49c55164856ac4f83f9"></a>
<a id="a3cf04300758f1802e0703428707035d7ace6e98ad1c1ac7232327d42b0f4302ef"></a>
<a id="a3cf04300758f1802e0703428707035d7ad2c8bf68306ca6bb22e88c5c6d957453"></a>
<a id="a3cf04300758f1802e0703428707035d7a89a96eb89044b208d3a6c29fc273fa26"></a>
<a id="a3cf04300758f1802e0703428707035d7a036303b6caf601b73bfb48b3a7423309"></a>
<a id="a3cf04300758f1802e0703428707035d7a5bd474bec0302248268ccff2eb9290a3"></a>
<a id="a3cf04300758f1802e0703428707035d7aa31397b2154b0f1f9b1e906c91a6bc8c"></a>
<a id="a0d969e434f941cf5af7143cca0cf0fe4a43aa77232e6c2aed82ecf2033c0a06b0"></a>
<a id="a0d969e434f941cf5af7143cca0cf0fe4a66c14a28074edc8631bd6b47f5c45888"></a>
<a id="a8a935ea7debb4ac73ea99c98d6ef4d3ba8f887b777e29fc05107ac406d4a87458"></a>
<a id="a8a935ea7debb4ac73ea99c98d6ef4d3bae87d4355340186b8a049346e3076f9ae"></a>
<a id="a58dc8b84784731500aa7f55afeb7e582a43616a8ad2465c7521aa9ed28460cf57"></a>
<a id="a58dc8b84784731500aa7f55afeb7e582a61cbc043ccd0a96ba2327d7bd95189c6"></a>
<a id="a58dc8b84784731500aa7f55afeb7e582af5ccdcc3eed53b0906b83667443e3667"></a>
<a id="a58dc8b84784731500aa7f55afeb7e582a73aeb813a098d600dfb60561bc042e2a"></a>
<a id="a58dc8b84784731500aa7f55afeb7e582a9f36e6c7688a62737beb203e82de91ef"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6cac84f9ad61c85bbce60e680639c3d88ad"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca5174a26b3b79356bf06402de46bc0774"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6caef6c925e20f072665bf55e435d37a6ac"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca07aa8c55e3504c0d19b1e123f4d2e7c7"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca6435225efac8c7ef6e336a84fa2e8932"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca263a724b491a6303d5486828a49a8961"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6caa2c68fe9d01bc4acf3054d667f3e2a77"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6cafea982067c784c47ae5b1ad7e91b4191"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca39492ba0c78d0290819b9410e2e55781"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca7f1d764aa078c284c575ec610d4f4853"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6cae3c6e42e75e69a34d7017d2f2aa3c70d"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca99b8f62b1d204b335a06ed6f3ef214e6"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca2a5cc3b49abc9be0c6bbab0a9963ba03"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca8787502b2d9a14d2ce79b1ce1713d6f3"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca884ab2ce56a1f7a08d4b9d06b944ad37"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6cad58d4ac5b57cbdd42d360560cc16fc0e"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca58ad56a546a2df6c9359927375da9904"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6ca5c12f57e0b4de16d09fc42f23740908b"></a>
<a id="aa221b68c53f25634d9f2f435f28c1a6cae6a2501b586793e75cdd0085170a9a27"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefad351fdc11590580b88ba5b486113e498"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefae28182c06da19d2b498f92d09d74b33e"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefae47dad429327e6a0cc89e339729b2651"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefa1f8c2845d6e8e41f62cc28b7f1681f43"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefa648f596240841758588749574998bd71"></a>
<a id="a173b6c1016562da43b8131b8d8f04fefa2c20469f6893f651ad14b8ed6a7c3845"></a>
<a id="a3384ec6c907acb911c4a9c32bcd473caaec46850a66dfd2d6bfcb18849a737fdc"></a>
<a id="a3384ec6c907acb911c4a9c32bcd473caa521219142a95c322e501497ab6262798"></a>
<a id="afbba8ada09d6c6489d52a3b9dc31725fa3661b89022659975720d3a022b21f194"></a>
<a id="afbba8ada09d6c6489d52a3b9dc31725fa7dcaa32f001d1a7b5b071cdf7621081e"></a>
<a id="afbba8ada09d6c6489d52a3b9dc31725fa95ea7c01a987a1e334f41c79642b8139"></a>
<a id="a359b0f88d3769af43c2b1699eb172f23a8bc6c6397d5bc342ebe0ea36522e96a5"></a>
<a id="a359b0f88d3769af43c2b1699eb172f23a34b4b516760245d0a5bbfcbb5937d74c"></a>
<a id="a359b0f88d3769af43c2b1699eb172f23a6fe85d7688c6730a492981fdc4623c67"></a>
<a id="a359b0f88d3769af43c2b1699eb172f23ab6c294e0f55696a8c90ec8211673ca80"></a>
<a id="a359b0f88d3769af43c2b1699eb172f23a8eeae948253c11b7f097dd06896e66f8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P070_zephyr__drivers__sensor__mlx90394.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P072_zephyr__mpipe__mpipe.h_文件参考.md)
