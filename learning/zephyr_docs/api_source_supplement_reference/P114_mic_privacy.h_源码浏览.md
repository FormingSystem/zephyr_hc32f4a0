---
id: learning.zephyr-docs.api-source-supplement-reference.page-114
title: mic_privacy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_mic\_privacy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html)。

## 114.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00017"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amic__privacy_8h_html_acbabb5c150f29668a23379bcb2180931"></a>
<a id="amic__privacy_8h_html_acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f"></a>
<a id="amic__privacy_8h_html_acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c"></a>
<a id="amic__privacy_8h_html_acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4"></a>
<a id="amic__privacy_8h_html_acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90"></a>
<a id="aspinlock_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructintel__adsp__mic__priv__cfg_html"></a>
<a id="astructintel__adsp__mic__priv__cfg_html_abbd9d8fbdef2f213c6d7fd05d087358c"></a>
<a id="astructintel__adsp__mic__priv__cfg_html_ad3b2a9026031e758618cf97dbb66c006"></a>
<a id="astructintel__adsp__mic__priv__data_html"></a>
<a id="astructintel__adsp__mic__priv__data_html_a35c90e6b6980e1015acb521b90f4992e"></a>
<a id="astructmic__privacy__api__funcs_html"></a>
<a id="astructmic__privacy__api__funcs_html_a1ee80c505a6a7d7bdf34c228acfc3b87"></a>
<a id="astructmic__privacy__api__funcs_html_a294e4cd3bb23ccb23f7143b6a9e4dba5"></a>
<a id="astructmic__privacy__api__funcs_html_a3e365ecf294cf653d0439d5d6d7d6ed5"></a>
<a id="astructmic__privacy__api__funcs_html_a558346b619a67f3f05b20cf62a7993ef"></a>
<a id="astructmic__privacy__api__funcs_html_a67548968f088126881ef11f7317e5036"></a>
<a id="astructmic__privacy__api__funcs_html_a6f21bade6b6041322cba6995f9140d6b"></a>
<a id="astructmic__privacy__api__funcs_html_a73ea5882b8af5f4a738913c1c16a3aaf"></a>
<a id="astructmic__privacy__api__funcs_html_a8cd74fd6817c3f5bfa0fc7697765d357"></a>
<a id="astructmic__privacy__api__funcs_html_a9b827a1b6b817d5e5ec19ffa94b531f0"></a>
<a id="astructmic__privacy__api__funcs_html_abedb0ba2dbb1d9ba639aab636308747f"></a>
<a id="astructmic__privacy__api__funcs_html_ac60beb8b72089feab7267c265d4bfe5d"></a>
<a id="astructmic__privacy__api__funcs_html_ad03e41de9d08b1cdd77abd6d40f14baf"></a>
<a id="astructmic__privacy__api__funcs_html_ae68b97acf6ec4f5812275ee682bdf96d"></a>
<a id="astructmic__privacy__api__funcs_html_afc87beb092fa02c06dcd84125ccc305a"></a>
<a id="aunionmic__privacy__mask_html"></a>
<a id="aunionmic__privacy__mask_html_a074ae40d422faa6a338454ca5072c978"></a>
<a id="aunionmic__privacy__mask_html_a7803afbf97e48fa202cbb40e96777437"></a>
<a id="aunionmic__privacy__mask_html_a9ca8420acd33e12b2454457d4e626c03"></a>

```c
/*
 * Copyright (c) 2025 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef __ZEPHYR_INCLUDE_MIC_PRIVACY_H__
#define __ZEPHYR_INCLUDE_MIC_PRIVACY_H__

#include <stdint.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/spinlock.h>
#include <zephyr/devicetree.h>

enum mic_privacy_policy {
        MIC_PRIVACY_DISABLED = 0,
        MIC_PRIVACY_HW_MANAGED = 1,
        MIC_PRIVACY_FW_MANAGED = 2,
        MIC_PRIVACY_FORCE_MIC_DISABLED = 3,
};

/* has to match HW register definition
 * (DZLS bit field in DFMICPVCP register)
 */
union mic_privacy_mask {
        uint32_t value;
        struct {
                uint32_t sndw:7;
                uint32_t dmic:1;
        };
};

struct intel_adsp_mic_priv_data {
        uint8_t rsvd;
};

struct intel_adsp_mic_priv_cfg {
        uint32_t base;
        uint32_t regblock_size;
};

struct mic_privacy_api_funcs {
        void (*enable_fw_managed_irq)(bool enable_irq, const void *fn);
        void (*clear_fw_managed_irq)();
        void (*enable_dmic_irq)(bool enable_irq, const void *fn);
        bool (*get_dmic_irq_status)(void);
        void (*clear_dmic_irq_status)(void);
        enum mic_privacy_policy (*get_policy)();
        uint32_t (*get_privacy_policy_register_raw_value)();
        uint32_t (*get_dma_data_zeroing_wait_time)();
        uint32_t (*get_dma_data_zeroing_link_select)();
        uint32_t (*get_dmic_mic_disable_status)(void);
        uint32_t (*get_fw_managed_mic_disable_status)();
        void (*set_fw_managed_mode)(bool is_fw_managed_enabled);
        void (*set_fw_mic_disable_status)(bool fw_mic_disable_status);
        uint32_t (*get_fw_mic_disable_status)();
};

#endif
```

## 114.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

必须与硬件寄存器定义匹配，即 `DFMICPVCP` 寄存器中的 `DZLS` 位域。

## 114.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [mic_privacy_policy](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931)
- [MIC_PRIVACY_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4)
- [MIC_PRIVACY_HW_MANAGED](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f)
- [MIC_PRIVACY_FW_MANAGED](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c)
- [MIC_PRIVACY_FORCE_MIC_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90)
- [mic_privacy_mask](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [value](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a9ca8420acd33e12b2454457d4e626c03)
- [sndw](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a7803afbf97e48fa202cbb40e96777437)
- [dmic](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a074ae40d422faa6a338454ca5072c978)
- [intel_adsp_mic_priv_data](../platform_security_model_reference/P013_intel_adsp_mic_priv_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rsvd](../platform_security_model_reference/P013_intel_adsp_mic_priv_data_结构体.md#a35c90e6b6980e1015acb521b90f4992e)
- [intel_adsp_mic_priv_cfg](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md)
- [base](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md#ad3b2a9026031e758618cf97dbb66c006)
- [regblock_size](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md#abbd9d8fbdef2f213c6d7fd05d087358c)
- [mic_privacy_api_funcs](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md)
- [enable_fw_managed_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a67548968f088126881ef11f7317e5036)
- [clear_fw_managed_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a294e4cd3bb23ccb23f7143b6a9e4dba5)
- [enable_dmic_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#afc87beb092fa02c06dcd84125ccc305a)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [get_dmic_irq_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a8cd74fd6817c3f5bfa0fc7697765d357)
- [clear_dmic_irq_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ae68b97acf6ec4f5812275ee682bdf96d)
- [get_policy](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a558346b619a67f3f05b20cf62a7993ef)
- [get_privacy_policy_register_raw_value](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ad03e41de9d08b1cdd77abd6d40f14baf)
- [get_dma_data_zeroing_wait_time](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a1ee80c505a6a7d7bdf34c228acfc3b87)
- [get_dma_data_zeroing_link_select](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a73ea5882b8af5f4a738913c1c16a3aaf)
- [get_dmic_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a3e365ecf294cf653d0439d5d6d7d6ed5)
- [get_fw_managed_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#abedb0ba2dbb1d9ba639aab636308747f)
- [set_fw_managed_mode](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a9b827a1b6b817d5e5ec19ffa94b531f0)
- [set_fw_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a6f21bade6b6041322cba6995f9140d6b)
- [get_fw_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ac60beb8b72089feab7267c265d4bfe5d)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [intel_adsp_mic_priv_cfg::regblock_size](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md#abbd9d8fbdef2f213c6d7fd05d087358c)
- [intel_adsp_mic_priv_cfg::base](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md#ad3b2a9026031e758618cf97dbb66c006)
- [intel_adsp_mic_priv_data::rsvd](../platform_security_model_reference/P013_intel_adsp_mic_priv_data_结构体.md#a35c90e6b6980e1015acb521b90f4992e)
- [mic_privacy_api_funcs::get_dma_data_zeroing_wait_time](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a1ee80c505a6a7d7bdf34c228acfc3b87)
- [mic_privacy_api_funcs::clear_fw_managed_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a294e4cd3bb23ccb23f7143b6a9e4dba5)
- [mic_privacy_api_funcs::get_dmic_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a3e365ecf294cf653d0439d5d6d7d6ed5)
- [mic_privacy_api_funcs::get_policy](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a558346b619a67f3f05b20cf62a7993ef)
- [mic_privacy_api_funcs::enable_fw_managed_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a67548968f088126881ef11f7317e5036)
- [mic_privacy_api_funcs::set_fw_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a6f21bade6b6041322cba6995f9140d6b)
- [mic_privacy_api_funcs::get_dma_data_zeroing_link_select](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a73ea5882b8af5f4a738913c1c16a3aaf)
- [mic_privacy_api_funcs::get_dmic_irq_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a8cd74fd6817c3f5bfa0fc7697765d357)
- [mic_privacy_api_funcs::set_fw_managed_mode](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#a9b827a1b6b817d5e5ec19ffa94b531f0)
- [mic_privacy_api_funcs::get_fw_managed_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#abedb0ba2dbb1d9ba639aab636308747f)
- [mic_privacy_api_funcs::get_fw_mic_disable_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ac60beb8b72089feab7267c265d4bfe5d)
- [mic_privacy_api_funcs::get_privacy_policy_register_raw_value](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ad03e41de9d08b1cdd77abd6d40f14baf)
- [mic_privacy_api_funcs::clear_dmic_irq_status](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#ae68b97acf6ec4f5812275ee682bdf96d)
- [mic_privacy_api_funcs::enable_dmic_irq](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md#afc87beb092fa02c06dcd84125ccc305a)
- [mic_privacy_mask::dmic](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a074ae40d422faa6a338454ca5072c978)
- [mic_privacy_mask::sndw](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a7803afbf97e48fa202cbb40e96777437)
- [mic_privacy_mask::value](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md#a9ca8420acd33e12b2454457d4e626c03)

---

[上一章](P113_smp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P115_mman.h_源码浏览.md)
