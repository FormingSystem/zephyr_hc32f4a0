---
id: learning.zephyr-docs.boards-shields.page-65
title: EVAL-AD4052-ARDZ
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/eval_ad4052_ardz/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="eval-ad4052-ardz"></a>

<a id="id1"></a>

# 第65章\_EVAL-AD4052-ARDZ

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/eval_ad4052_ardz/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

EVAL-AD4052-ARDZ是采用Analog Devices AD4052的16位逐次逼近寄存器型ADC（SAR ADC）Arduino扩展板。

![官方原图：EVAL-AD4052-ARDZ](images/eval_ad4052_ardz.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield eval_ad4052_ardz，例如：

```text
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield eval_ad4052_ardz samples/drivers/adc/
```

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="references"></a>

## 参考资料（References）


- [EVAL-AD4052-ARDZ产品页](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad4052-ardz.html#eb-overview)
- [EVAL-AD4052-ARDZ用户指南](https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad4050-ad4052-ug-2222.pdf)
- [EVAL-AD4052-ARDZ原理图](https://www.analog.com/media/en/evaluation-documentation/evaluation-design-files/eval-ad4052-ardz-designsupport-files.zip)
- [AD4052产品页](https://www.analog.com/en/products/ad4052.html)
- [AD4052数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/ad4052-ad4058.pdf)

---

[上一章](P064_ESP-8266_Modules.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P066_EVAL-AD5529R-ARDZ.md)
