---
id: learning.zephyr-docs.boards-shields.page-66
title: EVAL-AD5529R-ARDZ
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/eval_ad5529r_ardz/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="eval-ad5529r-ardz"></a>

<a id="id1"></a>

# 第66章\_EVAL-AD5529R-ARDZ

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/eval_ad5529r_ardz/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

EVAL-AD5529R-ARDZ用于评估Analog Devices AD5529R，即16通道、16位高压输出DAC。它提供板载电源方案、可选精密基准ADR4540，并通过Arduino R3排针以SPI连接主机开发板。

![官方原图：EVAL-AD5529R-ARDZ](images/eval_ad5529r_ardz.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield eval_ad5529r_ardz，例如：

```text
# From the root of the zephyr repository
west build -b nucleo_f401re --shield eval_ad5529r_ardz samples/drivers/dac
```

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能用于提供Arduino连接器配置，并定义SPI及GPIO接口节点别名的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>Arduino引脚</th>
<th>功能（Function）</th>
</tr>
<tr>
<td><code>D7</code></td>
<td>AD5529R CLEAR，低有效</td>
</tr>
<tr>
<td>D8</td>
<td>AD5529R RESET，低有效</td>
</tr>
<tr>
<td>D9</td>
<td>AD5529R LDAC/TG0，低有效</td>
</tr>
<tr>
<td>D10</td>
<td>SPI片选，直接映射到CS0</td>
</tr>
<tr>
<td>D11</td>
<td>SPI主机输出从机输入（MOSI）</td>
</tr>
<tr>
<td>D12</td>
<td>SPI主机输入从机输出（MISO）</td>
</tr>
<tr>
<td>D13</td>
<td>SPI串行时钟（SCLK）</td>
</tr>
</table>

<a id="references"></a>

## 参考资料（References）


- [EVAL-AD5529R-ARDZ产品页](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5529r.html)
- [AD5529R产品页](https://www.analog.com/en/products/ad5529r.html)
- [AD5529R数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/ad5529r.pdf)

---

[上一章](P065_EVAL-AD4052-ARDZ.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P067_EVAL-ADXL362-ARDZ.md)
