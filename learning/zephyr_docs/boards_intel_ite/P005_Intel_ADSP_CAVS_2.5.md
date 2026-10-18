---
id: learning.zephyr-docs.boards-intel-ite.page-5
title: Intel ADSP CAVS 2.5
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_cavs25.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel-adsp-cavs-2-5"></a>

<a id="intel-adsp-cavs25"></a>

# 第5章\_Intel ADSP CAVS 2.5

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_cavs25.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此开发板配置用于在Intel CAVS 2.5音频DSP上运行Zephyr，Intel [Tiger Lake](https://www.intel.com/content/www/us/en/products/platforms/details/tiger-lake-h.html)等微处理器采用该配置。关于Intel ADSP ACE和CAVS，详见[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)。

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="xtensa-toolchain"></a>

### Xtensa工具链（Toolchain）

若选择Xtensa工具链而不使用Zephyr SDK，除了[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)中列出的Xtensa工具链环境变量，还需设置以下开发板专用环境变量。

```text
export TOOLCHAIN_VER=RG-2017.8-linux
export XTENSA_CORE=cavs2x_LX6HiFi3_2017_8
```

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

适用于所有CAVS及ACE平台的通用编程和调试说明见[Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md#intel-adsp-generic)。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [tiger-lake-h.html](https://www.intel.com/content/www/us/en/products/platforms/details/tiger-lake-h.html)：HTTP Error 403: Forbidden。

---

[上一章](P004_Intel_ADSP_ACE_1.5.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_Intel_ADSP_cAVS_and_ACE.md)
