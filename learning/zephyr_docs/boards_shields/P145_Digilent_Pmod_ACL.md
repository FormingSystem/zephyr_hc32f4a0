---
id: learning.zephyr-docs.boards-shields.page-145
title: Digilent Pmod ACL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/pmod_acl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="digilent-pmod-acl"></a>

<a id="pmod-acl"></a>

# 第145章\_Digilent Pmod ACL加速度计模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/pmod_acl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Digilent Pmod ACL采用Analog Devices ADXL345三轴数字加速度计。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield pmod_acl，例如：

```text
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield pmod_acl samples/sensor/sensor_shell
```

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Pmod连接器配置并定义SPI及GPIO节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）


- [Pmod ACL产品页](https://digilent.com/shop/pmod-acl-3-axis-accelerometer/)
- [Pmod ACL参考手册](https://digilent.com/reference/pmod/pmodacl/reference-manual)
- [Pmod ACL原理图](https://digilent.com/reference/_media/reference/pmod/pmodacl/pmodacl_sch.pdf)
- [ADXL345产品页](https://www.analog.com/en/products/adxl345.html)
- [ADXL345数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [pmodacl_sch.pdf](https://digilent.com/reference/_media/reference/pmod/pmodacl/pmodacl_sch.pdf)：HTTP Error 403: Forbidden。
- [reference-manual](https://digilent.com/reference/pmod/pmodacl/reference-manual)：HTTP Error 403: Forbidden。
- [](https://digilent.com/shop/pmod-acl-3-axis-accelerometer/)：HTTP Error 403: Forbidden。

---

[上一章](P144_P3T1755DP_Arduino_Shield_Evaluation_Board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P146_Digilent_Pmod_SD.md)
