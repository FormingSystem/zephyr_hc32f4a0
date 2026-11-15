---
id: learning.zephyr-docs.api-source-device-reference.page-29
title: nrf_clock_control.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_nrf\_clock\_control.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h.html)。

## 29.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
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
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
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
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00299"></a>
<a id="l00332"></a>
<a id="foldopen00333"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00372"></a>
<a id="foldopen00373"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00401"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="foldopen00419"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="foldopen00442"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="aclock__control_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a2b0530c13706c66229d35977c6553db9"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__clock__control__interface__backend_html_ga459b95cb726892b95537d15273413099"></a>
<a id="agroup__clock__control__interface_html_gaa7d3935eaaf18902801a7d94859483db"></a>
<a id="agroup__clock__control__nrf_html_ga0ac2c96482c7551b16f1cc4eadd01560"></a>
<a id="agroup__clock__control__nrf_html_ga259dfa1a679d21c4b92ecbf9fdfd3d13"></a>
<a id="agroup__clock__control__nrf_html_ga2da9657c008b903a9131238bde6ed1ac"></a>
<a id="agroup__clock__control__nrf_html_ga3ecff5c6b37ced253c030fd032c61a70"></a>
<a id="agroup__clock__control__nrf_html_ga502110bf4c35eca120f883ba766705b7"></a>
<a id="agroup__clock__control__nrf_html_gaa46e3e407fb02b206772c438a0108634"></a>
<a id="agroup__clock__control__nrf_html_gaadc162ec2c250d17572546d74a08ee7d"></a>
<a id="agroup__clock__control__nrf_html_gadd7ed9d76f521cc2894ba21abc8e4d94"></a>
<a id="agroup__clock__control__nrf_html_gaf334bc4e8b5ca0eb63b2bc4b1d963ac8"></a>
<a id="agroup__clock__control__nrf_html_ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df"></a>
<a id="agroup__clock__control__nrf_html_ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4"></a>
<a id="agroup__clock__control__nrf_html_ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="aonoff_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructonoff__client_html"></a>
<a id="astructonoff__manager_html"></a>

```c
/*
 * Copyright (c) 2016 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NRF_CLOCK_CONTROL_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NRF_CLOCK_CONTROL_H_

#include <zephyr/device.h>
#include <zephyr/sys/onoff.h>
#include <zephyr/drivers/clock_control.h>


#ifdef __cplusplus
extern "C" {
#endif

#ifndef CONFIG_HAS_NORDIC_MULTI_OPTION_CLOCKS

#include <hal/nrf_clock.h>

#if defined(CONFIG_CLOCK_CONTROL_NRF)
enum __deprecated clock_control_nrf_type {
        CLOCK_CONTROL_NRF_TYPE_HFCLK,
        CLOCK_CONTROL_NRF_TYPE_LFCLK,
#if NRF_CLOCK_HAS_HFCLK24M
        CLOCK_CONTROL_NRF_TYPE_HFCLK24M,
#endif
#if NRF_CLOCK_HAS_HFCLK192M
        CLOCK_CONTROL_NRF_TYPE_HFCLK192M,
#endif
#if NRF_CLOCK_HAS_HFCLKAUDIO
        CLOCK_CONTROL_NRF_TYPE_HFCLKAUDIO,
#endif
        CLOCK_CONTROL_NRF_TYPE_COUNT
};

#define CLOCK_CONTROL_NRF_SUBSYS_HF \
        ((clock_control_subsys_t)CLOCK_CONTROL_NRF_TYPE_HFCLK) __DEPRECATED_MACRO
#define CLOCK_CONTROL_NRF_SUBSYS_LF \
        ((clock_control_subsys_t)CLOCK_CONTROL_NRF_TYPE_LFCLK) __DEPRECATED_MACRO
#define CLOCK_CONTROL_NRF_SUBSYS_HF24M \
        ((clock_control_subsys_t)CLOCK_CONTROL_NRF_TYPE_HFCLK24M) __DEPRECATED_MACRO
#define CLOCK_CONTROL_NRF_SUBSYS_HF192M \
        ((clock_control_subsys_t)CLOCK_CONTROL_NRF_TYPE_HFCLK192M) __DEPRECATED_MACRO
#define CLOCK_CONTROL_NRF_SUBSYS_HFAUDIO \
        ((clock_control_subsys_t)CLOCK_CONTROL_NRF_TYPE_HFCLKAUDIO) __DEPRECATED_MACRO


/* Define 32KHz clock source */
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_RC
#define CLOCK_CONTROL_NRF_K32SRC NRF_CLOCK_LFCLK_RC __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_XTAL
#define CLOCK_CONTROL_NRF_K32SRC NRF_CLOCK_LFCLK_XTAL __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_SYNTH
#define CLOCK_CONTROL_NRF_K32SRC NRF_CLOCK_LFCLK_SYNTH __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_LOW_SWING
#define CLOCK_CONTROL_NRF_K32SRC NRF_CLOCK_LFCLK_XTAL_LOW_SWING __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_EXT_FULL_SWING
#define CLOCK_CONTROL_NRF_K32SRC NRF_CLOCK_LFCLK_XTAL_FULL_SWING __DEPRECATED_MACRO
#endif

/* Define 32KHz clock accuracy */
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 0 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_250PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 1 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_150PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 2 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_100PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 3 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_75PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 4 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_50PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 5 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_30PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 6 __DEPRECATED_MACRO
#endif
#ifdef CONFIG_CLOCK_CONTROL_NRF_K32SRC_20PPM
#define CLOCK_CONTROL_NRF_K32SRC_ACCURACY 7 __DEPRECATED_MACRO
#endif


#endif /* defined(CONFIG_CLOCK_CONTROL_NRF) */

enum nrf_lfclk_start_mode {
        CLOCK_CONTROL_NRF_LF_START_NOWAIT,
        CLOCK_CONTROL_NRF_LF_START_AVAILABLE,
        CLOCK_CONTROL_NRF_LF_START_STABLE,
};


void z_nrf_clock_calibration_force_start(void);

int z_nrf_clock_calibration_count(void);

int z_nrf_clock_calibration_skips_count(void);


bool z_nrf_clock_calibration_is_in_progress(void);

#if defined(CONFIG_CLOCK_CONTROL_NRF)
struct onoff_manager __deprecated *z_nrf_clock_control_get_onoff(clock_control_subsys_t sys);
#endif

void z_nrf_clock_control_lf_on(enum nrf_lfclk_start_mode start_mode);

void z_nrf_clock_bt_ctlr_hf_request(void);

void z_nrf_clock_bt_ctlr_hf_release(void);

uint32_t z_nrf_clock_bt_ctlr_hf_get_startup_time_us(void);


#endif /* CONFIG_HAS_NORDIC_MULTI_OPTION_CLOCKS */

#define NRF_CLOCK_CONTROL_FREQUENCY_MAX UINT32_MAX

#define NRF_CLOCK_CONTROL_ACCURACY_MAX      1
#define NRF_CLOCK_CONTROL_ACCURACY_PPM(ppm) (ppm)

#define NRF_CLOCK_CONTROL_PRECISION_HIGH    1
#define NRF_CLOCK_CONTROL_PRECISION_DEFAULT 0

#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ        80000000
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ 11289591
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ     24000000
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ  12287963


/* Internal helper macro to map DT property value to output frequency */
#define _CLOCK_CONTROL_NRF_AUXPLL_MAP_FREQ(freq_val)                      \
        ((freq_val) == NRF_AUXPLL_FREQ_DIV_MIN ?                          \
                       CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ :         \
         (freq_val) == NRF_AUXPLL_FREQ_DIV_AUDIO_44K1 ?                   \
                       CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ :  \
         (freq_val) == NRF_AUXPLL_FREQ_DIV_USB24M ?                       \
                       CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ :      \
         (freq_val) == NRF_AUXPLL_FREQ_DIV_AUDIO_48K ?                    \
                       CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ : 0)


#define CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ(node) \
        COND_CODE_1(DT_NODE_HAS_PROP(node, nordic_frequency), \
                (_CLOCK_CONTROL_NRF_AUXPLL_MAP_FREQ(DT_PROP(node, nordic_frequency))), \
                (0))


struct nrf_clock_spec {
        uint32_t frequency;
        uint16_t accuracy : 15;
        uint16_t precision : 1;
};

__subsystem struct nrf_clock_control_driver_api {
        struct clock_control_driver_api std_api;

        int (*request)(const struct device *dev,
                       const struct nrf_clock_spec *spec,
                       struct onoff_client *cli);
        int (*release)(const struct device *dev,
                       const struct nrf_clock_spec *spec);
        int (*cancel_or_release)(const struct device *dev,
                                 const struct nrf_clock_spec *spec,
                                 struct onoff_client *cli);
        int (*resolve)(const struct device *dev,
                       const struct nrf_clock_spec *req_spec,
                       struct nrf_clock_spec *res_spec);
        int (*get_startup_time)(const struct device *dev,
                                const struct nrf_clock_spec *spec,
                                uint32_t *startup_time_us);
};

DEVICE_API_EXTENDS(nrf_clock_control, clock_control, std_api);


static inline
int nrf_clock_control_request(const struct device *dev,
                              const struct nrf_clock_spec *spec,
                              struct onoff_client *cli)
{
        return DEVICE_API_GET(nrf_clock_control, dev)->request(dev, spec, cli);
}

int nrf_clock_control_request_sync(const struct device *dev,
                                   const struct nrf_clock_spec *spec,
                                   k_timeout_t timeout);

static inline
int nrf_clock_control_release(const struct device *dev,
                              const struct nrf_clock_spec *spec)
{
        return DEVICE_API_GET(nrf_clock_control, dev)->release(dev, spec);
}

static inline
int nrf_clock_control_cancel_or_release(const struct device *dev,
                                        const struct nrf_clock_spec *spec,
                                        struct onoff_client *cli)
{
        return DEVICE_API_GET(nrf_clock_control, dev)->cancel_or_release(dev, spec, cli);
}

static inline int nrf_clock_control_resolve(const struct device *dev,
                                            const struct nrf_clock_spec *req_spec,
                                            struct nrf_clock_spec *res_spec)
{
        const struct nrf_clock_control_driver_api *api = DEVICE_API_GET(nrf_clock_control, dev);

        if (api->resolve == NULL) {
                return -ENOSYS;
        }

        return api->resolve(dev, req_spec, res_spec);
}

static inline int nrf_clock_control_get_startup_time(const struct device *dev,
                                                     const struct nrf_clock_spec *spec,
                                                     uint32_t *startup_time_us)
{
        const struct nrf_clock_control_driver_api *api = DEVICE_API_GET(nrf_clock_control, dev);

        if (api->get_startup_time == NULL) {
                return -ENOSYS;
        }

        return api->get_startup_time(dev, spec, startup_time_us);
}

void nrf_clock_control_hfxo_request(void);

void nrf_clock_control_hfxo_release(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NRF_CLOCK_CONTROL_H_ */
```

## 29.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 78 行

定义 32 kHz 时钟源（Clock Source）。

### 注释 3：原第 95 行

定义 32 kHz 时钟精度（Clock Accuracy）。

### 注释 4：原第 123 行

条件编译（Conditional Compilation）：`defined(CONFIG_CLOCK_CONTROL_NRF)`。

### 注释 5：原第 209 行

条件编译配置（Configuration）标记：`CONFIG_HAS_NORDIC_MULTI_OPTION_CLOCKS`。

### 注释 6：原第 241 行

将设备树属性值（DT Property Value）映射为输出频率（Output Frequency）的内部辅助宏（Internal Helper Macro）。

### 注释 7：原第 485 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_NRF_CLOCK_CONTROL_H_`。

## 29.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/onoff.h](../memory_services/P017_开关服务头文件.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [nrf_lfclk_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaadc162ec2c250d17572546d74a08ee7d)
- [CLOCK_CONTROL_NRF_LF_START_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec)
- [CLOCK_CONTROL_NRF_LF_START_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df)
- [CLOCK_CONTROL_NRF_LF_START_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4)
- [onoff_manager](../memory_services/P020_开关管理器结构.md)
- [clock_control_subsys_t](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaa7d3935eaaf18902801a7d94859483db)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [DEVICE_API_EXTENDS](../device_reference/P007_设备模型头文件参考.md#a2b0530c13706c66229d35977c6553db9)
- [clock_control](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface__backend.html#ga459b95cb726892b95537d15273413099)
- [nrf_clock_control_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga2da9657c008b903a9131238bde6ed1ac)
- [device](../device_reference/P002_设备对象结构.md)
- [onoff_client](../memory_services/P019_开关客户端结构.md)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [nrf_clock_control_request_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaf334bc4e8b5ca0eb63b2bc4b1d963ac8)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [nrf_clock_control_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaa46e3e407fb02b206772c438a0108634)
- [nrf_clock_control_cancel_or_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga3ecff5c6b37ced253c030fd032c61a70)
- [nrf_clock_control_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gadd7ed9d76f521cc2894ba21abc8e4d94)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [nrf_clock_control_get_startup_time](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga0ac2c96482c7551b16f1cc4eadd01560)
- [nrf_clock_control_hfxo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga259dfa1a679d21c4b92ecbf9fdfd3d13)
- [nrf_clock_control_hfxo_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga502110bf4c35eca120f883ba766705b7)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [onoff.h](../memory_services/P017_开关服务头文件.md)

---

[上一章](P028_npcx_fiu_qspi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P030_pinctrl_rcar_common.h_源码浏览.md)
