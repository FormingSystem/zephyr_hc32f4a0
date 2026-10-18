---
id: learning.zephyr-docs.api-file-service-reference.page-3
title: zephyr__drivers__clock_control__clock_control_silabs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_clock\_control\_\_clock\_control\_silabs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__silabs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Silicon Labs设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
```

查看此文件的源码。

Silicon Labs设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_silabs_5Fclock_5Fcontrol_5Fcmu_5Fconfig"></a>

```c
struct silabs_clock_control_cmu_config
```

相关声明：[silabs_clock_control_cmu_config](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md)。

外设的时钟管理单元（Clock Management Unit，CMU）时钟配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga2238842842469b06a3cb0d0cf187583c"></a>

```c
#define SILABS_DT_CLOCK_CFG(node_id)
```

相关声明：[SILABS_DT_CLOCK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga2238842842469b06a3cb0d0cf187583c)。

根据设备树节点（DT Node）初始化 `silabs_clock_control_cmu_config`。

<a id="r_ga109d85a9e8fe8ec3730927a91d885721"></a>

```c
#define SILABS_DT_INST_CLOCK_CFG(inst)
```

相关声明：[SILABS_DT_INST_CLOCK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga109d85a9e8fe8ec3730927a91d885721)。

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG()` 等效的操作。

<a id="r_ga6aee6d89bb6d61cc82f43bf9d2c0f35b"></a>

```c
#define SILABS_DT_CLOCK_CFG_BY_NAME(node_id, name)
```

相关声明：[SILABS_DT_CLOCK_CFG_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga6aee6d89bb6d61cc82f43bf9d2c0f35b)。

根据设备树节点（DT Node），按名称（By Name）初始化 `silabs_clock_control_cmu_config`。

<a id="r_ga558497745851c6074caebc726c243333"></a>

```c
#define SILABS_DT_INST_CLOCK_CFG_BY_NAME(inst, name)
```

相关声明：[SILABS_DT_INST_CLOCK_CFG_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga558497745851c6074caebc726c243333)。

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG_BY_NAME()` 等效的操作。


## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_reference/P104_clock_control_silabs.h_源码浏览.md)
- [silabs_clock_control_cmu_config](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md)
- [SILABS_DT_CLOCK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga2238842842469b06a3cb0d0cf187583c)
- [SILABS_DT_INST_CLOCK_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga109d85a9e8fe8ec3730927a91d885721)
- [SILABS_DT_CLOCK_CFG_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga6aee6d89bb6d61cc82f43bf9d2c0f35b)
- [SILABS_DT_INST_CLOCK_CFG_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html#ga558497745851c6074caebc726c243333)

<a id="header-details"></a>

---

[上一章](P002_zephyr__llext__buf_loader.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__coap_mgmt.h_文件参考.md)
