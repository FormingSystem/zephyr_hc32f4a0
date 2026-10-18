---
id: learning.zephyr-docs.tfm.page-3
title: TFM环境与硬件要求
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/services/tfm/requirements.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_TFM环境与硬件要求

原文：[官方页面](https://docs.zephyrproject.org/latest/services/tfm/requirements.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_开发板要求

以下是部分可与可信固件 M（Trusted Firmware-M，TF-M）配合使用的开发板。非安全处理环境（Non-Secure Processing Environment，NSPE）对应的板级目标名称如下。

| 开发板（Board） | NSPE 板级目标名称 |
| --- | --- |
| [ARM MPS2+ AN521](https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/mps2_an521.html#mps2-an521-board) | `mps2/an521/cpu0/ns`，支持 QEMU |
| [MPS3 FPGA/Corstone FVP](https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html#mps3) | `mps3/corstone300/fvp/ns`、`mps3/corstone310/fvp/ns`，支持 `armfvp` |
| [MPS4 Corstone FVP](https://docs.zephyrproject.org/latest/boards/arm/mps4/doc/index.html#mps4) | `mps4/corstone315/fvp/ns`、`mps4/corstone320/fvp/ns`，支持 `armfvp` |
| [BL5340 DVK](https://docs.zephyrproject.org/latest/boards/ezurio/bl5340_dvk/doc/index.html#bl5340_dvk) | `bl5340_dvk/nrf5340/cpuapp/ns` |
| [LPCXPRESSO55S69](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#lpcxpresso55s69) | `lpcxpresso55s69_ns` |
| [nrf9160dk_nrf9160](https://docs.zephyrproject.org/latest/boards/nordic/nrf9160dk/doc/index.html#nrf9160dk) | `nrf9160dk/nrf9160/ns` |
| [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk) | `nrf5340dk/nrf5340/cpuapp/ns` |
| [B-U585I-IOT02A Discovery kit](https://docs.zephyrproject.org/latest/boards/st/b_u585i_iot02a/doc/index.html#b_u585i_iot02a) | `b_u585i_iot02a/stm32u585xx/ns` |
| [Nucleo L552ZE Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.html#nucleo_l552ze_q) | `nucleo_l552ze_q/stm32l552xx/ns` |
| [STM32L562E-DK Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32l562e_dk/doc/index.html#stm32l562e_dk) | `stm32l562e_dk/stm32l562xx/ns` |
| [V2M Musca B1](https://docs.zephyrproject.org/latest/boards/arm/v2m_musca_b1/doc/index.html#v2m_musca_b1) | `v2m_musca_b1/musca_b1/ns` |

原文要求：要确认开发板输出支持 TF-M，应检查该板默认配置中的 [`CONFIG_TRUSTED_EXECUTION_NONSECURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRUSTED_EXECUTION_NONSECURE) 是否设为 `y`。

译注：表格保留原页目标名称，包括 `lpcxpresso55s69_ns` 这样的旧式名称；实际可用目标以所用源码版本的板级定义为准。非安全执行配置为 `y` 只是必要检查项，不能单独证明完整 TF-M 支持。核对时还需确认 TF-M 已移植到相应板／SoC、`CONFIG_TFM_BOARD` 非空，以及 `CONFIG_BUILD_WITH_TFM` 对 TrustZone-M 等条件的依赖，见[集成说明](P005_TFM与Zephyr集成.md)。

## 3.2\_软件要求（Software Requirements）

构建 TF-M 二进制文件所需的 Python 模块列在 TF-M 仓库的 `tools/requirements.txt` 中，可用以下命令安装。

```sh
$ pip3 install -r "$(west list trusted-firmware-m -f '{abspath}')/tools/requirements.txt"
```

这些模块供 TF-M 签名工具使用，将固件镜像准备成引导加载程序（Bootloader）可验证的形式。

译注：命令中的 `$(...)` 属于 Bash 等兼容终端的命令替换语法；`west list ... -f '{abspath}'` 从当前 west 工作区查询模块实际位置，没有写死作者机器目录。需先取得该工作区的 TF-M 模块，并使用准备好的 Python 环境；不能原样当作 PowerShell 命令。

为 QEMU 生成二进制文件，以及在某些平台上合并已签名的安全／非安全二进制文件，还需要 `srec_cat` 工具。

在 Linux 上，可通过以下命令安装：

```sh
$ sudo apt-get install srecord
```

在 OS X 上，可通过以下命令安装：

```sh
$ brew install srecord
```

Windows 系统需保证能从系统搜索路径（`PATH`）找到该工具，例如参见 [Windows 版 SRecord](https://sourceforge.net/projects/srecord/files/srecord-win32)。


译注核对来源：[modules/trusted-firmware-m/Kconfig.tfm](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm)。

本仓库的[对应源码](../../../modules/trusted-firmware-m/Kconfig.tfm)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="tf-m-requirements"></a>
<a id="software-requirements"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFM体系概述](P002_TFM体系概述.md) · [本模块主线目录](../reading/tfm.md) · [全部主线](../reading/README.md) · [下一篇：TFM构建系统](P004_TFM构建系统.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_TFM体系概述.md) · [返回大纲](大纲.md) · [下一章](P004_TFM构建系统.md)

</details>

<!-- reading-navigation:end -->
