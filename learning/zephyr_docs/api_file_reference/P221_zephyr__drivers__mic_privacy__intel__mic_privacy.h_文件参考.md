---
id: learning.zephyr-docs.api-file-reference.page-221
title: zephyr__drivers__mic_privacy__intel__mic_privacy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第221章\_zephyr\_\_drivers\_\_mic\_privacy\_\_intel\_\_mic\_privacy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mic__privacy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <errno.h>
#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/spinlock.h>
#include <zephyr/devicetree.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 221.1\_数据结构（Data Structures）

<a id="r_mic_5Fprivacy_5Fmask"></a>

```c
union mic_privacy_mask
```

相关声明：[mic_privacy_mask](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md)。

<a id="r_intel_5Fadsp_5Fmic_5Fpriv_5Fdata"></a>

```c
struct intel_adsp_mic_priv_data
```

相关声明：[intel_adsp_mic_priv_data](../platform_security_model_reference/P013_intel_adsp_mic_priv_data_结构体.md)。

<a id="r_intel_5Fadsp_5Fmic_5Fpriv_5Fcfg"></a>

```c
struct intel_adsp_mic_priv_cfg
```

相关声明：[intel_adsp_mic_priv_cfg](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md)。

<a id="r_mic_5Fprivacy_5Fapi_5Ffuncs"></a>

```c
struct mic_privacy_api_funcs
```

相关声明：[mic_privacy_api_funcs](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 221.2\_枚举（Enumerations）

<a id="r_acbabb5c150f29668a23379bcb2180931"></a>

```c
enum mic_privacy_policy { MIC_PRIVACY_DISABLED = 0 , MIC_PRIVACY_HW_MANAGED = 1 , MIC_PRIVACY_FW_MANAGED = 2 , MIC_PRIVACY_FORCE_MIC_DISABLED = 3 }
```

相关声明：[mic_privacy_policy](#acbabb5c150f29668a23379bcb2180931)、[MIC_PRIVACY_DISABLED](#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4)、[MIC_PRIVACY_HW_MANAGED](#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f)、[MIC_PRIVACY_FW_MANAGED](#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c)、[MIC_PRIVACY_FORCE_MIC_DISABLED](#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90)。

## 221.3\_详细说明（Detailed Documentation）

<a id="acbabb5c150f29668a23379bcb2180931"></a>

### `mic_privacy_policy`

```c
enum mic_privacy_policy
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MIC_PRIVACY_DISABLED` |  |
| `MIC_PRIVACY_HW_MANAGED` |  |
| `MIC_PRIVACY_FW_MANAGED` |  |
| `MIC_PRIVACY_FORCE_MIC_DISABLED` |  |


## 221.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/spinlock.h](../kernel/P068_自旋锁头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P114_mic_privacy.h_源码浏览.md)
- [mic_privacy_mask](../audio_video_model_reference/P068_mic_privacy_mask_联合体.md)
- [intel_adsp_mic_priv_data](../platform_security_model_reference/P013_intel_adsp_mic_priv_data_结构体.md)
- [intel_adsp_mic_priv_cfg](../platform_security_model_reference/P012_intel_adsp_mic_priv_cfg_结构体.md)
- [mic_privacy_api_funcs](../audio_video_model_reference/P010_mic_privacy_api_funcs_结构体.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4"></a>
<a id="acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f"></a>
<a id="acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c"></a>
<a id="acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90"></a>

---

[上一章](P220_zephyr__drivers__mfd__mfd_ite_it8801.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P222_zephyr__dt-bindings__gpio__microchip-sam-gpio.h_文件参考.md)
