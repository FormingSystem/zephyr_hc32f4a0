---
id: learning.zephyr-docs.boards-shields.page-91
title: MikroElektronika ACCEL 13 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_accel13_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-accel-13-click"></a>

<a id="mikroe-accel13-click-shield"></a>

# 第91章\_MikroElektronika ACCEL 13 Click加速度计扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_accel13_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

MikroElektronika ACCEL 13 Click采用[IIS2DLPC](https://www.st.com/en/mems-and-sensors/iis2dlpc.html)超低功耗三轴加速度计，外形符合mikroBUS。（[mikroBUS™](https://www.mikroe.com/mikrobus)）

[IIS2DLPC](https://www.st.com/en/mems-and-sensors/iis2dlpc.html)支持SPI及I2C，但本扩展板当前仅支持I2C。

<a id="id1"></a>

![官方原图：MikroElektronika ACCEL 13 Click](images/accel-13-click.jpg)

MikroElektronika ACCEL 13 Click加速度计扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS连接器配置并定义其I2C节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

IIS2DLPC及ACCEL 13 Click接口详情见：


- [IIS2DLPC数据手册](https://www.st.com/resource/en/datasheet/iis2dlpc.pdf)
- [ACCEL 13 Click加速度计扩展板](https://www.mikroe.com/accel-13-click)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikro_accel13_click，例如：

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s69 --shield mikroe_accel13_click samples/sensor/sensor_shell
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [accel-13-click](https://www.mikroe.com/accel-13-click)：HTTP Error 403: Forbidden。
- [mikrobus](https://www.mikroe.com/mikrobus)：HTTP Error 403: Forbidden。
- [iis2dlpc.html](https://www.st.com/en/mems-and-sensors/iis2dlpc.html)：HTTP Error 567: Unknown Status。
- [iis2dlpc.pdf](https://www.st.com/resource/en/datasheet/iis2dlpc.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P090_MikroElektronika_3D_Hall_3_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P092_MikroElektronika_3_axis_Accel_4_Click.md)
