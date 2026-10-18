---
id: learning.zephyr-docs.flash-reference.page-10
title: Flash公共头文件源码
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Flash公共头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/flash_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P009_Flash公共头文件参考.md)及[本册大纲](大纲.md)。

## 10.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
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
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00061"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
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
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00121"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
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
<a id="l00136"></a>
<a id="foldopen00149"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00157"></a>
<a id="l00163"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00285"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="foldopen00296"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00323"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00345"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="foldopen00527"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00779"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="foldopen00791"></a>
<a id="l00791"></a>
<a id="l00795"></a>
<a id="l00796"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="foldopen00813"></a>
<a id="l00813"></a>
<a id="l00817"></a>
<a id="l00818"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00853"></a>
<a id="l00854"></a>
<a id="l00855"></a>
<a id="l00856"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__flash__interface__backend_html_ga088369ef7593aa7c1fbe4cdad6e5b994"></a>
<a id="agroup__flash__interface__backend_html_ga2178a2338e652396ba9811ca449f4cb5"></a>
<a id="agroup__flash__interface__backend_html_ga2dee3874cb1be4ef4dab599963c30e70"></a>
<a id="agroup__flash__interface__backend_html_ga358404d040b7ef30c8d24106e97bc290"></a>
<a id="agroup__flash__interface__backend_html_ga7576411536217c9ec3e167e7a5ca82a5"></a>
<a id="agroup__flash__interface__backend_html_ga97ab6540136589aaafbe049cf4302285"></a>
<a id="agroup__flash__interface__backend_html_gac7b802015885044df6a1872513b89ab5"></a>
<a id="agroup__flash__interface__backend_html_gacff972cc16c1afa0a85e3118eff0afb2"></a>
<a id="agroup__flash__interface__backend_html_gaf6b0c3aa2b6514ac8936aa0c7fda96ba"></a>
<a id="agroup__flash__interface_html_ga022838332e905b0111d5136dd963889b"></a>
<a id="agroup__flash__interface_html_ga05f9c8b0c1ff7273f71797e7ff799c95"></a>
<a id="agroup__flash__interface_html_ga07b516708224b7a69a5169ef9c5c26e3"></a>
<a id="agroup__flash__interface_html_ga11eda0cdc7be12636a90d2e8c7264e4a"></a>
<a id="agroup__flash__interface_html_ga1649b22ba5c5974060b4a3c44a0e44e2"></a>
<a id="agroup__flash__interface_html_ga275f2346e88b5e4d050dae426f0953fe"></a>
<a id="agroup__flash__interface_html_ga41bfc5eb05a8e73873763c36f3e1ec6f"></a>
<a id="agroup__flash__interface_html_ga471edb53a2b1abe3dff0f4e2d216521e"></a>
<a id="agroup__flash__interface_html_ga5571fbed2babb0036255d7a4d5e66f6c"></a>
<a id="agroup__flash__interface_html_ga760f7d79cb9f23bc0326abfea85808aa"></a>
<a id="agroup__flash__interface_html_ga76d7880cc5e18ca40237736d3bd94324"></a>
<a id="agroup__flash__interface_html_ga847407358a20d3d5918d8ef11657ce2b"></a>
<a id="agroup__flash__interface_html_ga8e9b921299bfb059bf72445a2ffa5a97"></a>
<a id="agroup__flash__interface_html_ga8eeb7135fbe276e7c287d895a91c6116"></a>
<a id="agroup__flash__interface_html_gaa7c9382796aad64da0da683f54600b5f"></a>
<a id="agroup__flash__interface_html_gaadfb323bc1b4efa39e7bc0a048c472a6"></a>
<a id="agroup__flash__interface_html_gaae733082fa92f80261d5895d3f81a98b"></a>
<a id="agroup__flash__interface_html_gabc73e8888dcb8f4f79cd80b8d02a6a2c"></a>
<a id="agroup__flash__interface_html_gadb273ed317e1088b57adcac3385f50a7"></a>
<a id="agroup__flash__interface_html_gae401e7b13d22a0f405e8d2ca0ef33c51"></a>
<a id="agroup__flash__interface_html_gaf750fe20c02758be7e37f36d2d16345e"></a>
<a id="agroup__flash__interface_html_gafc959b0363eb27d6a3237e4288d60979"></a>
<a id="agroup__flash__interface_html_gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7"></a>
<a id="agroup__flash__interface_html_gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb"></a>
<a id="agroup__flash__interface_html_ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342"></a>
<a id="agroup__flash__interface_html_ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd"></a>
<a id="agroup__flash__interface_html_ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructflash__driver__api_html"></a>
<a id="astructflash__driver__api_html_a0d8122a16fe671099cb9c13459fc022c"></a>
<a id="astructflash__driver__api_html_a2696431e3b94db2f8a830e3142a577fc"></a>
<a id="astructflash__driver__api_html_a82b03b535d86e98c083b701176a5556b"></a>
<a id="astructflash__driver__api_html_a8914c40aef441921123ee8ff6aee94c2"></a>
<a id="astructflash__driver__api_html_aa3f58e76ce1a1bacf57d874a4e190480"></a>
<a id="astructflash__driver__api_html_aa59f704dfaa541860983a89731a47302"></a>
<a id="astructflash__driver__api_html_aa799a18761bbe6d43a82dc12a8de44c4"></a>
<a id="astructflash__driver__api_html_acaf3275b42cb048eca00818026f10f15"></a>
<a id="astructflash__driver__api_html_add4026f7bd3a49de6de1dfee7c43d57b"></a>
<a id="astructflash__pages__info_html"></a>
<a id="astructflash__pages__info_html_a1ef4b965caaeed26014a6d6ae85c93c1"></a>
<a id="astructflash__pages__info_html_a5c841987fef1636b83141871456ea867"></a>
<a id="astructflash__pages__info_html_adca463710082164f4323d3011235eb6f"></a>
<a id="astructflash__pages__layout_html"></a>
<a id="astructflash__pages__layout_html_aabdad4d8a197936f7756950bc73326ee"></a>
<a id="astructflash__pages__layout_html_af5e496e680dbe9f4fd2738e6dc2534ec"></a>
<a id="astructflash__parameters_html"></a>
<a id="astructflash__parameters_html_a218b0cbc797572ce096d0d6f55475ff9"></a>
<a id="astructflash__parameters_html_a9795a3e4fae4d7b81745e876f62ab3a8"></a>

```c
/*
 * Copyright (c) 2017-2024 Nordic Semiconductor ASA
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_H_


#include <errno.h>

#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

struct flash_pages_layout {
        size_t pages_count;
        size_t pages_size;
};



struct flash_parameters {
        const size_t write_block_size;

        /* User code should call flash_params_get_ functions on flash_parameters
         * to get capabilities, rather than accessing object contents directly.
         */
        struct {
                /* Device has no explicit erase, so it either erases on
                 * write or does not require it at all.
                 * This also includes devices that support erase but
                 * do not require it.
                 */
                bool no_explicit_erase: 1;

                /* Erased area does not read back as erase_value, for example
                 * because the read path decrypts what is stored.
                 */
                bool erase_value_readback_unsupported: 1;
        } caps;
        uint8_t erase_value;
};

#define FLASH_ERASE_C_EXPLICIT          0x01
#define FLASH_ERASE_CAPS_UNSET          (int)-1
/* The values below are now reserved but not used */
#define FLASH_ERASE_C_SUPPORTED         0x02
#define FLASH_ERASE_C_VAL_BIT           0x04
#define FLASH_ERASE_UNIFORM_PAGE        0x08

static inline
int flash_params_get_erase_cap(const struct flash_parameters *p)
{
#if defined(CONFIG_FLASH_HAS_EXPLICIT_ERASE)
#if defined(CONFIG_FLASH_HAS_NO_EXPLICIT_ERASE)
        return (p->caps.no_explicit_erase) ? 0 : FLASH_ERASE_C_EXPLICIT;
#else
        ARG_UNUSED(p);
        return FLASH_ERASE_C_EXPLICIT;
#endif
#else
        ARG_UNUSED(p);
#endif
        return 0;
}

static inline bool flash_params_erase_value_readable(const struct flash_parameters *p)
{
        return !p->caps.erase_value_readback_unsupported;
}



typedef int (*flash_api_read)(const struct device *dev, off_t offset,
                              void *data,
                              size_t len);
typedef int (*flash_api_write)(const struct device *dev, off_t offset,
                               const void *data, size_t len);

typedef int (*flash_api_erase)(const struct device *dev, off_t offset,
                               size_t size);

#if defined(CONFIG_FLASH_HAS_DRIVER_FILL)
typedef int (*flash_api_fill)(const struct device *dev, uint8_t val,
                              off_t offset, size_t size);
#endif /* CONFIG_FLASH_HAS_DRIVER_FILL */

typedef int (*flash_api_get_size)(const struct device *dev, uint64_t *size);

typedef const struct flash_parameters* (*flash_api_get_parameters)(const struct device *dev);

typedef void (*flash_api_pages_layout)(const struct device *dev,
                                       const struct flash_pages_layout **layout,
                                       size_t *layout_size);

typedef int (*flash_api_sfdp_read)(const struct device *dev, off_t offset,
                                   void *data, size_t len);
typedef int (*flash_api_read_jedec_id)(const struct device *dev, uint8_t *id);
typedef int (*flash_api_ex_op)(const struct device *dev, uint16_t code,
                               const uintptr_t in, void *out);

__subsystem struct flash_driver_api {
        flash_api_read read;
        flash_api_write write;
        flash_api_erase erase;
#if defined(CONFIG_FLASH_HAS_DRIVER_FILL)
        flash_api_fill fill;
#endif /* CONFIG_FLASH_HAS_DRIVER_FILL */
        flash_api_get_parameters get_parameters;
        flash_api_get_size get_size;
#if defined(CONFIG_FLASH_PAGE_LAYOUT) || defined(__DOXYGEN__)
        flash_api_pages_layout page_layout;
#endif /* CONFIG_FLASH_PAGE_LAYOUT */
#if defined(CONFIG_FLASH_JESD216_API) || defined(__DOXYGEN__)
        flash_api_sfdp_read sfdp_read;
        flash_api_read_jedec_id read_jedec_id;
#endif /* CONFIG_FLASH_JESD216_API */
#if defined(CONFIG_FLASH_EX_OP_ENABLED) || defined(__DOXYGEN__)
        flash_api_ex_op ex_op;
#endif /* CONFIG_FLASH_EX_OP_ENABLED */
};



__syscall int flash_read(const struct device *dev, off_t offset, void *data,
                         size_t len);

static inline int z_impl_flash_read(const struct device *dev, off_t offset,
                                    void *data,
                                    size_t len)
{
        return DEVICE_API_GET(flash, dev)->read(dev, offset, data, len);
}

__syscall int flash_write(const struct device *dev, off_t offset,
                          const void *data,
                          size_t len);

static inline int z_impl_flash_write(const struct device *dev, off_t offset,
                                     const void *data, size_t len)
{
        return DEVICE_API_GET(flash, dev)->write(dev, offset, data, len);
}

__syscall int flash_erase(const struct device *dev, off_t offset, size_t size);

static inline int z_impl_flash_erase(const struct device *dev, off_t offset,
                                     size_t size)
{
        int rc = -ENOSYS;

        const struct flash_driver_api *api = DEVICE_API_GET(flash, dev);

        if (api->erase != NULL) {
                rc = api->erase(dev, offset, size);
        }

        return rc;
}

__syscall int flash_get_size(const struct device *dev, uint64_t *size);

static inline int z_impl_flash_get_size(const struct device *dev, uint64_t *size)
{
        int rc = -ENOSYS;
        const struct flash_driver_api *api = DEVICE_API_GET(flash, dev);

        if (api->get_size != NULL) {
                rc = api->get_size(dev, size);
        }

        return rc;
}

__syscall int flash_fill(const struct device *dev, uint8_t val, off_t offset, size_t size);

__syscall int flash_flatten(const struct device *dev, off_t offset, size_t size);

struct flash_pages_info {
        off_t start_offset;
        size_t size;
        uint32_t index;
};

#if defined(CONFIG_FLASH_PAGE_LAYOUT) || defined(__DOXYGEN__)
__syscall int flash_get_page_info_by_offs(const struct device *dev,
                                          off_t offset,
                                          struct flash_pages_info *info);

__syscall int flash_get_page_info_by_idx(const struct device *dev,
                                         uint32_t page_index,
                                         struct flash_pages_info *info);

__syscall size_t flash_get_page_count(const struct device *dev);

typedef bool (*flash_page_cb)(const struct flash_pages_info *info, void *data);

void flash_page_foreach(const struct device *dev, flash_page_cb cb,
                        void *data);
#endif /* CONFIG_FLASH_PAGE_LAYOUT */

#if defined(CONFIG_FLASH_JESD216_API) || defined(__DOXYGEN__)
__syscall int flash_sfdp_read(const struct device *dev, off_t offset,
                              void *data, size_t len);

static inline int z_impl_flash_sfdp_read(const struct device *dev,
                                         off_t offset,
                                         void *data, size_t len)
{
        int rv = -ENOTSUP;
        const struct flash_driver_api *api = DEVICE_API_GET(flash, dev);

        if (api->sfdp_read != NULL) {
                rv = api->sfdp_read(dev, offset, data, len);
        }
        return rv;
}

__syscall int flash_read_jedec_id(const struct device *dev, uint8_t *id);

static inline int z_impl_flash_read_jedec_id(const struct device *dev,
                                             uint8_t *id)
{
        int rv = -ENOTSUP;
        const struct flash_driver_api *api = DEVICE_API_GET(flash, dev);

        if (api->read_jedec_id != NULL) {
                rv = api->read_jedec_id(dev, id);
        }
        return rv;
}
#endif /* CONFIG_FLASH_JESD216_API */

__syscall size_t flash_get_write_block_size(const struct device *dev);

static inline size_t z_impl_flash_get_write_block_size(const struct device *dev)
{
        return DEVICE_API_GET(flash, dev)->get_parameters(dev)->write_block_size;
}


__syscall const struct flash_parameters *flash_get_parameters(const struct device *dev);

static inline const struct flash_parameters *z_impl_flash_get_parameters(const struct device *dev)
{
        return DEVICE_API_GET(flash, dev)->get_parameters(dev);
}

__syscall int flash_ex_op(const struct device *dev, uint16_t code,
                          const uintptr_t in, void *out);

__syscall int flash_copy(const struct device *src_dev, off_t src_offset,
                         const struct device *dst_dev, off_t dst_offset, off_t size, uint8_t *buf,
                         size_t buf_size);
/*
 *  Extended operation interface provides flexible way for supporting flash
 *  controller features. Code space is divided equally into Zephyr codes
 *  (MSb == 0) and vendor codes (MSb == 1). This way we can easily add extended
 *  operations to the drivers without cluttering the API or problems with API
 *  incompatibility. Extended operation can be promoted from vendor codes to
 *  Zephyr codes if the feature is available in most flash controllers and
 *  can be represented in the same way.
 *
 *  It's not forbidden to have operation in Zephyr codes and vendor codes for
 *  the same functionality. In this case, vendor operation could provide more
 *  specific access when abstraction in Zephyr counterpart is insufficient.
 */
#define FLASH_EX_OP_VENDOR_BASE 0x8000
#define FLASH_EX_OP_IS_VENDOR(c) ((c) & FLASH_EX_OP_VENDOR_BASE)

enum flash_ex_op_types {
        FLASH_EX_OP_RESET = 0,

        FLASH_EX_OP_IS_BAD_BLOCK = 1,

        FLASH_EX_OP_MARK_BAD_BLOCK = 2,
};

enum flash_block_status {
        FLASH_BLOCK_GOOD = 0,

        FLASH_BLOCK_BAD = 1,
};

static inline int z_impl_flash_ex_op(const struct device *dev, uint16_t code,
                                     const uintptr_t in, void *out)
{
#if defined(CONFIG_FLASH_EX_OP_ENABLED)
        const struct flash_driver_api *api = DEVICE_API_GET(flash, dev);

        if (api->ex_op == NULL) {
                return -ENOTSUP;
        }

        return api->ex_op(dev, code, in, out);
#else
        ARG_UNUSED(dev);
        ARG_UNUSED(code);
        ARG_UNUSED(in);
        ARG_UNUSED(out);

        return -ENOSYS;
#endif /* CONFIG_FLASH_EX_OP_ENABLED */
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/flash.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_H_ */
```

## 10.2\_可见注释译文（Comments）

1. 版权为2017–2024年Nordic Semiconductor ASA及2016年Intel Corporation；许可证为Apache-2.0。代码块中的法律署名保持原样。

2. 用户代码应对flash_parameters调用flash_params_get_系列函数取得能力，而不是直接读取对象内部内容。

3. 设备不需要显式擦除（Explicit Erase）：可能在写入时擦除，也可能完全无需擦除；还包括支持擦除、但并不要求擦除的设备。

4. 已擦除区域无法读回erase_value，例如读取路径会解密存储的内容。

5. 下面的值目前保留，尚未使用。

6. 结束CONFIG_FLASH_HAS_DRIVER_FILL控制的条件编译区域。

7. 结束CONFIG_FLASH_HAS_DRIVER_FILL控制的条件编译区域。

8. 结束CONFIG_FLASH_PAGE_LAYOUT控制的条件编译区域。

9. 结束CONFIG_FLASH_JESD216_API控制的条件编译区域。

10. 结束CONFIG_FLASH_EX_OP_ENABLED控制的条件编译区域。

11. 结束CONFIG_FLASH_PAGE_LAYOUT控制的条件编译区域。

12. 结束CONFIG_FLASH_JESD216_API控制的条件编译区域。

13. 扩展操作接口（Extended Operation Interface）以灵活方式支持闪存控制器功能。操作码空间平均划分为Zephyr操作码（最高有效位，Most Significant Bit，MSb为0）与厂商操作码（MSb为1），这样可以向驱动增加扩展操作，同时避免接口杂乱或API不兼容。如果某功能在大多数闪存控制器上都可用，并且能用相同方式表达，可以从厂商操作码提升为Zephyr操作码。同一种功能同时使用Zephyr操作码和厂商操作码并不被禁止；当Zephyr抽象不足时，厂商操作可以提供更具体的访问。

14. 结束CONFIG_FLASH_EX_OP_ENABLED控制的条件编译区域。

15. 结束ZEPHYR_INCLUDE_DRIVERS_FLASH_H_头文件包含保护（Header Include Guard）。

## 10.3\_源码跟踪译注

> 译注——条件与公开参考：本源码页包含CONFIG_FLASH_HAS_DRIVER_FILL下的flash_api_fill类型和fill成员，而[头文件参考](P009_Flash公共头文件参考.md)及[后端API](P002_Flash驱动后端接口.md)未列出它们。去掉注释与展示空白后，本次源码浏览页的代码与读取的官方main头文件一致，不能据此判断为版本不同。page_layout、sfdp_read、read_jedec_id和ex_op分别受其配置条件控制；其中__DOXYGEN__分支用于文档展示，不表示实际构建一定包含该成员。

> 译注——调用转发：公共系统调用（System Call）的内联实现取得设备的flash_driver_api后转发给驱动。get_size、sfdp_read、read_jedec_id等可选回调为空时返回-ENOTSUP；ex_op未启用时的包装返回-ENOSYS。fill回调的参数依次为设备、填充值、设备内偏移和长度；它是否被使用还要看辅助实现及配置，详见[公共接口](P001_Flash公共接口.md)。

本仓库相对定位为[flash.h](../../../include/zephyr/drivers/flash.h)，已核对的上游来源为[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash.h)。本地源码、源码网页与main不能在其他时间自动视为同版本。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 10.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P009_Flash公共头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [flash_pages_layout](P006_Flash页布局结构.md)
- [pages_count](P006_Flash页布局结构.md#af5e496e680dbe9f4fd2738e6dc2534ec)
- [pages_size](P006_Flash页布局结构.md#aabdad4d8a197936f7756950bc73326ee)
- [flash_parameters](P004_Flash存储参数结构.md)
- [write_block_size](P004_Flash存储参数结构.md#a9795a3e4fae4d7b81745e876f62ab3a8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [erase_value](P004_Flash存储参数结构.md#a218b0cbc797572ce096d0d6f55475ff9)
- [flash_params_get_erase_cap](P001_Flash公共接口.md#gabc73e8888dcb8f4f79cd80b8d02a6a2c)
- [FLASH_ERASE_C_EXPLICIT](P001_Flash公共接口.md#ga760f7d79cb9f23bc0326abfea85808aa)
- [flash_params_erase_value_readable](P001_Flash公共接口.md#ga1649b22ba5c5974060b4a3c44a0e44e2)
- [flash_api_read](P002_Flash驱动后端接口.md#ga358404d040b7ef30c8d24106e97bc290)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [flash_api_write](P002_Flash驱动后端接口.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)
- [flash_api_erase](P002_Flash驱动后端接口.md#ga2178a2338e652396ba9811ca449f4cb5)
- [flash_api_get_size](P002_Flash驱动后端接口.md#ga97ab6540136589aaafbe049cf4302285)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [flash_api_pages_layout](P002_Flash驱动后端接口.md#ga7576411536217c9ec3e167e7a5ca82a5)
- [flash_api_sfdp_read](P002_Flash驱动后端接口.md#gac7b802015885044df6a1872513b89ab5)
- [flash_api_read_jedec_id](P002_Flash驱动后端接口.md#ga088369ef7593aa7c1fbe4cdad6e5b994)
- [flash_api_ex_op](P002_Flash驱动后端接口.md#gacff972cc16c1afa0a85e3118eff0afb2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [flash_driver_api](P007_Flash驱动操作结构.md)
- [read](P007_Flash驱动操作结构.md#aa3f58e76ce1a1bacf57d874a4e190480)
- [write](P007_Flash驱动操作结构.md#aa799a18761bbe6d43a82dc12a8de44c4)
- [erase](P007_Flash驱动操作结构.md#acaf3275b42cb048eca00818026f10f15)
- [flash_api_get_parameters](P002_Flash驱动后端接口.md#ga2dee3874cb1be4ef4dab599963c30e70)
- [get_parameters](P007_Flash驱动操作结构.md#a2696431e3b94db2f8a830e3142a577fc)
- [get_size](P007_Flash驱动操作结构.md#aa59f704dfaa541860983a89731a47302)
- [page_layout](P007_Flash驱动操作结构.md#a82b03b535d86e98c083b701176a5556b)
- [sfdp_read](P007_Flash驱动操作结构.md#a0d8122a16fe671099cb9c13459fc022c)
- [read_jedec_id](P007_Flash驱动操作结构.md#add4026f7bd3a49de6de1dfee7c43d57b)
- [ex_op](P007_Flash驱动操作结构.md#a8914c40aef441921123ee8ff6aee94c2)
- [flash_read](P001_Flash公共接口.md#gaa7c9382796aad64da0da683f54600b5f)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [flash_write](P001_Flash公共接口.md#ga76d7880cc5e18ca40237736d3bd94324)
- [flash_erase](P001_Flash公共接口.md#ga05f9c8b0c1ff7273f71797e7ff799c95)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [flash_get_size](P001_Flash公共接口.md#ga471edb53a2b1abe3dff0f4e2d216521e)
- [flash_fill](P001_Flash公共接口.md#ga022838332e905b0111d5136dd963889b)
- [flash_flatten](P001_Flash公共接口.md#ga11eda0cdc7be12636a90d2e8c7264e4a)
- [flash_pages_info](P005_Flash页信息结构.md)
- [start_offset](P005_Flash页信息结构.md#a5c841987fef1636b83141871456ea867)
- [size](P005_Flash页信息结构.md#a1ef4b965caaeed26014a6d6ae85c93c1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [index](P005_Flash页信息结构.md#adca463710082164f4323d3011235eb6f)
- [flash_get_page_info_by_offs](P001_Flash公共接口.md#gafc959b0363eb27d6a3237e4288d60979)
- [flash_get_page_info_by_idx](P001_Flash公共接口.md#gaae733082fa92f80261d5895d3f81a98b)
- [flash_get_page_count](P001_Flash公共接口.md#gaf750fe20c02758be7e37f36d2d16345e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [flash_page_cb](P001_Flash公共接口.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)
- [flash_page_foreach](P001_Flash公共接口.md#ga275f2346e88b5e4d050dae426f0953fe)
- [flash_sfdp_read](P001_Flash公共接口.md#ga8e9b921299bfb059bf72445a2ffa5a97)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [flash_read_jedec_id](P001_Flash公共接口.md#gadb273ed317e1088b57adcac3385f50a7)
- [flash_get_write_block_size](P001_Flash公共接口.md#gaadfb323bc1b4efa39e7bc0a048c472a6)
- [flash_get_parameters](P001_Flash公共接口.md#ga07b516708224b7a69a5169ef9c5c26e3)
- [flash_ex_op](P001_Flash公共接口.md#ga5571fbed2babb0036255d7a4d5e66f6c)
- [flash_copy](P001_Flash公共接口.md#ga847407358a20d3d5918d8ef11657ce2b)
- [flash_ex_op_types](P001_Flash公共接口.md#gae401e7b13d22a0f405e8d2ca0ef33c51)
- [FLASH_EX_OP_RESET](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd)
- [FLASH_EX_OP_IS_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a56ea1df211a928c8bd2ade61df9cce34)
- [FLASH_EX_OP_MARK_BAD_BLOCK](P001_Flash公共接口.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a22b688ac088aead1f989ecb656fc7342)
- [flash_block_status](P001_Flash公共接口.md#ga8eeb7135fbe276e7c287d895a91c6116)
- [FLASH_BLOCK_GOOD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a1974162ef10f5b83bb8428e3c7c513c7)
- [FLASH_BLOCK_BAD](P001_Flash公共接口.md#gga8eeb7135fbe276e7c287d895a91c6116a398def014a3982b35e4557f93bfa44bb)

---

[上一章](P009_Flash公共头文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_M95P32扩展操作接口.md)
