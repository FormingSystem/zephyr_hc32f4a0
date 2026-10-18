---
id: learning.zephyr-docs.api-file-configuration-reference.page-5
title: zephyr__drivers__flash__andes_flash_xip_api_ex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_flash\_\_andes\_flash\_xip\_api\_ex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Andes QSPI-NOR就地执行（XIP）闪存扩展操作的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/flash.h>
```

查看此文件的源码。

Andes QSPI-NOR就地执行（XIP）闪存扩展操作的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_andes_5Fxip_5Fex_5Fops_5Fget_5Fout"></a>

```c
struct andes_xip_ex_ops_get_out
```

相关声明：[andes_xip_ex_ops_get_out](../driver_model_reference/P009_Andes原位执行读取参数.md)。

`FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS` 操作的输出参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Fset_5Fin"></a>

```c
struct andes_xip_ex_ops_set_in
```

相关声明：[andes_xip_ex_ops_set_in](../driver_model_reference/P013_Andes原位执行设置参数.md)。

`FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS` 操作的输入参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Flock_5Fin"></a>

```c
struct andes_xip_ex_ops_lock_in
```

相关声明：[andes_xip_ex_ops_lock_in](../driver_model_reference/P010_Andes原位执行锁定参数.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK` 操作的输入参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Flock_5Fstate_5Fout"></a>

```c
struct andes_xip_ex_ops_lock_state_out
```

相关声明：[andes_xip_ex_ops_lock_state_out](../driver_model_reference/P011_Andes原位执行锁状态.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK_STATE` 操作的输出参数。

<a id="r_andes_5Fxip_5Fex_5Fops_5Fmem_5Fread_5Fcmd_5Fin"></a>

```c
struct andes_xip_ex_ops_mem_read_cmd_in
```

相关声明：[andes_xip_ex_ops_mem_read_cmd_in](../driver_model_reference/P012_Andes原位执行存储器读命令.md)。

`FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD` 操作的输入参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_ga4b46df3b8254c20bf81be3957f9a0d1e"></a>

```c
enum flash_andes_xip_ex_ops { FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS = FLASH_EX_OP_VENDOR_BASE , FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS , FLASH_ANDES_XIP_EX_OP_LOCK , FLASH_ANDES_XIP_EX_OP_LOCK_STATE , FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD }
```

相关声明：[flash_andes_xip_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ga4b46df3b8254c20bf81be3957f9a0d1e)、[FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7)、[FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f)、[FLASH_ANDES_XIP_EX_OP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0)、[FLASH_ANDES_XIP_EX_OP_LOCK_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f)、[FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc)。

Andes 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

<a id="r_gabb24a40e5fd9462fe0cd06f426e0583f"></a>

```c
enum flash_andes_xip_mem_rd_cmd { FLASH_ANDES_XIP_MEM_RD_CMD_03 = 0 , FLASH_ANDES_XIP_MEM_RD_CMD_0B = 1 , FLASH_ANDES_XIP_MEM_RD_CMD_3B = 2 , FLASH_ANDES_XIP_MEM_RD_CMD_6B = 3 , FLASH_ANDES_XIP_MEM_RD_CMD_BB = 4 , FLASH_ANDES_XIP_MEM_RD_CMD_EB = 5 , FLASH_ANDES_XIP_MEM_RD_CMD_13 = 8 , FLASH_ANDES_XIP_MEM_RD_CMD_0C = 9 , FLASH_ANDES_XIP_MEM_RD_CMD_3C = 10 , FLASH_ANDES_XIP_MEM_RD_CMD_6C = 11 , FLASH_ANDES_XIP_MEM_RD_CMD_BC = 12 , FLASH_ANDES_XIP_MEM_RD_CMD_EC = 13 }
```

相关声明：[flash_andes_xip_mem_rd_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gabb24a40e5fd9462fe0cd06f426e0583f)、[FLASH_ANDES_XIP_MEM_RD_CMD_03](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa8a3b5bbe3ec17ce470a9636934dd2bce)、[FLASH_ANDES_XIP_MEM_RD_CMD_0B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa2dcf42c1425ed5483e3db48733f2eefc)、[FLASH_ANDES_XIP_MEM_RD_CMD_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583facd50bfc16ae83b41ffcac3d0941a5c00)、[FLASH_ANDES_XIP_MEM_RD_CMD_6B](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa6c0d9468075b962602fa0cc652a92bc3)、[FLASH_ANDES_XIP_MEM_RD_CMD_BB](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fad48e3482a04cb3aff0bb6afca65cf36b)、[FLASH_ANDES_XIP_MEM_RD_CMD_EB](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa7e7321429e68649e18743a3d697cf999)、[FLASH_ANDES_XIP_MEM_RD_CMD_13](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa2bfc829bb2e088af96ad309e0ff924c8)、[FLASH_ANDES_XIP_MEM_RD_CMD_0C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583faf12149f961944dea851ccc7e494ba190)、[FLASH_ANDES_XIP_MEM_RD_CMD_3C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa5464912c8f396f13e00bb4e7342185a8)、[FLASH_ANDES_XIP_MEM_RD_CMD_6C](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa7e8f108992e34d0cca57cfddde68bd6a)、[FLASH_ANDES_XIP_MEM_RD_CMD_BC](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa65afd15579c86eb3d60aae8d4b6dee19)、[FLASH_ANDES_XIP_MEM_RD_CMD_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ggabb24a40e5fd9462fe0cd06f426e0583fa6211518baeefc2eeeb000757e500c8d3)。

用于内存映射读取模式（Memory-Mapped Read Mode）的 SPI 命令（Commands）。


## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](../flash_reference/P010_Flash公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P030_andes_flash_xip_api_ex.h_源码浏览.md)
- [andes_xip_ex_ops_get_out](../driver_model_reference/P009_Andes原位执行读取参数.md)
- [FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7)
- [andes_xip_ex_ops_set_in](../driver_model_reference/P013_Andes原位执行设置参数.md)
- [FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f)
- [andes_xip_ex_ops_lock_in](../driver_model_reference/P010_Andes原位执行锁定参数.md)
- [FLASH_ANDES_XIP_EX_OP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0)
- [andes_xip_ex_ops_lock_state_out](../driver_model_reference/P011_Andes原位执行锁状态.md)
- [FLASH_ANDES_XIP_EX_OP_LOCK_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f)
- [andes_xip_ex_ops_mem_read_cmd_in](../driver_model_reference/P012_Andes原位执行存储器读命令.md)
- [FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc)
- [flash_andes_xip_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#ga4b46df3b8254c20bf81be3957f9a0d1e)
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

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__pinctrl__aesc-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__gpio__andestech-atcgpio100.h_文件参考.md)
