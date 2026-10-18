---
id: learning.zephyr-docs.hardware.stepext-1
title: DRV84XX步进扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第238章\_DRV84XX步进扩展

原文：[group__drv84xx__stepper__ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html)。读取日期：2026-10-13，`latest`。

## 238.1\_范围

本页提供德州仪器（Texas Instruments，TI）DRV84XX **步进控制器（Stepper Controller）**专用的公共 **应用程序编程接口（Application Programming Interface，API）**，头文件为 `zephyr/drivers/stepper/stepper_drv84xx.h`。

## 238.2\_微步设置失败后的恢复

函数 [`drv84xx_microstep_recovery()`](https://docs.zephyrproject.org/latest/doxygen/html/group__drv84xx__stepper__ctrl.html#gaee40af14c8f26a7df237e9be0597942e) 在微步（Micro-step）设置函数失败后，尝试恢复到之前的状态。

```c
int drv84xx_microstep_recovery(const struct device *dev);
```

参数 `dev` 指向步进电机控制器实例。返回 0 表示成功；返回小于 0 的错误码时，其具体含义取决于微步选择引脚所用的 **通用输入输出（General-Purpose Input/Output，GPIO）**控制器。

---

[上一章：步进器件扩展目录](P237_步进器件扩展目录.md) · [下一章：TMCM3216步进扩展](P239_TMCM3216步进扩展.md) · [返回大纲](大纲.md)
