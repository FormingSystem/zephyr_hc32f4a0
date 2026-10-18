---
id: learning.zephyr-docs.api-source-reference.page-152
title: crc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第152章\_crc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h.html)。

## 152.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00040"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00109"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00140"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00161"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00187"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00281"></a>
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
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__crc__interface__backend_html_ga7d6a2a6b119a8fb51d91e6f5f6269af7"></a>
<a id="agroup__crc__interface__backend_html_ga8babc96e0e656e3974c5e3df32f59107"></a>
<a id="agroup__crc__interface__backend_html_gadaec1299bbc8b5a03e4b724b32064abc"></a>
<a id="agroup__crc__interface_html_ga45ff64f03c4bfadd47ba66ce944c09bf"></a>
<a id="agroup__crc__interface_html_ga7c6663d361406882a73e8ba171840adc"></a>
<a id="agroup__crc__interface_html_ga938a05769aa6a61c22217611fb375218"></a>
<a id="agroup__crc__interface_html_gab144200cba95d6cc08c85cf9c5c1dd91"></a>
<a id="agroup__crc__interface_html_gab463a891df58c677e5cafb160dfdb9a3"></a>
<a id="agroup__crc__interface_html_gae6f2adfd858b18765b2e58d8135c28fa"></a>
<a id="agroup__crc__interface_html_gaed8caf868b83c4ea1271a9f5ab6abd35"></a>
<a id="agroup__crc__interface_html_gaf5e71e99b5838e4b21f30e4b2fb4a684"></a>
<a id="agroup__crc__interface_html_ggab463a891df58c677e5cafb160dfdb9a3a2b46dc7210559c77073ad46d5757c7a2"></a>
<a id="agroup__crc__interface_html_ggab463a891df58c677e5cafb160dfdb9a3ad3b521b0f1ec5fc7760f22f318b68c56"></a>
<a id="agroup__crc_html_gabc40e4ffd6da1175eb8ee8573a527edd"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga8368025077a0385849d6817b2007c095"></a>
<a id="agroup__system__errno_html_gadd669d31505a077f769cff8e66c780b3"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructcrc__ctx_html"></a>
<a id="astructcrc__ctx_html_a332fc129740671c28628dad7a86d3626"></a>
<a id="astructcrc__ctx_html_a4f30eca04c874cf473f48c0324fab4ae"></a>
<a id="astructcrc__ctx_html_ac1319345dc28aed6c72422e3e076d3cd"></a>
<a id="astructcrc__ctx_html_aca061dba391e5b236f6ad426815248ba"></a>
<a id="astructcrc__ctx_html_aee1dc43966d4f418139be8d52f9fdcba"></a>
<a id="astructcrc__ctx_html_afdbc947c22f2a0c048d841ef1ce50cd6"></a>
<a id="astructcrc__driver__api_html"></a>
<a id="astructcrc__driver__api_html_a644cf87e1a1f1105dd0bbbcbe66be32b"></a>
<a id="astructcrc__driver__api_html_a82cb49e5025deedbc80159e5d5817a89"></a>
<a id="astructcrc__driver__api_html_abf45e92362c5cb1d3c2e6503eea0a974"></a>
<a id="astructdevice_html"></a>
<a id="asys_2crc_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Brill Power Ltd.
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CRC_H
#define ZEPHYR_INCLUDE_DRIVERS_CRC_H

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/crc.h>

#ifdef __cplusplus
extern "C" {
#endif



#define CRC_FLAG_REVERSE_INPUT BIT(0)

#define CRC_FLAG_REVERSE_OUTPUT BIT(1)



#define CRC4_INIT_VAL 0x0

#define CRC4_TI_INIT_VAL 0x0

#define CRC7_BE_INIT_VAL 0x0

#define CRC8_INIT_VAL 0x0

#define CRC8_CCITT_INIT_VAL 0xFF

#define CRC8_ROHC_INIT_VAL 0xFF

#define CRC16_INIT_VAL 0x0

#define CRC16_ANSI_INIT_VAL 0x0

#define CRC16_CCITT_INIT_VAL 0x0000

#define CRC16_ITU_T_INIT_VAL 0x0000

#define CRC24_PGP_INIT_VALUE 0x00B704CEU

#define CRC32_C_INIT_VAL 0xFFFFFFFFU

#define CRC32_IEEE_INIT_VAL 0xFFFFFFFFU

#define CRC32_K_4_2_INIT_VAL 0xFFFFFFFFU

#define CRC32_MPEG2_INIT_VAL 0xFFFFFFFFU



enum crc_state {
        CRC_STATE_IDLE = 0,
        CRC_STATE_IN_PROGRESS
};

typedef uint32_t crc_init_val_t;

typedef uint32_t crc_poly_t;

typedef uint32_t crc_result_t;


struct crc_ctx {
        enum crc_type type;
        enum crc_state state;
        uint32_t reversed;
        crc_poly_t polynomial;
        crc_init_val_t seed;
        crc_result_t result;
};


typedef int (*crc_api_begin)(const struct device *dev, struct crc_ctx *ctx);

typedef int (*crc_api_update)(const struct device *dev, struct crc_ctx *ctx, const void *buffer,
                              size_t bufsize);

typedef int (*crc_api_finish)(const struct device *dev, struct crc_ctx *ctx);

__subsystem struct crc_driver_api {
        crc_api_begin begin;
        crc_api_update update;
        crc_api_finish finish;
};


__syscall int crc_begin(const struct device *dev, struct crc_ctx *ctx);

static inline int z_impl_crc_begin(const struct device *dev, struct crc_ctx *ctx)
{
        const struct crc_driver_api *api = DEVICE_API_GET(crc, dev);

        if (api->begin == NULL) {
                return -ENOSYS;
        }

        return api->begin(dev, ctx);
}

__syscall int crc_update(const struct device *dev, struct crc_ctx *ctx, const void *buffer,
                         size_t bufsize);

static inline int z_impl_crc_update(const struct device *dev, struct crc_ctx *ctx,
                                    const void *buffer, size_t bufsize)
{
        const struct crc_driver_api *api = DEVICE_API_GET(crc, dev);

        if (api->update == NULL) {
                return -ENOSYS;
        }

        return api->update(dev, ctx, buffer, bufsize);
}

__syscall int crc_finish(const struct device *dev, struct crc_ctx *ctx);

static inline int z_impl_crc_finish(const struct device *dev, struct crc_ctx *ctx)
{
        const struct crc_driver_api *api = DEVICE_API_GET(crc, dev);

        if (api->finish == NULL) {
                return -ENOSYS;
        }

        return api->finish(dev, ctx);
}

static inline int crc_verify(struct crc_ctx *ctx, crc_result_t expected)
{
        if (ctx == NULL) {
                return -EINVAL;
        }

        if (ctx->state == CRC_STATE_IN_PROGRESS) {
                return -EBUSY;
        }

        if (expected != ctx->result) {
                return -EPERM;
        }

        return 0;
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/crc.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_CRC_H */
```

## 152.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Brill Power Ltd.。

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 308 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CRC_H`。

## 152.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/crc.h](../data_utilities/P004_CRC系统头文件.md)
- [crc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab463a891df58c677e5cafb160dfdb9a3)
- [CRC_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3ad3b521b0f1ec5fc7760f22f318b68c56)
- [CRC_STATE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3a2b46dc7210559c77073ad46d5757c7a2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [crc_init_val_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga45ff64f03c4bfadd47ba66ce944c09bf)
- [crc_poly_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga938a05769aa6a61c22217611fb375218)
- [crc_result_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc)
- [crc_ctx](../hardware/P046_CRC上下文结构.md)
- [crc_type](../data_utilities/P003_CRC计算接口.md#gabc40e4ffd6da1175eb8ee8573a527edd)
- [type](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#afdbc947c22f2a0c048d841ef1ce50cd6)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a4f30eca04c874cf473f48c0324fab4ae)
- [reversed](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aca061dba391e5b236f6ad426815248ba)
- [polynomial](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a332fc129740671c28628dad7a86d3626)
- [seed](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#ac1319345dc28aed6c72422e3e076d3cd)
- [result](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aee1dc43966d4f418139be8d52f9fdcba)
- [crc_api_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga8babc96e0e656e3974c5e3df32f59107)
- [device](../device_reference/P002_设备对象结构.md)
- [crc_api_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga7d6a2a6b119a8fb51d91e6f5f6269af7)
- [crc_api_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#gadaec1299bbc8b5a03e4b724b32064abc)
- [crc_driver_api](../hardware/P052_CRC驱动操作结构.md)
- [begin](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#abf45e92362c5cb1d3c2e6503eea0a974)
- [update](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a82cb49e5025deedbc80159e5d5817a89)
- [finish](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a644cf87e1a1f1105dd0bbbcbe66be32b)
- [crc_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gae6f2adfd858b18765b2e58d8135c28fa)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [crc_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaf5e71e99b5838e4b21f30e4b2fb4a684)
- [crc_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab144200cba95d6cc08c85cf9c5c1dd91)
- [crc_verify](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaed8caf868b83c4ea1271a9f5ab6abd35)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [EBUSY](../error_reference/P003_系统错误号公共接口.md#ga8368025077a0385849d6817b2007c095)
- [EPERM](../error_reference/P003_系统错误号公共接口.md#gadd669d31505a077f769cff8e66c780b3)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [crc_ctx::polynomial](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a332fc129740671c28628dad7a86d3626)
- [crc_ctx::state](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a4f30eca04c874cf473f48c0324fab4ae)
- [crc_ctx::seed](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#ac1319345dc28aed6c72422e3e076d3cd)
- [crc_ctx::reversed](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aca061dba391e5b236f6ad426815248ba)
- [crc_ctx::result](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aee1dc43966d4f418139be8d52f9fdcba)
- [crc_ctx::type](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#afdbc947c22f2a0c048d841ef1ce50cd6)
- [crc_driver_api::finish](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a644cf87e1a1f1105dd0bbbcbe66be32b)
- [crc_driver_api::update](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a82cb49e5025deedbc80159e5d5817a89)
- [crc_driver_api::begin](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#abf45e92362c5cb1d3c2e6503eea0a974)
- [crc.h](../data_utilities/P004_CRC系统头文件.md)

---

[上一章](P151_console.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P153_dma_smartbond.h_源码浏览.md)
