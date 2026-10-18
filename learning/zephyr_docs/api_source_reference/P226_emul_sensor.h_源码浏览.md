---
id: learning.zephyr-docs.api-source-reference.page-226
title: emul_sensor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第226章\_emul\_sensor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h.html)。

## 226.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00025"></a>
<a id="l00031"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00053"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00078"></a>
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
<a id="foldopen00111"></a>
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
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="agroup__sensor__emulator__backend_html_ga271513cf5b2b5ee28d5f37e42449ee1e"></a>
<a id="agroup__sensor__emulator__backend_html_ga3bf83e34c2218823386489cf4f1cd84c"></a>
<a id="agroup__sensor__emulator__backend_html_gadb7174783ab8466ab55aebb463fdfdd7"></a>
<a id="agroup__sensor__emulator__backend_html_gadfa5c6618361bb382e5b44dc1a03f735"></a>
<a id="agroup__sensor__emulator__backend_html_gaec1ddd02bc6ff1c66c83ca3f3af98fa8"></a>
<a id="agroup__sensor__interface_html_ga0dcb6842bc969492bd1c9eb49708940b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="aminmax_8h_html_ac6afabdc09a49a433ee19d8a9486056d"></a>
<a id="aminmax_8h_html_affe776513b24d84b39af8ab0930fef7f"></a>
<a id="asensor_8h_html"></a>
<a id="asensor__attribute__types_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructemul_html"></a>
<a id="astructemul_html_ac7e90a7ff00a0c08836821c7d49b7dea"></a>
<a id="astructsensor__chan__spec_html"></a>

```c
/*
 * Copyright (c) 2023 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */


#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/sensor_attribute_types.h>

#include <stdint.h>



__subsystem struct emul_sensor_driver_api {
        int (*set_channel)(const struct emul *target, struct sensor_chan_spec ch,
                           const q31_t *value, int8_t shift);
        int (*get_sample_range)(const struct emul *target, struct sensor_chan_spec ch, q31_t *lower,
                                q31_t *upper, q31_t *epsilon, int8_t *shift);
        int (*set_attribute)(const struct emul *target, struct sensor_chan_spec ch,
                             enum sensor_attribute attribute, const void *value);
        int (*get_attribute_metadata)(const struct emul *target, struct sensor_chan_spec ch,
                                      enum sensor_attribute attribute, q31_t *min, q31_t *max,
                                      q31_t *increment, int8_t *shift);
};

static inline bool emul_sensor_backend_is_supported(const struct emul *target)
{
        return target && target->backend_api;
}

static inline int emul_sensor_backend_set_channel(const struct emul *target,
                                                  struct sensor_chan_spec ch, const q31_t *value,
                                                  int8_t shift)
{
        if (!target || !target->backend_api) {
                return -ENOTSUP;
        }

        struct emul_sensor_driver_api *api = (struct emul_sensor_driver_api *)target->backend_api;

        if (api->set_channel) {
                return api->set_channel(target, ch, value, shift);
        }
        return -ENOTSUP;
}

static inline int emul_sensor_backend_get_sample_range(const struct emul *target,
                                                       struct sensor_chan_spec ch, q31_t *lower,
                                                       q31_t *upper, q31_t *epsilon, int8_t *shift)
{
        if (!target || !target->backend_api) {
                return -ENOTSUP;
        }

        struct emul_sensor_driver_api *api = (struct emul_sensor_driver_api *)target->backend_api;

        if (api->get_sample_range) {
                return api->get_sample_range(target, ch, lower, upper, epsilon, shift);
        }
        return -ENOTSUP;
}

static inline int emul_sensor_backend_set_attribute(const struct emul *target,
                                                    struct sensor_chan_spec ch,
                                                    enum sensor_attribute attribute,
                                                    const void *value)
{
        if (!target || !target->backend_api) {
                return -ENOTSUP;
        }

        struct emul_sensor_driver_api *api = (struct emul_sensor_driver_api *)target->backend_api;

        if (api->set_attribute == NULL) {
                return -ENOTSUP;
        }
        return api->set_attribute(target, ch, attribute, value);
}

static inline int emul_sensor_backend_get_attribute_metadata(const struct emul *target,
                                                             struct sensor_chan_spec ch,
                                                             enum sensor_attribute attribute,
                                                             q31_t *min, q31_t *max,
                                                             q31_t *increment, int8_t *shift)
{
        if (!target || !target->backend_api) {
                return -ENOTSUP;
        }

        struct emul_sensor_driver_api *api = (struct emul_sensor_driver_api *)target->backend_api;

        if (api->get_attribute_metadata == NULL) {
                return -ENOTSUP;
        }
        return api->get_attribute_metadata(target, ch, attribute, min, max, increment, shift);
}

```

## 226.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 226.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h.html)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [zephyr/drivers/sensor_attribute_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [emul_sensor_backend_is_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadb7174783ab8466ab55aebb463fdfdd7)
- [emul](../hardware/P477_仿真器实例结构.md)
- [backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [emul_sensor_backend_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadfa5c6618361bb382e5b44dc1a03f735)
- [sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [emul_sensor_backend_get_sample_range](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga271513cf5b2b5ee28d5f37e42449ee1e)
- [emul_sensor_backend_set_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)
- [emul_sensor_backend_get_attribute_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga3bf83e34c2218823386489cf4f1cd84c)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h.html)
- [emul::backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)

---

[上一章](P225_emul_fuel_gauge.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P227_ene-kb106x-gpio.h_源码浏览.md)
