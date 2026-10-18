---
id: learning.zephyr-docs.boards-shields.page-68
title: EVAL-ADXL367-ARDZ
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/eval_adxl367_ardz/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="eval-adxl367-ardz"></a>

<a id="id1"></a>

# 第68章\_EVAL-ADXL367-ARDZ

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/eval_adxl367_ardz/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

EVAL-ADXL367-ARDZ是采用Analog Devices ADXL367的三轴数字加速度计Arduino扩展板。

![官方原图：EVAL-ADXL367-ARDZ](images/eval_adxl367_ardz.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield eval_adxl367_ardz，例如：

```text
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_adxl367_ardz samples/sensor/sensor_shell
```

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）


- [ADXL367产品页](https://www.analog.com/en/products/adxl367.html)
- [ADXL367数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/adxl367.pdf)

---

[上一章](P067_EVAL-ADXL362-ARDZ.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P069_EVAL-ADXL372-ARDZ.md)
