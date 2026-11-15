---
id: learning.zephyr-docs.api-source-reference.page-824
title: stepper_trinamic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第824章\_stepper\_trinamic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h.html)。

## 824.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00206"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="agroup__trinamic__stepper__ctrl_html_ga08b0b69ad4db741165d128cb2b2c3188"></a>
<a id="agroup__trinamic__stepper__ctrl_html_ga27c449d5c0bbacabae333c1356aedfd9"></a>
<a id="agroup__trinamic__stepper__ctrl_html_ga3c59d8c7e49d3f5959712b23b2df47ac"></a>
<a id="agroup__trinamic__stepper__ctrl_html_ga7ef8f93f0301b2437b98eceac43407c7"></a>
<a id="agroup__trinamic__stepper__ctrl_html_gaa2534eba96364f813617706a08ea73f7"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astepper_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructtmc__ramp__generator__data_html"></a>
<a id="astructtmc__ramp__generator__data_html_a277403bbb0bbc8a7562bf7b6c3e22333"></a>
<a id="astructtmc__ramp__generator__data_html_a34bc24f327a5c1a6315fa4869c5418df"></a>
<a id="astructtmc__ramp__generator__data_html_a3b7d2176725aef71e12950fde1ae3ee0"></a>
<a id="astructtmc__ramp__generator__data_html_a522f3c11bcac25852a0d7088795f46bd"></a>
<a id="astructtmc__ramp__generator__data_html_a54558710f19a1781bbec3dc857cb8fcf"></a>
<a id="astructtmc__ramp__generator__data_html_a5ee17564fb78bbbfd1097c6b440bd30c"></a>
<a id="astructtmc__ramp__generator__data_html_a5f4a921ae3ba0fec18633e659ad42573"></a>
<a id="astructtmc__ramp__generator__data_html_a6b861b90bb7e4c637b21b7809608152f"></a>
<a id="astructtmc__ramp__generator__data_html_a8045473482ca1272a75e99938564a700"></a>
<a id="astructtmc__ramp__generator__data_html_a8672451e2bff4af7f13b72f8a4bc4ed1"></a>
<a id="astructtmc__ramp__generator__data_html_a871cb11fb3d1aacfd29b85f8ea42b502"></a>
<a id="astructtmc__ramp__generator__data_html_a94352ae1924cbc900545065c7302379b"></a>
<a id="astructtmc__ramp__generator__data_html_acd7d7b5170ce3ce8839272ecc4dccd52"></a>
<a id="astructtmc__ramp__generator__data_html_ad3846d55690f835623fceca620ec3b23"></a>
<a id="astructtmc__ramp__generator__data_html_ae9377878720cc03760d207b750997997"></a>
<a id="astructtmc__ramp__generator__data_html_aff69cc918c9ed7e067d728a936b9a5f0"></a>
<a id="astructtmc__stallguard__settings_html"></a>
<a id="astructtmc__stallguard__settings_html_a953ef8f63bbf5dff74b91723a435cb42"></a>
<a id="astructtmc__stallguard__settings_html_aadc55163f314403e5d4cd231d4d209df"></a>
<a id="astructtmc__stallguard__settings_html_ac517501bdcb980b2690301bcdce78c98"></a>

```c


/*
 * SPDX-FileCopyrightText: Copyright (c) 2024 Carl Zeiss Meditec AG
 * SPDX-FileCopyrightText: Copyright (c) 2025 Prevas A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_STEPPER_STEPPER_TRINAMIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_STEPPER_STEPPER_TRINAMIC_H_


#include <stdint.h>
#include <zephyr/drivers/stepper/stepper.h>

#ifdef __cplusplus
extern "C" {
#endif

#define TMC_RAMP_VACTUAL_SHIFT  23
#define TMC_RAMP_XACTUAL_SHIFT  31

struct tmc_stallguard_settings {
        bool is_sg_enabled;
        uint16_t sg_velocity_check_interval_ms;
        uint32_t sg_threshold_velocity;
};

struct tmc_ramp_generator_data {
        uint32_t vstart;
        uint32_t v1;
        uint32_t vmax;
        uint16_t a1;
        uint16_t amax;
        uint16_t d1;
        uint16_t dmax;
        uint32_t vstop;
        uint16_t tzerowait;
        uint32_t iholdrun;
        union {
                struct {
                        uint32_t vcoolthrs;
                        uint32_t vhigh;
                };
                struct {
                        uint32_t tpowerdown;
                        uint32_t tpwmthrs;
                        uint32_t tcoolthrs;
                        uint32_t thigh;
                };
        };
};

#define TMC_RAMP_DT_SPEC_GET_COMMON(node)                                       \
                .vstart = DT_PROP(node, vstart),                                \
                .v1 = DT_PROP(node, v1),                                        \
                .vmax = DT_PROP(node, vmax),                                    \
                .a1 = DT_PROP(node, a1),                                        \
                .amax = DT_PROP(node, amax),                                    \
                .d1 = DT_PROP(node, d1),                                        \
                .dmax = DT_PROP(node, dmax),                                    \
                .vstop = DT_PROP(node, vstop),                                  \
                .tzerowait = DT_PROP(node, tzerowait),                          \
                .iholdrun = (TMC5XXX_IRUN(DT_PROP(node, irun)) |                \
                             TMC5XXX_IHOLD(DT_PROP(node, ihold)) |              \
                             TMC5XXX_IHOLDDELAY(DT_PROP(node, iholddelay))),

#define TMC_RAMP_DT_SPEC_GET_TMC50XX(node)                                      \
        {                                                                       \
                TMC_RAMP_DT_SPEC_GET_COMMON(node)                               \
                .vhigh = DT_PROP(node, vhigh),                                  \
                .vcoolthrs = DT_PROP(node, vcoolthrs),                          \
        }

#define TMC_RAMP_DT_SPEC_GET_TMC51XX(node)                                      \
        {                                                                       \
                TMC_RAMP_DT_SPEC_GET_COMMON(DT_DRV_INST(node))                  \
                .tpowerdown = DT_INST_PROP(node, tpowerdown),                   \
                .tpwmthrs = DT_INST_PROP(node, tpwmthrs),                       \
                .tcoolthrs = DT_INST_PROP(node, tcoolthrs),                     \
                .thigh = DT_INST_PROP(node, thigh),                             \
        }

int tmc50xx_stepper_ctrl_set_ramp(const struct device *dev,
                             const struct tmc_ramp_generator_data *ramp_data);

int tmc50xx_stepper_ctrl_set_max_velocity(const struct device *dev, uint32_t velocity);

void tmc50xx_stepper_ctrl_configure_stallguard(const struct device *dev,
                                               const struct tmc_stallguard_settings *sg_settings);

void tmc51xx_stepper_ctrl_configure_stallguard(const struct device *dev,
                                               const struct tmc_stallguard_settings *sg_settings);

int tmc51xx_stepper_ctrl_set_max_velocity(const struct device *dev, uint32_t velocity);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_STEPPER_STEPPER_TRINAMIC_H_ */
```

## 824.2\_可见注释译文（Comments）

### 注释 1：原第 9 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2024 Carl Zeiss Meditec AG。

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2025 Prevas A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 215 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_STEPPER_STEPPER_TRINAMIC_H_`。

## 824.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stepper__trinamic_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/stepper/stepper.h](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)
- [tmc_stallguard_settings](../hardware/P242_Trinamic堵转检测设置.md)
- [is_sg_enabled](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#a953ef8f63bbf5dff74b91723a435cb42)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sg_velocity_check_interval_ms](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#aadc55163f314403e5d4cd231d4d209df)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sg_threshold_velocity](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#ac517501bdcb980b2690301bcdce78c98)
- [tmc_ramp_generator_data](../hardware/P243_Trinamic斜坡发生器参数.md)
- [vstart](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a6b861b90bb7e4c637b21b7809608152f)
- [v1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ae9377878720cc03760d207b750997997)
- [vmax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a54558710f19a1781bbec3dc857cb8fcf)
- [a1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#aff69cc918c9ed7e067d728a936b9a5f0)
- [amax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a277403bbb0bbc8a7562bf7b6c3e22333)
- [d1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8672451e2bff4af7f13b72f8a4bc4ed1)
- [dmax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a34bc24f327a5c1a6315fa4869c5418df)
- [vstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5f4a921ae3ba0fec18633e659ad42573)
- [tzerowait](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ad3846d55690f835623fceca620ec3b23)
- [iholdrun](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#acd7d7b5170ce3ce8839272ecc4dccd52)
- [vcoolthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a522f3c11bcac25852a0d7088795f46bd)
- [vhigh](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5ee17564fb78bbbfd1097c6b440bd30c)
- [tpowerdown](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a3b7d2176725aef71e12950fde1ae3ee0)
- [tpwmthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a94352ae1924cbc900545065c7302379b)
- [tcoolthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a871cb11fb3d1aacfd29b85f8ea42b502)
- [thigh](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8045473482ca1272a75e99938564a700)
- [tmc50xx_stepper_ctrl_set_ramp](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga27c449d5c0bbacabae333c1356aedfd9)
- [device](../device_reference/P002_设备对象结构.md)
- [tmc50xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga3c59d8c7e49d3f5959712b23b2df47ac)
- [tmc50xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga7ef8f93f0301b2437b98eceac43407c7)
- [tmc51xx_stepper_ctrl_configure_stallguard](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga08b0b69ad4db741165d128cb2b2c3188)
- [tmc51xx_stepper_ctrl_set_max_velocity](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#gaa2534eba96364f813617706a08ea73f7)
- [stepper.h](https://docs.zephyrproject.org/latest/doxygen/html/stepper_8h.html)
- [tmc_ramp_generator_data::amax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a277403bbb0bbc8a7562bf7b6c3e22333)
- [tmc_ramp_generator_data::dmax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a34bc24f327a5c1a6315fa4869c5418df)
- [tmc_ramp_generator_data::tpowerdown](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a3b7d2176725aef71e12950fde1ae3ee0)
- [tmc_ramp_generator_data::vcoolthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a522f3c11bcac25852a0d7088795f46bd)
- [tmc_ramp_generator_data::vmax](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a54558710f19a1781bbec3dc857cb8fcf)
- [tmc_ramp_generator_data::vhigh](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5ee17564fb78bbbfd1097c6b440bd30c)
- [tmc_ramp_generator_data::vstop](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5f4a921ae3ba0fec18633e659ad42573)
- [tmc_ramp_generator_data::vstart](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a6b861b90bb7e4c637b21b7809608152f)
- [tmc_ramp_generator_data::thigh](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8045473482ca1272a75e99938564a700)
- [tmc_ramp_generator_data::d1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8672451e2bff4af7f13b72f8a4bc4ed1)
- [tmc_ramp_generator_data::tcoolthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a871cb11fb3d1aacfd29b85f8ea42b502)
- [tmc_ramp_generator_data::tpwmthrs](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a94352ae1924cbc900545065c7302379b)
- [tmc_ramp_generator_data::iholdrun](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#acd7d7b5170ce3ce8839272ecc4dccd52)
- [tmc_ramp_generator_data::tzerowait](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ad3846d55690f835623fceca620ec3b23)
- [tmc_ramp_generator_data::v1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ae9377878720cc03760d207b750997997)
- [tmc_ramp_generator_data::a1](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#aff69cc918c9ed7e067d728a936b9a5f0)
- [tmc_stallguard_settings::is_sg_enabled](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#a953ef8f63bbf5dff74b91723a435cb42)
- [tmc_stallguard_settings::sg_velocity_check_interval_ms](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#aadc55163f314403e5d4cd231d4d209df)
- [tmc_stallguard_settings::sg_threshold_velocity](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#ac517501bdcb980b2690301bcdce78c98)

---

[上一章](P823_stepper_tmcm3216.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P825_stm32-common.h_源码浏览.md)
