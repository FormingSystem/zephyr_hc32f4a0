---
id: learning.zephyr-docs.boards-shields.page-1
title: Abrobot ESP32 C3 OLED Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/abrobot_esp32c3_oled/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="abrobot-esp32-c3-oled-shield"></a>

<a id="abrobot-esp32c3oled-shield"></a>

# 第1章\_Abrobot ESP32 C3 OLED扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/abrobot_esp32c3_oled/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

![官方原图：Abrobot ESP32 C3 OLED Shield](images/abrobot_esp32c3_oled.webp)

Abrobot ESP32-C3 OLED只能使用兼容SH1106的显示驱动，不支持SSD1306显示驱动命令。屏幕分辨率为72×40，起始坐标为30、12。

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板只能与esp32c3_042_oled开发板一起使用。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置-b esp32c3_042_oled --shield abrobot_sh1106_72x40，例如：

```text
# From the root of the zephyr repository
west build -b esp32c3_042_oled --shield abrobot_sh1106_72x40 samples/drivers/display
```

## 译注

此OLED仅兼容SH1106命令，不能换用SSD1306驱动；72×40显示区域偏移为30、12。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_AD-APARDPFW-SL.md)
