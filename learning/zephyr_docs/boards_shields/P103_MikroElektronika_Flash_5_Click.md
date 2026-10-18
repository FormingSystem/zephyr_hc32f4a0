---
id: learning.zephyr-docs.boards-shields.page-103
title: MikroElektronika Flash 5 Click
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mikroe_flash_5_click/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mikroelektronika-flash-5-click"></a>

<a id="mikroe-flash-5-click-shield"></a>

# 第103章\_MikroElektronika Flash 5 Click闪存扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mikroe_flash_5_click/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[Flash 5 Click](https://www.mikroe.com/flash-5-click)为多种嵌入式应用提供大容量存储。

它采用华邦Winbond W25N01GVZEIG/IT 1 Gbit串行SLC NAND Flash，适合空间、引脚及功耗受限系统。W25N SpiFlash结合SPI接口与大容量NAND非易失空间；原文列举用途包括将代码复制到RAM、从双线／四线SPI就地执行XIP，以及存储语音、文字和数据。

<a id="id1"></a>

[![官方原图：Flash 5 Click](images/mikroe_flash_5_click.webp)](images/mikroe_flash_5_click.webp)

Flash 5 Click闪存扩展板

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于提供mikroBUS插座，并为SPI定义mikrobus_spi节点标签的开发板，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield mikroe_flash_5_click，例如：

```text
# From the root of the zephyr repository
west build -b frdm_mcxn947/mcxn947/cpu0 --shield mikroe_flash_5_click samples/drivers/flash_shell
```

<a id="references"></a>

## 参考资料（References）


- [Flash 5 Click闪存扩展板](https://www.mikroe.com/flash-5-click)

## 译注

Flash 5采用W25N NAND；原文列举的XIP用途保留为来源说明，不据此增加Zephyr支持承诺。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [flash-5-click](https://www.mikroe.com/flash-5-click)：HTTP Error 403: Forbidden。

---

[上一章](P102_MikroElektronika_ETH_Click.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P104_MikroElektronika_Flash_6_Click.md)
