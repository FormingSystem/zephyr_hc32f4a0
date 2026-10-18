---
id: learning.zephyr-docs.boards-shields.page-142
title: Olimex SHIELD-MIDI
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/olimex_shield_midi/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="olimex-shield-midi"></a>

<a id="id1"></a>

# 第142章\_Olimex MIDI扩展板（SHIELD-MIDI）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/olimex_shield_midi/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此MIDI扩展板让Arduino类开发板收发MIDI消息，可直接连接最多5个压电传感器及由按键和串联电阻构成的键盘，适合电子鼓项目。

![官方原图：Olimex SHIELD-MIDI](images/olimex_shield_midi.jpg)


- MIDI输入IN、输出OUT及直通THRU连接器
- 5个压电传感器，用于鼓应用
- 键盘，用于钢琴应用
- 兼容3.3 V及5 V Arduino类开发板

更多信息见SHIELD-MIDI网站。（[SHIELD-MIDI 网站](https://www.olimex.com/Products/Duino/Shields/SHIELD-MIDI/open-source-hardware)）

<a id="peripherals"></a>

## 外设（Peripherals）

Zephyr提供以下外设：


- MIDI输入／输出：midi_serial，速率31.25 kbit/s
- LED：midi_green_led及midi_red_led

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield olimex_shield_midi，例如：

```text
# From the root of the zephyr repository
west build -b nucleo_f429zi --shield olimex_shield_midi samples/net/midi2
```

---

[上一章](P141_OD-6010_SLCD_Panel_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P143_OpenThread_RCP_over_Arduino_header.md)
