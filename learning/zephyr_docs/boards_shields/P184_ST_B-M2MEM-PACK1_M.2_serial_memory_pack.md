---
id: learning.zephyr-docs.boards-shields.page-184
title: ST B-M2MEM-PACK1 M.2 serial memory pack
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/st_b_m2mem_pack1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="st-b-m2mem-pack1-m-2-serial-memory-pack"></a>

<a id="st-b-m2mem-pack1-shield"></a>

# 第184章\_ST B-M2MEM-PACK1 M.2串行存储器套件

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/st_b_m2mem_pack1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

ST B-M2MEM-PACK1是一系列M.2串行存储器附加板，用于提供ST M.2 Key A串行存储器连接器的Nucleo-144开发板。

在Zephyr中，每种装有存储器的模块对应一个独立扩展板变体。所有变体都在M.2 I2C总线上提供相同的识别EEPROM，并在M.2 XSPI总线上提供一个串行NOR Flash设备。

<a id="supported-variants"></a>

## 支持的变体（Supported Variants）

<table>
<tr>
<th>扩展板（Shield）</th>
<th>模块（Module）</th>
<th>串行NOR存储器</th>
<th>总线模式</th>
<th>容量（Capacity）</th>
<th>I/O供电电压</th>
</tr>
<tr>
<td><code>b_m2mem_pack1_mb1927_33ba</code></td>
<td>MB1927-33BA</td>
<td>MX25LM51245GXDI00</td>
<td>八线单倍传输速率（Octal STR）</td>
<td>512 Mbit容量</td>
<td>3.3 V</td>
</tr>
<tr>
<td><code>b_m2mem_pack1_mb1927_18ba</code></td>
<td>MB1927-18BA</td>
<td>MX25UW25645GXDI00</td>
<td>八线单倍传输速率（Octal STR）</td>
<td>256 Mbit容量</td>
<td>1.8 V电压</td>
</tr>
<tr>
<td><code>b_m2mem_pack1_mb1928_33la</code></td>
<td>MB1928-33LA</td>
<td>IS25LP032DJNLE-TR</td>
<td>四线单倍传输速率（Quad STR）</td>
<td>32 Mbit容量</td>
<td>3.3 V</td>
</tr>
<tr>
<td><code>b_m2mem_pack1_mb1928_33lb</code></td>
<td>MB1928-33LB</td>
<td>W25Q16JVSNIQ</td>
<td>四线单倍传输速率（Quad STR）</td>
<td>16 Mbit容量</td>
<td>3.3 V</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板系列可用于任何提供ST M.2串行存储器连接器，并导出以下板端设备树标签的开发板：


- m2mem_i2c：识别EEPROM的总线
- m2mem_xspi：串行NOR接口
- m2mem_ldo_en：模块断电重启／复位控制

在开发板目录中按st,m2-memory-connector硬件特性筛选，可找到提供此连接器的主板。（[开发板目录（Board Catalog）](https://docs.zephyrproject.org/latest/boards/index.html#boards)）

<a id="programming"></a>

## 编程（Programming）

调用west build时选择所需扩展板变体，例如：

```text
west build -b nucleo_u3c5zi_q --shield b_m2mem_pack1_mb1928_33lb samples/basic/blinky
```

构建其他模块时，将扩展板名称替换为以下之一：


- `b_m2mem_pack1_mb1927_33ba`
- `b_m2mem_pack1_mb1927_18ba`
- `b_m2mem_pack1_mb1928_33la`
- `b_m2mem_pack1_mb1928_33lb`

无论选择哪种变体，扩展板都通过固定的m2mem_flash设备树标签公开串行NOR设备，应用或示例可用一致方式访问，例如通过flash0别名。可用Flash Shell示例查看设备。共有的识别EEPROM也在设备树中描述，应用可通过[EEPROM驱动API](https://docs.zephyrproject.org/latest/hardware/peripherals/eeprom/api.html#eeprom-api)访问。（[Flash命令行Shell](../storage/P091_闪存命令行示例.md#flash-shell)）

<a id="references"></a>

## 参考资料（References）

ST提供的套件及连接器资料包括：


- B-M2MEM-PACK1产品简介（Data Brief）
- <a id="id2"></a>

  [UM3611](https://www.st.com/resource/en/user_manual/um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf)[注1](#id1)：Nucleo-144开发板M.2串行存储器套件
- <a id="id4"></a>

  [TN1618](https://www.st.com/resource/en/technical_note/tn1618-m2serialmemory-interface-specification-stmicroelectronics.pdf)[注2](#id3)：M.2串行存储器接口规范

<a id="id1"></a>

〔[1](#id2)〕 [https://www.st.com/resource/en/user_manual/um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf)

<a id="id3"></a>

〔[2](#id4)〕 [https://www.st.com/resource/en/technical_note/tn1618-m2serialmemory-interface-specification-stmicroelectronics.pdf](https://www.st.com/resource/en/technical_note/tn1618-m2serialmemory-interface-specification-stmicroelectronics.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [tn1618-m2serialmemory-interface-specification-stmicroelectronics.pdf](https://www.st.com/resource/en/technical_note/tn1618-m2serialmemory-interface-specification-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。
- [um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P183_ST_B-LCD40-DSI1.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P185_ST_LCD_DSI_MB1835.md)
