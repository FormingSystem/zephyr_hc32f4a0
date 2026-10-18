---
id: learning.zephyr-docs.boards-shields.page-29
title: Adafruit LTR-329 Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/adafruit_ltr329/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="adafruit-ltr-329-shield"></a>

<a id="adafruit-ltr329"></a>

# 第29章\_Adafruit LTR-329扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/adafruit_ltr329/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Adafruit LTR-329光照传感器扩展板采用光宝LiteOn LTR-329ALS-01数字光传感器，带2个STEMMA QT连接器。（[Adafruit LTR-329 光照传感器 扩展板](https://learn.adafruit.com/adafruit-ltr-329-ltr-303)；[LiteOn LTR-329ALS-01 数字光传感器](https://optoelectronics.liteon.com/upload/download/DS86-2014-0006/LTR-329ALS-01_DS_V1.8.PDF)）

<a id="id1"></a>

![官方原图：Adafruit LTR-329 Shield](images/adafruit_ltr329.webp)

Adafruit LTR-329扩展板（Shield），图片来源：Adafruit

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板可用于提供I2C连接器的开发板，例如STEMMA QT或Qwiic；目标板必须定义zephyr_i2c节点标签，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>扩展板引脚（Shield Pin）</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>串行数据线（SDA）</td>
<td>LTR-329 I2C数据线（SDA）</td>
</tr>
<tr>
<td>串行时钟线（SCL）</td>
<td>LTR-329 I2C时钟线（SCL）</td>
</tr>
</table>

如何修改设备树，例如调整积分时间，见[liteon,ltr329](../sensor_liteon_maxim_temperature_binding_reference/P005_liteon_ltr329.md#std-dtcompatible-liteon-ltr329)绑定文档。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield adafruit_ltr329，例如运行通用光照传感器轮询测量示例：（[通用光照传感器轮询（Generic Light Sensor Polling）](../sensors/P019_光照传感器轮询示例.md#light_sensor_polling)）

```text
# From the root of the zephyr repository
west build -b adafruit_metro_rp2040 --shield adafruit_ltr329 samples/sensor/light_polling
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [LTR-329ALS-01_DS_V1.8.PDF](https://optoelectronics.liteon.com/upload/download/DS86-2014-0006/LTR-329ALS-01_DS_V1.8.PDF)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P028_Adafruit_LPS22_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P030_Adafruit_MAX17048_Shield.md)
