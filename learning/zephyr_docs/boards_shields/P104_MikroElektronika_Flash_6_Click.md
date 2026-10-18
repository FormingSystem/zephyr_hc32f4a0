---
id: learning.zephyr-docs.boards-shields.page-104
title: MikroElektronika Flash 6 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_flash_6_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-flash-6-click"></a>

<a id="mikroe-flash-6-click-shield"></a>

# 第104章\_MikroElektronika Flash 6 Click闪存扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_flash_6_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id3"></a>

[Flash 6 Click](https://www.mikroe.com/flash-6-click) [注1](#id2)为多种嵌入式应用提供大容量存储。

<a id="id7"></a>

<a id="id5"></a>

它采用华邦Winbond [W25Q128JV](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/index.html?__locale=en&partNo=W25Q128JV) 128 Mbit串行NOR Flash [注3](#id6)，适合空间、引脚及功耗受限系统。[W25Q](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/index.html?__locale=en) SpiFlash系列[注2](#id4)结合SPI与中等容量NOR非易失空间，适用于代码复制到RAM、双线／四线SPI就地执行XIP，以及语音、文字与数据存储。4 KB小扇区使数据及参数存储更灵活。

<a id="id1"></a>

![官方原图：Flash 6 Click](images/mikroe_flash_6_click.webp)

Flash 6 Click扩展板，图片来源：MikroElektronika

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为SPI定义mikrobus_spi节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_flash_6_click，例如：

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --shield mikroe_flash_6_click samples/drivers/flash_shell
```

<a id="references"></a>

## 参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.mikroe.com/flash-6-click](https://www.mikroe.com/flash-6-click)

<a id="id4"></a>

〔[2](#id5)〕 [华邦Winbond串行NOR Flash产品系列](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/index.html?__locale=en)

<a id="id6"></a>

〔[3](#id7)〕 [华邦Winbond W25Q128JV串行NOR Flash产品页](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/index.html?__locale=en&partNo=W25Q128JV)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [flash-6-click](https://www.mikroe.com/flash-6-click)：HTTP Error 403: Forbidden。

---

[上一章](P103_MikroElektronika_Flash_5_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P105_MikroElektronika_Flash_8_Click.md)
