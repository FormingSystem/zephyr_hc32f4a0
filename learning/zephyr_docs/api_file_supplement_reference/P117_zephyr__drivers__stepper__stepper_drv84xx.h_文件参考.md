---
id: learning.zephyr-docs.api-file-supplement-reference.page-117
title: zephyr__drivers__stepper__stepper_drv84xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stepper__drv84xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_zephyr\_\_drivers\_\_stepper\_\_stepper\_drv84xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stepper__drv84xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DRV84XX步进电机控制器专用功能（Stepper Controller Specific Functions）的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/drivers/stepper/stepper.h>
```

查看此文件的源码。

DRV84XX步进电机控制器专用功能（Stepper Controller Specific Functions）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 117.1\_函数（Functions）

<a id="r_gaee40af14c8f26a7df237e9be0597942e"></a>

```c
int drv84xx_microstep_recovery (const struct device *dev)
```

相关声明：[drv84xx_microstep_recovery](https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html#gaee40af14c8f26a7df237e9be0597942e)、[device](../device_reference/P002_设备对象结构.md)。

微步设置器（Microstep Setter）失败后，尝试恢复到先前状态（Previous State）。


## 117.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/drivers/stepper/stepper.h](../api_source_reference/P820_stepper.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P822_stepper_drv84xx.h_源码浏览.md)
- [drv84xx_microstep_recovery](https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html#gaee40af14c8f26a7df237e9be0597942e)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P116_zephyr__bluetooth__mesh__sol_pdu_rpl_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P118_zephyr__dt-bindings__reset__stm32-common.h_文件参考.md)
