---
id: learning.zephyr-docs.api-file-supplement-reference.page-38
title: zephyr__drivers__gpio__gpio_nct38xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_drivers\_\_gpio\_\_gpio\_nct38xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__nct38xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NCT38XX GPIO驱动的头文件。

查看此文件的源码。

<a id="details"></a>

NCT38XX GPIO驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 38.1\_函数（Functions）

<a id="r_ga05e658cb957b13402371054aa9f59302"></a>

```c
void nct38xx_gpio_alert_handler (const struct device *dev)
```

相关声明：[nct38xx_gpio_alert_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html#ga05e658cb957b13402371054aa9f59302)、[device](../device_reference/P002_设备对象结构.md)。

分派 NCT38XX 设备中所有 GPIO 端口的中断服务程序（Interrupt Service Routines，ISRs）。


## 38.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P299_gpio_nct38xx.h_源码浏览.md)
- [nct38xx_gpio_alert_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__nct38xx__interface.html#ga05e658cb957b13402371054aa9f59302)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P037_zephyr__drivers__gpio__gpio_mcux_lpc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__drivers__gpio__gpio_pca_series.h_文件参考.md)
