---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-33
title: zephyr__dt-bindings__sensor__rm3100.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rm3100_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_dt-bindings\_\_sensor\_\_rm3100.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rm3100_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the PNI RM3100 magnetometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the PNI RM3100 magnetometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_gac727772f9ea2aece28b2dfead89def53"></a>

```c
#define RM3100_DT_ODR_600 0x92
```

相关声明：[RM3100_DT_ODR_600](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gac727772f9ea2aece28b2dfead89def53)。

600 赫兹（Hz）。

<a id="r_ga7695e7791cf1679c8833e6c1431023dd"></a>

```c
#define RM3100_DT_ODR_300 0x93
```

相关声明：[RM3100_DT_ODR_300](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga7695e7791cf1679c8833e6c1431023dd)。

300 赫兹（Hz）。

<a id="r_ga51ea2a9c28b6ffe296fd18832f43d8ba"></a>

```c
#define RM3100_DT_ODR_150 0x94
```

相关声明：[RM3100_DT_ODR_150](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga51ea2a9c28b6ffe296fd18832f43d8ba)。

150 赫兹（Hz）。

<a id="r_gaf33b8c4f505132b0f847e7a0e42c2da3"></a>

```c
#define RM3100_DT_ODR_75 0x95
```

相关声明：[RM3100_DT_ODR_75](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gaf33b8c4f505132b0f847e7a0e42c2da3)。

频率：75 Hz。

<a id="r_gacc174641dfa0283489a3833879905891"></a>

```c
#define RM3100_DT_ODR_37_5 0x96
```

相关声明：[RM3100_DT_ODR_37_5](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gacc174641dfa0283489a3833879905891)。

37.5 赫兹（Hz）。

<a id="r_ga943f55eae38b28ba21e8c262c4ed7d7a"></a>

```c
#define RM3100_DT_ODR_18 0x97
```

相关声明：[RM3100_DT_ODR_18](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga943f55eae38b28ba21e8c262c4ed7d7a)。

18 赫兹（Hz）。

<a id="r_ga4e03894db32a3bb415e16cee7b8d9152"></a>

```c
#define RM3100_DT_ODR_9 0x98
```

相关声明：[RM3100_DT_ODR_9](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga4e03894db32a3bb415e16cee7b8d9152)。

9 赫兹（Hz）。

<a id="r_ga18dedeef6a6fdde32968317b0dc0252d"></a>

```c
#define RM3100_DT_ODR_4_5 0x99
```

相关声明：[RM3100_DT_ODR_4_5](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga18dedeef6a6fdde32968317b0dc0252d)。

4.5 赫兹（Hz）。

<a id="r_ga1f97e962a6025e9043139af08ff11602"></a>

```c
#define RM3100_DT_ODR_2_3 0x9A
```

相关声明：[RM3100_DT_ODR_2_3](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga1f97e962a6025e9043139af08ff11602)。

2.3 赫兹（Hz）。

<a id="r_gae9a471c15befad48be14ff66e85dca4c"></a>

```c
#define RM3100_DT_ODR_1_2 0x9B
```

相关声明：[RM3100_DT_ODR_1_2](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gae9a471c15befad48be14ff66e85dca4c)。

1.2 赫兹（Hz）。

<a id="r_gadc56deaf583f71b7e88f8467388d1a36"></a>

```c
#define RM3100_DT_ODR_0_6 0x9C
```

相关声明：[RM3100_DT_ODR_0_6](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gadc56deaf583f71b7e88f8467388d1a36)。

0.6 赫兹（Hz）。

<a id="r_ga65a97784021f182cd63b7a68a39674bd"></a>

```c
#define RM3100_DT_ODR_0_3 0x9D
```

相关声明：[RM3100_DT_ODR_0_3](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga65a97784021f182cd63b7a68a39674bd)。

0.3 赫兹（Hz）。

<a id="r_ga2f6555b7fcc899c4344d2d757b891075"></a>

```c
#define RM3100_DT_ODR_0_015 0x9E
```

相关声明：[RM3100_DT_ODR_0_015](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga2f6555b7fcc899c4344d2d757b891075)。

0.015 赫兹（Hz）。

<a id="r_gab1fd570c8a4758346bc6ddcc91a19bf0"></a>

```c
#define RM3100_DT_ODR_0_0075 0x9F
```

相关声明：[RM3100_DT_ODR_0_0075](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gab1fd570c8a4758346bc6ddcc91a19bf0)。

0.0075 赫兹（Hz）。


## 33.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P720_rm3100.h_源码浏览.md)
- [RM3100_DT_ODR_600](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gac727772f9ea2aece28b2dfead89def53)
- [RM3100_DT_ODR_300](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga7695e7791cf1679c8833e6c1431023dd)
- [RM3100_DT_ODR_150](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga51ea2a9c28b6ffe296fd18832f43d8ba)
- [RM3100_DT_ODR_75](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gaf33b8c4f505132b0f847e7a0e42c2da3)
- [RM3100_DT_ODR_37_5](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gacc174641dfa0283489a3833879905891)
- [RM3100_DT_ODR_18](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga943f55eae38b28ba21e8c262c4ed7d7a)
- [RM3100_DT_ODR_9](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga4e03894db32a3bb415e16cee7b8d9152)
- [RM3100_DT_ODR_4_5](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga18dedeef6a6fdde32968317b0dc0252d)
- [RM3100_DT_ODR_2_3](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga1f97e962a6025e9043139af08ff11602)
- [RM3100_DT_ODR_1_2](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gae9a471c15befad48be14ff66e85dca4c)
- [RM3100_DT_ODR_0_6](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gadc56deaf583f71b7e88f8467388d1a36)
- [RM3100_DT_ODR_0_3](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga65a97784021f182cd63b7a68a39674bd)
- [RM3100_DT_ODR_0_015](../api_security_memory_topic_reference/P012_RM3100 API主题.md#ga2f6555b7fcc899c4344d2d757b891075)
- [RM3100_DT_ODR_0_0075](../api_security_memory_topic_reference/P012_RM3100 API主题.md#gab1fd570c8a4758346bc6ddcc91a19bf0)

<a id="header-details"></a>

---

[上一章](P032_zephyr__drivers__interrupt_controller__riscv_imsic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__mgmt__mcumgr__transport__serial.h_文件参考.md)
