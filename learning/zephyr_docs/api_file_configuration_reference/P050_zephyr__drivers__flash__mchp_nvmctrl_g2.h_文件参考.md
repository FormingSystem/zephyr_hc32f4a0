---
id: learning.zephyr-docs.api-file-configuration-reference.page-50
title: zephyr__drivers__flash__mchp_nvmctrl_g2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_drivers\_\_flash\_\_mchp\_nvmctrl\_g2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持Microchip flash-controller G2驱动ex_op扩展操作的头文件。

查看此文件的源码。

<a id="details"></a>

支持 Microchip G2 闪存控制器驱动（Flash-Controller G2 Driver）扩展操作（`ex_op`）的头文件。本头文件定义 Microchip NVMCTRL G2 闪存控制器特有的附加闪存操作。它通过提供区域锁定／解锁（Region Locking / Unlocking）、清除页缓冲区（Clear Page Buffer）等高级操作，扩展标准闪存驱动的能力。

注意（Note）：只有目标设备采用 NVMCTRL G2 闪存控制器时，才应包含本文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 50.1\_枚举（Enumerations）

<a id="r_ga4dae21b9b6e0a90faddfa045b30e19a8"></a>

```c
enum flash_mchp_ex_ops_t { FLASH_EX_OP_REGION_LOCK , FLASH_EX_OP_REGION_UNLOCK , FLASH_EX_OP_SET_PWR_REDUCTION_MODE , FLASH_EX_OP_CLR_PWR_REDUCTION_MODE , FLASH_EX_OP_CLR_PAGE_BUFFER , FLASH_EX_OP_SET_SECURITY_BIT , FLASH_EX_OP_INVALIDATE_CACHE_LINES , FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK }
```

相关声明：[flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga4dae21b9b6e0a90faddfa045b30e19a8)、[FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)、[FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)、[FLASH_EX_OP_SET_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a)、[FLASH_EX_OP_CLR_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e)、[FLASH_EX_OP_CLR_PAGE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1)、[FLASH_EX_OP_SET_SECURITY_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b)、[FLASH_EX_OP_INVALIDATE_CACHE_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb)、[FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312)。

本枚举（Enumeration）定义可对闪存执行的扩展操作（Extended Operations），例如擦除或写入用户行（User Row），以及锁定或解锁特定闪存区域（Flash Regions）。


## 50.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P499_mchp_nvmctrl_g2.h_源码浏览.md)
- [flash_mchp_ex_ops_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#ga4dae21b9b6e0a90faddfa045b30e19a8)
- [FLASH_EX_OP_REGION_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a28aeedfece9b637e6698a64ad7e036e8)
- [FLASH_EX_OP_REGION_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a412cbb9c36affa8a61e38c8ec77d22e4)
- [FLASH_EX_OP_SET_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a7f180551fd905e7ca4d217932087787a)
- [FLASH_EX_OP_CLR_PWR_REDUCTION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a5b1b658937299999761f59173a16b93e)
- [FLASH_EX_OP_CLR_PAGE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a953190cedd6519ce991793a07b990cc1)
- [FLASH_EX_OP_SET_SECURITY_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8aefa3c18a91556306795f51a14fba9f4b)
- [FLASH_EX_OP_INVALIDATE_CACHE_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8acdbe7b8985bb07f8fb0faadee3072dcb)
- [FLASH_EX_OP_SET_CHIP_ERASE_HARDLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__flash__interface.html#gga4dae21b9b6e0a90faddfa045b30e19a8a6525dc6f8c6b289b1d2f6402f57ad312)

<a id="header-details"></a>

---

[上一章](P049_zephyr__drivers__flash__mchp_nvmctrl_g1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_zephyr__sys__mem_manage.h_文件参考.md)
