---
id: learning.zephyr-docs.kconfig-reference.page-44
title: "`boards/espressif`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第44章\_`boards/espressif`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/espressif` 的 1 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESPRESSIF_QEMU"></a>

## 44.1 `CONFIG_ESPRESSIF_QEMU`

**提示（Prompt）**：乐鑫 QEMU 仿真支持（Espressif QEMU Emulation Support）

**说明（Help）**

生成合并后的 SPI 闪存镜像（Flash Image），并使用[乐鑫 QEMU 分支](https://github.com/espressif/qemu)启用 `west build -t run` 目标。对于 SoC 受支持的任意开发板，可通过 `-DCONFIG_ESPRESSIF_QEMU=y` 启用；也可以构建 DevKitC 的 `/qemu` 开发板变体，例如 `esp32c3_devkitc/esp32c3/qemu`，这类变体面向 Twister／持续集成（CI），并在 `defconfig` 中设置此选项。

要求 `PATH` 中能找到该 QEMU 分支提供的 `qemu-system-xtensa`（ESP32、ESP32-S3）或 `qemu-system-riscv32`（ESP32-C3、ESP32-C6）；也可以将 `ESPRESSIF_QEMU_PATH` 或 `QEMU_BIN_PATH` 设置为包含该可执行文件的目录。

对于简单启动（Simple Boot）构建，合并的是单个应用镜像。对于 MCUboot／sysbuild 构建，会将引导加载程序（Bootloader）和已签名应用（Signed Application）按各自的分区偏移合并到应用镜像中。MCUboot 镜像本身不启用仿真／闪存合并路径，因为 CMake 会跳过 `CONFIG_MCUBOOT` 构建。

对于 ESP32，运行目标（Run Target）提供 ECO3 eFuse 镜像，设置 `CHIP_VER_REV1` 和 `CHIP_VER_REV2`，使客户机（Guest）报告芯片修订版本 v3.0，而无需启用 `CONFIG_ESP32_USE_UNSUPPORTED_REVISION`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32C3 || CONFIG_SOC_SERIES_ESP32C6) && !CONFIG_SOC_ESP32_APPCPU && !CONFIG_SOC_ESP32S3_APPCPU && !CONFIG_SOC_ESP32C6_LPCORE
```

**主动选择（Selects）**

```text
CONFIG_ESPRESSIF_QEMU_TARGET
CONFIG_BUILD_OUTPUT_BIN
```

**定义位置（Location）**：[`boards/espressif/common/Kconfig.qemu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/espressif/common/Kconfig.qemu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_ESP32_APPCPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_APPCPU)、[`CONFIG_SOC_ESP32S3_APPCPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32S3_APPCPU)、[`CONFIG_SOC_ESP32C6_LPCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32C6_LPCORE)、[`CONFIG_ESPRESSIF_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_ESPRESSIF_QEMU_TARGET)、[`CONFIG_BUILD_OUTPUT_BIN`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_BIN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C6`。

<!-- kconfig-navigation -->

[上一章](P043_boards_Kconfig.whisper_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P045_boards_lilygo_配置项参考.md)
