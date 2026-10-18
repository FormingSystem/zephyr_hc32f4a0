---
id: learning.zephyr-docs.api-file-runtime-reference.page-6
title: zephyr__drivers__clock_control__clock_control_numicro.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_numicro.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nuvoton NuMicro系列的时钟控制（Clock Control）头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

Nuvoton NuMicro 系列的时钟控制头文件（Clock Control Header）。本文件提供该系列的时钟驱动接口定义（Clock Driver Interface Definitions）和结构体（Structures）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_numicro_5Fscc_5Fsubsys_5Fpcc"></a>

```c
struct numicro_scc_subsys_pcc
```

相关声明：[numicro_scc_subsys_pcc](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md)。

外设时钟控制（Peripheral Clock Control）的配置结构。

<a id="r_numicro_5Fscc_5Fsubsys"></a>

```c
struct numicro_scc_subsys
```

相关声明：[numicro_scc_subsys](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md)。

Numicro外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gafc2d65af18944d55ab57cc75b281aa99"></a>

```c
#define NUMICRO_SCC_SUBSYS_ID_PCC 1
```

相关声明：[NUMICRO_SCC_SUBSYS_ID_PCC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#gafc2d65af18944d55ab57cc75b281aa99)。

外设时钟控制（Peripheral Clock Control，PCC）使用的 SCC 子系统标识（Subsystem ID）。

<a id="r_ga07e3998b15407f2724b1902825ea84a4"></a>

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM(dev)
```

相关声明：[DT_NUMICRO_CLOCK_PCC_SUBSYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#ga07e3998b15407f2724b1902825ea84a4)。

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="r_ga67a68984d536fcb9c7f00d6c6eed6b9e"></a>

```c
#define DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST(inst)
```

相关声明：[DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#ga67a68984d536fcb9c7f00d6c6eed6b9e)。

根据设备树（Devicetree）创建 Numicro 外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。


## 6.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P102_clock_control_numicro.h_源码浏览.md)
- [numicro_scc_subsys_pcc](../device_power_control_model_reference/P054_numicro_scc_subsys_pcc_结构体.md)
- [numicro_scc_subsys](../device_power_control_model_reference/P053_numicro_scc_subsys_结构体.md)
- [NUMICRO_SCC_SUBSYS_ID_PCC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#gafc2d65af18944d55ab57cc75b281aa99)
- [DT_NUMICRO_CLOCK_PCC_SUBSYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#ga07e3998b15407f2724b1902825ea84a4)
- [DT_NUMICRO_CLOCK_PCC_SUBSYSTEM_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numicro.html#ga67a68984d536fcb9c7f00d6c6eed6b9e)

<a id="header-details"></a>

---

[上一章](P005_zephyr__drivers__sensor__bmp581_user.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__net__conn_mgr__connectivity_wifi_mgmt.h_文件参考.md)
