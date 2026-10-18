---
id: learning.zephyr-docs.boards-shields.page-70
title: EVAL-CN0391-ARDZ
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/eval_cn0391_ardz/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="eval-cn0391-ardz"></a>

<a id="id1"></a>

# 第70章\_EVAL-CN0391-ARDZ

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/eval_cn0391_ardz/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

EVAL-CN0391-ARDZ是4通道热电偶Arduino扩展板，采用Analog Devices AD7124-8多通道24位Σ-Δ ADC。

![官方原图：EVAL-CN0391-ARDZ](images/eval_cn0391_ardz.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield eval_cn0391_ardz，例如：

```text
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_cn0391_ardz samples/drivers/adc/adc_dt
```

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供Arduino连接器配置并定义SPI节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）


- [EVAL-CN0391-ARDZ产品页](https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/CN0391.html)
- [EVAL-CN0391-ARDZ用户指南](https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/hardware/cn0391)
- [EVAL-CN0391-ARDZ原理图](https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/cn0391/02-042340-01-a-1.pdf)
- [AD7124-8产品页](https://www.analog.com/en/products/ad7124-8.html)
- [AD7124-8数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/ad7124-8.pdf)

---

[上一章](P069_EVAL-ADXL372-ARDZ.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P071_NXP_FRDM-CR20A.md)
