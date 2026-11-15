---
id: learning.zephyr-docs.timer_reference.systemtimer-78
title: InfineonTCPWM定时器头文件参考
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__tcpwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第78章\_InfineonTCPWM定时器头文件参考

原文：[ifx__tcpwm_8h](https://docs.zephyrproject.org/latest/doxygen/html/ifx__tcpwm_8h.html)。读取日期：2026-10-13，`latest`。

本页对应`zephyr/drivers/timer/ifx_tcpwm.h`文件参考。原页列出两个包含项，并提供源码入口：

```c
#include <stdint.h>
#include "cy_tcpwm.h"
```

## 78.1\_源码入口

[完整头文件源码](P079_InfineonTCPWM定时器头文件源码.md)保存Infineon TCPWM适配宏和原注释。原文件参考页没有列出独立的宏或函数说明。

TCPWM指计时器、计数器与PWM（Timer Counter PWM）模块；PWM为脉宽调制（Pulse Width Modulation）。外设驱动库（Peripheral Driver Library，PDL）是源码注释提到的底层库。

> 术语补注：TCPWM名称与PDL名称参照[Infineon官方PDL文档](https://infineon.github.io/mtb-pdl-cat2/pdl_api_reference_manual/html/group__group__tcpwm.html)。本页只补充术语，不把该厂商页面针对其他器件的规格移入Zephyr译文。

---

[上一章：Arm架构定时器头文件源码](P077_Arm架构定时器头文件源码.md) · [下一章：InfineonTCPWM定时器头文件源码](P079_InfineonTCPWM定时器头文件源码.md) · [返回大纲](大纲.md)
