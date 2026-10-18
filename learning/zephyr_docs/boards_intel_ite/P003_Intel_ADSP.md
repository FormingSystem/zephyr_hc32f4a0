---
id: learning.zephyr-docs.boards-intel-ite.page-3
title: Intel ADSP
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel-adsp"></a>

<a id="boards-intel-adsp"></a>

# 第3章\_Intel音频数字信号处理器（ADSP）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。


- [Intel ADSP cAVS与ACE](P006_Intel_ADSP_cAVS_and_ACE.md)
  - [系统要求（System Requirements）](P006_Intel_ADSP_cAVS_and_ACE.md#system-requirements)
    - [设置目标开发板（Target Board）](P006_Intel_ADSP_cAVS_and_ACE.md#setting-up-target-board)
    - [签名工具（Signing Tool）](P006_Intel_ADSP_cAVS_and_ACE.md#signing-tool)
    - [Xtensa工具链，可选（Optional）](P006_Intel_ADSP_cAVS_and_ACE.md#xtensa-toolchain-optional)
  - [烧录与调试（Programming and Debugging）](P006_Intel_ADSP_cAVS_and_ACE.md#programming-and-debugging)
    - [构建（Building）](P006_Intel_ADSP_cAVS_and_ACE.md#building)
    - [签名（Signing）](P006_Intel_ADSP_cAVS_and_ACE.md#signing)
    - [远程烧录基于cAVS的ADSP（Remote Flashing）](P006_Intel_ADSP_cAVS_and_ACE.md#remote-flashing-to-cavs-based-adsp)
    - [本地烧录基于cAVS的ADSP（Local Flashing）](P006_Intel_ADSP_cAVS_and_ACE.md#local-flashing-to-cavs-based-adsp)
    - [烧录基于ACE的ADSP](P006_Intel_ADSP_cAVS_and_ACE.md#flashing-to-ace-based-adsp)
    - [调试（Debugging）](P006_Intel_ADSP_cAVS_and_ACE.md#debugging)
  - [故障排查（Troubleshooting）](P006_Intel_ADSP_cAVS_and_ACE.md#troubleshooting)
- [在Chromebook上开发Zephyr音频DSP（Audio DSP Development）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md)
  - [TGL Chromebook初始设置（Initial Setup）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#initial-tgl-chromebook-setup)
    - [启用开发者模式（Developer Mode）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#enable-developer-mode)
    - [制作恢复盘（Recovery Drive）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#make-a-recovery-drive)
    - [使根文件系统可写（Writable Root Filesystem）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#make-the-root-filesystem-writable)
    - [启用ChromeOS SSH](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#enable-chromeos-ssh)
  - [安装Crouton](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#install-crouton)
  - [构建并安装定制内核（Custom Kernel）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#building-and-installing-a-custom-kernel)
    - [封装并安装ChromeOS内核镜像（Pack and Install）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#pack-and-install-chromeos-kernel-image)
    - [修复Wi-Fi固件（Firmware Fixup）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#wifi-firmware-fixup)
  - [构建并运行Zephyr应用（Build and Run）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#build-and-run-a-zephyr-application)
    - [构建rimage签名工具（Signing Tool）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#build-rimage-signing-tool)
    - [将集成脚本复制到Chromebook（Integration Scripting）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#copy-integration-scripting-to-chromebook)
    - [构建并签名Zephyr应用（Build and Sign）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#build-and-sign-zephyr-app)
    - [运行应用（Run It）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#run-it)
  - [其他参考资料（Misc References）](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md#misc-references)
- [Intel ADSP CAVS 2.5](P005_Intel_ADSP_CAVS_2.5.md)
  - [概述（Overview）](P005_Intel_ADSP_CAVS_2.5.md#overview)
  - [系统要求（System Requirements）](P005_Intel_ADSP_CAVS_2.5.md#system-requirements)
    - [Xtensa工具链（Toolchain）](P005_Intel_ADSP_CAVS_2.5.md#xtensa-toolchain)
  - [烧录与调试（Programming and Debugging）](P005_Intel_ADSP_CAVS_2.5.md#programming-and-debugging)
- [Intel ADSP ACE 1.5](P004_Intel_ADSP_ACE_1.5.md)
  - [概述（Overview）](P004_Intel_ADSP_ACE_1.5.md#overview)
  - [系统要求（System Requirements）](P004_Intel_ADSP_ACE_1.5.md#system-requirements)
    - [Xtensa工具链（Toolchain）](P004_Intel_ADSP_ACE_1.5.md#xtensa-toolchain)
  - [烧录与调试（Programming and Debugging）](P004_Intel_ADSP_ACE_1.5.md#programming-and-debugging)

---

[上一章](P002_Zephyr_Audio_DSP_Development_on_Chromebooks.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_Intel_ADSP_ACE_1.5.md)
