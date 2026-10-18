---
id: learning.zephyr-docs.boards-shields.page-82
title: M5Stack-Cardputer base shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/m5stack_cardputer/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="m5stack-cardputer-base-shield"></a>

<a id="m5stack-cardputer"></a>

# 第82章\_M5Stack-Cardputer底座扩展板（Base Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/m5stack_cardputer/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id4"></a>

[M5Stack-Cardputer](https://docs.m5stack.com/en/core/Cardputer) [注1](#id3)是适合工程应用的卡片大小便携计算机，核心为基于ESP32-S3的M5StampS3迷你开发板。

56键键盘及1.14英寸TFT屏便于输入和查看信息。板载SPM1423数字MEMS麦克风及扬声器支持录音、唤醒和音频播放等语音操作；红外发射器可控制电视、空调等设备。HY2.0-4P接口可扩展I2C温湿度、光照或压力传感器，另有microSD卡槽扩展存储。

设备由内部120 mAh及底座1400 mAh锂电池供电。

<a id="id2"></a>

[![官方原图：M5Stack-Cardputer](images/m5stack_cardputer.webp)](images/m5stack_cardputer.webp)

M5Stack-Cardputer

注意（Note）

NS4186 I2S编解码器、SPM1423麦克风、红外LED及键盘功能尚未实现。

<a id="pins-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>ESP32-S3 GPIO引脚</th>
<th colspan="2">功能（Function）</th>
</tr>
<tr>
<td>0</td>
<td colspan="2">用户按键（User Button）</td>
</tr>
<tr>
<td>1</td>
<td colspan="2">I2C串行时钟（SCL）</td>
</tr>
<tr>
<td>2</td>
<td colspan="2">I2C串行数据（SDA）</td>
</tr>
<tr>
<td>10</td>
<td colspan="2">VBAT电压</td>
</tr>
<tr>
<td>33</td>
<td colspan="2">LCD复位RST</td>
</tr>
<tr>
<td>34</td>
<td colspan="2">LCD寄存器／数据命令选择RS/DC</td>
</tr>
<tr>
<td>35</td>
<td colspan="2">LCD主出从入MOSI</td>
</tr>
<tr>
<td>36</td>
<td colspan="2">LCD串行时钟SCLK</td>
</tr>
<tr>
<td>37</td>
<td colspan="2">LCD片选CS</td>
</tr>
<tr>
<td>38</td>
<td colspan="2">LCD背光</td>
</tr>
<tr>
<td>39</td>
<td colspan="2">microSD主入从出MISO</td>
</tr>
<tr>
<td>40</td>
<td colspan="2">microSD串行时钟SCLK</td>
</tr>
<tr>
<td>12</td>
<td colspan="2">microSD片选CS</td>
</tr>
<tr>
<td>14</td>
<td colspan="2">microSD主出从入MOSI</td>
</tr>
</table>

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield m5stack_cardputer，例如：

```text
# From the root of the zephyr repository
west build -b m5stack_stamps3/esp32s3/procpu --shield m5stack_cardputer samples/drivers/display
```

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://docs.m5stack.com/en/core/Cardputer](https://docs.m5stack.com/en/core/Cardputer)

## 译注

原文列出的扬声器、麦克风、红外及键盘未实现项均保留，硬件存在不代表驱动已支持。

---

[上一章](P081_Sharp_memory_display_generic_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P083_M5Stack-Core2_base_shield.md)
