---
id: learning.zephyr-docs.api-file-service-reference.page-57
title: zephyr__drivers__clock_control__tisci_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_zephyr\_\_drivers\_\_clock\_control\_\_tisci\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tisci__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI TISCI系统控制器（System Controller）接口的时钟控制定义。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

TI TISCI系统控制器（System Controller）接口的时钟控制定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 57.1\_数据结构（Data Structures）

<a id="r_tisci_5Fclock_5Fconfig"></a>

```c
struct tisci_clock_config
```

相关声明：[tisci_clock_config](../platform_security_model_reference/P064_tisci_clock_config_结构体.md)。

时钟配置结构（Clock Configuration Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 57.2\_宏定义（Macros）

<a id="r_ga4048d6a28a71a725f5e34362189e2cf4"></a>

```c
#define TISCI_GET_CLOCK(node_id)
```

相关声明：[TISCI_GET_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga4048d6a28a71a725f5e34362189e2cf4)。

获取节点 `clocks` 引用句柄（Phandle）所引用的时钟控制器设备（Clock Controller Device）。

<a id="r_ga3176cb1d06b703090ede7e2e3264e743"></a>

```c
#define TISCI_GET_CLOCK_DETAILS(node_id)
```

相关声明：[TISCI_GET_CLOCK_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga3176cb1d06b703090ede7e2e3264e743)。

根据节点的时钟说明符（Clock Specifier）初始化 `tisci_clock_config`。

<a id="r_ga845867bfd9264f27ac7bf99fcb8456d2"></a>

```c
#define TISCI_GET_CLOCK_BY_INST(inst)
```

相关声明：[TISCI_GET_CLOCK_BY_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga845867bfd9264f27ac7bf99fcb8456d2)。

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK()` 等效的操作。

<a id="r_gac45d403310257b6aa58566b764a7022b"></a>

```c
#define TISCI_GET_CLOCK_DETAILS_BY_INST(inst)
```

相关声明：[TISCI_GET_CLOCK_DETAILS_BY_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#gac45d403310257b6aa58566b764a7022b)。

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK_DETAILS()` 等效的操作。


## 57.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P867_tisci_clock_control.h_源码浏览.md)
- [tisci_clock_config](../platform_security_model_reference/P064_tisci_clock_config_结构体.md)
- [TISCI_GET_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga4048d6a28a71a725f5e34362189e2cf4)
- [TISCI_GET_CLOCK_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga3176cb1d06b703090ede7e2e3264e743)
- [TISCI_GET_CLOCK_BY_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#ga845867bfd9264f27ac7bf99fcb8456d2)
- [TISCI_GET_CLOCK_DETAILS_BY_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html#gac45d403310257b6aa58566b764a7022b)

<a id="header-details"></a>

---

[上一章](P056_zephyr__xen__dom0__sysctl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P058_zephyr__modem__ubx.h_文件参考.md)
