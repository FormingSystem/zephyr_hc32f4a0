---
id: learning.zephyr-docs.boards-shields.page-146
title: Digilent Pmod SD
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/pmod_sd/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="digilent-pmod-sd"></a>

<a id="pmod-sd"></a>

# 第146章\_Digilent Pmod SD存储模块

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/pmod_sd/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

Digilent Pmod SD B版使系统开发板可读写SD卡。

<a id="features"></a>

## 功能（Features）


- 全尺寸SD卡槽
- 通过系统开发板存储及访问大量数据；原文date按上下文译作数据
- 不限制所用SD卡文件系统或容量
- 1位及4位通信
- 12针Pmod端口，带SPI接口

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield pmod_sd，例如：

```text
# From the root of the zephyr repository
west build -b ek_ra8m1 --shield pmod_sd tests/drivers/disk/disk_access
```

<a id="pinout"></a>

### 引脚分配（Pinout）

<a id="id1"></a>

![官方原图：PMOD SD Pinout](images/pmod_sd_pins.webp)

Pmod SD引脚图，图片来源：Digilent

<a id="references"></a>

## 参考资料（References）


- [Pmod SD产品页](https://digilent.com/shop/pmod-sd-full-sized-sd-card-slot/)
- [Pmod SD参考手册](https://digilent.com/reference/pmod/pmodsd/reference-manual)
- [Pmod SD原理图](https://digilent.com/reference/_media/reference/pmod/pmodsd/pmodsd_sch.pdf)

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [pmodsd_sch.pdf](https://digilent.com/reference/_media/reference/pmod/pmodsd/pmodsd_sch.pdf)：HTTP Error 403: Forbidden。
- [reference-manual](https://digilent.com/reference/pmod/pmodsd/reference-manual)：HTTP Error 403: Forbidden。
- [](https://digilent.com/shop/pmod-sd-full-sized-sd-card-slot/)：HTTP Error 403: Forbidden。

---

[上一章](P145_Digilent_Pmod_ACL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P147_RAK19007_WisBlock_Base_Board_2nd_Gen.md)
