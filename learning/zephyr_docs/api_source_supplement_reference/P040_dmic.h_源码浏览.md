---
id: learning.zephyr-docs.api-source-supplement-reference.page-40
title: dmic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_dmic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h.html)。

## 40.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00147"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00227"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="foldopen00258"></a>
<a id="l00258"></a>
<a id="l00262"></a>
<a id="l00266"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00276"></a>
<a id="foldopen00289"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="foldopen00308"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="foldopen00331"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="foldopen00347"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="foldopen00363"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="foldopen00384"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__audio__dmic__interface__backend_html_ga777e407deafee37c7f26039dd3144c4a"></a>
<a id="agroup__audio__dmic__interface__backend_html_gab53ad4a4dddc12cdc7d012774f0ef63a"></a>
<a id="agroup__audio__dmic__interface__backend_html_gaf8f2d714a8e93df2178b19ba46533909"></a>
<a id="agroup__audio__dmic__interface_html_ga09fc7074323c2f3115b06c5212d21fc7"></a>
<a id="agroup__audio__dmic__interface_html_ga24aae0a7871b3bd31b130061feeefc14"></a>
<a id="agroup__audio__dmic__interface_html_ga5d1fcefaf085962d779b8082b3480cbd"></a>
<a id="agroup__audio__dmic__interface_html_ga74b51bddaa175c518d45211f936d08e6"></a>
<a id="agroup__audio__dmic__interface_html_ga7c2067bbb1e07fa8afe315f91a127991"></a>
<a id="agroup__audio__dmic__interface_html_gaa1fded235751a71632965011a62ddead"></a>
<a id="agroup__audio__dmic__interface_html_gac99a4f579b6aa45bb6cce1f797247a23"></a>
<a id="agroup__audio__dmic__interface_html_gaf5abf489fe6ed18c2daea5d918aa2f80"></a>
<a id="agroup__audio__dmic__interface_html_gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa"></a>
<a id="agroup__audio__dmic__interface_html_gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5"></a>
<a id="agroup__audio__dmic__interface_html_gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804"></a>
<a id="agroup__audio__dmic__interface_html_gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79"></a>
<a id="agroup__audio__dmic__interface_html_gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23"></a>
<a id="agroup__audio__dmic__interface_html_gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0"></a>
<a id="agroup__audio__dmic__interface_html_gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba"></a>
<a id="agroup__audio__dmic__interface_html_ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructdevice_html"></a>
<a id="astructdmic__cfg_html"></a>
<a id="astructdmic__cfg_html_a90f08070236a8e2c07c30edc54c687a5"></a>
<a id="astructdmic__cfg_html_aaef2d2b475ce65d18c48d60cd1d393c4"></a>
<a id="astructdmic__cfg_html_abac7595e0a03cf976d8359a86259f54b"></a>
<a id="astructdmic__driver__api_html"></a>
<a id="astructdmic__driver__api_html_a58d828a7da4feb293b5805f62b30ea78"></a>
<a id="astructdmic__driver__api_html_ac6cf5dd47f26ba6fe555969d6a724a4a"></a>
<a id="astructdmic__driver__api_html_add04e9c034726b05d8e02681be04ddb5"></a>
<a id="astructpcm__stream__cfg_html"></a>
<a id="astructpcm__stream__cfg_html_a3c224ba6f6c6fa7a128a739b6f1c36bf"></a>
<a id="astructpcm__stream__cfg_html_a64a94db251a8ff9358040bc23cba6de5"></a>
<a id="astructpcm__stream__cfg_html_a7d9fd0039bc25de292f35f60c99c6615"></a>
<a id="astructpcm__stream__cfg_html_ade324dcfe8604fcb94400544ddb4517e"></a>
<a id="astructpcm__stream__cfg_html_ae6e3790576f910943b0383f4731a5545"></a>
<a id="astructpdm__chan__cfg_html"></a>
<a id="astructpdm__chan__cfg_html_a028c8cd3dfcf0bfce618ef8937a7b211"></a>
<a id="astructpdm__chan__cfg_html_a11a258f6b21126e1d50c5a3f46b2cad7"></a>
<a id="astructpdm__chan__cfg_html_a3268169aaee14827cb15778fbc44ceb1"></a>
<a id="astructpdm__chan__cfg_html_a34d2e2d03df48e26245835d4df88b60b"></a>
<a id="astructpdm__chan__cfg_html_a7614fefd7976ba7b195afb4e81f7100e"></a>
<a id="astructpdm__chan__cfg_html_a9a91e9341f4c033243effbebd5ffa194"></a>
<a id="astructpdm__chan__cfg_html_aa2518c6f577c3fd92ec009fa134a6185"></a>
<a id="astructpdm__chan__cfg_html_ae1398759382606cc60cf8944a1b9e5f6"></a>
<a id="astructpdm__io__cfg_html"></a>
<a id="astructpdm__io__cfg_html_a14d6d390746f7731c4ff203a4beec5fe"></a>
<a id="astructpdm__io__cfg_html_a4a12d293f2c8edae3e7e5b71646ee55e"></a>
<a id="astructpdm__io__cfg_html_a4f07b2239435b0ac21e1049413d1a03a"></a>
<a id="astructpdm__io__cfg_html_a692d7e838db86ca84558eb3e3170551a"></a>
<a id="astructpdm__io__cfg_html_aa03fbcc1f17fb2597bfa8c1898b74455"></a>
<a id="astructpdm__io__cfg_html_aa242b3383b20e0673ed47eea8450e9a7"></a>
<a id="astructpdm__io__cfg_html_ae308635d30eaee617cb62c03c0255f37"></a>

```c
/*
 * Copyright (c) 2018, Intel Corporation
 *
 * Author:      Seppo Ingalsuo <seppo.ingalsuo@linux.intel.com>
 *              Sathish Kuttan <sathish.k.kuttan@intel.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUDIO_DMIC_H_
#define ZEPHYR_INCLUDE_AUDIO_DMIC_H_




#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>

#ifdef __cplusplus
extern "C" {
#endif

enum dmic_state {
        DMIC_STATE_UNINIT,
        DMIC_STATE_INITIALIZED,
        DMIC_STATE_CONFIGURED,
        DMIC_STATE_ACTIVE,
        DMIC_STATE_PAUSED,
        DMIC_STATE_ERROR,
};

enum dmic_trigger {
        DMIC_TRIGGER_STOP,
        DMIC_TRIGGER_START,
        DMIC_TRIGGER_PAUSE,
        DMIC_TRIGGER_RELEASE,
        DMIC_TRIGGER_RESET,
};

enum pdm_lr {
        PDM_CHAN_LEFT,
        PDM_CHAN_RIGHT,
};

struct pdm_io_cfg {
        uint32_t min_pdm_clk_freq;
        uint32_t max_pdm_clk_freq;
        uint8_t min_pdm_clk_dc;
        uint8_t max_pdm_clk_dc;

        uint8_t pdm_clk_pol;
        uint8_t pdm_data_pol;
        uint32_t pdm_clk_skew;
};

#define PDM_DT_IO_CFG_GET(node_id)                                              \
        {                                                                       \
                .min_pdm_clk_freq = DT_PROP(node_id, clk_frequency_min),        \
                .max_pdm_clk_freq = DT_PROP(node_id, clk_frequency_max),        \
                .min_pdm_clk_dc = DT_PROP(node_id, clk_duty_cycle_min),         \
                .max_pdm_clk_dc = DT_PROP(node_id, clk_duty_cycle_max),         \
        }

#define PDM_DT_HAS_LEFT_CHANNEL(node_id)        DT_PROP(node_id, channel_left)

#define PDM_DT_HAS_RIGHT_CHANNEL(node_id)       DT_PROP(node_id, channel_right)

struct pcm_stream_cfg {
        uint32_t pcm_rate;
        uint8_t pcm_width;
        uint16_t block_size;
        int8_t gain_db;
        struct k_mem_slab *mem_slab;
};

struct pdm_chan_cfg {
        uint32_t req_chan_map_lo;
        uint32_t req_chan_map_hi;

        uint32_t act_chan_map_lo;
        uint32_t act_chan_map_hi;

        uint8_t req_num_chan;
        uint8_t act_num_chan;
        uint8_t req_num_streams;
        uint8_t act_num_streams;
};

struct dmic_cfg {
        struct pdm_io_cfg io;
        struct pcm_stream_cfg *streams;
        struct pdm_chan_cfg channel;
};


typedef int (*dmic_configure_t)(const struct device *dev, struct dmic_cfg *config);

typedef int (*dmic_trigger_t)(const struct device *dev, enum dmic_trigger cmd);

typedef int (*dmic_read_t)(const struct device *dev, uint8_t stream, void **buffer,
                           size_t *size, int32_t timeout);

#define _dmic_ops dmic_driver_api __DEPRECATED_MACRO

__subsystem struct dmic_driver_api {
        dmic_configure_t configure;
        dmic_trigger_t trigger;
        dmic_read_t read;
};


static inline uint32_t dmic_build_channel_map(uint8_t channel, uint8_t pdm,
                enum pdm_lr lr)
{
        return ((((pdm & BIT_MASK(3)) << 1) | lr) <<
                        ((channel & BIT_MASK(3)) * 4U));
}

static inline void dmic_parse_channel_map(uint32_t channel_map_lo,
                uint32_t channel_map_hi, uint8_t channel, uint8_t *pdm, enum pdm_lr *lr)
{
        uint32_t channel_map;

        channel_map = (channel < 8) ? channel_map_lo : channel_map_hi;
        channel_map >>= ((channel & BIT_MASK(3)) * 4U);

        *pdm = (channel_map >> 1) & BIT_MASK(3);
        *lr = (enum pdm_lr) (channel_map & BIT(0));
}

static inline uint32_t dmic_build_clk_skew_map(uint8_t pdm, uint8_t skew)
{
        return ((skew & BIT_MASK(4)) << ((pdm & BIT_MASK(3)) * 4U));
}

static inline int dmic_configure(const struct device *dev,
                                 struct dmic_cfg *cfg)
{
        return DEVICE_API_GET(dmic, dev)->configure(dev, cfg);
}

static inline int dmic_trigger(const struct device *dev,
                               enum dmic_trigger cmd)
{
        return DEVICE_API_GET(dmic, dev)->trigger(dev, cmd);
}

static inline int dmic_read(const struct device *dev, uint8_t stream,
                            void **buffer,
                            size_t *size, int32_t timeout)
{
        return DEVICE_API_GET(dmic, dev)->read(dev, stream, buffer, size, timeout);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUDIO_DMIC_H_ */
```

## 40.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018, Intel Corporation。

作者（Author）：Seppo Ingalsuo <seppo.ingalsuo@linux.intel.com>；Sathish Kuttan <sathish.k.kuttan@intel.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 399 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUDIO_DMIC_H_`。

## 40.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dmic_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [dmic_state](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gac99a4f579b6aa45bb6cce1f797247a23)
- [DMIC_STATE_UNINIT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be)
- [DMIC_STATE_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1)
- [DMIC_STATE_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826)
- [DMIC_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4)
- [DMIC_STATE_PAUSED](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81)
- [DMIC_STATE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)
- [dmic_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga24aae0a7871b3bd31b130061feeefc14)
- [DMIC_TRIGGER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23)
- [DMIC_TRIGGER_START](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa)
- [DMIC_TRIGGER_PAUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5)
- [DMIC_TRIGGER_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804)
- [DMIC_TRIGGER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)
- [pdm_lr](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga7c2067bbb1e07fa8afe315f91a127991)
- [PDM_CHAN_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345)
- [PDM_CHAN_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0)
- [pdm_io_cfg](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [min_pdm_clk_freq](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#ae308635d30eaee617cb62c03c0255f37)
- [max_pdm_clk_freq](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a4f07b2239435b0ac21e1049413d1a03a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [min_pdm_clk_dc](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a14d6d390746f7731c4ff203a4beec5fe)
- [max_pdm_clk_dc](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#aa03fbcc1f17fb2597bfa8c1898b74455)
- [pdm_clk_pol](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a4a12d293f2c8edae3e7e5b71646ee55e)
- [pdm_data_pol](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#aa242b3383b20e0673ed47eea8450e9a7)
- [pdm_clk_skew](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a692d7e838db86ca84558eb3e3170551a)
- [pcm_stream_cfg](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md)
- [pcm_rate](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#ae6e3790576f910943b0383f4731a5545)
- [pcm_width](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a7d9fd0039bc25de292f35f60c99c6615)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [block_size](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a3c224ba6f6c6fa7a128a739b6f1c36bf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [gain_db](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a64a94db251a8ff9358040bc23cba6de5)
- [mem_slab](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#ade324dcfe8604fcb94400544ddb4517e)
- [pdm_chan_cfg](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md)
- [req_chan_map_lo](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a028c8cd3dfcf0bfce618ef8937a7b211)
- [req_chan_map_hi](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a11a258f6b21126e1d50c5a3f46b2cad7)
- [act_chan_map_lo](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a34d2e2d03df48e26245835d4df88b60b)
- [act_chan_map_hi](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a9a91e9341f4c033243effbebd5ffa194)
- [req_num_chan](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#aa2518c6f577c3fd92ec009fa134a6185)
- [act_num_chan](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a3268169aaee14827cb15778fbc44ceb1)
- [req_num_streams](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#ae1398759382606cc60cf8944a1b9e5f6)
- [act_num_streams](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a7614fefd7976ba7b195afb4e81f7100e)
- [dmic_cfg](../audio_video_model_reference/P006_dmic_cfg_结构体.md)
- [io](../audio_video_model_reference/P006_dmic_cfg_结构体.md#abac7595e0a03cf976d8359a86259f54b)
- [streams](../audio_video_model_reference/P006_dmic_cfg_结构体.md#a90f08070236a8e2c07c30edc54c687a5)
- [channel](../audio_video_model_reference/P006_dmic_cfg_结构体.md#aaef2d2b475ce65d18c48d60cd1d393c4)
- [dmic_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gaf8f2d714a8e93df2178b19ba46533909)
- [device](../device_reference/P002_设备对象结构.md)
- [dmic_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#ga777e407deafee37c7f26039dd3144c4a)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [dmic_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface__backend.html#gab53ad4a4dddc12cdc7d012774f0ef63a)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [dmic_driver_api](../audio_video_model_reference/P007_dmic_driver_api_结构体.md)
- [configure](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#a58d828a7da4feb293b5805f62b30ea78)
- [trigger](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#add04e9c034726b05d8e02681be04ddb5)
- [read](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#ac6cf5dd47f26ba6fe555969d6a724a4a)
- [dmic_build_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga5d1fcefaf085962d779b8082b3480cbd)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [dmic_parse_channel_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaa1fded235751a71632965011a62ddead)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [dmic_build_clk_skew_map](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#gaf5abf489fe6ed18c2daea5d918aa2f80)
- [dmic_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga09fc7074323c2f3115b06c5212d21fc7)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [dmic_read](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__dmic__interface.html#ga74b51bddaa175c518d45211f936d08e6)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [dmic_cfg::streams](../audio_video_model_reference/P006_dmic_cfg_结构体.md#a90f08070236a8e2c07c30edc54c687a5)
- [dmic_cfg::channel](../audio_video_model_reference/P006_dmic_cfg_结构体.md#aaef2d2b475ce65d18c48d60cd1d393c4)
- [dmic_cfg::io](../audio_video_model_reference/P006_dmic_cfg_结构体.md#abac7595e0a03cf976d8359a86259f54b)
- [dmic_driver_api::configure](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#a58d828a7da4feb293b5805f62b30ea78)
- [dmic_driver_api::read](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#ac6cf5dd47f26ba6fe555969d6a724a4a)
- [dmic_driver_api::trigger](../audio_video_model_reference/P007_dmic_driver_api_结构体.md#add04e9c034726b05d8e02681be04ddb5)
- [pcm_stream_cfg::block_size](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a3c224ba6f6c6fa7a128a739b6f1c36bf)
- [pcm_stream_cfg::gain_db](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a64a94db251a8ff9358040bc23cba6de5)
- [pcm_stream_cfg::pcm_width](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#a7d9fd0039bc25de292f35f60c99c6615)
- [pcm_stream_cfg::mem_slab](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#ade324dcfe8604fcb94400544ddb4517e)
- [pcm_stream_cfg::pcm_rate](../audio_video_model_reference/P042_pcm_stream_cfg_结构体.md#ae6e3790576f910943b0383f4731a5545)
- [pdm_chan_cfg::req_chan_map_lo](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a028c8cd3dfcf0bfce618ef8937a7b211)
- [pdm_chan_cfg::req_chan_map_hi](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a11a258f6b21126e1d50c5a3f46b2cad7)
- [pdm_chan_cfg::act_num_chan](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a3268169aaee14827cb15778fbc44ceb1)
- [pdm_chan_cfg::act_chan_map_lo](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a34d2e2d03df48e26245835d4df88b60b)
- [pdm_chan_cfg::act_num_streams](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a7614fefd7976ba7b195afb4e81f7100e)
- [pdm_chan_cfg::act_chan_map_hi](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#a9a91e9341f4c033243effbebd5ffa194)
- [pdm_chan_cfg::req_num_chan](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#aa2518c6f577c3fd92ec009fa134a6185)
- [pdm_chan_cfg::req_num_streams](../audio_video_model_reference/P043_pdm_chan_cfg_结构体.md#ae1398759382606cc60cf8944a1b9e5f6)
- [pdm_io_cfg::min_pdm_clk_dc](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a14d6d390746f7731c4ff203a4beec5fe)
- [pdm_io_cfg::pdm_clk_pol](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a4a12d293f2c8edae3e7e5b71646ee55e)
- [pdm_io_cfg::max_pdm_clk_freq](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a4f07b2239435b0ac21e1049413d1a03a)
- [pdm_io_cfg::pdm_clk_skew](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#a692d7e838db86ca84558eb3e3170551a)
- [pdm_io_cfg::max_pdm_clk_dc](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#aa03fbcc1f17fb2597bfa8c1898b74455)
- [pdm_io_cfg::pdm_data_pol](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#aa242b3383b20e0673ed47eea8450e9a7)
- [pdm_io_cfg::min_pdm_clk_freq](../audio_video_model_reference/P044_pdm_io_cfg_结构体.md#ae308635d30eaee617cb62c03c0255f37)

---

[上一章](P039_dfu_cli.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P041_display.h_源码浏览.md)
