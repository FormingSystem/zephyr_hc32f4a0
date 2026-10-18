---
id: learning.zephyr-docs.boards-shields.page-123
title: MikroElektronika Weather Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_weather_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-weather-click"></a>

<a id="mikroe-weather-click"></a>

# 第123章\_MikroElektronika Weather Click气象扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_weather_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

MikroElektronika [Weather Click](https://www.mikroe.com/weather-click)采用[BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)集成环境传感器，外形符合mikroBUS，可测量相对湿度、气压及环境温度。（[mikroBUS™](https://www.mikroe.com/mikrobus)）

<a id="id1"></a>

![官方原图：MikroElektronika Weather Click](images/weather-click.webp)

MikroElektronika Weather Click气象扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

开发板须提供mikroBUS插座，并为I2C定义mikrobus_i2c，或为SPI定义mikrobus_spi节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

注意（Note）

Weather Click默认配置为I2C，使用SPI前须更改跳线，详情见原理图。（[Weather Click原理图](https://download.mikroe.com/documents/add-on-boards/click/weather/weather-click-schematic-v101.pdf)）

更多BME280及Weather Click信息见：


- [Weather Click气象扩展板](https://www.mikroe.com/weather-click)
- [Weather Click原理图](https://download.mikroe.com/documents/add-on-boards/click/weather/weather-click-schematic-v101.pdf)
- [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
- [BME280数据手册](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf)

<a id="programming"></a>

## 编程（Programming）

调用west build时选择--shield mikroe_weather_click_i2c或--shield mikroe_weather_click_spi，例如：

```text
# From the root of the zephyr repository
west build -b lpcxpresso55s16 --shield [mikroe_weather_click_i2c | mikroe_weather_click_spi] samples/sensor/bme280
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mikrobus](https://www.mikroe.com/mikrobus)：HTTP Error 403: Forbidden。
- [weather-click](https://www.mikroe.com/weather-click)：HTTP Error 403: Forbidden。

---

[上一章](P122_MikroElektronika_Two_Wire_ETH_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P124_MikroElektronika_WIFI_and_BLE_Shield.md)
