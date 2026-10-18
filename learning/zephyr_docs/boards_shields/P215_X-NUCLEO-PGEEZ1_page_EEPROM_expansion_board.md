---
id: learning.zephyr-docs.boards-shields.page-215
title: X-NUCLEO-PGEEZ1 page EEPROM expansion board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_pgeez1/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-pgeez1-page-eeprom-expansion-board"></a>

<a id="x-nucleo-pgeez1-shield"></a>

# 第215章\_X-NUCLEO-PGEEZ1页式EEPROM扩展板（Page EEPROM）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_pgeez1/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-PGEEZ1扩展板采用ST M95P32 32 Mbit SPI页式EEPROM，支持单线、双线及四线输出读取，以及由串行Flash可发现参数SFDP描述的NOR兼容阵列操作。

![官方原图：X-NUCLEO-PGEEZ1](images/x_nucleo_pgeez1.webp)

Zephyr通过MSPI上的Flash API公开M95P32主存储阵列。扩展板配置使用1-1-4四线读取及单线页编程，因为M95P32不提供四线页编程命令。M95P32兼容通用jedec,nor MSPI驱动。

扩展板详情见X-NUCLEO-PGEEZ1产品页。（[X-NUCLEO-PGEEZ1 产品页](https://www.st.com/en/evaluation-tools/x-nucleo-pgeez1.html)）

<a id="requirements"></a>

## 前置要求（Requirements）

在STM32开发板全面迁移到MSPI API之前，此扩展板要求主板提供st_zio_qspi连接器。目前支持[Nucleo U575ZI Q](../boards_st_nucleo/P070_Nucleo_U575ZI_Q.md#nucleo_u575zi_q)。

<a id="programming"></a>

## 编程（Programming）

启用扩展板并构建MSPI Flash示例：

```text
# From the root of the zephyr repository
west build -b nucleo_u575zi_q --shield x_nucleo_pgeez1 samples/drivers/mspi/mspi_flash
```

在[Nucleo U575ZI Q](../boards_st_nucleo/P070_Nucleo_U575ZI_Q.md#nucleo_u575zi_q)上，扩展板将原本位于内部Flash的MCUboot次槽替换为M95P32上的分区，并选择MCUmgr使用的UART。板级扩展配置采用8 KiB页布局，使外部存储布局匹配STM32U575内部Flash布局。采用偏移交换（Swap Using Offset）还要求sysbuild配置SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET=y。

例如，按以下方式构建带MCUboot的MCUmgr SMP服务器：

```text
west build --sysbuild -b nucleo_u575zi_q \
  samples/subsys/mgmt/mcumgr/smp_svr --shield x_nucleo_pgeez1 -- \
  -DEXTRA_CONF_FILE=serial.conf \
  -DSB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET=y
```

## 译注

M95P32通过MSPI上的Flash API访问；支持四线读取而不提供四线页编程。MCUboot偏移交换另需sysbuild配置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-pgeez1.html](https://www.st.com/en/evaluation-tools/x-nucleo-pgeez1.html)：HTTP Error 567: Unknown Status。

---

[上一章](P214_X-NUCLEO-IKS5A1_MEMS_Inertial_and_Environmental_Multi_sensor_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P216_X-NUCLEO-WB05KN1_BLE_expansion_board.md)
