---
id: learning.zephyr-docs.api-file-management-reference.page-12
title: zephyr__drivers__haptics__drv2605.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drv2605_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_haptics\_\_drv2605.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drv2605_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供DRV2605触觉反馈（Haptic）驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/haptics.h>
#include <zephyr/types.h>
```

查看此文件的源码。

提供DRV2605触觉反馈（Haptic）驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_drv2605_5From_5Fdata"></a>

```c
struct drv2605_rom_data
```

相关声明：[drv2605_rom_data](../hardware/P157_DRV2605只读波形配置.md)。

只读存储器（ROM）数据配置。

<a id="r_drv2605_5Frtp_5Fdata"></a>

```c
struct drv2605_rtp_data
```

相关声明：[drv2605_rtp_data](../hardware/P158_DRV2605实时播放配置.md)。

实时播放（Real-Time Playback，RTP）数据配置。

<a id="r_drv2605_5Fconfig_5Fdata"></a>

```c
union drv2605_config_data
```

相关声明：[drv2605_config_data](../hardware/P159_DRV2605配置联合体.md)。

配置数据联合体（Configuration Data Union）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 辅助定义（Helpers）

<a id="r_gab9069fcfd891cadbe5838d0caac5bca0"></a>

```c
#define DRV2605_WAVEFORM_SEQUENCER_MAX 8
```

相关声明：[DRV2605_WAVEFORM_SEQUENCER_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gab9069fcfd891cadbe5838d0caac5bca0)。

序列器（sequencer）能够保存的最大波形数量。

<a id="r_ga810b863fcc057e7e1d20647f46511282"></a>

```c
#define DRV2605_WAVEFORM_SEQUENCER_WAIT_MS(ms)
```

相关声明：[DRV2605_WAVEFORM_SEQUENCER_WAIT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ga810b863fcc057e7e1d20647f46511282)。

为波形序列器（waveform sequencer）创建等待／延迟值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.3\_枚举（Enumerations）

<a id="r_gad8242facf545ff18b81f0703bcf6bb16"></a>

```c
enum drv2605_library { DRV2605_LIBRARY_EMPTY = 0 , DRV2605_LIBRARY_TS2200_A , DRV2605_LIBRARY_TS2200_B , DRV2605_LIBRARY_TS2200_C , DRV2605_LIBRARY_TS2200_D , DRV2605_LIBRARY_TS2200_E , DRV2605_LIBRARY_LRA }
```

相关声明：[drv2605_library](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gad8242facf545ff18b81f0703bcf6bb16)、[DRV2605_LIBRARY_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aad90f2d8bdee21c390c4344bd808d345)、[DRV2605_LIBRARY_TS2200_A](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a3babadb779b635c80d88fbd5eeb1dd7a)、[DRV2605_LIBRARY_TS2200_B](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a368575d421fedc421e0540393cc27845)、[DRV2605_LIBRARY_TS2200_C](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a53c2477779bae577572c1d38ccffbcf1)、[DRV2605_LIBRARY_TS2200_D](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aa2df9656713c03702620e945de72de56)、[DRV2605_LIBRARY_TS2200_E](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aa3656aebd793e203c0b986abb7846f64)、[DRV2605_LIBRARY_LRA](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a3f114d1e1095105c5db786e9aa2dff60)。

效果库（effect libraries）。

<a id="r_ga01ec80a028b1101fbdf3e624800ca02a"></a>

```c
enum drv2605_mode { DRV2605_MODE_INTERNAL_TRIGGER = 0 , DRV2605_MODE_EXTERNAL_EDGE_TRIGGER , DRV2605_MODE_EXTERNAL_LEVEL_TRIGGER , DRV2605_MODE_PWM_ANALOG_INPUT , DRV2605_MODE_AUDIO_TO_VIBE , DRV2605_MODE_RTP , DRV2605_MODE_DIAGNOSTICS , DRV2605_MODE_AUTO_CAL }
```

相关声明：[drv2605_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ga01ec80a028b1101fbdf3e624800ca02a)、[DRV2605_MODE_INTERNAL_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaab537e7781201365d04f1b61ca1293b5)、[DRV2605_MODE_EXTERNAL_EDGE_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaeb3d84bd67bd5ffa36cd11628d051fb9)、[DRV2605_MODE_EXTERNAL_LEVEL_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa8303fe0cf8044350d6be89eb0865b254)、[DRV2605_MODE_PWM_ANALOG_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa62b722c2507a7f9160f775631894cc2f)、[DRV2605_MODE_AUDIO_TO_VIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aafca2555c87c8b63e417e5353f24b2c24)、[DRV2605_MODE_RTP](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaf9d11ca9fce86e99cad74b77a2089d9a)、[DRV2605_MODE_DIAGNOSTICS](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa3c980005d0daee97567fa5e35d8a2836)、[DRV2605_MODE_AUTO_CAL](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aadcfb6eb9e12238478bf23fb76423f248)。

运行模式（modes of operation）。

<a id="r_gae98fe02355253b7d8f4583a36919639c"></a>

```c
enum drv2605_haptics_source { DRV2605_HAPTICS_SOURCE_ROM , DRV2605_HAPTICS_SOURCE_RTP , DRV2605_HAPTICS_SOURCE_AUDIO , DRV2605_HAPTICS_SOURCE_PWM , DRV2605_HAPTICS_SOURCE_ANALOG }
```

相关声明：[drv2605_haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gae98fe02355253b7d8f4583a36919639c)、[DRV2605_HAPTICS_SOURCE_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca38623b24d3ca65f42e8ab09ad2764d5d)、[DRV2605_HAPTICS_SOURCE_RTP](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca51dd1dcc3db5a89efd31a9f72c7db43a)、[DRV2605_HAPTICS_SOURCE_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca3903c6a4404288eaa77a8d365cfc344a)、[DRV2605_HAPTICS_SOURCE_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639caa30841998fe2092cdf959153291e0d08)、[DRV2605_HAPTICS_SOURCE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca84df3211177d36ab92cd44fde7bb1b1a)。

触觉信号源（haptic signal sources）的类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_gafe7decc53e258a7162b44ae2076c10d1"></a>

```c
int drv2605_haptic_config (const struct device *dev, enum drv2605_haptics_source source, const union drv2605_config_data *config_data)
```

相关声明：[drv2605_haptic_config](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gafe7decc53e258a7162b44ae2076c10d1)、[device](../device_reference/P002_设备对象结构.md)、[drv2605_haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gae98fe02355253b7d8f4583a36919639c)、[drv2605_config_data](../hardware/P159_DRV2605配置联合体.md)。

将 DRV2605 设备配置为使用指定信号源。


## 12.5\_原页交叉引用（Cross References）

- [zephyr/drivers/haptics.h](../api_source_system_reference/P013_haptics.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P046_drv2605.h_源码浏览.md)
- [drv2605_rom_data](../hardware/P157_DRV2605只读波形配置.md)
- [drv2605_rtp_data](../hardware/P158_DRV2605实时播放配置.md)
- [drv2605_config_data](../hardware/P159_DRV2605配置联合体.md)
- [DRV2605_WAVEFORM_SEQUENCER_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gab9069fcfd891cadbe5838d0caac5bca0)
- [DRV2605_WAVEFORM_SEQUENCER_WAIT_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ga810b863fcc057e7e1d20647f46511282)
- [drv2605_library](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gad8242facf545ff18b81f0703bcf6bb16)
- [DRV2605_LIBRARY_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aad90f2d8bdee21c390c4344bd808d345)
- [DRV2605_LIBRARY_TS2200_A](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a3babadb779b635c80d88fbd5eeb1dd7a)
- [DRV2605_LIBRARY_TS2200_B](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a368575d421fedc421e0540393cc27845)
- [DRV2605_LIBRARY_TS2200_C](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a53c2477779bae577572c1d38ccffbcf1)
- [DRV2605_LIBRARY_TS2200_D](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aa2df9656713c03702620e945de72de56)
- [DRV2605_LIBRARY_TS2200_E](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16aa3656aebd793e203c0b986abb7846f64)
- [DRV2605_LIBRARY_LRA](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggad8242facf545ff18b81f0703bcf6bb16a3f114d1e1095105c5db786e9aa2dff60)
- [drv2605_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ga01ec80a028b1101fbdf3e624800ca02a)
- [DRV2605_MODE_INTERNAL_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaab537e7781201365d04f1b61ca1293b5)
- [DRV2605_MODE_EXTERNAL_EDGE_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaeb3d84bd67bd5ffa36cd11628d051fb9)
- [DRV2605_MODE_EXTERNAL_LEVEL_TRIGGER](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa8303fe0cf8044350d6be89eb0865b254)
- [DRV2605_MODE_PWM_ANALOG_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa62b722c2507a7f9160f775631894cc2f)
- [DRV2605_MODE_AUDIO_TO_VIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aafca2555c87c8b63e417e5353f24b2c24)
- [DRV2605_MODE_RTP](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aaf9d11ca9fce86e99cad74b77a2089d9a)
- [DRV2605_MODE_DIAGNOSTICS](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aa3c980005d0daee97567fa5e35d8a2836)
- [DRV2605_MODE_AUTO_CAL](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gga01ec80a028b1101fbdf3e624800ca02aadcfb6eb9e12238478bf23fb76423f248)
- [drv2605_haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gae98fe02355253b7d8f4583a36919639c)
- [DRV2605_HAPTICS_SOURCE_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca38623b24d3ca65f42e8ab09ad2764d5d)
- [DRV2605_HAPTICS_SOURCE_RTP](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca51dd1dcc3db5a89efd31a9f72c7db43a)
- [DRV2605_HAPTICS_SOURCE_AUDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca3903c6a4404288eaa77a8d365cfc344a)
- [DRV2605_HAPTICS_SOURCE_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639caa30841998fe2092cdf959153291e0d08)
- [DRV2605_HAPTICS_SOURCE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#ggae98fe02355253b7d8f4583a36919639ca84df3211177d36ab92cd44fde7bb1b1a)
- [drv2605_haptic_config](https://docs.zephyrproject.org/latest/doxygen/html/group__drv2605__interface.html#gafe7decc53e258a7162b44ae2076c10d1)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__sensor__tmag5273.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__sent__sent.h_文件参考.md)
