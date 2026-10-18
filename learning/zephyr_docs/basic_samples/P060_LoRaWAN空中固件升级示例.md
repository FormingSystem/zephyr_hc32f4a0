---
id: learning.zephyr-docs.basic_samples.page-60
title: LoRaWAN空中固件升级示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/lorawan/fuota/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lorawan-fuota"></a>

# 第60章\_LoRaWAN空中固件升级示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/lorawan/fuota/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/lorawan/fuota/README.rst/..)。

<a id="overview"></a>

## 60.1 概述（Overview）

本应用展示如何通过LoRaWAN进行空中固件升级（Firmware Upgrade Over the Air，FUOTA）。它使用LoRa联盟（LoRa Alliance）规定的以下服务：

- 应用层时钟同步（Application Layer Clock Synchronization）：[TS003-2.0.0](https://resources.lora-alliance.org/technical-specifications/ts003-2-0-0-application-layer-clock-synchronization)。
- 远程组播设置（Remote Multicast Setup）：[TS005-1.0.0](https://resources.lora-alliance.org/technical-specifications/lorawan-remote-multicast-setup-specification-v1-0-0)。
- 分片数据块传输（Fragmented Data Block Transport）：[TS004-1.0.0](https://resources.lora-alliance.org/technical-specifications/lorawan-fragmented-data-block-transport-specification-v1-0-0)。

FUOTA流程由应用启动，随后在自己的工作队列线程（Work Queue Thread）中后台运行。成功接收固件升级后，应用通过回调（Callback）得到通知，并可以重启设备进入MCUboot以应用升级。

本示例需要实现相关服务的LoRaWAN应用服务器（Application Server）才能工作。

> 译注——完成回调的实际动作：当前`fuota_finished()`只打印“重置设备以应用固件升级”的提示，并没有调用重启接口。主应用启动时钟同步和分片传输服务，远程组播服务在后台安排C类（Class C）会话；应用每180秒发送一次普通上行，为A类（Class A）会话中的服务器配置下行提供接收机会。接收到固件、收到完成通知和重启应用升级是不同阶段。

<a id="building-and-running"></a>

## 60.2 构建与运行（Building and Running）

构建示例之前，务必在`prj.conf`中选择正确的区域（Region）。以下命令构建并烧录示例：

```sh
west build -b nucleo_wl55jc samples/subsys/lorawan/fuota
west flash
```

> 译注——MCUboot构建边界：当前示例的`sysbuild.conf`设置`SB_CONFIG_BOOTLOADER_MCUBOOT=y`，该配置由Sysbuild多映像构建读取；原命令没有`--sysbuild`，不能仅凭这两行就认定已经同时构建和烧录MCUboot。如果板上尚未准备兼容的MCUboot及分区布局，应按Sysbuild方式构建，并核对映像、签名和升级槽配置。下面是据当前示例配置给出的独立构建目录写法，未修改上方原命令。

> 译注——执行前提：在已准备Zephyr开发依赖、目标工具链及烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。先准备匹配的LoRaWAN应用服务器、设备身份和密钥、区域及闪存分区。构建成功后才烧录；入网失败先检查网络配置，接收完成后还需按引导配置验证实际升级结果。当前示例的设备标识及密钥为占位值，本文没有执行入网、下载固件或升级。

```sh
west build --sysbuild -d build/lorawan-fuota -b nucleo_wl55jc samples/subsys/lorawan/fuota
west flash -d build/lorawan-fuota
```

> 译注——测试与存储条件：当前测试只允许`nucleo_wl55jc`，并检查主／次级映像槽及闪存驱动条件；其控制台通过条件仍只是开始尝试OTAA入网的日志。配置已启用Settings持久化及分片传输，但这些配置本身不证明网络加入、固件接收、签名校验或升级启动已经通过。

<a id="see-also"></a>

## 60.3 另请参阅（See also）

- [LoRaWAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html)。


> 译注——实现依据：[samples/subsys/lorawan/fuota/prj.conf](../../../samples/subsys/lorawan/fuota/prj.conf)、[samples/subsys/lorawan/fuota/tests.yaml](../../../samples/subsys/lorawan/fuota/tests.yaml)、[samples/subsys/lorawan/fuota/sysbuild.conf](../../../samples/subsys/lorawan/fuota/sysbuild.conf)、[samples/subsys/lorawan/fuota/sysbuild/mcuboot.conf](../../../samples/subsys/lorawan/fuota/sysbuild/mcuboot.conf)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/lorawan/fuota/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/lorawan/fuota/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/lorawan/fuota/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/lorawan/fuota/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P059_LoRaWANA类设备示例.md) · [返回大纲](大纲.md) · [下一章](P061_ArmSiP服务示例.md)
