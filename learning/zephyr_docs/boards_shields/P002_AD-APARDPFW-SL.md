---
id: learning.zephyr-docs.boards-shields.page-2
title: AD-APARDPFW-SL
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/ad_apardpfw_sl/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="ad-apardpfw-sl"></a>

<a id="id1"></a>

# 第2章\_AD-APARDPFW-SL

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/ad_apardpfw_sl/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

AD-APARDPFW-SL是支持单对线以太网供电（Single Pair Power over Ethernet，SPoE）的双端口10BASE-T1L电源转发器，采用Analog Devices ADIN2111以太网交换机，用于在AD-APARD32690-SL平台板上开发现场设备及应用。

![官方原图：AD-APARDPFW-SL](images/ad_apardpfw_sl.webp)

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield ad_apardpfw_sl，例如：

```text
# From the root of the zephyr repository
west build -b apard32690/max32690/m4 --shield ad_apardpfw_sl samples/net/sockets/echo_server
```

<a id="requirements"></a>

## 前置要求（Requirements）

该扩展板专为AD-APARD32690-SL平台板设计。

<a id="references"></a>

## 参考资料（References）


- [AD-APARDPFW-SL产品页](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-apardpfw-sl.html)
- [AD-APARDPFW-SL用户指南](https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-apard32690-sl/ad-apardpfwd-sl/index.html)
- [ADIN2111产品页](https://www.analog.com/en/products/adin2111.html)
- [ADIN2111数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/adin2111.pdf)

---

[上一章](P001_Abrobot_ESP32_C3_OLED_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Adafruit_24LC32_EEPROM_Shield.md)
