---
id: learning.board.labs.hc32-port.readme
title: HC32F4A0 板级与 SoC 适配模块
kind: reference
status: maintained
domains: [documentation]
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# HC32F4A0 板级与 SoC 适配模块

配套正文是[新增开发板](../../../P01_zephyr_make_project/P011_编译示例与新增开发板_Windows.md)。将 learning 材料放到实验源码根后，本目录位于 `G:\zephyr_practice\zephyr-main\learning\board\labs\hc32_port`。它是本章提供、需要显式接入的移植模块，官方原生源码没有这块板。

模块包含 UYUP-RPI-A-2.5 / HC32F4A0PITB 的板定义、SoC 启动、设备树、GPIO 与轮询 UART 实现。`zephyr/module.yml` 将本目录登记为板、SoC 和设备树搜索根；根 CMake/Kconfig 接入驱动。厂商 HAL 和 CMSIS 另按正文取得，不包含在此模块中。

依赖选择的入口是[型号与依赖依据](../../../P01_zephyr_make_project/环境与依赖导航.md#chip-selection)，完整下载命令在配套 P005 的 5.2.2 和 5.2.3 节：

| 输入 | 依据与来源 | 核验位置 |
| --- | --- | --- |
| HC32F4A0PITB / LQFP100 | 实装丝印、BOM 与[厂商数据手册](https://www.xhsc.com.cn/product/1220.html) | 本模块 board.yml、SoC Kconfig、DTS 与实际板卡一致 |
| CMSIS_6 | 当前实验 Zephyr 的架构接入与 west.yml；不固定为其他工程的版本 | 模块入口、CMSIS/Core/Include/core_cm4.h、构建 include 路径 |
| hal_xhsc | [固定提交 ZIP](https://github.com/zephyrproject-rtos/hal_xhsc/archive/a84e04900616f68097d80cda2e89eaa8af3afadd.zip)，修订 a84e04900616f68097d80cda2e89eaa8af3afadd | zephyr/module.yml、hc32_ddl/hc32f4a0/soc 和 drivers；对应本模块 SoC CMakeLists 引用 |

HAL 修订是本移植的 API 基线，不是由芯片型号自动推导；2026-10-05 核对的原生 Zephyr 清单没有 hal_xhsc，不能直接 west update 此项目。HAL 包提供芯片设备头和 DDL，CMSIS_6 提供 Core 头，SDK 提供编译器，三者用途不同。下载包完整不等于本次构建已使用它，须反查模块列表、.config 与 compile_commands.json。更新依赖后重新检查兼容性并分别记录构建和实板结果。

首版使用实装 12 MHz 晶振直接作为系统时钟，未启用 PLL；主 SRAM 为 `0x1ffe0000` 起的 512 KiB，Flash 为 2 MiB。UART 仅支持 USART1 PA9/PA10 轮询；GPIO 保留封装未引出引脚的限制。本章先完成构建验收，`board.cmake` 不配置烧录器。不得将 AN386 的固件烧入此板，也不得由 ELF 成功推断硬件工作正常。

完整 `.c`、`.S`、`.dtsi` 材料用于逐项阅读和复现已有适配。P011 11.6 在 `build/learning-tools/p003/hc32_port` 新建工作模块，按身份、设备树与板卡、启动与 HAL、驱动、完整性检查五个阶段逐组加入文件，正文说明各层如何接入，不把改板名等同于从零实现芯片驱动。后续若将支持移入源码根对应目录，须同时撤下本模块的重复定义，不能两套注册一起启用。

目录按当前 Zephyr 硬件模型组织：`boards/uyup/uyup_rpi_a` 的 uyup 表示板厂，`soc/xhsc/hc32f4a0` 的 xhsc 表示芯片厂商；Arm/Cortex-M 共用实现来自 Zephyr 的 `arch/arm`。厂商名不代表独立架构，目录不按 `arm/cortex-m4/xhsc/uyup` 逐层嵌套。设计原因、异构硬件例子与配置关系见 [P011 11.5 目录说明](../../../P01_zephyr_make_project/P011_编译示例与新增开发板_Windows.md#board-layout)。

正式登记使用模块名 `hc32_port`。随附 `dts/bindings/vendor-prefixes.txt` 使原生源码能够识别 uyup 与 xhsc；`board.yml`、`soc.yml`、`Kconfig.soc` 保持同一硬件身份，板平台 YAML 只登记已经实现的能力。SoC Kconfig 描述内核与硬件能力，HEX 输出放在板级 defconfig 中作为默认选项。SoC CMake 从原生 `ZEPHYR_HAL_XHSC_MODULE_DIR` 取得 HAL，缺失匹配设备头时明确报错。详细文件职责与检查步骤见 [P011 11.6 分阶段接入](../../../P01_zephyr_make_project/P011_编译示例与新增开发板_Windows.md#section-11-6)。

迁入源码树时按排序合并厂商前缀，不覆盖官方完整表；同步接入驱动 CMake/Kconfig，并撤掉同名模块注册。遵循官方格式不等于上游已经收录，编译结果与实板能力分别记录。

## 实验阶段边界

本模块保留 12 MHz 晶振直驱、GPIO 与轮询 UART 的入门移植阶段。后续完整工程增加的 48 MHz PLLH、USBFS CDC ACM 和 HWINFO 不包含在此快照；不能仅凭板名相同就认为两者外设能力一致。板名、芯片型号和存储布局仍须一致，`supported` 按各阶段真实驱动分别登记。
