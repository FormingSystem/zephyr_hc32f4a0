---
id: learning.zephyr-docs.boards-shields.page-120
title: MikroElektronika Stepper 19 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_stepper_19_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-stepper-19-click"></a>

<a id="mikroe-stepper-19-click-shield"></a>

# 第120章\_MikroElektronika Stepper 19 Click步进驱动扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_stepper_19_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

<a id="id5"></a>

<a id="id7"></a>

[Stepper 19 Click](https://www.mikroe.com/stepper-19-click) [注1](#id2)包含通过GPIO访问的[TI DRV8424](https://www.ti.com/product/DRV8424)步进驱动器[注2](#id4)及通过I2C访问的[NXP PCA9538A](https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A) GPIO扩展器[注3](#id6)；DRV8424部分引脚经GPIO扩展器访问。

<a id="id1"></a>

![官方原图：MikroElektronika Stepper 19 Click](images/stepper_19_click.webp)

MikroElektronika Stepper 19 Click步进驱动扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

扩展板使用mikroBUS，目标板须定义mikrobus_i2c及mikrobus_header节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

```text
# From the root of the zephyr repository
west build -b <board> --shield mikroe_stepper_19_click samples/drivers/stepper/generic/
west flash
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/stepper-19-click](https://www.mikroe.com/stepper-19-click)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.ti.com/product/DRV8424](https://www.ti.com/product/DRV8424)

<a id="id6"></a>

〔[3](#id7)〕 [https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A](https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [stepper-19-click](https://www.mikroe.com/stepper-19-click)：HTTP Error 403: Forbidden。
- [low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A](https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/general-purpose-i-o-gpio/low-voltage-8-bit-ic-bus-i-o-port-with-interrupt-and-reset:PCA9538A)：HTTP Error 404: Not Found。

---

[上一章](P119_MikroElektronika_Stepper_18_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P121_MikroElektronika_Temp_Hum_Click.md)
