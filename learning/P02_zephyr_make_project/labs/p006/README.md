---
id: zephyr-p006-lab-files
title: P006 普通组件与应用源码原件
kind: reference
status: evolving
---

# 普通组件怎样随应用配置进入固件

固定 `mps2/an386` 和同一套编译工具，只改变问候组件的配置。预期两次构建都发现模块：开启时编入 `greeting.c`，关闭时应用改走备用输出。目录名 `p006` 是材料标识，完整实验在 [P013](../../P013_自定义源码模块与配置开关.md#section-13-1)。

1. 完成 [MPS2 基线构建](../../reference/MPS2串口构建与驱动源码实验.md#section-10-3-3)，确认这套工具可以构建官方应用。
2. 按[文件布局与创建步骤](../../P013_自定义源码模块与配置开关.md#section-13-1-1)准备[组件声明](components/app_greeting/zephyr/module.yml)、[选源规则](components/app_greeting/CMakeLists.txt)和[应用](applications/component_hello/src/main.c)。目录内共九个原件。[创建组件命令](../../commands/current/P013_自定义源码模块与配置开关/complete/create-greeting-component.txt) · [创建应用命令](../../commands/current/P013_自定义源码模块与配置开关/complete/create-component-application.txt)
3. 先[构建开启版](../../P013_自定义源码模块与配置开关.md#section-13-1-7)，再按[关闭对照](../../P013_自定义源码模块与配置开关.md#section-13-1-10)传入 [off.conf](applications/component_hello/off.conf)，分别保留输出目录。
4. 对照两份 `zephyr/.config` 与 `compile_commands.json`。若两边均编入 `greeting.c`，先查关闭版是否确实读到了 `off.conf`。有 QEMU 时可进一步比较两次串口输出。

配套 9 个文件曾与实验副本逐字节核对，启用/关闭构建和 QEMU 输出的历史验证范围见 [P013 13.1.12](../../P013_自定义源码模块与配置开关.md#section-13-1-12)。复现时仍需核对自己使用的源码、工具与生成结果。
