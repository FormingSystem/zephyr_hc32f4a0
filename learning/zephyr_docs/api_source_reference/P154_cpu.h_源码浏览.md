---
id: learning.zephyr-docs.api-source-reference.page-154
title: cpu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第154章\_cpu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html)。

## 154.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="adrivers_2firmware_2scmi_2protocol_8h_html"></a>
<a id="agroup__scmi__nxp__cpu_html_ga346872d9b23f24a5f9d2636c6c31b9d8"></a>
<a id="agroup__scmi__nxp__cpu_html_ga3f3524711a4dacadbb2fcfeae9d5e008"></a>
<a id="agroup__scmi__nxp__cpu_html_ga493e417adeb9b63b48613e7ca1f625e8"></a>
<a id="agroup__scmi__nxp__cpu_html_ga49704cb9c07b198c7609f2f87628dfc0"></a>
<a id="agroup__scmi__nxp__cpu_html_ga73ecf2457ad66f98f96b9eb654915c83"></a>
<a id="agroup__scmi__nxp__cpu_html_gab8211fd0eb9f9be04b441b5488fe8d93"></a>
<a id="agroup__scmi__nxp__cpu_html_gae8e104786d96b8c5a03fc54d201e09ed"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructscmi__nxp__cpu__info_html"></a>
<a id="astructscmi__nxp__cpu__info_html_a53cab503c7619e68a5a7b6ddc71bcad8"></a>
<a id="astructscmi__nxp__cpu__info_html_a7642f805dd7a70bfc216c1526c3e3e7d"></a>
<a id="astructscmi__nxp__cpu__info_html_a9e8ef984d7613ef2893cd0fe42dc750b"></a>
<a id="astructscmi__nxp__cpu__info_html_ab817f075da09dea4359ae39a351fc966"></a>
<a id="astructscmi__nxp__cpu__irq__mask__config_html"></a>
<a id="astructscmi__nxp__cpu__irq__mask__config_html_a416a9df0f67c107d490725d2eeff8623"></a>
<a id="astructscmi__nxp__cpu__irq__mask__config_html_a53fb756537e3dd3c997371726b11a3f1"></a>
<a id="astructscmi__nxp__cpu__irq__mask__config_html_a5ffe5fae57289b1d53b8a19ca676f6e9"></a>
<a id="astructscmi__nxp__cpu__irq__mask__config_html_a75f9b3c94bef32627ca92af1c90ca032"></a>
<a id="astructscmi__nxp__cpu__pd__lpm__config_html"></a>
<a id="astructscmi__nxp__cpu__pd__lpm__config_html_a44654e7633e8d5705397e994ecf44f60"></a>
<a id="astructscmi__nxp__cpu__pd__lpm__config_html_a49f57505c116e79ca16f848662965604"></a>
<a id="astructscmi__nxp__cpu__pd__lpm__config_html_ac8f0fdc610b66703baaf1e177b0ef593"></a>
<a id="astructscmi__nxp__cpu__sleep__mode__config_html"></a>
<a id="astructscmi__nxp__cpu__sleep__mode__config_html_a016a162f5af8523cd84926f1355f62e8"></a>
<a id="astructscmi__nxp__cpu__sleep__mode__config_html_a24d167a783d564a2639332437c15ce21"></a>
<a id="astructscmi__nxp__cpu__sleep__mode__config_html_a2f34473f39d718c29209e10e4c45b14b"></a>
<a id="astructscmi__nxp__cpu__vector__config_html"></a>
<a id="astructscmi__nxp__cpu__vector__config_html_a02ce732308b9861367bf22be4bebe8fa"></a>
<a id="astructscmi__nxp__cpu__vector__config_html_a4583b0c5ff44c994c612765b8b91edcc"></a>
<a id="astructscmi__nxp__cpu__vector__config_html_a5d5d72d7ca43ac41a112822578fa3135"></a>
<a id="astructscmi__nxp__cpu__vector__config_html_a6ca9bb699b63aec9a15f3259173a07a9"></a>
<a id="astructscmi__pd__lpm__settings_html"></a>
<a id="astructscmi__pd__lpm__settings_html_a18de2ecf5f1d072967eacf7375d9e64c"></a>
<a id="astructscmi__pd__lpm__settings_html_a35c3e1f1f5ab7339b6ae736fb3dcde31"></a>
<a id="astructscmi__pd__lpm__settings_html_ae3614c23f92717999d2058ef8636fe7c"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_CPU_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_CPU_H_

#include <zephyr/drivers/firmware/scmi/protocol.h>
#if __has_include("scmi_cpu_soc.h")
#include <scmi_cpu_soc.h>
#endif


#define SCMI_NXP_CPU_SLEEP_FLAG_IRQ_MUX 0x1U

#define SCMI_PROTOCOL_NXP_CPU_DOMAIN 130

#define SCMI_NXP_CPU_MAX_PDCONFIGS_T 7U

#define SCMI_NXP_CPU_IRQ_WAKE_NUM       22U

#define SCMI_NXP_CPU_VEC_FLAGS_BOOT    BIT(29)

#define SCMI_NXP_CPU_VEC_FLAGS_START   BIT(30)

#define SCMI_NXP_CPU_VEC_FLAGS_RESUME  BIT(31)

#define SCMI_NXP_CPU_PROTOCOL_SUPPORTED_VERSION 0x10000

struct scmi_nxp_cpu_sleep_mode_config {
        uint32_t cpu_id;
        uint32_t flags;
        uint32_t sleep_mode;
};

struct scmi_pd_lpm_settings {
        uint32_t domain_id;
        uint32_t lpm_setting;
        uint32_t ret_mask;
};

struct scmi_nxp_cpu_pd_lpm_config {
        uint32_t cpu_id;
        uint32_t num_cfg;
        struct scmi_pd_lpm_settings cfgs[SCMI_NXP_CPU_MAX_PDCONFIGS_T];
};

struct scmi_nxp_cpu_irq_mask_config {
        uint32_t cpu_id;
        uint32_t mask_idx;
        uint32_t num_mask;
        uint32_t mask[SCMI_NXP_CPU_IRQ_WAKE_NUM];
};

struct scmi_nxp_cpu_vector_config {
        uint32_t cpu_id;
        uint32_t flags;
        uint32_t vector_low;
        uint32_t vector_high;
};

struct scmi_nxp_cpu_info {
        uint32_t run_mode;
        uint32_t sleep_mode;
        uint32_t vector_low;
        uint32_t vector_high;
};

int scmi_nxp_cpu_sleep_mode_set(struct scmi_nxp_cpu_sleep_mode_config *cfg);

int scmi_nxp_cpu_pd_lpm_set(struct scmi_nxp_cpu_pd_lpm_config *cfg);

int scmi_nxp_cpu_set_irq_mask(struct scmi_nxp_cpu_irq_mask_config *cfg);

int scmi_nxp_cpu_reset_vector(struct scmi_nxp_cpu_vector_config *cfg);

int scmi_nxp_cpu_info_get(uint32_t cpu_id, struct scmi_nxp_cpu_info *cfg);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_CPU_H_ */
```

## 154.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 195 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_NXP_CPU_H_`。

## 154.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html)
- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_nxp_cpu_sleep_mode_config](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cpu_id](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a016a162f5af8523cd84926f1355f62e8)
- [flags](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a24d167a783d564a2639332437c15ce21)
- [sleep_mode](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a2f34473f39d718c29209e10e4c45b14b)
- [scmi_pd_lpm_settings](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md)
- [domain_id](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#ae3614c23f92717999d2058ef8636fe7c)
- [lpm_setting](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#a35c3e1f1f5ab7339b6ae736fb3dcde31)
- [ret_mask](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#a18de2ecf5f1d072967eacf7375d9e64c)
- [scmi_nxp_cpu_pd_lpm_config](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md)
- [cpu_id](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#a44654e7633e8d5705397e994ecf44f60)
- [num_cfg](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#a49f57505c116e79ca16f848662965604)
- [cfgs](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#ac8f0fdc610b66703baaf1e177b0ef593)
- [SCMI_NXP_CPU_MAX_PDCONFIGS_T](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#ga73ecf2457ad66f98f96b9eb654915c83)
- [scmi_nxp_cpu_irq_mask_config](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md)
- [cpu_id](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a53fb756537e3dd3c997371726b11a3f1)
- [mask_idx](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a75f9b3c94bef32627ca92af1c90ca032)
- [num_mask](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a5ffe5fae57289b1d53b8a19ca676f6e9)
- [mask](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a416a9df0f67c107d490725d2eeff8623)
- [SCMI_NXP_CPU_IRQ_WAKE_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#ga49704cb9c07b198c7609f2f87628dfc0)
- [scmi_nxp_cpu_vector_config](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md)
- [cpu_id](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a4583b0c5ff44c994c612765b8b91edcc)
- [flags](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a02ce732308b9861367bf22be4bebe8fa)
- [vector_low](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a5d5d72d7ca43ac41a112822578fa3135)
- [vector_high](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a6ca9bb699b63aec9a15f3259173a07a9)
- [scmi_nxp_cpu_info](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md)
- [run_mode](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a9e8ef984d7613ef2893cd0fe42dc750b)
- [sleep_mode](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a53cab503c7619e68a5a7b6ddc71bcad8)
- [vector_low](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a7642f805dd7a70bfc216c1526c3e3e7d)
- [vector_high](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#ab817f075da09dea4359ae39a351fc966)
- [scmi_nxp_cpu_sleep_mode_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#gab8211fd0eb9f9be04b441b5488fe8d93)
- [scmi_nxp_cpu_pd_lpm_set](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#ga346872d9b23f24a5f9d2636c6c31b9d8)
- [scmi_nxp_cpu_set_irq_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#gae8e104786d96b8c5a03fc54d201e09ed)
- [scmi_nxp_cpu_reset_vector](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#ga493e417adeb9b63b48613e7ca1f625e8)
- [scmi_nxp_cpu_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html#ga3f3524711a4dacadbb2fcfeae9d5e008)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h.html)
- [scmi_nxp_cpu_info::sleep_mode](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a53cab503c7619e68a5a7b6ddc71bcad8)
- [scmi_nxp_cpu_info::vector_low](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a7642f805dd7a70bfc216c1526c3e3e7d)
- [scmi_nxp_cpu_info::run_mode](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#a9e8ef984d7613ef2893cd0fe42dc750b)
- [scmi_nxp_cpu_info::vector_high](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md#ab817f075da09dea4359ae39a351fc966)
- [scmi_nxp_cpu_irq_mask_config::mask](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a416a9df0f67c107d490725d2eeff8623)
- [scmi_nxp_cpu_irq_mask_config::cpu_id](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a53fb756537e3dd3c997371726b11a3f1)
- [scmi_nxp_cpu_irq_mask_config::num_mask](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a5ffe5fae57289b1d53b8a19ca676f6e9)
- [scmi_nxp_cpu_irq_mask_config::mask_idx](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md#a75f9b3c94bef32627ca92af1c90ca032)
- [scmi_nxp_cpu_pd_lpm_config::cpu_id](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#a44654e7633e8d5705397e994ecf44f60)
- [scmi_nxp_cpu_pd_lpm_config::num_cfg](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#a49f57505c116e79ca16f848662965604)
- [scmi_nxp_cpu_pd_lpm_config::cfgs](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md#ac8f0fdc610b66703baaf1e177b0ef593)
- [scmi_nxp_cpu_sleep_mode_config::cpu_id](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a016a162f5af8523cd84926f1355f62e8)
- [scmi_nxp_cpu_sleep_mode_config::flags](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a24d167a783d564a2639332437c15ce21)
- [scmi_nxp_cpu_sleep_mode_config::sleep_mode](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md#a2f34473f39d718c29209e10e4c45b14b)
- [scmi_nxp_cpu_vector_config::flags](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a02ce732308b9861367bf22be4bebe8fa)
- [scmi_nxp_cpu_vector_config::cpu_id](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a4583b0c5ff44c994c612765b8b91edcc)
- [scmi_nxp_cpu_vector_config::vector_low](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a5d5d72d7ca43ac41a112822578fa3135)
- [scmi_nxp_cpu_vector_config::vector_high](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md#a6ca9bb699b63aec9a15f3259173a07a9)
- [scmi_pd_lpm_settings::ret_mask](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#a18de2ecf5f1d072967eacf7375d9e64c)
- [scmi_pd_lpm_settings::lpm_setting](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#a35c3e1f1f5ab7339b6ae736fb3dcde31)
- [scmi_pd_lpm_settings::domain_id](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md#ae3614c23f92717999d2058ef8636fe7c)

---

[上一章](P153_dma_smartbond.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P155_pinctrl.h_源码浏览.md)
