---
id: learning.zephyr-docs.api-source-reference.page-397
title: intc_nxp_gint.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第397章\_intc\_nxp\_gint.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html)。

## 397.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aintc__nxp__gint_8h_html_a04d305e582dc9babc28a5d01edd9963d"></a>
<a id="aintc__nxp__gint_8h_html_a07f2264ca2366594a571858cc5ee6b9a"></a>
<a id="aintc__nxp__gint_8h_html_a07f2264ca2366594a571858cc5ee6b9aa9199715bc7fa26a7936e167b57dc81b6"></a>
<a id="aintc__nxp__gint_8h_html_a07f2264ca2366594a571858cc5ee6b9aaed72091eeef574afdae0d9b576980bad"></a>
<a id="aintc__nxp__gint_8h_html_a3ca522907628e534477c45e1faef89cf"></a>
<a id="aintc__nxp__gint_8h_html_a5371cc92fc4a3516784601a0f060699e"></a>
<a id="aintc__nxp__gint_8h_html_a5e4f2bdb5749f1a582ef3ee407cb8bdc"></a>
<a id="aintc__nxp__gint_8h_html_a76a33bc514ae1e0b7923ef8610614ddb"></a>
<a id="aintc__nxp__gint_8h_html_a9df8c215c7b27faef4ce781d253a217a"></a>
<a id="aintc__nxp__gint_8h_html_ab2bb2c06c72c6dd81a3e6616296d3d7e"></a>
<a id="aintc__nxp__gint_8h_html_abc9f321deac34cacd128dc16c2db3df6"></a>
<a id="aintc__nxp__gint_8h_html_abc9f321deac34cacd128dc16c2db3df6a3a05e0f414cd4401b2858650598a3f66"></a>
<a id="aintc__nxp__gint_8h_html_abc9f321deac34cacd128dc16c2db3df6a68ac19cd2c60a8b5413a34a5305630f2"></a>
<a id="aintc__nxp__gint_8h_html_ad046213e6efeea292323f1af3b3df4fa"></a>
<a id="aintc__nxp__gint_8h_html_ad046213e6efeea292323f1af3b3df4faa98c4639c9ce35ecfd855f8604c8c86b4"></a>
<a id="aintc__nxp__gint_8h_html_ad046213e6efeea292323f1af3b3df4faacdaa397042505f1f90b15ff3c8d4b64d"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructnxp__gint__group__config_html"></a>
<a id="astructnxp__gint__group__config_html_a4a3d57e34c8386775bb0b6302fc2b7c3"></a>
<a id="astructnxp__gint__group__config_html_aac30f37bb02cc8d10cf308b666efd767"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_GINT_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_GINT_H_

#include <zephyr/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
        NXP_GINT_TRIG_EDGE = 0,
        NXP_GINT_TRIG_LEVEL = 1,
} nxp_gint_trigger_type;

typedef enum {
        NXP_GINT_COMB_OR = 0,
        NXP_GINT_COMB_AND = 1,
} nxp_gint_combination_type;

typedef enum {
        NXP_GINT_POL_LOW = 0,
        NXP_GINT_POL_HIGH = 1,
} nxp_gint_polarity_type;

struct nxp_gint_group_config {
        nxp_gint_trigger_type trigger;
        nxp_gint_combination_type combination;
};

typedef void (*nxp_gint_callback_t)(const struct device *dev, void *user_data);

int nxp_gint_configure_group(const struct device *dev,
                             const struct nxp_gint_group_config *config);

int nxp_gint_enable_pin(const struct device *dev, uint8_t port, uint8_t pin,
                        nxp_gint_polarity_type polarity);

int nxp_gint_disable_pin(const struct device *dev, uint8_t port, uint8_t pin);

bool nxp_gint_is_pending(const struct device *dev);

int nxp_gint_clear_pending(const struct device *dev);

int nxp_gint_register_callback(const struct device *dev,
                               nxp_gint_callback_t callback,
                               void *user_data);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_GINT_H_ */
```

## 397.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 135 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_NXP_GINT_H_`。

## 397.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [NXP_GINT_TRIG_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a07f2264ca2366594a571858cc5ee6b9aa9199715bc7fa26a7936e167b57dc81b6)
- [NXP_GINT_TRIG_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a07f2264ca2366594a571858cc5ee6b9aaed72091eeef574afdae0d9b576980bad)
- [nxp_gint_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a07f2264ca2366594a571858cc5ee6b9a)
- [NXP_GINT_COMB_OR](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#abc9f321deac34cacd128dc16c2db3df6a3a05e0f414cd4401b2858650598a3f66)
- [NXP_GINT_COMB_AND](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#abc9f321deac34cacd128dc16c2db3df6a68ac19cd2c60a8b5413a34a5305630f2)
- [nxp_gint_combination_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#abc9f321deac34cacd128dc16c2db3df6)
- [NXP_GINT_POL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#ad046213e6efeea292323f1af3b3df4faacdaa397042505f1f90b15ff3c8d4b64d)
- [NXP_GINT_POL_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#ad046213e6efeea292323f1af3b3df4faa98c4639c9ce35ecfd855f8604c8c86b4)
- [nxp_gint_polarity_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#ad046213e6efeea292323f1af3b3df4fa)
- [nxp_gint_group_config](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md)
- [trigger](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md#a4a3d57e34c8386775bb0b6302fc2b7c3)
- [combination](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md#aac30f37bb02cc8d10cf308b666efd767)
- [nxp_gint_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#ab2bb2c06c72c6dd81a3e6616296d3d7e)
- [device](../device_reference/P002_设备对象结构.md)
- [nxp_gint_configure_group](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a5e4f2bdb5749f1a582ef3ee407cb8bdc)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [nxp_gint_enable_pin](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a3ca522907628e534477c45e1faef89cf)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [nxp_gint_disable_pin](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a76a33bc514ae1e0b7923ef8610614ddb)
- [nxp_gint_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a04d305e582dc9babc28a5d01edd9963d)
- [nxp_gint_clear_pending](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a5371cc92fc4a3516784601a0f060699e)
- [nxp_gint_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a9df8c215c7b27faef4ce781d253a217a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [nxp_gint_group_config::trigger](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md#a4a3d57e34c8386775bb0b6302fc2b7c3)
- [nxp_gint_group_config::combination](../platform_security_model_reference/P022_nxp_gint_group_config_结构体.md#aac30f37bb02cc8d10cf308b666efd767)

---

[上一章](P396_intc_mchp_eic_g1.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P398_intc_nxp_siul2_eirq.h_源码浏览.md)
