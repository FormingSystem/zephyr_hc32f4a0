---
id: learning.zephyr-docs.boards-intel-ite.page-4
title: Intel ADSP ACE 1.5
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_ace15_mtpm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel-adsp-ace-1-5"></a>

<a id="intel-adsp-ace15"></a>

# 第4章\_Intel ADSP ACE 1.5

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_ace15_mtpm.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此开发板配置用于在Intel ACE 1.5音频DSP上运行Zephyr，Intel Meteor Lake等微处理器采用该配置。关于Intel ADSP ACE和CAVS，详见[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)。

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="xtensa-toolchain"></a>

### Xtensa工具链（Toolchain）

若选择Xtensa工具链而不使用Zephyr SDK，除了[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)中列出的Xtensa工具链环境变量，还需设置以下开发板专用环境变量。

```text
export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
export TOOLCHAIN_VER=RI-2021.7-linux
export XTENSA_CORE=ace10_LX7HiFi4
```

较旧工具链版本应将工具链变体（Toolchain Variant）设为`xcc`。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

适用于所有CAVS及ACE平台的通用编程和调试说明见[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)。

---

[上一章](P003_Intel_ADSP.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_Intel_ADSP_CAVS_2.5.md)
