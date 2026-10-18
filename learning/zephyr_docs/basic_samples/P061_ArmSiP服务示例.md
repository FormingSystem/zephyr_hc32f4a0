---
id: learning.zephyr-docs.basic_samples.page-61
title: ArmSiP服务示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/sip_svc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sip_svc"></a>

# 第61章\_ArmSiP服务示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/sip_svc/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/sip_svc/README.rst/..)。

<a id="overview"></a>

## 61.1 概述（Overview）

本示例展示SiP SVC子系统的用法，通过它从Intel Agilex片上系统现场可编程门阵列（SoC FPGA）的安全设备管理器（Secure Device Manager，SDM）查询电压值。

<a id="caveats"></a>

## 61.2 注意事项（Caveats）

- SiP SVC子系统要求运行在异常级别3（Exception Level 3，EL3）的固件，与工程使用的SiP SVC子系统内部定义的协议兼容。
- 示例依赖Intel Agilex SoC FPGA中的Arm可信固件（Trusted Firmware Arm），通过它查询安全设备管理器中的电压水平。

<a id="building-and-running"></a>

## 61.3 构建与运行（Building and Running）

构建应用：

> 译注——执行前提：在已准备Zephyr开发依赖及目标工具链的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行下方构建命令。构建成功只说明获得映像，运行还依赖该平台的可信固件、启动介质及加载布局。若构建失败先检查目标和配置；若服务访问失败，应核对EL3固件与协议兼容性。本文没有操作启动介质或加载硬件映像。

```sh
# From the root of the zephyr repository
west build -b intel_socfpga_agilex_socdk samples/subsys/sip_svc
```

运行时，可由ATF BL2从SD卡或QSPI闪存将Zephyr映像加载到DDR内存地址`0x00100000`，并将ATF BL31加载到`0x00001000`。

> 译注——地址与启动阶段：ATF是原文对Arm可信固件的称呼，也常称Trusted Firmware-A（TF-A）；BL2、BL31为对应启动阶段。这里保留的十六进制数是原示例的目标内存加载地址，不是本机文件路径，也不能直接推广为其他SoC的加载布局。

> 译注——当前源码的断言问题：`sip_svc_send()`成功时返回事务编号、失败时返回负错误码，`k_sem_take()`成功时返回0。当前示例却分别写成`__ASSERT(trans_id < 0, ...)`和`__ASSERT(err != 0, ...)`，其条件与上述成功语义相反；在断言启用时，正常成功路径也可能触发断言。下面的官方旧日志不能证明当前代码在任意断言配置下已经运行通过。这里只记录源码核对结果，未修改上游实现。

<a id="sample-output"></a>

## 61.4 示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v3.3.0-2963-gb5ba49ae300e ***
Got response of transaction id 0x00 and voltage is 0.846878v
Got response of transaction id 0x01 and voltage is 0.858170v
Got response of transaction id 0x02 and voltage is 0.860168v
Got response of transaction id 0x03 and voltage is 0.846832v
Got response of transaction id 0x04 and voltage is 0.858337v
Got response of transaction id 0x05 and voltage is 0.871704v
Got response of transaction id 0x06 and voltage is 0.859421v
Got response of transaction id 0x07 and voltage is 0.857254v
Got response of transaction id 0x08 and voltage is 0.858429v
Got response of transaction id 0x09 and voltage is 0.859879v
Got response of transaction id 0x0a and voltage is 0.845139v
Got response of transaction id 0x0b and voltage is 0.858459v
Got response of transaction id 0x0c and voltage is 0.859283v
Got response of transaction id 0x0d and voltage is 0.846207v
Got response of transaction id 0x0e and voltage is 0.855850v
Got response of transaction id 0x0f and voltage is 0.859283v
Got response of transaction id 0x00 and voltage is 0.846832v
Got response of transaction id 0x01 and voltage is 0.856049v
Got response of transaction id 0x02 and voltage is 0.859879v
```

> 译注——数值含义：当前源码将收到的电压定点值除以65536转换为浮点电压，并在两次请求之间休眠1000毫秒。上述事务编号和电压均来自官方示例日志，不是对当前板卡的实测值。


> 译注——实现依据：[samples/subsys/sip_svc/tests.yaml](../../../samples/subsys/sip_svc/tests.yaml)、[include/zephyr/sip_svc/sip_svc.h](../../../include/zephyr/sip_svc/sip_svc.h)、[include/zephyr/kernel.h](../../../include/zephyr/kernel.h)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/sip_svc/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/sip_svc/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/sip_svc/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/sip_svc/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P060_LoRaWAN空中固件升级示例.md) · [返回大纲](大纲.md) · [下一章](P062_示例定义与准则.md)
