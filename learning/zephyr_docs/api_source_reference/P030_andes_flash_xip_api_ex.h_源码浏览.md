---
id: learning.zephyr-docs.api-source-reference.page-30
title: andes_flash_xip_api_ex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_andes\_flash\_xip\_api\_ex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h.html)。

## 30.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00041"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00070"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00090"></a>
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
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ga4b46df3b8254c20bf81be3957f9a0d1e"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gabb24a40e5fd9462fe0cd06f426e0583f"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f"></a>
<a id="agroup__andes__flash__xip__ex__op_html_gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa2bfc829bb2e088af96ad309e0ff924c8"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa2dcf42c1425ed5483e3db48733f2eefc"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa5464912c8f396f13e00bb4e7342185a8"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa6211518baeefc2eeeb000757e500c8d3"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa65afd15579c86eb3d60aae8d4b6dee19"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa6c0d9468075b962602fa0cc652a92bc3"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa7e7321429e68649e18743a3d697cf999"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa7e8f108992e34d0cca57cfddde68bd6a"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fa8a3b5bbe3ec17ce470a9636934dd2bce"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583facd50bfc16ae83b41ffcac3d0941a5c00"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583fad48e3482a04cb3aff0bb6afca65cf36b"></a>
<a id="agroup__andes__flash__xip__ex__op_html_ggabb24a40e5fd9462fe0cd06f426e0583faf12149f961944dea851ccc7e494ba190"></a>
<a id="agroup__flash__interface_html_ga67418b2d5cbbec83463dce3d426162e3"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructandes__xip__ex__ops__get__out_html"></a>
<a id="astructandes__xip__ex__ops__get__out_html_a70bbb5025fbfed276ff31b5f0024f32e"></a>
<a id="astructandes__xip__ex__ops__lock__in_html"></a>
<a id="astructandes__xip__ex__ops__lock__in_html_a3d640ec6d0177dbf33670b02a2a36891"></a>
<a id="astructandes__xip__ex__ops__lock__state__out_html"></a>
<a id="astructandes__xip__ex__ops__lock__state__out_html_a58c0503aa43c700ed986362c6f974afa"></a>
<a id="astructandes__xip__ex__ops__mem__read__cmd__in_html"></a>
<a id="astructandes__xip__ex__ops__mem__read__cmd__in_html_aa642d9ed612a34c20332ea0396207bfa"></a>
<a id="astructandes__xip__ex__ops__set__in_html"></a>
<a id="astructandes__xip__ex__ops__set__in_html_a2210892b339e0ab05c27eacef4d84128"></a>
<a id="astructandes__xip__ex__ops__set__in_html_a75b6d154c433edb2f179c50c4b962881"></a>
<a id="astructandes__xip__ex__ops__set__in_html_afb0c626010d671ddb496ac3dcce4e667"></a>

```c
/*
 * Copyright 2025 The ChromiumOS Authors.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_ANDES_FLASH_XIP_API_EX_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_ANDES_FLASH_XIP_API_EX_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/flash.h>

enum flash_andes_xip_ex_ops {
        FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS = FLASH_EX_OP_VENDOR_BASE,
        FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS,
        FLASH_ANDES_XIP_EX_OP_LOCK,
        FLASH_ANDES_XIP_EX_OP_LOCK_STATE,
        FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD,
};

enum flash_andes_xip_mem_rd_cmd {
        FLASH_ANDES_XIP_MEM_RD_CMD_03 = 0,
        FLASH_ANDES_XIP_MEM_RD_CMD_0B = 1,
        FLASH_ANDES_XIP_MEM_RD_CMD_3B = 2,
        FLASH_ANDES_XIP_MEM_RD_CMD_6B = 3,
        FLASH_ANDES_XIP_MEM_RD_CMD_BB = 4,
        FLASH_ANDES_XIP_MEM_RD_CMD_EB = 5,
        FLASH_ANDES_XIP_MEM_RD_CMD_13 = 8,
        FLASH_ANDES_XIP_MEM_RD_CMD_0C = 9,
        FLASH_ANDES_XIP_MEM_RD_CMD_3C = 10,
        FLASH_ANDES_XIP_MEM_RD_CMD_6C = 11,
        FLASH_ANDES_XIP_MEM_RD_CMD_BC = 12,
        FLASH_ANDES_XIP_MEM_RD_CMD_EC = 13,
};

struct andes_xip_ex_ops_get_out {
        uint8_t regs[3];
};

struct andes_xip_ex_ops_set_in {
        uint8_t regs[3];
        uint8_t masks[3];
        bool volatile_write;
};

struct andes_xip_ex_ops_lock_in {
        bool enable;
};

struct andes_xip_ex_ops_lock_state_out {
        bool state;
};

struct andes_xip_ex_ops_mem_read_cmd_in {
        enum flash_andes_xip_mem_rd_cmd cmd;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_ANDES_FLASH_XIP_API_EX_H_ */
```

## 30.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 The ChromiumOS Authors.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 157 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_ANDES_FLASH_XIP_API_EX_H_`。

## 30.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [flash_andes_xip_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ga4b46df3b8254c20bf81be3957f9a0d1e)
- [FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7)
- [FLASH_EX_OP_VENDOR_BASE](../flash_reference/P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)
- [FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f)
- [FLASH_ANDES_XIP_EX_OP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0)
- [FLASH_ANDES_XIP_EX_OP_LOCK_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f)
- [FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc)
- [flash_andes_xip_mem_rd_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gabb24a40e5fd9462fe0cd06f426e0583f)
- [FLASH_ANDES_XIP_MEM_RD_CMD_03](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa8a3b5bbe3ec17ce470a9636934dd2bce)
- [FLASH_ANDES_XIP_MEM_RD_CMD_0B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa2dcf42c1425ed5483e3db48733f2eefc)
- [FLASH_ANDES_XIP_MEM_RD_CMD_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583facd50bfc16ae83b41ffcac3d0941a5c00)
- [FLASH_ANDES_XIP_MEM_RD_CMD_6B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa6c0d9468075b962602fa0cc652a92bc3)
- [FLASH_ANDES_XIP_MEM_RD_CMD_BB](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fad48e3482a04cb3aff0bb6afca65cf36b)
- [FLASH_ANDES_XIP_MEM_RD_CMD_EB](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa7e7321429e68649e18743a3d697cf999)
- [FLASH_ANDES_XIP_MEM_RD_CMD_13](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa2bfc829bb2e088af96ad309e0ff924c8)
- [FLASH_ANDES_XIP_MEM_RD_CMD_0C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583faf12149f961944dea851ccc7e494ba190)
- [FLASH_ANDES_XIP_MEM_RD_CMD_3C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa5464912c8f396f13e00bb4e7342185a8)
- [FLASH_ANDES_XIP_MEM_RD_CMD_6C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa7e8f108992e34d0cca57cfddde68bd6a)
- [FLASH_ANDES_XIP_MEM_RD_CMD_BC](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa65afd15579c86eb3d60aae8d4b6dee19)
- [FLASH_ANDES_XIP_MEM_RD_CMD_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa6211518baeefc2eeeb000757e500c8d3)
- [andes_xip_ex_ops_get_out](../driver_model_reference/P009_Andes原位执行读取参数.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [regs](../driver_model_reference/P009_Andes原位执行读取参数.md#a70bbb5025fbfed276ff31b5f0024f32e)
- [andes_xip_ex_ops_set_in](../driver_model_reference/P013_Andes原位执行设置参数.md)
- [regs](../driver_model_reference/P013_Andes原位执行设置参数.md#afb0c626010d671ddb496ac3dcce4e667)
- [masks](../driver_model_reference/P013_Andes原位执行设置参数.md#a2210892b339e0ab05c27eacef4d84128)
- [volatile_write](../driver_model_reference/P013_Andes原位执行设置参数.md#a75b6d154c433edb2f179c50c4b962881)
- [andes_xip_ex_ops_lock_in](../driver_model_reference/P010_Andes原位执行锁定参数.md)
- [enable](../driver_model_reference/P010_Andes原位执行锁定参数.md#a3d640ec6d0177dbf33670b02a2a36891)
- [andes_xip_ex_ops_lock_state_out](../driver_model_reference/P011_Andes原位执行锁状态.md)
- [state](../driver_model_reference/P011_Andes原位执行锁状态.md#a58c0503aa43c700ed986362c6f974afa)
- [andes_xip_ex_ops_mem_read_cmd_in](../driver_model_reference/P012_Andes原位执行存储器读命令.md)
- [cmd](../driver_model_reference/P012_Andes原位执行存储器读命令.md#aa642d9ed612a34c20332ea0396207bfa)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [andes_xip_ex_ops_get_out::regs](../driver_model_reference/P009_Andes原位执行读取参数.md#a70bbb5025fbfed276ff31b5f0024f32e)
- [andes_xip_ex_ops_lock_in::enable](../driver_model_reference/P010_Andes原位执行锁定参数.md#a3d640ec6d0177dbf33670b02a2a36891)
- [andes_xip_ex_ops_lock_state_out::state](../driver_model_reference/P011_Andes原位执行锁状态.md#a58c0503aa43c700ed986362c6f974afa)
- [andes_xip_ex_ops_mem_read_cmd_in::cmd](../driver_model_reference/P012_Andes原位执行存储器读命令.md#aa642d9ed612a34c20332ea0396207bfa)
- [andes_xip_ex_ops_set_in::masks](../driver_model_reference/P013_Andes原位执行设置参数.md#a2210892b339e0ab05c27eacef4d84128)
- [andes_xip_ex_ops_set_in::volatile_write](../driver_model_reference/P013_Andes原位执行设置参数.md#a75b6d154c433edb2f179c50c4b962881)
- [andes_xip_ex_ops_set_in::regs](../driver_model_reference/P013_Andes原位执行设置参数.md#afb0c626010d671ddb496ac3dcce4e667)

---

[上一章](P029_amebag2-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P031_andestech-atcgpio100.h_源码浏览.md)
