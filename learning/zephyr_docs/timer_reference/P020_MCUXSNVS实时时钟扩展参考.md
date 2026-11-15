---
id: learning.zephyr-docs.timer_reference.rtcext-20
title: MCUXSNVS实时时钟扩展参考
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcux__snvs__rtc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第20章\_MCUXSNVS实时时钟扩展参考

原文：[mcux__snvs__rtc_8h](https://docs.zephyrproject.org/latest/doxygen/html/mcux__snvs__rtc_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/rtc/mcux_snvs_rtc.h`基于MCUX i.MX SNVS计数器（Counter）API提供实时时钟（Real-Time Clock，RTC）控制。**Zephyr对该设备的核心接口是计数器接口。** 文件包含设备声明：

```c
#include <zephyr/device.h>
```

## 20.1\_实现细节

使用时应考虑原文列出的四点：

- 可选的安全实时时钟（Secure Real-Time Clock，SRTC）可通过配置选项启用，默认启用。
- 高功耗通道（High-Power Channel，ID为0）始终可用，低功耗通道（Low-Power Channel，ID为1）为可选。
- 低功耗闹钟（Low-Power Alarm）可用于发出唤醒（Wake-up）请求。
- 计数器以固定的1赫兹（Hertz，Hz）速率递增。原文在概述中将其写为“1Hz period”；这里按后文“advances at 1Hz”的含义说明，1 Hz是频率而非时间周期单位。

> 术语补注：SNVS为安全非易失性存储（Secure Non-Volatile Storage），名称见[NXP官方SNVS说明](https://mcuxpresso.nxp.com/api_doc/dev/4558/a00075.html)；SRTC的安全实时时钟英文全称见[NXP i.MX RT1160数据手册](https://www.nxp.com/docs/en/data-sheet/IMXRT1160AIEC.pdf)。这里只引用术语全称，不据此扩展Zephyr原页的设备能力。

## 20.2\_设置计数值

`mcux_snvs_rtc_set`设置当前计数器值：

```c
int mcux_snvs_rtc_set(const struct device *dev, uint32_t ticks);
```

`dev`是i.MX SNVS RTC设备指针，`ticks`是内部计数器的新值。由于计数器按1 Hz递增，通常将其设置为当前UNIX时间戳（UNIX Timestamp）。

原文规定成功返回**非负值（Non-negative）**，没有把成功限定为0，也没有在此列出失败错误码。完整声明见[源码页](P021_MCUXSNVS实时时钟扩展源码.md)，计数器概览见[计数器](../hardware/P017_计数器.md)。

---

[上一章：MAX31331实时时钟扩展源码](P019_MAX31331实时时钟扩展源码.md) · [下一章：MCUXSNVS实时时钟扩展源码](P021_MCUXSNVS实时时钟扩展源码.md) · [返回大纲](大纲.md)
